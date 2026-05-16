---
title: "Integrity Monitoring"
tags: [integrity-monitoring, ut-survey, eddy-current, mfl, apb, downhole-gauge, corrosion-coupon, production-engineering, well-integrity]
sources:
  - nace-sp0106
added: 2026-05-16
last_updated: 2026-05-16
---

# Integrity Monitoring

## Scope

Integrity monitoring is the suite of continuous-and-episodic data-acquisition techniques that operators deploy to track the operating-time condition of producing-well barriers. The monitoring discipline provides the ground-truth corrosion-rate and degradation-rate data that the [Corrosion Management](corrosion-management.md) mitigation program is calibrated against and that the [Intervention Triggers](intervention-triggers.md) decisioning framework consumes. It sits inside the [Well Integrity During Production](well-integrity-during-production.md) operating-time scope.

This page covers the four major technique families that operators routinely deploy: ultrasonic and electromagnetic wall-thickness surveying, annular-pressure-buildup diagnostics, permanent-downhole-gauge trending, and corrosion-coupon-and-residual-analysis monitoring. The framework anchors to [NACE SP0106](../standards/nace-sp0106.md) at the operating-time methodology level and to AMPP SP0775 (see engineering-standards [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md)) at the coupon-line-item-methodology level.

## Four monitoring-technique families

### 1. Wall-thickness surveying (UT / eddy-current / MFL)

Direct measurement of casing and tubing wall thickness is the most-direct integrity-monitoring data source. Three families of in-line and tool-deployed techniques are in industry use:

- **Ultrasonic (UT) surveying** — high-frequency sound waves are transmitted from the tool into the metal and the echo from the inner and outer wall surfaces is timed. The technique gives high-resolution wall-thickness measurement directly; the deployment configuration varies (in-line inspection tools for pipelines, wireline-deployed downhole tools for tubing and casing, hand-held UT gauges for surface piping). Operating-time accuracy is excellent for well-conditioned surfaces; degraded surfaces (heavy scale, internal coatings, deposits) can defeat the technique.
- **Eddy-current testing (ECT)** — an alternating-magnetic field induces eddy currents in the metal, and the impedance response of the inducing coil is interpreted for thickness and defect indications. The technique is particularly effective for detecting near-surface and internal-surface defects in tubing and casing; depth penetration is more limited than UT, making the technique a strong complement for surface-defect inspection rather than a substitute for through-wall thickness measurement.
- **Magnetic-flux-leakage (MFL) testing** — a strong magnetic field is induced in the wall and any defect (pit, crack, wall-thickness reduction) causes flux leakage that is detected by sensor arrays. The technique is the workhorse for pipeline in-line-inspection (smart-pig) wall-thickness surveying. For downhole tubing and casing, MFL is deployed via specialised wireline tools.

Operating practice typically combines techniques: UT for the highest-resolution wall-thickness measurement, ECT for surface-defect characterisation in regions where UT data quality is degraded, and MFL for pipeline in-line inspection where through-the-line tool deployment is feasible. The surveying program is structured per risk-based-inspection methodology (API RP 581; see engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md)) with intervals tightened where monitoring trending indicates accelerated degradation.

Multi-finger caliper logs deserve specific mention as a complementary downhole-tubular technique: mechanical-finger arrays measure the inside-diameter profile of the tubular at high spatial resolution, detecting inside-surface wall loss, pitting, and mechanical damage. The caliper technique is paired with UT and ECT for comprehensive downhole-tubular condition characterisation.

### 2. Annular-pressure-buildup (APB) diagnostics

APB monitoring tracks the pressure in the casing-by-casing annuli of a producing well. The monitoring is **continuous** (real-time pressure trending at wellhead annulus-monitoring valves) or **periodic** (recorded pressure at routine well-test intervals); both deployments are widely used.

APB diagnosis distinguishes several mechanisms that produce pressure rise in a closed annulus:

- **Thermal expansion of trapped annular fluid** — the dominant non-integrity-related cause of APB; high-rate producing wells transfer significant heat to the casing annuli, expanding the trapped fluid. The thermal contribution is predictable from operating-condition data and is subtracted from observed APB to isolate integrity-related signal.
- **Tubing leak** — a leak in the production tubing communicates produced fluid into the tubing-by-production-casing annulus. The diagnostic signature is APB that tracks operating pressure and that does not bleed off on flowing conditions.
- **Casing leak** — a leak in an outer casing communicates formation fluid into the casing-by-casing annulus. The diagnostic signature is APB that tracks formation pressure and that may bleed off slowly on annulus venting.
- **Sustained casing pressure (SCP)** — APB that persists across operating conditions and that does not bleed off; typically indicative of cement-sheath compromise allowing formation-fluid communication into the annulus. SCP is a well-recognised integrity-threat indicator with specific regulator-mandated reporting and intervention requirements in some jurisdictions (BSEE NTLs in US OCS, equivalent regulations in other jurisdictions).

APB diagnostic methodology is well-developed in practitioner literature; the discipline-wide reference framework distinguishes thermal, leak, and SCP signatures by their pressure-vs-time behaviour and by the response to controlled bleed-off and operating-condition perturbation. Where APB indicates SCP, the typical follow-up is cement-evaluation re-surveying (CBL / VDL / ultrasonic-imaging-tool) to characterise the cement-sheath condition, paired with annular-fluid-chemistry sampling if accessible to identify the source.

### 3. Permanent-downhole-gauge (PDG) trending

PDGs are downhole pressure-and-temperature sensors installed at completion time, typically at or near the production-tubing tail or at the packer level, communicating to surface via control-line cable. Real-time PDG data supports operating-time integrity monitoring through several diagnostic axes:

- **Pressure-trend integrity diagnostics** — sudden pressure shifts, unexpected pressure-rate-of-change patterns, and pressure responses inconsistent with the established IPR/TPR operating envelope can indicate downhole integrity events (tubing leak, packer leak, sand-control screen breach, ESP shaft failure).
- **Temperature-trend diagnostics** — temperature shifts at the gauge location can indicate flow-path changes (e.g. a tubing leak above the gauge changes the heat-balance at the gauge location), gas-coning or water-coning events, and changes in the flow-regime above the gauge.
- **Bottomhole-pressure-vs-rate operating-point trending** — long-period drift in the operating point at constant choke setting can indicate accumulating skin (perforation-tunnel plugging, scale buildup, asphaltene deposition) or, conversely, gradual restoration if a continuous-injection program is gradually clearing pre-existing deposition.

PDG data is the most-information-dense downhole-monitoring channel that producing-well integrity work has access to; modern data-acquisition platforms support automated anomaly-detection on PDG trends with operator-defined alert thresholds. PDG-data interpretation has industry-wide best-practice patterns but no single canonical procedural reference — operators typically synthesise practice from practitioner literature and internal experience.

### 4. Corrosion-coupon and inhibitor-residual analysis

Corrosion coupons and electrical-resistance probes provide direct mass-loss measurements at instrumented points in the production system; inhibitor-residual analysis at the same points provides verification that the chemical-inhibition mitigation strategy is performing as designed. The line-item methodology is anchored at AMPP SP0775 (see engineering-standards [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md)).

- **Coupon-based mass-loss measurement** — metal coupons of known initial mass are exposed in the production stream at selected monitoring points for a defined exposure period (typically of order months in continuous service), retrieved, cleaned, and weighed; the mass loss is converted to a time-averaged corrosion rate at the coupon location. Multiple coupon-installation geometries support different operating-time questions (general-corrosion coupons, pitting-characterisation coupons, MIC-detection coupons).
- **Electrical-resistance (ER) probes** — sensor element exposed to the production stream measures wall thinning by tracking electrical resistance of the sensor element; provides continuous trending with finer time-resolution than discrete-coupon retrieval cycles. Linear-polarisation-resistance (LPR) probes provide complementary near-instantaneous corrosion-rate-indicator data.
- **Inhibitor-residual analysis** — periodic sampling of the production stream at monitoring points, analysed for inhibitor residual concentration. The residual concentration verifies that the inhibitor is reaching the monitoring point at the design concentration; lower-than-design residuals indicate ineffective inhibition coverage and trigger inhibitor-program review.

Operating-time integration of the coupon / ER-probe / residual-analysis data is the daily routine of the corrosion-management discipline; the data feeds back into inhibitor-program adjustment per [NACE SP0106](../standards/nace-sp0106.md) operating-time methodology.

## Cross-link to deposition-monitoring (flow-assurance interaction)

The four deposition families covered in [Flow Assurance](flow-assurance.md) — paraffin, asphaltene, mineral scale, and hydrate — have their own monitoring techniques (rate-and-pressure trending, recovered-deposit analysis from interventions, downhole-sample analysis, downstream-piping inspection). Monitoring of those families is folded into each deposition-family page rather than duplicated here; the cross-references are:

- [Paraffin Deposition](paraffin-deposition.md) — paraffin monitoring methodology
- [Asphaltene Precipitation](asphaltene-precipitation.md) — asphaltene monitoring methodology
- [Mineral Scale](mineral-scale.md) — scale monitoring methodology (and the iron-carbonate / iron-sulfide scale-vs-corrosion-rate coupling)
- [Hydrate Management](hydrate-management.md) — hydrate-formation diagnostic indicators

The integrity-monitoring discipline and the deposition-monitoring discipline overlap in practice (the same coupons, the same downhole gauges, the same UT surveys frequently inform both); the conceptual separation in this wiki keeps the data-acquisition framework here while the deposition-mechanism-specific interpretation lives in the flow-assurance family pages.

## Cross-link to ESP-failure-mode operational signatures

ESP installations provide a rich VFD-telemetry data channel (current draw, voltage balance, frequency response, vibration in some installations) that supports continuous monitoring of pump-condition and indirectly of the produced-fluid integrity. The VFD-telemetry-driven failure-mode patterns are catalogued at [ESP Failure Modes](esp-failure-modes.md); the data is part of the broader integrity-monitoring data envelope that production engineering consumes.

## Risk-based-inspection methodology integration

Operating-time inspection-interval design typically follows risk-based-inspection (RBI) methodology per API RP 581 (see engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md)). The RBI framework consumes integrity-monitoring data as the input for corrosion-rate distribution that drives inspection-interval optimisation: where monitoring data indicates low and stable corrosion rate with high confidence, inspection intervals can be extended; where monitoring data indicates high rate or trending toward accelerated degradation, intervals are tightened.

The RBI methodology is the bridge from raw monitoring data (this page) to intervention decisioning ([Intervention Triggers](intervention-triggers.md)). Operators with mature integrity-management programs typically deploy formal RBI software with documented decision rationale; operators without dedicated RBI software apply the methodology informally through engineering judgement.

## Standards anchors

- [NACE SP0106](../standards/nace-sp0106.md) — operating-time internal-corrosion management methodology that structures the monitoring discipline
- AMPP SP0775 — corrosion-coupon line-item methodology (see engineering-standards [AMPP SP0775](../../../engineering-standards/wiki/standards/ampp-sp0775.md))
- API RP 581 — risk-based inspection methodology (see engineering-standards [API RP 581](../../../engineering-standards/wiki/standards/api-rp-581.md))
- [ISO 21457](../standards/iso-21457.md) — system-level material-selection and corrosion-control philosophy; design-time inspection-and-monitoring-plan requirements
- [API RP 14C](../standards/api-rp-14c.md) — function-testing methodology for safety-system components

## Cross-references

- [Well Integrity During Production](well-integrity-during-production.md) — operating-time well-integrity router
- [Corrosion Management](corrosion-management.md) — monitoring data calibrates inhibitor program and validates mitigation performance
- [Intervention Triggers](intervention-triggers.md) — monitoring data feeds RBI-driven intervention decisioning
- [Paraffin Deposition](paraffin-deposition.md), [Asphaltene Precipitation](asphaltene-precipitation.md), [Mineral Scale](mineral-scale.md), [Hydrate Management](hydrate-management.md) — deposition-family monitoring
- [Flow Assurance](flow-assurance.md) — integrated thermal-hydraulic-chemical envelope monitoring
- [ESP Failure Modes](esp-failure-modes.md) — VFD-telemetry-based ESP integrity monitoring
- Drilling-engineering: [Cement Evaluation](../../../drilling-engineering/wiki/concepts/cement-evaluation.md) — construction-time cement evaluation that operating-time re-survey is compared against

## Public references

- **Heidersbach, R.** — *Metallurgy and Corrosion Control in Oil and Gas Production*, 2nd ed., Wiley 2018 (ISBN 978-1-119-25925-6). Covers operating-time integrity-monitoring techniques and corrosion-rate-data interpretation.
- **Papavinasam, S.** — *Corrosion Control in the Oil and Gas Industry*, Elsevier 2014 (ISBN 978-0-12-397022-0). Comprehensive coverage of integrity-monitoring methodology and corrosion-monitoring-data interpretation.
- **API RP 571** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry*, 3rd ed., 2020. Catalogue of damage mechanisms widely applied to upstream-production integrity-monitoring data interpretation.
- **Bourgoyne, A. T., Scott, S. L. & Manowski, W.** — "A Review of Sustained Casing Pressure Occurring on the OCS," Mineral Management Service final report (MMS Project 305, 2000). Foundational APB / SCP industry-survey work; widely cited in subsequent practitioner literature on annular-pressure-monitoring methodology.
- **Bellarby, J.** — *Well Completion Design*, Developments in Petroleum Science Vol 56, Elsevier, 2009 (ISBN 978-0-444-53210-7). Coverage of permanent-downhole-gauge deployment and operating-time use; relevant to PDG-trending integrity-monitoring.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover the integrity-monitoring discipline at handbook depth.
- **SPE OnePetro integrity-monitoring literature** — extensive corpus on UT / ECT / MFL surveying methodology, APB / SCP diagnostic methodology, PDG-trend interpretation, and integrity-monitoring-data-driven RBI workflows across operator practice.
- **API RP 580 / API RP 581** — risk-based inspection introduction (RP 580) and risk-based-inspection methodology (RP 581); the discipline-wide RBI framework that operating-time integrity-monitoring data flows into.

## Notes

- Wall-thickness-surveying technique selection (UT vs ECT vs MFL vs caliper) depends on the operating-time service environment, the tubular geometry, the deployment platform (in-line pig vs wireline vs intervention), and the data-quality requirements; operators typically deploy a mix of techniques rather than a single technique. The technique-selection decisioning is operator-program-specific and is not transcribed here at recipe level.
- APB-diagnosis methodology is well-developed in practitioner literature but the specific signature thresholds and operating-condition perturbation procedures vary across operator-developed programs; the framework-level signatures captured here are the discipline-wide common-ground, with specific operator procedures structured around them.
- Modern operating-time monitoring is increasingly augmented by real-time-data analytics that consume PDG, VFD-telemetry, and surface-flow-and-pressure data streams in integrated software platforms. The data-analytics technique selection is operator-program-specific; the methodology framework remains the underlying discipline that this page covers.
