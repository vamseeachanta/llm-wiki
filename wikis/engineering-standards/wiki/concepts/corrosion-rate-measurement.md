---
title: "Corrosion-Rate Measurement and Estimation"
slug: corrosion-rate-measurement
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - corrosion-rate
  - mass-loss
  - electrochemical
  - in-service-inspection
  - ltcr
  - stcr
sources:
  - standards/astm-g48.md
  - standards/api-510.md
---

# Corrosion-Rate Measurement and Estimation

> Concept anchor for the rate-of-metal-loss metric that drives remaining-life calculations and inspection-interval setting under [[api-510]], [[api-570]], and [[api-653]]. Bidirectional with [[risk-based-inspection]] (POF input) and [[fitness-for-service]] (remaining-life input). Distinct from [[pitting-and-crevice-corrosion]], which is depth-driven, not rate-driven.

## What is corrosion rate?

**Corrosion rate** is the loss of metal per unit time, expressed as a thickness-loss rate (mils-per-year, *mpy*; mm/yr; μm/yr) or as a mass-loss rate per unit area (g/m²·day, mg/dm²·day). It is the headline metric that drives three downstream engineering decisions:

- **Remaining-life calculation** — how long the component can stay in service before its measured wall thickness reaches the code-minimum retiring thickness.
- **Inspection-interval setting** — how soon the next [[api-510]] / [[api-570]] / [[api-653]] inspection must occur, given the rate of consumption of remaining wall.
- **Material-replacement decisions** — when to upgrade metallurgy, add corrosion allowance, install a coating, energise cathodic protection, or inject inhibitor.

In-service inspection codes operationalise corrosion rate in two forms:

- **LTCR — long-term corrosion rate** = (T_initial − T_actual) / (years in service from the oldest credible thickness reference). Smooths through transient excursions; reflects the bulk damage history.
- **STCR — short-term corrosion rate** = (T_previous − T_actual) / (years between the two most recent thickness measurements). Catches recent damage acceleration that LTCR may dilute. Per [[api-510]] / [[api-570]] / [[api-653]] practice, the **larger** of LTCR and STCR governs the next inspection interval — a conservative selection rule that prevents an averaging-out of recent process upset.

## Three measurement modalities

Corrosion-rate evidence reaches the engineer through three operationally distinct modalities, each with its own standard family:

| Modality | Methods | Standards |
|---|---|---|
| Mass-loss (laboratory coupon) | weight before/after timed exposure; conversion of mass loss to penetration rate | ASTM G1 (specimen prep + cleaning) + ASTM G31 (laboratory immersion practice) + ASTM G102 (mass-loss → rate conversion) |
| Electrochemical | linear polarisation resistance (LPR), Tafel extrapolation, electrochemical impedance spectroscopy (EIS), zero-resistance ammetry (ZRA) | ASTM G3 (electrochemical conventions) + ASTM G5 (potentiostatic / potentiodynamic procedure) + ASTM G59 (LPR procedure) + ASTM G102 (current density → rate) + ASTM G106 (EIS practice) |
| In-service thickness | ultrasonic thickness (UT — manual, AUT, PAUT), radiographic profile (RT), electromagnetic acoustic transducer (EMAT), internal rotary inspection (IRIS), in-line inspection (ILI) for pipelines | API RP 574 (inspection-practice for piping components); plus the technique-specific NDT standards (ASME BPVC Section V, API RP 577, etc.) |

**Mass-loss** is the calibration ground truth — it is what every rate model is ultimately validated against — but it is offline, slow, and aggregate (one number per coupon per exposure). **Electrochemical** methods are fast and continuous and deliver instantaneous rate values, but require a calibration of the polarisation resistance against mass-loss for the specific environment. **In-service thickness** is what the code inspection programme actually consumes; it is direct, traceable, and comparable across surveys, but it has a detection floor set by the technique's resolution and by surface-condition variability.

## In-service workflow

The in-service path from instrument reading to inspection-interval is codified in the API inspection trilogy:

1. **CML selection.** The owner-user designates **Condition Monitoring Locations (CMLs)** per [[api-510]] / [[api-570]] / [[api-653]] — discrete repeatable points on the equipment where wall thickness will be tracked over time. CML density and placement reflect the credible damage mechanisms (high-velocity elbows, dead legs, weld heat-affected zones, vapour-space-to-liquid interfaces, soil-air interfaces on tank shells).
2. **Periodic UT thickness survey.** Each CML is measured on the inspection schedule (typically with manual UT or AUT). Results are entered into the equipment thickness history database with date and technician traceability.
3. **Rate computation per CML.** For every CML on every survey, compute LTCR and STCR. Flag CMLs where STCR > LTCR (recent acceleration) for engineering review.
4. **Remaining-life per CML.** Remaining life = (T_actual − T_min) / max(LTCR, STCR), where T_min is the code-minimum thickness from the [[api-std-579]] FFS Level-1 screening or from the original-construction-code retiring thickness, whichever the operator's integrity programme designates.
5. **Inspection-interval setting.** The next inspection date for the equipment item is set by the most-aggressive CML's remaining life, capped by the code's maximum-interval rule (half-life or absolute cap, whichever is shorter).
6. **RBI feedback.** [[risk-based-inspection|RBI]] consumes the corrosion-rate trends as a primary POF input — both the rate magnitude and the rate trend (accelerating, stable, decelerating) modify the asset's failure-probability score for the next RBI re-evaluation cycle.

## Damage-mechanism corrosion rates

Indicative ranges for common damage mechanisms — these are illustrative, not normative, and project-specific data always supersedes any tabulated band:

| Mechanism | Typical rate |
|---|---|
| General atmospheric corrosion (carbon steel, temperate climate) | 25 – 150 μm/yr |
| Sour-service carbon-steel corrosion (H2S + Cl⁻ + water) | 100 – 1000 μm/yr |
| CRA pitting (after CPT exceeded) | localised — depth-driven, not rate-driven; see [[pitting-and-crevice-corrosion]] |
| Sulfidation (refinery hot piping) | per the **Couper–Gorman** or **McConomy** curves (sulfur content, temperature, alloy class) |
| CO2 corrosion (sweet O&G production) | per the **de Waard–Milliams** model with chloride, H2S, and flow-regime modifiers |
| Microbiologically Influenced Corrosion (MIC) | highly variable; often manifests as locally accelerated pitting under biofilm rather than as a uniform rate |
| Corrosion under insulation (CUI) | strongly temperature-window-dependent (≈ 75 – 175 °C for carbon steel); rates can rival or exceed atmospheric corrosion |

Because several of the most aggressive mechanisms (pitting, MIC, CUI under-deposit attack) produce localised damage rather than uniform thinning, a single rate-of-loss value can mis-represent the actual integrity threat. The corrosion engineer pairs the rate metric with the damage-mechanism catalogue (see [API RP 571](https://www.api.org/) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry*) to interpret what the rate number actually means for a given equipment item.

## Lab-versus-field reconciliation

Laboratory corrosion-rate data (ASTM G31 immersion coupons, ASTM G59 LPR cells) feed **material-selection** decisions during design and qualification. In-service thickness data (UT surveys, ILI runs) feed **integrity-management** decisions during operation. The two data streams routinely diverge, for substantive reasons:

- **Flow regime.** Lab coupons typically run in a stagnant or rotating-cylinder cell; field components see complex flow with shear, turbulence, droplet impingement, and stagnant dead-legs. Flow-induced corrosion or erosion-corrosion can lift the field rate well above the lab baseline.
- **Biofilm.** Field equipment routinely develops biofilm, which lab coupon programmes rarely reproduce. Biofilm shifts the local chemistry (oxygen depletion, sulfate-reducing bacteria, acidification) and is a primary driver of MIC.
- **Intermittent operation.** Lab tests run continuous exposure; field equipment cycles between operating, idle, drained, and steam-out conditions. Wet-dry cycling, condensate accumulation, and start-up upset chemistry can produce field rates that are uncorrelated with steady-state lab data.
- **Surface condition.** Lab coupons are prepared per ASTM G1; field surfaces carry mill scale, weld spatter, residual fabrication oils, and prior-service product films that change the corrosion kinetics.

Bridging the two — choosing which lab data are predictive for which field service, and conversely diagnosing which field excursions are credible for re-test in the lab — is part of the corrosion engineer's craft and a recurring topic in operator integrity-management programmes.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [[astm-g48]] — Pitting and Crevice Corrosion Tests in FeCl3; **depth-and-attack-rating output, not a rate-of-loss test** — included here because the G48 mass-loss output is sometimes mis-reported as a "rate" when it is in fact an exposure-window-bounded mass loss. See [[pitting-and-crevice-corrosion]] for the localised-attack metric framework.
- [[api-510]] — Pressure Vessel Inspection Code; consumes LTCR/STCR for vessel inspection-interval setting.
- [[api-570]] — Piping Inspection Code; consumes LTCR/STCR for piping-circuit inspection-interval setting and CML-level remaining-life calculation.
- [[api-653]] — Atmospheric Storage Tank Inspection Code; consumes LTCR/STCR for tank shell, bottom, and roof inspection-interval setting.
- **ASTM G1** — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Future first-class standards page candidate.
- **ASTM G3** — *Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Future first-class standards page candidate.
- **ASTM G31** — *Laboratory Immersion Corrosion Testing of Metals.* Future first-class standards page candidate.
- **ASTM G59** — *Conducting Potentiodynamic Polarization Resistance Measurements.* Future first-class standards page candidate.
- **ASTM G102** — *Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* Future first-class standards page candidate.
- **ASTM G106** — *Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* Future first-class standards page candidate.
- **API RP 571** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Catalogue used to interpret which mechanism a measured rate represents. Future first-class standards page candidate.
- **API RP 574** — *Inspection Practices for Piping System Components.* CML practice and UT thickness conventions consumed by [[api-570]]. Future first-class standards page candidate.
- **NACE SP0775** — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* On-line corrosion monitoring / coupon-station practice. Future first-class standards page candidate.

## Related concepts

- [[risk-based-inspection]] — POF input; corrosion-rate magnitude and trend feed the asset's failure-probability score in every RBI re-evaluation cycle.
- [[fitness-for-service]] — remaining-life input; FFS Level-1/2/3 thinning assessments consume the LTCR/STCR pair to compute the run/repair/replace verdict for thinned components.
- [[pitting-and-crevice-corrosion]] — different metric: localised attack is depth-driven (and CPT/CCT-screened), not rate-of-loss-driven. A general rate of loss does not characterise pitting damage.
- [[cathodic-protection]] — rate-suppression mechanism for buried, immersed, and CP-protected structures; a properly-energised CP system drives the structure-to-electrolyte potential into the immune region and collapses the corrosion rate to near-zero. Surveys of CP-on-potential, off-potential, and current density are themselves an indirect corrosion-rate measurement.

## Source materials

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-series slice of the local catalog; records the G1 / G3 / G31 / G59 / G102 / G106 references underpinning the laboratory-modality column above.
- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API inspection-trilogy ([[api-510]] / [[api-570]] / [[api-653]]) plus API RP 571 / RP 574 that frame the in-service workflow.

## Notes

- This is a concept page, not a standards page. No clause text, conversion-factor tables, or model coefficients (Couper–Gorman, McConomy, de Waard–Milliams) are reproduced here. For normative use, cite the publisher edition of the relevant ASTM, API, or NACE document directly.
- The damage-mechanism rate ranges above are illustrative bands intended to anchor relative magnitude — actual project rates depend on fluid composition, temperature, flow, and metallurgy and must be supported by either qualified laboratory data or in-service trending evidence.
- LTCR/STCR is a convention from API in-service inspection codes; other regimes (pipeline ILI run-comparison, offshore-topsides DNV practice) use parallel but not-identical rate-pair conventions. The principle — preserving sensitivity to recent acceleration alongside long-term average — is shared.
