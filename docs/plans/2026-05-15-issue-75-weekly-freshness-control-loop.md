---
title: "Issue #75 plan — weekly freshness control loop for concepts, coverage, and issue recommendations"
issue: 75
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: metadata-only repo health + public OSS concept watchlist; no raw/vendor/client/private path leakage
---

# Issue #75 Plan — Weekly Freshness Control Loop

## Summary
Issue [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) should establish a **weekly, public-safe operations loop** for `llm-wiki` that does four things in one reproducible run:

1. measures repository freshness and coverage drift from committed `wikis/` content,
2. flags stale or structurally weak pages/domains,
3. tracks a small curated watchlist of external concepts relevant to `llm-wiki` operations,
4. emits deduplicated issue recommendations tied back to roadmap anchor [#13](https://github.com/vamseeachanta/llm-wiki/issues/13).

This plan is intentionally **control-plane only**. It does not implement `llms.txt`, graph retrieval, RAG benchmarks, OSS tool crawling, or MCP surfaces directly; those remain separate issues [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) through [#80](https://github.com/vamseeachanta/llm-wiki/issues/80). #75 should consume their status as dependencies and report on them, not absorb their implementation scope.

## Gate status
- GitHub issue: [vamseeachanta/llm-wiki#75](https://github.com/vamseeachanta/llm-wiki/issues/75)
- Local plan status: `plan-review`
- Implementation status: not started
- Approval rule: do not implement until adversarial review is complete and the issue has explicit user approval for execution.

## Current evidence / intelligence

### GitHub issues inspected live
1. [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) — target issue; defines weekly cadence, report content, local `uv run` requirement, and tests for stale-page detection, frontmatter counts, and duplicate-issue suggestions.
2. [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — durable roadmap anchor; #75 must link recommendations back here rather than inventing a replacement umbrella.
3. [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — `llms.txt` entrypoints; dependency/input only.
4. [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — graph/link-graph manifests; dependency/input only.
5. [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — RAG evaluation benchmark; dependency/input only.
6. [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — OSS engineering-tool watchlist; dependency/input only.
7. [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — CLI/MCP query surface; dependency/input only.

### Repository files inspected
1. `README.md` — confirms `llm-wiki` is the public content storehouse while orchestration remains in `workspace-hub`; supports keeping #75 repo-local and metadata-only.
2. `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` — defines practical completion, raw/private boundary, and explicit instruction to use #13 as the durable roadmap anchor.
3. `docs/reports/llm-wiki-strengthening-scorecard.md` — existing deterministic scorecard already computes actionable freshness-adjacent signals by domain.
4. `docs/reports/llm-wiki-strengthening-scorecard.json` — machine-readable domain totals and freshness metrics suitable as seed inputs.
5. `scripts/llm_wiki_strengthening_scorecard.py` — existing repo-local metric engine already calculates page counts, missing frontmatter, missing index entries, orphan curated pages, and `freshness_days` by domain.
6. `scripts/validate_completion_artifacts.py` — existing validation pattern for public-safe control-plane artifacts.
7. `tests/test_completion_artifacts.py` — existing test style for artifact validators.
8. `docs/plans/README.md` — confirms plan-review gate language and public-safety defaults for issue plans.
9. `docs/plans/2026-05-15-issue-73-pe-phase-2-completions.md` — recent plan structure reference for frontmatter and gating conventions.

### Concrete intelligence gathered from current artifacts
- The current scorecard covers **8 domains**, **19,769 markdown content pages**, and already exposes domain-level `freshness_days`, missing frontmatter counts, missing index counts, and orphan curated-page counts.
- `scripts/llm_wiki_strengthening_scorecard.py` already contains reusable logic for:
  - frontmatter detection,
  - domain iteration,
  - page counting,
  - link analysis,
  - `last_updated` parsing and `freshness_days` inference.
- Existing validators and tests are artifact-focused and dependency-light, which matches #75’s requirement that the weekly loop run locally via `uv run` without relying on private orchestration.
- The issue portfolio already separates adjacent work into #76-#80, so #75 should operate as a **weekly reporting/control loop over existing and future artifacts**, not as a replacement for those feature lanes.

## Problem statement refined for #75
The repo has good one-shot scorecards and completion-planning artifacts, but not yet a **repeatable weekly control loop** that turns repo metrics plus concept-watch inputs into a single Markdown report and actionable issue recommendations. The gap is operational cadence, not raw content generation.

## Scope boundaries

### In scope
- Weekly report artifact under `docs/reports/` with a deterministic filename/date pattern.
- Local script/CLI runnable with `uv run` that reads committed public repo content only.
- Repo-health metrics for:
  - domain page counts,
  - missing frontmatter,
  - stale `last_updated`,
  - broken internal markdown links,
  - orphan curated pages / low-link-density indicators,
  - open-issue recommendation candidates deduplicated against known roadmap lanes.
- A curated external concept watchlist section in the report covering only public-safe summaries/links relevant to #75’s body: `llms.txt`, MCP, GraphRAG/LightRAG, and RAG evaluation.
- Recommendation output tied to #13 and to existing open issue lanes where appropriate.

### Explicitly out of scope
- Implementing repo-wide `llms.txt` manifests themselves — belongs to #76.
- Generating graph/link-graph exports — belongs to #77.
- Building the benchmark/eval harness — belongs to #78.
- Running a broad external OSS tool-update crawler — belongs to #79.
- Implementing CLI/MCP serving/query interfaces — belongs to #80.
- Any raw `/mnt/ace` scanning, vendor-derivative publication, copied standards text, or client/private corpus access.
- Any scheduled GitHub Actions / cron deployment beyond planning the local command contract.

## Proposed implementation approach

### Phase 1 — Lock the data contract for the weekly report
Define a deterministic report schema so weekly runs produce the same sections every time:
1. run metadata (`date`, generator, issue link, public-safety note),
2. repo freshness summary,
3. domain coverage deltas,
4. stale-page / metadata / broken-link findings,
5. concept watchlist notes,
6. open-issue recommendation table,
7. blocked / approval-gated lanes,
8. validation evidence and command transcript.

Key design choice: use the existing scorecard as an input, not a replacement. #75 should either call shared logic from `scripts/llm_wiki_strengthening_scorecard.py` or extract reusable helpers into a shared module, but should avoid re-implementing the same counting rules twice.

### Phase 2 — Add repo-local freshness analyzers
Implement deterministic analyzers for the acceptance criteria explicitly named in #75:
- **stale-page detection**: compute pages older than a configurable threshold from `last_updated` frontmatter;
- **frontmatter aggregation**: count pages with/without frontmatter by domain and repo-wide;
- **broken internal links**: validate repo-relative `.md` links and optionally wikilink targets where unambiguous;
- **coverage drift summary**: compare current totals to the previous weekly report or current scorecard JSON snapshot when available.

Recommendation: keep thresholds configurable via CLI flags with safe defaults, e.g. `--stale-days 30` and `--max-report-items N`.

### Phase 3 — Add issue recommendation logic
Generate recommendation rows from deterministic findings instead of free-form prose.

Recommendation buckets:
- **use existing issue** when a finding maps cleanly to an open issue like #20/#21/#27/#28/#29/#30/#38/#39 or #76-#80;
- **recommend update/comment on #13** when the item is portfolio-wide or cross-cutting;
- **recommend new issue** only when no open issue covers the finding and the recommendation is specific, non-duplicative, and public-safe.

Deduplication contract:
- normalize candidate titles/slugs,
- compare against a maintained allowlist/map of known open issue themes,
- never auto-open issues from #75’s first implementation scope; only recommend.

### Phase 4 — Emit a public-safe weekly report artifact
Generate a dated artifact such as:
- `docs/reports/2026-05-15-llm-wiki-weekly-freshness-report.md`

The report should include exact command lines used for reproduction and link back to #13 plus any relevant open issue(s). If external concept-watch updates are included, they must remain summary/link-level only.

### Phase 5 — Add validators and tests
Add focused tests for the weekly-control-loop logic and validator coverage for report safety/content contract.

## File map

### Existing files likely to modify
- `scripts/llm_wiki_strengthening_scorecard.py`
  - reuse or extract metric helpers already computing freshness/count/link signals.
- `README.md`
  - document the weekly freshness command and artifact location after implementation.
- `docs/plans/README.md`
  - optional only if the new plan should be indexed there during implementation closeout.

### New files likely to add
- `docs/reports/<run-date>-llm-wiki-weekly-freshness-report.md`
  - generated weekly report artifact.
- `scripts/llm_wiki_weekly_freshness.py`
  - primary CLI/report generator for #75.
- `scripts/validate_weekly_freshness_report.py`
  - validator for required sections, issue links, and public-safety scan.
- `tests/test_llm_wiki_weekly_freshness.py`
  - unit tests for stale-page detection, frontmatter aggregation, broken-link handling, and issue recommendation deduplication.
- `tests/test_weekly_freshness_artifacts.py`
  - artifact-validator regression tests.
- `tests/fixtures/weekly-freshness/`
  - small synthetic markdown corpus for deterministic stale/frontmatter/link/recommendation tests.

### Optional refactor path if needed
- `scripts/_llm_wiki_metrics.py`
  - shared metric helpers if scorecard and weekly report need common logic without code duplication.

## Tests and validation plan

### Unit/integration tests to add
1. **stale-page detection**
   - identifies pages older than threshold,
   - ignores malformed/missing `last_updated` safely,
   - preserves deterministic ordering of reported stale pages.
2. **frontmatter count aggregation**
   - counts per-domain and repo-wide totals correctly,
   - distinguishes missing frontmatter from missing `last_updated`.
3. **broken internal link detection**
   - flags missing repo-relative markdown targets,
   - does not fail on external `http(s)` links.
4. **duplicate-issue suggestion logic**
   - routes covered findings to existing issue IDs,
   - suppresses duplicate “new issue” recommendations when a mapped open issue already exists.
5. **artifact validation**
   - report includes required sections, #13 link, and public-safety language,
   - report fails if it contains forbidden private paths or secret-like tokens.

### Expected local validation commands
- `uv run pytest tests/test_llm_wiki_weekly_freshness.py tests/test_weekly_freshness_artifacts.py -q`
- `uv run python scripts/llm_wiki_weekly_freshness.py --date YYYY-MM-DD --output docs/reports/YYYY-MM-DD-llm-wiki-weekly-freshness-report.md`
- `uv run python scripts/validate_weekly_freshness_report.py docs/reports/YYYY-MM-DD-llm-wiki-weekly-freshness-report.md`

### Reuse of existing checks
Where practical, #75 implementation should preserve compatibility with existing scorecard/control-plane checks rather than introducing a second inconsistent metric vocabulary.

## Public-safety / secrets constraints
- Use committed repo content only; do not traverse or publish raw/private corpora.
- Do not include `/mnt/ace` subpaths, private manifests, vendor PDF filenames, copied standards clauses/tables, client names, credential-like strings, or workspace-private memory.
- External concept-watch notes must be **summary + public URL/reference only**.
- Recommendation text must stay repo-operational and not reveal blocked private inputs.
- If future work integrates GitHub API reads for open issues, responses should be reduced to public issue metadata only.

## Risks
1. **Metric duplication drift**
   - Risk: weekly script and scorecard diverge in how they count pages or freshness.
   - Mitigation: share helpers or make the weekly script consume scorecard JSON/output.
2. **Overlapping adjacent issues**
   - Risk: #75 accidentally absorbs implementation from #76-#80.
   - Mitigation: constrain #75 to reporting on those lanes, not building them.
3. **False-positive issue recommendations**
   - Risk: recommendation engine suggests opening issues already covered by existing open work.
   - Mitigation: maintain explicit mapping to known issue IDs and require deterministic dedup rules.
4. **Noise from huge domains**
   - Risk: marine-engineering scale overwhelms weekly reports with low-value detail.
   - Mitigation: cap examples and report summarized counts plus top-N offenders.
5. **Missing historical baseline**
   - Risk: first weekly run lacks prior delta comparison.
   - Mitigation: allow baseline mode that reports absolute metrics on week 1 and enables deltas once a prior artifact exists.

## Acceptance criteria mapping

| Issue #75 acceptance criterion | Plan response |
|---|---|
| Weekly run produces a public-safe markdown report with repo freshness, concept watchlist, domain completion deltas, issue recommendations, and blocked/approval-gated lanes | Covered by report schema in Phases 1-4 and validator coverage in Phase 5 |
| Report links to #13 and any newly opened/updated issues | #13 is mandatory in validator; other issue links come from recommendation mapping/output |
| Workflow runnable locally with `uv run ...` and suitable for later cron/job scheduling | CLI contract and validation commands are explicitly local-first and dependency-light |
| Tests cover stale-page detection, frontmatter count aggregation, and duplicate-issue suggestion logic | Explicitly required in `tests/test_llm_wiki_weekly_freshness.py` |

## Dependencies and coordination

### Hard dependencies
- None for initial local implementation; #75 can ship with an internal curated concept watchlist and repo-local metrics.

### Soft dependencies / coordination points
- [#13](https://github.com/vamseeachanta/llm-wiki/issues/13): roadmap anchor for posting/reporting recommendations.
- [#37](https://github.com/vamseeachanta/llm-wiki/issues/37): scorecard logic is the best existing metric substrate and should be reused.
- [#20](https://github.com/vamseeachanta/llm-wiki/issues/20), [#21](https://github.com/vamseeachanta/llm-wiki/issues/21), [#27](https://github.com/vamseeachanta/llm-wiki/issues/27), [#28](https://github.com/vamseeachanta/llm-wiki/issues/28), [#29](https://github.com/vamseeachanta/llm-wiki/issues/29), [#30](https://github.com/vamseeachanta/llm-wiki/issues/30), [#38](https://github.com/vamseeachanta/llm-wiki/issues/38), [#39](https://github.com/vamseeachanta/llm-wiki/issues/39): likely existing lanes for many weekly findings.
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) through [#80](https://github.com/vamseeachanta/llm-wiki/issues/80): weekly report should treat them as tracked recommendation categories/dependencies, not as work to absorb.

## Follow-up issues
- **No immediate new follow-up issue is required at planning time.**
- If implementation reveals a clearly separate concern, the only justified split would be a narrow validator/CI issue for scheduled publication plumbing; that should be created only if the local-first implementation becomes too large or if scheduling concerns threaten to blur #75’s reporting scope.

## Adversarial review synthesis and accepted hardening

Three independent plan reviews completed on 2026-05-15. Consensus verdict: **MINOR**. The plan is approval-candidate quality only with the following clarifications treated as binding implementation contract.

### Accepted changes from review
- **Machine-readable companion required:** every weekly run must emit both:
  - `docs/reports/<run-date>-llm-wiki-weekly-freshness-report.md`
  - `artifacts/freshness/<run-date>-weekly-freshness-summary.json`
- **Baseline source is fixed:** first run is absolute baseline; later runs compare only against the previous JSON artifact with the same schema version. Do not mix prior Markdown parsing with scorecard snapshots for week-over-week deltas.
- **Repo-local default:** v1 does not fetch network data. The concept-watch section uses a checked-in curated config/summary and public URLs only; live concept/tool monitoring remains #79 scope.
- **Issue-routing source is checked in:** deduplication uses a versioned mapping file such as `data/issue_routing_map.json`; live GitHub issue reads are optional enrichment only and must not be required for tests.
- **Bounded output:** stale pages, broken links, and recommendations must support top-N caps and deterministic sorting to prevent marine-scale report explosions.
- **Confidence/reason codes:** recommendation rows must include a stable reason code and confidence tier, not only prose.

### Revised data contract
Minimum JSON fields:
- `schema_version`
- `run_date`
- `baseline_run_date`
- `repo_totals`
- `domain_freshness[]`
- `stale_pages[]`
- `broken_links[]`
- `recommendations[]` with `issue_route`, `reason_code`, `confidence`, and `public_safe_summary`
- `validation` command/evidence fields

### Residual risk
Low. Remaining risk is implementation discipline: keep #75 as a control/reporting loop and do not absorb #76-#80 feature work.

## Approval-gate note
This plan is review-ready for the standard `plan-review` gate only. It is **not** implementation approval. Before execution:
1. complete adversarial review,
2. confirm the plan still avoids overlap with #76-#80,
3. obtain explicit user approval,
4. then move to implementation via TDD with repo-local `uv run` commands.

## Recommended implementation sequence after approval
1. extract/reuse scorecard metric helpers,
2. add stale/frontmatter/link analyzers,
3. add issue recommendation mapping + dedup logic,
4. generate first weekly report artifact,
5. add validator and tests,
6. document the local run command in `README.md`.

## Complexity
**T2** — moderate repo-local automation/reporting task with deterministic test surface and meaningful scope boundaries, but without external service deployment or raw-data access.