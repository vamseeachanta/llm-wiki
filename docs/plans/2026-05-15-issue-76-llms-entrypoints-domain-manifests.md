---
title: "Issue #76 plan — llms.txt entrypoints and curated domain manifests"
issue: 76
status: plan-approved
created: 2026-05-15
last_updated: 2026-05-15
public_safety: public-safe navigation manifests only; no raw/private/vendor/client content or path-rich manifests
---

# Issue #76 Plan — llms.txt Entry Points and Curated Domain Manifests

## Approval gate

- GitHub issue: [vamseeachanta/llm-wiki#76](https://github.com/vamseeachanta/llm-wiki/issues/76)
- Current local plan state: `plan-approved`
- Implementation status: **approved for implementation; implementation must follow TDD and closeout gates**
- Approval note: user approved this plan on 2026-05-15; implementation may proceed under TDD, validation, cross-review, and transactional closeout gates.

## Summary

Issue #76 should add a small, canonical AI-agent entry surface for `llm-wiki` so an agent can discover the repo purpose, public/private boundary, major domain entry points, and high-value link maps without scanning the entire corpus blindly.

The recommended implementation is:

1. add a root `llms.txt` as the primary repo entry point;
2. add domain-level `llms.txt` manifests for the three domains named in the issue body:
   - `wikis/marine-engineering/llms.txt`
   - `wikis/engineering/llms.txt`
   - `wikis/engineering-standards/llms.txt`
3. add `llms-full.txt` only where the domain size justifies it, with marine-engineering as the expected first candidate;
4. add a deterministic validator and tests that enforce existing-path links and public-safety rules;
5. update human-facing docs so README-level discovery and agent discovery stay aligned.

This work should stay tightly scoped to curated navigation manifests. It should not expand into retrieval infrastructure, knowledge-graph generation, benchmark harnesses, weekly freshness automation, or MCP/CLI query surfaces.

## Current evidence / intelligence

Fresh inspection on 2026-05-15 covered the live issue plus the repo surfaces most relevant to manifest design.

### Issues inspected

- [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) — source issue; requires root/domain `llms.txt`, optional `llms-full.txt`, validator, README guidance, and plan-review gate.
- [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) — roadmap anchor; #76 should attach to this navigation/completeness lane rather than create a new umbrella.
- [#28](https://github.com/vamseeachanta/llm-wiki/issues/28) — marine canonical index chunking; relevant dependency because marine is too large for naive one-file navigation.
- [#29](https://github.com/vamseeachanta/llm-wiki/issues/29) — source-title aliasing; relevant dependency for readable source labels in any future marine `llms-full.txt` or source-oriented manifest.
- [#30](https://github.com/vamseeachanta/llm-wiki/issues/30) — provenance backfill; relevant because manifests should prefer pages with complete frontmatter/provenance.
- [#36](https://github.com/vamseeachanta/llm-wiki/issues/36) — cross-wiki link discovery/infrastructure; adjacent but separate from this entrypoint work.
- [#75](https://github.com/vamseeachanta/llm-wiki/issues/75) — weekly freshness control loop; out of scope here except as a future consumer of manifests.
- [#77](https://github.com/vamseeachanta/llm-wiki/issues/77) — public-safe knowledge-graph/link-graph manifests; explicitly separate from this simpler markdown-entrypoint issue.
- [#78](https://github.com/vamseeachanta/llm-wiki/issues/78) — RAG evaluation benchmark; downstream validation lane, not part of #76 implementation.
- [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) — weekly OSS watchlist; unrelated to navigation manifests.
- [#80](https://github.com/vamseeachanta/llm-wiki/issues/80) — CLI/MCP query surface; downstream access layer, not part of #76.

### Files inspected

Repo/governance/doc surfaces:

- `README.md`
- `CLAUDE.md`
- `docs/plans/README.md`
- `docs/governance/service-provider-data-routing.md`
- `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md`
- `wikis/cross-links-tier1.md`
- `wikis/marine-engineering/wiki/code-results-links.md`
- `wikis/engineering/wiki/public-data-software-links.md`

Existing related plans:

- `docs/plans/2026-05-11-issue-28-marine-index-chunking.md`
- `docs/plans/2026-05-11-issue-29-source-title-aliasing.md`

Validation/test/script surfaces:

- `scripts/validate_completion_artifacts.py`
- `scripts/validate_governance_artifacts.py`
- `scripts/llm_wiki_strengthening_scorecard.py`
- `tests/test_completion_artifacts.py`
- `tests/test_governance_artifacts.py`
- `tests/test_scan_source_families_safe.py`

Domain entry points inspected:

- `wikis/marine-engineering/wiki/index.md`
- `wikis/engineering/wiki/index.md`
- `wikis/engineering-standards/wiki/index.md`

### Evidence found

- No `llms.txt` or `llms-full.txt` files currently exist in the repo.
- `README.md` already explains repo purpose, wiki layout, and licensing/public-boundary rules, so root `llms.txt` can be derived from committed public-safe repo facts rather than invented policy.
- `CLAUDE.md` and `docs/governance/service-provider-data-routing.md` already define the strongest agent-safety constraints that must be surfaced in root/domain manifests.
- `docs/reports/2026-05-11-llm-wiki-completion-control-plane.md` and the Tier-1 cross-link pages already provide high-value code/data/results/gov links that root `llms.txt` should point agents to instead of repeating large prose blocks.
- Existing validator patterns are deterministic and repo-local (`validate_completion_artifacts.py`, `validate_governance_artifacts.py`), so #76 should follow that pattern rather than invent an ad hoc check.
- `scripts/llm_wiki_strengthening_scorecard.py` already treats `index.md`, `log.md`, `overview.md`, and `portal.md` as non-content control pages. New `llms*.txt` entrypoints may require explicit treatment so scorecard metrics do not misclassify them.
- Current domain sizes justify curated entrypoints rather than brute-force listings:
  - `wikis/marine-engineering/wiki/index.md`: 21,658 lines; frontmatter reports `page_count: 19214`, `source_count: 19169`
  - `wikis/engineering/wiki/index.md`: 173 lines; frontmatter reports `page_count: 108`, `source_count: 24`
  - `wikis/engineering-standards/wiki/index.md`: 248 lines; frontmatter reports `page_count: 216`, `source_count: 19`
- Current section counts from repo inspection:
  - `marine-engineering`: concepts 23, entities 22, sources 19,173, standards 1, comparisons 1
  - `engineering`: concepts 63, entities 27, sources 24, standards 9, workflows 5
  - `engineering-standards`: concepts 35, entities 0, sources 19, standards 162
- Marine engineering is the only obviously oversized domain; it likely needs a root domain `llms.txt` plus either a bounded `llms-full.txt` or chunk-aware references that build on #28/#29.

## Scope boundaries

### In scope

- Root-level `llms.txt` for repository purpose, safety rules, domain map, and high-value public-safe links.
- Domain-level `llms.txt` for `marine-engineering`, `engineering`, and `engineering-standards`.
- Optional `llms-full.txt` support where justified by domain size, starting with marine-engineering.
- Deterministic generation or hand-authored curation rules for manifest content.
- Validation that linked paths exist and that manifests do not contain forbidden raw/private path patterns.
- README guidance for humans and agents on how to use these entrypoints.
- Tests for manifest generation/validation and any scorecard exemptions needed for `llms*.txt` files.

### Out of scope

- No implementation of retrieval APIs, MCP servers, or query CLIs from #80.
- No knowledge-graph or link-graph artifact generation from #77.
- No benchmark harness or evaluation dataset work from #78.
- No weekly freshness automation or recurring update scheduler from #75/#79.
- No broad domain expansion or page-authoring work beyond the manifests themselves.
- No raw/private archive reading, no vendor-derivative text promotion, no path-rich private manifests.

## Implementation phases

### Phase 1 — Contract, safety model, and failing tests

Define the manifest contract before writing files.

- Decide whether manifests are fully hand-authored markdown, generated from a small config, or hybrid.
- Write failing tests for:
  - required root/domain sections;
  - existing-target validation;
  - forbidden path/private-pattern rejection;
  - deterministic output/order if generation is used;
  - scorecard/content-page handling if `llms*.txt` would otherwise be counted incorrectly.
- Reuse the narrow-validator pattern already used in `scripts/validate_completion_artifacts.py` and `scripts/validate_governance_artifacts.py`.

### Phase 2 — Root repo entrypoint

Add `llms.txt` at repo root as the canonical agent landing page.

Expected content:

- repo purpose and license split;
- public/private boundary and vendor-routing summary;
- “start here” links to README, governance, completion-control-plane, Tier-1 cross-links, and the three initial domain manifests;
- a “how to find X” section mapping common intents to domain entrypoints;
- explicit instruction to prefer curated manifests over deep source scanning.

### Phase 3 — Domain manifests for engineering and engineering-standards

Add concise domain manifests where the current domain indexes are already human-scale.

- `wikis/engineering/llms.txt` should prioritize methodology concepts, workflows, public-data/software links, and top-level standards/concepts pages.
- `wikis/engineering-standards/llms.txt` should prioritize standards-family navigation, concept anchors, source catalogs, and standards routing cautions.
- These should remain concise and likely do not require `llms-full.txt` initially.

### Phase 4 — Marine manifest strategy

Add `wikis/marine-engineering/llms.txt` as a curated, non-exhaustive navigation page.

Recommended design:

- route agents first to `wiki/portal.md`, `wiki/index.md`, key concept/entity hubs, and `wiki/code-results-links.md`;
- include a clear warning that the domain contains ~19k source pages and should not be scanned blindly;
- if an exhaustive-ish manifest is needed, either:
  - create `wikis/marine-engineering/llms-full.txt` built from already-curated chunk/index surfaces, or
  - defer that file behind #28/#29 if readable and bounded source discovery is not yet stable.

The plan should assume marine `llms.txt` is required now, while marine `llms-full.txt` is conditional on chunking/alias readiness.

### Phase 5 — Validation, docs, and integration

- Add a dedicated validator, likely `scripts/validate_llms_manifests.py`.
- Add pytest coverage, likely a new `tests/test_llms_manifests.py`.
- Update `README.md` with a short “AI agent entrypoints” section.
- If needed, update `scripts/llm_wiki_strengthening_scorecard.py` so `llms.txt` / `llms-full.txt` are treated as control/navigation artifacts rather than content pages.

## Proposed file map

### New files expected

- `llms.txt`
- `wikis/marine-engineering/llms.txt`
- `wikis/engineering/llms.txt`
- `wikis/engineering-standards/llms.txt`
- `scripts/validate_llms_manifests.py`
- `tests/test_llms_manifests.py`

### Conditional new files

- `llms-full.txt` only if the root manifest needs a longer companion
- `wikis/marine-engineering/llms-full.txt` if marine exhaustive navigation can be made bounded and readable
- `wikis/engineering/llms-full.txt` and `wikis/engineering-standards/llms-full.txt` only if later evidence shows a need; not required for the first pass

### Existing files likely to change during implementation

- `README.md`
- `scripts/llm_wiki_strengthening_scorecard.py` (only if `llms*.txt` needs exclusion/handling)
- possibly `tests/test_completion_artifacts.py` or another existing validator test only if the repo adopts a shared validator pattern for entrypoint docs

## Tests and validation

### TDD checklist

Minimum tests before implementation:

- `test_root_llms_manifest_contains_repo_boundary_and_domain_entrypoints`
- `test_domain_llms_manifests_link_only_to_existing_repo_paths`
- `test_llms_validator_rejects_raw_private_or_vendor_path_patterns`
- `test_llms_validator_rejects_missing_required_sections`
- `test_llms_manifest_generation_is_deterministic` (if generated)
- `test_scorecard_ignores_llms_navigation_files_as_content_pages` (if scorecard behavior changes)

### Validation commands after implementation

Run from repo root:

```bash
uv run python scripts/validate_llms_manifests.py
uv run python scripts/validate_completion_artifacts.py
uv run python scripts/validate_governance_artifacts.py
PYTHONDONTWRITEBYTECODE=1 uv run pytest -q -p no:cacheprovider
```

### Manual spot checks

- confirm each manifest path exists and renders cleanly on GitHub;
- confirm every listed repo-relative target exists;
- confirm root `llms.txt` alone answers “where do I find marine / engineering / standards / governance / code-results links?”;
- confirm marine manifest does not dump thousands of source links directly.

## Public-safety / secrets constraints

Allowed:

- only committed public-safe repo paths;
- README/governance/control-plane summaries already present in this repo;
- aggregate page/domain counts and repo-relative navigation links;
- public GitHub URLs and public repo-relative target references.

Forbidden:

- raw `/mnt/ace` or `/mnt/ace-data` subpaths;
- vendor-derivative standards text, tables, figures, formulas, or brochure prose;
- client/project-sensitive content;
- personal/admin/credential data;
- path-rich private manifests;
- any “helpful” direct source dump of the marine source corpus.

Validator requirements should explicitly scan for the same classes of leakage already blocked by the current governance/completion validators.

## Risks and mitigations

- **Risk: marine manifest becomes another oversized dump.**  
  Mitigation: require curated sections and bounded lists; route exhaustive discovery through #28 chunking and #29 aliasing instead of embedding giant source tables.

- **Risk: manifests drift from actual repo entrypoints.**  
  Mitigation: validator must check every linked repo-relative path exists.

- **Risk: manifests accidentally serialize forbidden local/private paths.**  
  Mitigation: copy the existing regex-scan model from current validators and add explicit tests for raw-path rejection.

- **Risk: `llms*.txt` files distort scorecard/content counts.**  
  Mitigation: update scorecard exclusions if needed and add a regression test.

- **Risk: overlap with #77/#80 expands scope.**  
  Mitigation: keep #76 markdown-only and entrypoint-focused; treat machine-readable graph/query surfaces as follow-on work.

## Acceptance criteria mapping

| Issue acceptance criterion | Planned implementation response | Verification |
| --- | --- | --- |
| Agents can answer “where do I find X?” for major domains from root `llms.txt` alone. | Root `llms.txt` includes repo map, domain routing, and links to governance / Tier-1 / domain manifests. | Read root manifest only and verify it routes to marine, engineering, standards, governance, and code/results anchors. |
| Marine-engineering avoids a 19k-page dump by using curated chunks/indexes. | Marine `llms.txt` stays curated; any marine `llms-full.txt` is bounded by chunk/index strategy and may depend on #28/#29 readiness. | Manual check plus tests that the curated manifest is concise and existing links resolve. |
| Validator fails on missing manifest targets or unsafe local/private path patterns. | Add `scripts/validate_llms_manifests.py` with target-existence checks and safety regex checks. | Validator unit tests and direct script run. |
| README documents how humans and agents should use the manifests. | Add an “AI agent entrypoints” section in `README.md`. | README review plus test/validator if README coverage is added. |

## Adversarial review synthesis and accepted hardening

Three independent plan reviews completed on 2026-05-15. Consensus verdict: **MINOR**. The plan is approval-candidate quality with the following binding clarifications.

### Accepted changes from review
- **Authorship mode:** v1 is **hybrid but deterministic**: manifests are hand-curated in repo text files and validated/generated checks are script-enforced. No live crawler or automatic corpus dump is part of v1.
- **Strict manifest shape:** every `llms*.txt` manifest must use this ordered section contract:
  1. `Purpose`
  2. `Safety Boundary`
  3. `Start Here`
  4. `Key Entry Paths`
  5. `How To Find X`
  6. `Do Not Scan Blindly`
  7. `Related Surfaces`
  8. `Last Updated`
- **Size/curation caps:** root and domain manifests must enforce bounded sections. Implementation must define max lines/links per curated section; marine `llms-full.txt` is optional and not required for v1 unless bounded chunk/index prerequisites are ready.
- **Root coverage rule:** root `llms.txt` briefly routes all major public domains, but only the initial target domains receive deeper domain manifests in v1.
- **Routing smoke tests:** add fixture-backed tests that ask canonical “where do I find X?” intents and verify the expected manifest/entrypoint path is returned.
- **Scorecard note corrected:** because existing scorecard logic walks Markdown, `llms*.txt` should not affect current content counts unless implementation changes scan surfaces.

### Residual risk
Low. Main risk is over-expanding manifests into exhaustive indexes; validators and caps are the control.

## Dependencies

### Hard or near-hard dependencies

- Existing governance rules in `CLAUDE.md` and `docs/governance/service-provider-data-routing.md` are the safety authority for manifest language.
- Existing validation style in `scripts/validate_completion_artifacts.py` and `scripts/validate_governance_artifacts.py` should be reused for consistency.

### Functional dependencies / coordination

- [#28](https://github.com/vamseeachanta/llm-wiki/issues/28): marine chunking improves any future marine `llms-full.txt` and should be referenced rather than duplicated.
- [#29](https://github.com/vamseeachanta/llm-wiki/issues/29): source-title aliasing improves readability of source-facing manifests.
- [#30](https://github.com/vamseeachanta/llm-wiki/issues/30): provenance backfill increases confidence in which pages deserve promotion into manifests.
- [#36](https://github.com/vamseeachanta/llm-wiki/issues/36): cross-wiki link infrastructure is adjacent and can enrich future manifests, but it is not required to ship the first #76 pass.

## Follow-up issues if needed

Create follow-up issues only if implementation uncovers genuine residual work:

1. **Marine `llms-full.txt` follow-up** if #28/#29 must land first for readable bounded source navigation.
2. **Manifest freshness automation** only if static manifests show real drift pressure; route this to #75 rather than expanding #76.
3. **Machine-readable retrieval/graph export** should route to #77 and/or #80, not back into #76.
4. **Cross-domain expansion** for additional domain manifests beyond the three named in #76 can be a separate issue after the initial pattern is proven.

## Done criteria

- Root `llms.txt` exists and is a credible single-file repo entrypoint.
- The three requested domain manifests exist and route to real public-safe targets.
- Marine entrypoint stays curated and does not reproduce a raw 19k-page listing.
- Validator and tests exist and pass.
- README explains how humans/agents should use the manifest surface.
- No overlap creep into #75 or #77-#80 beyond clearly stated dependencies.
- Main-agent closeout can point to this plan as approval-gated, review-ready planning for #76.
