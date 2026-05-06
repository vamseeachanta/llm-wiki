#!/usr/bin/env python3
"""Generate deterministic llm-wiki strengthening scorecards and portal pages.

This script is intentionally dependency-free so the public spinout repository can
score itself without the private workspace-hub pipeline. It reads only committed
markdown/wiki metadata and never copies raw source files into git.
"""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Iterable

WIKI_ROOT = Path("wikis")
REPORT_DIR = Path("docs/reports")
PORTAL_SECTIONS = ("concepts", "entities", "standards", "sources", "comparisons", "workflows")

WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+\.md)(?:#[^)]+)?\)")
FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
TITLE_RE = re.compile(r"^title:\s*[\"']?(.+?)[\"']?\s*$", re.M)
TAGS_RE = re.compile(r"^tags:\s*(.+?)\s*$", re.M)


@dataclass
class DomainScore:
    domain: str
    total_pages: int
    curated_pages: int
    source_pages: int
    concepts: int
    entities: int
    standards: int
    comparisons: int
    workflows: int
    has_index: bool
    has_log: bool
    has_overview: bool
    frontmatter_pages: int
    missing_frontmatter: int
    indexed_pages: int
    missing_from_index: int
    outbound_links: int
    inbound_linked_pages: int
    orphan_curated_pages: int
    freshness_days: int | None
    structural_score: float
    navigation_score: float
    provenance_score: float
    graph_score: float
    balance_score: float
    completeness_score: float
    recommended_action: str


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except FileNotFoundError:
        return ""


def iter_domains(root: Path = WIKI_ROOT) -> list[Path]:
    return sorted(p for p in root.iterdir() if p.is_dir() and (p / "wiki").is_dir())


def md_files(domain_dir: Path) -> list[Path]:
    return sorted((domain_dir / "wiki").rglob("*.md"))


def rel(path: Path) -> str:
    return path.as_posix()


def content_pages(files: Iterable[Path]) -> list[Path]:
    return [p for p in files if p.name not in {"index.md", "log.md", "overview.md", "portal.md"}]


def page_title(path: Path, text: str | None = None) -> str:
    text = read_text(path) if text is None else text
    fm = FRONTMATTER_RE.search(text)
    if fm:
        m = TITLE_RE.search(fm.group(1))
        if m:
            return m.group(1).strip().strip('"\'')
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def frontmatter_tags(text: str) -> list[str]:
    fm = FRONTMATTER_RE.search(text)
    if not fm:
        return []
    m = TAGS_RE.search(fm.group(1))
    if not m:
        return []
    raw = m.group(1).strip()
    if raw.startswith("[") and raw.endswith("]"):
        return [x.strip().strip('"\'') for x in raw[1:-1].split(",") if x.strip()]
    return [raw.strip('"\'')]


def count_indexed_paths(index_text: str, domain_dir: Path, pages: list[Path]) -> set[str]:
    indexed: set[str] = set()
    wiki_dir = domain_dir / "wiki"
    for link in MD_LINK_RE.findall(index_text):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        candidate = (wiki_dir / link).resolve()
        try:
            indexed.add(candidate.relative_to(Path.cwd()).as_posix())
        except ValueError:
            pass
    # Also catch plain filenames in enormous generated indexes if markdown parsing misses a row.
    for p in pages:
        if p.name in index_text or p.relative_to(wiki_dir).as_posix() in index_text:
            indexed.add(p.as_posix())
    return indexed


def resolve_md_link(source: Path, target: str, domain_dir: Path) -> str | None:
    if target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    candidate = (source.parent / target).resolve()
    try:
        return candidate.relative_to(Path.cwd()).as_posix()
    except ValueError:
        try:
            return candidate.relative_to(domain_dir).as_posix()
        except ValueError:
            return None


def infer_last_updated_days(files: list[Path], today: date) -> int | None:
    newest: date | None = None
    date_re = re.compile(r"last_updated:\s*(\d{4}-\d{2}-\d{2})")
    for p in files:
        m = date_re.search(read_text(p)[:800])
        if not m:
            continue
        try:
            d = date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if newest is None or d > newest:
            newest = d
    return None if newest is None else (today - newest).days


def clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def score_domain(domain_dir: Path, today: date) -> DomainScore:
    domain = domain_dir.name
    files = md_files(domain_dir)
    pages = content_pages(files)
    wiki_dir = domain_dir / "wiki"
    by_section = {section: list((wiki_dir / section).glob("*.md")) if (wiki_dir / section).exists() else [] for section in PORTAL_SECTIONS}

    texts = {p: read_text(p) for p in pages}
    fm_pages = sum(1 for t in texts.values() if FRONTMATTER_RE.search(t))
    missing_fm = len(pages) - fm_pages

    index_text = read_text(wiki_dir / "index.md")
    indexed = count_indexed_paths(index_text, domain_dir, pages)
    page_paths = {p.as_posix() for p in pages}
    missing_from_index = len(page_paths - indexed)

    slug_to_paths: dict[str, set[str]] = defaultdict(set)
    for p in pages:
        slug_to_paths[p.stem.lower()].add(p.as_posix())
        slug_to_paths[page_title(p, texts[p]).lower().replace(" ", "-")].add(p.as_posix())

    outbound = 0
    inbound: Counter[str] = Counter()
    for p, text in texts.items():
        for link in WIKILINK_RE.findall(text):
            outbound += 1
            for target in slug_to_paths.get(Path(link).stem.lower(), set()):
                inbound[target] += 1
        for link in MD_LINK_RE.findall(text):
            target = resolve_md_link(p, link, domain_dir)
            if target:
                outbound += 1
                inbound[target] += 1

    curated = [p for p in pages if p.parent.name in {"concepts", "entities", "standards", "comparisons", "workflows"}]
    orphan_curated = sum(1 for p in curated if inbound[p.as_posix()] == 0)
    freshness_days = infer_last_updated_days(files, today)

    total = len(pages)
    source_count = len(by_section["sources"])
    curated_count = len(curated)
    structural_score = 100.0 * sum((wiki_dir / n).exists() for n in ("index.md", "log.md", "overview.md")) / 3
    navigation_score = 100.0 if total == 0 else 100.0 * (1 - missing_from_index / max(total, 1))
    provenance_score = 100.0 if total == 0 else 100.0 * fm_pages / max(total, 1)
    graph_score = 0.0 if curated_count == 0 else 100.0 * (1 - orphan_curated / max(curated_count, 1))
    # Balance rewards having curated synthesis in addition to source inventory, without punishing source-heavy domains too hard.
    curated_ratio = curated_count / max(total, 1)
    if curated_ratio >= 0.25:
        balance_score = 100.0
    elif curated_ratio >= 0.05:
        balance_score = 70.0 + 30.0 * (curated_ratio - 0.05) / 0.20
    else:
        balance_score = 20.0 + 50.0 * curated_ratio / 0.05
    completeness = 0.25 * structural_score + 0.20 * navigation_score + 0.20 * provenance_score + 0.20 * graph_score + 0.15 * balance_score

    if not (wiki_dir / "index.md").exists() or not (wiki_dir / "overview.md").exists():
        action = "Restore core index/log/overview scaffold before content expansion."
    elif missing_from_index > 0:
        action = f"Backfill index entries for {missing_from_index} unindexed pages."
    elif missing_fm > 0:
        action = f"Backfill frontmatter/provenance on {missing_fm} pages."
    elif curated_count and orphan_curated / curated_count > 0.25:
        action = f"Add cross-links/backlinks for {orphan_curated} orphan curated pages."
    elif source_count > 1000 and curated_ratio < 0.01:
        action = "Prioritize generated portals and curated concept/entity hubs over more source-page volume."
    elif curated_count < 10:
        action = "Promote a small batch of source-backed concept/entity pages to create a navigable core."
    else:
        action = "Maintain cadence: add targeted cross-links and provenance while executing approved promotion packs."

    return DomainScore(
        domain=domain,
        total_pages=total,
        curated_pages=curated_count,
        source_pages=source_count,
        concepts=len(by_section["concepts"]),
        entities=len(by_section["entities"]),
        standards=len(by_section["standards"]),
        comparisons=len(by_section["comparisons"]),
        workflows=len(by_section["workflows"]),
        has_index=(wiki_dir / "index.md").exists(),
        has_log=(wiki_dir / "log.md").exists(),
        has_overview=(wiki_dir / "overview.md").exists(),
        frontmatter_pages=fm_pages,
        missing_frontmatter=missing_fm,
        indexed_pages=len(indexed & page_paths),
        missing_from_index=missing_from_index,
        outbound_links=outbound,
        inbound_linked_pages=len([p for p in page_paths if inbound[p] > 0]),
        orphan_curated_pages=orphan_curated,
        freshness_days=freshness_days,
        structural_score=round(clamp(structural_score), 1),
        navigation_score=round(clamp(navigation_score), 1),
        provenance_score=round(clamp(provenance_score), 1),
        graph_score=round(clamp(graph_score), 1),
        balance_score=round(clamp(balance_score), 1),
        completeness_score=round(clamp(completeness), 1),
        recommended_action=action,
    )


def markdown_table(rows: list[list[object]], headers: list[str]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(lines)


def generate_report(scores: list[DomainScore], today: date) -> str:
    ranked = sorted(scores, key=lambda s: s.completeness_score)
    total_pages = sum(s.total_pages for s in scores)
    total_curated = sum(s.curated_pages for s in scores)
    total_sources = sum(s.source_pages for s in scores)
    rows = [
        [s.domain, s.completeness_score, s.total_pages, s.curated_pages, s.source_pages, s.missing_frontmatter, s.missing_from_index, s.orphan_curated_pages, s.recommended_action]
        for s in ranked
    ]
    queue = []
    for s in ranked:
        if s.domain == "marine-engineering":
            queue.append("1. **#22 / marine-engineering portal** — keep improving generated portal facets because this domain carries almost all source volume but has a very low curated/source ratio.")
        elif s.missing_frontmatter:
            queue.append(f"1. **{s.domain} provenance pass** — backfill {s.missing_frontmatter} frontmatter gaps before further expansion.")
        elif s.orphan_curated_pages:
            queue.append(f"1. **{s.domain} graph pass** — add backlinks/cross-links for {s.orphan_curated_pages} orphan curated pages.")
        elif s.curated_pages < 10:
            queue.append(f"1. **{s.domain} seed promotion** — promote source-backed concept/entity pages to create a minimum navigable core.")
        if len(queue) >= 8:
            break
    queue = [re.sub(r"^1\.", f"{i}.", item, count=1) for i, item in enumerate(queue, 1)]

    return f"""---
title: "LLM-Wiki Strengthening Scorecard"
created: {today.isoformat()}
last_updated: {today.isoformat()}
auto_generated: true
generator: scripts/llm_wiki_strengthening_scorecard.py
related_issue: 37
---

# LLM-Wiki Strengthening Scorecard

This deterministic scorecard ranks each public `wikis/<domain>/wiki/` corpus using only committed markdown metadata. It does **not** read or copy raw private archives, vendor PDFs, or non-public source material.

## Repository Totals

- Domains scored: **{len(scores)}**
- Markdown content pages scored: **{total_pages:,}**
- Curated synthesis pages: **{total_curated:,}**
- Source-summary pages: **{total_sources:,}**

## Domain Ranking

{markdown_table(rows, ["Domain", "Score", "Pages", "Curated", "Sources", "Missing FM", "Missing Index", "Orphan Curated", "Recommended next action"])}

## Scoring Model

The final score is a weighted composite:

- **Structural (25%)** — index/log/overview scaffold exists.
- **Navigation (20%)** — content pages appear in the domain index.
- **Provenance (20%)** — content pages have YAML frontmatter.
- **Graph (20%)** — curated pages have inbound wiki/markdown links.
- **Balance (15%)** — domain has navigable curated synthesis, not only source-page volume.

This intentionally distinguishes structural weakness from scale differences. A small domain can score well if it is navigable and provenance-ready; a huge source-heavy domain can still rank as needing portal/curation work.

## Prioritized Safe Action Queue

{chr(10).join(queue) if queue else '- No immediate structural queue items found; continue approved promotion waves.'}

## Approval Boundary Notes

- Do **not** execute `status:plan-review` issues (#14-#19) without user approval.
- Safe work now: scorecard/reporting (#37), generated navigation/portal improvements for plan-approved #22, and metadata/provenance checks that use committed public files only.
- Raw/source-family extraction remains bounded to separately approved plans; this report is metadata-only.
"""


def source_sort_key(item: tuple[str, str]) -> tuple[int, str]:
    """Prefer descriptive source pages over numeric vendor/PDF filenames."""
    title, path = item
    slug = Path(path).stem.lower()
    generic = bool(re.fullmatch(r"\d+[a-z]{0,3}", slug)) or title.lower().endswith((".pdf", ".doc", ".docx", ".xls", ".xlsx"))
    return (1 if generic else 0, title.lower())


def top_items(domain_dir: Path, section: str, limit: int = 20) -> list[tuple[str, str]]:
    directory = domain_dir / "wiki" / section
    if not directory.exists():
        return []
    items = []
    for p in sorted(directory.glob("*.md")):
        text = read_text(p)
        title = page_title(p, text)
        relpath = p.relative_to(domain_dir / "wiki").as_posix()
        items.append((title, relpath))
    if section == "sources":
        items = sorted(items, key=source_sort_key)
    return items[:limit]


def make_portal(domain_dir: Path, score: DomainScore, today: date) -> str:
    domain = domain_dir.name
    display_domain = domain.replace('-', ' ').title()
    section_blocks = []
    counts = {
        "Concepts": score.concepts,
        "Entities": score.entities,
        "Standards": score.standards,
        "Sources": score.source_pages,
        "Comparisons": score.comparisons,
        "Workflows": score.workflows,
    }
    for title, section in [("Concept hubs", "concepts"), ("Entity hubs", "entities"), ("Standards", "standards"), ("Comparisons", "comparisons"), ("Representative source summaries", "sources")]:
        items = top_items(domain_dir, section, 18 if section != "sources" else 22)
        if not items:
            continue
        links = "\n".join(f"- [{name}]({path})" for name, path in items)
        section_blocks.append(f"## {title}\n\n{links}\n")

    source_note = ""
    if score.source_pages > 1000:
        source_note = "\n> This domain is source-heavy. Treat this portal as the human/agent entry point and use the canonical index for exhaustive source-page lookup.\n"

    content = f"""---
title: "{display_domain} Portal"
type: portal
domain: {domain}
created: {today.isoformat()}
last_updated: {today.isoformat()}
auto_generated: true
generator: scripts/llm_wiki_strengthening_scorecard.py
related_issue: 22
---

# {display_domain} Portal

Generated faceted entry point for the `{domain}` wiki. It complements, but does not replace, the exhaustive [domain index](index.md).{source_note}

## Corpus Snapshot

{markdown_table([[k, f'{v:,}'] for k, v in counts.items()], ["Facet", "Pages"])}

## Recommended Use

- Start here for curated concepts, entities, standards, and comparisons.
- Use [index.md](index.md) for exhaustive page lookup.
- Use [log.md](log.md) to inspect recent ingest/maintenance activity.
- Use [overview.md](overview.md) for narrative domain scope when it is current.

{chr(10).join(section_blocks)}
"""
    return content.rstrip() + "\n"


def ensure_index_portal_link(domain_dir: Path, today: date) -> bool:
    index = domain_dir / "wiki" / "index.md"
    text = read_text(index)
    if "portal.md" in text:
        return False
    marker = "# Knowledge Index:"
    lines = text.splitlines()
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith(marker):
            insert_at = i + 1
            break
    if insert_at is None:
        insert_at = 0
    block = ["", f"> Faceted navigation: [Domain portal](portal.md) (generated {today.isoformat()}).", ""]
    lines[insert_at:insert_at] = block
    index.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--write", action="store_true", help="Write JSON/Markdown reports and portal pages")
    parser.add_argument("--portal-domain", default="marine-engineering", help="Domain for generated portal page")
    args = parser.parse_args()
    today = date.fromisoformat(args.date)

    scores = [score_domain(d, today) for d in iter_domains()]
    payload = {
        "generated": today.isoformat(),
        "generator": "scripts/llm_wiki_strengthening_scorecard.py",
        "domains": [asdict(s) for s in sorted(scores, key=lambda s: s.domain)],
        "ranked": [s.domain for s in sorted(scores, key=lambda s: s.completeness_score)],
    }

    if args.write:
        REPORT_DIR.mkdir(parents=True, exist_ok=True)
        (REPORT_DIR / "llm-wiki-strengthening-scorecard.json").write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        (REPORT_DIR / "llm-wiki-strengthening-scorecard.md").write_text(generate_report(scores, today), encoding="utf-8")
        target = WIKI_ROOT / args.portal_domain
        score_by_domain = {s.domain: s for s in scores}
        if target.exists() and args.portal_domain in score_by_domain:
            portal_path = target / "wiki" / "portal.md"
            portal_path.write_text(make_portal(target, score_by_domain[args.portal_domain], today), encoding="utf-8")
            ensure_index_portal_link(target, today)
    else:
        print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
