---
title: "Erosion, Erosion-Corrosion, and Flow-Accelerated Corrosion (FAC)"
slug: erosion-and-fac
tags:
  - erosion
  - fac
  - flow-accelerated-corrosion
  - sand-erosion
  - cavitation
  - mihama
  - refinery
  - downstream
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
---

# Erosion, Erosion-Corrosion, and Flow-Accelerated Corrosion (FAC)

> Concept anchor for the family of velocity-driven and impact-driven wall-loss mechanisms — pure mechanical erosion (solid-particle impact), erosion-corrosion (combined mechanical + chemical attack with synergistic rate), and flow-accelerated corrosion (FAC, the carbon-steel-in-flowing-water mechanism that drove the Mihama-3 rupture). Sits alongside [[sulfidation-and-naphthenic-acid]] in the high-velocity-zone screening branch of [[damage-mechanism-screening]] and feeds [[corrosion-rate-measurement]] for STCR/LTCR interpretation downstream of injection points and on the carbon-steel water-and-steam balance-of-plant.

## Three related-but-distinct mechanisms

- **Pure mechanical erosion** — solid particle impact (sand, catalyst fines, FCC slurry) abrades the metal surface; corrosion is secondary or absent. Rate scales with **particle velocity³** (cubic dependence is the dominant lever), **impact angle** (the angle-dependence varies by material — ductile metals peak around 20–30°, brittle materials peak near normal incidence), and **particle concentration / loading**. The mechanism is mechanical — fluid chemistry matters only through its effect on the protective scale.
- **Erosion-corrosion** — combined mechanical erosion + flowing-fluid chemistry. The flow disrupts protective scales (FeS, magnetite, oxide, NAC-resistant Mo-rich layer), exposes fresh metal, and accelerates corrosion. The key feature is **synergy**: the combined wall-loss rate is greater than the sum of the pure-erosion rate and the pure-corrosion rate measured separately. This is the dominant mechanism on hot-circuit refining piping at high-velocity zones (vacuum-tower transfer-line elbows, FCC slurry tees, downstream of injection points), on amine-treating high-velocity locations, and on heat-exchanger tube inlets where the inlet-end flow disturbance strips the protective layer.
- **Flow-accelerated corrosion (FAC)** — specifically applies to **carbon steel and low-alloy steel in flowing single-phase water and water/steam mixtures at 80–300 °C (175–570 °F)**. The protective magnetite (Fe3O4) layer is dissolved by the boundary-layer flow, exposing fresh steel and producing a continuous mass-transfer-limited rate. **No solid particles required** — the mechanism is electrochemical with mass-transfer-limited kinetics. FAC is the most-cited wall-loss mechanism for nuclear and fossil-power balance-of-plant piping (feedwater, condensate, extraction-steam, drain lines).

## Where erosion + FAC bite

| Service | Mechanism | Reference |
|---|---|---|
| FCC slurry-oil piping (refinery) | Catalyst fines erosion | API RP 571 §4 |
| Sand-laden production tubing (oilfield) | Sand erosion + erosion-corrosion | API RP 14E |
| Crude-tower transfer line (high-velocity 2-phase) | Erosion-corrosion + NAC | API RP 571 + NACE 34103 |
| Boiler-feedwater + condensate-return piping | FAC | EPRI / NRC NUREG-1801 |
| Steam-extraction lines (turbine) | FAC + thermal cycling | EPRI |
| Pump impellers | Cavitation erosion | API 610 |
| Heat-exchanger tube inlets (water side) | Inlet-end erosion-corrosion | TEMA / API 660 |

The locations span both refining hot circuits (where erosion-corrosion couples to sulfidation and NAC, and where the velocity-amplified mechanism story already discussed in [[sulfidation-and-naphthenic-acid]] applies in parallel) and the steam-and-water balance-of-plant (where FAC is the dominant single-mechanism rate driver on pre-1980 carbon-steel piping that has not yet been replaced with FAC-resistant alloy).

## Mihama-3 incident (2004)

In **August 2004** the secondary-side feedwater piping at the **Mihama-3 reactor** in Japan ruptured catastrophically when an elbow downstream of an orifice flowmeter failed at full power. The failure killed **5 workers** and injured several more. Investigation found the elbow wall thickness had thinned from the original **~10 mm to less than 1 mm** by **flow-accelerated corrosion**, undetected over decades because the location had been omitted from the licensee's FAC-management inspection programme. Mihama-3 drove **global FAC-management programme adoption** in nuclear and fossil-power fleets and the formal inspection-frequency requirements that became codified in **ASME OM-S/G-2007** and successor editions. The incident is the canonical case study for FAC and is referenced in nearly every FAC-management training programme worldwide.

## Velocity limits (API RP 14E erosional velocity)

The **API RP 14E** *Recommended Practice for Design and Installation of Offshore Production Platform Piping Systems* gives the historical erosional-velocity screening formula:

```
V_e = C / sqrt(ρ)
```

where:

- `V_e` — limiting (erosional) fluid velocity (ft/s)
- `ρ` — fluid density at flowing conditions (lb/ft³)
- `C` — empirical constant; conventionally **100 for continuous service** and **125 for intermittent service** with carbon steel; higher values are used for corrosion-resistant alloys and for sand-free service per the operator's metallurgy / sand-monitoring policy

Current API guidance and industry practice treat the 14E formula as a **starting screen** rather than an absolute limit. Modern multiphase erosion modelling for sand-laden production fluids — the **Salama** and **Shirazi / E/CRC (Erosion / Corrosion Research Center)** correlations — gives more accurate sand-erosion rate predictions by explicitly capturing particle size, particle loading, geometry (elbow vs. tee vs. straight pipe), and material erosion-resistance properties. Operators with significant sand production typically use a 14E-style screen at concept-select stage and a Salama-or-Shirazi rate model at detailed-design / operating-envelope stage.

## Mitigation

- **Design** — sweeping bends instead of short-radius elbows; larger pipe ID (lower bulk velocity); upstream separation of solids (sand cyclones, hydrocyclones, catalyst-fines knockout) before velocity-sensitive equipment; flow-distribution devices at heat-exchanger tube inlets to suppress inlet-end erosion-corrosion.
- **Material upgrade** — corrosion-resistant alloys (CRAs — duplex, super-duplex, 6Mo, Alloy 625) for severe erosion-corrosion; chromium-bearing low-alloy steels (1.25Cr–0.5Mo, 2.25Cr–1Mo) for FAC service (the chromium content shifts the magnetite-dissolution equilibrium and the FAC rate drops by an order of magnitude); hardfacing (Stellite, tungsten-carbide overlay) for cavitation-erosion duty on pump impellers and valve trim.
- **Velocity control** — flow restrictors, parallel piping runs, geometry choices that avoid local high-shear zones; for sand-producing wells, **erosional-velocity-managed choke and gathering-system design** with field-monitored sand-rate budgets.
- **Monitoring** — UT thickness time-trend at high-velocity zones (CMLs biased per [[corrosion-rate-measurement]]); intrusive and non-intrusive sand-monitor probes for production service; ER (electrical-resistance) probes for erosion-corrosion service; FAC-management inspection programmes for nuclear and fossil-power balance-of-plant piping.
- **Separation** — sand cyclones at the wellhead or first-stage separator, hydrocyclones at produced-water-treatment stages, knockout drums and electrostatic separators at refinery hot-circuit branches feeding velocity-sensitive equipment.

## FAC modelling

Three correlation lineages dominate FAC rate prediction:

- **Chexal–Horowitz** (United States) — implemented in the EPRI **CHECWORKS** code (industry-standard FAC-management tool for US/Canada nuclear and fossil-power fleets). Rate as f(temperature, pH, alloy chromium content, flow geometry / mass-transfer coefficient, dissolved oxygen, water-chemistry treatment).
- **Sanchez-Caldera** (United States) — earlier model, mass-transfer-limited dissolution framework that influenced subsequent codes.
- **KWU-Kastner** (Germany / European) — Siemens / KWU lineage; widely deployed in European nuclear and fossil-power fleets via successor codes.

The three families agree in functional form (FAC rate is mass-transfer-limited, accelerates with temperature in the 80–300 °C window peaking near 150 °C, drops sharply with even small alloy-chromium additions, and is suppressed by oxygenated water-chemistry treatment) but differ in fitted coefficients and recommended operating-envelope ranges. **EPRI CHECWORKS** is the *de facto* industry-standard implementation in the US — it is not a published consensus standard but is referenced by NRC and ASME OM in successor FAC-management editions and is the working tool for nearly every US balance-of-plant FAC-management programme.

## Standards

Bidirectional cross-references — each standards page below should cross-link back to this concept page once the convention propagates.

- [[api-rp-571]] — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* §4 mechanism catalogue; erosion, erosion-corrosion, and (by extension to balance-of-plant) FAC are entries in the loss-of-thickness family. Primary technical-content anchor for refining service.
- [[api-rp-574]] — *Inspection Practices for Piping System Components.* CML selection downstream of injection points and at high-velocity zones (elbows, tees, downstream of orifices and control valves) follows the velocity-and-shear-rate bias driven by erosion + erosion-corrosion susceptibility.
- [[api-rp-581]] — *Risk-Based Inspection Methodology.* Quantitative RBI; embeds erosion and FAC contributions in the **thinning damage factor** computation as part of the per-asset thinning-rate model, with rate-band selection driven by the screening output.
- **API RP 14E** — *Recommended Practice for Design and Installation of Offshore Production Platform Piping Systems.* Holds the `V_e = C / sqrt(ρ)` erosional-velocity screen referenced industry-wide for offshore production-piping concept-select. Future first-class standards page candidate (promotion when the API 14-series source slice lands in the catalog).
- **NRC NUREG-1801** — *Generic Aging Lessons Learned (GALL) Report.* Holds the FAC-management ageing-management programme requirements for US nuclear license-renewal applicants; the post-Mihama-3 codification reference for FAC inspection-frequency and scope expectations.
- **EPRI CHECWORKS** — *Chexal-Horowitz FAC Rate-Prediction Code.* Industry-standard FAC-modelling tool (not a published consensus standard, but referenced by NRC and ASME OM and used as the working FAC-management calculation engine across US/Canada nuclear and fossil-power fleets).

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [[sulfidation-and-naphthenic-acid]] — adjacent mechanism; NAC is a **velocity-amplified** mechanism (rate scales with shear at the metal surface) and routinely co-locates with erosion-corrosion at vacuum-line elbows, FCC slurry tees, and downstream of injection points. Combined-mechanism CML placement is the principal screening output where both apply.
- [[damage-mechanism-screening]] — upstream concept; screens erosion / erosion-corrosion / FAC as credible mechanisms on the per-asset shortlist when the service is high-velocity, particle-laden, or carbon-steel-in-flowing-water-and-steam.
- [[corrosion-rate-measurement]] — paired metric; UT-thickness CML programmes track the wall-loss rate at high-velocity zones, and STCR/LTCR step-changes signal feedstock or operating-envelope shifts that have moved the asset across an erosion-corrosion or FAC threshold.
- [[risk-based-inspection]] — POF input; the API RP 581 thinning damage factor is one of the primary POF terms for high-velocity-zone assets, and the erosion / erosion-corrosion / FAC rate-band choice is a principal RBI re-evaluation trigger when geometry or feedstock changes.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API RP 571 / RP 574 / RP 581 / RP 14E references underpinning the mechanism description, velocity-limit formula, mitigation framework, and inspection-programme structure above.

## Notes

- This is a concept page, not a standards page. No clause text, Chexal-Horowitz / Sanchez-Caldera / KWU-Kastner correlation coefficients, Salama / Shirazi sand-erosion model parameters, RP 14E `C` constants beyond the headline 100/125 values, or RP 581 thinning damage-factor coefficients are reproduced here. For normative use, cite the publisher edition of [[api-rp-571]] / [[api-rp-574]] / [[api-rp-581]] / API RP 14E / NRC NUREG-1801 directly.
- The Mihama-3 wall-thickness numbers (~10 mm → <1 mm) and casualty count (5 fatalities) are the figures consistently cited in the public-record investigation literature; the exact pre-rupture thickness is documented in the Japanese regulatory-investigation report and varies modestly across cited summaries.
- The boundary between **pure mechanical erosion** and **erosion-corrosion** is set by whether the fluid chemistry would corrode the substrate at low velocity. Sand-laden inert-gas flow is pure erosion; sand-laden produced fluid with CO2 / H2S is erosion-corrosion. The boundary between **erosion-corrosion** and **FAC** is set by phase: erosion-corrosion can occur in any flowing corrosive fluid (oil, multiphase, amine), while FAC is reserved in the standards literature for the carbon-steel-in-flowing-water-and-steam mechanism with magnetite-layer dissolution as the rate-controlling step.
