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
- **Worked-example anchor — Cleveland 1944 (East Ohio Gas).** The 1944 East Ohio Gas LNG-tank failure in Cleveland is the canonical historic LNG release: a 3.4 % Ni inner-tank shell (selected for then-perceived cryogenic toughness but inadequate to the duty) catastrophically failed, releasing roughly 4,200 m^3 of LNG that flowed through storm sewers, vapourised, and ignited; 128 fatalities and a multi-block urban fire followed. Cleveland is cited in nearly every NFPA 59A and EN 1473 historical preamble as the founding case for full-containment-tank doctrine and 9 % Ni metallurgy adoption (see [LNG Storage Tanks](./lng-storage-tanks.md)).
- **Worked-example anchor — Skikda 2004 (Sonatrach GL1K).** The 19 January 2004 Skikda liquefaction-plant explosion in Algeria killed 27 and injured ~74. Sequence: a steam-boiler hydrocarbon ingress event in Train 40's high-pressure steam circuit caused a deflagration that escalated when boil-off vapour from a refrigerant leak was drawn into the same fired equipment. Skikda is the modern reference for cold-box-and-utility-coupling escalation; QRA fault-tree practice for liquefaction trains was significantly tightened post-Skikda, particularly on the steam-system / refrigerant-loop interface that is no longer treated as a benign utility boundary.

### Pool fire

- Sustained combustion above a contained or unconfined LNG pool. Thermal-radiation flux at receptors governs separation distances; jurisdictional thresholds are typically 5 kW/m^2 (or equivalent) at the property line for unprotected receptors, with stepped tolerances for occupied buildings, control rooms, and ignition sources.
- Surface emissive power (SEP) of a clean LNG pool fire is high — large-pool experiments (Maplin Sands, China Lake, Sandia LNG fire tests) reported SEP in the 200-300 kW/m^2 range, with substantial sooting on larger pools that lowers the effective SEP from the unobstructed envelope.
- Pool size is set by the release rate, the bund geometry, and the time to ignition. Bund design (high impounding versus low spill containment) trades pool height against vapor generation; both are valid options under NFPA 59A and EN 1473 with different downstream consequences.
- **Multi-criteria comparison — bund design choices.** The two principal containment philosophies trade pool footprint against vapour generation and structural cost; jurisdictions accept either with different downstream consequence profiles:

  | Choice | Pool footprint | Vapor generation rate | Substrate brittle-fracture risk | Typical jurisdictions |
  |---|---|---|---|---|
  | High-impounding bund (deep, small footprint) | Smaller, deeper pool | Lower per unit area; total may be higher per unit time | Higher (cold liquid concentrated against bund wall) | Common in space-constrained European terminals under EN 1473 |
  | Low spill containment (shallow, wide footprint) | Larger, shallower pool | Higher per unit area at full pool | Distributed; bund wall less exposed | Common in US greenfield under NFPA 59A |
  | Full-containment outer-tank impoundment | Pool inside outer tank — no ground spill | Determined by inner-tank failure-mode envelope | Designed-out by 9% Ni outer wall | Most modern membrane and self-supporting tanks |
  | Membrane impounding | Distributed across membrane footprint | Driven by membrane failure-mode | Substrate is concrete + membrane composite | French / Korean membrane-tank LNG terminals |

### Vapor cloud explosion (VCE)

- A flammable cloud that finds an ignition source inside or downwind of confinement or congestion can transition from deflagration to detonation. Open-terrain unconfined LNG releases historically produce flash fires rather than blast-pressure VCEs, but module-yard congestion, pipe-rack obstruction, and partial enclosures change that picture materially.
- Modern VCE quantification uses TNO multi-energy or Baker-Strehlow-Tang correlations driven by congestion-and-confinement classification of the actual plot plan; CFD (FLACS) is now standard for large or contested cases.
- Blast overpressure receptors of regulatory concern: control rooms (typically 0.21 bar / 3 psi structural-damage threshold), occupied buildings (escalation thresholds depending on construction class), and ignition sources within the cloud envelope.
- **Multi-criteria comparison — VCE quantification methods.** Each method has a distinct congestion-and-confinement modelling envelope, fidelity, and runtime cost:

  | Method | Modelling principle | Fidelity for congested module yards | Runtime per case | Typical use |
  |---|---|---|---|---|
  | TNT-equivalent | Empirical scaling from TNT blast | Low — coarse upper bound | Minutes | Screening / order-of-magnitude only |
  | TNO multi-energy | Severity index assigned by confinement class | Moderate | Hours | Conventional FEED siting studies |
  | Baker-Strehlow-Tang | Flame-speed correlation by reactivity / congestion / confinement | Moderate-to-high | Hours | Conventional FEED + post-FEED |
  | FLACS-CFD | 3D Reynolds-averaged Navier-Stokes with combustion model | Highest available | Days per case | Contested cases, regulator-required defence, large modules |

### Rapid Phase Transition (RPT)

- A physical (non-combustion) explosion that occurs when LNG contacts water and undergoes rapid film-boiling collapse, releasing kinetic energy comparable to 2-10 kg TNT-equivalent for credible spill volumes.
- RPT is most consequential for marine transfer, ship-to-ship operations, and offshore release scenarios; it is rarely consequential for onshore terminal exclusion-zone setting.
- Composition-dependent: heavier hydrocarbon fractions (ethane, propane) in the LNG raise RPT susceptibility relative to lean methane-rich cargoes. See [LNG Composition Management](./lng-composition-management.md) for the cargo-quality interface.
- **Worked-example anchor — Zeebrugge 2002 jetty.** A spurious release at the Zeebrugge LNG terminal jetty during a transfer-arm disconnect produced a small-scale RPT event that, although low-energy, demonstrated that ship-shore transfer-arm purge sequencing and quick-connect/disconnect (QC/DC) hardware are part of the RPT-control envelope. Post-incident, SIGTTO transfer-arm procedural guidance and emergency-release-system (ERS) inerting practices were tightened across European import terminals.
- **Worked-example anchor — Soyo 2014 (Angola LNG).** The April 2014 Soyo plant flare-line failure shut down Angola LNG for ~14 months. Although the proximate root cause was metallurgical (cryogenic carbon-steel embrittlement on flare-header tie-in piping that was outside the original cold-service envelope), the consequence pathway is RPT-adjacent: cold liquid found a ground-level water collection pad through the failed line. Soyo is cited as the modern case where MDT (minimum design temperature) discipline on flare and vent lines is no longer optional — bridge to [Brittle Fracture and the Brittle-Ductile Transition](../../../engineering-standards/wiki/concepts/brittle-fracture.md).

### Rollover

- A stratified-tank density inversion in which a denser bottom layer suddenly mixes with a lighter top layer, releasing boil-off vapor in excess of the relief-system capacity. The 1971 La Spezia rollover at the Panigaglia terminal is the canonical incident reference.
- Mitigation is operational: routine density-and-composition monitoring, controlled top/bottom filling sequencing for cargoes of differing composition, and tank-level recirculation pumping. Modern terminals additionally use thermal-and-density profiling lances.
- Rollover relief sizing is part of NFPA 59A and EN 1473 storage-tank design; relief-system capacity is verified against the credible rollover-vapor generation rate, not just nominal boil-off.
- **Worked-example anchor — Hassi R'Mel 2008 (residual heat-leak rollover).** A 2008 rollover-class event at a North African storage facility was traced to a long-duration residual heat-leak gradient that produced more bottom-layer aging-and-warming than the operator's monitoring frequency could detect; relief capacity was sufficient but flare-system loading approached the upper-bound design case for an extended window. The lesson generalised: rollover risk is not exclusively a multi-cargo blending problem — slow heat-leak gradients in a long-resident single-source inventory can create a stratification that is invisible to surface-level density measurement.
- **Multi-criteria comparison — rollover detection technologies.** Modern terminals layer detection methods rather than relying on any single instrument, on the principle that no individual modality covers the full envelope of slow-developing stratification:

  | Method | Coverage | Latency | False-positive rate | Cost band |
  |---|---|---|---|---|
  | Single-point density (top/bottom) | Bulk-fill mismatch only | Hours | Low | Low |
  | Multi-point thermal lance | Vertical temperature profile | Minutes | Medium | Medium |
  | Combined density-and-temperature profiling | Full stratification map | Minutes | Low | Medium-high |
  | Boil-off-rate trending vs. composition prediction | Holistic, model-based | Hours-to-days | Medium-high (model-dependent) | Low (instruments) / High (modelling work) |
  | CFD-based what-if rollover simulation | Forward-looking decision support | Off-line | Not applicable | High |

### BLEVE and other secondary scenarios

- BLEVE (boiling-liquid expanding-vapor explosion) is less commonly cited for LNG cargo and storage than for LPG because LNG is typically stored at near-atmospheric pressure with a low boiling point. It is referenced in some LNG-as-fuel and pressurized small-scale storage hazard surveys for Type C tanks.
- Cryogenic embrittlement of secondary containment is treated as an escalation pathway, not a primary scenario; failure of the secondary barrier converts an inner-tank release into a much larger pool-spread case.
- Loss of refrigeration on a large outer-tank insulation system can drive an extended boil-off transient that interacts with rollover and relief sizing.

## Hazard-evaluation techniques across the lifecycle

- **HAZID (hazard identification)** — early conceptual study to enumerate credible release scenarios; outputs feed siting, plot plan, and Resource Report preparation. HAZID is typically convened at concept-select and pre-FEED, with deliverables that anchor the FERC Resource Report 13 (Reliability and Safety) preparation track.
- **HAZOP (hazard and operability study)** — systematic node-by-node deviation study using guide words (no, more, less, reverse, as well as, other than) on flow, pressure, temperature, level, composition. Mature LNG projects HAZOP at FEED, post-FEED, and pre-startup stages. Each HAZOP node carries a deviation-cause-consequence-safeguard-recommendation chain that becomes the auditable record handed to the operator's management-of-change (MoC) system at startup.
- **LOPA (layers of protection analysis)** — semi-quantitative estimation of consequence frequency, used to verify that independent protection layers (basic process control, alarms, operator response, SIS, physical relief, mitigation) achieve the target risk reduction. Drives SIL allocation for the safety-instrumented system.
- **QRA (quantitative risk assessment)** — full-frequency-and-consequence aggregation across the scenario set, producing PLL (potential loss of life), LSIR/SLIR (location/site-specific individual risk), and societal F-N curves. Required for FERC, FERC-equivalent jurisdictions, EN 1473 in some EU member states, and most lender risk reviews.
- **Bow-tie analysis** — graphical synthesis used in operator-training and management-of-change reviews; not a primary quantitative tool but increasingly required by class societies and SIGTTO best-practice guidance.

### Lifecycle stage-gate alignment

| Stage | Primary technique | Output deliverable | Downstream consumer |
|---|---|---|---|
| Concept select | HAZID | Site-specific scenario register | Plot plan + siting study + permit-track decision |
| Pre-FEED | HAZID refresh + preliminary QRA | Preliminary risk envelope | FERC pre-filing / EN 1473 risk envelope statement |
| FEED | HAZOP (FEED) + LOPA + QRA | Independent-protection-layer credit register; SIL allocation | SIS engineering specification |
| Detailed design | HAZOP (post-FEED) + bow-tie | Updated MoC baseline | Construction-readiness review |
| Pre-startup | PSSR + final HAZOP-action-tracker | Pre-Startup Safety Review (PSSR) close-out | Operations turnover dossier |
| Operations | MoC + bow-tie + periodic QRA refresh | Updated F-N and PLL trending | Lender risk-covenant compliance + insurer reviews |

### LOPA worked example (illustrative — methodology only, not normative)

A loss-of-containment scenario at a BOG compressor suction strainer might be evaluated as follows. Initiating event frequency (suction-strainer plug-induced overpressure on the upstream piping) is taken from a generic-data resource and modified with site-specific aging factors. Independent protection layers credited for the scenario could include the basic process-control loop (high-pressure alarm with operator action), an independent SIS high-pressure trip on the compressor, and a mechanical relief valve sized for the worst-credible flow case. Each layer is assigned a probability of failure on demand (PFD) consistent with its IEC 61511 SIL classification — for example, a SIL 1 trip carries a PFD of 10⁻¹ to 10⁻² per demand. The product of initiating frequency and PFDs gives an estimated mitigated-event frequency that is compared against the operator's risk-tolerance criterion. The illustrative pattern: LOPA does not invent risk numbers; it composes credit from auditable independent layers, and the audit trail is what makes the SIL allocation defensible at design review.

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
