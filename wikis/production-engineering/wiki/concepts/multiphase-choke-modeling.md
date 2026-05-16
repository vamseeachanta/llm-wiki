---
title: "Multiphase Choke Modeling"
tags: [choke, multiphase-flow, critical-flow, subcritical-flow, sachdeva, perkins, ashford-pierce, nodal-analysis, production-engineering]
sources: []
added: 2026-05-16
last_updated: 2026-05-16
---

# Multiphase Choke Modeling

## Scope

Multiphase choke modelling is the body of correlations and physical frameworks that predicts the flow rate through a production choke given upstream pressure, choke geometry, fluid composition (oil / water / gas), and downstream pressure. The problem is non-trivial because the choke is operating most of the time in a regime where the gas phase is at or near sonic velocity through the orifice while the liquid phase is subsonic, and the two phases interact through slip, momentum exchange, and phase-change at the orifice throat.

This page describes the four foundational frameworks that anchor practitioner choke modelling (Sachdeva 1986, Perkins 1993, Ashford-Pierce 1975, and the Bertuzzi-Tek-Poettmann modern industry framing) at the **prose level**, with explicit framing of what each framework adds to the operator's toolkit. Per the production-engineering wiki's calc-citation discipline, this page does **not** transcribe the engineering-unit formulas from these papers; operators implementing choke modelling in nodal-analysis software should consult the original SPE references directly.

For choke management as an operational discipline, see [Choke Management](choke-management.md). For choke hardware architectures, see [Choke Types](choke-types.md). For erosion considerations, see [Choke Sand Erosion](choke-sand-erosion.md).

## Why multiphase choke modelling is hard

Single-phase choke modelling (gas-only or liquid-only flow through an orifice) is a textbook problem with clean closed-form solutions: gas flow follows isentropic-nozzle theory with sonic-velocity capping at the throat, liquid flow follows the incompressible Bernoulli-orifice form with a discharge coefficient. Multiphase flow defeats both clean forms simultaneously:

- **Phase-slip at the throat** — gas accelerates more rapidly than liquid through the converging-orifice geometry, so the in-situ gas-liquid ratio at the throat differs from the upstream ratio. Slip velocity affects momentum balance and energy balance independently.
- **Phase-change during expansion** — pressure drop across the choke causes flashing (light-component vaporisation from the oil) and condensation (heavy-component dropout from the gas in some envelopes). The phase composition at the throat is not the same as the upstream composition.
- **Critical-vs-subcritical transition** — at sufficient downstream-to-upstream pressure ratio the gas phase reaches sonic velocity at the throat (critical flow); further downstream pressure reduction does not increase flow. The transition point is sensitive to mixture composition and is not the single-phase-gas critical-pressure ratio.
- **Non-equilibrium effects** — at high acceleration through the orifice, the gas and liquid phases may not be in thermodynamic equilibrium; phase composition at the throat may lag the equilibrium calculation.
- **Sand and water in the stream** — sand-laden flow modifies the effective fluid density and viscosity; high water cut changes the slip behaviour relative to oil-dominated flow.

The dominant industry approach treats these effects with empirical correlations calibrated against field and laboratory data, and accepts a wider uncertainty band than single-phase choke modelling carries.

## Sachdeva 1986 — critical-flow framework (SPE 15657)

The Sachdeva 1986 paper (SPE 15657, "Two-Phase Flow Through Chokes") established the dominant industry framework for **critical multiphase flow** through production chokes. The paper develops an analytical framework based on simultaneous mass-balance, energy-balance, and momentum-balance equations for a two-phase mixture accelerating through a convergent orifice, with explicit treatment of the critical-flow boundary at the throat.

**What the framework adds:**

- Provides a closed-form determination of the critical pressure ratio for a two-phase mixture as a function of the upstream gas-liquid ratio, gas and liquid densities, and an isentropic exponent for the mixture.
- Predicts the critical-flow mass flux through the choke under critical conditions; once the downstream pressure ratio falls below the critical ratio, the predicted flow rate is independent of further downstream-pressure reduction.
- Has been validated against laboratory and field data across a range of oil-gas-water mixtures and choke geometries.

**Operational use:** Sachdeva 1986 is the default critical-flow correlation in many commercial nodal-analysis packages and is the most widely-cited industry framework for multiphase choke critical flow. Operators reading software-output choke-rate predictions should know whether the software uses Sachdeva or one of the alternatives, because the difference between frameworks at the same operating point can be material for facility-sizing or production-allocation purposes.

**Implementation note:** the engineering-unit equations are in the original SPE paper; operators implementing the framework should consult SPE 15657 directly and validate against their reservoir-fluid PVT and field-test data. This wiki page intentionally does not transcribe the formulas — calc-citation candidates must be implemented from primary sources with proper sidecar citation per the calc-citation contract.

## Perkins 1993 — subcritical-flow extension (SPE 20633)

The Perkins 1993 paper (SPE 20633, "Critical and Subcritical Flow of Multiphase Mixtures Through Chokes") extends the Sachdeva framework to the **subcritical-flow** regime where the downstream pressure ratio is above the critical ratio and the flow rate depends on both upstream and downstream pressures (rather than being capped by the critical-flow ceiling).

**What the framework adds:**

- Provides a unified correlation that returns mass flow rate as a function of upstream pressure, downstream pressure, and fluid composition, valid across both subcritical and critical regimes.
- Reduces to the Sachdeva critical-flow result when the downstream-to-upstream pressure ratio falls below the critical threshold.
- Handles the operational regime where the choke is partially open and the well is producing below the critical-flow flow rate (e.g. bean-up conditions, intentional flow rate restriction, well-test conditions).

**Operational use:** Perkins 1993 is the standard for subcritical flow in multiphase choke modelling. Critical-flow operation is the dominant production-well operating regime (most production chokes operate critically through most of the well's life), but bean-up, late-life low-rate operation, and well-test operation often cross into subcritical territory and require the Perkins framework.

**Implementation note:** as with Sachdeva 1986, engineering-unit equations are in the original SPE paper. The continuous-transition between subcritical and critical regimes is a key reliability property of the Perkins framework that simpler regime-switching correlations do not preserve.

## Ashford-Pierce 1975 — early framework (SPE 5482)

The Ashford-Pierce 1975 paper (SPE 5482, "Determining Multiphase Pressure Drops and Flow Capacities in Down-Hole Safety Valves") established an earlier multiphase-choke framework that pre-dates the Sachdeva and Perkins corpus. The framework was developed for downhole safety valves specifically (a related but distinct device class) but the underlying flow-through-restriction physics applies to production chokes as well.

**What the framework adds:**

- Provides a polytropic-expansion approach to the two-phase pressure drop across an orifice, with empirical coefficients calibrated against downhole-safety-valve laboratory data.
- Was widely adopted in pre-Sachdeva-era choke modelling and remains in some legacy software packages.
- Is the historical reference point against which Sachdeva 1986 and Perkins 1993 are often compared in benchmarking studies.

**Operational use:** Ashford-Pierce 1975 is less commonly used in modern modelling than Sachdeva or Perkins, but operators encountering legacy software or older operating-procedure documents may still see Ashford-Pierce-derived choke predictions. When benchmarking choke models against field data, Ashford-Pierce, Sachdeva, and Perkins should all be on the comparison panel.

## Bertuzzi-Tek-Poettmann (BTP) and modern industry approaches

The Bertuzzi-Tek-Poettmann formulation (and its descendants in modern industry-standard nodal-analysis packages) extends the Sachdeva-Perkins core with explicit handling of:

- **Non-Newtonian fluid behaviour** at the choke for heavy oils and emulsion-laden streams
- **High-water-cut operations** where the liquid phase is water-dominated rather than oil-dominated, changing the slip behaviour
- **Sand-laden and solids-laden flow** where the effective mixture density and viscosity differ from clean-fluid assumptions
- **HPHT envelope corrections** where the PVT framework underpinning the Sachdeva-Perkins energy balance must be extended to high-pressure / high-temperature conditions

Most modern commercial nodal-analysis packages (PIPESIM, PROSPER, WellFlo, GAP) include several multiphase-choke correlations as user-selectable options, with Sachdeva and Perkins as defaults for most service envelopes and BTP / vendor-specific extensions for specialised service. Operators should validate the selected correlation against well-test data before relying on it for production-allocation or facility-design decisions.

## Critical-to-subcritical regime transition

A central operational fact is that production chokes operate most of the time in the **critical-flow regime** — the downstream-to-upstream pressure ratio is below the critical threshold and the flow rate is set entirely by upstream pressure and choke geometry. This is operationally desirable because:

- Flow rate is insensitive to downstream pressure fluctuations (separator pressure variations, sales-line backpressure variations) — the well "sees" only the upstream side.
- Operating-point prediction is straightforward: the choke-flow correlation returns mass flux as a function of upstream conditions only.
- Facility-side disturbances (compressor trips, separator-level transients) do not propagate upstream past the choke during critical operation.

**Operational subcritical-regime triggers:**

- Bean-up sequences (small bean openings during well startup) cross into subcritical before the well reaches steady operating-point
- Late-life low-rate wells with high downstream pressure relative to upstream may operate subcritically
- Well-test sequences may intentionally explore subcritical operating points
- Facility-upset conditions can transiently push wells into subcritical operation as separator pressure rises

Choke modelling that does not handle the regime transition continuously (e.g. simple critical-flow-only correlations) can produce material discontinuities at the regime boundary and unreliable predictions during bean-up or transient operation. The Perkins 1993 framework's continuous regime treatment addresses this.

## Calibration and uncertainty

Multiphase choke models are not point predictions; they are correlations with finite predictive accuracy. Practitioner discipline includes:

- **Calibration against well-test data** — every well's actual rate-vs-upstream-pressure-vs-choke-position data should be compared to the model prediction; systematic deviations should be folded into a per-well calibration factor or a re-selection of the correlation family.
- **Uncertainty propagation** — predicted rates from choke models carry uncertainty bands that depend on the correlation choice, the fluid characterisation quality, and the operating-regime location. Production-allocation and facility-sizing calculations should propagate these uncertainties.
- **Updating with operating history** — wells age, fluid composition shifts (water cut climbs, GOR changes), and choke trim wears; correlation calibration that was good early-life may drift over time and should be refreshed periodically.
- **Cross-checks against alternative methods** — pressure-temperature surveys, multiphase flow meters, and well-test-separator measurements provide independent rate measurements that should be used to cross-check choke-model predictions.

## Calc-citation note

The multiphase choke correlations described above are prime calc-citation candidates per the workspace-hub#2481 calc-citation contract. Any future implementation in `digitalmodel` or sibling computational packages should:

- Consume the constants and coefficients from the original SPE papers (Sachdeva 1986, Perkins 1993, Ashford-Pierce 1975) rather than from this wiki page
- Emit a `Citation` sidecar pointing to the SPE reference (or an intermediate wiki page if/when one is created for the specific correlation)
- Track correlation-selection in the sidecar so downstream consumers can reconstruct which framework produced the prediction

This page intentionally does not transcribe the engineering-unit equations to avoid creating a derivative-citation hazard; the original SPE papers are the authoritative sources and any implementation should cite them directly.

## Cross-references

- [Choke Management](choke-management.md) — operational discipline router
- [Choke Types](choke-types.md) — choke architecture families that the multiphase models describe
- [Choke Sand Erosion](choke-sand-erosion.md) — sand-laden multiphase flow erosion physics
- [Gas Lift Overview](gas-lift-overview.md) — IPR / TPR / choke nodal-analysis context

## Public references

- **Sachdeva, R., Schmidt, Z., Brill, J. P. & Blais, R. M.** — "Two-Phase Flow Through Chokes," SPE 15657, presented at the SPE Annual Technical Conference and Exhibition, October 1986. Foundational critical-flow correlation.
- **Perkins, T. K.** — "Critical and Subcritical Flow of Multiphase Mixtures Through Chokes," SPE 20633, SPE Drilling & Completion 8(4), December 1993. Unified critical/subcritical-regime correlation.
- **Ashford, F. E. & Pierce, P. E.** — "Determining Multiphase Pressure Drops and Flow Capacities in Down-Hole Safety Valves," SPE 5482, JPT 27(9), September 1975. Pre-Sachdeva-era framework, still referenced in legacy software.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, 1999 (ISBN 978-1-55563-080-5). Foundational multiphase-flow reference; choke-modelling chapter contextualises the SPE-paper corpus.
- **Beggs, H. D.** — *Production Optimization Using Nodal Analysis*, 2nd ed., OGCI Publications, 2003 (ISBN 0-930972-14-7). Nodal-analysis framework that consumes multiphase-choke correlations.
- **SPE OnePetro multiphase-choke literature** — extensive corpus on correlation comparisons, field-calibration studies, and HPHT / heavy-oil / high-water-cut extensions of the Sachdeva-Perkins core.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapter covers choke modelling overview.

## Notes

- This page describes the four foundational frameworks at the prose level. Engineering-unit equations, coefficient values, and worked examples are not transcribed here — operators implementing choke modelling should consult the original SPE references and calibrate against well-test data.
- Correlation selection (Sachdeva vs Perkins vs Ashford-Pierce vs BTP) is service-envelope-dependent; no single correlation is universally best. Practitioner discipline is to validate the chosen correlation against the specific well's measured data.
- Modern commercial nodal-analysis packages include several multiphase-choke correlations as user-selectable options. The correlation choice should be documented in the production-engineering operating-procedure record for each well.
- Calc-citation sidecar implementation guidance: any computational consumer of these correlations should cite the original SPE paper as the authoritative source, not this wiki page or a derived intermediate.
