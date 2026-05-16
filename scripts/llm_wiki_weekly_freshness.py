#!/usr/bin/env python3
"""Generate the weekly public-safe llm-wiki freshness report.

The weekly loop is intentionally offline and dependency-free. It reads committed
repo content, a checked-in concept watchlist, and a checked-in issue routing map;
it does not fetch GitHub or private/raw archives.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

SCHEMA_VERSION = "weekly-freshness/v1"
WIKI_ROOT = Path("wikis")
REPORT_DIR = Path("docs/reports")
FRESHNESS_DIR = Path("artifacts/freshness")
CONCEPT_WATCHLIST = Path("data/concept_watchlist.json")
ISSUE_ROUTING_MAP = Path("data/issue_routing_map.json")
ROADMAP_URL = "https://github.com/vamseeachanta/llm-wiki/issues/13"
REPO_URL = "https://github.com/vamseeachanta/llm-wiki"

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
TITLE_RE = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.M)
LAST_UPDATED_RE = re.compile(r"^last_updated:\s*[\"']?(\d{4}-\d{2}-\d{2})[\"']?\s*$", re.M)
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
SKIP_PAGE_NAMES = {"index.md", "log.md", "overview.md", "portal.md", "_template.md", "template.md"}
PUBLIC_SAFETY_NOTE = "public-safe metadata-only report; no raw/private/vendor/client content."
ACTIVE_UPDATE_ACTIONS = {"update-existing-issue", "reuse-existing-issue"}
KNOWN_CLOSED_ROUTE_ISSUES = {76, 79}
ROADMAP_FALLBACK_ROUTE = {"issue": 13, "title": "Roadmap anchor update", "action": "comment-on-roadmap"}


@dataclass(frozen=True)
class DomainFreshness:
    domain: str
    total_pages: int
    missing_frontmatter: int
    missing_last_updated: int
    stale_pages: int
    broken_links: int
    total_pages_delta: int = 0
    missing_frontmatter_delta: int = 0
    missing_last_updated_delta: int = 0
    stale_pages_delta: int = 0
    broken_links_delta: int = 0


@dataclass(frozen=True)
class RepoTotals:
    total_pages: int
    missing_frontmatter: int
    missing_last_updated: int
    stale_pages: int
    broken_links: int
    total_pages_delta: int = 0
    missing_frontmatter_delta: int = 0
    missing_last_updated_delta: int = 0
    stale_pages_delta: int = 0
    broken_links_delta: int = 0


@dataclass(frozen=True)
class PageFinding:
    path: str
    domain: str
    age_days: int | None
    last_updated: str | None
    reason: str


@dataclass(frozen=True)
class BrokenLink:
    source: str
    domain: str
    target: str
    reason: str


@dataclass(frozen=True)
class Recommendation:
    action: str
    issue: int
    title: str
    rationale: str
    reason_code: str = "manual-route"
    confidence: str = "medium"
    issue_route: str = "portfolio-roadmap"
    public_safe_summary: str = "Public-safe weekly routing recommendation."


@dataclass(frozen=True)
class WeeklyReport:
    schema_version: str
    run_date: str
    baseline_run_date: str
    totals: RepoTotals
    domains: dict[str, DomainFreshness]
    stale_pages: list[PageFinding]
    broken_links: list[BrokenLink]
    concept_watchlist: list[dict[str, str]]
    recommendations: list[Recommendation]
    validation: dict[str, str]
    public_safety_note: str = PUBLIC_SAFETY_NOTE


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def iter_domain_dirs(repo_root: Path) -> list[Path]:
    root = repo_root / WIKI_ROOT
    if not root.exists():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and (path / "wiki").is_dir())


def iter_markdown_pages(domain_dir: Path) -> list[Path]:
    return sorted(path for path in (domain_dir / "wiki").rglob("*.md") if path.name.lower() not in SKIP_PAGE_NAMES)


def rel(repo_root: Path, path: Path) -> str:
    return path.relative_to(repo_root).as_posix()


def parse_frontmatter(text: str) -> str | None:
    match = FRONTMATTER_RE.search(text)
    return match.group(1) if match else None


def parse_last_updated(text: str) -> date | None:
    frontmatter = parse_frontmatter(text)
    if not frontmatter:
        return None
    match = LAST_UPDATED_RE.search(frontmatter)
    if not match:
        return None
    try:
        return date.fromisoformat(match.group(1))
    except ValueError:
        return None


def strip_link_target(target: str) -> str:
    target = unquote(target.strip())
    target = target.split("#", 1)[0]
    target = target.split("?", 1)[0]
    return target.strip()


def is_external_link(target: str) -> bool:
    lowered = target.lower()
    return lowered.startswith(("http://", "https://", "mailto:", "tel:", "ftp://", "#"))


def resolve_md_link(repo_root: Path, source: Path, target: str) -> Path | None:
    cleaned = strip_link_target(target)
    if not cleaned or is_external_link(cleaned) or not cleaned.endswith(".md"):
        return None
    if cleaned.startswith("/"):
        candidate = repo_root / cleaned.lstrip("/")
    else:
        candidate = source.parent / cleaned
    return candidate.resolve()


def detect_broken_links(repo_root: Path, source: Path, text: str, domain: str) -> list[BrokenLink]:
    findings: list[BrokenLink] = []
    for target in MD_LINK_RE.findall(text):
        cleaned = strip_link_target(target)
        candidate = resolve_md_link(repo_root, source, cleaned)
        if candidate is not None and not candidate.exists():
            findings.append(BrokenLink(source=rel(repo_root, source), domain=domain, target=cleaned, reason="missing-md-target"))
    # Wikilinks are intentionally conservative: only report absolute/path-like wikilinks.
    for target in WIKILINK_RE.findall(text):
        cleaned = strip_link_target(target)
        if "/" not in cleaned or not cleaned.endswith(".md"):
            continue
        candidate = resolve_md_link(repo_root, source, cleaned)
        if candidate is not None and not candidate.exists():
            findings.append(BrokenLink(source=rel(repo_root, source), domain=domain, target=cleaned, reason="missing-wikilink-target"))
    return findings


def load_json_list(path: Path, fallback: list[dict[str, str]]) -> list[dict[str, str]]:
    if not path.exists():
        return fallback
    loaded = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(loaded, dict):
        return list(loaded.get("items", []))
    return list(loaded)


def default_concepts() -> list[dict[str, str]]:
    return [
        {"concept": "llms.txt", "why": "Agent-friendly repo/site entrypoints and curated markdown manifests.", "public_reference": "https://llmstxt.org/"},
        {"concept": "Model Context Protocol (MCP)", "why": "Standard tool/context protocol for agent query surfaces and future llm-wiki integrations.", "public_reference": "https://modelcontextprotocol.io/"},
        {"concept": "GraphRAG / LightRAG", "why": "Graph-backed retrieval patterns for entity, community, and citation-aware knowledge navigation.", "public_reference": "https://github.com/microsoft/graphrag"},
        {"concept": "RAG evaluation", "why": "Faithfulness, context precision/recall, and answer-correctness checks for downstream code-assistant usefulness.", "public_reference": "https://docs.ragas.io/"},
    ]



def _metric_delta(current: int, previous: dict[str, int] | None, key: str) -> int:
    if previous is None:
        return 0
    try:
        return current - int(previous.get(key, 0))
    except (TypeError, ValueError):
        return 0


def _load_previous_summary(repo_root: Path, run_date: date) -> dict | None:
    freshness_dir = repo_root / FRESHNESS_DIR
    if not freshness_dir.exists():
        return None
    candidates: list[tuple[date, Path, dict]] = []
    for path in sorted(freshness_dir.glob("*-weekly-freshness-summary.json")):
        prefix = path.name.split("-weekly-freshness-summary.json", 1)[0]
        try:
            candidate_date = date.fromisoformat(prefix)
        except ValueError:
            continue
        if candidate_date >= run_date:
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if data.get("schema_version") == SCHEMA_VERSION:
            candidates.append((candidate_date, path, data))
    if not candidates:
        return None
    return max(candidates, key=lambda item: item[0])[2]


def _previous_domain_map(previous: dict | None) -> dict[str, dict]:
    if not previous:
        return {}
    if isinstance(previous.get("domains"), dict):
        return {str(key): value for key, value in previous["domains"].items() if isinstance(value, dict)}
    rows = previous.get("domain_freshness", [])
    if isinstance(rows, list):
        return {str(row.get("domain")): row for row in rows if isinstance(row, dict) and row.get("domain")}
    return {}


def _previous_totals(previous: dict | None) -> dict | None:
    if not previous:
        return None
    totals = previous.get("repo_totals") or previous.get("totals")
    return totals if isinstance(totals, dict) else None


def analyze_repo(repo_root: Path, run_date: date, stale_days: int = 30, max_items: int = 25) -> WeeklyReport:
    repo_root = repo_root.resolve()
    previous = _load_previous_summary(repo_root, run_date)
    previous_domains = _previous_domain_map(previous)
    previous_totals = _previous_totals(previous)
    domain_rows: dict[str, DomainFreshness] = {}
    stale: list[PageFinding] = []
    broken: list[BrokenLink] = []
    total_pages = missing_frontmatter = missing_last_updated = 0

    for domain_dir in iter_domain_dirs(repo_root):
        domain = domain_dir.name
        pages = iter_markdown_pages(domain_dir)
        d_missing_fm = d_missing_lu = 0
        d_stale = 0
        d_broken = 0
        for page in pages:
            text = read_text(page)
            total_pages += 1
            frontmatter = parse_frontmatter(text)
            if not frontmatter:
                missing_frontmatter += 1
                d_missing_fm += 1
            updated = parse_last_updated(text)
            if updated is None:
                missing_last_updated += 1
                d_missing_lu += 1
            else:
                age = (run_date - updated).days
                if age > stale_days:
                    d_stale += 1
                    stale.append(PageFinding(path=rel(repo_root, page), domain=domain, age_days=age, last_updated=updated.isoformat(), reason=f"last_updated older than {stale_days} days"))
            page_broken = detect_broken_links(repo_root, page, text, domain)
            d_broken += len(page_broken)
            broken.extend(page_broken)
        previous_domain = previous_domains.get(domain)
        domain_rows[domain] = DomainFreshness(
            domain=domain,
            total_pages=len(pages),
            missing_frontmatter=d_missing_fm,
            missing_last_updated=d_missing_lu,
            stale_pages=d_stale,
            broken_links=d_broken,
            total_pages_delta=_metric_delta(len(pages), previous_domain, "total_pages"),
            missing_frontmatter_delta=_metric_delta(d_missing_fm, previous_domain, "missing_frontmatter"),
            missing_last_updated_delta=_metric_delta(d_missing_lu, previous_domain, "missing_last_updated"),
            stale_pages_delta=_metric_delta(d_stale, previous_domain, "stale_pages"),
            broken_links_delta=_metric_delta(d_broken, previous_domain, "broken_links"),
        )

    stale_sorted = sorted(stale, key=lambda item: (-(item.age_days or -1), item.path))[:max_items]
    broken_sorted = sorted(broken, key=lambda item: (item.domain, item.source, item.target))[:max_items]
    totals = RepoTotals(
        total_pages=total_pages,
        missing_frontmatter=missing_frontmatter,
        missing_last_updated=missing_last_updated,
        stale_pages=len(stale),
        broken_links=len(broken),
        total_pages_delta=_metric_delta(total_pages, previous_totals, "total_pages"),
        missing_frontmatter_delta=_metric_delta(missing_frontmatter, previous_totals, "missing_frontmatter"),
        missing_last_updated_delta=_metric_delta(missing_last_updated, previous_totals, "missing_last_updated"),
        stale_pages_delta=_metric_delta(len(stale), previous_totals, "stale_pages"),
        broken_links_delta=_metric_delta(len(broken), previous_totals, "broken_links"),
    )
    concepts = load_json_list(repo_root / CONCEPT_WATCHLIST, default_concepts())
    partial = WeeklyReport(
        schema_version=SCHEMA_VERSION,
        run_date=run_date.isoformat(),
        baseline_run_date=str(previous.get("run_date", run_date.isoformat())) if previous else run_date.isoformat(),
        totals=totals,
        domains=domain_rows,
        stale_pages=stale_sorted,
        broken_links=broken_sorted,
        concept_watchlist=concepts,
        recommendations=[],
        validation={
            "tests": "uv run pytest tests/test_llm_wiki_weekly_freshness.py tests/test_weekly_freshness_artifacts.py -q",
            "generate": f"uv run python scripts/llm_wiki_weekly_freshness.py --date {run_date.isoformat()} --write",
            "validator": f"uv run python scripts/validate_weekly_freshness_report.py docs/reports/{run_date.isoformat()}-llm-wiki-weekly-freshness-report.md && uv run python scripts/validate_issue_route_state.py data/issue_routing_map.json data/oss_tool_issue_map.json",
        },
    )
    recommendations = build_recommendations(partial, repo_root=repo_root)
    return WeeklyReport(**{**asdict(partial), "totals": totals, "domains": domain_rows, "stale_pages": stale_sorted, "broken_links": broken_sorted, "recommendations": recommendations})


def _safe_route(route: dict[str, str | int]) -> dict[str, str | int]:
    issue = int(route.get("issue", 13))
    action = str(route.get("action", "comment-on-roadmap"))
    if action in ACTIVE_UPDATE_ACTIONS and issue in KNOWN_CLOSED_ROUTE_ISSUES:
        return {**ROADMAP_FALLBACK_ROUTE, "title": str(route.get("title", ROADMAP_FALLBACK_ROUTE["title"]))}
    return route


def validate_issue_routes(routes: dict[str, dict[str, str | int]], issue_states: dict[int, str]) -> list[str]:
    failures: list[str] = []
    for key, route in routes.items():
        action = str(route.get("action", "comment-on-roadmap"))
        issue = int(route.get("issue", 13))
        state = str(issue_states.get(issue, "UNKNOWN")).upper()
        if action in ACTIVE_UPDATE_ACTIONS and state == "CLOSED":
            failures.append(f"{key} targets closed issue #{issue} with active action {action}")
    return failures


def load_issue_routes(repo_root: Path | None = None) -> dict[str, dict[str, str | int]]:
    root = repo_root or Path.cwd()
    path = root / ISSUE_ROUTING_MAP
    if not path.exists():
        return {
            "portfolio-roadmap": dict(ROADMAP_FALLBACK_ROUTE),
            "llms-entrypoints": {**ROADMAP_FALLBACK_ROUTE, "title": "llms.txt entrypoints"},
            "oss-watchlist": {**ROADMAP_FALLBACK_ROUTE, "title": "Weekly OSS engineering-tool watchlist"},
        }
    data = json.loads(path.read_text(encoding="utf-8"))
    routes = data.get("routes", data)
    return {str(key): _safe_route(value) for key, value in routes.items()}


def _recommendation(route: dict[str, str | int], rationale: str, reason_code: str, confidence: str = "high", issue_route: str = "portfolio-roadmap") -> Recommendation:
    return Recommendation(
        action=str(route.get("action", "comment-on-roadmap")),
        issue=int(route.get("issue", 13)),
        title=str(route.get("title", "Weekly freshness routing")),
        rationale=rationale,
        reason_code=reason_code,
        confidence=confidence,
        issue_route=issue_route,
        public_safe_summary=rationale,
    )


def build_recommendations(report: WeeklyReport, repo_root: Path | None = None) -> list[Recommendation]:
    routes = load_issue_routes(repo_root)
    recs: list[Recommendation] = []
    roadmap_rationale = "Post weekly freshness summary and domain deltas to the roadmap anchor instead of opening a duplicate umbrella."
    if report.totals.missing_frontmatter or report.totals.stale_pages or report.totals.broken_links:
        roadmap_rationale += " Route stale metadata, missing frontmatter, and broken-link deltas through the existing roadmap queue for prioritization."
    recs.append(_recommendation(routes["portfolio-roadmap"], roadmap_rationale, "portfolio-weekly-summary", issue_route="portfolio-roadmap"))
    for item in report.concept_watchlist:
        route_key = str(item.get("route_key", "")).strip()
        if not route_key or route_key not in routes:
            continue
        concept = item.get("concept", "curated concept")
        rationale = f"Track curated public concept `{concept}` through `{route_key}`; #75 reports the signal but does not implement adjacent feature scope."
        recs.append(_recommendation(routes[route_key], rationale, f"concept-{route_key}", confidence=str(item.get("confidence", "medium")), issue_route=route_key))

    deduped: dict[tuple[str, int, str], Recommendation] = {}
    for rec in recs:
        deduped[(rec.action, rec.issue, rec.reason_code)] = rec
    return list(deduped.values())


def issue_link(issue: int) -> str:
    return f"https://github.com/vamseeachanta/llm-wiki/issues/{issue}"


def render_report(report: WeeklyReport, recommendations: list[Recommendation] | None = None) -> str:
    recommendations = recommendations if recommendations is not None else report.recommendations
    lines: list[str] = [
        f"# llm-wiki weekly freshness report — {report.run_date}",
        "",
        "## Run metadata",
        f"- Date: {report.run_date}",
        f"- Schema version: `{report.schema_version}`",
        f"- Baseline run date: {report.baseline_run_date}",
        f"- Roadmap anchor: {ROADMAP_URL}",
        f"- Public-safety note: {report.public_safety_note}",
        "- Data sources: committed `wikis/` markdown, `data/concept_watchlist.json`, and `data/issue_routing_map.json` only.",
        "",
        "## Repo freshness summary",
        "| Metric | Value | Delta vs baseline |",
        "|---|---:|---:|",
        f"| Total pages | {report.totals.total_pages} | {report.totals.total_pages_delta:+d} |",
        f"| Missing frontmatter | {report.totals.missing_frontmatter} | {report.totals.missing_frontmatter_delta:+d} |",
        f"| Missing `last_updated` | {report.totals.missing_last_updated} | {report.totals.missing_last_updated_delta:+d} |",
        f"| Stale pages | {report.totals.stale_pages} | {report.totals.stale_pages_delta:+d} |",
        f"| Broken internal markdown links | {report.totals.broken_links} | {report.totals.broken_links_delta:+d} |",
        "",
        "## Domain coverage deltas",
        "First weekly run is an absolute baseline. Future runs compare against the previous JSON artifact with the same schema version.",
        "",
        "| Domain | Pages | Δ pages | Missing frontmatter | Δ missing FM | Missing `last_updated` | Δ missing updated | Stale pages | Δ stale | Broken links | Δ broken |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for domain in sorted(report.domains):
        row = report.domains[domain]
        lines.append(f"| {domain} | {row.total_pages} | {row.total_pages_delta:+d} | {row.missing_frontmatter} | {row.missing_frontmatter_delta:+d} | {row.missing_last_updated} | {row.missing_last_updated_delta:+d} | {row.stale_pages} | {row.stale_pages_delta:+d} | {row.broken_links} | {row.broken_links_delta:+d} |")
    lines.extend(["", "## Stale pages and structural findings"])
    if report.stale_pages:
        lines.extend(["| Path | Last updated | Age days | Reason |", "|---|---:|---:|---|"])
        for item in report.stale_pages:
            lines.append(f"| `{item.path}` | {item.last_updated or 'unknown'} | {item.age_days if item.age_days is not None else 'n/a'} | {item.reason} |")
    else:
        lines.append("No stale pages above the configured threshold.")
    if report.broken_links:
        lines.extend(["", "### Broken internal markdown links", "| Source | Target | Reason |", "|---|---|---|"])
        for item in report.broken_links:
            lines.append(f"| `{item.source}` | `{item.target}` | {item.reason} |")
    else:
        lines.append("No broken internal markdown links found in the bounded scan.")

    lines.extend(["", "## Concept watchlist", "| Concept | Why it matters | Public reference |", "|---|---|---|"])
    for item in report.concept_watchlist:
        lines.append(f"| {item.get('concept', '')} | {item.get('why', '')} | {item.get('public_reference', '')} |")

    lines.extend(["", "## Issue recommendations", "| Action | Issue | Issue route | Reason code | Confidence | Title | Public-safe summary |", "|---|---|---|---|---|---|---|"])
    for rec in recommendations:
        lines.append(f"| {rec.action} | [#{rec.issue}]({issue_link(rec.issue)}) | `{rec.issue_route}` | `{rec.reason_code}` | {rec.confidence} | {rec.title} | {rec.public_safe_summary} |")

    lines.extend([
        "",
        "## Blocked / approval-gated lanes",
        "- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76), [#77](https://github.com/vamseeachanta/llm-wiki/issues/77), [#78](https://github.com/vamseeachanta/llm-wiki/issues/78), [#79](https://github.com/vamseeachanta/llm-wiki/issues/79), and [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) are adjacent lanes. #75 reports on their status categories but does not implement their feature scope.",
        "- Approval-gated or unapproved lanes must stay as issue recommendations only until explicitly moved through the repo workflow.",
        "",
        "## Validation evidence",
        f"- `{report.validation['tests']}`",
        f"- `{report.validation['generate']}`",
        f"- `{report.validation['validator']}`",
        "",
        "## Public-safety guardrail",
        "This artifact is public-safe: it contains summary metadata, repo-relative committed paths, public issue links, and public concept URLs only.",
    ])
    return "\n".join(lines) + "\n"



def to_json_dict(report: WeeklyReport) -> dict:
    data = asdict(report)
    data["repo_totals"] = data["totals"]
    data["domain_freshness"] = [data["domains"][domain] for domain in sorted(data["domains"])]
    return data


def write_outputs(repo_root: Path, report: WeeklyReport) -> tuple[Path, Path]:
    md_path = repo_root / REPORT_DIR / f"{report.run_date}-llm-wiki-weekly-freshness-report.md"
    json_path = repo_root / FRESHNESS_DIR / f"{report.run_date}-weekly-freshness-summary.json"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(render_report(report), encoding="utf-8")
    json_path.write_text(json.dumps(to_json_dict(report), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return md_path, json_path


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--stale-days", type=int, default=30)
    parser.add_argument("--max-report-items", type=int, default=25)
    parser.add_argument("--write", action="store_true", help="Write Markdown and JSON artifacts")
    parser.add_argument("--output", type=Path, help="Optional Markdown output path; implies writing the Markdown report")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    run_date = date.fromisoformat(args.date)
    repo_root = args.repo_root.resolve()
    report = analyze_repo(repo_root, run_date, stale_days=args.stale_days, max_items=args.max_report_items)
    if args.write:
        md_path, json_path = write_outputs(repo_root, report)
        print(f"wrote {md_path.relative_to(repo_root)}")
        print(f"wrote {json_path.relative_to(repo_root)}")
    elif args.output:
        output = args.output if args.output.is_absolute() else repo_root / args.output
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_report(report), encoding="utf-8")
        print(f"wrote {output.relative_to(repo_root)}")
    else:
        print(render_report(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
