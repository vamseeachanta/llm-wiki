---
title: "Intervention Triggers"
tags: [intervention-triggers, workover, rbi, risk-based-inspection, regulator-mandated, bsee, ntl, rrc, production-engineering, well-integrity]
sources:
  - nace-sp0106
added: 2026-05-16
last_updated: 2026-05-16
---

# Intervention Triggers

## Scope

Intervention triggers are the decision-framework artefacts that determine **when** operating-time integrity-monitoring findings cross thresholds that justify well intervention. The discipline sits at the intersection of integrity-monitoring data, risk-based-inspection methodology, regulator-mandated reporting and intervention rules, and the economic decisioning that weighs intervention cost against the cost of continued operation under degraded integrity.

This page covers two trigger families that operators routinely apply: **risk-based inspection (RBI) triggers** that derive from accumulated monitoring data per API RP 581 methodology, and **regulator-mandated triggers** that derive from prescriptive regulator rules (BSEE Notices to Lessees in US OCS, state oil-and-gas regulator requirements onshore, equivalent regimes internationally). Both families coexist in operating practice — wells that pass RBI triggers may still require intervention on regulator-mandated triggers, and vice versa — and the operating-time discipline manages both in an integrated framework.

This page is the **intervention-decisioning concept anchor** for the production-engineering wiki's operating-time integrity scope; it consumes data from [Integrity Monitoring](integrity-monitoring.md), interacts with mitigation programs covered in [Corrosion Management](corrosion-management.md), and sits inside the [Well Integrity During Production](well-integrity-during-production.md) router scope.

## Two trigger families

### 1. Risk-based-inspection (RBI) triggers

RBI methodology under API RP 581 (see engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md)) provides the structured framework that operators use to convert integrity-monitoring data into inspection-and-intervention decisioning. The methodology combines:

- **Probability-of-failure (PoF) assessment** — derived from observed corrosion-rate distribution at the monitored component, the remaining-life envelope at current corrosion rate, and the uncertainty distribution around the rate estimate. The PoF dimension is the quantitative output of the integrity-monitoring discipline as fed through the RBI methodology.
- **Consequence-of-failure (CoF) assessment** — derived from the safety, environmental, and production-deferral consequences of a hypothetical failure at the component. CoF differs strongly across components: a tubing leak above the SSV has different consequences than a leak below the SSSV; a flowline leak in deepwater has different consequences than in shallow water; a leak on a gas-bearing line has different consequences than on a liquid-bearing line.
- **Risk-matrix placement** — PoF × CoF places each component on an inspection-and-intervention risk matrix that determines both inspection-interval and intervention-trigger threshold. Components in high-risk cells receive tighter inspection intervals and lower intervention-trigger thresholds; components in low-risk cells receive extended inspection intervals and looser intervention-trigger thresholds.

RBI-driven intervention triggers are typically expressed as:

- **Wall-thickness-remaining trigger** — when monitored wall thickness falls below a threshold derived from design-pressure plus corrosion-allowance plus safety margin, intervention is triggered to restore wall thickness or to derate the component.
- **Corrosion-rate trigger** — when measured corrosion rate exceeds the design-corrosion-rate-distribution upper bound, intervention is triggered to investigate the rate excursion (inhibitor-program failure, service-condition change, monitoring-technique false-positive) and to apply corrective action.
- **Defect-indication trigger** — when ECT, MFL, or UT surveying detects a specific defect (crack, deep pit, weld-quality indication), intervention is triggered to characterise the defect further and to repair or replace the affected component.
- **Trending-anomaly trigger** — when monitoring trending shifts in a manner inconsistent with prior operating-time behaviour (e.g. sudden APB rise, unexpected PDG-pressure shift, ESP-VFD-telemetry pattern change), intervention is triggered to investigate the underlying cause.

The RBI methodology is data-driven and adaptive: as operating-time monitoring data accumulates, the rate distributions and the consequence envelopes are updated, and the trigger thresholds shift accordingly. Operators with mature RBI programs typically integrate the methodology into formal software platforms with documented decision rationale and version-controlled trigger thresholds.

### 2. Regulator-mandated triggers

Regulator-mandated triggers derive from prescriptive rules issued by the upstream-oil-and-gas regulatory authority for the jurisdiction in which the well operates. Unlike RBI triggers (which are operator-determined within methodology guidance), regulator-mandated triggers are **prescriptive**: when the trigger condition is met, the regulator requires that the operator take specified action within specified time, regardless of the operator's internal RBI assessment.

Several major regulator regimes that production-engineering practitioners encounter:

- **US OCS — BSEE Notices to Lessees and Operators (NTLs)** — BSEE (Bureau of Safety and Environmental Enforcement) issues NTLs that establish prescriptive integrity-management requirements for OCS operators. Specific NTLs have addressed sustained casing pressure reporting and remediation timelines, well-integrity-monitoring data submission, intervention reporting requirements, and safety-and-environmental-management-system (SEMS) requirements. Operators are required to report SCP exceeding specified thresholds, to develop remediation plans, and to execute remediation within specified time intervals. BSEE NTLs are public-domain documents retrievable from bsee.gov.
- **US onshore — state oil-and-gas-regulator requirements** — major producing states maintain their own integrity-management and intervention-trigger rules. Texas Railroad Commission (RRC) requirements include well-integrity reporting, sustained-casing-pressure remediation, and orphan-well prevention rules. Other major producing states (Oklahoma Corporation Commission, North Dakota Industrial Commission, Pennsylvania DEP, Colorado COGCC) maintain comparable rule frameworks. The specific trigger thresholds and remediation timelines differ by state; operators with multi-state portfolios manage the rule-set differences as part of their integrity-management program.
- **UK Continental Shelf — HSE / Offshore Safety Directive** — UK Health and Safety Executive operates a safety-case-based regulatory regime in which the operator's safety case establishes the integrity-management commitments and the trigger thresholds; HSE verifies that the operator's program meets the safety-case commitments. The trigger framework is operator-defined within the safety-case structure rather than prescribed line-item by HSE.
- **Norwegian Continental Shelf — Petroleum Safety Authority (Ptil/HSA)** — operates a similar safety-case framework; NORSOK D-010 well-integrity standard provides the technical methodology basis that operators' safety-case integrity-management commitments are typically structured against.
- **Australian — NOPSEMA** — operates a safety-case framework comparable to the UK and Norwegian regimes; integrity-management requirements are operator-defined within safety-case structure with regulator verification.
- **Brazilian — ANP** — operates regulatory framework that integrates safety-case elements with prescriptive technical requirements; integrity-management commitments are structured against ANP-issued technical rules and against operator-internal methodology.

Operators reviewing regulator-mandated triggers should consult the current regulator-issued rules directly; the rule-text and the specific threshold values are subject to revision and the current version takes precedence over any summary reference. The general principle is that regulator-mandated triggers establish a **floor** below which the operator is required to take prescribed action — the operator's internal RBI methodology may set tighter triggers above that floor, but cannot relax the regulator-mandated requirement.

## Integration of the two trigger families

Operating-time integrity-management programs typically integrate the two trigger families in a unified intervention-decisioning framework:

- **Both triggers fire concurrently** for any monitored component; the operator evaluates RBI and regulator-mandated triggers in parallel and treats the tighter of the two as the binding trigger.
- **Regulator-mandated triggers are inherently conservative** in most regimes; operators with mature RBI programs frequently find that their internal RBI triggers are tighter than the regulator-mandated triggers for most components, with the regulator-mandated triggers serving as a backstop.
- **Integration with the safety case (where applicable)** — in safety-case-based regulatory regimes, the operator-defined safety-case commitments include the trigger thresholds; the regulator-mandated triggers are therefore embedded in the operator's own safety-case framework rather than being separately-imposed prescriptive rules.

## Intervention-decisioning economic frame

Once a trigger fires, the operator decisioning framework determines what intervention to perform. The decisioning typically combines:

- **Intervention-cost estimate** — the all-in cost of the workover or repair action: rig or intervention-vessel cost, service-company costs, replacement-hardware cost, deferred-production cost during the intervention shutdown, and the post-intervention production-restoration trajectory.
- **Continued-operation cost-and-risk estimate** — the cost of accepting the degraded integrity state without intervention: increased monitoring program cost, increased risk of failure and associated consequence, and the risk of regulator enforcement action if regulator-mandated triggers are exceeded.
- **Workover-candidate-selection framing** — when multiple wells in a field reach intervention triggers concurrently, the operator schedules interventions in order of economic priority (highest expected uplift first) subject to safety, environmental, and regulator-compliance constraints.
- **Recompletion-vs-replacement framing** — for some triggers, intervention is a one-time repair (e.g. squeeze cement to restore zonal isolation, replace a tubing-string section); for other triggers, intervention is a major recompletion (e.g. tubing-string replacement, casing-string scab-liner, expandable-liner installation); for catastrophic triggers, intervention may not restore the well economically and the decision is to plug and abandon rather than repair. The intervention-vs-replacement-vs-P&A decision is the highest-stakes intervention-decisioning framing operators apply.

The economic frame interacts with the refrac candidate-selection workflow (see [Refrac](refrac.md)): wells that reach intervention triggers may also be refrac candidates, and the operator-decisioning framework combines integrity-driven intervention triggers with stimulation-driven refrac candidacy in a single recompletion-economics analysis.

## Specific intervention categories and trigger linkages

Common intervention categories and the trigger conditions that typically initiate them:

### Workover for tubing-string replacement

Triggered by: wall-thickness-remaining trigger on production tubing, tubing-leak diagnosis (APB or production-data signatures), cumulative-coupon-data corrosion-rate exceeding design.

### Remedial cementing (squeeze) for zonal-isolation restoration

Triggered by: SCP that bleeds-off slowly and re-builds (cement-sheath compromise diagnosis), water-cut breakthrough inconsistent with reservoir-engineering expectation suggesting cross-flow through compromised cement, formation-gas migration into upper zones diagnosed via gas-chemistry analysis.

### Surface or subsurface safety valve replacement

Triggered by: function-test failure per [API RP 14C](../standards/api-rp-14c.md) SAFE-chart test-interval methodology, downhole-gauge or VFD-telemetry signature of valve-related flow anomaly, regulator-mandated function-test-interval-driven replacement.

### Choke-trim or choke-body replacement

Triggered by: choke discharge piping ultrasonic-survey indication of erosion-driven wall loss, choke-performance trending diverging from baseline at constant bean (indicating trim erosion), choke-trim function inspection during scheduled intervention.

### ESP pull-and-replace

Triggered by: VFD-telemetry signature of catastrophic ESP failure (current spike, single-phasing, sudden current collapse), head-degradation trending past operability threshold, run-life trending toward operator-program-defined replacement schedule. See [ESP Failure Modes](esp-failure-modes.md).

### Sand-control-completion remediation

Triggered by: produced-sand count breakthrough above design-tolerance, choke-trim erosion-rate excursion indicating sand-carryover, ESP-failure-rate cluster indicating sand-control breach. See [Sand Control](sand-control.md) for the integrity-coupling framework.

### Refrac recompletion

Triggered by: production-history decline-analysis indicating refrac-treatable depletion state combined with DFIT indicating usable stress-state geometry, in combination with wellbore-integrity inspection determining recompletion-architecture feasibility (cement-and-perf, mechanical isolation, expandable liner). See [Refrac](refrac.md) for the candidate-selection workflow.

### Plug and abandonment (P&A)

Triggered by: integrity degradation past economically-restorable threshold, end-of-economic-life from reservoir-engineering perspective, regulator-mandated abandonment of orphaned or non-producing wells. P&A is the boundary case where production-engineering operating-time integrity work ends and drilling-engineering construction-time integrity work resumes for the abandonment-barrier-establishment phase (see [P&A Barrier Philosophy](../../../drilling-engineering/wiki/concepts/pa-barrier-philosophy.md)).

## Coupling with regulatory reporting

Several jurisdictions require **periodic integrity reporting** independent of intervention triggers — annual integrity status reports, periodic SCP-monitoring reports, periodic safety-case revalidations. Operators typically integrate integrity-reporting with intervention-decisioning in a single annual operating-cycle review that produces both the regulatory report and the intervention-priorisation plan. The integration ensures that regulator-mandated intervention triggers are tracked in the same workflow as RBI-driven triggers and that there are no reporting gaps or intervention-priorisation conflicts.

## Standards anchors

- API RP 581 — risk-based inspection methodology (see engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md))
- API RP 580 — risk-based inspection introduction (companion standard to RP 581)
- [NACE SP0106](../standards/nace-sp0106.md) — operating-time integrity-management methodology that informs intervention triggers for internal-corrosion threats
- [ISO 21457](../standards/iso-21457.md) — system-level material-selection and corrosion-control philosophy; inspection-and-monitoring-plan requirements that the trigger-framework operationalises
- [API RP 14C](../standards/api-rp-14c.md) — safety-system test-interval methodology that defines function-test-driven trigger conditions
- API RP 571 — damage-mechanism catalogue (see engineering-standards [API RP 571](../../../engineering-standards/wiki/standards/api-rp-571.md))
- NACE MR0175 / ISO 15156 — sour-service material qualification (relevant where intervention involves material upgrades; see engineering-standards [ISO 15156](../../../engineering-standards/wiki/standards/iso-15156.md))
- Regulator-specific rules — BSEE NTLs (US OCS, bsee.gov), Texas RRC rules and other state-regulator rules (US onshore), HSE safety-case framework (UK), Ptil / HSA guidance (Norway), NOPSEMA (Australia), ANP (Brazil)

## Cross-references

- [Well Integrity During Production](well-integrity-during-production.md) — operating-time well-integrity router
- [Integrity Monitoring](integrity-monitoring.md) — monitoring techniques that feed trigger-decisioning data
- [Corrosion Management](corrosion-management.md) — mitigation-program management that intervention triggers interact with
- [Refrac](refrac.md) — refrac candidate-selection workflow integrating integrity-driven and stimulation-driven decisioning
- [Sand Control](sand-control.md) — sand-control-completion integrity coupling
- [ESP Failure Modes](esp-failure-modes.md) — ESP-specific intervention-trigger signatures
- [Choke Sand Erosion](choke-sand-erosion.md) — choke-erosion-driven intervention triggers
- [API RP 14C](../standards/api-rp-14c.md) — safety-system function-testing methodology
- Drilling-engineering: [P&A Barrier Philosophy](../../../drilling-engineering/wiki/concepts/pa-barrier-philosophy.md) — abandonment-barrier-establishment as the boundary case between PE intervention scope and DE construction scope

## Public references

- **API RP 580** — *Risk-Based Inspection*, 4th ed. (current edition retrievable from api.org). Companion standard to RP 581 providing the methodology introduction; many operators cite both standards in their integrity-management documentation.
- **API RP 581** — *Risk-Based Inspection Technology*, 3rd ed., 2016 (current edition retrievable from api.org). The detailed methodology standard for RBI implementation.
- **Heidersbach, R.** — *Metallurgy and Corrosion Control in Oil and Gas Production*, 2nd ed., Wiley 2018 (ISBN 978-1-119-25925-6). Covers operating-time integrity-management methodology including intervention-trigger framing.
- **Papavinasam, S.** — *Corrosion Control in the Oil and Gas Industry*, Elsevier 2014 (ISBN 978-0-12-397022-0). Covers intervention-decisioning frameworks integrating corrosion-monitoring data with economic decisioning.
- **30 CFR 250 Subpart H** — US BSEE offshore safety regulations; incorporate API RP 14C by reference and establish the regulatory framework that BSEE NTLs operate within. Retrievable from ecfr.gov.
- **BSEE Notices to Lessees and Operators** — issued at bsee.gov; specific NTLs cover well-integrity reporting, SCP remediation, and intervention reporting.
- **Texas Railroad Commission Statewide Rules** — Texas oil-and-gas regulator rules covering well-integrity-related operator obligations; retrievable from rrc.texas.gov.
- **NORSOK D-010** — *Well Integrity in Drilling and Well Operations* (Norwegian sector standard; retrievable from standard.no). Provides the technical-methodology basis that Norwegian-sector operator safety-case commitments are structured against.
- **SPE OnePetro intervention-trigger literature** — extensive corpus on RBI-implementation case studies, intervention-decisioning frameworks, regulator-rule-compliance methodology, and post-incident retrospectives that inform trigger-threshold calibration.

## Notes

- Regulator-mandated trigger thresholds, reporting requirements, and remediation timelines are subject to revision. Operators reviewing intervention triggers for compliance purposes should consult the current rule-text from the relevant regulatory authority directly; this page summarises the trigger-framework at concept level only and does not transcribe specific threshold values.
- RBI methodology under API RP 581 is the discipline-wide framework for converting monitoring data into intervention decisioning; the specific implementation (software platform, decision-rule encoding, threshold calibration) varies across operator programs and is operator-program-specific.
- Intervention decisioning for high-consequence triggers (well-control-event indicators, sour-service material-degradation indicators in populated environments, leak-detection indicators on near-shore lines) typically escalates beyond the routine integrity-management workflow into operator emergency-response procedures. The escalation framework is operator-specific and is not transcribed here.
