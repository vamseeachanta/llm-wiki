---
title: "Well Test and Reconciliation"
tags: [well-test, test-separator, three-phase-separator, multiphase-flow-meter, mpfm, allocation-factor, reconciliation, residual, recalibration, production-accounting]
added: 2026-05-16
last_updated: 2026-05-16
---

# Well Test and Reconciliation

## Scope

The periodic well test is the primary measurement event that calibrates the per-well allocation factor used in [Production Allocation](production-allocation.md). The test isolates a single producing well from the commingled bulk stream, routes it to dedicated three-phase measurement (either a test separator with discrete oil / gas / water rate measurements, or a multiphase flow meter), and produces the per-well three-phase rate plus the per-well water-cut and GOR samples. The well-test rate then feeds the allocation arithmetic until the next test.

Reconciliation is the recurring activity (typically monthly for fiscal-allocation, daily-to-weekly for operational reservoir-management) of comparing the sum of well-test-derived theoretical contributions against the actual measured commingled volume at the export meter, computing the closure residual, posting it to the allocation books, and triggering follow-up actions (re-test on accelerated cadence, audit of the export meter or test separator, investigation of evaporation / line-pack / fugitive losses).

This page covers the periodic well-test workflow, the two dominant test-measurement architectures (three-phase separator and multiphase flow meter), the reconciliation residual diagnostic, and the allocation-factor recalibration mechanics. It is the operational complement to the framework framing on [Production Allocation](production-allocation.md).

## Periodic well-test workflow

The standard operator workflow for the periodic well test runs:

1. **Schedule** — each well in the field is on a defined test schedule (commonly weekly to monthly, with cadence varying by field size, well count, test-equipment availability, and operator preference). The schedule is published to operations as a forward-looking calendar and tracked against actual completion in the production-accounting system.
2. **Route** — at the scheduled time, the field-control system (DCS or SCADA) routes the target well from the bulk-production header to the test header (test-separator inlet or multiphase-meter inlet). All other wells continue to the bulk header. Valve sequencing is configured to avoid commingling during the routing transition; a stabilisation period (commonly minutes to hours depending on field operating practice) is allowed before measurements are accepted.
3. **Stabilise** — the test stream is allowed to reach steady state at the new operating point. Surface pressures, separator levels, gas and liquid rates are monitored for stability. Operations that disrupt stability during this window (choke change, lift-gas-injection change, ESP frequency change on other wells affecting separator-pressure setpoint) are coordinated to avoid corrupting the test.
4. **Measure** — three-phase rates are integrated across a defined test duration (commonly 4-24 hours depending on field practice, well stability, and statistical confidence required). Discrete samples for water-cut, GOR, and (less commonly) basic-sediment-and-water (BS&W) and salt content are taken at scheduled intervals during the test window.
5. **Sample lab analysis** — water-cut grab samples are analysed for produced-water content (centrifuge, Karl Fischer titration, or distillation methodology); GOR samples are analysed in a sample lab for solution-gas content. Lab-analysis results are reconciled against the field rate measurements as a cross-check.
6. **Update allocation factor** — the lab-reconciled test rate replaces the prior allocation-factor input for that well. The allocation books are updated forward from the test date until the next test.
7. **Return to bulk header** — the well is routed back to the bulk-production header; the next well in the schedule is routed to the test header.

The workflow is repeated indefinitely across the producing life of the field. The operational discipline is the operator's primary defence against allocation-factor drift.

## Three-phase separator test

The classic well-test architecture is a dedicated **test separator** — a three-phase vessel that separates produced fluid into discrete oil, gas, and water streams, with rate measurements on each outlet:

- **Oil stream** — measured at the oil outlet by a positive-displacement meter, turbine meter, or Coriolis meter (Coriolis increasingly preferred for direct mass measurement and density inference). Volume-based meters require density correction.
- **Gas stream** — measured at the gas outlet typically by an orifice meter (per API MPMS Chapter 14), ultrasonic meter, or Coriolis meter. Gas measurement requires composition input (chromatograph or assumed standard composition) for energy-content and density correction.
- **Water stream** — measured at the water outlet by a positive-displacement or turbine meter. Water-cut and salt content are sampled separately for chemistry tracking.

The three-phase test separator is the dominant architecture in mature onshore and offshore production where dedicated test infrastructure is cost-justified. The separator is typically a horizontal or vertical pressure vessel sized to the highest-rate well in the field at expected operating pressure, with internals (weirs, baffles, demisters) to maximise three-phase separation efficiency.

### Operational limitations

- **Carry-over** — small oil carry-over into the gas stream (mist entrainment) and small gas carry-under into the oil stream (incomplete gravity separation) bias the three-phase measurement. The biases are typically <1-2% for well-designed separators on stable wells but can be substantially larger on unstable (slugging) wells.
- **Stabilisation time** — full three-phase separation requires the test stream to fill the separator and reach steady-state level control. For wells with low rate or large liquid hold-up, the stabilisation window can consume a meaningful fraction of the test budget.
- **Composition assumption for gas measurement** — orifice-meter rate calculation requires a gas composition input (chromatograph stream or assumed composition). On dry-gas wells the assumption is acceptable; on wet-gas or condensate wells the assumed composition can introduce bias.

## Multiphase flow meter (MPFM) test

For subsea wells, deepwater wells with limited topsides space, and onshore wells where a dedicated test separator is not cost-justified, the **multiphase flow meter** is the alternative architecture. The MPFM measures the three-phase rate directly without separating the phases, using a combination of density measurement (gamma-ray, microwave attenuation), velocity measurement (Venturi differential pressure, cross-correlation between two pressure sensors), and water-cut measurement (microwave permittivity, capacitance):

- **Inline placement** — the MPFM sits inline with the flow, typically downstream of the wellhead choke and upstream of any commingling. No phase separation; the meter consumes the live multiphase stream.
- **Three-phase output** — the meter outputs continuous oil, gas, and water rates derived from the density / velocity / water-cut measurements through a vendor-proprietary inversion algorithm. The proprietary algorithm internals are not transcribed in this wiki — they are the vendor's IP and are not part of the public-literature framework.
- **Subsea application** — MPFMs are routinely installed on subsea trees in deepwater field developments where allocating subsea-well contributions to a shared host-facility production stream requires per-well measurement at the seabed. Topsides MPFMs are also widely deployed.

### Measurement vendor-citation discipline

MPFM vendors are cited in this wiki by name and general capability only. Proprietary inversion-algorithm internals, accuracy-spec transcriptions, and performance-curve copies are out of scope per the workspace vendor-IP discipline.

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **Schlumberger / SLB** | "Schlumberger PhaseTester / Vx — gamma-ray multiphase meter family widely deployed for subsea well-test duty" | Proprietary gamma-ray inversion algorithm, accuracy curves vs water-cut, calibration-correction internals |
| **TechnipFMC** | "TechnipFMC subsea multiphase metering offering, used on subsea-tree well-test installations" | Detailed accuracy-vs-GVF performance curves, proprietary signal-processing pipeline |
| **Roxar (Emerson)** | "Roxar / Emerson topsides and subsea MPFM family; microwave-and-impedance principle widely used in mature North-Sea installations" | Microwave-permittivity calibration internals, proprietary multi-energy gamma processing |
| **Pietro Fiorentini** | "Pietro Fiorentini multiphase meter family — independent vendor in the MPFM market" | Proprietary spool internals or pressure-transducer signal-processing |

Vendor mentions in this wiki are at the "named at name + general capability" level only; no proprietary internals are reproduced. The vendor archetype framing matches the pattern established in [Choke Sand Erosion](choke-sand-erosion.md) and [Electric Submersible Pumps](electric-submersible-pumps.md).

### Operational limitations

- **Calibration drift** — MPFM accuracy depends on periodic calibration against a reference (commonly the test separator at a campaign-level calibration event, where the MPFM is intercompared against the separator on a known well). Drift between calibrations is the dominant uncertainty source.
- **Water-cut range** — many MPFM technologies degrade in measurement accuracy at extreme water cuts (very low, near 0%; very high, >95%). Operator selection accounts for the expected well-life water-cut trajectory.
- **Gas volume fraction (GVF) range** — high-GVF wells (>95% gas by volume at meter conditions) stress MPFM technology beyond the design envelope of some meter families. Wet-gas-specific meter families address this segment.

## Reconciliation residual

The reconciliation residual is the closure check on the allocation framework. Computed at each allocation period (commonly monthly for fiscal-allocation, daily-to-weekly for operational reservoir-management):

`Residual = Measured commingled volume (at export meter) − Sum of theoretical well contributions (well-test-derived rate × producing time)`

The residual is the operator's primary diagnostic for allocation-framework health:

- **|Residual| < operator threshold (commonly ±2-5% of measured volume on a per-stream basis)** — framework is operating inside its intended uncertainty envelope. No follow-up.
- **Persistent positive residual** — measured stream consistently exceeds theoretical sum. Investigate: well-test undercounting (test-separator gas carryover, MPFM bias low at current GVF); wells producing higher rate than last-test rate; line-pack accumulation that the residual is absorbing.
- **Persistent negative residual** — measured stream consistently lower than theoretical sum. Investigate: well-test overcounting (water-cut sample non-representative biasing water rate high → oil rate low → theoretical contribution understated); evaporation losses between wellhead and export meter; fugitive emissions; line-pack depletion.
- **Drifting residual** — residual trends across allocation periods. Trigger: accelerate the well-test schedule for the wells whose contribution is least certain; audit the export-meter calibration; audit the test-separator calibration history.

The residual disposition (which book absorbs it) depends on the allocation method elected per [Production Allocation](production-allocation.md):

- Under **allocation by proportion**, the residual is distributed across all wells in proportion to their theoretical contribution.
- Under **allocation by difference**, the residual is fully absorbed into the single designated well's allocation. The other wells' allocations equal their theoretical contributions exactly.

The accounting policy is fixed at field-development time and documented in the production-allocation procedure.

## Virtual metering — model-based well-test alternative

A third architecture, increasingly deployed alongside physical test separators and MPFMs, is the **virtual flow meter (VFM)** — a software model that infers per-well rate from continuously-measured surface inputs (wellhead pressure, wellhead temperature, choke position, downstream pressure) plus a per-well calibrated multiphase-flow model. The VFM does not replace the periodic physical test; it estimates rate continuously between tests and reduces the operator's dependence on the test schedule for routine reservoir-management diagnostics.

VFM technology is consumed at concept level only in this wiki — vendor-specific calibration algorithms, model-update procedures, and accuracy-claim specifics are proprietary and out of scope. Operator adoption is uneven; the VFM is the dominant per-well continuous-rate mechanism on subsea-tieback developments where physical re-testing is operationally costly, and is widely deployed alongside MPFMs and test separators on mature offshore facilities.

The VFM does not eliminate the periodic physical test — operators run the physical test on a reduced cadence to recalibrate the VFM and to maintain bilateral acceptance of the rate measurement. The VFM's value is in the **between-test** period, where reservoir-management diagnostics benefit from continuous rate signal rather than waiting for the next physical test.

## Allocation-factor recalibration mechanics

After each well test, the allocation-factor input for that well is updated:

1. **Lab-reconcile** — field test rates are reconciled against the lab water-cut and GOR analyses. Significant lab/field disagreement (>operator threshold) triggers re-sample or re-test.
2. **Compute new test rate** — the lab-reconciled three-phase rate (oil, gas, water at standard conditions) is the new allocation-factor input for the well.
3. **Forward-apply** — the new test rate is applied to the well's allocated production from the test date forward, until the next test.
4. **Backward-correction policy** — operators differ in whether new test rates trigger backward correction of prior allocation periods. Conservative operators forward-apply only; some operators backward-correct the period since the previous test if the rate-change is large. The policy is documented in the production-allocation procedure and agreed with partners and regulators.
5. **Closure-residual review** — after the new well test, the reconciliation residual for the previous and following periods is re-examined to confirm the new test rate is internally consistent with the closure books.

## Cross-domain interactions

- **Production allocation** — well-test rate is the primary input to the allocation factor; the framework framing is on [Production Allocation](production-allocation.md).
- **GOR and water-cut tracking** — well-test GOR and water-cut sample results are the per-well chemistry inputs that drive allocation accuracy and feed reservoir-management decisions. See [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md).
- **Custody-transfer measurement** — the export-meter measurement is the reference against which the reconciliation residual is computed. See [Custody-Transfer Overview](custody-transfer-overview.md).
- **Flow-measurement uncertainty** — the uncertainty budget on the per-well-allocated volume is the convolution of test-measurement uncertainty (separator or MPFM), GOR / water-cut sampling uncertainty, period-rate-drift uncertainty (true rate may vary across the test interval), and export-meter uncertainty. See [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).
- **Artificial lift** — well-test results inform artificial-lift performance tracking. ESP test rate vs design rate is the run-life trending input ([Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Failure Modes](esp-failure-modes.md)). Gas-lift injection-gas-to-produced-fluid ratio per well is a test-derived operating metric ([Gas Lift Overview](gas-lift-overview.md)). Plunger-cycle test rate is the input to cycle-tuning ([Plunger Lift Cycle Optimization](plunger-lift-cycle-optimization.md)).
- **Flow assurance** — closure-residual investigation can surface line-pack accumulation, evaporation losses, or fugitive-emission paths; these overlap with [Flow Assurance](flow-assurance.md) for evaporation / line-management context.
- **Reservoir management** — well-test rate is the primary input to per-well decline analysis. See [Production History Decline Analysis](production-history-decline-analysis.md).

## Cross-references

- [Production Allocation](production-allocation.md) — framework anchor; allocation factor methodology and theoretical-vs-actual reconciliation framing
- [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md) — chemistry inputs to the well test
- [Custody-Transfer Overview](custody-transfer-overview.md) — export-meter reference for the residual computation
- [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md) — uncertainty budget on the test rate and on the residual
- [Production History Decline Analysis](production-history-decline-analysis.md) — test rate as decline-analysis input
- [Electric Submersible Pumps](electric-submersible-pumps.md), [Gas Lift Overview](gas-lift-overview.md), [Plunger Lift](plunger-lift.md) — artificial-lift test-rate consumers
- [Choke Management](choke-management.md) — choke changes trigger re-test
- [Flow Assurance](flow-assurance.md) — closure-residual investigation overlap
- Phase 5 forward-refs (not yet authored): [State Production Reporting](state-production-reporting.md), [Production SCADA Architecture](production-scada-architecture.md)

## Public references

- **API MPMS Chapter 20** — Manual of Petroleum Measurement Standards, Chapter 20 (Allocation Measurement). The publisher framework for allocation arithmetic that consumes well-test rate as input.
- **API MPMS Chapter 14** — Natural Gas Fluids Measurement (orifice-meter and related gas-measurement methodology). Referenced for test-separator gas-rate measurement.
- **API MPMS Chapter 4** — Proving Systems (meter-proving methodology for liquid-rate measurement on test-separator oil-outlet meters).
- **Smith Jr., M.** — *Practical Industrial Flow Measurement*, Wiley 2007 (ISBN 978-0-470-04162-7). Practitioner reference for measurement-technology selection across the well-test architectures.
- **Miller, R. W.** — *Flow Measurement Engineering Handbook*, 3rd edition, McGraw-Hill 1996 (ISBN 978-0-07-042366-4). Comprehensive metering reference covering all major technology families used in well-test duty.
- **Falcone, G., Hewitt, G. F., Alimonti, C.** — *Multiphase Flow Metering: Principles and Applications*, Elsevier 2009 (ISBN 978-0-444-52991-6). The reference textbook for MPFM technology principles.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Well-test and production-accounting chapters.
- **SPE OnePetro well-test literature** — extensive corpus on test-separator design, MPFM deployment, well-test interpretation, and allocation reconciliation field cases.
