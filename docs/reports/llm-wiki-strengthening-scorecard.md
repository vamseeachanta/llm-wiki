---
title: "LLM-Wiki Strengthening Scorecard"
created: 2026-05-06
last_updated: 2026-05-06
auto_generated: true
generator: scripts/llm_wiki_strengthening_scorecard.py
related_issue: 37
---

# LLM-Wiki Strengthening Scorecard

This deterministic scorecard ranks each public `wikis/<domain>/wiki/` corpus using only committed markdown metadata. It does **not** read or copy raw private archives, vendor PDFs, or non-public source material.

## Repository Totals

- Domains scored: **8**
- Markdown content pages scored: **19,549**
- Curated synthesis pages: **304**
- Source-summary pages: **19,245**

## Domain Ranking

| Domain | Score | Pages | Curated | Sources | Missing FM | Missing Index | Orphan Curated | Recommended next action |
|---|---|---|---|---|---|---|---|---|
| marine-engineering | 84.6 | 19209 | 43 | 19166 | 0 | 1 | 8 | Backfill index entries for 1 unindexed pages. |
| engineering | 96.7 | 126 | 103 | 23 | 0 | 1 | 16 | Backfill index entries for 1 unindexed pages. |
| naval-architecture | 96.9 | 69 | 26 | 43 | 0 | 0 | 4 | Maintain cadence: add targeted cross-links and provenance while executing approved promotion packs. |
| lng-projects | 97.5 | 11 | 8 | 3 | 0 | 0 | 1 | Promote a small batch of source-backed concept/entity pages to create a navigable core. |
| engineering-standards | 97.8 | 78 | 73 | 5 | 0 | 1 | 7 | Backfill index entries for 1 unindexed pages. |
| maritime-law | 99.3 | 29 | 27 | 2 | 0 | 0 | 1 | Maintain cadence: add targeted cross-links and provenance while executing approved promotion packs. |
| acma-projects | 100.0 | 4 | 2 | 2 | 0 | 0 | 0 | Promote a small batch of source-backed concept/entity pages to create a navigable core. |
| asset-management | 100.0 | 23 | 22 | 1 | 0 | 0 | 0 | Maintain cadence: add targeted cross-links and provenance while executing approved promotion packs. |

## Scoring Model

The final score is a weighted composite:

- **Structural (25%)** — index/log/overview scaffold exists.
- **Navigation (20%)** — content pages appear in the domain index.
- **Provenance (20%)** — content pages have YAML frontmatter.
- **Graph (20%)** — curated pages have inbound wiki/markdown links.
- **Balance (15%)** — domain has navigable curated synthesis, not only source-page volume.

This intentionally distinguishes structural weakness from scale differences. A small domain can score well if it is navigable and provenance-ready; a huge source-heavy domain can still rank as needing portal/curation work.

## Prioritized Safe Action Queue

1. **#22 / marine-engineering portal** — keep improving generated portal facets because this domain carries almost all source volume but has a very low curated/source ratio.
2. **engineering graph pass** — add backlinks/cross-links for 16 orphan curated pages.
3. **naval-architecture graph pass** — add backlinks/cross-links for 4 orphan curated pages.
4. **lng-projects graph pass** — add backlinks/cross-links for 1 orphan curated pages.
5. **engineering-standards graph pass** — add backlinks/cross-links for 7 orphan curated pages.
6. **maritime-law graph pass** — add backlinks/cross-links for 1 orphan curated pages.
7. **acma-projects seed promotion** — promote source-backed concept/entity pages to create a minimum navigable core.

## Approval Boundary Notes

- Do **not** execute `status:plan-review` issues (#14-#19) without user approval.
- Safe work now: scorecard/reporting (#37), generated navigation/portal improvements for plan-approved #22, and metadata/provenance checks that use committed public files only.
- Raw/source-family extraction remains bounded to separately approved plans; this report is metadata-only.
