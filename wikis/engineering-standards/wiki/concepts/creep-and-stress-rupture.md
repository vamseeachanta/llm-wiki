---
title: "Creep and Stress Rupture"
slug: creep-and-stress-rupture
tags:
  - creep
  - stress-rupture
  - larson-miller
  - omega
  - high-temperature
  - refinery
  - ffs-input
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/api-std-579.md
---

# Creep and Stress Rupture

> Concept anchor for the **time-dependent high-temperature damage family** that drives furnace-tube life, hydroprocessing-reactor remaining-life calculations, and the boiler / steam-cycle integrity envelope. Sits between the [damage-mechanism-screening](damage-mechanism-screening.md) catalogue (which flags creep as credible above the homologous-temperature threshold) and the [fitness-for-service](fitness-for-service.md) FFS Part 10 assessment that quantifies remaining life from a measured damage state. Routes into [api-rp-571](../standards/api-rp-571.md) (mechanism description and morphology) and [api-std-579](../standards/api-std-579.md) Part 10 (Omega method, time-fraction summation, replication-driven recalibration).

## What is creep?

**Creep** is time-dependent plastic deformation of materials at temperatures above approximately **0.4 of the absolute melting point** (homologous temperature, T / T<sub>m</sub>). For ferritic steels this threshold is operationally crossed above roughly **370 °C (700 °F)**; for austenitic stainless and Ni-base alloys the onset is higher in absolute terms but the homologous-temperature rule still governs. Once a component operates in this regime, deformation accumulates as a function of **stress + temperature + time** and can lead to dimensional change, cavity nucleation along grain boundaries, and eventually **stress rupture** at applied stresses well below room-temperature yield.

"Creep" and "stress rupture" name the same physical process at different end-states: creep is the strain-accumulation history; stress rupture is the terminal fracture event reached when tertiary-stage strain rate accelerates to failure. Both share the same governing variables and are described by a common parametric framework (Larson-Miller, Manson-Haferd, Orr-Sherby-Dorn, Omega).

## Three stages of creep

Creep curves at constant stress and temperature exhibit three distinct stages:

1. **Primary (transient) creep.** High initial strain rate that decreases with time as dislocation density rises and substructure rearranges. Hours to days. Most of the strain is recoverable on unloading at low stress; not recoverable at high stress.
2. **Secondary (steady-state) creep.** Near-constant **minimum strain rate**, where work-hardening and recovery (climb, cross-slip, dynamic recrystallisation) balance. Years to decades for design-stress refinery service. **This is the stage design analyses target** — Larson-Miller curves, allowable-stress tables, and Omega-method calibrations are all anchored on the secondary regime.
3. **Tertiary (accelerating) creep.** Void / cavity coalescence on grain boundaries, micro-crack linkage, local necking at the most-loaded section, and an accelerating strain rate that terminates in **stress rupture**. **This is the inspection-detection target** — replica metallography (cavity classification A → B → C → D), dimensional creep (tube-OD growth past limit), and capacitance-strain probes are calibrated to flag entry into tertiary before catastrophic rupture.

## Larson-Miller parameter

The **Larson-Miller parameter (LMP)** is the dominant time-temperature parameter for extrapolating short-term laboratory rupture data to long-term service:

> LMP = T · (C + log<sub>10</sub> t<sub>r</sub>)

where T is absolute temperature (typically °R for the API 530 / ASME II-D form), t<sub>r</sub> is rupture time in hours, and **C ≈ 20** for most ferritic and austenitic steels (calibration constant; revisit per material). Plotting **applied stress versus LMP** collapses rupture data over a wide temperature-time envelope onto a single master curve. The curves published in **API 530** (heater-tube design), **ASME BPVC Section II Part D** (allowable stresses), and EPRI / NIMS / proprietary databases provide the reference allowable-stress envelope used in design and remaining-life calculations.

LMP-based remaining-life estimates are sensitive to assumed C, to extrapolation distance from the calibration window, and to whether the stress used is the as-designed or actual time-weighted-average operating stress. **Manson-Haferd** and **Orr-Sherby-Dorn** are alternative time-temperature parameters used when LMP fits poorly (e.g., for some Ni-base superalloys or for materials with strong stress-dependent activation energy).

## Where it matters in O&G

Components that operate in the creep regime drive the high-consequence end of the refinery-and-petrochem creep / stress-rupture portfolio.

| Component | Material | Service T | Reference |
|---|---|---|---|
| Furnace tubes (cracker, reformer) | HK-40, HP-40, HP-Nb-Mo, 25Cr-35Ni, 35Cr-45Ni | 800–1100 °C | API 530, API 573 |
| Hydrocracker reactor shell | 2.25Cr-1Mo, 2.25Cr-1Mo-V | 350–450 °C | API 934 series |
| Catalytic-reformer reactor | 1.25Cr-0.5Mo | 480–540 °C | API 934 series |
| Boiler tubing (steam superheater) | T22, T91, T92 | 540–650 °C | ASME I + B31.1 |
| Steam-turbine rotor | 12Cr martensitic | ~540 °C | EPRI project guides |

Furnace-tube creep is the canonical refinery creep problem: ethylene-cracker and steam-methane-reformer radiant tubes operate at metal temperatures above 1000 °C, and **dimensional creep (tube-OD growth)** is the primary in-service surveillance metric. Hydroprocessing-reactor creep is lower-rate but higher-consequence because the wall thickness is large and replacement is capital-intensive; **2.25Cr-1Mo-V** is now the preferred metallurgy for new builds because of its improved temper-embrittlement and creep-rupture envelope versus plain 2.25Cr-1Mo.

## Damage models

The creep / stress-rupture analysis stack runs from screening through advanced FE simulation:

- **Larson-Miller / Manson-Haferd / Orr-Sherby-Dorn** parametric models — primary and secondary creep, allowable-stress derivation, design-life estimation. Calibrated against rupture-test databases.
- **Omega method (API 579-1 Part 10)** — Monkman-Grant strain-energy approach calibrated for in-service remaining-life estimation. Inputs: time-weighted-average metal temperature, applied stress (membrane + bending), and material parameter Ω from the API 579 Annex F / EPRI / proprietary database. Output: remaining strain capacity and remaining life. **The most-used FFS creep methodology** in refining-integrity practice.
- **Continuum-damage mechanics (CDM)** — Kachanov / Rabotnov damage-evolution equations integrated into elastic-creep FE solvers. Used for advanced FFS Level 3 assessments of complex geometries (nozzles, dissimilar-metal welds, transitions) where simple stress-classification cannot bound the answer.
- **Time-fraction summation** per **ASME B31.1** Section NB-3221 and **ASME B31.3** §5.1.6 — accumulates creep damage across a service history of varying T and σ as a sum of (t<sub>i</sub> / t<sub>r,i</sub>) fractions, with creep-fatigue interaction handled by adding the fatigue-cycle fraction (n / N).

## Inspection

Creep-damage detection is multi-modal because no single technique catches all stages:

- **Replica metallography** — surface-replication and grain-boundary-cavity classification per the **A / B / C / D** scheme (A = isolated cavities, B = oriented cavities, C = micro-cracks, D = macro-cracks). The A → D progression maps onto secondary → tertiary stage transition.
- **Creep-strain measurement** — capacitance probes, optical strain gauges, and high-temperature DIC where access permits.
- **Dimensional surveys** — tube-OD growth past the operator-defined creep limit (commonly 1.5 % for HK-40 / HP-40 furnace tubes) is the operational tertiary-stage trigger for retubing.
- **In-situ metallography** — base-metal and HAZ replication on hydroprocessing-reactor shells and steam-cycle headers, calibrated against destructive sister-coupon analysis where available.
- **Hardness profiling** — secondary-stage creep softens ferritic steels (recovery + carbide-coarsening); hardness drift is a screening proxy.

## FFS

**API 579-1 / ASME FFS-1 Part 10** is the assessment standard for in-service creep and creep-rupture damage. The Omega method is the load-bearing methodology: given a measured / inferred damage state, an operating-history reconstruction (time-weighted-average metal temperature and applied stress), and the material Ω parameter from the calibrated database, Part 10 produces a **remaining-life estimate** and a **replication-recommendation interval**.

Inputs the FFS practitioner must produce upstream:

- Temperature history — TWA metal temperature is non-trivial for furnace tubes with skin-thermocouple drift; use of process-side modelling (radiant-section heat-transfer simulation) is common.
- Stress history — pressure × geometry for primary stress, plus bending from supports / spring-hanger settings, plus secondary stresses where they cycle into the calculation (start-up / shutdown).
- Material parameters — Ω from API 579 Annex F, EPRI databases, or proprietary licensor data; **never** extrapolated outside the calibration envelope without explicit justification.

Output: remaining-life estimate (years) plus the next replication / inspection interval. The verdict feeds the run / repair / replace decision under the gating in-service inspection code (API 510 / 570 / 653) and integrates with the [risk-based-inspection](risk-based-inspection.md) POF input via the **API RP 581 creep damage-factor family**.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Catalogue entry for creep / stress rupture under the mechanical-metallurgical class. Covers description, susceptible materials, critical operating factors, morphology, prevention, and inspection — the technical-content anchor referenced by every downstream programme document.
- [api-std-579](../standards/api-std-579.md) — *Fitness-for-Service.* Part 10 *Assessment of Components Operating in the Creep Range* is the FFS methodology consumer; Omega method, time-fraction summation, and replication-driven recalibration live here.
- [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) — *Pressure-Vessel Construction (Design-by-Rule).* New-build allowable-stress envelope for components in the creep range; ASME II-D allowable-stress tables embed the Larson-Miller-derived design margins.
- [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) — *Pressure-Vessel Construction (Design-by-Analysis Alternative Rules).* Stress-classification and linearisation conventions used by FFS Part 10 are inherited from VIII-2; design-by-analysis margins for creep-range vessels.
- **API 530** — *Calculation of Heater-Tube Thickness in Petroleum Refineries.* Heater-tube design code; the Larson-Miller stress-vs-LMP curves used in furnace-tube design and remaining-life calculation are tabulated here. Future first-class standards page candidate.
- **API 573** — *Inspection of Fired Boilers and Heaters.* Heater-inspection code; defines the dimensional-creep, replication, and metallurgical-survey practices for radiant-section tubes.
- **API 934-A / 934-C / 934-E** — *Materials and Fabrication of 2.25Cr-1Mo, 2.25Cr-1Mo-V, and Cr-Mo-V Steels for Hydroprocessing Reactors.* Hydroprocessing-reactor metallurgy and fabrication code; creep-rupture envelope and step-cooling temper-embrittlement requirements live here. Future first-class standards page candidate.

## Related concepts

Wikilinks below point to concept pages — leave as wikilinks where the page does not yet exist, per the spinout's link-and-fill convention.

- [damage-mechanism-screening](damage-mechanism-screening.md) — upstream concept; flags creep as credible once homologous-temperature threshold is crossed and routes into the API RP 571 catalogue and API RP 581 creep damage-factor family.
- [fitness-for-service](fitness-for-service.md) — downstream consumer; FFS Part 10 governs creep-damage assessment, with the Omega method as the dominant Level-2 methodology.
- [htha-nelson-curves](htha-nelson-curves.md) — parallel high-temperature mechanism in hydrogen service; HTHA and creep can be co-credible on hydroprocessing-reactor shells and reformer-furnace tubes operating in H<sub>2</sub>-rich service. Distinct mechanisms (HTHA = hydrogen attack on carbides, creep = thermally-activated dislocation glide / climb) but overlapping equipment populations and coupled damage-factor families.
- [risk-based-inspection](risk-based-inspection.md) — downstream consumer; creep damage-factor family in API RP 581 is populated from the screening and FFS outputs.
- [fracture-toughness-measurement](fracture-toughness-measurement.md) — paired metric for the creep-fatigue-fracture interaction at high-temperature service; J-integral and CTOD measurements at elevated temperature feed FFS Level 3 advanced creep-crack-growth assessments.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API RP 571 / API 579 / API 530 / API 573 / API 934 catalog references underpinning the creep / stress-rupture framework above.

## Notes

- This is a concept page, not a standards page. No clause text, Larson-Miller calibration constants for specific alloys, Omega parameter values, allowable-stress tables, or API 530 / ASME II-D design curves are reproduced here. For normative use, cite the publisher edition of API RP 571 / API 579-1 / API 530 / ASME II-D / ASME B31.1 / ASME B31.3 directly.
- The component / material / temperature table is illustrative of typical refining and steam-cycle experience; actual service envelope for any specific asset must consider feed chemistry, firing pattern, skin-thermocouple calibration history, and cycle-count exposure.
- The Omega method's published Ω parameter ranges are calibration-bounded; extrapolation to service conditions outside the calibration envelope is not sanctioned by API 579 Part 10 and will not satisfy regulator or insurer expectations under a tier-1 mechanical-integrity programme. Where in-service conditions fall outside the calibration window, sister-coupon destructive testing or licensor-proprietary creep-database access is the route to a defensible remaining-life estimate.
