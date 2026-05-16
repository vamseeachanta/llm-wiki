#!/usr/bin/env python3
"""Generate the public-safe OSS engineering-tool watchlist report.

The v1 implementation is fixture/offline-first. It reads a static checked-in
watchlist, optional fixture observations, optional prior state, and a checked-in
issue-routing map. It writes a human report plus normalized state; it never
persists raw upstream API payloads.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any

SCHEMA_VERSION = "oss-tool-watchlist-report/v1"
STATE_SCHEMA_VERSION = "oss-tool-watchlist-state/v1"
WATCHLIST_SCHEMA_VERSION = "oss-tool-watchlist/v1"
ISSUE_MAP_SCHEMA_VERSION = "oss-tool-issue-map/v1"
WATCHLIST_PATH = Path("data/oss_tool_watchlist.json")
ISSUE_MAP_PATH = Path("data/oss_tool_issue_map.json")
REPORT_DIR = Path("docs/reports")
STATE_DIR = Path("artifacts/watchlist")
ROADMAP_URL = "https://github.com/vamseeachanta/llm-wiki/issues/13"
PUBLIC_SAFETY_NOTE = "public-safe metadata-only report; no raw/private/vendor/client content."

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
ALLOWED_URL_PREFIXES = ("https://", "http://")
FORBIDDEN_PATTERN = re.compile(
    r"/mnt/ace/(?!\s|`|$)|/mnt/ace-data/(?!\s|`|$)|BEGIN (?:RSA|OPENSSH|PRIVATE) KEY|pass\s*word\s*=|sec\s*ret\s*=|api[_-]?key\s*=|\bSSN\b|social security|bank account",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class WatchlistRow:
    name: str
    slug: str
    domain: str
    signal_strategy: str
    source_url: str
    docs_url: str
    wiki_target: str
    tier1_repo_links: list[str]
    affected_paths: list[str]
    signal_type: str
    observed_value: str
    previous_value: str
    observed_release_date: str
    previous_release_date: str
    observed_at: str
    observed_docs_marker: str
    confidence: str
    why_it_matters: str
    signal_summary: str
    recommendation_action: str
    recommendation_rationale: str
    route_action: str
    route_issue: int
    route_title: str
    route_reason: str


@dataclass(frozen=True)
class WatchlistReport:
    schema_version: str
    run_date: str
    totals: dict[str, int]
    rows: list[WatchlistRow]
    validation: dict[str, str]
    public_safety_note: str = PUBLIC_SAFETY_NOTE


def read_json(path: Path, fallback: Any | None = None) -> Any:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def load_watchlist(path: Path) -> dict[str, Any]:
    data = read_json(path, {"schema_version": WATCHLIST_SCHEMA_VERSION, "tools": []})
    if not isinstance(data, dict):
        raise ValueError("watchlist must be a JSON object")
    data.setdefault("tools", [])
    return data


def _safe_rel_path(value: str) -> bool:
    return bool(value) and not value.startswith(("/", "~")) and ".." not in Path(value).parts


def _public_url(value: str) -> bool:
    return value.startswith(ALLOWED_URL_PREFIXES) and not FORBIDDEN_PATTERN.search(value)


def validate_watchlist(data: dict[str, Any], repo_root: Path | None = None) -> list[str]:
    failures: list[str] = []
    raw = json.dumps(data, sort_keys=True)
    if FORBIDDEN_PATTERN.search(raw):
        failures.append("watchlist public-safety scan matched forbidden text")
    if data.get("schema_version") != WATCHLIST_SCHEMA_VERSION:
        failures.append(f"watchlist schema_version must be {WATCHLIST_SCHEMA_VERSION}")
    tools = data.get("tools")
    if not isinstance(tools, list):
        return failures + ["watchlist tools must be a list"]
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
        wiki_target = str(tool.get("wiki_target", ""))
        if wiki_target and not _safe_rel_path(wiki_target):
            failures.append(f"tool {label} wiki_target must be a safe repo-relative path")
        affected = tool.get("affected_paths", [])
        if not isinstance(affected, list) or not all(isinstance(item, str) and _safe_rel_path(item) for item in affected):
            failures.append(f"tool {label} affected_paths must be safe repo-relative paths")
    return failures


def load_issue_map(path: Path) -> dict[str, Any]:
    data = read_json(path, {"schema_version": ISSUE_MAP_SCHEMA_VERSION, "routes": {}})
    if not isinstance(data, dict):
        return {"schema_version": ISSUE_MAP_SCHEMA_VERSION, "routes": {}}
    data.setdefault("routes", {})
    return data


def _load_fixture(fixtures_dir: Path | None, slug: str) -> dict[str, Any] | None:
    if fixtures_dir is None:
        return None
    path = fixtures_dir / f"{slug}.json"
    data = read_json(path, None)
    return data if isinstance(data, dict) else None


def _previous_for_tool(tool: dict[str, Any], previous_state: dict[str, Any] | None = None) -> dict[str, Any]:
    slug = str(tool.get("slug", ""))
    if previous_state:
        rows = previous_state.get("rows", [])
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict) and row.get("slug") == slug:
                    return {
                        "observed_value": row.get("observed_value", ""),
                        "observed_release_date": row.get("observed_release_date", ""),
                        "observed_docs_marker": row.get("observed_docs_marker", ""),
                    }
    return {
        "observed_value": tool.get("last_seen_version", ""),
        "observed_release_date": tool.get("last_seen_release_date", ""),
        "observed_docs_marker": tool.get("last_seen_docs_marker", ""),
    }


def normalize_signal(tool: dict[str, Any], observed: dict[str, Any] | None, previous: dict[str, Any] | None, repo_root: Path, observed_at: str) -> WatchlistRow:
    observed = observed or {}
    previous = previous or {}
    slug = str(tool["slug"])
    observed_value = str(observed.get("observed_value", tool.get("last_seen_version", "")))
    previous_value = str(previous.get("observed_value", tool.get("last_seen_version", "")))
    observed_release_date = str(observed.get("observed_release_date", tool.get("last_seen_release_date", "")))
    previous_release_date = str(previous.get("observed_release_date", tool.get("last_seen_release_date", "")))
    observed_docs_marker = str(observed.get("observed_docs_marker", ""))
    previous_docs_marker = str(previous.get("observed_docs_marker", ""))
    wiki_exists = (repo_root / str(tool["wiki_target"])).exists()

    if observed.get("error"):
        signal_type = "signal_unavailable"
    elif observed_value and previous_value and observed_value != previous_value:
        signal_type = "new_release"
    elif observed_docs_marker and previous_docs_marker and observed_docs_marker != previous_docs_marker:
        signal_type = "docs_changed"
    elif not wiki_exists:
        signal_type = "candidate_page_missing"
    else:
        signal_type = "no_change"

    if signal_type == "new_release" and not wiki_exists:
        action = "create_initial_seed_page"
        rationale = "Public release changed and wiki target is missing."
    elif signal_type == "candidate_page_missing":
        action = "create_initial_seed_page"
        rationale = "Tool is watchlisted but the candidate wiki target does not exist."
    elif signal_type in {"new_release", "docs_changed"}:
        action = "update_existing_wiki_page"
        rationale = "Public upstream signal changed; review the affected wiki paths."
    elif signal_type == "signal_unavailable":
        action = "manual_review"
        rationale = "Public signal was unavailable; do not invent update details."
    else:
        action = "no_action"
        rationale = "No actionable public signal change detected."

    return WatchlistRow(
        name=str(tool["name"]),
        slug=slug,
        domain=str(tool["domain"]),
        signal_strategy=str(tool["signal_strategy"]),
        source_url=str(tool["source_url"]),
        docs_url=str(tool["docs_url"]),
        wiki_target=str(tool["wiki_target"]),
        tier1_repo_links=list(tool.get("tier1_repo_links", [])),
        affected_paths=list(tool.get("affected_paths", [])),
        signal_type=signal_type,
        observed_value=observed_value,
        previous_value=previous_value,
        observed_release_date=observed_release_date,
        previous_release_date=previous_release_date,
        observed_at=observed_at,
        observed_docs_marker=observed_docs_marker,
        confidence=str(observed.get("confidence", tool.get("confidence", "medium"))),
        why_it_matters=str(tool.get("why_it_matters", "Public OSS tool coverage supports code-development retrieval.")),
        signal_summary=str(observed.get("signal_summary", tool.get("last_seen_signal_summary", "No public signal summary."))),
        recommendation_action=action,
        recommendation_rationale=rationale,
        route_action="comment-on-roadmap",
        route_issue=13,
        route_title="Roadmap anchor",
        route_reason="default route; issue map not applied",
    )


def _apply_route(row: WatchlistRow, issue_map: dict[str, Any]) -> WatchlistRow:
    routes = issue_map.get("routes", {}) if isinstance(issue_map.get("routes", {}), dict) else {}
    route = routes.get(row.slug) or routes.get(row.signal_type) or routes.get(row.recommendation_action) or routes.get("default") or {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"}
    route_reason = str(route.get("reason", "Watchlist recommendation is deduplicated through the checked-in issue map."))
    return WatchlistRow(**{**asdict(row), "route_action": str(route.get("action", "comment-on-roadmap")), "route_issue": int(route.get("issue", 13)), "route_title": str(route.get("title", "Roadmap anchor")), "route_reason": route_reason})


def scan_watchlist(repo_root: Path, watchlist_path: Path, issue_map_path: Path, fixtures_dir: Path | None = None, run_date: str | None = None, previous_state_path: Path | None = None) -> WatchlistReport:
    repo_root = repo_root.resolve()
    run_date = run_date or date.today().isoformat()
    watchlist = load_watchlist(watchlist_path)
    failures = validate_watchlist(watchlist, repo_root=repo_root)
    if failures:
        raise ValueError("invalid watchlist: " + "; ".join(failures))
    issue_map = load_issue_map(issue_map_path)
    previous_state = read_json(previous_state_path, None) if previous_state_path else None
    rows: list[WatchlistRow] = []
    for tool in watchlist["tools"]:
        observed = _load_fixture(fixtures_dir, str(tool["slug"]))
        if observed is None:
            observed = {
                "observed_value": tool.get("last_seen_version", ""),
                "observed_release_date": tool.get("last_seen_release_date", ""),
                "signal_summary": "Offline baseline check; enable fixture/live enrichment for upstream deltas.",
                "observed_docs_marker": tool.get("last_seen_docs_marker", ""),
            }
        row = normalize_signal(tool, observed, _previous_for_tool(tool, previous_state), repo_root=repo_root, observed_at=run_date)
        rows.append(_apply_route(row, issue_map))
    totals = {"tools_checked": len(rows)}
    for signal in ("new_release", "docs_changed", "candidate_page_missing", "signal_unavailable", "manual_review", "no_change"):
        totals[signal] = sum(1 for row in rows if row.signal_type == signal)
    validation = {
        "tests": "uv run pytest tests/test_oss_tool_watchlist.py tests/test_oss_tool_watchlist_artifacts.py -q",
        "generate": f"uv run python scripts/llm_wiki_oss_tool_watchlist.py --date {run_date} --write",
        "validator": f"uv run python scripts/validate_oss_tool_watchlist.py data/oss_tool_watchlist.json docs/reports/{run_date}-oss-engineering-tool-watchlist.md",
    }
    return WatchlistReport(schema_version=SCHEMA_VERSION, run_date=run_date, totals=totals, rows=rows, validation=validation)


def issue_link(issue: int) -> str:
    return f"https://github.com/vamseeachanta/llm-wiki/issues/{issue}"


def _fmt_paths(paths: list[str]) -> str:
    return ", ".join(f"`{path}`" for path in paths) if paths else "n/a"


def render_report(report: WatchlistReport) -> str:
    lines: list[str] = [
        f"# OSS engineering-tool watchlist — {report.run_date}",
        "",
        "## Run metadata",
        f"- Date: {report.run_date}",
        f"- Schema version: `{report.schema_version}`",
        f"- Roadmap anchor: {ROADMAP_URL}",
        f"- Public-safety note: {report.public_safety_note}",
        "- Data sources: committed `data/oss_tool_watchlist.json`, optional fixture observations, optional prior state, and `data/oss_tool_issue_map.json` only.",
        "",
        "## Tools checked and signal sources",
        "| Tool | Signal strategy | Source URL | Docs URL | Tier-1 links | Wiki target |",
        "|---|---|---|---|---|---|",
    ]
    for row in report.rows:
        tier1_links = ", ".join(row.tier1_repo_links)
        lines.append(f"| {row.name} | {row.signal_strategy} | {row.source_url} | {row.docs_url} | {tier1_links} | `{row.wiki_target}` |")
    lines.extend([
        "",
        "## Detected changes",
        "| Tool | Signal type | Observed | Previous | Confidence | Why it matters |",
        "|---|---|---|---|---|---|",
    ])
    for row in report.rows:
        lines.append(f"| {row.name} | {row.signal_type} | {row.observed_value or 'n/a'} | {row.previous_value or 'n/a'} | {row.confidence} | {row.why_it_matters} |")
    lines.extend([
        "",
        "## Candidate wiki updates",
        "| Tool | Candidate action | Affected paths | Rationale |",
        "|---|---|---|---|",
    ])
    for row in report.rows:
        lines.append(f"| {row.name} | {row.recommendation_action} | {_fmt_paths(row.affected_paths)} | {row.recommendation_rationale} |")
    lines.extend([
        "",
        "## Duplicate/open-issue routing",
        "| Tool | Route action | Issue | Route reason |",
        "|---|---|---|---|",
    ])
    for row in report.rows:
        lines.append(f"| {row.name} | {row.route_action} | [#{row.route_issue}]({issue_link(row.route_issue)}) | {row.route_reason} |")
    blocked = [row for row in report.rows if row.signal_type in {"signal_unavailable", "manual_review"} or row.recommendation_action == "manual_review"]
    lines.extend(["", "## Blocked/manual-review items"])
    if blocked:
        lines.extend(["| Tool | Signal type | Rationale |", "|---|---|---|"])
        for row in blocked:
            lines.append(f"| {row.name} | {row.signal_type} | {row.recommendation_rationale} |")
    else:
        lines.append("No blocked or manual-review items.")
    lines.extend([
        "",
        "## Validation evidence",
        f"- `{report.validation['tests']}`",
        f"- `{report.validation['generate']}`",
        f"- `{report.validation['validator']}`",
        "",
        "## Public-safety guardrail",
        "This artifact is public-safe: it contains public URLs, repo-relative paths, normalized signal metadata, and GitHub issue links only. It does not copy upstream docs, source code, release-note bodies, unprocessed upstream response bodies, secrets, cookies, headers, or private paths.",
    ])
    return "\n".join(lines) + "\n"


def to_state_dict(report: WatchlistReport) -> dict[str, Any]:
    return {
        "schema_version": STATE_SCHEMA_VERSION,
        "run_date": report.run_date,
        "totals": report.totals,
        "rows": [asdict(row) for row in report.rows],
        "public_safety_note": report.public_safety_note,
    }


def write_outputs(repo_root: Path, report: WatchlistReport, output: Path | None = None, state_output: Path | None = None) -> tuple[Path, Path]:
    md_path = output or repo_root / REPORT_DIR / f"{report.run_date}-oss-engineering-tool-watchlist.md"
    state_path = state_output or repo_root / STATE_DIR / f"{report.run_date}-oss-tool-watchlist-state.json"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_report(report), encoding="utf-8")
    state_path.write_text(json.dumps(to_state_dict(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    latest = repo_root / STATE_DIR / "latest-state.json"
    latest.write_text(json.dumps(to_state_dict(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return md_path, state_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--watchlist", type=Path, default=WATCHLIST_PATH)
    parser.add_argument("--issue-map", type=Path, default=ISSUE_MAP_PATH)
    parser.add_argument("--fixtures-dir", type=Path)
    parser.add_argument("--previous-state", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--state-output", type=Path)
    parser.add_argument("--write", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    repo_root = args.repo_root.resolve()
    fixtures_dir = None
    if args.fixtures_dir:
        fixtures_dir = args.fixtures_dir if args.fixtures_dir.is_absolute() else repo_root / args.fixtures_dir
    previous_state = None
    if args.previous_state:
        previous_state = args.previous_state if args.previous_state.is_absolute() else repo_root / args.previous_state
    output = args.output if (args.output is None or args.output.is_absolute()) else repo_root / args.output
    state_output = args.state_output if (args.state_output is None or args.state_output.is_absolute()) else repo_root / args.state_output
    report = scan_watchlist(repo_root, repo_root / args.watchlist if not args.watchlist.is_absolute() else args.watchlist, repo_root / args.issue_map if not args.issue_map.is_absolute() else args.issue_map, fixtures_dir=fixtures_dir, run_date=args.date, previous_state_path=previous_state)
    if args.write or output or state_output:
        md_path, state_path = write_outputs(repo_root, report, output, state_output)
        print(f"wrote {md_path}")
        print(f"wrote {state_path}")
    else:
        print(render_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
