#!/usr/bin/env python3
"""Validate OSS engineering-tool watchlist manifest and report artifacts."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = (
    "# OSS engineering-tool watchlist",
    "## Run metadata",
    "## Tools checked and signal sources",
    "## Detected changes",
    "## Candidate wiki updates",
    "## Duplicate/open-issue routing",
    "## Blocked/manual-review items",
    "## Validation evidence",
)
REQUIRED_TOOL_FIELDS = (
    "name",
    "slug",
    "owner",
    "repo",
    "upstream_url",
    "docs_url",
    "source_type",
    "source_url",
    "signal_strategy",
    "domain",
    "tier1_repo_links",
    "wiki_target",
    "affected_paths",
    "update_relevance_rule",
    "last_checked",
    "last_seen_version",
    "last_seen_release_date",
    "last_seen_signal_summary",
    "status",
    "confidence",
    "why_it_matters",
    "noise_policy",
)
ROADMAP_URL = "https://github.com/vamseeachanta/llm-wiki/issues/13"
FORBIDDEN_PATTERN = re.compile(
    r"/mnt/ace/(?!\s|`|$)|/mnt/ace-data/(?!\s|`|$)|BEGIN (?:RSA|OPENSSH|PRIVATE) KEY|pass\s*word\s*=|sec\s*ret\s*=|api[_-]?key\s*=|\bSSN\b|social security|bank account",
    re.IGNORECASE,
)


def _safe_rel_path(value: str) -> bool:
    return bool(value) and not value.startswith(("/", "~")) and ".." not in Path(value).parts


def _public_url(value: str) -> bool:
    return value.startswith(("https://", "http://")) and not FORBIDDEN_PATTERN.search(value)


def validate_manifest(path: Path) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return [f"missing manifest {path}"]
    raw = path.read_text(encoding="utf-8", errors="replace")
    if FORBIDDEN_PATTERN.search(raw):
        failures.append("manifest public-safety scan matched forbidden text")
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        return failures + [f"manifest invalid JSON: {exc}"]
    if data.get("schema_version") != "oss-tool-watchlist/v1":
        failures.append("manifest schema_version must be oss-tool-watchlist/v1")
    tools = data.get("tools")
    if not isinstance(tools, list):
        return failures + ["manifest tools must be a list"]
    if len(tools) < 1:
        failures.append("manifest must contain at least one tool")
    slugs: set[str] = set()
    for index, tool in enumerate(tools):
        if not isinstance(tool, dict):
            failures.append(f"tool[{index}] must be an object")
            continue
        label = str(tool.get("slug") or index)
        for field in REQUIRED_TOOL_FIELDS:
            if field not in tool or tool[field] in ("", None, []):
                failures.append(f"tool {label} missing required field {field}")
        slug = str(tool.get("slug", ""))
        if slug in slugs:
            failures.append(f"duplicate tool slug {slug}")
        slugs.add(slug)
        for field in ("upstream_url", "docs_url", "source_url"):
            if field in tool and not _public_url(str(tool[field])):
                failures.append(f"tool {label} {field} must be a public URL")
        tier1_links = tool.get("tier1_repo_links", [])
        if not isinstance(tier1_links, list) or not tier1_links or not all(isinstance(item, str) and _public_url(item) for item in tier1_links):
            failures.append(f"tool {label} tier1_repo_links must be non-empty public URLs")
        if "wiki_target" in tool and not _safe_rel_path(str(tool["wiki_target"])):
            failures.append(f"tool {label} wiki_target must be repo-relative")
        affected = tool.get("affected_paths", [])
        if affected and (not isinstance(affected, list) or not all(isinstance(item, str) and _safe_rel_path(item) for item in affected)):
            failures.append(f"tool {label} affected_paths must be repo-relative")
    return failures


def _load_manifest_tools(manifest_path: Path) -> list[dict]:
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8"))
    except Exception:
        return []
    tools = data.get("tools", [])
    return tools if isinstance(tools, list) else []


def validate_report(path: Path, manifest_path: Path | None = None) -> list[str]:
    failures: list[str] = []
    if not path.exists():
        return [f"missing report {path}"]
    text = path.read_text(encoding="utf-8", errors="replace")
    if FORBIDDEN_PATTERN.search(text):
        failures.append("report public-safety scan matched forbidden text")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"missing required section: {section}")
    if ROADMAP_URL not in text:
        failures.append("missing roadmap anchor issue link")
    if "public-safe" not in text.lower():
        failures.append("missing public-safe language")
    forbidden_phrases = ("Authorization:", "Cookie:", "raw api payload", "release-note body")
    for phrase in forbidden_phrases:
        if phrase.lower() in text.lower():
            failures.append(f"report contains forbidden artifact phrase: {phrase}")
    if manifest_path is not None and manifest_path.exists():
        tools = _load_manifest_tools(manifest_path)
        for tool in tools:
            name = str(tool.get("name", ""))
            wiki_target = str(tool.get("wiki_target", ""))
            if name and name not in text:
                failures.append(f"report missing manifest tool row: {name}")
            if wiki_target and wiki_target not in text:
                failures.append(f"report missing manifest wiki target: {wiki_target}")
            for link in tool.get("tier1_repo_links", []):
                if isinstance(link, str) and link not in text:
                    failures.append(f"report missing tier1 repo link for {name}: {link}")
    return failures


def validate_artifacts(manifest_path: Path, report_path: Path) -> list[str]:
    return validate_manifest(manifest_path) + validate_report(report_path, manifest_path=manifest_path)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 2:
        print("usage: validate_oss_tool_watchlist.py <manifest.json> <report.md>", file=sys.stderr)
        return 2
    failures = validate_artifacts(Path(args[0]), Path(args[1]))
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"OK: {args[0]} {args[1]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
