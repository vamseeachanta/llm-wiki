---
title: "Issue #40 plan — reservoir engineering literature corpus build-out"
issue: 40
status: draft
created: 2026-05-15
last_updated: 2026-05-15
public_safety: local-corpus triage + concept-page authoring; NO ingestion of paywalled/proprietary content; license-filter required
---

# Issue #40 Plan — Reservoir Engineering Literature Corpus

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#40](https://github.com/vamseeachanta/llm-wiki/issues/40)
- Current live label state: `status:plan-approved` (set 2026-05-06)
- Local plan status: `draft` (this file) — **state-drift remediation per `issue-planning-mode` missing-plan rule**: issue was labelled plan-approved on 2026-05-06 without a canonical local plan or `.planning/plan-approved/40.md` marker. This plan promotes the issue-body scope into the template-shaped canonical form. Per skill: do NOT downgrade the live label to match stale local state; instead bring local state up to live state.
- Implementation status: **not started**; awaiting fresh adversarial review on this canonical plan before re-confirming plan-approved is still warranted.

## Resource intelligence

Sources consulted:

1. **Issue body** ([#40](https://github.com/vamseeachanta/llm-wiki/issues/40)) — comprehensive: scope (in/out), source lists (local `/mnt/ace` + 8 online), workflow (5 steps), acceptance criteria (5 items), risks (2). Reads as a plan, not just an issue.
2. **llm-wiki existing structure** (`ls wikis/`) — 10 founded domains as of 2026-05-15: drilling-engineering, production-engineering, marine-engineering, lng-projects, maritime-law, naval-architecture, asset-management, engineering-standards, financial-services, plus one more. **No `wikis/reservoir-engineering/` directory yet** — this plan creates it.
3. **Companion issue** [vamseeachanta/kaggle-rogii-2026#5](https://github.com/vamseeachanta/kaggle-rogii-2026/issues/5) — competition-specific prior art (datasets + ML papers); this plan covers the broader educational foundation.
4. **Governance precedent** [vamseeachanta/workspace-hub#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) — wiki sources/ deny-list (cite the canonical page, not the sources/ entry).
5. **Calc citation contract** `.claude/rules/calc-citation-contract.md` — applies when formulas appear in concept pages.
6. **PE wiki overview** (`wikis/production-engineering/wiki/overview.md`) — explicitly anticipates a future reservoir-engineering domain ("Reservoir engineering ... separate domain (not yet founded as of 2026-05-13)"). This plan is the founding event.

**Gaps identified:**

- No `wikis/reservoir-engineering/` directory exists.
- No `docs/research/reservoir-engineering-corpus.md` inventory exists.
- No prior plan exists for this issue (the drift this plan resolves).

## Public-safety boundary

**Allowed:**

- Inventory of `/mnt/ace/rock-oil-field/` and other candidate dirs into a manifest at `docs/research/reservoir-engineering-corpus.md` (file paths + metadata only; NO copying source content into the manifest).
- Authoring of original concept pages under `wikis/reservoir-engineering/concepts/` and methodology pages under `wikis/reservoir-engineering/methodology/`, citing sources but never copying >30-word chunks.
- Citation of public-domain works (>70 years old), creative-commons, USGS, university OCW, arXiv, open-access OnePetro/AAPG/SEG entries.
- Standards-page anchors using the #2471-shape frontmatter (`code_id`, `publisher`, `revision`) for DNV / API / ISO references.

**Forbidden:**

- Ingestion of paywalled textbooks even if found locally on `/mnt/ace` (license-incompatible with MIT + CC-BY-4.0 publication).
- Vendor-derivative material under proprietary license.
- Citation of pages under `knowledge/wikis/*/wiki/sources/` per the [#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) deny-list — cite the canonical standard or concept page instead.
- Verbatim copying of paragraphs >30 words from any source regardless of license (paraphrase + cite).

## Deliverable

A founded `wikis/reservoir-engineering/` wiki domain populated with ≥5 concept pages + ≥2 methodology pages, plus a corpus manifest at `docs/research/reservoir-engineering-corpus.md` listing ≥50 triaged candidate sources, ready for downstream consumption by the Kaggle ROGII competition modeling work.

## Artifact map

| Artifact | Path |
|---|---|
| This plan | `llm-wiki/docs/plans/2026-05-15-issue-40-reservoir-engineering-literature.md` |
| Corpus inventory | `llm-wiki/docs/research/reservoir-engineering-corpus.md` |
| Wiki domain (new) | `llm-wiki/wikis/reservoir-engineering/wiki/` |
| Concept pages (≥5) | `wikis/reservoir-engineering/wiki/concepts/{porosity,permeability,gamma-ray-log-interpretation,dip-azimuth,formation-tops}.md` |
| Methodology pages (≥2) | `wikis/reservoir-engineering/wiki/methodology/{geosteering-workflow,log-correlation}.md` |
| Standards anchors | `wikis/reservoir-engineering/wiki/standards/` (≥1 page per cited standard with #2471 frontmatter) |
| Wiki index | `wikis/reservoir-engineering/wiki/index.md` |
| Wiki log | `wikis/reservoir-engineering/wiki/log.md` |
| Plan review — Claude | `scripts/review/results/2026-05-15-plan-40-claude.md` |
| Plan review — Codex | `scripts/review/results/2026-05-15-plan-40-codex.md` |

## Files to change

| Action | Path | Reason |
|---|---|---|
| Create | `docs/research/reservoir-engineering-corpus.md` | License-triaged source manifest |
| Create | `wikis/reservoir-engineering/wiki/index.md` | Founding-state index |
| Create | `wikis/reservoir-engineering/wiki/log.md` | Iteration log per ingest |
| Create | `wikis/reservoir-engineering/wiki/concepts/porosity.md` | Concept anchor |
| Create | `wikis/reservoir-engineering/wiki/concepts/permeability.md` | Concept anchor |
| Create | `wikis/reservoir-engineering/wiki/concepts/gamma-ray-log-interpretation.md` | Concept anchor |
| Create | `wikis/reservoir-engineering/wiki/concepts/dip-azimuth.md` | Concept anchor (Kaggle ROGII relevant) |
| Create | `wikis/reservoir-engineering/wiki/concepts/formation-tops.md` | Concept anchor |
| Create | `wikis/reservoir-engineering/wiki/methodology/geosteering-workflow.md` | Methodology anchor |
| Create | `wikis/reservoir-engineering/wiki/methodology/log-correlation.md` | Methodology anchor |

## TDD test list (governance/safety tests)

| Test | What it verifies |
|---|---|
| `tests/test_completion_artifacts.py` extended | reservoir-engineering wiki index passes existing schema check |
| `tests/test_governance_artifacts.py` extended | no >30-word verbatim chunks against a sample of cited public-domain sources |
| `scripts/validate_governance_artifacts.py` extended | corpus manifest passes license-filter rules (no vendor-derivative entries) |

No runtime calc to reproduce per Step 1.5 — this is a corpus-build issue, not a runtime-failure issue. **Reproduction proofs: N/A — content-authoring scope.**

## Acceptance criteria

- [ ] Corpus inventory at `docs/research/reservoir-engineering-corpus.md` lists ≥50 triaged sources with `(filepath/URL, classification ingest/skip/defer, license note)` per row
- [ ] ≥5 concept pages drafted under `wikis/reservoir-engineering/concepts/` covering core fundamentals (porosity, permeability, gamma-ray log interpretation, dip/azimuth, formation tops)
- [ ] ≥2 methodology pages under `wikis/reservoir-engineering/methodology/` covering geosteering workflow + log correlation
- [ ] `wikis/reservoir-engineering/wiki/index.md` lists the founding state with page_count + last_updated
- [ ] All cited sources licensed for redistribution OR cited only as reference (no in-page copying)
- [ ] Cross-link added to [kaggle-rogii-2026#5](https://github.com/vamseeachanta/kaggle-rogii-2026/issues/5) so modeling work can reference the wiki pages
- [ ] `tests/test_completion_artifacts.py` + `tests/test_governance_artifacts.py` pass post-build
- [ ] Plan + adversarial review artifacts posted to `scripts/review/results/2026-05-15-plan-40-*.md`

## Risks and open questions

- **Risk:** `/mnt/ace/rock-oil-field/` may contain user-purchased textbooks not licensed for redistribution. Mitigation: license-triage column in the corpus manifest is mandatory; default = skip if license unclear.
- **Risk:** Hermes execution layer was 0-of-6 on overnight 2026-05-14 dispatch (per goal-catalog [#2695](https://github.com/vamseeachanta/workspace-hub/issues/2695) feedback comment). For this issue specifically, Hermes routing tag should be `claude-main-direct` not `hermes-claude-code` until [#2696](https://github.com/vamseeachanta/workspace-hub/issues/2696) audit closes — concept-page authoring is the wrong workload for kanban worker.
- **Open:** Citation style (IEEE-numeric vs APA vs inline `code_id` from #2471). Recommend matching the existing llm-wiki convention; surface in adversarial review.
- **Open:** Is the founding-event commit-message standard the same as drilling-engineering ([`7dc802d1`](https://github.com/vamseeachanta/llm-wiki/commit/7dc802d1)) and production-engineering? Default to mirroring.

## Complexity: T3

**T3** — multi-session scope (issue body says "few sessions across 1-2 weeks"), founds a new wiki domain (governance impact), requires license-triage of ≥50 sources, authors ≥7 wiki pages with cross-domain anchoring. Comparable in scope to production-engineering founding + Phase 1 combined.

## Adversarial review summary

PENDING — fill in after Step 4 completes.

| Provider | Verdict | Key findings |
|---|---|---|
| Claude | — | — |
| Codex | — | — |
