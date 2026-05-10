---
title: "LNG Process Safety"
tags: [lng-projects, concept, safety, vce, pool-fire, rollover, rpt, hazop, qra, lopa, dispersion]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-regulatory-framework.md
  - ../concepts/lng-cargo-containment-systems.md
  - ../concepts/lng-vapor-handling.md
  - ../../standards/nfpa-59a.md
  - ../../standards/phmsa-49-cfr-193.md
  - ../../standards/ferc-18-cfr-153.md
  - ../../standards/en-1473.md
  - ../../standards/igc-code.md
---

# LNG Process Safety

## Scope

This page summarizes the canonical release scenarios and consequence categories that drive LNG hazard identification, risk assessment, and exclusion-zone design. It does **not** restate jurisdictional exclusion-zone formulas, deterministic versus probabilistic methodology coefficients, dispersion-model constants, or the radiative-flux thresholds that NFPA 59A, EN 1473, CSA Z276, and SIGTTO each prescribe distinctly — those are reserved for the corresponding standards-page authoring routes. Hazard-evaluation technique mechanics (LOPA layers-of-protection counting, HAZOP node decomposition, QRA frequency aggregation) are covered at concept depth here, not procedural depth.

## Why process safety governs LNG project design

- **Exclusion-zone control of plot plan** — NFPA 59A and EN 1473 each require that thermal-radiation and flammable-vapor exclusion zones from the release scenarios below remain inside the property line. The exclusion-zone footprint — not equipment cost — frequently sets minimum site area and dictates whether a brownfield expansion can proceed.
- **Cryogenic-failure-mode coupling** — release scenarios are intertwined with cryogenic embrittlement of the surrounding hull, deck, or grade slab. A small spill that overwhelms the cryogenic spill-containment can brittle-fracture carbon-steel substrate and escalate to a much larger release; this is a first-order design constraint, not a worst-case-only concern.
- **Permitting gate** — for US export terminals, FERC's environmental review (under 18 CFR 153) requires Resource Reports that incorporate the consequence-modelling outputs of the release scenarios below. PHMSA 49 CFR 193 then governs in-service safety operations once siting is approved.
- **Insurance and finance covenants** — terminal lender and reinsurance markets require demonstrated QRA coverage of these scenarios (typically with PLL or LSIR/SLIR risk-tolerance criteria) as a precondition for project finance close.

## Canonical LNG release scenarios

### Vapor cloud dispersion

- LNG vapor at the cryogenic boil-off temperature (around minus 162 degrees C) is initially denser than ambient air, hugs grade, and disperses as a slumping plume; warming through entrainment and ground heat transfer brings the cloud to neutral or buoyant.
- Dispersion modelling must handle the dense-gas regime (e.g. via DEGADIS, FEM3A, FLACS-CFD, PHAST, or jurisdiction-approved equivalents). NFPA 59A names approved models in the US; EN 1473 leaves model selection to the operator with peer-review provisions.
- The half-LFL (2.5 percent methane) and full-LFL (5 percent methane) iso-concentration distances are the typical exclusion-zone metrics. Wind speed, atmospheric stability class (Pasquill A-F), substrate roughness, and obstruction layout drive the absolute distances.

### Pool fire

- Sustained combustion above a contained or unconfined LNG pool. Thermal-radiation flux at receptors governs separation distances; jurisdictional thresholds are typically 5 kW/m^2 (or equivalent) at the property line for unprotected receptors, with stepped tolerances for occupied buildings, control rooms, and ignition sources.
- Surface emissive power (SEP) of a clean LNG pool fire is high — large-pool experiments (Maplin Sands, China Lake, Sandia LNG fire tests) reported SEP in the 200-300 kW/m^2 range, with substantial sooting on larger pools that lowers the effective SEP from the unobstructed envelope.
- Pool size is set by the release rate, the bund geometry, and the time to ignition. Bund design (high impounding versus low spill containment) trades pool height against vapor generation; both are valid options under NFPA 59A and EN 1473 with different downstream consequences.

### Vapor cloud explosion (VCE)

- A flammable cloud that finds an ignition source inside or downwind of confinement or congestion can transition from deflagration to detonation. Open-terrain unconfined LNG releases historically produce flash fires rather than blast-pressure VCEs, but module-yard congestion, pipe-rack obstruction, and partial enclosures change that picture materially.
- Modern VCE quantification uses TNO multi-energy or Baker-Strehlow-Tang correlations driven by congestion-and-confinement classification of the actual plot plan; CFD (FLACS) is now standard for large or contested cases.
- Blast overpressure receptors of regulatory concern: control rooms (typically 0.21 bar / 3 psi structural-damage threshold), occupied buildings (escalation thresholds depending on construction class), and ignition sources within the cloud envelope.

### Rapid Phase Transition (RPT)

- A physical (non-combustion) explosion that occurs when LNG contacts water and undergoes rapid film-boiling collapse, releasing kinetic energy comparable to 2-10 kg TNT-equivalent for credible spill volumes.
- RPT is most consequential for marine transfer, ship-to-ship operations, and offshore release scenarios; it is rarely consequential for onshore terminal exclusion-zone setting.
- Composition-dependent: heavier hydrocarbon fractions (ethane, propane) in the LNG raise RPT susceptibility relative to lean methane-rich cargoes. See [LNG Composition Management](./lng-composition-management.md) for the cargo-quality interface.

### Rollover

- A stratified-tank density inversion in which a denser bottom layer suddenly mixes with a lighter top layer, releasing boil-off vapor in excess of the relief-system capacity. The 1971 La Spezia rollover at the Panigaglia terminal is the canonical incident reference.
- Mitigation is operational: routine density-and-composition monitoring, controlled top/bottom filling sequencing for cargoes of differing composition, and tank-level recirculation pumping. Modern terminals additionally use thermal-and-density profiling lances.
- Rollover relief sizing is part of NFPA 59A and EN 1473 storage-tank design; relief-system capacity is verified against the credible rollover-vapor generation rate, not just nominal boil-off.

### BLEVE and other secondary scenarios

- BLEVE (boiling-liquid expanding-vapor explosion) is less commonly cited for LNG cargo and storage than for LPG because LNG is typically stored at near-atmospheric pressure with a low boiling point. It is referenced in some LNG-as-fuel and pressurized small-scale storage hazard surveys for Type C tanks.
- Cryogenic embrittlement of secondary containment is treated as an escalation pathway, not a primary scenario; failure of the secondary barrier converts an inner-tank release into a much larger pool-spread case.
- Loss of refrigeration on a large outer-tank insulation system can drive an extended boil-off transient that interacts with rollover and relief sizing.

## Hazard-evaluation techniques across the lifecycle

- **HAZID (hazard identification)** — early conceptual study to enumerate credible release scenarios; outputs feed siting, plot plan, and Resource Report preparation.
- **HAZOP (hazard and operability study)** — systematic node-by-node deviation study using guide words (no, more, less, reverse, as well as, other than) on flow, pressure, temperature, level, composition. Mature LNG projects HAZOP at FEED, post-FEED, and pre-startup stages.
- **LOPA (layers of protection analysis)** — semi-quantitative estimation of consequence frequency, used to verify that independent protection layers (basic process control, alarms, operator response, SIS, physical relief, mitigation) achieve the target risk reduction. Drives SIL allocation for the safety-instrumented system.
- **QRA (quantitative risk assessment)** — full-frequency-and-consequence aggregation across the scenario set, producing PLL (potential loss of life), LSIR/SLIR (location/site-specific individual risk), and societal F-N curves. Required for FERC, FERC-equivalent jurisdictions, EN 1473 in some EU member states, and most lender risk reviews.
- **Bow-tie analysis** — graphical synthesis used in operator-training and management-of-change reviews; not a primary quantitative tool but increasingly required by class societies and SIGTTO best-practice guidance.

## Standards and references

- [NFPA 59A](../standards/nfpa-59a.md) — US LNG production, storage, and handling primary standard; deterministic exclusion-zone methodology.
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations including incident reporting and operator-qualification rules.
- [FERC 18 CFR 153](../standards/ferc-18-cfr-153.md) — US LNG siting framework whose Resource Reports incorporate the QRA outputs above.
- [EN 1473](../standards/en-1473.md) — European primary standard for onshore LNG installation; allows risk-based methodology with peer review.
- [CSA Z276](../standards/csa-z276.md) — Canadian LNG production / storage / handling national standard; deterministic methodology aligned with NFPA 59A.
- [IGC Code](../standards/igc-code.md) — IMO ship-construction code governing the marine cargo-side hazard envelope.
- SIGTTO publications: <https://www.sigtto.org/publications> — operational guidance on terminal and carrier safety practice.
- Sandia LNG safety reports (public DOE-funded research) — foundational pool-fire and dispersion experimental basis.

## Future trends

- **Risk-based exclusion zones** in US jurisdictions — long-standing industry interest in moving from deterministic to risk-based methodology under NFPA 59A revisions; persistent regulatory caution but incremental rule changes are landing.
- **Methane-emission integration** — process safety and methane-emission accounting are converging; vent and flare events are increasingly measured both for safety hazard and for greenhouse-gas inventory under EU Methane Regulation 2024/1787 and US EPA Subpart W.
- **Floating LNG and small-scale safety frameworks** — FLNG units and LNG-as-fuel bunker operations have driven SIGTTO and IGF Code (small-scale, ship's-fuel) updates that bring back-end safety logic from carrier service into terminal-style operations.
- **Hydrogen and ammonia transition cross-pollination** — many of the dispersion, RPT, and pool-fire methodologies above are being adapted for liquid-hydrogen and ammonia carrier and terminal hazard analysis; LNG-derived methodology is the precedent baseline for the next-generation cryogenic-fuel exclusion-zone work.

## Cross-references

- [LNG Storage Tanks](./lng-storage-tanks.md) — terminal containment whose design is driven by the consequence categories above.
- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — ship-side containment whose type-approval scrutiny is anchored on these scenarios.
- [LNG Regulatory Framework](./lng-regulatory-framework.md) — standards bodies that codify safety distances and methodology.
- [LNG Vapor Handling](./lng-vapor-handling.md) — vapor-disposition systems whose failure modes connect to the release scenarios above.
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — BOG generation and rollover-relief interface.
- **Cross-wiki (marine-engineering)**: [Process Safety](../../../marine-engineering/wiki/concepts/process-safety.md) — broader marine process-safety scope; LNG-specific scenarios above are a subset.
- **Cross-wiki (engineering-standards)**: [Brittle Fracture and the Brittle-Ductile Transition](../../../engineering-standards/wiki/concepts/brittle-fracture.md) — **bidirectional bridge**: cryogenic-failure-mode coverage on this page (cold-spill, RPT, rollover-driven thermal transients) defines the minimum design temperature (MDT) that the brittle-fracture / Charpy / `T₀` screening must clear for LNG inner tanks (9% Ni / ASTM A553), membrane systems (Invar), and process piping under EN 1473 and NFPA 59A.
- **Cross-wiki (engineering-standards)**: [ISO 15156 / NACE MR0175 — H2S Sour Service Materials](../../../engineering-standards/wiki/standards/iso-15156.md) — **bidirectional bridge**: LNG cargoes carry trace H2S below pipeline-specification thresholds, but ISO 15156 still binds materials qualification for cargo-handling, reliquefaction, and BOG-treatment equipment because H2S partial pressure (not concentration) sets the SSC and HIC regime. Most consequential for 9% Ni inner-tank welds (ASTM A553), Invar membrane attachments, and 22Cr/25Cr duplex / super-duplex cargo-handling components.
- **Cross-wiki (engineering-standards)**: [API RP 571 — Damage Mechanisms Affecting Fixed Equipment in the Refining Industry](../../../engineering-standards/wiki/standards/api-rp-571.md) — **bidirectional bridge**: the canonical LNG release scenarios on this page (RPT, rollover-driven relief overpressure, cryogenic-shock secondary-barrier brittle fracture, BOG-compressor rapid-cycling fatigue, vapour-cloud-dispersion ignition) require RP 571's damage-mechanism taxonomy for incident-investigation root-cause analysis on liquefaction-train fixed equipment. Highest-yield mechanism mappings: cryogenic-shock + warm-cold cycling on 9 % Ni inner tanks (brittle-fracture and thermal-fatigue entries — the consequence-side counterpart of the cryogenic-failure-mode coupling identified above); BOG compressor and reliquefaction skid mechanical and thermal fatigue; cryogenic-piping cold-spot CUI on warm-cold cycling sections; amine-unit caustic SCC and amine SCC on acid-gas-removal trains feeding the liquefaction cold box; flare-tip and waste-heat-recovery oxidation / sulfidation on regen-gas circuits. The RP 571 catalogue feeds RBI / RP 580 / RP 581 screening on the same liquefaction-train fixed equipment whose leak frequencies populate the QRA and exclusion-zone calculations. Use this pairing when authoring liquefaction-train RBI plans, FERC 18 CFR 153 / EN 1473 Resource Reports that need mechanism-level credibility for fixed-equipment leak-frequency inputs, or post-incident root-cause reports reconciling regulator findings with metallurgical evidence.
