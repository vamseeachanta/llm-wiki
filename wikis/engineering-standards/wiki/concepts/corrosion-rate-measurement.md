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

> Concept anchor for the rate-of-metal-loss metric that drives remaining-life calculations and inspection-interval setting under [api-510](../standards/api-510.md), [api-570](../standards/api-570.md), and [api-653](../standards/api-653.md). Bidirectional with [risk-based-inspection](risk-based-inspection.md) (POF input) and [fitness-for-service](fitness-for-service.md) (remaining-life input). Distinct from [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md), which is depth-driven, not rate-driven.

## What is corrosion rate?

**Corrosion rate** is the loss of metal per unit time, expressed as a thickness-loss rate (mils-per-year, *mpy*; mm/yr; μm/yr) or as a mass-loss rate per unit area (g/m²·day, mg/dm²·day). It is the headline metric that drives three downstream engineering decisions:

- **Remaining-life calculation** — how long the component can stay in service before its measured wall thickness reaches the code-minimum retiring thickness.
- **Inspection-interval setting** — how soon the next [api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-653](../standards/api-653.md) inspection must occur, given the rate of consumption of remaining wall.
- **Material-replacement decisions** — when to upgrade metallurgy, add corrosion allowance, install a coating, energise cathodic protection, or inject inhibitor.

In-service inspection codes operationalise corrosion rate in two forms:

- **LTCR — long-term corrosion rate** = (T_initial − T_actual) / (years in service from the oldest credible thickness reference). Smooths through transient excursions; reflects the bulk damage history.
- **STCR — short-term corrosion rate** = (T_previous − T_actual) / (years between the two most recent thickness measurements). Catches recent damage acceleration that LTCR may dilute. Per [api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-653](../standards/api-653.md) practice, the **larger** of LTCR and STCR governs the next inspection interval — a conservative selection rule that prevents an averaging-out of recent process upset.

## Three measurement modalities

Corrosion-rate evidence reaches the engineer through three operationally distinct modalities, each with its own standard family:

| Modality | Methods | Standards |
|---|---|---|
| Mass-loss (laboratory coupon) | weight before/after timed exposure; conversion of mass loss to penetration rate | ASTM G1 (specimen prep + cleaning) + ASTM G31 (laboratory immersion practice) + ASTM G102 (mass-loss → rate conversion) |
| Electrochemical | linear polarisation resistance (LPR), Tafel extrapolation, electrochemical impedance spectroscopy (EIS), zero-resistance ammetry (ZRA) | ASTM G3 (electrochemical conventions) + ASTM G5 (potentiostatic / potentiodynamic procedure) + ASTM G59 (LPR procedure) + ASTM G102 (current density → rate) + ASTM G106 (EIS practice) |
| In-service thickness | ultrasonic thickness (UT — manual, AUT, PAUT), radiographic profile (RT), electromagnetic acoustic transducer (EMAT), internal rotary inspection (IRIS), in-line inspection (ILI) for pipelines | API RP 574 (inspection-practice for piping components); plus the technique-specific NDT standards (ASME BPVC Section V, API RP 577, etc.) |

**Mass-loss** is the calibration ground truth — it is what every rate model is ultimately validated against — but it is offline, slow, and aggregate (one number per coupon per exposure). **Electrochemical** methods are fast and continuous and deliver instantaneous rate values, but require a calibration of the polarisation resistance against mass-loss for the specific environment. **In-service thickness** is what the code inspection programme actually consumes; it is direct, traceable, and comparable across surveys, but it has a detection floor set by the technique's resolution and by surface-condition variability.

### Multi-criteria comparison of measurement modalities

| Criterion | Mass-loss coupon | Electrochemical (LPR / EIS) | In-service UT | In-service ILI |
|---|---|---|---|---|
| Output type | Aggregate exposure-window rate | Instantaneous rate | Discrete-point thickness | Pipeline-length thickness profile |
| Time resolution | Weeks-to-months per data point | Seconds-to-minutes | Per inspection cycle (years) | Per ILI run (years) |
| Spatial resolution | One coupon per station | One probe per cell | One CML at a time | Continuous along pipeline length |
| Localised-attack sensitivity | Visible at coupon retrieval | Limited (averaged signal unless arrayed) | Localised wall-thinning visible if CML coincides | Localised-thinning detection is the design strength |
| Calibration burden | Native unit (mass loss) | High — Tafel constants per environment | Low (well-established UT practice) | High — tool-specific calibration |
| Field-reality coupling | Low (lab-only) or moderate (sidestream loop) | Moderate (real fluid, simplified flow) | High (actual asset, actual service) | High (actual pipeline, actual fluid) |
| Cost per data point | Low (per coupon) / Medium (per programme) | Medium (per probe channel) | Low (per CML reading) / Medium (PAUT campaign) | High (per ILI run) |
| Standards anchor | ASTM G1 + G31 + G102 | ASTM G3 + G5 + G59 + G102 + G106 | API RP 574 + ASME V | API STD 1163 + NACE SP0102 family |

### Modality-selection worked examples

- **Worked example — refinery sour-water stripper overhead.** The damage-mechanism candidates (NH4HS-induced erosion-corrosion; cyanide-aggravated SSC) span both rate-driven thinning and localised cracking. Coupon programmes alone cannot resolve flow-induced upper-bound rates; site practice combines a mass-loss coupon station upstream of the air-cooler header with PAUT thickness mapping at high-velocity elbows and near-the-tubesheet-end. The combined data feed an [API RP 571](../standards/api-rp-571.md) damage-mechanism interpretation that supports the [risk-based-inspection](risk-based-inspection.md) screening.
- **Worked example — offshore topsides produced-water injection line.** A field operator deploying a corrosion-inhibitor injection programme uses an LPR probe immediately downstream of the inhibitor injection quill for *real-time inhibitor-effectiveness feedback* (fast control loop) plus an ER probe for cumulative-damage trending plus a mass-loss coupon for monthly calibration. The three data streams are reconciled at the well-pad telemetry layer; the LPR probe drives the inhibitor injection-rate controller, while the coupon is the auditable rate-of-record reported to the integrity-management system.
- **Worked example — LNG cryogenic-piping cold-spot CUI.** Although LNG pipework runs cold, sections that warm to within the CUI window during defrost or upset can experience accelerated CUI under jacketing. UT thickness mapping is the primary in-service tool, but selection of CMLs is driven by a [CUI](corrosion-under-insulation.md) damage-mechanism heat-map of the line (see also the LNG cross-wiki bridge in [LNG Process Safety](../../../lng-projects/wiki/concepts/lng-process-safety.md) RP 571 mapping section). Electrochemical probes are not generally usable in the cryogenic service itself; they appear instead on accompanying utility lines (glycol, hot-oil) where wet conditions admit a probe cell.
- **Worked example — atmospheric storage tank shell course (API 653 driver).** An ageing carbon-steel shell with a 25-year service history might be evaluated with a primary survey of vertical-and-horizontal UT grids on each shell course (driven by API 653 inspection-interval rules), supplemented at suspected high-rate zones with PAUT C-scans, and correlated against the historical [LTCR](#what-is-corrosion-rate) trend. A mass-loss coupon programme on the tank's internal floor / bottom plate (API 653 Annex C type) feeds the bottom-plate corrosion-rate input to the next out-of-service inspection planning cycle.

## In-service workflow

The in-service path from instrument reading to inspection-interval is codified in the API inspection trilogy:

1. **CML selection.** The owner-user designates **Condition Monitoring Locations (CMLs)** per [api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-653](../standards/api-653.md) — discrete repeatable points on the equipment where wall thickness will be tracked over time. CML density and placement reflect the credible damage mechanisms (high-velocity elbows, dead legs, weld heat-affected zones, vapour-space-to-liquid interfaces, soil-air interfaces on tank shells).
2. **Periodic UT thickness survey.** Each CML is measured on the inspection schedule (typically with manual UT or AUT). Results are entered into the equipment thickness history database with date and technician traceability.
3. **Rate computation per CML.** For every CML on every survey, compute LTCR and STCR. Flag CMLs where STCR > LTCR (recent acceleration) for engineering review.
4. **Remaining-life per CML.** Remaining life = (T_actual − T_min) / max(LTCR, STCR), where T_min is the code-minimum thickness from the [api-std-579](../standards/api-std-579.md) FFS Level-1 screening or from the original-construction-code retiring thickness, whichever the operator's integrity programme designates.
5. **Inspection-interval setting.** The next inspection date for the equipment item is set by the most-aggressive CML's remaining life, capped by the code's maximum-interval rule (half-life or absolute cap, whichever is shorter).
6. **RBI feedback.** [RBI](risk-based-inspection.md) consumes the corrosion-rate trends as a primary POF input — both the rate magnitude and the rate trend (accelerating, stable, decelerating) modify the asset's failure-probability score for the next RBI re-evaluation cycle.

## Damage-mechanism corrosion rates

Indicative ranges for common damage mechanisms — these are illustrative, not normative, and project-specific data always supersedes any tabulated band:

| Mechanism | Typical rate |
|---|---|
| General atmospheric corrosion (carbon steel, temperate climate) | 25 – 150 μm/yr |
| Sour-service carbon-steel corrosion (H2S + Cl⁻ + water) | 100 – 1000 μm/yr |
| CRA pitting (after CPT exceeded) | localised — depth-driven, not rate-driven; see [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) |
| Sulfidation (refinery hot piping) | per the **Couper–Gorman** or **McConomy** curves (sulfur content, temperature, alloy class) |
| CO2 corrosion (sweet O&G production) | per the **de Waard–Milliams** model with chloride, H2S, and flow-regime modifiers |
| Microbiologically Influenced Corrosion (MIC) | highly variable; often manifests as locally accelerated pitting under biofilm rather than as a uniform rate |
| Corrosion under insulation (CUI) | strongly temperature-window-dependent (≈ 75 – 175 °C for carbon steel); rates can rival or exceed atmospheric corrosion |

Because several of the most aggressive mechanisms (pitting, MIC, CUI under-deposit attack) produce localised damage rather than uniform thinning, a single rate-of-loss value can mis-represent the actual integrity threat. The corrosion engineer pairs the rate metric with the damage-mechanism catalogue (see [API RP 571](https://www.api.org/) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry*) to interpret what the rate number actually means for a given equipment item.

## In-service corrosion-monitoring instrumentation

The in-service modality column above hides a distinction that field practice routinely makes: between *survey* methods (taken on a campaign basis at scheduled CMLs) and *continuous-monitoring* methods (live-data probes that the operator's distributed control system reads on a polling interval). Continuous-monitoring instruments are not a substitute for survey UT — code inspection programmes still require the periodic CML record — but they are now standard for service environments where the rate is expected to vary on a timescale shorter than the inspection interval.

| Probe class | Measurement principle | Industry-application context | Primary standard / practice |
|---|---|---|---|
| Mass-loss coupons (CCD) | Recovered specimen weight loss after fixed exposure | Refining, petrochem, oilfield wet service, water-injection systems | NACE SP0775 — coupon installation, retrieval, interpretation |
| Electrical-resistance (ER) probes | Resistance increase as probe element thins | Process piping, water injection, gas-treatment loops | API RP 571 (mechanism interpretation) + manufacturer practice |
| Linear polarisation resistance (LPR) probes | Polarisation-resistance inverse proportional to corrosion current density | Cooling-water, water-injection, inhibitor-effectiveness loops; only in conductive electrolytes | ASTM G59 + ASTM G102 |
| Galvanic-pair / ZRA probes | Coupling current between dissimilar electrodes | Bimetallic-couple risk monitoring; oxygen-ingress detection | ASTM G71 (galvanic test) + ASTM G3 conventions |
| Hydrogen-flux (H probes) | Permeated H2 from corrosion reactions on the back face of process steel | Sour service, HF alkylation, amine units — leading indicator for HIC / SOHIC environments | API RP 939-C (ammonia / amine SCC reference) + manufacturer practice |
| Ultrasonic permanently-installed monitors (UT-PIM) | Wireless or wired UT transducers at fixed locations | High-temperature piping, sulfidation circuits, hydrogen reformer transfer lines | Vendor-specific; some operator integrity-management standards reference |
| Acoustic emission (AE) | Stress-wave detection during active cracking | Atmospheric tanks (API 653 internal-inspection deferral), pressure vessels — qualitative | ASTM E1316 + ASME BPVC Section V |
| Field signature method (FSM) | Multi-electrode array measuring local resistance change | Subsea pipelines, riser-base monitoring, splash-zone | Vendor-specific; operator-validated |

### Industry-application context table

| Sector | Dominant rate-monitoring stack | Driver |
|---|---|---|
| Refining (atmospheric / vacuum / coker) | UT survey + UT-PIM on sulfidation circuits + H-flux probes on amine / sour-water units | Ageing-asset run-length under API 510 / 570 + RP 571 mechanism mix |
| Petrochemical (olefins / aromatics) | UT survey + ER probes on caustic-treater loops + AE on critical reactor vessels | Chloride SCC + caustic SCC in stainless-steel circuits |
| Offshore upstream (topsides) | LPR + ER + coupons on injection lines + UT survey on piping circuits | Combined CO2 / H2S / chloride service; multi-mechanism interpretation |
| LNG (liquefaction / regasification) | UT survey on cold-box utilities + CUI inspection on warm-cold-cycling piping | Cryogenic envelope makes electrochemical probes inapplicable in cold service |
| Pipelines (long-distance) | ILI run-comparison + above-ground UT spot-checks at exposed crossings | Inaccessibility makes ILI the primary modality; survey-rate, not continuous |
| Storage tanks (API 653) | Floor-bottom robotic UT + shell-course UT grids + AE for in-service screening | Floor inspection drives the longest planning-and-cost element of API 653 cycles |

## Lab-versus-field reconciliation — worked reconciliation example

Consider a refinery operator running a new amine-treater overhead circuit. Pre-startup material qualification used ASTM G31 immersion coupons in synthetic lean-amine + 1 % H2S at 60 °C, returning a measured corrosion rate on carbon-steel coupons that supported the original metallurgical selection of carbon steel with a 3 mm corrosion allowance and a 10-year design life. Two years into service, on-line UT survey at the high-velocity elbow downstream of the reflux drum shows an STCR several times higher than the lab-derived prediction. The reconciliation gap admits four substantive interpretations, each with a different remediation:

1. The lab cell did not reproduce the field flow regime — actual elbow shear is well above the rotating-cylinder lab condition; remediation is targeted PAUT C-scan + flow-induced-corrosion screening per [API RP 571](../standards/api-rp-571.md).
2. The actual field chemistry has drifted from the design basis — heat-stable salt accumulation, oxygen ingress at the makeup point, or upstream process upset have all shifted the local corrosivity; remediation is process-condition root-cause analysis through Element 9-style operational reporting.
3. The CMLs were poorly placed — the high-velocity elbow CML is now revealing what the survey programme would have shown if a flow-impingement-aware CML map had been used at startup; remediation is a CML-replan informed by the [risk-based-inspection](risk-based-inspection.md) feedback loop.
4. The UT measurement itself is biased — surface scale, calibration drift, or operator variability are inflating the apparent thinning; remediation is repeat-with-different-technique (PAUT, IRIS) and inter-technician verification.

The discipline that the lab-versus-field reconciliation requires is identifying *which* of these interpretations the data supports — not retreating to the most-conservative assumption automatically. This reconciliation work is a recurring topic in refinery and petrochemical [fitness-for-service](fitness-for-service.md) campaigns and is the substrate that the [risk-based-inspection](risk-based-inspection.md) re-evaluation cycle consumes.

Laboratory corrosion-rate data (ASTM G31 immersion coupons, ASTM G59 LPR cells) feed **material-selection** decisions during design and qualification. In-service thickness data (UT surveys, ILI runs) feed **integrity-management** decisions during operation. The two data streams routinely diverge, for substantive reasons:

- **Flow regime.** Lab coupons typically run in a stagnant or rotating-cylinder cell; field components see complex flow with shear, turbulence, droplet impingement, and stagnant dead-legs. Flow-induced corrosion or erosion-corrosion can lift the field rate well above the lab baseline.
- **Biofilm.** Field equipment routinely develops biofilm, which lab coupon programmes rarely reproduce. Biofilm shifts the local chemistry (oxygen depletion, sulfate-reducing bacteria, acidification) and is a primary driver of MIC.
- **Intermittent operation.** Lab tests run continuous exposure; field equipment cycles between operating, idle, drained, and steam-out conditions. Wet-dry cycling, condensate accumulation, and start-up upset chemistry can produce field rates that are uncorrelated with steady-state lab data.
- **Surface condition.** Lab coupons are prepared per ASTM G1; field surfaces carry mill scale, weld spatter, residual fabrication oils, and prior-service product films that change the corrosion kinetics.

Bridging the two — choosing which lab data are predictive for which field service, and conversely diagnosing which field excursions are credible for re-test in the lab — is part of the corrosion engineer's craft and a recurring topic in operator integrity-management programmes.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [astm-g48](../standards/astm-g48.md) — Pitting and Crevice Corrosion Tests in FeCl3; **depth-and-attack-rating output, not a rate-of-loss test** — included here because the G48 mass-loss output is sometimes mis-reported as a "rate" when it is in fact an exposure-window-bounded mass loss. See [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) for the localised-attack metric framework.
- [api-510](../standards/api-510.md) — Pressure Vessel Inspection Code; consumes LTCR/STCR for vessel inspection-interval setting.
- [api-570](../standards/api-570.md) — Piping Inspection Code; consumes LTCR/STCR for piping-circuit inspection-interval setting and CML-level remaining-life calculation.
- [api-653](../standards/api-653.md) — Atmospheric Storage Tank Inspection Code; consumes LTCR/STCR for tank shell, bottom, and roof inspection-interval setting.
- **ASTM G1** — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Future first-class standards page candidate.
- **ASTM G3** — *Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Future first-class standards page candidate.
- **ASTM G31** — *Laboratory Immersion Corrosion Testing of Metals.* Future first-class standards page candidate.
- **ASTM G59** — *Conducting Potentiodynamic Polarization Resistance Measurements.* Future first-class standards page candidate.
- **ASTM G102** — *Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* Future first-class standards page candidate.
- **ASTM G106** — *Verification of Algorithm and Equipment for Electrochemical Impedance Measurements.* Future first-class standards page candidate.
- **API RP 571** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Catalogue used to interpret which mechanism a measured rate represents. Future first-class standards page candidate.
- **API RP 574** — *Inspection Practices for Piping System Components.* CML practice and UT thickness conventions consumed by [api-570](../standards/api-570.md). Future first-class standards page candidate.
- **NACE SP0775** — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* On-line corrosion monitoring / coupon-station practice. Future first-class standards page candidate.

## Related concepts

- [risk-based-inspection](risk-based-inspection.md) — POF input; corrosion-rate magnitude and trend feed the asset's failure-probability score in every RBI re-evaluation cycle.
- [fitness-for-service](fitness-for-service.md) — remaining-life input; FFS Level-1/2/3 thinning assessments consume the LTCR/STCR pair to compute the run/repair/replace verdict for thinned components.
- [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) — different metric: localised attack is depth-driven (and CPT/CCT-screened), not rate-of-loss-driven. A general rate of loss does not characterise pitting damage.
- [cathodic-protection](cathodic-protection.md) — rate-suppression mechanism for buried, immersed, and CP-protected structures; a properly-energised CP system drives the structure-to-electrolyte potential into the immune region and collapses the corrosion rate to near-zero. Surveys of CP-on-potential, off-potential, and current density are themselves an indirect corrosion-rate measurement.

## Source materials

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-series slice of the local catalog; records the G1 / G3 / G31 / G59 / G102 / G106 references underpinning the laboratory-modality column above.
- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API inspection-trilogy ([api-510](../standards/api-510.md) / [api-570](../standards/api-570.md) / [api-653](../standards/api-653.md)) plus API RP 571 / RP 574 that frame the in-service workflow.

## Notes

- This is a concept page, not a standards page. No clause text, conversion-factor tables, or model coefficients (Couper–Gorman, McConomy, de Waard–Milliams) are reproduced here. For normative use, cite the publisher edition of the relevant ASTM, API, or NACE document directly.
- The damage-mechanism rate ranges above are illustrative bands intended to anchor relative magnitude — actual project rates depend on fluid composition, temperature, flow, and metallurgy and must be supported by either qualified laboratory data or in-service trending evidence.
- LTCR/STCR is a convention from API in-service inspection codes; other regimes (pipeline ILI run-comparison, offshore-topsides DNV practice) use parallel but not-identical rate-pair conventions. The principle — preserving sensitivity to recent acceleration alongside long-term average — is shared.
