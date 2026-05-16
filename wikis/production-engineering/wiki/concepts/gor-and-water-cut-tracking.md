---
title: "GOR and Water-Cut Tracking"
tags: [gor, gas-oil-ratio, water-cut, watercut, bsw, microwave-watercut, capacitance-watercut, coriolis, phase-envelope, reservoir-management, allocation-input]
added: 2026-05-16
last_updated: 2026-05-16
---

# GOR and Water-Cut Tracking

## Scope

Gas-oil ratio (GOR) and water cut are the two phase-composition metrics that, alongside the three-phase rate, fully characterise a producing well's stream for both production-accounting (allocation) and reservoir-management purposes. Both are sampled discretely during the periodic well test (see [Well Test and Reconciliation](well-test-and-reconciliation.md)) and increasingly measured continuously by inline meters on the wellhead or test header. Both evolve continuously across the producing life of the well, and their trajectories carry critical reservoir-management signal.

This page covers:

- GOR measurement methodology (separator gas-rate-to-oil-rate ratio, downhole-sample PVT analysis, continuous inline gas-rate metering)
- Water-cut measurement methodology (grab sample by centrifuge / Karl Fischer / distillation; inline microwave, capacitance, and Coriolis-density technologies)
- Phase-envelope implications (GOR shift across bubble point, water-cut shift across breakthrough)
- Reservoir-management feedback loop (rising GOR diagnostic; water-cut-breakthrough diagnostic; the operator response framework)

## GOR — gas-oil ratio

GOR expresses the volumetric ratio of produced gas to produced oil, both at standard conditions (60°F, 14.7 psia in US convention; 15°C, 101.325 kPa in SI/metric convention). The reported quantity is in standard cubic feet of gas per stock-tank barrel of oil (scf/STB) in US practice, or standard cubic metres of gas per standard cubic metre of oil (sm³/sm³) in metric practice.

### Solution-GOR vs producing-GOR

Two distinct GORs are relevant operationally:

- **Solution-GOR (R_s)** — the dissolved-gas-in-oil ratio at reservoir conditions. A PVT property determined by laboratory analysis of bottomhole or wellhead-recombined samples. Bounds the maximum GOR that the well can produce when reservoir pressure is above bubble point (all dissolved gas stays in oil; producing GOR equals R_s minus surface-flash losses).
- **Producing-GOR (R_p)** — the actual surface-measured gas-to-oil rate ratio. Equals R_s when reservoir pressure is above bubble point; rises above R_s when reservoir pressure has fallen below bubble point and free-gas mobility in the reservoir delivers extra gas to the wellbore.

The relationship between R_s and R_p is the diagnostic axis. A rising R_p above R_s — at constant reservoir-pressure-drawdown operating point — signals that the reservoir-pressure depletion has crossed the bubble-point envelope and free gas is now flowing.

### GOR measurement during the well test

Three approaches dominate operator practice:

1. **Separator gas rate / separator oil rate** — the direct ratio from the three-phase test separator (per [Well Test and Reconciliation](well-test-and-reconciliation.md)). The simplest method; accuracy is bounded by the separator gas-rate and oil-rate measurements.
2. **Bottomhole sample PVT analysis** — periodic bottomhole sampling combined with laboratory PVT analysis produces a high-accuracy R_s measurement. Cost-intensive (single-sample-per-well lab cost in the tens of thousands of dollars); typically run once per well at completion and again only on significant operating change.
3. **Inline gas-and-liquid rate continuous metering** — wellhead-mounted three-phase flowmeter or paired single-phase meters produce continuous GOR; reduces dependence on the test-separator schedule.

### Producing-GOR shift across bubble point

The producing-GOR trajectory is one of the most-watched reservoir-management curves:

- **Above bubble point** — R_p ≈ R_s; GOR flat across the producing period.
- **Crossing bubble point** — R_p begins to rise above R_s as free gas in the reservoir flows preferentially to the wellbore (gas mobility > oil mobility in two-phase flow). The rate of rise depends on relative-permeability characteristics, vertical permeability (gas coning susceptibility), and drawdown discipline.
- **Far below bubble point** — R_p can rise to multiples of R_s as the gas-saturation in the near-wellbore zone increases. In severe cases the well becomes a gas-dominant producer with the oil rate collapsing to negligible.

The operator response to rising R_p is graduated:

- Reduce drawdown (bean back the choke) to slow the gas coning
- Pull the well off production temporarily (shut-in to allow gas-saturation redistribution)
- Workover (re-perforation higher in the column to avoid the gas-coned section; or downhole-flow-control intervention via ICVs)
- Acceptance (some fields run R_p:R_s ratios of several multiples for years in steady-state; the management threshold depends on processing-facility gas-handling capacity and on the lease economic envelope)

## Water cut

Water cut is the volumetric fraction of the liquid produced stream that is water. Reported as a percentage (0% = dry oil; 100% = pure water). Distinct from basic-sediment-and-water (BS&W), which adds solid-particulate content to the water fraction for custody-transfer purposes.

### Water-cut measurement — grab-sample methods

Discrete sampling during the well test is the legacy methodology and remains the reconciliation reference for inline meters:

- **Centrifuge** — sample is centrifuged in a graduated tube; oil and water separate by density; water fraction is read directly. Standard ASTM D4007 methodology. Fast (minutes per sample) and low-cost; accuracy degrades on stable emulsions.
- **Karl Fischer titration** — chemical reaction with iodine in the presence of water produces a stoichiometric titration endpoint. Standard ASTM D4928. High accuracy at low water cuts; analytical-lab procedure (turnaround typically hours).
- **Distillation** — sample is co-distilled with toluene or xylene; water separates and is measured volumetrically in a graduated receiver. Standard ASTM D4006 / D95. Slow but reliable across the full water-cut range; the reference method for custody-transfer BS&W.

### Water-cut measurement — inline meter technologies

Continuous wellhead-mounted water-cut meters have largely replaced grab-sampling-only practice in mature fields. Three principal technologies dominate:

**Microwave permittivity** — measures the dielectric permittivity of the flowing fluid; water and oil have very different permittivities (water ~80, oil ~2 at low frequency), so the mixture permittivity is a sensitive function of water content. Accurate across most of the water-cut range, with degraded performance at very low water cut (small dielectric contrast) and at very high water cut (the technology has to invert to read water content as the residual). Vendor families include Roxar (Emerson), Phase Dynamics, AGAR, and Weatherford Red Eye.

**Capacitance** — measures the electrical capacitance of the flowing fluid between two electrodes; capacitance is dominated by water content. Lower-cost than microwave; performance degrades at high water cut (continuous-water phase short-circuits the electrodes) and on emulsions where the phase-distribution is unstable. Vendor families include AGAR, Endress+Hauser, Yokogawa.

**Coriolis density inference** — Coriolis mass-flow meters report fluid density continuously; if the pure-oil density and pure-water density are both known, the water-cut can be inferred from the measured mixture density. Accurate at high water cut where the density contrast is largest; degraded at low water cut where density contrast is smaller and gas entrainment biases density. Vendor families include Emerson Micro Motion, Endress+Hauser Promass, Krohne Optimass.

### Measurement vendor-citation discipline

Water-cut and inline-metering vendors are cited by name and general capability only.

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **Roxar (Emerson)** | "Roxar microwave water-cut family — widely deployed in mature North-Sea production" | Microwave-permittivity calibration internals, accuracy vs salinity curves |
| **Phase Dynamics** | "Phase Dynamics microwave water-cut meter — independent vendor in the inline water-cut market" | Proprietary signal-processing algorithm or calibration-protocol internals |
| **Endress+Hauser** | "Endress+Hauser Promass Coriolis family used for water-cut density inference" | Proprietary density-temperature correction internals, performance-curve transcriptions |
| **Emerson Micro Motion** | "Emerson Micro Motion Coriolis family widely deployed for liquid-rate and density measurement" | Proprietary multi-variable signal-processing algorithms |

Vendor mentions in this wiki are at the "named at name + general capability" level only. No proprietary internals.

### Water-cut breakthrough diagnostic

Water-cut breakthrough is one of the most-watched reservoir-management events:

- **Pre-breakthrough** — water cut is 0% (or trace, reflecting connate-water co-production at low levels). The well produces dry oil.
- **Breakthrough event** — water cut rises above background. Source can be aquifer encroachment (bottom-water drive), water-injection breakthrough from a nearby injector (water-flood pattern), or coning from a perched water zone above or below the producing perfs.
- **Rising water cut** — water cut continues to climb as the swept zone expands or as coning accelerates. The trajectory depends on reservoir architecture, drainage pattern, and drawdown discipline.
- **High-water-cut steady state** — many mature wells run at 80-95% water cut for years; oil rate falls as water rate rises, but the well can remain economic as long as the oil-revenue minus produced-water-handling cost is positive.

The operator response to water-cut breakthrough varies by source diagnosis:

- **Aquifer encroachment** — typically accepted; pattern-management response is field-wide rather than per-well
- **Injector breakthrough** — water-flood pattern adjustment (injection rate redistribution, conformance treatment, polymer injection in some plays)
- **Coning** — reduce drawdown to slow coning; workover for re-perforation or zonal isolation; downhole-flow-control intervention via [Downhole Flow Control](downhole-flow-control.md) ICDs/ICVs

## Phase-envelope implications

GOR and water-cut both interact with flow-assurance phase-envelope analysis:

- **Rising GOR shifts the fluid composition toward higher gas content**, lowering the bubble-point pressure margin in surface-piping operations and shifting the hydrate-stability envelope. Increased gas content at the choke discharge worsens choke-cooling Joule-Thomson behaviour and raises hydrate-formation risk. See [Hydrate Management](hydrate-management.md).
- **Rising water cut shifts the produced stream toward water-dominant chemistry**, accelerating mineral-scale deposition risk (sulphate scales, calcium carbonate where production waters mix), accelerating microbiologically-influenced corrosion in low-flow regions, and increasing the demineralised-water carry-over to downstream processing. See [Mineral Scale](mineral-scale.md), [Corrosion Management](corrosion-management.md).
- **Combined GOR-and-water-cut shift** changes the operating point on the multiphase-flow regime map for the producing string ([Flow Regime Maps](flow-regime-maps.md)), with consequences for liquid loading in gas wells and slug-flow onset in oil wells.

## Reservoir-management feedback loop

GOR and water-cut tracking close the feedback loop from surface-measurement back to subsurface-decision:

- **Surface measurement** — well-test sample analysis and inline meter trending produces the per-well-per-period GOR and water-cut series
- **Allocation input** — the per-well GOR and water-cut go into the [Production Allocation](production-allocation.md) arithmetic to attribute the commingled stream back to wells
- **Reservoir diagnostic** — the per-well GOR and water-cut trajectories feed reservoir-management analysis (decline analysis, type-well curves, conformance diagnosis, infill-drilling-candidate selection)
- **Reservoir intervention** — workover priorities, infill-drilling pattern adjustments, conformance-treatment campaigns, and pattern-management changes are triggered by GOR / water-cut signals
- **Surface-facility response** — facility design (water-handling capacity, gas-handling capacity, separator sizing) is partially driven by the field-level GOR / water-cut projection; persistent surprise to the projection triggers brownfield-modification AFEs

## Cross-domain interactions

- **Production allocation** — GOR and water-cut from the well test are critical inputs to allocation arithmetic. See [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md).
- **Custody-transfer measurement** — BS&W (the water + sediment fraction) is the custody-transfer-grade water-cut measurement at the LACT unit. See [Custody-Transfer Overview](custody-transfer-overview.md).
- **Flow assurance** — GOR and water-cut shifts move the operating point on hydrate, scale, asphaltene, and corrosion envelopes. See [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md), [Mineral Scale](mineral-scale.md).
- **Well integrity** — produced-water chemistry (salinity, dissolved-gas content, microbial activity) drives internal corrosion mechanisms. See [Well Integrity During Production](well-integrity-during-production.md), [Corrosion Management](corrosion-management.md).
- **Artificial lift** — water-cut rise changes ESP head requirements (denser fluid column) and gas-lift performance (denser fluid raises lift-gas demand). GOR rise changes ESP gas-handling stress (free gas at intake) and plunger-lift cycle behaviour (free gas changes minimum-GLR margin). See [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md).
- **Reservoir management** — GOR and water-cut trajectories are primary inputs to decline analysis and to refrac / workover candidate selection. See [Production History Decline Analysis](production-history-decline-analysis.md), [Refrac (Re-Fracturing)](refrac.md).
- **Choke management** — drawdown change (choke bean-up or bean-down) shifts the GOR and water-cut trajectory. See [Choke Management](choke-management.md).

## Cross-references

- [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md) — allocation arithmetic consumes GOR and water-cut
- [Custody-Transfer Overview](custody-transfer-overview.md) — BS&W as the custody-transfer water-cut measurement
- [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md) — GOR and water-cut sampling uncertainty contribute to allocation uncertainty
- [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md), [Mineral Scale](mineral-scale.md), [Corrosion Management](corrosion-management.md) — chemistry / envelope impact of composition shifts
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md) — artificial-lift implications
- [Production History Decline Analysis](production-history-decline-analysis.md), [Refrac (Re-Fracturing)](refrac.md) — reservoir-management diagnostic feedback
- [Choke Management](choke-management.md) — drawdown control as GOR / water-cut intervention
- [Downhole Flow Control](downhole-flow-control.md), [Selective Production](selective-production.md) — coning-management interventions
- Phase 5 forward-refs: [Production SCADA Architecture](production-scada-architecture.md), [Production Data Historian Patterns](production-data-historian-patterns.md) — continuous-meter data path

## Public references

- **McCain, W. D.** — *The Properties of Petroleum Fluids*, 2nd edition, PennWell 1990 (ISBN 978-0-87814-335-5). The practitioner-canonical PVT reference; the source for solution-GOR vs producing-GOR distinction and for bubble-point-crossing diagnostics.
- **Ahmed, T.** — *Reservoir Engineering Handbook*, 5th edition, Gulf Professional Publishing (Elsevier) 2018 (ISBN 978-0-12-813649-2). Reservoir-engineering reference covering coning, breakthrough, and per-well GOR / water-cut interpretation.
- **Smith Jr., M.** — *Practical Industrial Flow Measurement*, Wiley 2007 (ISBN 978-0-470-04162-7). Inline measurement-technology coverage including water-cut meter families.
- **Falcone, G., Hewitt, G. F., Alimonti, C.** — *Multiphase Flow Metering: Principles and Applications*, Elsevier 2009 (ISBN 978-0-444-52991-6). MPFM technology reference; covers the inline water-cut and GOR measurement principles.
- **ASTM D4007** — Standard Test Method for Water and Sediment in Crude Oil by the Centrifuge Method (Laboratory Procedure). Standard for centrifuge water-cut measurement.
- **ASTM D4928** — Standard Test Methods for Water in Crude Oils by Coulometric Karl Fischer Titration. Standard for Karl Fischer water-cut measurement.
- **ASTM D4006 / D95** — Standard Test Methods for Water in Crude Oil by Distillation. Standard for distillation water-cut / BS&W measurement.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover well-test sampling and the GOR / water-cut framework.
- **SPE OnePetro literature on water-cut metering and GOR trending** — extensive corpus on inline-meter deployment, MPFM water-cut accuracy, and reservoir-management GOR diagnostic field cases.
