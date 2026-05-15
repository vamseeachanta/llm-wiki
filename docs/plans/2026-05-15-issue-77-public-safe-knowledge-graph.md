---
title: "Issue #77 plan — public-safe knowledge-graph and link-graph manifests"
issue: 77
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: metadata-only graph extraction from committed markdown; NO raw/private paths, copied standards text, vendor/client content, or secret-bearing manifests
---

# Issue #77 Plan — Public-Safe Knowledge Graph and Link-Graph Manifests

## Approval-gate note

- GitHub issue: [vamseeachanta/llm-wiki#77](https://github.com/vamseeachanta/llm-wiki/issues/77)
- Local plan status: `plan-review`
- Implementation status: **not started**
- This artifact is planning-only. It does **not** authorize implementation, issue-label edits, issue comments, or code changes beyond this plan file.
- Per repo workflow, implementation should begin only after explicit user approval and the issue is advanced to the approved state by the main agent.

## Summary

Issue #77 should add a deterministic, repo-local graph generation layer over committed `llm-wiki` markdown so agents and future tooling can traverse:

- pages
- standards
- concepts
- entities
- source summaries
- code/data/result link pages
- governance blockers
- cross-domain bridges

The first implementation should stay deliberately simple and public-safe: extract nodes and typed edges from frontmatter plus internal markdown links, then emit machine-readable manifests and a human-readable gap report. The plan recommends a **CLI/script + tests + validator + report** shape, with JSONL/CSV as required outputs and GraphML explicitly deferred unless the JSONL schema proves stable.

## Current evidence / intelligence

### Live issues inspected

1. [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — target issue; defines graph-manifest goal, relationship types, public-safety requirements, and acceptance criteria.
2. [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) — weekly freshness loop; related consumer of graph outputs but out of scope for #77.
3. [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — `llms.txt` manifests; adjacent discovery layer, not the graph-generation layer.
4. [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — retrieval benchmark; should consume #77 outputs later, but benchmark definition is separate.
5. [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — OSS tool watchlist; independent metadata feed, not graph extraction.
6. [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — CLI/MCP query surface; depends on stable graph/manifests, but query APIs are out of scope here.

### Exact repo files inspected

1. `README.md` — repo layout and exposure contract (`wikis/`, `cross-links.md`, supporting scripts/tests live in this repo).
2. `docs/plans/README.md` — canonical plan workflow and public-safety default for plan artifacts.
3. `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` — practical-completion definition, raw/private boundary, and approval-blocking rules.
4. `docs/reports/2026-05-11-tier1-ecosystem-link-map.md` — authoritative data/software/results/governance link taxonomy.
5. `docs/reports/llm-wiki-strengthening-scorecard.md` — current graph weakness signals (especially orphan curated pages and missing inbound links).
6. `wikis/cross-links-tier1.md` — existing tier-1 cross-link map; useful seed for `public-result` / implementation edge extraction.
7. `wikis/marine-engineering/wiki/code-results-links.md` — concrete code/result link-page pattern.
8. `wikis/engineering/wiki/public-data-software-links.md` — concrete data/software link-page pattern.
9. `wikis/drilling-engineering/wiki/standards/norsok-d-010.md` — standards page with frontmatter + typed textual relationships (`supersedes` semantics, cross-references, concept links).
10. `scripts/llm_wiki_strengthening_scorecard.py` — existing deterministic markdown parser, frontmatter regexes, internal-link resolution, orphan-page logic, and repo-local reporting pattern.
11. `scripts/validate_completion_artifacts.py` — validator pattern for public-safe documentation artifacts and forbidden-path scanning.
12. `tests/test_completion_artifacts.py` — regression-test style for documentation/control-plane validators.
13. `tests/test_scan_source_families_safe.py` — existing safety-test precedent for redaction and no-path-leak guarantees.
14. `docs/session-handoffs/2026-05-15-issues-41-42-standards-routing-exit.md` — evidence that cross-wiki standards bridges already exist and should be graph-addressable.
15. `wikis/_audit/iter-56-W252-frontmatter-audit.md` — evidence that frontmatter field normalization remains imperfect (`cross_links`, `supersedes` shape drift), which affects graph extraction robustness.

### Key intelligence derived from inspection

- The repo already has a **metadata-only analysis pattern** in `scripts/llm_wiki_strengthening_scorecard.py`; #77 should reuse that approach rather than invent a heavier parser stack.
- The repo already has **human-readable link-map artifacts** (`wikis/cross-links-tier1.md`, domain link pages), but no normalized machine graph manifest.
- Existing reports and validators repeatedly enforce a **no raw/private path leakage** rule; #77 must treat this as a first-class acceptance gate, not a documentation footnote.
- Current frontmatter is **not fully uniform** across domains, so the first graph pass must tolerate missing/variant fields and emit warnings rather than require perfect schema normalization.
- The strongest near-term value is not GraphRAG sophistication; it is a **stable node/edge manifest + gap report** that future issues can consume.

## Problem statement specific to #77

`llm-wiki` has navigable markdown, tier-1 link maps, and per-domain pages, but agents still need to scrape prose ad hoc to answer questions like:

- which standards validate this concept?
- which repo/result link pages operationalize this topic?
- which pages are orphaned or weakly connected?
- which cross-domain bridges exist?
- which topics are blocked by clearance or lack a public result link?

Issue #77 closes that gap by converting committed markdown into a public-safe graph substrate.

## Scope boundaries

### In scope

- Deterministic extraction from committed repo content under `wikis/` plus selected committed docs/link artifacts.
- Node manifest generation for public wiki pages and graph-relevant control artifacts.
- Typed edge extraction from:
  - markdown links
  - wikilinks
  - frontmatter fields such as `cross_links`, `sources`, `code_id`, `publisher`, `supersedes`, and domain/type metadata where present
  - curated link-map pages that explicitly connect wiki topics to repos/results
- JSONL and CSV exports for nodes/edges.
- A human-readable report covering graph gaps:
  - orphan nodes
  - missing backlinks
  - missing code/result links
  - standards metadata gaps
  - cross-domain bridge opportunities
  - overlarge/high-degree nodes if thresholds are exceeded
- Tests and validation for schema, determinism, repo-relative outputs, and no unsafe path leakage.

### Out of scope

- Weekly execution / scheduling / issue-posting automation from [#75](https://github.com/vamseeachanta/llm-wiki/issues/75).
- Root/domain `llms.txt` manifests from [#76](https://github.com/vamseeachanta/llm-wiki/issues/76).
- Retrieval benchmark questions, scorers, or scorecards from [#78](https://github.com/vamseeachanta/llm-wiki/issues/78).
- OSS tool watchlist ingestion from [#79](https://github.com/vamseeachanta/llm-wiki/issues/79).
- CLI query surface or MCP server design from [#80](https://github.com/vamseeachanta/llm-wiki/issues/80).
- Graph database integration, embeddings, community detection, reranking, or online GraphRAG infrastructure.
- Broad frontmatter cleanup across the whole repo; #77 may document normalization gaps but should not absorb schema-remediation epics.
- Parsing raw archives, vendor/client materials, or any non-committed/private source family data.

## Proposed implementation shape

### Recommended artifact contract

Machine artifacts should live under a new repo-local output directory:

- `artifacts/retrieval/public-graph/nodes.jsonl`
- `artifacts/retrieval/public-graph/edges.jsonl`
- `artifacts/retrieval/public-graph/nodes.csv`
- `artifacts/retrieval/public-graph/edges.csv`
- `artifacts/retrieval/public-graph/summary.json`

Human-readable analysis should live under:

- `docs/reports/<date>-public-safe-knowledge-graph-report.md`

This split keeps machine outputs separate from narrative reports while remaining committed and repo-relative.

### Minimal schema recommendation

#### Node fields

- `node_id` — stable repo-relative identifier
- `kind` — `page`, `standard`, `concept`, `entity`, `source`, `comparison`, `workflow`, `index`, `report`, `link_map`, `issue_anchor` (if used)
- `domain` — e.g. `marine-engineering`, `engineering`, `drilling-engineering`
- `path` — repo-relative only
- `title`
- `tags`
- `code_id` — when present
- `publisher` — when present
- `revision` — when present
- `added`
- `last_updated`
- `is_curated`
- `is_public_safe` — always true for emitted nodes; useful as explicit schema field

#### Edge fields

- `edge_id` — deterministic hash or stable concatenation
- `source_node`
- `target_node`
- `relation`
- `evidence_type` — `markdown_link`, `wikilink`, `frontmatter_cross_links`, `frontmatter_sources`, `frontmatter_supersedes`, `derived_domain_bridge`, `link_map_row`
- `evidence_path` — repo-relative page/report path
- `is_cross_domain`
- `is_public_safe`

### Relationship types for phase-1 delivery

Issue #77 names the canonical relationship set. The plan recommends supporting these in phase 1, with clear derivation rules:

- `implements` — wiki topic -> public software/code target, primarily from curated link-map pages
- `validates` — wiki topic -> public result/demo/report target, primarily from code/result link pages and result-oriented reports
- `cites` — page -> source/standard/page via markdown or frontmatter `sources`
- `supersedes` — standard/page -> prior standard/page when frontmatter or prose provides a canonical mapping
- `related-domain` — cross-domain wiki links or derived cross-domain page references
- `source-family` — page/report -> aggregate source-family or provenance grouping only when already represented safely in committed content
- `public-result` — page/topic -> public demo/report/result artifact
- `blocked-by-clearance` — page/topic/report -> issue/governance blocker when an explicit clearance dependency is expressed in committed docs

Note: `blocked-by-clearance` should be limited to explicit public issue/governance references already in committed docs. It must not infer or expose private blockers.

## Implementation phases

### Phase 0 — design freeze and schema selection

- Choose output directory and file names.
- Finalize node/edge schemas.
- Define deterministic ID rules.
- Decide the exact set of graph input surfaces for v1:
  - all `wikis/*/wiki/**/*.md`
  - `wikis/cross-links-tier1.md`
  - selected `docs/reports/*.md` that encode public result / governance relationships
- Explicitly defer GraphML and graph-db adapters until JSONL/CSV are stable.

### Phase 1 — parser and node inventory

- Reuse/adapt regex/link-resolution logic from `scripts/llm_wiki_strengthening_scorecard.py`.
- Enumerate graphable markdown files.
- Extract frontmatter + headings + repo-relative IDs.
- Classify nodes by domain and content type.
- Record missing/variant frontmatter without failing the entire run.

### Phase 2 — typed edge extraction

- Parse markdown links and wikilinks.
- Resolve internal targets repo-relatively.
- Translate known frontmatter fields into typed edges.
- Add specialized extraction for curated link-map pages:
  - `wikis/cross-links-tier1.md`
  - domain code/result link pages
- Mark cross-domain edges and count them separately.

### Phase 3 — graph diagnostics and gap report

- Compute orphan nodes and orphan curated nodes.
- Detect missing backlinks where curated links are one-way.
- Detect standards metadata gaps affecting graph quality.
- Detect pages lacking code/result/public-result coverage where issue text or link-map precedent suggests they should have it.
- Flag overlarge / high-degree nodes using explicit thresholds documented in the report.

### Phase 4 — validator and test hardening

- Add schema validation for output files.
- Add determinism checks for stable node/edge counts on fixture inputs.
- Add no-unsafe-path / no-secret scans over generated artifacts.
- Add targeted seed expectations for marine/engineering/standards examples.

### Phase 5 — documentation and operator contract

- Document generation command using `uv run python ...`.
- Document output locations and intended downstream consumers.
- State explicitly that #77 is a metadata graph, not a raw-content index or retrieval benchmark.

## File map

### New files expected during implementation

- `scripts/generate_public_graph_manifests.py` — main generator CLI
- `scripts/validate_public_graph_manifests.py` — artifact validator
- `tests/test_public_graph_manifests.py` — graph-generation/unit regression tests
- `tests/fixtures/public_graph_fixture/` — minimal deterministic markdown fixture corpus for node/edge expectations
- `artifacts/retrieval/public-graph/nodes.jsonl`
- `artifacts/retrieval/public-graph/edges.jsonl`
- `artifacts/retrieval/public-graph/nodes.csv`
- `artifacts/retrieval/public-graph/edges.csv`
- `artifacts/retrieval/public-graph/summary.json`
- `docs/reports/2026-05-15-public-safe-knowledge-graph-report.md` or implementation-date equivalent

### Existing files likely to be referenced or modestly updated

- `README.md` — only if the repo should advertise the graph artifacts/command
- `scripts/llm_wiki_strengthening_scorecard.py` — optional shared helper extraction, but avoid unnecessary coupling
- `tests/test_completion_artifacts.py` — only if a new validator pattern should be included in the existing artifact-governance test suite

### Existing files that should remain untouched by #77 unless absolutely necessary

- domain wiki content under `wikis/*/wiki/` except where a tiny seed-fix is explicitly approved later
- issue plans unrelated to #77
- weekly/reporting automation for #75
- any `llms.txt` or MCP/query-surface artifacts for #76/#80

## Tests and validation plan

### Generator command

Preferred operator command:

- `uv run python scripts/generate_public_graph_manifests.py`

### Validation command

- `uv run python scripts/validate_public_graph_manifests.py`

### Test command

- `uv run pytest tests/test_public_graph_manifests.py -q`

### Required test coverage

1. **Node schema test** — every node has required fields and repo-relative `path`.
2. **Edge schema test** — every edge has required fields, allowed `relation`, and repo-relative `evidence_path`.
3. **Determinism test** — fixture corpus emits stable counts and IDs.
4. **Link resolution test** — markdown links and wikilinks resolve correctly across folders/domains.
5. **Seed relationship test** — at least one expected relationship each for:
   - marine/engineering implementation/result links
   - drilling/standards concept references
   - cross-domain standards bridge
6. **Orphan detection test** — known fixture orphan is reported.
7. **Safety scan test** — generated outputs do not contain forbidden private path patterns, secrets, or non-repo-relative local paths.
8. **Large-node threshold test** — summary/report flags nodes exceeding configured edge-degree threshold.

### Validation rules

The validator should fail if any generated artifact contains:

- `/mnt/ace/` or similar raw/private subpaths
- secrets/credential patterns analogous to `scripts/validate_completion_artifacts.py`
- absolute local filesystem paths
- missing output files
- disallowed relation names
- edges pointing to unresolved non-public targets

## Public-safety / secrets constraints

This issue is explicitly public-safe only if all outputs remain metadata-only and repo-relative.

### Allowed

- Repo-relative page paths
- Public GitHub URLs already present in committed docs
- Frontmatter metadata such as `code_id`, `publisher`, `revision`, `tags`, `added`, `last_updated`
- Link-derived relationships between already-public pages and public repos/results
- Aggregate counts and diagnostics

### Forbidden

- Raw/private archive paths or path-rich manifests
- Copied standards clauses, tables, formulas, or vendor text
- Client/project identifiers
- Credentials, tokens, or secret-like strings
- Parsing uncommitted local files outside the repo
- Graph nodes representing private source families unless they are already abstracted safely in committed docs

### Public-safety implementation notes

- Treat `/mnt/ace` only as a prohibited raw-root pattern except where existing governance docs mention the safe root label in prose.
- Prefer extracting from committed wiki/report pages rather than from raw source inventories.
- If a graph edge would require opening a private source or inferring a hidden target, drop it and record a warning instead.

## Risks

1. **Frontmatter drift risk** — field shapes vary across domains (`cross_links`, `supersedes`, extra standards metadata). Mitigation: tolerant parser + warning counters + fixture coverage.
2. **Over-scope risk** — GraphRAG ambitions could drag #77 into retrieval benchmarking, llms manifests, or MCP design. Mitigation: hold v1 to manifest generation + validation + report only.
3. **False precision risk** — some relationship types (especially `implements`, `validates`, `blocked-by-clearance`) can be over-inferred from prose. Mitigation: only derive typed edges from explicit links/structured fields/documented curated link maps.
4. **Safety leakage risk** — generated artifacts may accidentally preserve unsafe paths from future content. Mitigation: dedicated validator + tests scanning generated outputs.
5. **Repo-noise risk** — full-corpus graph outputs may be large and churny. Mitigation: document stable ordering and consider compressed/summary-friendly structure; if needed, split report from machine outputs.
6. **Coupling risk** — reusing scorecard parser logic too tightly may make both tools harder to evolve. Mitigation: extract shared helpers only if clearly beneficial.

## Acceptance criteria mapping

### Issue acceptance criterion 1

> A reproducible command generates `docs/reports/` or `artifacts/` graph outputs from `wikis/`.

Planned satisfaction:

- `uv run python scripts/generate_public_graph_manifests.py`
- emits node/edge artifacts under `artifacts/retrieval/public-graph/`
- emits human-readable report under `docs/reports/`

### Issue acceptance criterion 2

> Tests assert graph schema, edge counts, no unsafe paths, and expected seed relationships for marine/engineering/standards pages.

Planned satisfaction:

- `tests/test_public_graph_manifests.py`
- validator command for path/secret scanning
- fixture-based seed relationship assertions grounded in inspected link-map and standards pages

### Issue acceptance criterion 3

> A human-readable report lists top gaps: orphan nodes, missing code/result links, standards metadata gaps, and domain bridge opportunities.

Planned satisfaction:

- `docs/reports/<date>-public-safe-knowledge-graph-report.md`
- required sections: orphan nodes, missing backlinks, code/result gaps, standards metadata gaps, cross-domain bridge opportunities, high-degree node warnings

### Issue acceptance criterion 4

> Output can be consumed by future RAG/MCP tooling without scraping markdown ad hoc.

Planned satisfaction:

- normalized JSONL/CSV schemas
- deterministic IDs and repo-relative targets
- explicit documentation that #78 and #80 should consume these artifacts rather than rescrape prose

## Dependencies

### Hard dependencies / constraints

- Existing public-safety contract from:
  - `docs/plans/README.md`
  - `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md`
  - `scripts/validate_completion_artifacts.py`
- Existing markdown parsing/link-resolution precedent from `scripts/llm_wiki_strengthening_scorecard.py`

### Soft dependencies / coordination

- [#37](https://github.com/vamseeachanta/llm-wiki/issues/37) scorecard work — useful precedent for deterministic corpus analytics
- [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) freshness loop — should consume graph outputs later, not be implemented here
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) `llms.txt` manifests — should link to graph/report artifacts later, not block #77
- [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) retrieval benchmark — should use #77 outputs as retrieval substrate
- [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) CLI/MCP surface — should wait for stable #77 schema
- [#19](https://github.com/vamseeachanta/llm-wiki/issues/19) and clearance/governance issues [#43](https://github.com/vamseeachanta/llm-wiki/issues/43)-[#48](https://github.com/vamseeachanta/llm-wiki/issues/48) — define what remains blocked-by-clearance, but #77 must only reference already-public blocker evidence

## Follow-up issues likely needed after #77

These should be separate issues unless already covered:

1. **Frontmatter normalization pass** — if `cross_links` / `supersedes` drift materially reduces graph quality.
2. **Graph consumer docs / CLI queries** — likely folded into [#80](https://github.com/vamseeachanta/llm-wiki/issues/80).
3. **Benchmark integration** — likely folded into [#78](https://github.com/vamseeachanta/llm-wiki/issues/78).
4. **Weekly graph delta reporting** — likely folded into [#75](https://github.com/vamseeachanta/llm-wiki/issues/75).
5. **`llms.txt` references to graph artifacts** — likely folded into [#76](https://github.com/vamseeachanta/llm-wiki/issues/76).

No new follow-up issue should be opened during #77 planning itself unless the main agent explicitly chooses to do so later.

## Recommended sequencing

1. Approve this plan.
2. Implement parser + node inventory with no output writes beyond fixture tests.
3. Add typed edges for explicit links/frontmatter only.
4. Add report + validator.
5. Run tests and validation.
6. Only after #77 stabilizes, let #78 and #80 consume the artifacts.

## Complexity

**T2** — moderate repo-local tooling work with meaningful schema and safety design, but bounded to committed markdown analysis and deterministic artifact generation. This is more substantial than a pure docs issue, but far smaller than a new domain-founding corpus build.

## Approval recommendation

**Approval-ready for implementation after review**, with two cautions to preserve scope discipline:

1. lock v1 to JSONL/CSV + report; do not expand into GraphML/MCP/RAG benchmark work;
2. enforce a strict explicit-evidence rule for typed edges so the first graph is trustworthy and public-safe.
