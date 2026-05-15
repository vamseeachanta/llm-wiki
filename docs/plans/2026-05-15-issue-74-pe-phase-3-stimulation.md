---
title: "Issue #74 plan — Production Engineering Phase 3 corpus build-out (stimulation)"
issue: 74
status: plan-review
created: 2026-05-15
last_updated: 2026-05-15
public_safety: API/SPE standards anchors + original concept authoring; NO vendor-confidential frac-design or stimulation-chemistry manuals
---

# Issue #74 Plan — PE Phase 3 (Stimulation)

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#74](https://github.com/vamseeachanta/llm-wiki/issues/74) (created 2026-05-15)
- Local plan status: `draft`
- Implementation status: not started; awaiting adversarial review + user approval.
- Predecessors: [Phase 1 #61](https://github.com/vamseeachanta/llm-wiki/issues/61) (closed 2026-05-15), [Phase 2 #73](https://github.com/vamseeachanta/llm-wiki/issues/73) (this same slate, must complete before Phase 3 begins).

## Resource intelligence

Sources consulted:

1. **PE overview** (`wikis/production-engineering/wiki/overview.md` lines 62-66) — Phase 3 scope: matrix acid stimulation, hydraulic fracturing (frac fluids, proppants, frac design), refrac decisioning.
2. **Phase 2 plan** (`docs/plans/2026-05-15-issue-73-pe-phase-2-completions.md`, this same slate) — sand-control page is the Phase-2/Phase-3 boundary topic for frac pack; cross-links pre-installed there.
3. **drilling-engineering Phase 1 close-out** ([#49](https://github.com/vamseeachanta/llm-wiki/issues/49)) — references API RP 13B (mud testing, applies to frac-fluid rheology) and API RP 39 (stimulation chemicals).
4. **engineering-standards wiki** — check existence of API RP 39 standards-page; cross-link if present, create if not.
5. **Calc citation contract** — applies to frac-design formulas (PKN, KGD, pseudo-3D models), proppant-pack permeability, fluid-leakoff coefficient.

**Gaps identified:**

- No `wikis/production-engineering/wiki/concepts/matrix-acid-stimulation.md` exists.
- No `wikis/production-engineering/wiki/concepts/hydraulic-fracturing.md` exists.
- No `wikis/production-engineering/wiki/concepts/refrac.md` exists.
- API RP 39 standards-page TBD.

## Public-safety boundary

**Allowed:**

- API / SPE / ISO recommended-practices ingest at the standards-page level (`code_id`, `publisher`, `revision`).
- Original concept authoring with frac-design formulas under the calc-citation contract.
- Reference to public state-RRC frac-completion registries (Texas RRC W-2, Pennsylvania DEP, Colorado COGCC, Wyoming Oil & Gas Conservation Commission).
- USGS produced-water and hydraulic-fracturing chemical disclosure databases (FracFocus is industry-managed; cite carefully for jurisdictional scope).

**Forbidden:**

- Vendor-confidential frac-design / chemistry manuals (Halliburton FracDesign, Schlumberger StimFRACTM, BJ Services proprietary docs).
- Verbatim copying of paragraphs >30 words from API/SPE standards (paraphrase + cite).
- Citation of pages under `wikis/*/wiki/sources/` per [#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) deny-list.
- Vendor proppant performance datasheets (cite vendor by name + general proppant class — sand, RCS, ceramic — without proprietary performance curves).

## Deliverable

Phase 3 corpus expansion adding 3 sub-issues each landing concept page(s) + ≥1 standards page, growing `wikis/production-engineering/wiki/` from post-Phase-2 target ~35 pages to ~45-55 pages total. Cross-links established between Phase 2 completions (perforating, sand control) and Phase 3 stimulation.

## Artifact map

| Artifact | Path |
|---|---|
| This plan | `llm-wiki/docs/plans/2026-05-15-issue-74-pe-phase-3-stimulation.md` |
| Sub-issue 1 (matrix acid) — new | created during execution; title `research+ingest(production-engineering): matrix acid stimulation — sandstone/carbonate acidizing + chemistry + diversion + candidate selection` |
| Sub-issue 2 (hydraulic fracturing) — new | title `research+ingest(production-engineering): hydraulic fracturing — frac fluids + proppants + frac design (PKN/KGD/3D) + microseismic` |
| Sub-issue 3 (refrac) — new | title `research+ingest(production-engineering): refrac decisioning — candidate selection + recompletion architectures + DFIT analysis` |
| Concept pages (≥3) | `wikis/production-engineering/wiki/concepts/{matrix-acid-stimulation,hydraulic-fracturing,refrac}.md` |
| Standards pages | `wikis/production-engineering/wiki/standards/{api-rp-39,…}.md` OR cross-links to existing `engineering-standards/` |
| Wiki index update | `wikis/production-engineering/wiki/index.md` |
| Wiki log entries | `wikis/production-engineering/wiki/log.md` (one per sub-issue) |
| Plan review — Claude | `scripts/review/results/2026-05-15-plan-74-claude.md` |
| Plan review — Codex | `scripts/review/results/2026-05-15-plan-74-codex.md` |

## Sub-issue scope breakdown

### Sub-issue 1 — Matrix acid stimulation

**Pages to create:**

- `concepts/matrix-acid-stimulation.md` — sandstone vs carbonate matrix acidizing (mud acid HCl/HF, retarded acid, organic acid), diversion mechanisms (foam, ball sealers, fiber, mechanical), candidate selection (skin damage vs reservoir damage), near-wellbore damage diagnosis.
- `standards/api-rp-39.md` (if not in `engineering-standards/`) — stimulation chemicals testing.

**Cross-links:**

- Phase 2 `concepts/perforating.md` — perforation strategy affects matrix-acid placement.
- Future reservoir-engineering domain — formation-damage skin theory anchors here.

### Sub-issue 2 — Hydraulic fracturing

**Pages to create:**

- `concepts/hydraulic-fracturing.md` — frac fluid systems (slickwater, linear gel, crosslinked, energized, foamed, cleanup characteristics), proppants (sand, resin-coated sand, ceramic, ultra-light), frac design (PKN, KGD, pseudo-3D, 3D — when each applies), pump schedule (pad, slurry, flush), microseismic monitoring, refrac vs new-well decisioning at the design phase.
- Calc-citation entries for PKN width formula, KGD width formula, proppant-pack permeability. Primary reference: **SPE Monograph 17** (Reservoir Stimulation, 3rd Ed., Economides & Nolte) — license-clear authoritative reference for frac-design formulas. API RP 39 cited only for its narrow scope (frac-fluid viscosity testing); API RP 42 for surfactant testing.

**Cross-links:**

- Phase 2 `concepts/sand-control.md` — frac pack is the Phase-2/Phase-3 boundary.
- `drilling-engineering/concepts/casing-program-design.md` — frac pressures must respect casing burst.
- Future reservoir-engineering domain — productivity index post-frac.

### Sub-issue 3 — Refrac decisioning

**Pages to create:**

- `concepts/refrac.md` — refrac vs new-well economics, candidate selection, recompletion architectures (cement-and-perf, mechanical isolation, expandable liner).
- `concepts/diagnostic-fracture-injection-test.md` — **Diagnostic Fracture Injection Test (DFIT)** methodology: pre-frac mini-frac procedure to measure closure pressure, instantaneous shut-in pressure, leak-off coefficient. Reference: SPE Monograph 17 (Reservoir Stimulation, Economides & Nolte) for theory; SPE 167165 + SPE 124292 for field-practice procedures.
- `concepts/production-history-decline-analysis.md` — Arps decline curves, type-curve matching, b-factor estimation for refrac candidate selection. Cross-link to future reservoir-engineering domain.

**Cross-links:**

- Phase 3 `concepts/hydraulic-fracturing.md` — refrac is hydraulic fracturing applied to a previously-stimulated well; major content overlap, page disambiguation by decision-framing.
- Future Phase 4 `concepts/well-integrity-during-production.md` — refrac risk depends on existing well-integrity state.

## Sequencing

Recommended order: **Sub-issue 1 (matrix acid) → Sub-issue 2 (hydraulic fracturing) → Sub-issue 3 (refrac)**. Reason: matrix acid is the simplest scope (one technique family), hydraulic fracturing is the largest scope (frac-design formulas + proppant taxonomy + fluid taxonomy), refrac builds on hydraulic fracturing context.

**Cross-phase dependency:** Phase 2 #73 should land FIRST. Phase 2 sand-control page contains the frac-pack cross-link target; Phase 3 hydraulic-fracturing page links into it. Out-of-order execution creates broken-link transient state.

## TDD test list (governance/safety tests)

| Test | What it verifies |
|---|---|
| `tests/test_completion_artifacts.py` | new pages pass schema check |
| `tests/test_governance_artifacts.py` | no >30-word verbatim API/SPE chunks; no vendor proprietary content |
| `tests/test_scan_source_families_safe.py` | new pages don't reference vendor-confidential PDFs |
| New: `tests/test_calc_citations.py` (if frac-design formulas appear) | calc citations match #2471 schema |

No runtime calc to reproduce. **Reproduction proofs: N/A — content-authoring scope.**

## Acceptance criteria

- [ ] 3 sub-issues created under this epic with `research+ingest(production-engineering):` prefix
- [ ] ≥5 concept pages landed (matrix-acid, hydraulic-fracturing, refrac, DFIT-methodology, production-history-decline-analysis) — scope expanded per Claude r1 MINOR-3
- [ ] ≥1 standards page per sub-issue (or cross-link to `engineering-standards/`)
- [ ] `wiki/index.md` page_count reflects new pages (post-Phase-2 target ≥35 → post-Phase-3 target ≥45)
- [ ] `wiki/log.md` carries one entry per ingest (3 minimum)
- [ ] Bidirectional cross-links: Phase 2 completions ↔ Phase 3 stimulation
- [ ] Calc-citation entries for any frac-design formulas
- [ ] All tests pass post-build
- [ ] Plan + adversarial review artifacts posted to `scripts/review/results/2026-05-15-plan-74-*.md`

## Risks and open questions

- **Risk:** Hydraulic-fracturing scope can balloon (frac-fluid chemistry alone is a 200-page topic in SPE Monograph 17). Mitigation: bound concept page to ≤300 lines; defer deeper coverage to sub-pages only if user approves scope expansion.
- **Risk:** Vendor proprietary frac-design tools (FracPro, GOHFER, StimPlan, Mfrac) are essential context but their algorithm details are confidential. Mitigation: name them as "industry-standard frac-design simulators" without algorithm internals.
- **Risk:** FracFocus disclosure-database citation has license terms; verify before reference.
- **Risk:** Phase 3 execution before Phase 2 lands creates broken cross-links — enforce sequencing.
- **Open:** Should refrac get its own concept page or fold into hydraulic-fracturing? Recommend separate page (decision-framing is distinct); confirm in adversarial review.

## Complexity: T2

**T2** — 3 sub-issues, ≥3 new concept pages, multi-week scope, no runtime test surface, requires calc-citation entries for frac-design formulas (adds rigor). Comparable to Phase 2 in shape; matrix-acid and refrac sub-issues are T2, hydraulic-fracturing sub-issue trends T3 due to scope depth.

## Adversarial review summary

**Round 1 — 2026-05-15** (single-author Claude fallback per [[feedback_permission_gate_blocks_cross_review]])

| Provider | Verdict | Key findings |
|---|---|---|
| Claude | MINOR | (1) API RP 39 has narrow scope (frac-fluid viscosity testing only) — supplement with SPE Monograph 17 (Reservoir Stimulation, Economides & Nolte) as broader frac reference; API RP 42 for surfactant testing. (2) DFIT acronym needs first-use expansion (Diagnostic Fracture Injection Test) in plan body and concept page. (3) Refrac sub-issue scope is thin (1 page); either fold into hydraulic-fracturing OR expand to also cover DFIT methodology + production-history-analysis decisioning. (4) "≤300 line" page bound is not enforceable — drop or replace with `tests/test_page_length.py` enforcing ≤500. (5) Phase 2 sand-control page name aligned; implementation should verify before cross-linking. |
| Codex | — | not run this round (T2 scope warrants Codex; deferred to user direction) |

**Overall result:** approval-ready after standards-reference correction (MINOR-1) and refrac sub-issue scope decision (MINOR-3). Review artifact: [scripts/review/results/2026-05-15-plan-74-claude.md](../../../scripts/review/results/2026-05-15-plan-74-claude.md).
