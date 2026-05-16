#!/usr/bin/env python3
"""Validate that active issue routes do not target closed GitHub issues."""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

ACTIVE_UPDATE_ACTIONS = {"update-existing-issue", "reuse-existing-issue"}


def load_routes(path: Path) -> dict[str, dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    routes = data.get("routes", data)
    if not isinstance(routes, dict):
        raise ValueError(f"{path}: routes must be an object")
    normalized: dict[str, dict[str, Any]] = {}
    for key, value in routes.items():
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{key} route must be an object")
        if "issue" not in value:
            raise ValueError(f"{path}:{key} route missing issue")
        if "action" not in value:
            raise ValueError(f"{path}:{key} route missing action")
        normalized[str(key)] = value
    return normalized


def _gh_issue_state(issue: int) -> str:
    result = subprocess.run(
        ["gh", "issue", "view", str(issue), "--json", "state", "--jq", ".state"],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.stdout.strip().upper()


def validate_routes(path: Path, issue_states: dict[int, str] | None = None) -> list[str]:
    routes = load_routes(path)
    failures: list[str] = []
    state_cache: dict[int, str] = {int(issue): state.upper() for issue, state in (issue_states or {}).items()}
    for key, route in routes.items():
        action = str(route.get("action", "comment-on-roadmap"))
        issue = int(route.get("issue", 13))
        if action not in ACTIVE_UPDATE_ACTIONS:
            continue
        state = state_cache.get(issue)
        if state is None:
            state = _gh_issue_state(issue)
            state_cache[issue] = state
        if state == "CLOSED":
            failures.append(f"{path}:{key} targets closed issue #{issue} with active action {action}")
    return failures


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("route_maps", nargs="+", type=Path, help="Route-map JSON files to validate")
    parser.add_argument("--state-json", type=Path, help="Optional fixture mapping of issue number to OPEN/CLOSED state")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    issue_states = None
    if args.state_json:
        issue_states = {int(key): str(value) for key, value in json.loads(args.state_json.read_text(encoding="utf-8")).items()}
    failures: list[str] = []
    for path in args.route_maps:
        try:
            failures.extend(validate_routes(path, issue_states))
        except ValueError as exc:
            failures.append(str(exc))
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("Issue route state validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
