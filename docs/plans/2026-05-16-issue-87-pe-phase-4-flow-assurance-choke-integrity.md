---
title: "Issue #87 plan — Production Engineering Phase 4 corpus build-out (flow assurance + choke management + well integrity during production)"
issue: 87
status: plan-review
created: 2026-05-16
last_updated: 2026-05-16
public_safety: API/SPE/NACE/ISO standards anchors + original concept authoring; NO vendor-confidential inhibitor chemistry recipes; NO proprietary multiphase-flow simulator algorithm internals; cite vendor by name + general chemistry class only
---

# Issue #87 Plan — PE Phase 4 (Flow Assurance + Choke Management + Well Integrity During Production)

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#87](https://github.com/vamseeachanta/llm-wiki/issues/87) — to be created by main session with `status:plan-review` label after this plan is committed
- Local plan status: `plan-review` (NOT `plan-approved` — user-approval gate is load-bearing per [[feedback_never_offer_to_self_label_plan_approved]])
- Implementation status: not started; awaiting adversarial review + user approval
- Predecessors (all CLOSED): [Phase 1 #61](https://github.com/vamseeachanta/llm-wiki/issues/61), [Phase 2 #73](https://github.com/vamseeachanta/llm-wiki/issues/73), [Phase 3 #74](https://github.com/vamseeachanta/llm-wiki/issues/74) — Phase 3 closed 2026-05-16 in commits [`d2b45293`](https://github.com/vamseeachanta/llm-wiki/commit/d2b45293) + [`3b6a2b08`](https://github.com/vamseeachanta/llm-wiki/commit/3b6a2b08) + [`9c856bda`](https://github.com/vamseeachanta/llm-wiki/commit/9c856bda)
- PE wiki current state: **54 pages** (post-Phase 3); Phase 4 target ~64-67

## Resource intelligence

**Sources consulted:**

1. **PE overview** (`wikis/production-engineering/wiki/overview.md` lines 71-75) — definitive Phase 4 scope: flow assurance (paraffin/hydrate/scale/asphaltene), choke management, well integrity during production (corrosion + scale + paraffin monitoring + intervention triggers)
2. **PE wiki concepts directory** (`wikis/production-engineering/wiki/concepts/`) — 40 concept pages already landed (post-Phase 3); confirmed NO existing flow-assurance / choke / well-integrity concept pages
3. **PE wiki standards directory** (`wikis/production-engineering/wiki/standards/`) — 13 standards pages landed (API RP 11* series, API RP 19B, API RP 39, API SPEC 11*, API SPEC 14A, ISO 17824); no API RP 14C, no ISO 21457, no NACE SP0106
4. **engineering-standards wiki** — existing pages relevant to Phase 4: `api-rp-14e.md` (erosional-velocity criterion, primary flow-assurance anchor), `api-rp-17b.md` (subsea flexible-pipe, adjacent), `api-rp-581.md` (RBI, well-integrity-adjacent), `ampp-mr-0175-*.md` (sour-service, 4 pages already), `ampp-sp0775.md` (corrosion coupons), `nace-34103.md` (adjacent); cross-link rather than duplicate. Concept pages: `corrosion-rate-measurement.md`, `electrochemical-corrosion.md`, `pitting-and-crevice-corrosion.md`, `stress-corrosion-cracking.md`, `microbiologically-influenced-corrosion.md`, `mooring-integrity-management.md` (10 corrosion-family concepts in eng-standards — significant cross-link opportunity)
5. **marine-engineering wiki** — `concepts/corrosion-control.md` exists; PE well-corrosion is different scope (internal production-tubing corrosion vs external marine structural corrosion); cross-link with explicit scope distinction
6. **drilling-engineering wiki** — `concepts/pa-barrier-philosophy.md`, `concepts/cement-evaluation.md`, `concepts/primary-cementing.md`, `concepts/cement-job-execution.md` are the well-construction-integrity anchors; PE Phase 4 well-integrity is OPERATING-time degradation only — scope-edge boundary must be explicit
7. **Phase 3 plan** ([`docs/plans/2026-05-15-issue-74-pe-phase-3-stimulation.md`](2026-05-15-issue-74-pe-phase-3-stimulation.md)) — shape template; section structure adopted here; landing commits demonstrate the framing precedent for vendor-archetype + paywall-discipline patterns
8. **Phase 3 exit handoff** ([`workspace-hub/docs/session-handoffs/2026-05-16-epic-74-pe-phase-3-stimulation-exit.md`](https://github.com/vamseeachanta/workspace-hub/blob/main/docs/session-handoffs/2026-05-16-epic-74-pe-phase-3-stimulation-exit.md)) — two-batch dispatch strategy validated; carries forward to Phase 4
9. **Calc-citation contract** (`workspace-hub/.claude/rules/calc-citation-contract.md`, #2481, #2685) — applies to V_e erosional-velocity formula (API RP 14E), corrosion-rate (NACE), scale-prediction (Oddo-Tomson SI), paraffin wax-appearance-temperature (correlations), hydrate stability (van der Waals-Platteeuw)
10. **Service-provider data routing** (`llm-wiki/docs/governance/service-provider-data-routing.md`) — 6-row matrix; vendor inhibitor recipes off-repo, public NACE/SPE/textbook on-repo

**Gaps identified:**

- No `wikis/production-engineering/wiki/concepts/flow-assurance.md` exists (or any of its sub-pages: multiphase-flow / paraffin / asphaltene / scale / hydrate / erosional-velocity)
- No `wikis/production-engineering/wiki/concepts/choke-management.md` exists (or sub-pages: choke-types / multiphase-choke-modeling / sand-laden-duty)
- No `wikis/production-engineering/wiki/concepts/well-integrity-during-production.md` exists (or sub-pages: corrosion-management / scale-management / paraffin-management / asphaltene-management / integrity-monitoring / intervention-triggers)
- No `wikis/production-engineering/wiki/standards/api-rp-14c.md` exists (PE-specific or cross-link to engineering-standards if it gets added there)
- No `wikis/production-engineering/wiki/standards/iso-21457.md` exists
- No `wikis/production-engineering/wiki/standards/nace-sp0106.md` exists
- `wikis/production-engineering/wiki/index.md` requires page-count and table-row updates post-build
- `wikis/production-engineering/wiki/log.md` requires 3 new iter entries

## Public-safety boundary

**Allowed:**

- API / SPE / NACE / ISO recommended-practices ingest at the standards-page level (`code_id`, `publisher`, `revision` — L0-prose enforcement per `wikis/production-engineering/CLAUDE.md`)
- Original concept authoring with corrosion-rate / scale / paraffin / hydrate formulas under the calc-citation contract
- Multiphase-flow correlation formulas (Beggs-Brill 1973, Hagedorn-Brown 1965, Duns-Ros 1963, Gray 1974) — public-domain SPE-paper anchors with DOI references
- Multiphase choke models (Sachdeva 1986 SPE 15657, Perkins 1993 SPE 20633, Ashford-Pierce 1975 SPE 5482) — public SPE-paper anchors
- Hydrate-stability framework (van der Waals-Platteeuw 1959, CSMHYD academic reference, Sloan & Koh *Clathrate Hydrates of Natural Gases* 3rd ed Wiley 2007 ISBN 978-0-8493-9078-4)
- Bai & Bai *Subsea Engineering Handbook* (Elsevier 2010 ISBN 978-1-85617-689-7) — flow-assurance reference textbook
- Brill & Mukherjee *Multiphase Flow in Wells* (SPE Monograph 17, 1999) — well-flow textbook
- NACE corrosion-handbook + Schweitzer *Corrosion of Linings & Coatings* + ASM Metals Handbook Vol 13 — corrosion-management public references
- Public state-RRC and regulator-side guidance on intervention triggers (Texas RRC W-1H, BSEE NTLs) — public-domain anchors
- Vendor archetypes (cite-by-name only): Schlumberger flow-assurance services, Halliburton MultiChem, Baker Hughes ProductionQuest, Champion-X / Nalco production-chemistry — name-level only, no proprietary inhibitor recipes

**Forbidden:**

- Vendor-confidential inhibitor chemistry recipes (proprietary paraffin / scale / corrosion / asphaltene / hydrate-inhibitor formulations) — name vendor + general chemistry-class only (e.g. "polyacrylate-based scale inhibitor")
- Verbatim copying of paragraphs >30 words from API / SPE / NACE / ISO standards (paraphrase + cite per Phase 3 #85 precedent)
- Multiphase-flow simulator algorithm internals (OLGA, LedaFlow, PIPESIM, MEPO, FlowManager, K-Spice) — cite by name as "industry-standard multiphase-flow simulators" per the Phase 3 #85 framing precedent
- Citation of pages under `wikis/*/wiki/sources/` per [workspace-hub#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) deny-list
- Vendor production-chemistry datasheets (cite vendor + general class without proprietary performance curves)
- Operator-confidential well-integrity intervention case-studies (cite SPE-paper anonymized field cases only)

### Vendor-citation allowed / blocked examples (per Codex r2 MAJOR-5)

The "cite vendor by name + general chemistry class only" policy creates a silent-failure path where implementers may cite vendor marketing pages and think they have complied. The following examples clarify the operational boundary:

**ALLOWED** (cite-by-name + chemistry-class only):
- "Champion-X markets paraffin inhibitors based on polyacrylate and EVA-copolymer chemistry"
- "Halliburton MultiChem provides production-chemistry services for paraffin, scale, asphaltene, and hydrate management"
- "LDHI families include kinetic hydrate inhibitors (KHI — typically vinyl-pyrrolidone or vinyl-caprolactam copolymer chemistry) and anti-agglomerants (AA — typically quaternary-ammonium chemistry)"
- "Nalco Champion (Ecolab) is a major supplier of scale inhibitors using phosphonate and polyphosphate chemistry families"
- "Industry-standard multiphase-flow simulators include OLGA, LedaFlow, PIPESIM, and K-Spice — proprietary algorithm internals are not reproduced in this wiki"

**BLOCKED** (proprietary detail — would fail `test_production_chemistry_deny_list.py`):
- "Champion-X XS-7000 achieves 12% wax-inhibition at 50 ppm per [vendor datasheet]"
- "Nalco EC9012 dosage of 80-120 ppm for North Sea brine, performance curve at 80°F vs 120°F"
- "Halliburton MC-1500 paraffin-inhibitor shows X% effectiveness in lab-screening matrix Y"
- "Baker Hughes ProductionQuest-A100 KHI provides subcooling protection to ΔT = 10°C at 0.5 wt%"
- Direct transcription of any vendor performance curve, dosage table, or lab-screening matrix

The discrimination test: ALLOWED references describe the **class** of chemistry and the **vendor's market position**. BLOCKED references contain **quantitative performance claims** tied to **specific commercial products** that originate from vendor marketing or datasheets.

## Deliverable

Phase 4 corpus expansion adding 3 sub-issues each landing concept-page cluster + ≥1 standards-page-or-cross-link, growing `wikis/production-engineering/wiki/` from post-Phase-3 state of 54 pages to target 64-67 pages. Cross-links established between Phase 4 operational scope and Phases 1/2/3 design/intervention scopes + cross-domain anchors to drilling-engineering (well-construction integrity hand-off) + engineering-standards (corrosion-family concepts already landed).

## Artifact map

| Artifact | Path |
|---|---|
| This plan | `llm-wiki/docs/plans/2026-05-16-issue-87-pe-phase-4-flow-assurance-choke-integrity.md` |
| Sub-issue 1 (flow assurance) — new | created during execution; title `research+ingest(production-engineering): flow assurance — multiphase flow + erosional-velocity + paraffin/asphaltene/scale + hydrate management` |
| Sub-issue 2 (choke management) — new | title `research+ingest(production-engineering): choke management — choke types + multiphase choke modeling + sand-laden duty + ESD interlocks` |
| Sub-issue 3 (well integrity during production) — new | title `research+ingest(production-engineering): well integrity during production — corrosion / scale / paraffin / asphaltene + monitoring + intervention triggers` |
| Concept pages (~11-14, per Claude r1 MINOR-5 + MINOR-7 user-decisions) | `wikis/production-engineering/wiki/concepts/{flow-assurance,multiphase-flow-in-wells,vertical-flow-correlations,horizontal-inclined-flow,flow-regime-maps,erosional-velocity,paraffin-deposition,asphaltene-precipitation,mineral-scale,hydrate-management,choke-management,multiphase-choke-modeling,well-integrity-during-production,corrosion-management,integrity-monitoring,intervention-triggers}.md` (NOTE: `scale-paraffin-asphaltene-monitoring.md` folded into per-family pages per MINOR-5; `multiphase-flow-in-wells.md` pre-decomposed into router + 3 sub-pages per MINOR-7) |
| Standards pages | `wikis/production-engineering/wiki/standards/{api-rp-14c,iso-21457,nace-sp0106}.md` (or cross-links to engineering-standards where matching pages exist) |
| Wiki index update | `wikis/production-engineering/wiki/index.md` |
| Wiki log entries | `wikis/production-engineering/wiki/log.md` (one per sub-issue, 3 minimum) |
| Plan review — Claude | `scripts/review/results/2026-05-16-plan-87-claude.md` (T1 single-author, this drafting session) |
| Plan review — Codex (optional) | `scripts/review/results/2026-05-16-plan-87-codex.md` (T2 escalation if user requests cross-provider) |
| Plan review — disagreement (optional) | `scripts/review/results/2026-05-16-plan-87-disagreement.md` (T2 escalation if Codex disagrees with Claude r1) |

## Sub-issue scope breakdown

### Sub-issue 1 — Flow Assurance

**Pages to create (~4-5 concept + 0-1 standards):**

- `concepts/flow-assurance.md` — router/index page; flow-assurance scope (multiphase flow, erosional limits, deposition management — wax/asphaltene/scale/hydrate), thermal-hydraulic-chemical envelope concept, life-of-well planning vs operational-response framing
- `concepts/multiphase-flow-in-wells.md` — **router page** (per Claude r1 MINOR-7 decomposition) covering regime taxonomy (bubble, slug, churn, annular, mist), mechanistic-vs-empirical model choice, when each correlation applies, system-level synthesis. Links out to the 3 sub-pages below. Brill & Mukherjee SPE Monograph 17 anchor.
- `concepts/vertical-flow-correlations.md` — Hagedorn-Brown 1965 vertical-well correlation, Duns-Ros 1963 vertical-flow map, Gray 1974 wet-gas correlation. Each correlation's applicability envelope and historical/practitioner context.
- `concepts/horizontal-inclined-flow.md` — Beggs-Brill 1973 (SPE 4007) horizontal/inclined two-phase flow correlation; flow-pattern map for inclination angles; modern extensions.
- `concepts/flow-regime-maps.md` — Taitel-Dukler regime-transition maps, Mandhane vertical-flow map, observed-vs-predicted regime selection logic, instrument-and-measurement framework for regime identification in production wells.
- `concepts/erosional-velocity.md` — API RP 14E V_e = C/sqrt(rho_m) formula and C-factor jurisdictional debate (the well-known C=100 vs C=200+ erosion-controversy literature — Salama 1993 SPE 26569 + DNV RP O501 sand-erosion model). Cross-link to engineering-standards `api-rp-14e.md`. **Calc-citation entry candidate** (V_e formula + C-factor).
- `concepts/paraffin-deposition.md` — paraffin (n-alkane) deposition physics, wax-appearance-temperature (WAT) measurement (cross-polarized microscopy, DSC), wax-deposition modeling (molecular-diffusion mechanism, shear-stripping limit), inhibition families (pour-point depressants, dispersants, paraffin-inhibitor PPDs cite-by-class only), remediation (hot-oiling, mechanical pigging, solvent treatments). Reference: NACE corrosion-handbook + SPE OnePetro wax-management corpus + Hammami & Raines 1999 SPE 38776.
- `concepts/asphaltene-precipitation.md` — asphaltene SARA characterization, onset-pressure thermodynamic prediction (de Boer plot, asphaltene stability index ASI, modified Hirschberg + cubic equations of state for asphaltene phase behavior), inhibition (dispersants cite-by-class only, solvent washes), remediation (xylene/toluene treatments, mechanical removal). Reference: Hammami & Ratulowski 2007 *Asphaltenes, Heavy Oils, and Petroleomics* Springer ISBN 978-0-387-31734-2 + de Boer 1995 SPE 24987.
- `concepts/mineral-scale.md` — common scale families (CaCO3 calcite, BaSO4 barite, SrSO4 celestite, halite, iron sulfide, iron carbonate), scaling-tendency prediction (Oddo-Tomson 1994 saturation index, Stiff-Davis, Langelier), inhibition (phosphonate / polyacrylate / polymer chemistry cite-by-class only), remediation (acid jobs, mechanical milling, scale-dissolver treatments). Reference: NACE TM0374 brine-compatibility framework + Kelland *Production Chemicals for the Oil & Gas Industry* 2nd ed CRC ISBN 978-1-4398-7280-3.
- `concepts/hydrate-management.md` — natural-gas hydrate stability (van der Waals-Platteeuw 1959 statistical thermodynamic framework, CSMHYD academic predictive code), formation temperature/pressure envelope, prevention families (THI thermodynamic-inhibitors methanol/MEG, LDHI low-dosage-hydrate-inhibitors kinetic + anti-agglomerant cite-by-class only), once-formed remediation (depressurization, hot-oil circulation, methanol treatment). Reference: Sloan & Koh *Clathrate Hydrates of Natural Gases* 3rd ed Wiley 2007.

**Standards:**

- Cross-link to `wikis/engineering-standards/wiki/standards/api-rp-14e.md` (already landed) — primary erosional-velocity anchor
- New PE-side standards page deferred (no PE-specific flow-assurance standard exists — flow-assurance is operational not equipment-spec)

**Cross-links:**

- Phase 1 `concepts/electric-submersible-pumps.md` — ESP performance affected by hydrate / wax / scale deposition; flow-assurance is the operating-envelope constraint
- Phase 1 `concepts/gas-lift-overview.md` — gas-lift coverage interacts with hydrate formation when injection-gas dehydration is marginal
- Phase 3 `concepts/refrac.md` — refrac decisioning factors include cumulative flow-assurance-related downtime
- engineering-standards `concepts/corrosion-rate-measurement.md` — flow-assurance and corrosion both consume the same multiphase-flow context

### Sub-issue 2 — Choke Management

**Pages to create (~3-4 concept + 1 standards):**

- `concepts/choke-management.md` — router/index; choke families (positive/fixed-bore vs adjustable vs cage), well-deliverability matching framing, bean-up / bean-down operational procedure, ESD interlock context, choke-position-as-control-variable framing
- `concepts/choke-types.md` — fixed-bore / adjustable / cage / multistage choke architectures, materials (tungsten carbide, ceramic, stellite cite-by-class), sand-erosion-rated vs general-service, subsea vs surface duty
- `concepts/multiphase-choke-modeling.md` — Sachdeva 1986 (SPE 15657) critical-flow modeling, Perkins 1993 (SPE 20633) subcritical-flow extension, Ashford-Pierce 1975 (SPE 5482) early framework, Tangren-Dodge-Seifert critical-flow vs the modern Bertuzzi-Tek-Poettmann approaches. Public SPE-paper anchors. **Calc-citation entry candidate** (critical-flow formula).
- `concepts/choke-sand-erosion.md` — erosion-rated choke selection, sand-screen integration with choke selection, DNV RP O501 erosion model coupling, choke-replacement-frequency operational tracking

**Standards:**

- `standards/api-rp-14c.md` — Analysis, Design, Installation, and Testing of Safety Systems for Offshore Production Facilities (ESD logic, choke-coordinated shutdown, surface safety valves). NEW page — no engineering-standards equivalent currently. L0-prose `code_id: api-rp-14c` / `publisher: American Petroleum Institute` / `revision: "8th edition, 2017 (Errata 1, 2018)"` per fact-verification 2026-05-16. **NOTE:** title is "Production Facilities" (8th ed nomenclature) not "Production Platforms" (predates 7th ed).
- Cross-link to existing engineering-standards `api-rp-14e.md` — choke sizing tied to V_e erosional-velocity limit
- (Defer ISO 10417 SSV standards page to a future epic — adjacent, not core Phase 4)

**Cross-links:**

- Phase 1 `concepts/gas-lift-overview.md` — gas-lift coverage requires choke coordination on injection-gas side
- Phase 2 `concepts/perforating.md` — perforation-strategy interacts with choke-bean-up rates (flush-flow vs reservoir-deliverability-limited)
- Phase 4 sibling `concepts/flow-assurance.md` — choke pressure-drop interacts with hydrate-formation envelope and asphaltene-precipitation onset

### Sub-issue 3 — Well Integrity During Production

**Pages to create (~4-5 concept + 1-2 standards):**

- `concepts/well-integrity-during-production.md` — router/index; scope-boundary statement vs drilling-engineering well-construction integrity (PE side covers OPERATING-time degradation of installed barriers + tubular corrosion + chemical-deposit management + intervention triggers; DE side covers barrier ESTABLISHMENT). Cross-link to DE `pa-barrier-philosophy.md` + `cement-evaluation.md` with explicit hand-off.
- `concepts/corrosion-management.md` — internal corrosion mechanisms (CO2 sweet corrosion, H2S sour corrosion, microbiologically-influenced corrosion MIC, oxygen ingress, pitting), corrosion-rate prediction (de Waard-Milliams 1991 SPE 22210, Norsok M-506 model), inhibition families (filming amines, oxygen scavengers, biocides cite-by-class only). Cross-link to engineering-standards `concepts/electrochemical-corrosion.md`, `microbiologically-influenced-corrosion.md`, `pitting-and-crevice-corrosion.md`. **Calc-citation entry candidate** (corrosion-rate formula).
- `concepts/integrity-monitoring.md` — wall-thickness monitoring (ultrasonic, eddy-current, MFL, intelligent pigs at surface but PE scope is downhole), casing-pressure monitoring (annular pressure buildup APB diagnosis), downhole gauges (PDG permanent downhole gauges for pressure + temperature trending), corrosion-coupon programs (NACE SP0775 anchor). Cross-link to engineering-standards `ampp-sp0775.md` + `concepts/corrosion-rate-measurement.md`.
- `concepts/intervention-triggers.md` — when-does-a-workover-get-called decision framework: economic triggers (cumulative deferred production NPV vs intervention cost), risk-based triggers (RBI methodology per API RP 581), regulator-mandated triggers (BSEE NTLs, state RRC requirements), barrier-degradation triggers (API SIF safety-integrity-function-related). Cross-link to engineering-standards `api-rp-581.md`.
- ~~`concepts/scale-paraffin-asphaltene-monitoring.md`~~ — **FOLDED per Claude r1 MINOR-5 user-decision 2026-05-16**: monitoring methodology now appears as a "Monitoring" section in each of the deposition-family pages (`paraffin-deposition.md`, `asphaltene-precipitation.md`, `mineral-scale.md`) rather than as a standalone integrating page. Reduces redundancy; mirrors Phase 3 precedent (no separate monitoring page in #84/#85). Total Phase 4 page count target adjusts accordingly.

**Standards:**

- `standards/iso-21457.md` — Material selection and corrosion control for oil and gas production systems (NEW page, no engineering-standards equivalent currently). L0-prose `code_id` / `publisher` / `revision`.
- `standards/nace-sp0106.md` — Control of Internal Corrosion in Steel Pipelines (NEW page; engineering-standards-side has corrosion-family concept pages but not this SP). L0-prose.
- Cross-link to engineering-standards `ampp-mr-0175-*.md` (sour-service materials, already landed) and `ampp-sp0775.md` (corrosion coupons, already landed) and `api-rp-581.md` (RBI, already landed)

**Cross-links:**

- drilling-engineering `concepts/pa-barrier-philosophy.md` + `cement-evaluation.md` + `primary-cementing.md` — explicit scope-edge hand-off statement on both sides
- Phase 1 `concepts/electric-submersible-pumps.md` + `esp-failure-modes.md` — ESP failure-mode coverage interacts with corrosion-induced motor failures
- Phase 2 `concepts/sand-control.md` — sand-control screen integrity is part of well-integrity-during-production (operating-time degradation of installed gravel-pack)
- Phase 3 `concepts/refrac.md` — refrac decisioning intersects with well-integrity-during-production (refrac candidacy depends on cumulative integrity-state degradation)
- marine-engineering `concepts/corrosion-control.md` — explicit scope-distinction (marine = external structural, PE = internal production-tubing/casing)

## Sequencing recommendation

**Recommended order: Sub-issue 1 (flow assurance) → Sub-issue 2 (choke management) → Sub-issue 3 (well integrity during production).**

**Reasoning:**

1. **Flow assurance is the broadest sub-issue and lands foundational multiphase-flow content** that choke-management depends on (multiphase choke modeling assumes multiphase-flow context). Flow-assurance pages have to land first OR the choke-management `multiphase-choke-modeling.md` page can't cleanly cross-link upstream context.

2. **Choke management is the narrowest sub-issue and the second-most-mature scope** — fewer pages, fewer external dependencies, well-bounded public SPE-paper anchors. Lands second cleanly.

3. **Well-integrity-during-production lands third** because it consumes BOTH flow-assurance (scale/paraffin/asphaltene deposition is integrity-relevant) AND choke-management (choke-erosion-management is integrity-relevant) context. It's also the most cross-domain-sensitive sub-issue (DE well-construction-integrity hand-off + engineering-standards corrosion-family cross-links + marine-engineering scope-distinction).

**Execution-model recommendation:** **Two-batch parallel-author dispatch** per [[feedback_parallel_subagent_shared_target_manifest_deferral]] discipline validated on Phase 3:

- **Batch 1 (parallel, 2 subagents)**: Sub-issue 1 (flow assurance) + Sub-issue 2 (choke management) — disjoint topic surfaces, minimal shared-target conflict. Cross-link targets between them are forward-references that can be installed by the second sub-issue after the first lands.
- **Batch 2 (solo, 1 subagent)**: Sub-issue 3 (well integrity during production) — heaviest cross-link surface, including back to Batch 1 sub-issues; benefits from solo dispatch after Batch 1 has committed (per Phase 3 [[surprise 2 in exit handoff]] "solo subagent for trailing sub-issue is cleaner than 3-way parallel")

**Cross-phase dependency:** No predecessor-blocking; Phase 3 is CLOSED. Phase 4 can begin as soon as `status:plan-approved` is set by user.

## TDD test list (governance/safety tests)

| Test | What it verifies |
|---|---|
| `tests/test_completion_artifacts.py` (existing) | new pages pass schema check (frontmatter required fields, page format) |
| `tests/test_governance_artifacts.py` (existing) | no >30-word verbatim API/SPE/NACE/ISO chunks; no vendor proprietary content; no `sources/` deny-list citations |
| `tests/test_scan_source_families_safe.py` (existing) | new pages don't reference vendor-confidential PDFs |
| `tests/test_calc_citations.py` (existing, add cases) | new calc-citation entries (V_e, corrosion-rate, scale-SI, paraffin-WAT, hydrate-stability) match #2471 schema |
| `tests/test_production_chemistry_deny_list.py` (NEW per Codex r2 MAJOR-1) | new pages do NOT contain commercial inhibitor product names (e.g. Champion-X XS-*, Nalco EC-*, Halliburton MC-*, Baker Hughes ProductionQuest-* SKUs), dosage-rate citations with units (`X ppm`, `X-Y ppm`), or performance-curve transcriptions (`achieves X% inhibition at Y conditions`). Enforces the vendor-IP guard testability gap that Phase 3 vendor-archetype framing did not catch for production chemistry. |
| Validator scripts (direct invocation per [[feedback_local_venv_pytest_import_hang]]) | `python3 scripts/validate_completion_artifacts.py`, `python3 scripts/validate_governance_artifacts.py`, `python3 scripts/validate_llms_manifests.py` |

No runtime calc to reproduce — content-authoring scope. **Reproduction proofs: N/A**.

## Acceptance criteria

- [ ] 3 sub-issues created under this epic with `research+ingest(production-engineering):` prefix, in canonical numerical order (serialize `gh issue create` calls per [[feedback_parallel_gh_issue_create_reverses_numbers]])
- [ ] ≥10 concept pages landed across all 3 sub-issues (target 10-13)
- [ ] ≥1 standards page OR cross-link to `engineering-standards/` per sub-issue
- [ ] `wikis/production-engineering/wiki/index.md` — `page_count` bumped (54 → 64-67), `last_updated`, table rows added
- [ ] `wikis/production-engineering/wiki/log.md` — one iter entry per sub-issue (3 minimum)
- [ ] Bidirectional cross-links: Phase 4 ↔ Phase 2 (perforating, sand-control), Phase 4 ↔ Phase 3 (hydraulic-fracturing/refrac), Phase 4 ↔ Phase 1 (ESP, gas-lift)
- [ ] Scope-edge cross-link Phase 4 well-integrity ↔ drilling-engineering well-construction-integrity (pa-barrier-philosophy.md, cement-evaluation.md) — explicit hand-off on both sides
- [ ] Calc-citation entries for V_e (API RP 14E) + corrosion-rate (de Waard-Milliams or Norsok M-506) + scale-SI (Oddo-Tomson) + paraffin-WAT + hydrate-stability — flagged in plan, instrumented as wiki-side `citations:` frontmatter even if no calc module currently consumes them (establishes downstream contract)
- [ ] All tests pass post-build
- [ ] **(Per Codex r2 MAJOR-1)** Each new concept + standards page passes `test_production_chemistry_deny_list.py` (enumerated vendor-IP deny-list for production chemistry — see TDD test list above)
- [ ] Plan + adversarial review artifacts at `scripts/review/results/2026-05-16-plan-87-*.md`

## Risks and open questions

- **Risk:** Flow-assurance scope can balloon (multiphase-flow modeling alone is a 600-page topic in Brill-Mukherjee SPE Monograph 17). Mitigation: bound concept-page cluster to overview-level coverage; defer correlation deep-dives to sub-pages only if user approves scope expansion. Pages target 150-220 lines each per Phase 3 precedent.
- **Risk:** Multiphase-flow simulator names (OLGA, LedaFlow, PIPESIM, K-Spice) — algorithm details are confidential. Mitigation: cite by name as "industry-standard multiphase-flow simulators" per Phase 3 #85 frac-design simulator framing precedent.
- **Risk:** Vendor production-chemistry inhibitor recipes — biggest IP-leakage risk in Phase 4 (production chemistry is heavily proprietary). Mitigation: aggressive cite-by-class discipline (e.g. "polyacrylate-based scale inhibitor" not specific commercial product names with chemistry); reference Kelland *Production Chemicals* textbook for canonical chemistry framework.
- **Risk:** Well-integrity-during-production scope-collision with drilling-engineering well-construction-integrity — risk of accidentally re-covering cement-barrier integrity in PE wiki. Mitigation: explicit scope-edge statement on `concepts/well-integrity-during-production.md` router page top + bidirectional hand-off cross-links + r1 review checks this specifically.
- **Risk:** Engineering-standards corrosion-family concept pages (10 already landed) overlap with PE Phase 4 well-integrity coverage. Mitigation: PE pages stay focused on PRODUCTION-WELL-INTERNAL corrosion (CO2/H2S/MIC inside tubing); engineering-standards pages stay general (electrochemistry / cathodic protection). Cross-link rather than duplicate.
- **Risk:** Marine-engineering `corrosion-control.md` cross-scope conflict — marine = external structural marine corrosion (mooring, hull), PE = internal production-tubing/casing corrosion. Mitigation: explicit scope-distinction sentence on PE `concepts/corrosion-management.md` referencing the marine page with scope-difference framing.
- **Risk:** API RP 14E V_e C-factor controversy literature is contentious (C=100 vs C=150-300 depending on study). Mitigation: present BOTH the API-spec C=100 conservative value AND the Salama 1993 SPE 26569 + DNV RP O501 erosion-model alternative framings without endorsing either; this is the standard academic treatment.
- **Open:** Should `concepts/erosional-velocity.md` live in PE Phase 4 OR be promoted to engineering-standards as a cross-cutting concept? Recommend PE Phase 4 (production-engineering-specific operational framing); engineering-standards pages can cross-link.
- **Open:** Should ESD interlock coverage go in Phase 4 choke-management OR defer to a future safety-systems-focused PE phase? Recommend Phase 4 choke-management (ESD context is operationally inseparable from choke management) with API RP 14C standards-page anchor.
- **Open:** Calc-citation entries — wiki-side `citations:` frontmatter or sidecar files? Per `workspace-hub/.claude/rules/calc-citation-contract.md`, the canonical pattern is sidecar dict alongside calc-module return value. For wiki pages with no consuming calc module yet, recommend wiki-side `citations:` frontmatter list as the placeholder contract; downstream `digitalmodel` integration consumes those.

## Complexity: T2

**T2** — 3 sub-issues, 10-13 new concept pages, 2-3 new standards pages, multi-week scope, no runtime test surface, requires calc-citation entries for 5 formula families (adds rigor). Comparable to Phase 3 in shape (Phase 3 landed 12 pages in 2,105 lines across 3 sub-issues; Phase 4 targets 10-13 pages in ~1,800-2,500 lines).

T2 because:
- Multi-file write surface with cross-link coordination across phases
- Standards-anchor research load (API RP 14C, ISO 21457, NACE SP0106 are new; verify existence + revision before drafting standards pages)
- Cross-domain scope-edge work (PE↔DE well-integrity boundary, PE↔marine-eng corrosion scope-distinction, PE↔engineering-standards corrosion-family cross-links)
- Vendor-IP discipline is more sensitive than Phase 3 (production chemistry IP > frac chemistry IP)

NOT T3 because:
- No multi-repo coordination beyond standard llm-wiki + workspace-hub
- No runtime calc-execution scope
- Shape-template available from Phase 3 commits

Adversarial-review depth: **T1 single-author Claude (this drafting session)** per "scale depth not presence" discipline ([[feedback_always_adversarial_review_scale_depth]]). T2 escalation to Codex available if user requests cross-provider review (per Phase 3 plan's MINOR-5 follow-up).

## Adversarial review summary

**Round 1 — 2026-05-16** (single-author Claude per [[feedback_always_adversarial_review_scale_depth]] T1 floor; Claude review prompt explicitly adversarial per [[feedback_adversarial_review_stance]])

| Provider | Verdict | Key findings |
|---|---|---|
| Claude | MINOR-7 | (1) Brill-Mukherjee SPE Monograph number ambiguity — confirmed it IS Monograph 17 (1999), distinct from Economides-Nolte Reservoir Stimulation 3rd Ed (which is Wiley 2000, not an SPE Monograph). User-prompt-flagged ambiguity resolved; surface explicitly in plan body. (2) API RP 14C revision verification needed before drafting standards page (current edition is 8th 2017; verify availability before drafting). **RESOLVED 2026-05-16 via fact-verification subagent (HIGH confidence):** 8th edition (2017) + Errata 1 (2018); status Active; title is "Safety Systems for Offshore Production Facilities" not "Platforms" per 8th-ed nomenclature change. (3) ISO 21457 revision verification needed (2010 first ed; may have been revised). **RESOLVED 2026-05-16 via fact-verification subagent (HIGH confidence):** 1st edition (2010), reviewed and reconfirmed by ISO/TC 67 in 2024; status Active; no 2nd edition in progress. (4) `concepts/erosional-velocity.md` placement decision (PE vs engineering-standards) — recommend PE per operational-framing argument; surface as open question. (5) `concepts/scale-paraffin-asphaltene-monitoring.md` page risks redundancy with the three deposition-family individual pages — consider folding into `integrity-monitoring.md` OR keeping as integrated-operational-view page (different framing); flag as scope-decision for user. (6) Sub-issue 3 standards-page count is highest (2 new + 3 cross-links); consider whether to land ISO 21457 and NACE SP0106 in this epic or defer one to scope-control. (7) Multiphase-flow correlation page list (Beggs-Brill + Hagedorn-Brown + Duns-Ros + Gray) is intentionally broad — bound `multiphase-flow-in-wells.md` to ≤350 lines per Phase 3 page-length precedent OR split into sub-pages. |
| Codex | — | not run this round (T1 floor; T2 escalation deferred to user direction per "scale depth not presence" — appropriate for plan-scope where vendor-IP discipline is the dominant risk and that's well-bounded by Phase 3 precedent) |

**Overall result:** MINOR-2 (API RP 14C revision) + MINOR-3 (ISO 21457 revision) RESOLVED 2026-05-16 via fact-verification subagent (HIGH confidence, both standards verified Active with current revisions noted above). Approval-ready after user-decision on MINOR-1 (PE-vs-DE well-integrity boundary enforcement), MINOR-4 (`erosional-velocity.md` placement), MINOR-5 (monitoring page consolidation), MINOR-6 (sub-issue 3 standards-page scope-control), and MINOR-7 (multiphase-flow page decomposition).

**Round 2 — 2026-05-16** (Codex r2 via direct `codex exec` CLI, session id `019e3171-4904-7e82-980f-aa4b09e8a2b6`)

| Provider | Verdict | Key findings |
|---|---|---|
| Codex | MAJOR-5 | (1) Vendor-IP guard NOT testable for production chemistry. (2) Calc-citation contract half-activated. (3) Multiphase-flow scope risk is formula-transcription drift not page-length. (4) PE-vs-DE boundary needs enforceable test not prose. (5) Vendor citation policy silent-failure — needs allowed/blocked example table. |

**Overall result r2 (consensus-vs-minority per [[feedback_codex_sustained_major_loop]]):** Codex r2 MAJOR-5 surfaced as user-judgment decision rather than auto-cycle. User chose path 2026-05-16: **partial patches — apply MAJOR-1 + MAJOR-5 only** (defer MAJOR-2/3/4 to sub-issue implementation time per Claude r1 MINOR-severity acceptance). Patches applied: (MAJOR-1) added `test_production_chemistry_deny_list.py` to TDD test list with enumerated commercial-product / dosage / performance-curve deny-list patterns + acceptance criterion; (MAJOR-5) added allowed/blocked vendor-citation example table to Public-safety boundary section. Full Codex r2 review at [`scripts/review/results/2026-05-16-plan-87-codex.md`](../../scripts/review/results/2026-05-16-plan-87-codex.md); disagreement summary at [`scripts/review/results/2026-05-16-plan-87-disagreement.md`](../../scripts/review/results/2026-05-16-plan-87-disagreement.md).

**Round 3 — 2026-05-16** (user-decision close-out on Claude r1 remaining MINORs)

All 5 Claude r1 user-decision MINORs resolved via AskUserQuestion 2026-05-16:

- **MINOR-1** (PE-vs-DE well-integrity boundary enforcement): user chose **prose-only boundary in plan + sub-issue acceptance criteria** (recommended). Lighter discipline consistent with the Codex-advisory acceptance posture; Phase 3 used prose-only and shipped clean. Codex MAJOR-4 deferred to sub-issue implementation if scope-creep surfaces.
- **MINOR-4** (`erosional-velocity.md` placement): user applied recommended default **PE Sub-issue 1**. Operational-framing wins per Phase 3 precedent (frac-design lives in PE not engineering-standards).
- **MINOR-5** (`scale-paraffin-asphaltene-monitoring.md` keep-or-fold): user chose **fold monitoring into per-family pages** (recommended). Less redundancy; Phase 3 had no separate monitoring page. Page count target adjusted: from 10-13 → 11-14 net after MINOR-7 decomposition.
- **MINOR-6** (Sub-issue 3 standards-page count): user chose **keep BOTH new standards (ISO 21457 + NACE SP0106)** (recommended). Scope-imbalance accepted (Sub-issue 3 = 4-5 concepts + 2 standards) given solo-batch dispatch absorbs it cleanly.
- **MINOR-7** (`multiphase-flow-in-wells.md` decomposition): user chose **pre-decompose into 3 pages** (recommended). Router + `vertical-flow-correlations.md` + `horizontal-inclined-flow.md` + `flow-regime-maps.md`. Mirrors Phase 3 #85 hyd-frac precedent (1 router + 3 sub-pages).

**Final approval state:** all r1 MINORs RESOLVED; r2 MAJORs handled (1+5 applied, 2/3/4 deferred). Plan is **approval-ready**. User explicit approval-action (label flip to `status:plan-approved` + write `.planning/plan-approved/87.md` marker) is the remaining gate. Review artifact: [`scripts/review/results/2026-05-16-plan-87-claude.md`](../../scripts/review/results/2026-05-16-plan-87-claude.md).

**NOT self-approved.** User-approval gate (`status:plan-approved` label) is load-bearing per [[feedback_never_offer_to_self_label_plan_approved]].
