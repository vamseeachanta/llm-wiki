---
title: "Well Integrity During Production"
tags: [well-integrity, operating-time-degradation, barrier-degradation, corrosion-management, integrity-monitoring, intervention-triggers, production-engineering, pe-de-boundary]
sources:
  - iso-21457
  - nace-sp0106
added: 2026-05-16
last_updated: 2026-05-16
---

# Well Integrity During Production

## Scope

Well integrity during production is the operational discipline that keeps the installed pressure-containing and flow-control barriers of a producing well **fit-for-service over the production life of the well**. It is the operating-time counterpart to the construction-time well-integrity work that drilling-engineering owns (primary cementing, casing-shoe integrity, BOP integrity at completion, the two-barrier philosophy in place at well hand-over).

Where drilling-engineering closes the well-construction phase by establishing the as-built barrier inventory and verifying each barrier through pressure testing, production-engineering inherits those barriers at well hand-over and is responsible for monitoring their condition, tracking their degradation, intervening when degradation crosses tolerance thresholds, and ultimately deciding when the well must be re-completed or abandoned. The PE side owns the **degradation trajectory** of the barriers across the producing life; the DE side owns the **establishment** of the barriers at construction time.

This page is the **router** for production-time well-integrity coverage in the production-engineering wiki. It states the PE-vs-DE scope boundary explicitly, frames the operating-time degradation taxonomy, and links out to dedicated pages for [Corrosion Management](corrosion-management.md), [Integrity Monitoring](integrity-monitoring.md), and [Intervention Triggers](intervention-triggers.md).

## CRITICAL: PE-vs-DE scope boundary

The phrase "well integrity" is used in two different but related senses across the upstream value chain, and conflating them produces engineering and operational confusion. This wiki uses an **explicit boundary statement** that operators should expect to find on both sides of the boundary:

- **Drilling-engineering scope — barrier ESTABLISHMENT.** The well-construction phase is responsible for placing the primary and secondary barriers that the two-barrier philosophy requires: production-casing integrity verified by pressure test, cement sheath verified by cement-bond logging and pressure testing, casing-shoe integrity verified by formation-integrity test or leak-off test, BOP integrity verified through pressure testing prior to completion hand-off. The construction-time integrity discipline establishes the as-built barrier inventory that production-engineering subsequently inherits. See drilling-engineering [P&A Barrier Philosophy](../../../drilling-engineering/wiki/concepts/pa-barrier-philosophy.md) and [Cement Evaluation](../../../drilling-engineering/wiki/concepts/cement-evaluation.md) for the construction-time framework.

- **Production-engineering scope — OPERATING-TIME degradation of the installed barriers.** Once the well is handed to production, the installed barriers begin to degrade in service. Tubing experiences internal corrosion from CO2, H2S, water, MIC, and oxygen ingress. Casing experiences external corrosion from formation-fluid contact through compromised cement, and internal corrosion in regions exposed to produced fluids. Cement sheath experiences mechanical degradation from thermal cycling, pressure cycling, and chemical degradation in some service environments. Wellhead and tree components experience erosion in sand-laden service and corrosion in sour service. Subsurface safety valves and downhole valves experience mechanical wear and elastomer degradation in cyclic service. The operating-time discipline is responsible for **monitoring** the degradation of each installed barrier, **predicting** when degradation will cross tolerance thresholds, and **triggering interventions** before barrier degradation causes loss of well control or productivity. This is the scope this wiki covers.

The boundary is **at well hand-over from completion to production** (formally: when the completion is verified, the well is brought online for the first time, and operating-time production data begins). The handover artefact is the as-built barrier inventory plus the baseline integrity verification (initial annular pressure test, baseline downhole-gauge pressures, baseline corrosion-coupon installation, baseline ultrasonic-tool survey of new tubular hardware).

The boundary is **not at the surface flange**, **not at the wellhead**, and **not at the Christmas tree**. All of these surfaces sit inside the PE-scope envelope: the production engineer is responsible for operating-time integrity of the wellhead and tree just as much as for operating-time integrity of the downhole tubing, because all are pressure-containing barriers that degrade in service. The boundary is purely **temporal**: construction vs operation, with the hand-over event as the inflection point.

## Why the boundary matters operationally

The PE-vs-DE boundary is load-bearing because the engineering disciplines, the data sources, the time-scales, and the regulatory anchors differ on each side:

- **Engineering disciplines** — construction-time integrity is dominated by cementing technology, casing-design engineering, and completion engineering. Operating-time integrity is dominated by corrosion engineering, integrity-monitoring engineering (UT, eddy-current, MFL surveying, downhole gauge interpretation), and intervention-decisioning engineering (workover economics, risk-based-inspection methodology).
- **Data sources** — construction-time data sources are cement-bond logs, formation-integrity tests, leak-off tests, casing pressure tests, and BOP pressure tests. Operating-time data sources are continuous downhole-gauge data, periodic UT and eddy-current surveys, corrosion-coupon analyses, annular-pressure-buildup diagnostics, and produced-fluid chemical analyses (water composition, gas composition, microbial activity, sand counts).
- **Time-scales** — construction-time integrity is an event-based discipline (each barrier verified at placement). Operating-time integrity is a continuous-trending discipline (each barrier's condition tracked across the producing life).
- **Regulatory anchors** — construction-time integrity is anchored to NORSOK D-010, API Std 53 (well-control), API Spec 10A (cement), API Spec 5CT (casing). Operating-time integrity is anchored to [ISO 21457](../standards/iso-21457.md) (system-level corrosion-control philosophy), [NACE SP0106](../standards/nace-sp0106.md) (internal corrosion of steel pipelines and piping; widely applied by analogy to downhole tubulars), API RP 581 (risk-based inspection), NACE MR0175 / ISO 15156 (sour-service material qualification), and regulator-specific operating-integrity rules (BSEE NTLs in US OCS, state oil-and-gas regulator requirements onshore, equivalent regulator regimes in other jurisdictions).
- **Intervention frameworks** — when construction-time integrity fails, the remediation is typically a remedial-cementing operation or a re-running of casing/tubing; the well is usually not yet producing and the economic consequences are scoped to the drilling-and-completion AFE. When operating-time integrity reaches an intervention trigger, the remediation is a workover that interrupts production, with economic consequences scoped to the production-deferral cost plus the workover cost; the decision framework is fundamentally different.

## The operating-time degradation taxonomy

Operating-time well-integrity work organises around five degradation mechanisms that act on installed barriers:

### 1. Internal corrosion of tubulars and pressure-containing components

The dominant operating-time well-integrity threat across most production service. Internal corrosion is driven by CO2, H2S, oxygen, microbial activity, and water in the produced stream. Mechanisms include uniform-attack wall thinning, localised pitting, mesa-attack in sweet service, stepwise cracking and sulfide stress cracking in sour service, and microbiologically-influenced corrosion under deposits and water hold-up regions. The [Corrosion Management](corrosion-management.md) page covers the mechanism framework, the prediction-modelling landscape, and the inhibition / mitigation strategy framework that operators deploy.

### 2. External corrosion of casing through compromised cement

Where the cement sheath does not fully isolate the casing from formation fluids — either because of as-built defects in primary cementing (channels, micro-annulus, lost-circulation regions) or because of cement degradation in service — formation fluids contact the casing exterior and drive external corrosion. The diagnostic is annular-pressure-buildup monitoring combined with periodic cement-evaluation re-survey; the [Integrity Monitoring](integrity-monitoring.md) page covers the diagnostic framework.

### 3. Erosion in sand-laden or high-velocity service

Sand-laden production erodes choke trim, valve seats, tubing restrictions, and surface-piping bends. High-velocity gas-and-liquid flow approaches the [Erosional Velocity](erosional-velocity.md) limit that bounds rate from above; sustained operation near this limit drives accelerated material loss even in non-sand-laden service. Sand-control completion integrity is a coupled threat — a breached sand-control completion changes the erosional-velocity calculation overnight (see [Sand Control](sand-control.md)).

### 4. Cement-sheath degradation

Cement degrades in service from several mechanisms: thermal cycling (in cyclic-steam and SAGD service especially), pressure cycling (in cyclic-injection service), chemical attack (carbonic acid in CO2-bearing service degrades Portland cement over time, more rapidly in some service environments), and mechanical damage from formation-movement loads (subsidence, compaction). The diagnostic is comparison of periodic cement-evaluation surveys against the as-built baseline, combined with annular-pressure-buildup trending and water-chemistry monitoring for cement-degradation indicators.

### 5. Mechanical degradation of valves, seals, and elastomers

Subsurface safety valves, surface safety valves, tree valves, wellhead seals, packer elements, and ESP elastomers all experience mechanical wear and elastomer degradation in service. The diagnostic is periodic function testing (per the SAFE-chart test-interval methodology in [API RP 14C](../standards/api-rp-14c.md) for surface and SSV elements), plus condition-monitoring for elements that support continuous monitoring (downhole gauges, ESP VFD telemetry, packer-set verification surveys).

## The four operating-time integrity workflows

Operating-time well-integrity discipline organises around four recurring workflows that this wiki's concept-page cluster covers in detail:

### Workflow 1: Continuous monitoring

Continuous data acquisition that supports trending and anomaly detection: permanent-downhole-gauge pressure and temperature trending, ESP VFD telemetry, surface flow-and-pressure trending, annular-pressure-buildup monitoring, periodic produced-fluid chemistry sampling. The monitoring program is designed at completion-engineering time and operated by the production-engineering team. See [Integrity Monitoring](integrity-monitoring.md).

### Workflow 2: Periodic inspection

Episodic surveys that produce direct measurements of barrier condition: UT wall-thickness surveys, eddy-current and MFL surveys of casing and tubing, cement-evaluation re-surveys, multi-finger caliper surveys, function-testing of safety valves and emergency-shutdown systems. The inspection-interval design is risk-based per API RP 581 methodology, with intervals tightened where monitoring trending suggests accelerated degradation. See [Integrity Monitoring](integrity-monitoring.md).

### Workflow 3: Mitigation-program management

Operating-time management of the corrosion-control mitigation strategy: chemical-inhibitor program (chemistry selection logic at programmatic level, application-rate decisioning, performance verification through coupon and residual analysis), biocide-program management for MIC threats, oxygen-scavenger-program management for water-injection lines feeding back to producers, pigging-program management. The mitigation-program management is the discipline that translates [ISO 21457](../standards/iso-21457.md) design-time corrosion-control philosophy and [NACE SP0106](../standards/nace-sp0106.md) operating-time methodology into day-to-day operating practice. See [Corrosion Management](corrosion-management.md).

### Workflow 4: Intervention decisioning

Decisioning workflow that determines when monitoring and inspection findings cross thresholds that justify intervention: workover candidate selection based on accumulated integrity-state degradation, regulator-mandated intervention triggers (BSEE NTLs, state regulator requirements), economic decisioning that compares intervention cost-of-deferred-production against the cost of continued operation under degraded integrity. See [Intervention Triggers](intervention-triggers.md).

## Cross-domain interactions

- **Drilling-engineering** — construction-time barrier-establishment integrity discipline (see [P&A Barrier Philosophy](../../../drilling-engineering/wiki/concepts/pa-barrier-philosophy.md), [Cement Evaluation](../../../drilling-engineering/wiki/concepts/cement-evaluation.md), [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md)). The DE hand-over artefact (as-built barrier inventory plus baseline integrity verification) is the foundational reference for all subsequent PE operating-time integrity work.
- **Flow assurance** — corrosion-driven scale deposition (iron carbonate, iron sulfide) interacts with [Mineral Scale](mineral-scale.md) management; chemical-inhibitor program for corrosion must be compatible with paraffin / asphaltene / scale inhibitor programs running in the same well. See [Flow Assurance](flow-assurance.md) for the integrated thermal-hydraulic-chemical envelope view.
- **Choke management** — choke-trim erosion in sand-laden service is one of the operating-time degradation paths; [Choke Sand Erosion](choke-sand-erosion.md) covers the choke-specific framework, [Choke Management](choke-management.md) covers the operating-discipline framework.
- **Artificial lift** — ESP, gas-lift, and PCP systems each have specific failure-mode interactions with the corrosion environment; the integrity-monitoring discipline informs the artificial-lift run-life trending and the ESP-failure-mode catalogue. See [Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Failure Modes](esp-failure-modes.md).
- **Stimulation** — refrac candidacy depends on cumulative integrity-state degradation (see [Refrac](refrac.md)); wellbore-integrity inspection is leg 3 of the refrac candidate-selection workflow, and the inspection findings determine which of the three recompletion architectures (cement-and-perf / mechanical isolation / expandable liner) is feasible.
- **Sand control** — sand-control completion integrity is itself an operating-time well-integrity threat: a breached gravel-pack or screen leaks formation sand at rates well above the design tolerance, triggering accelerated erosional damage downstream. See [Sand Control](sand-control.md) for the screen-integrity-as-PE-scope coupling.
- **Marine-engineering** — external structural corrosion of subsea hardware (Christmas trees, flowlines, manifolds) is covered at marine-engineering side via the [Corrosion Control](../../../marine-engineering/wiki/concepts/corrosion-control.md) page; the scope distinction is explicit (marine-engineering = external structural corrosion of submerged hardware; this wiki = internal production-tubing/casing corrosion). The two cross-link for full-system context.

## Standards anchors

- [ISO 21457](../standards/iso-21457.md) — system-level material-selection and corrosion-control philosophy; design-time anchor that operating-time integrity work consumes
- [NACE SP0106](../standards/nace-sp0106.md) — operating-time internal-corrosion management methodology for steel pipelines and piping, widely applied by analogy to downhole tubulars
- [API RP 14C](../standards/api-rp-14c.md) — safety-system methodology; SSV and safety-valve function-testing methodology that integrity-monitoring discipline relies on
- [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md) — risk-based inspection methodology (engineering-standards cross-link); inspection-interval optimisation framework
- [API RP 571](../../../engineering-standards/wiki/standards/api-rp-571.md) — damage mechanisms affecting fixed equipment; catalogue of degradation mechanisms relevant to production-system integrity
- AMPP / NACE MR0175 / ISO 15156 — sour-service material qualification (see engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md), [AMPP MR0175 Part 1-3](../../../engineering-standards/wiki/standards/ampp-mr-0175-pt1.md))
- AMPP SP0775 — corrosion-coupon methodology (see engineering-standards [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md))

## Cross-references

- [Corrosion Management](corrosion-management.md) — CO2/H2S/MIC/oxygen-ingress mechanisms and inhibition / mitigation framework
- [Integrity Monitoring](integrity-monitoring.md) — UT/eddy-current/MFL surveys, annular pressure buildup, permanent downhole gauges, corrosion coupons
- [Intervention Triggers](intervention-triggers.md) — RBI-driven workover decisioning and regulator-mandated intervention triggers
- [Flow Assurance](flow-assurance.md), [Mineral Scale](mineral-scale.md) — corrosion-driven scale deposition coupling
- [Choke Management](choke-management.md), [Choke Sand Erosion](choke-sand-erosion.md) — operating-time choke erosion as integrity threat
- [Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Failure Modes](esp-failure-modes.md) — artificial-lift run-life trending and failure-mode coupling
- [Refrac](refrac.md) — wellbore-integrity inspection as refrac candidate-selection leg
- [Sand Control](sand-control.md) — screen integrity as PE-scope integrity threat
- Drilling-engineering: [P&A Barrier Philosophy](../../../drilling-engineering/wiki/concepts/pa-barrier-philosophy.md), [Cement Evaluation](../../../drilling-engineering/wiki/concepts/cement-evaluation.md), [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — construction-time barrier establishment
- Marine-engineering: [Corrosion Control](../../../marine-engineering/wiki/concepts/corrosion-control.md) — external structural corrosion of submerged offshore hardware (complementary scope)

## Public references

- **King, G. E. & King, D. E.** — "Environmental Risk Arising from Well-Construction Failure: Differences Between Barrier Failure and Well Failure, and Estimates of Failure Frequency Across Common Well Types, Locations, and Well Age," SPE 166142 (2013). Practitioner-foundational analysis of barrier-failure modes across well populations; useful framing for the operating-time degradation-trajectory perspective.
- **Heidersbach, R.** — *Metallurgy and Corrosion Control in Oil and Gas Production*, 2nd ed., Wiley 2018 (ISBN 978-1-119-25925-6). Practitioner-oriented textbook covering operating-time corrosion-control engineering across the production system.
- **Papavinasam, S.** — *Corrosion Control in the Oil and Gas Industry*, Elsevier 2014 (ISBN 978-0-12-397022-0). Comprehensive industry-practitioner reference; covers the operating-time integrity discipline with field-case grounding.
- **ASM International** — *ASM Handbook Volume 13C: Corrosion: Environments and Industries*, 2006 (ISBN 978-0-87170-709-3). Industry-by-industry corrosion characterisation; the oil-and-gas chapters cover the operating-time integrity discipline.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Well-integrity and operating-corrosion chapters provide practitioner-level coverage.
- **NORSOK D-010** — *Well Integrity in Drilling and Well Operations* (Norwegian sector standard; retrievable from standard.no). Covers both the construction-time and operating-time integrity discipline in Norwegian-sector practice; provides one of the most explicit standards treatments of the construction-vs-operating boundary that this page frames.
- **Bourgoyne, A. T. et al.** — *Applied Drilling Engineering* (SPE Textbook Series Vol. 2, 1986, ISBN 978-1-55563-001-0). The well-construction foundation that this operating-time page builds atop; covered in drilling-engineering wiki.
- **SPE OnePetro well-integrity literature** — extensive corpus on operating-time well-integrity management, including the well-integrity-management-system (WIMS) framework that several major operators have published in concept form, and field-case retrospectives on operating-time integrity failures across well populations.
