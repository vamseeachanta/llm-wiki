---
title: "Issue #79 plan — weekly OSS engineering-tool watchlist and update candidates"
issue: 79
status: plan-approved
created: 2026-05-15
last_updated: 2026-05-15
public_safety: public upstream metadata, repo-relative links, and summary-only update notes; no vendored code/docs, private paths, or secret-bearing automation
---

# Issue #79 Plan — Weekly OSS Engineering-Tool Watchlist and Update Candidates

## Summary
Issue [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) should add a **small, public-safe weekly watchlist system** for priority OSS engineering tools so `llm-wiki` can notice upstream changes and recommend wiki updates without copying upstream code or documentation.

The first implementation should stay deliberately narrow:

1. maintain a structured watchlist manifest for priority tools;
2. run a local `uv run` scan that checks public change signals only;
3. emit a dated markdown delta report with candidate wiki updates;
4. deduplicate recommendations against open `llm-wiki` issues;
5. keep all output metadata/link/summary level only.

This issue is about **monitoring and recommendation generation**, not building the weekly master control loop, not authoring `llms.txt`, not generating graph manifests, not building a benchmark harness, and not exposing MCP/CLI retrieval services.

## Gate status
- GitHub issue: [vamseeachanta/llm-wiki#79](https://github.com/vamseeachanta/llm-wiki/issues/79)
- Local plan state: `plan-review`
- Implementation status: not started
- Approval rule: do not implement until plan review is complete and explicit user approval is given for execution.

## Current evidence / intelligence

### Issues inspected live
1. [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — target issue; requires a structured watchlist, a human-readable report, weekly scan/delta behavior, and open-issue deduplication.
2. [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap umbrella; #79 should remain a child lane and feed recommendations back to this steering surface instead of creating a new umbrella.
3. [#37](https://github.com/vamseeachanta/llm-wiki/issues/37) — completed strengthening scorecard; provides the strongest existing pattern for deterministic repo-local reporting and prioritized next actions.
4. [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — RAG benchmark lane; relevant only as a downstream consumer of better OSS-tool coverage, not as scope to absorb.
5. [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — future CLI/MCP access lane; relevant only as a consumer of watchlist artifacts, not part of #79 implementation.

### Repository files inspected
1. `README.md` — confirms `llm-wiki` is the public content storehouse and that orchestration stays lightweight/repo-local here.
2. `docs/plans/README.md` — confirms the `plan-review` gate and public-safety defaults for plan artifacts.
3. `docs/plans/2026-05-15-issue-75-weekly-freshness-control-loop.md` — important overlap boundary: #75 owns the overall weekly control loop and should consume #79 outputs rather than be reimplemented here.
4. `docs/plans/2026-05-15-issue-76-llms-entrypoints-domain-manifests.md` — overlap boundary: #76 owns agent entry manifests, not upstream tool monitoring.
5. `docs/plans/2026-05-15-issue-77-public-safe-knowledge-graph.md` — overlap boundary: #77 owns graph manifests and graph diagnostics, not tool-watch scanning.
6. `docs/reports/2026-05-11-tier1-practical-completeness-gap-report.md` — names OSS tooling seed pages for MoorDyn, MoorPy, Gmsh, OpenFAST, HAMS, WEC-Sim, Capytaine, and OPM as safe next artifacts.
7. `docs/reports/2026-05-11-llm-wiki-practical-completion-roadmap.md` — identifies the software layer, low-risk OSS candidate families, and “complete enough” coverage expectations for public OSS tool pages.
8. `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` — defines the raw/private boundary and the rule to publish only public-safe synthesis and links for OSS/public software folders.
9. `wikis/engineering/wiki/public-data-software-links.md` — existing public-link index pattern for repo/software linkage.
10. `wikis/engineering/wiki/entities/openfoam-cfd.md` — concrete example of an existing OSS tool page already in the wiki.
11. `wikis/engineering/wiki/entities/bemrosetta-tool.md` — concrete example of a tool page that exists today but is not fed by any watchlist/update lane.
12. `scripts/llm_wiki_strengthening_scorecard.py` — current deterministic reporting substrate and likely style reference for a new repo-local watchlist scanner.
13. `scripts/validate_completion_artifacts.py` — current validator pattern for public-safe report contracts.
14. `tests/test_completion_artifacts.py` — current regression-test style for artifact validation.

### Concrete evidence gathered
- The issue body already enumerates the initial watchlist shape: upstream URL, docs URL, domain, local tier-1 repo link, wiki page target, last checked, and change signal.
- The repo already has public-safe link index patterns, but no dedicated OSS-tool watchlist manifest or weekly scanner in `scripts/`.
- Existing tool coverage is partial:
  - confirmed present by file: `wikis/engineering/wiki/entities/openfoam-cfd.md`
  - confirmed present by file: `wikis/engineering/wiki/entities/bemrosetta-tool.md`
  - not found as wiki filenames during inspection: `MoorDyn`, `MoorPy`, `OpenFAST`, `Capytaine`, `HAMS`, `WEC-Sim`, `Gmsh`, `FreeCAD`, `ParaView`, `PyVista`, `OPM`
- The gap report and roadmap both explicitly call OSS tooling pages a safe growth lane, so #79 has a clear strategic role without needing raw/private inputs.
- The current script inventory is small and deterministic (`llm_wiki_strengthening_scorecard.py`, validators, tests), which is a good precedent: #79 should remain local-first and dependency-light.

## Problem statement refined for #79
`llm-wiki` has seed evidence that OSS engineering tools are a high-value, low-risk expansion lane, but it lacks a repeatable mechanism for:

1. tracking which upstream OSS tools matter most,
2. checking those tools on a weekly cadence,
3. identifying whether a change is worth a wiki update, and
4. avoiding duplicate issue churn when a related lane is already open.

The missing capability is a **public-safe monitoring and recommendation loop for engineering-tool sources**, not full retrieval infrastructure or full wiki-page generation.

## Scope boundaries

### In scope
- A structured watchlist manifest for the priority OSS tools named in #79, with room for later additions.
- Public metadata fields per tool such as:
  - tool name,
  - owner/repo,
  - upstream URL,
  - docs URL,
  - wiki target path,
  - related tier-1 repo(s),
  - domain,
  - status/tier,
  - last checked,
  - last seen release/docs signal.
- A local `uv run` scan command that checks public change signals only, such as:
  - latest release/tag metadata,
  - default-branch docs/reference URLs,
  - public issue/discussion pointers only if deliberately scoped and rate-safe.
- A dated markdown delta report under `docs/reports/` summarizing:
  - tools checked,
  - what changed,
  - candidate wiki updates,
  - duplicate/open-issue routing guidance,
  - blocked/noise/unknown cases.
- Deduplication against open `llm-wiki` issues so the scan recommends “reuse existing issue” when appropriate.
- Linkage to existing wiki pages and tier-1 repos where public and applicable.

### Explicitly out of scope
- Building the master weekly freshness/control loop — belongs to [#75](https://github.com/vamseeachanta/llm-wiki/issues/75).
- Authoring `llms.txt` manifests — belongs to [#76](https://github.com/vamseeachanta/llm-wiki/issues/76).
- Generating knowledge-graph exports/manifests — belongs to [#77](https://github.com/vamseeachanta/llm-wiki/issues/77).
- Building a retrieval benchmark harness — belongs to [#78](https://github.com/vamseeachanta/llm-wiki/issues/78).
- Implementing MCP or query CLI serving surfaces — belongs to [#80](https://github.com/vamseeachanta/llm-wiki/issues/80).
- Creating or bulk-updating the actual wiki tool pages for every watchlisted tool in the first pass.
- Vendoring upstream source trees, scraping/copying docs bodies, or mirroring release notes wholesale.
- Editing GitHub labels/comments or auto-opening issues as part of the first implementation scope.

## Proposed implementation phases

### Phase 1 — Define the watchlist contract
Create a canonical machine-readable schema for the watchlist before any scanner logic is added.

Required first-pass fields should include:
- `name`
- `slug`
- `owner`
- `repo`
- `upstream_url`
- `docs_url`
- `domain`
- `tier1_repo_links`
- `wiki_target`
- `watch_signals`
- `last_checked`
- `last_seen_version`
- `last_seen_release_date`
- `last_seen_signal_summary`
- `status`

Design rule: the manifest should be human-editable, deterministic, and explicit enough that later reports can explain *why* a tool was considered changed.

### Phase 2 — Seed the initial priority watchlist
Populate at least the issue-required first set, prioritizing the tools already called out in the issue and related reports:
- MoorDyn
- MoorPy
- OpenFAST
- Capytaine
- HAMS
- WEC-Sim
- OPM
- OpenFOAM
- Gmsh
- FreeCAD
- ParaView
- PyVista
- BEMRosetta

The seeded manifest should distinguish between:
- tools with an existing wiki target page,
- tools that have only indirect references today,
- tools with no current page and therefore only a candidate target path.

### Phase 3 — Implement the weekly public-signal scanner
Add a repo-local script that reads the manifest and queries public sources only.

Recommended first-pass signal hierarchy:
1. GitHub releases/tags when a tool has a stable GitHub upstream.
2. Docs homepage/version page timestamp or version marker when releases are absent or noisy.
3. Optional public issue/discussion signal only if it is low-noise and clearly useful.

The scanner should emit normalized per-tool statuses such as:
- `no_change`
- `new_release`
- `docs_changed`
- `candidate_page_missing`
- `signal_unavailable`
- `manual_review`

Key constraint: #79 should produce *recommendations*, not direct wiki-content synthesis.

### Phase 4 — Add issue-deduplicated update recommendations
Convert scan results into action rows such as:
- update existing wiki page,
- create initial seed page,
- link tool into an existing cross-link/index page,
- reuse an existing open issue,
- defer to another lane (#75/#76/#77/#78/#80),
- no action.

Deduplication policy should prefer:
1. existing open issue mapping,
2. roadmap anchor [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) for portfolio-wide notes,
3. a “recommend new issue” row only when no open lane covers the work.

### Phase 5 — Emit a dated watchlist report artifact
Generate a reproducible markdown artifact such as:
- `docs/reports/YYYY-MM-DD-oss-engineering-tool-watchlist.md`

Recommended report sections:
1. run metadata and safety note,
2. tools checked and signal sources,
3. detected changes,
4. candidate wiki updates,
5. duplicate/open-issue routing,
6. blocked/manual-review items,
7. validation evidence.

### Phase 6 — Add validator and tests
Add focused validation and test coverage so the artifact stays public-safe and deterministic.

## File map

### Existing files likely to modify
- `README.md`
  - document the watchlist command and artifact location after implementation.
- `scripts/llm_wiki_strengthening_scorecard.py`
  - optional only if shared helpers or coordinated report references are useful; avoid unnecessary coupling.
- `docs/plans/README.md`
  - optional plan-index update during later closeout, not required for first implementation.

### New files likely to add
- `data/oss_tool_watchlist.yaml`
  - canonical watchlist manifest.
- `scripts/llm_wiki_oss_tool_watchlist.py`
  - local scanner/report generator for #79.
- `scripts/validate_oss_tool_watchlist.py`
  - validator for manifest schema, report sections, allowed URL/source patterns, and public-safety checks.
- `docs/reports/<run-date>-oss-engineering-tool-watchlist.md`
  - weekly human-readable delta report.
- `tests/test_oss_tool_watchlist.py`
  - unit tests for manifest loading, signal normalization, candidate generation, and issue deduplication.
- `tests/test_oss_tool_watchlist_artifacts.py`
  - validator regression tests for report and manifest safety/structure.
- `tests/fixtures/oss_tool_watchlist/`
  - small deterministic upstream-response fixtures and sample manifests.

### Optional support files if the implementation benefits from separation
- `data/oss_tool_issue_map.yaml`
  - explicit mapping from tool/update categories to existing issue IDs or routing buckets.
- `scripts/_oss_watchlist_common.py`
  - shared helper utilities if the script grows beyond a single clear file.

## Tests and validation plan

### Unit/integration tests to add
1. **manifest schema/load test**
   - at least 10 priority tools exist,
   - each has owner/repo/docs/version/check fields required by the issue,
   - wiki target fields are present even when the page is only a candidate.
2. **signal detection normalization**
   - release-like upstream input becomes `new_release`,
   - docs/version drift becomes `docs_changed`,
   - unavailable upstream becomes `signal_unavailable`,
   - missing local wiki page becomes `candidate_page_missing` when relevant.
3. **issue deduplication**
   - findings route to existing issue IDs when mapped,
   - recommendations do not emit duplicate “new issue” suggestions for already covered work.
4. **report validation**
   - required sections are present,
   - issue [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) is linked where portfolio routing is discussed,
   - forbidden private-path or secret-like patterns are rejected.
5. **public-source allowlist behavior**
   - report and manifest contain only approved public URLs/repo-relative paths,
   - no local raw/private paths or vendored excerpts appear.

### Expected local validation commands
```bash
uv run pytest tests/test_oss_tool_watchlist.py tests/test_oss_tool_watchlist_artifacts.py -q
uv run python scripts/llm_wiki_oss_tool_watchlist.py --date YYYY-MM-DD --output docs/reports/YYYY-MM-DD-oss-engineering-tool-watchlist.md
uv run python scripts/validate_oss_tool_watchlist.py data/oss_tool_watchlist.yaml docs/reports/YYYY-MM-DD-oss-engineering-tool-watchlist.md
```

### Manual review checks
- confirm each upstream/docs link is public and stable;
- confirm the report summarizes changes rather than copying release notes;
- confirm recommendations clearly separate existing-page updates from missing-page candidates;
- confirm overlap with #75-#78/#80 is described as dependency/consumer only.

## Public-safety / secrets constraints
- Use public upstream metadata only: repo URLs, release/tag/version identifiers, docs URLs, and short authored summaries.
- Do not copy upstream source code, docs bodies, release-note paragraphs, or large changelog text blocks into the repo.
- Do not include `/mnt/ace`, `/mnt/ace-data`, private worktree paths, local cache paths, auth tokens, PATs, API keys, cookies, headers, or webhook secrets.
- Do not persist raw API responses if they contain excess metadata that is not needed for the report.
- Prefer anonymous/public endpoints or already-authenticated local GitHub CLI usage that does not write credentials into artifacts.
- Keep BEMRosetta treatment public-safe: the watchlist may track the public upstream/reference location if one exists, but should not promote private/local executable paths or non-public distributions.
- If a tool lacks a clean public signal, record `manual_review` or `signal_unavailable` rather than inventing data.

## Risks
1. **API rate limits / auth friction**
   - Risk: scanning many GitHub repos weekly may hit unauthenticated limits or behave inconsistently.
   - Mitigation: keep the initial tool set small, document auth expectations, prefer minimal metadata endpoints, and support cached/fixture-based tests.
2. **Noisy or unstable change signals**
   - Risk: some tools do not publish reliable releases, making automated “change” detection noisy.
   - Mitigation: allow per-tool signal strategy and normalized fallback statuses like `manual_review`.
3. **Overlap creep into #75**
   - Risk: the watchlist script becomes a generic weekly reporting framework.
   - Mitigation: keep #79 focused on the OSS tool manifest + delta report; #75 should later consume #79 artifacts.
4. **Overlap creep into content authoring**
   - Risk: implementation starts auto-generating tool pages.
   - Mitigation: stop at candidate recommendations and target paths in the first pass.
5. **Deduplication blind spots**
   - Risk: new recommendations duplicate existing work because issue routing is too shallow.
   - Mitigation: maintain an explicit issue-map/routing layer and require tests for existing-lane reuse.
6. **License/provenance ambiguity for some tools**
   - Risk: public URL exists but the repo/docs/release pattern is inconsistent or derivative.
   - Mitigation: record source type and confidence in the manifest; prefer official upstream pages and public repos only.

## Acceptance criteria mapping

| Issue #79 acceptance criterion | Plan response |
|---|---|
| Watchlist exists as a structured YAML/JSON plus human-readable markdown report | Covered by Phase 1 manifest contract, Phase 2 seeding, and Phase 5 report generation |
| At least 10 priority tools have owner/repo/docs/version/check fields | Explicitly required in the seeded manifest and in manifest-schema tests |
| A scan command produces a delta report with candidate wiki updates and deduplicates against open issues | Covered by Phases 3-5 and issue-dedup tests |
| Pages link to tier-1 code/result artifacts where public and applicable | Included in manifest fields and candidate-action/report design; reinforced by file-map and validation rules |
| External API rate limits or auth needs are documented in the plan if relevant | Covered in Risks and Dependencies sections below |

## Dependencies and coordination

### Hard dependencies
- None for the initial local-first implementation if public upstream URLs are hard-coded in the seed manifest.

### Soft dependencies / coordination points
- [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap anchor for routing recommendations and portfolio-level updates.
- [#37](https://github.com/vamseeachanta/llm-wiki/issues/37) — completed scorecard/reporting pattern worth reusing for deterministic local output.
- [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) — should consume #79 output later as one section of the weekly control loop rather than reimplement tool monitoring.
- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — future `llms.txt` entrypoints can link the watchlist/report outputs, but #79 should not implement manifests.
- [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — graph manifests may later ingest watchlist-tool relationships, but graph generation is not part of #79.
- [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — benchmark questions can later use watchlist-covered tools as retrieval/eval fixtures.
- [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — future CLI/MCP surfaces can expose watchlist/report artifacts once stabilized.

### External dependencies / assumptions
- Public GitHub repo metadata or official docs pages exist for most seeded tools.
- If GitHub API-backed scanning is used, the implementation may need either:
  - `gh` authenticated locally, or
  - low-rate anonymous requests with documented limits.
- Tests should not depend on live network calls; fixture-based normalization is preferred.

## Follow-up issues
- **No mandatory split issue is required at planning time.**
- Possible later follow-ups only if scope proves too large:
  1. a narrow issue for per-tool wiki seed-page creation from accepted watchlist candidates;
  2. a narrow issue for scheduled/CI execution once the local-first scanner is stable;
  3. a narrow issue for richer issue-routing maps if open-issue dedup becomes its own reusable substrate.

## Approval-gate note
This plan is review-ready for the standard `plan-review` gate only. It is **not** implementation approval. Before execution:
1. review the watchlist scope against #75-#78/#80 for overlap,
2. confirm the initial tool set and public signal sources are acceptable,
3. confirm whether `gh` auth/API assumptions are acceptable for local runs,
4. obtain explicit user approval,
5. then implement with TDD and local `uv run` validation.

## Recommended implementation sequence after approval
1. define the manifest schema and failing tests;
2. seed the first 10-13 tools with public URLs and candidate wiki targets;
3. implement signal normalization and per-tool status output;
4. add issue-routing/dedup logic;
5. generate the first dated watchlist report;
6. add validator coverage;
7. document the command in `README.md`.

## Adversarial review synthesis and accepted hardening

Three independent plan reviews completed on 2026-05-15. Normalized verdict: **MAJOR until state/network contracts are frozen; revised plan is approval-candidate with Medium residual risk**. The following changes are binding.

### Accepted changes from review
- **Static config separate from mutable state:** v1 uses separate artifacts, e.g.:
  - `data/oss_tool_watchlist.json` for canonical tool definitions;
  - `artifacts/watchlist/latest-state.json` for observed upstream metadata;
  - `docs/reports/<run-date>-oss-engineering-tool-watchlist.md` for human summary.
- **JSON over YAML for v1:** use JSON unless a dependency manifest is explicitly added.
- **Live mode vs fixture mode:** tests run fixture-only with no network. Live network scanning is optional, explicitly enabled, bounded by timeout/retry/rate-limit policy, and non-blocking for validation.
- **Scan/render split:** one step normalizes upstream signals into state JSON; another renders the report from state/config.
- **Per-tool signal strategy:** each watchlist entry must define `signal_strategy`, `source_type`, `source_url`, `affected_paths`, `update_relevance_rule`, and confidence/noise handling.
- **Evidence normalization:** report rows include `signal_type`, `observed_value`, `previous_value`, `observed_at`, `source_url`, `confidence`, and `why_it_matters`.
- **No-action path:** a detected upstream change may produce `no_action` with rationale to suppress churn.
- **Issue routing source:** dedup uses a checked-in issue map such as `data/oss_tool_issue_map.json`; live GitHub reads are optional enrichment only.
- **Auth/failure policy:** anonymous/public endpoints or already-authenticated `gh` may be used only in live mode; artifacts must never include tokens, headers, cookies, or raw API payloads.

### Residual risk
Medium. Network-facing weekly scans are inherently noisy; fixture mode, state separation, confidence fields, and no-action decisions control the risk.

## Complexity
**T2** — moderate repo-local automation/reporting task with external metadata inputs, deterministic test surface, and meaningful overlap boundaries, but no broad ingestion, no deployment, and no private-data access.