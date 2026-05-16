---
title: "Issue #92 plan — Production Engineering Phase 5 corpus build-out (production accounting + regulatory reporting + surface-handover + data integration)"
issue: 92
status: plan-review
created: 2026-05-16
last_updated: 2026-05-16
public_safety: API MPMS / 30 CFR 250 / Texas RRC / ISA-95 standards anchors + FracFocus public-registry framing + original concept authoring; NO proprietary SCADA tag schemas or licensed protocol implementation internals; cite SCADA + measurement vendors by name + general class only
---

# Issue #92 Plan — PE Phase 5 (Production Accounting + Regulatory Reporting + Surface-Handover + Data Integration)

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#92](https://github.com/vamseeachanta/llm-wiki/issues/92) — to be created by main session with `status:plan-review` label after this plan is committed
- Local plan status: `plan-review` (NOT `plan-approved` — user-approval gate is load-bearing per [[feedback_never_offer_to_self_label_plan_approved]])
- Implementation status: not started; awaiting adversarial review + user approval
- Predecessors (all CLOSED): [Phase 1 #61](https://github.com/vamseeachanta/llm-wiki/issues/61), [Phase 2 #73](https://github.com/vamseeachanta/llm-wiki/issues/73), [Phase 3 #74](https://github.com/vamseeachanta/llm-wiki/issues/74), [Phase 4 #87](https://github.com/vamseeachanta/llm-wiki/issues/87) — Phase 4 closed 2026-05-16
- PE wiki current state: **75 pages** (post-Phase 4); Phase 5 target ~87-90

## Resource intelligence

**Sources consulted:**

1. **PE overview** (`wikis/production-engineering/wiki/overview.md` lines 19-28) — Phase 5 scope is **NOT pre-named in the seed roadmap** (lines 49-77 cover Phases 1-4 only). This is a framing difference vs Phases 2-4 (which were named at founding-time). However the **Scope (in)** block (lines 19-28) explicitly enumerates:
   - line 27 — "Production-side regulatory and reporting — allowable rates, GOR limits, gas flaring rules, production accounting"
   - line 26 — "Surface-handover boundary — flowline tie-in to manifold, choke skid, separator inlet conditions"
   - These are the founding-scope-intent surfaces Phase 5 closes out. The seed roadmap's silence on Phase 5 is a roadmap-incompleteness artifact, not a scope-out signal — confirmed by the Scope (in) enumeration.
   - **Data integration (SCADA / historian)** is implied by line 24 ("production operations") but never explicitly named. Phase 5 adds it explicitly as a foundational surface for the production-side regulatory + accounting coverage (no SCADA = no allocation = no reporting).
2. **PE wiki concepts directory** (`wikis/production-engineering/wiki/concepts/`) — 59 concept pages landed (post-Phase 4); confirmed NO existing production-accounting / measurement / allocation / well-test / GOR-tracking / custody-transfer / allowable-rate / regulatory-reporting / SCADA / historian / surface-handover / manifold-tie-in / choke-skid / separator-inlet concept pages
3. **PE wiki standards directory** (`wikis/production-engineering/wiki/standards/`) — 16 standards pages landed; NO API MPMS, NO ISA-95, NO 30 CFR 250, NO FracFocus framing page
4. **engineering-standards wiki** — searched for cross-link candidates: no `api-mpms-*.md`, no `isa-95.md`, no `iec-62443.md` pages currently exist; no `30-cfr-250.md`. These are net-new standards-anchor pages for PE Phase 5.
5. **PE wiki index + log** — already reference 30 CFR 250 Subpart H + BSEE NTLs + Texas RRC Statewide Rules in Phase 4 log entry (well-integrity context), and the PE overview's Scope (in) names production reporting + flaring; Phase 5 promotes these from incidental mentions to dedicated concept-page coverage
6. **Phase 4 plan** (`docs/plans/2026-05-16-issue-87-pe-phase-4-flow-assurance-choke-integrity.md`) — full shape template (292 lines). Section structure adopted here. Phase 4 framing precedents carried forward: vendor-archetype + paywall-discipline + calc-citation candidate flagging + two-batch dispatch + allowed/blocked vendor-citation example table (per Codex r2 MAJOR-5 in Phase 4).
7. **Phase 4 exit handoff** (`workspace-hub/docs/session-handoffs/2026-05-16-epic-87-pe-phase-4-flow-assurance-exit.md`) — two-batch dispatch validated; surfaces Codex r2 MAJOR-2 lesson (calc-citation contract half-activation — don't punt to ambiguous middle); carries forward as explicit Phase 5 decision
8. **Phase 4 approval marker** (`.planning/plan-approved/87.md`) — user-decision close-out pattern (5 MINORs resolved via AskUserQuestion); Phase 5 anticipates similar pattern
9. **Calc-citation contract** (`workspace-hub/.claude/rules/calc-citation-contract.md`, #2481, #2685) — applies to allocation-factor formula (well-test reconciliation residual), measurement-uncertainty propagation (API MPMS Chapter 14.3), allowable-rate calculation framework (Texas RRC W-1H/W-2 formulas where they exist)
10. **Service-provider data routing** (`llm-wiki/docs/governance/service-provider-data-routing.md`) — 6-row matrix; SCADA vendor brochures off-repo, FracFocus public registry + 30 CFR 250 federal text + Texas RRC public rules on-repo; ISA-95 paywalled standard paraphrase only
11. **Production-engineering CLAUDE.md** (lines 14-15) — "Production-side regulatory" is explicitly in-scope, confirming Phase 5 alignment with wiki schema

**Gaps identified:**

- No `wikis/production-engineering/wiki/concepts/production-allocation.md` exists (or sub-pages: well-test-and-reconciliation, gor-and-water-cut-tracking, custody-transfer-overview, flow-measurement-uncertainty)
- No `wikis/production-engineering/wiki/concepts/production-allowable-rates.md` exists (or: state-production-reporting, federal-production-reporting, chemical-disclosure-fracfocus, gas-flaring-rules)
- No `wikis/production-engineering/wiki/concepts/surface-handover-boundary.md` exists (or: manifold-tie-in, choke-skid-and-separator-inlet, production-scada-architecture, production-data-historian-patterns)
- No `wikis/production-engineering/wiki/standards/api-mpms-*.md` exists — MPMS Chapter 20 (allocation measurement) is the most central chapter for Phase 5 scope
- No `wikis/production-engineering/wiki/standards/30-cfr-250.md` exists — federal-regulatory framework anchor
- No `wikis/production-engineering/wiki/standards/isa-95.md` exists — manufacturing-control hierarchy anchor (data integration)
- `wikis/production-engineering/wiki/index.md` requires page-count and table-row updates post-build (75 → 87-90 target)
- `wikis/production-engineering/wiki/log.md` requires 3 new iter entries
- `wikis/production-engineering/wiki/overview.md` seed-roadmap section (lines 49-77) should be amended to add **Phase 5** as a now-named-not-just-implied scope (cleanup the founding-roadmap silence noted in source #1 above)

## Public-safety boundary

**Allowed:**

- **Public federal regulatory text** — 30 CFR 250 (BSEE production reporting), 30 CFR 1206 (ONRR royalty production), 30 CFR 1210 (ONRR reporting) — federal regulations are public-domain. Cite by CFR section number; paraphrase prose where verbatim chunks would exceed 30 words.
- **Public state regulatory text** — Texas RRC Statewide Rules (rrc.texas.gov), W-1H (drilling permit), W-2 (oil-well completion), G-1 (gas-well completion), P-4 (operator designation), PR (monthly production report). State regulations are public-domain. Cite by rule number; paraphrase prose.
- **Public regulatory disclosure registries** — FracFocus.org (fracfocus.org) chemical disclosure data is publicly disclosed + machine-readable. Cite by URL + disclosure-record reference; do NOT ingest bulk-disclosure CSV/JSON into the repo (license-discipline — surface as MINOR in r1 review). Treat as "regulator-adjacent disclosure framework" not as a code or standard.
- **API MPMS (Manual of Petroleum Measurement Standards)** — Chapter 20 (allocation measurement), Chapter 14.3 (uncertainty), Chapter 21 (electronic measurement), other chapters as needed. Paywalled. Paraphrase only, no verbatim >30 words. L0-prose enforcement: `code_id` / `publisher: American Petroleum Institute` / `revision` required.
- **ISA-95 (Enterprise-Control System Integration)** — IEC 62264 international counterpart. Paywalled. Manufacturing-control hierarchy levels (L0 sensors / L1 control / L2 supervisory / L3 MES / L4 ERP) are public-knowledge taxonomy; paraphrase structural intent without verbatim text.
- **Public SPE and academic literature** — production-allocation methods (Cramer 1995 SPE 27602 well-test reconciliation framework, ProTechnics tracer-based allocation public papers), GOR/water-cut tracking (Fetkovich 1973 SPE 4629 + decline-curve corpus), measurement uncertainty (Cramer Rao bounds in measurement-statistics literature)
- **Textbook references** — Speers & Tendler *Subsea Production Allocation* (PennWell), Miesner & Leffler *Oil & Gas Production in Nontechnical Language* (PennWell), McAllister *Pipeline Rules of Thumb* (Elsevier) — public textbook anchors
- **Vendor archetypes (cite-by-name + general class only):**
  - SCADA / process-control: OSIsoft PI (now AVEVA PI System), AVEVA Process Optimization, Honeywell Experion, Emerson DeltaV, Schneider Electric EcoStruxure / Foxboro, Rockwell Automation PlantPAx, Siemens PCS 7, Yokogawa CENTUM VP, ABB 800xA
  - Production-allocation / well-test software: Emerson Roxar Tempest + ProAct, Schlumberger AvocetVx, Halliburton Landmark DecisionSpace Production, IBM Maximo Production
  - Flow measurement: Emerson (Daniel ultrasonic + Coriolis), Smith Meter (Gilbarco), FMC Technologies (TechnipFMC Smith), Sick Maihak ultrasonic, Krohne, Endress+Hauser, Halliburton MeasureSure, Schlumberger Vx multiphase metering, TechnipFMC PhaseWatcher

**Forbidden:**

- Verbatim copying of paragraphs >30 words from API MPMS / ISA-95 / IEC 62443 / IEC 62264 (paraphrase + cite per Phase 3+4 precedent)
- **SCADA vendor proprietary tag schemas, asset-models, protocol implementation internals** — OPC-UA implementation specifics, PI AF (Asset Framework) proprietary schema, DeltaV control-module internals, Experion CEE rule-set internals — cite by name as "industry-standard production-control systems" per the Phase 4 #87 multiphase-flow-simulator framing precedent
- **Vendor performance-curve / accuracy-spec transcription** — flow-meter accuracy curves at specific operating conditions, allocation-engine optimization-algorithm internals, vendor benchmark data from marketing collateral
- **Vendor SKU enumeration with quantitative claims** — e.g. "Daniel SeniorSonic 3413 achieves ±0.15% accuracy at conditions X" — cite vendor + general class without product-line-specific accuracy specs
- Citation of pages under `wikis/*/wiki/sources/` per [workspace-hub#2482](https://github.com/vamseeachanta/workspace-hub/issues/2482) deny-list
- **FracFocus bulk-download dataset** — public-disclosure-record level citation only; do NOT ingest the bulk CSV/JSON downloads into the repo (license is public-disclosure but bulk-redistribution warrants reviewer scrutiny; surface in r1)
- **Operator-confidential allocation case studies** — cite SPE-paper anonymized field cases only; no real-operator allocation-error case studies
- **Texas RRC + BSEE NTL verbatim quoting beyond 30 words** — even though federal/state text is public-domain, the wiki style is paraphrase-first; reserve verbatim for short rule-text citations only

### Vendor-citation allowed / blocked examples (SCADA + measurement specific, per Phase 4 #87 MAJOR-5 precedent)

The "cite vendor by name + general class only" policy creates a silent-failure path where implementers may cite vendor marketing pages and think they have complied. The following examples clarify the operational boundary for SCADA + measurement vendor coverage:

**ALLOWED** (cite-by-name + general-class only):
- "OSIsoft PI System (now AVEVA PI System) is an industry-standard production data historian deployed widely across upstream operators"
- "Emerson DeltaV and Honeywell Experion are common DCS platforms for offshore production-host facilities; Schneider EcoStruxure / Foxboro, Rockwell PlantPAx, and Siemens PCS 7 are alternatives"
- "Coriolis mass-flow meters are supplied by Emerson (Micro Motion), Endress+Hauser, KROHNE, and Yokogawa, among others; the operating principle is independent of vendor"
- "Multiphase flow meters for production allocation are offered by Schlumberger (Vx), TechnipFMC (PhaseWatcher), Roxar (now Emerson), and others"
- "FracFocus (fracfocus.org) is the public chemical-disclosure registry operated by GWPC and IOGCC; participating states use it to satisfy hydraulic-fracturing chemical-disclosure rules"

**BLOCKED** (proprietary detail — would fail `test_production_chemistry_deny_list.py` extended for SCADA + measurement):
- "AVEVA PI AF (Asset Framework) tag-naming convention follows the proprietary schema X for production-data normalization"
- "Daniel SeniorSonic 3413 ultrasonic meter achieves ±0.15% accuracy in custody-transfer service at 200 bar, 50°C"
- "Emerson Roxar Tempest allocation engine uses the proprietary objective-function Y for well-test reconciliation"
- "Honeywell Experion CEE control-rule pattern Z for choke-control coordination during ESD events"
- Direct transcription of any vendor performance curve, allocation-algorithm internals, or proprietary tag-schema documentation

The discrimination test: ALLOWED references describe the **class** of system and the **vendor's market position**. BLOCKED references contain **quantitative performance claims** or **proprietary implementation details** tied to **specific commercial products** that originate from vendor marketing, datasheets, or proprietary technical documentation.

## Deliverable

Phase 5 corpus expansion adding 3 sub-issues each landing concept-page cluster + ≥1 standards-page-or-cross-link, growing `wikis/production-engineering/wiki/` from post-Phase-4 state of **75 pages** to target **87-90 pages**. Cross-links established between Phase 5 reporting/handover/integration scope and Phases 1-4 operational scope + cross-domain anchors to engineering-standards (API MPMS), asset-management (production data → KPI lifecycle), and naval-architecture (FPSO topsides handover edge).

## Artifact map

| Artifact | Path |
|---|---|
| This plan | `llm-wiki/docs/plans/2026-05-16-issue-92-pe-phase-5-production-accounting-regulatory-handover.md` |
| Sub-issue 1 (production accounting + measurement) — new | created during execution; title `research+ingest(production-engineering): production accounting + measurement — allocation + well-test reconciliation + GOR/water-cut + custody transfer + measurement uncertainty` |
| Sub-issue 2 (regulatory reporting) — new | title `research+ingest(production-engineering): regulatory reporting — allowable rates + state (TX RRC W-1H/W-2/P-4) + federal (BSEE 30 CFR 250 / ONRR) + FracFocus + gas flaring rules` |
| Sub-issue 3 (surface-handover + data integration) — new | title `research+ingest(production-engineering): surface-handover + data integration — manifold tie-in + choke skid + separator inlet + SCADA architecture + production data historian` |
| Concept pages (~13-14 total target) | `wikis/production-engineering/wiki/concepts/{production-allocation,well-test-and-reconciliation,gor-and-water-cut-tracking,custody-transfer-overview,flow-measurement-uncertainty,production-allowable-rates,state-production-reporting,federal-production-reporting,chemical-disclosure-fracfocus,gas-flaring-rules,surface-handover-boundary,manifold-tie-in,choke-skid-and-separator-inlet,production-scada-architecture,production-data-historian-patterns}.md` |
| Standards pages | `wikis/production-engineering/wiki/standards/{api-mpms-chapter-20,30-cfr-250,isa-95}.md` (revision-research required at plan-time per MINOR — see r1 review) |
| Wiki index update | `wikis/production-engineering/wiki/index.md` |
| Wiki overview seed-roadmap update | `wikis/production-engineering/wiki/overview.md` — add Phase 5 to seed-roadmap section lines 49-77 (currently silent on Phase 5 per Resource intelligence source #1) |
| Wiki log entries | `wikis/production-engineering/wiki/log.md` (one per sub-issue, 3 minimum) |
| Plan review — Claude r1 | `scripts/review/results/2026-05-16-plan-92-claude.md` (T1 single-author, this drafting session) |
| Plan review — Codex r2 (optional) | `scripts/review/results/2026-05-16-plan-92-codex.md` (T2 escalation if user requests cross-provider) |

## Sub-issue scope breakdown

### Sub-issue 1 — Production Accounting + Measurement

**Pages to create (~5 concept + 1 standards):**

- `concepts/production-allocation.md` — router/index page; production-allocation problem statement (commingled-flow → per-well rates), allocation methods (test-separator-based, multiphase-meter-based, tracer-based, calculated-from-choke-and-PVT), allocation-uncertainty propagation, fiscal vs operational allocation distinction, single-well-host vs multi-well-host allocation. Reference: Cramer 1995 SPE 27602 + ProTechnics tracer literature + Speers & Tendler textbook.
- `concepts/well-test-and-reconciliation.md` — well-test procedure (bring well to test-separator, stabilize, integrate oil/gas/water rates over test duration), test-validation criteria, well-test-vs-continuous-measurement reconciliation (the "reconciliation residual" framework), well-test frequency vs allocation-accuracy trade-off, test-separator vs multiphase-meter operational distinction. **Calc-citation entry candidate** (well-test reconciliation residual formula). Reference: SPE OnePetro well-testing corpus.
- `concepts/gor-and-water-cut-tracking.md` — gas-oil-ratio (GOR / GOR_p / GOR_s solution-vs-produced) physics, water-cut (BS&W bottom-sediment-and-water) physics, time-series tracking methodology, deviation alarms tied to reservoir-management-and-integrity decisioning. Reference: Fetkovich 1973 SPE 4629 + standard PE textbook coverage.
- `concepts/custody-transfer-overview.md` — custody-transfer-vs-allocation-measurement distinction (custody = pipeline / sales-point hand-off, allocation = upstream-of-custody well-level apportionment), API MPMS Chapter 1-21 framework overview, custody-transfer measurement-uncertainty regime (typically ±0.25% to ±0.50% mass), proving / calibration discipline at the custody-transfer boundary. Cross-link to `standards/api-mpms-chapter-20.md` and (forward-reference) future MPMS Chapter 14 page.
- `concepts/flow-measurement-uncertainty.md` — measurement-uncertainty propagation framework (API MPMS Chapter 14.3 + ISO 5168 framework), individual instrument uncertainty (meter accuracy + repeatability + reproducibility), system-level uncertainty propagation (root-sum-square method, Monte Carlo propagation), allocation-uncertainty as a downstream consumer of measurement-uncertainty. **Calc-citation entry candidate** (uncertainty-propagation formula). Reference: API MPMS Chapter 14.3 + ISO 5168 (Measurement of fluid flow — Procedures for the evaluation of uncertainties).

**Standards:**

- `standards/api-mpms-chapter-20.md` — API Manual of Petroleum Measurement Standards Chapter 20 — Allocation Measurement. **Revision-research required at plan-time** (current chapter 20 has multiple parts — 20.1 Allocation Measurement, 20.2 Allocation Measurement by Mass-Difference, etc. — verify current revisions before drafting; surface as MINOR in r1 review). L0-prose `code_id: api-mpms-ch-20` / `publisher: American Petroleum Institute` / `revision: TBD-at-drafting`.
- (Defer dedicated API MPMS Chapter 14 page to follow-on epic; cross-reference in Chapter 20 page meanwhile)

**Cross-links:**

- Phase 1 `concepts/electric-submersible-pumps.md` — ESP-equipped wells require ESP-power data for allocation context (kWh per bbl tracking)
- Phase 1 `concepts/gas-lift-overview.md` — gas-lift wells have injection-gas allocation interleaved with production allocation
- Phase 4 `concepts/choke-management.md` — choke-position-as-control-variable feeds into the choke-based-rate-calculation allocation method
- Phase 4 `concepts/flow-assurance.md` — water-cut tracking is the leading indicator of scale-formation onset and corrosion-rate acceleration
- engineering-standards: cross-link to existing `standards/api-rp-14e.md` (where erosional-velocity in measurement piping enters the allocation context)
- asset-management `concepts/performance-standards.md` — allocation-uncertainty feeds into asset-level KPI confidence intervals

### Sub-issue 2 — Regulatory Reporting

**Pages to create (~5 concept + 1 standards — but see r1 MINOR-1 page-count discussion):**

- `concepts/production-allowable-rates.md` — router/index; "allowable" rate concept (state-imposed maximum-production-rate per well to manage waste / conservation / market-demand), MER (maximum efficient rate) vs allowable, the historical "Texas Railroad Commission allowable" prorationing mechanism (active 1930s-1972, residual today), modern allowable framework (well-by-well, field-by-field, basin-by-basin where state regulators retain authority), interaction with gas-flaring rules.
- `concepts/state-production-reporting.md` — state-level production-reporting framework: Texas RRC Form PR (monthly production), W-1H (horizontal drilling permit), W-2 (oil-well completion report), G-1 (gas-well completion report), P-4 (operator-designation, change-of-operator), state oil/gas commission portals (Oklahoma OCC, North Dakota Industrial Commission, Colorado COGCC/now ECMC, California CalGEM, Pennsylvania DEP, etc.). Reference: rrc.texas.gov + parallel state portals. Public-domain.
- `concepts/federal-production-reporting.md` — federal framework: BSEE 30 CFR 250 (production reporting for OCS leases — Subpart H Oil and Gas Production Safety Systems, Subpart K Oil and Gas Production Requirements), ONRR 30 CFR 1206 (royalty valuation) + 30 CFR 1210 (reporting). BSEE Notices to Lessees (NTLs) as supplementary guidance. Reference: bsee.gov + onrr.gov. Public-domain.
- `concepts/chemical-disclosure-fracfocus.md` — FracFocus.org chemical-disclosure registry framing — operated by GWPC + IOGCC, used by ~24 states + voluntary federal-side; chemical-disclosure-record contents (well API number, completion date, base fluid, chemical CAS numbers, ingredient concentration ranges, trade-secret claims). Reference: fracfocus.org + GWPC governance docs. Public-domain disclosure framework; treat as "regulator-adjacent disclosure registry", not a standard or code. **License-discipline framing**: cite by record-URL not by ingested-bulk-download (see r1 MINOR).
- `concepts/gas-flaring-rules.md` — gas-flaring regulatory landscape: state-level (Texas RRC Rule 32, ND Industrial Commission Order 24665, NM OCD venting/flaring rules), federal-level (BLM Methane Waste Reduction Rule history, EPA NSPS OOOOa-OOOOc), international (World Bank Zero Routine Flaring 2030 framework, GGFR initiative). Reference: state-portal links + bsee.gov + epa.gov + worldbank.org/GGFR. Public-domain. **Calc-citation entry candidate** (flare-rate calculation framework, where applicable).

**Standards:**

- `standards/30-cfr-250.md` — Code of Federal Regulations Title 30 Part 250 (BSEE — Oil and Gas and Sulfur Operations in the Outer Continental Shelf). Public-domain federal regulation. L0-prose `code_id: 30-cfr-250` / `publisher: U.S. Bureau of Safety and Environmental Enforcement (BSEE)` / `revision: current eCFR as-of date`. Note that 30 CFR 250 incorporates API RP 14C by reference (already a PE-wiki standards page) — surface the cross-link.
- (Texas RRC rules are referenced inline in `concepts/state-production-reporting.md` rather than as separate standards pages — state regulations are not "standards" in the API/ISO/NACE sense; surface as plan-time decision)

**Cross-links:**

- Phase 3 `concepts/hydraulic-fracturing.md` + `concepts/frac-fluids.md` — frac-fluid chemistry disclosure feeds into FracFocus
- Phase 4 `concepts/well-integrity-during-production.md` — BSEE 30 CFR 250 Subpart H well-integrity requirements feed into intervention-trigger framework
- Phase 4 `concepts/intervention-triggers.md` — regulator-mandated triggers (BSEE NTLs, state RRC requirements) already named in Phase 4; reverse-link from Phase 5
- engineering-standards `standards/api-rp-14c.md` (which IS a PE-wiki page) — 30 CFR 250 incorporates API RP 14C by reference
- asset-management `concepts/safety-critical-element-classification.md` — regulator-mandated SCE classification underpins production-reporting safety-system content

### Sub-issue 3 — Surface-Handover + Data Integration

**Pages to create (~5 concept + 1 standards):**

- `concepts/surface-handover-boundary.md` — router/index; the production-engineering / surface-facility-engineering scope boundary at the flowline-to-manifold tie-in; "where does PE responsibility end?" framing — PE owns wellhead → wing-valve → flowline → manifold-tie-in; facility-engineering owns manifold downstream → separator → treater → custody-transfer; choke skid sits ON the boundary (operationally part of PE control, physically often at manifold). Scope-edge cross-link to `naval-architecture/concepts/` where FPSO topsides processing is referenced (no overlap — naval-architecture covers the floater not the process; surface-facility-engineering wiki not yet founded).
- `concepts/manifold-tie-in.md` — flowline-to-manifold tie-in physics + operations: tie-in geometry (jumper / spool / direct-weld), pigging-receiver location at host, slugcatcher considerations on multiphase host flowlines, multi-well-manifold flow-coordination (header-design implications), insulation + heat-tracing requirements where flow-assurance hydrate/wax envelopes intersect with tie-in geometry. Reference: Bai & Bai *Subsea Engineering Handbook* + topside-engineering corpus.
- `concepts/choke-skid-and-separator-inlet.md` — choke-skid layout (multi-choke parallel for multi-well duty, single-choke serial for single-well duty), separator-inlet conditions (pressure, temperature, multiphase composition envelope, slug-handling capacity), separator-inlet-vs-choke-outlet pressure-drop budgeting, sand-handling considerations at the separator-inlet boundary. Cross-link to Phase 4 `concepts/choke-management.md` (already landed — bidirectional).
- `concepts/production-scada-architecture.md` — SCADA architecture for production-host operations: data-acquisition layer (RTU + PLC at well-pad, host-facility DCS), supervisory layer (control-room HMI + production-host-DCS), historian / data-platform layer (PI / equivalent), enterprise-MES layer (production-allocation engine, regulatory-reporting feeds). **Maps to ISA-95 levels L0-L4 framework**. Vendor archetypes (cite-by-name + general class only) — see Public-safety boundary section. Protocol context: Modbus / OPC-UA / IEC 61850 / DNP3 as the most-common SCADA protocols (cite by name + standardization body; do NOT transcribe protocol internals — surface as r1 MINOR for protocol-coverage scope-bound).
- `concepts/production-data-historian-patterns.md` — production-data-historian patterns: tag-naming conventions (operational practice — paraphrased structural intent only, NO proprietary tag-schemas), data-compression methods (swinging-door, boxcar), data-retention policies, data-quality framework (good/bad/uncertain quality bits per OPC-UA convention), integration with downstream consumers (allocation engine, regulatory-reporting engine, reservoir-management feed, asset-management performance-standard feed). Cybersecurity adjacency: surface IEC 62443 (industrial cybersecurity) as a related-but-out-of-scope anchor for Phase 5 — defer to a future cybersecurity-focused epic (surface as r1 open-question).

**Standards:**

- `standards/isa-95.md` — ISA-95 / IEC 62264 Enterprise-Control System Integration framework. Paywalled. **Revision-research required at plan-time** (ISA-95 has 5 parts; IEC 62264 is the international counterpart with its own part numbering — verify current revisions before drafting; surface as MINOR in r1 review). L0-prose `code_id: isa-95` / `publisher: International Society of Automation (ISA) + IEC` / `revision: TBD-at-drafting`. Paraphrase only.
- (Defer IEC 62443 / IEC 61850 / Modbus / OPC-UA / DNP3 to follow-on cybersecurity-and-protocols epic — surface as r1 open-question)

**Cross-links:**

- Phase 4 `concepts/choke-management.md` — surface-handover boundary INTERSECTS choke-skid (the most cross-link-dense linkage in Phase 5); choke-skid-and-separator-inlet bridges Phase 4 choke-management ↔ Phase 5 facility-handover
- Phase 4 `concepts/flow-assurance.md` — manifold-tie-in heat-tracing + insulation tied to flow-assurance hydrate/wax envelopes
- Phase 4 `concepts/well-integrity-during-production.md` — production data historian is the data-source for integrity-monitoring KPIs (wall-thickness trending, casing-pressure trending, downhole-gauge data)
- Sub-issue 1 `concepts/production-allocation.md` — production data historian feeds the allocation engine; explicit bidirectional cross-link
- Sub-issue 2 `concepts/state-production-reporting.md` + `concepts/federal-production-reporting.md` — production data historian feeds the regulatory-reporting engine; explicit bidirectional cross-link
- engineering-standards: no existing `isa-95.md` or `iec-62443.md` to cross-link to (new PE-side page; eng-std cross-link is forward-reference)
- asset-management `concepts/performance-standards.md` + `concepts/safety-critical-element-classification.md` — historian data → asset-management KPI lifecycle
- naval-architecture (NO direct cross-link — naval-architecture covers floater not process; surface explicit scope-distinction sentence on `surface-handover-boundary.md` per Phase 4 marine-engineering precedent)

## Sequencing recommendation

**Recommended order: Sub-issue 1 (production accounting) → Sub-issue 2 (regulatory reporting) → Sub-issue 3 (surface-handover + data integration).**

**Reasoning:**

1. **Production accounting + measurement lands first** — it's the foundational vocabulary (allocation, well-test, reconciliation, custody-transfer, measurement-uncertainty) that the other two sub-issues consume. Regulatory reporting (Sub-issue 2) is downstream of allocation in the data-flow; data integration (Sub-issue 3) is downstream of measurement in the data-flow.

2. **Regulatory reporting lands second** — narrower scope, well-bounded by public-domain regulator texts (30 CFR 250, Texas RRC rules, FracFocus). Depends on Sub-issue 1 vocabulary (allocation feeds into reporting) but no other dependencies.

3. **Surface-handover + data integration lands third** — heaviest cross-link surface (back to Phase 4 + Sub-issues 1+2 + asset-management + naval-architecture). Production data historian patterns specifically consume the allocation + reporting vocabulary established in Sub-issues 1+2. ISA-95 standards anchor is the trickiest revision-verification + scope-bound (surface as r1 MINORs).

**Execution-model recommendation:** **Two-batch parallel-author dispatch** per [[feedback_parallel_subagent_shared_target_manifest_deferral]] discipline validated on Phases 3 + 4:

- **Batch 1 (parallel, 2 subagents)**: Sub-issue 1 (production accounting + measurement) + Sub-issue 2 (regulatory reporting) — disjoint topic surfaces (allocation/measurement vs regulatory-text), minimal shared-target conflict. Cross-link targets between them are forward-references that can be installed by the second sub-issue after the first lands.
- **Batch 2 (solo, 1 subagent)**: Sub-issue 3 (surface-handover + data integration) — heaviest cross-link surface, including back to Batch 1 sub-issues AND back to Phase 4 #87 (choke-management is the densest single-page back-link); benefits from solo dispatch after Batch 1 has committed (per Phases 3+4 [[surprise 2 in exit handoff]] "solo subagent for trailing sub-issue is cleaner than 3-way parallel")

**Cross-phase dependency:** No predecessor-blocking; Phase 4 is CLOSED. Phase 5 can begin as soon as `status:plan-approved` is set by user.

## TDD test list (governance/safety tests)

| Test | What it verifies |
|---|---|
| `tests/test_completion_artifacts.py` (existing) | new pages pass schema check (frontmatter required fields, page format) |
| `tests/test_governance_artifacts.py` (existing) | no >30-word verbatim API MPMS / ISA-95 / 30 CFR / Texas RRC chunks; no vendor proprietary content; no `sources/` deny-list citations |
| `tests/test_scan_source_families_safe.py` (existing) | new pages don't reference vendor-confidential PDFs / SCADA proprietary documentation |
| `tests/test_calc_citations.py` (existing, add cases) | new calc-citation entries (allocation-factor formula, well-test-reconciliation residual, measurement-uncertainty propagation per API MPMS 14.3, flare-rate calculation) match #2471 schema |
| `tests/test_production_chemistry_deny_list.py` (EXTEND per Phase 4 #87 Codex r2 MAJOR-1 precedent — extend deny-list to SCADA + measurement vendors) | new pages do NOT contain commercial SCADA / measurement product names with quantitative performance claims (e.g. "Daniel SeniorSonic 3413 ±0.15% accuracy", "Roxar Tempest objective-function Y", "PI AF schema X"), proprietary tag-schemas, or licensed-protocol implementation internals. Enforces the vendor-IP guard testability gap that Phase 4 production-chemistry deny-list did not yet cover for SCADA + measurement vendor archetypes. |
| Validator scripts (direct invocation per [[feedback_local_venv_pytest_import_hang]]) | `python3 scripts/validate_completion_artifacts.py`, `python3 scripts/validate_governance_artifacts.py`, `python3 scripts/validate_llms_manifests.py` |

No runtime calc to reproduce — content-authoring scope. **Reproduction proofs: N/A**.

## Acceptance criteria

- [ ] 3 sub-issues created under this epic with `research+ingest(production-engineering):` prefix, in canonical numerical order (serialize `gh issue create` calls per [[feedback_parallel_gh_issue_create_reverses_numbers]])
- [ ] ≥12 concept pages landed across all 3 sub-issues (target 13-15: Sub-issue 1 ~5, Sub-issue 2 ~5, Sub-issue 3 ~5)
- [ ] ≥1 standards page OR cross-link to `engineering-standards/` per sub-issue (3 new PE-side standards pages: api-mpms-chapter-20, 30-cfr-250, isa-95)
- [ ] `wikis/production-engineering/wiki/index.md` — `page_count` bumped (75 → 87-90), `last_updated`, table rows added
- [ ] `wikis/production-engineering/wiki/overview.md` — seed-roadmap section (lines 49-77) amended to add Phase 5 entry (cleanup the founding-roadmap silence noted in Resource intelligence source #1)
- [ ] `wikis/production-engineering/wiki/log.md` — one iter entry per sub-issue (3 minimum)
- [ ] Bidirectional cross-links: Phase 5 ↔ Phase 4 (choke-management ↔ choke-skid-and-separator-inlet is densest), Phase 5 ↔ Phase 3 (hydraulic-fracturing/frac-fluids ↔ chemical-disclosure-fracfocus), Phase 5 ↔ Phase 2 (perforating completion-reporting integration), Phase 5 ↔ Phase 1 (ESP/gas-lift well-test framework)
- [ ] Scope-edge cross-link Phase 5 surface-handover ↔ naval-architecture (no overlap; explicit scope-distinction sentence)
- [ ] Calc-citation entries for allocation-factor formula + well-test-reconciliation residual + measurement-uncertainty propagation (API MPMS 14.3 framework) + flare-rate calculation — **decide at plan-time whether each is wiki-side `citations:` frontmatter metadata OR a real calc-citation sidecar contract entry per Phase 4 #87 Codex r2 MAJOR-2 lesson**; do NOT punt to ambiguous middle. See "Risks and open questions" — flagged as user-decision gate.
- [ ] All tests pass post-build
- [ ] **(Per Phase 4 Codex r2 MAJOR-1 precedent EXTENDED)** Each new concept + standards page passes `test_production_chemistry_deny_list.py` (extended deny-list now includes SCADA + measurement commercial product names with quantitative performance claims + proprietary tag-schemas + licensed-protocol implementation details — see TDD test list above)
- [ ] Each new page carries ≥3 public references (SPE / textbook / DOI / API / federal/state regulatory / public registry) per [[feedback_llm_wiki_concept_pages_need_public_references]]
- [ ] Plan + adversarial review artifacts at `scripts/review/results/2026-05-16-plan-92-*.md`

## Risks and open questions

- **Risk:** Production-accounting scope can balloon — allocation literature alone is a substantial SPE OnePetro corpus (well-test reconciliation methods, multiphase-meter-based allocation, tracer-based allocation, calculated-from-choke-and-PVT allocation, fiscal-vs-operational allocation, single-host-vs-multi-host allocation). Mitigation: bound Sub-issue 1 to overview-level coverage of each method; defer method deep-dives to per-method sub-pages only if user approves scope expansion. Pages target 150-220 lines each per Phase 3+4 precedent.
- **Risk:** SCADA vendor proprietary IP (tag-schemas, asset-models, protocol implementations) — biggest IP-leakage risk in Phase 5 (SCADA vendor docs are extensive and heavily proprietary). Mitigation: aggressive cite-by-name + general class discipline (e.g. "industry-standard data historian" not specific vendor schema details); reference public ISA-95 framework for canonical taxonomy. **TDD test `test_production_chemistry_deny_list.py` EXTENDED to SCADA + measurement vendors** (the most concrete mitigation).
- **Risk:** FracFocus bulk-download license — public-disclosure data is public BUT bulk-CSV/JSON download terms warrant review; risk of treating public-disclosure as same-as-public-redistribution. Mitigation: cite by individual disclosure-record URL only; do NOT ingest bulk-download into the repo. Surface in r1 review as MINOR.
- **Risk:** Texas RRC + BSEE NTL verbatim quoting risk — even though federal/state regulatory text is public-domain, the wiki style is paraphrase-first; reserve verbatim for short rule-text citations only. Mitigation: same as Phase 3+4 paraphrase discipline.
- **Risk:** ISA-95 vs IEC 62443 (cybersecurity) scope-collision — Phase 5 names ISA-95 as the manufacturing-control hierarchy anchor; IEC 62443 is the industrial-cybersecurity counterpart that's increasingly bundled with SCADA architecture discussions. Mitigation: defer IEC 62443 to a future cybersecurity-focused epic; surface as r1 open-question. NOT in Phase 5 scope.
- **Risk:** SCADA-protocol coverage scope-creep — Modbus / OPC-UA / IEC 61850 / DNP3 are each their own ecosystem. Mitigation: cite protocols by name + standardization body only; do NOT transcribe protocol internals. Surface as r1 MINOR for explicit scope-bound.
- **Risk:** Surface-handover boundary scope-collision with naval-architecture FPSO topsides — FPSO topsides processing is naval-architecture-adjacent (the floater carries the topside). Phase 5 surface-handover stops at the manifold-tie-in / choke-skid / separator-inlet; downstream-of-separator processing is surface-facility-engineering scope (not yet founded as an llm-wiki domain). Mitigation: explicit scope-distinction sentence on `surface-handover-boundary.md`; cross-link to naval-architecture with scope-difference framing.
- **Risk:** API MPMS revision verification — API MPMS Chapter 20 has multiple parts (20.1 Allocation Measurement, 20.2 Allocation Measurement by Mass-Difference, etc.) with their own revision histories. Mitigation: **pre-drafting check** — verify each MPMS Chapter 20 part's current revision via API catalog before drafting standards page; surface as r1 MINOR.
- **Risk:** ISA-95 revision verification — ISA-95 has 5 parts (ISA-95.00.01 through ISA-95.00.05) and IEC 62264 international counterpart has its own part numbering. Mitigation: **pre-drafting check** — verify ISA-95 Part 1 (and which other parts to include) current revision via ISA catalog before drafting; surface as r1 MINOR.
- **Open:** Should Texas RRC rules + state-portal references get their own `standards/` pages, or stay as inline-cited content in `concepts/state-production-reporting.md`? Recommend stay inline (state regulations are not "standards" in the API/ISO/NACE sense). Surface as user-decision.
- **Open:** Calc-citation entries — wiki-side `citations:` frontmatter or sidecar contract? Per Phase 4 Codex r2 MAJOR-2 lesson, **decide explicitly at plan-time** (don't punt to ambiguous middle). Recommendation: wiki-side `citations:` frontmatter for Phase 5 (no consuming calc module exists yet for allocation / well-test-reconciliation / uncertainty-propagation / flare-rate). Surface as user-decision.
- **Open:** Should SCADA-protocol coverage (Modbus / OPC-UA / IEC 61850 / DNP3) be in Phase 5 or out-of-scope? Recommend out-of-scope for Phase 5 (defer to a future cybersecurity-and-protocols epic alongside IEC 62443). Surface as user-decision.
- **Open:** Should production-data-historian patterns include a separate dedicated page for cybersecurity adjacency, or fold it into a "Cybersecurity considerations" section on `production-scada-architecture.md`? Recommend defer entirely (out-of-Phase-5-scope). Surface as user-decision.

## Complexity: T2

**T2** — 3 sub-issues, 13-15 new concept pages, 3 new standards pages, multi-week scope, no runtime test surface, requires calc-citation entries for 4 formula families (adds rigor). Comparable to Phase 4 in shape (Phase 4 landed 12 pages in 2,481 lines across 3 sub-issues; Phase 5 targets 13-15 pages in ~2,000-2,800 lines).

T2 because:
- Multi-file write surface with cross-link coordination across all 4 prior phases + asset-management + engineering-standards + naval-architecture
- Standards-anchor research load (API MPMS Chapter 20 multiple parts, 30 CFR 250 multiple subparts, ISA-95 multiple parts; verify existence + revision before drafting standards pages)
- Cross-domain scope-edge work (PE↔naval-architecture FPSO topsides boundary, PE↔asset-management KPI-lifecycle, PE↔engineering-standards MPMS anchor)
- Vendor-IP discipline EXTENDED to SCADA + measurement vendors (Phase 4 covered production-chemistry; Phase 5 extends to data-systems vendors which is a different domain of proprietary IP)
- Regulatory-text license-discipline (federal/state public-domain but paraphrase-first; FracFocus bulk-download license-scrutiny)

NOT T3 because:
- No multi-repo coordination beyond standard llm-wiki + workspace-hub
- No runtime calc-execution scope
- Shape-template available from Phase 4 commits
- No new safety-critical hardware coverage (Phase 5 is reporting + integration scope, not hardware-spec scope)

Adversarial-review depth: **T1 single-author Claude (this drafting session)** per "scale depth not presence" discipline ([[feedback_always_adversarial_review_scale_depth]]). T2 escalation to Codex available if user requests cross-provider review (per Phase 4 plan's user-decision precedent).

## Adversarial review summary

**Round 1 — 2026-05-16** (single-author Claude per [[feedback_always_adversarial_review_scale_depth]] T1 floor; Claude review prompt explicitly adversarial per [[feedback_adversarial_review_stance]])

| Provider | Verdict | Key findings |
|---|---|---|
| Claude | see [`scripts/review/results/2026-05-16-plan-92-claude.md`](../../scripts/review/results/2026-05-16-plan-92-claude.md) for full findings | targets ≥5 MINOR + MAJOR findings across vendor-IP guard testability for SCADA, standards-revision verification, cross-link enumeration completeness, scope-creep risk for production accounting, regulatory-text license-discipline, FracFocus license framing, ISA-95 vs IEC 62443 separation, calc-citation half-activation risk, SCADA-protocol coverage scope, surface-handover scope-collision |
| Codex | — | not run this round (T1 floor; T2 escalation deferred to user direction per "scale depth not presence" — appropriate for plan-scope where vendor-IP discipline is the dominant risk and that's well-bounded by Phases 3+4 precedent) |

**Overall result:** see r1 review file for verdict line and finding count. Approval-ready after user-decisions on the open questions (calc-citation activation, Texas RRC standards-vs-inline placement, SCADA-protocol scope, cybersecurity-adjacency deferral) and pre-drafting standards-revision verification (API MPMS Chapter 20 parts, 30 CFR 250 subparts current eCFR date, ISA-95 parts current revision).

**NOT self-approved.** User-approval gate (`status:plan-approved` label) is load-bearing per [[feedback_never_offer_to_self_label_plan_approved]].
