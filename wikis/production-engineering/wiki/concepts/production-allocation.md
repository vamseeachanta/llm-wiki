---
title: "Production Allocation"
tags: [production-allocation, allocation-factor, well-test, reconciliation, custody-transfer, theoretical-vs-actual, allocation-by-difference, allocation-by-proportion, api-mpms-ch-20]
added: 2026-05-16
last_updated: 2026-05-16
---

# Production Allocation

## Scope

Production allocation is the operational discipline that attributes the **measured** commingled stream at a custody-transfer or facility-export meter back to the **individual wells** that contributed to it. The wells are typically commingled before the export meter — at the wellhead manifold, at the test-separator bypass, at the LACT-unit inlet, or further downstream at a fiscal-meter on a tieback to shore — and the allocation framework is what turns the single measured stream back into per-well-per-stream (oil / gas / water) volumes that can be booked to leases, partners, and reservoir-management accounts.

This page is the **router** for production-accounting coverage in the production-engineering wiki. It frames the allocation-factor methodology, the theoretical-vs-actual reconciliation framing, the two canonical allocation-by-difference vs allocation-by-proportion methods, and the cross-domain interactions with custody-transfer measurement and reservoir-management feedback. It links out to dedicated pages for [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody-Transfer Overview](custody-transfer-overview.md), and [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).

## Calc-citation contract status (this page)

Concept pages in this wiki describe foundational frameworks **structurally and qualitatively only** — engineering-unit equation forms with numeric coefficients and citation emission are deferred to standards-anchor pages and to downstream calc modules. When a downstream consumer (e.g. a `digitalmodel` production-allocation module) emits an allocation factor or a reconciled per-well volume, that module is expected to carry an explicit citation to API MPMS Chapter 20 (or equivalent operator-side allocation policy) per the workspace `calc-citation-contract` rule.

Posture for Phase 5 (production accounting + measurement cluster): **doc-only metadata**. This wiki page does NOT carry a `citations:` frontmatter block. Allocation-factor formulae, uncertainty-propagation expressions, and coverage-factor framework are described structurally; the engineering-unit forms with numeric coefficients are deferred to the standards page ([API MPMS Chapter 20](../standards/api-mpms-ch-20.md)) and to downstream calc modules whose responsibility it is to emit `Citation` instances per the workspace contract. No downstream consuming calc module exists at the time of writing (Phase 5 is the wiki coverage; consuming module work would land separately under a later digitalmodel issue), so the wiki page sits as **explanatory anchor only**.

This posture matches the production-engineering Phase 4 pattern (see `multiphase-choke-modeling.md`, `corrosion-management.md`) and the reservoir-engineering `permeability.md` precedent. Applied uniformly across the Phase 5 batch.

## What gets allocated

Production allocation attributes a measured commingled volume back to the contributing wells along three axes that vary in importance across operations:

- **Per-well** — each well's contribution to the commingled stream. This is the dominant axis for partner-allocation, royalty calculation, and reservoir-management feedback. Lease-allocated volumes are reported to regulators (Texas RRC, North Dakota Industrial Commission, BSEE for OCS, equivalents in other jurisdictions).
- **Per-stream** — oil, gas, water (and condensate where reported separately from oil). The three-phase split is what allocation is most commonly concerned with; uncertainty on the water phase is typically the largest, on the oil phase the smallest in a stable producing field.
- **Per-zone or per-completion** — when the well is a multi-zone completion (selective production with downhole flow control), the operator may need to allocate the well's contribution further across producing zones. This is the most uncertain allocation axis and depends on downhole instrumentation (PT gauges, ICVs with position telemetry, downhole flowmeters where installed). See [Selective Production](selective-production.md) and [Intelligent-Well Completions](intelligent-well-completions.md) for the completion-architecture context.

The framework on this page covers the per-well-per-stream axis as the core case; per-zone allocation is a specialised extension typically handled by the same arithmetic with additional downhole-measurement inputs and substantially higher uncertainty.

## Where allocation sits in the production-accounting workflow

Allocation is one step in the broader production-accounting workflow that runs from field-measurement through reporting:

1. **Field measurement** — well-tests, MPFM readings, custody-transfer meter readings captured continuously by the SCADA / data-historian layer (see [Production SCADA Architecture](production-scada-architecture.md) forward-ref, not yet authored)
2. **Validation** — automated and manual gates flag measurement-quality issues (out-of-range, frozen-sensor, stuck-value), removing bad data before it enters the closure books
3. **Allocation arithmetic** — closure of the period books with the chosen method (proportion or difference), distributing the measured commingled volume back to wells per the framework on this page
4. **Reservoir-management posting** — per-well-allocated volumes feed decline analysis, type-well curve maintenance, and intervention-candidate selection
5. **Partner-allocation posting** — per-partner shares of allocated volumes are computed against the joint-operating-agreement working-interest table
6. **Royalty-payment computation** — per-lease allocated volumes feed royalty payments to lease owners (typically by reference to the prior month's allocated volume series at month-end)
7. **Regulatory reporting** — per-lease allocated volumes feed state and federal regulator forms with their own submission cadence; see [State Production Reporting](state-production-reporting.md) forward-ref (Sub-issue 2, not yet authored)

The allocation step is the structural pivot — it is where measurement data becomes attributable, contractable, taxable. Errors here propagate forward into every downstream consumer.

## The allocation-factor methodology

Allocation factors are dimensionless scalars (one per well, per stream, per allocation period) that distribute the measured commingled volume back to the wells. The factor is calibrated from the periodic **well test** — a single-well test where the producing well is routed to a dedicated test separator (or measured by a multiphase flow meter), with all other wells routed to the bulk-production header. The well-test rate is the well's **theoretical** rate at the test conditions; the well's theoretical contribution to the commingled stream over the allocation period is the test rate scaled to the producing time across the period.

The allocation factor is the ratio that closes the books — it is what is multiplied against the well's theoretical contribution to produce the well's allocated share of the measured commingled stream. Because the measured commingled volume rarely equals the sum of theoretical-well contributions exactly (well-test measurement error, post-test rate drift, evaporation, line-pack changes, sampling representativeness, meter uncertainty all contribute residual), the allocation factor absorbs the closure residual.

Two canonical methods dominate operator practice and are codified in API MPMS Chapter 20 (paraphrased structurally here; see the standards page for the publisher framing):

### Allocation by proportion

Each well's allocated volume = (well's theoretical contribution / sum of theoretical contributions across wells) × measured commingled volume.

This method **distributes the closure residual proportionally** across all contributing wells. A well that contributes 30% of the theoretical commingled stream absorbs 30% of the closure residual. The method is symmetric, simple to compute, and dominant in onshore lease-allocation practice where partners and regulators expect a transparent distribution rule. It is the default method in API MPMS Chapter 20 informational treatment.

### Allocation by difference

One designated well (typically the largest or most stable) is allocated as the **difference** between the measured commingled volume and the sum of the other wells' theoretical contributions. The other wells take their theoretical contribution at face value; the designated well absorbs all closure residual.

This method is used when one well dominates the commingled stream (high contribution share, low relative measurement noise) or when one well's metering is materially less certain than the others. The dominant well's allocation has higher uncertainty than its theoretical contribution suggests; the other wells' allocations have lower uncertainty than the proportional method would assign them.

The method choice is an operator-side accounting policy decision, not a measurement decision. API MPMS Chapter 20 frames both methods; the operator and partners (or operator and regulator) agree on the method during field development and document it in the production-allocation procedure.

## Theoretical-vs-actual reconciliation

The closure residual is the gap between the **theoretical** sum (sum of well-test-derived contributions) and the **actual** measured commingled volume. The residual is the operational diagnostic for the allocation framework:

- **Small residual (operator-defined threshold, often ±2-5% of measured volume)** — allocation framework is operating inside its intended uncertainty envelope. No action.
- **Persistent positive residual** — measured stream consistently exceeds theoretical sum. Plausible causes: well-test undercounting (test separator carryover into vapour, multiphase-meter bias low), unaccounted-for production from a well that has not been re-tested recently, or systematic line-pack accumulation.
- **Persistent negative residual** — measured stream consistently lower than theoretical sum. Plausible causes: well-test overcounting (water-cut sample non-representative, GOR sample non-representative), evaporation losses between wellhead and export meter, fugitive emissions, or systematic line-pack depletion.
- **Drifting residual** — residual trend across allocation periods indicates the well-test calibration is decaying. Trigger: re-test the field on an accelerated schedule, audit the export-meter calibration, audit the test-separator calibration.

Reconciliation is the recurring activity (typically monthly for fiscal-allocation, more frequent for operational reservoir-management) of computing the residual, posting it to the closure books, and triggering investigation when the residual exceeds threshold. See [Well Test and Reconciliation](well-test-and-reconciliation.md) for the per-well-test workflow.

## Allocation-factor recalibration triggers

Allocation factors decay over time as fluid composition evolves, reservoir pressure declines, water-cut breaks through, GOR rises, and operating conditions drift. The recalibration triggers are operationally important:

- **Periodic well-test schedule** — most operators run each well through the test separator on a defined cadence (weekly to monthly depending on field, well count, and test-equipment availability). The fresh well-test rate replaces the prior allocation factor input.
- **Significant operating change** — choke change, artificial-lift change (gas-lift injection rate adjustment, ESP frequency change, plunger-cycle change), workover, intervention — all trigger an out-of-schedule well test to recalibrate.
- **Water-cut breakthrough** — when water cut on a previously-dry well rises above a threshold (see [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md)), the prior allocation factor is unreliable. The well must be re-tested and the new water-cut measurement carried into the allocation books.
- **GOR shift** — a rising GOR (gas coning, reservoir pressure decline crossing bubble point) similarly invalidates the prior allocation factor.
- **Persistent closure residual** — when the reconciliation residual exceeds operator threshold, the response is typically to accelerate the well-test schedule for the wells whose contribution is least certain.

## Cross-domain interactions

- **Custody-transfer measurement** — the upper bound on allocation accuracy is set by the custody-transfer meter at the export point. If the LACT unit or the fiscal-gas meter has a 0.25% uncertainty, the allocation arithmetic cannot recover per-well precision better than that. See [Custody-Transfer Overview](custody-transfer-overview.md).
- **Well-test methodology** — the input to allocation is the per-well rate measured during the periodic well test. Test-separator three-phase rates (oil, gas, water) and multiphase flow meter rates feed allocation arithmetic; sampling representativeness (water-cut grab sample, GOR sample) controls allocation accuracy. See [Well Test and Reconciliation](well-test-and-reconciliation.md).
- **GOR and water-cut tracking** — the allocation factor is sensitive to the per-well GOR and water-cut measurements made during the well test. Errors propagate into the allocated volumes for that well across the period until the next test. See [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md).
- **Reservoir management** — the per-well-allocated-volume series is the primary input to reservoir-management decisions: which wells are declining faster than expected, which wells should receive intervention, where infill drilling is justified. Bad allocation distorts reservoir-management signal. See [Production History Decline Analysis](production-history-decline-analysis.md).
- **Artificial lift** — allocation interacts with [Gas Lift Overview](gas-lift-overview.md) (allocated lift-gas consumption is a per-well operating cost), [Electric Submersible Pumps](electric-submersible-pumps.md) (allocated power consumption per pumped barrel is an operating metric), and [Plunger Lift](plunger-lift.md) (allocated per-cycle production is a unit-of-measure for plunger-cycle optimisation).
- **Flow-measurement uncertainty** — the uncertainty budget for allocated volumes is the convolution of well-test uncertainty, period-rate-drift uncertainty, and export-meter uncertainty. See [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).
- **Regulatory reporting** — allocated per-lease volumes feed state regulator reports (Texas RRC PR forms, ND IIC production reports, BSEE OGOR-A, equivalents elsewhere) and federal royalty reports (ONRR for federal leases). State-production-reporting workflow connects: forward-ref to [State Production Reporting](state-production-reporting.md) (Sub-issue 2, not yet authored).

## Forward references

This page is the router; the following pages develop subtopics in more depth:

- [Well Test and Reconciliation](well-test-and-reconciliation.md) — periodic well-test workflow, three-phase separator test, multiphase flow meter test, reconciliation residual, allocation-factor recalibration mechanics.
- [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md) — gas-oil ratio measurement, water-cut measurement (microwave, capacitance, Coriolis), phase-envelope implications, reservoir-management feedback.
- [Custody-Transfer Overview](custody-transfer-overview.md) — custody-transfer measurement framework, API MPMS series introduction, LACT unit, metering-skid architecture, uncertainty budget.
- [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md) — measurement uncertainty propagation, GUM framework (Type A statistical + Type B systematic), coverage factor, error-budget tree.

Phase 5 sister sub-issue forward-refs (pages not yet authored):

- [State Production Reporting](state-production-reporting.md) — regulator forms and submission cadence by jurisdiction (Sub-issue 2).
- [Chemical Disclosure (FracFocus)](chemical-disclosure-fracfocus.md) — stimulation-chemical disclosure framework (Sub-issue 2).
- [Production SCADA Architecture](production-scada-architecture.md) — SCADA-to-data-historian-to-business-systems data path (Sub-issue 3).
- [Production Data Historian Patterns](production-data-historian-patterns.md) — time-series-database patterns for production data (Sub-issue 3).

## Standards anchors

- [API MPMS Chapter 20](../standards/api-mpms-ch-20.md) — Allocation Measurement; the publisher-canonical framework for allocation-by-difference and allocation-by-proportion methods, and for uncertainty allocation across the measurement chain.
- [API MPMS Chapters 4, 5, 6](../concepts/custody-transfer-overview.md) — dynamic flow measurement, proving, metering assemblies (covered via the custody-transfer overview page; structural reference only).
- ISO/IEC Guide 98-3 (GUM) — Guide to the Expression of Uncertainty in Measurement; public uncertainty-framework reference consumed by [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).

## Cross-references

- [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody-Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md)
- [Production History Decline Analysis](production-history-decline-analysis.md) — allocated per-well volume series is the primary input
- [Selective Production](selective-production.md), [Intelligent-Well Completions](intelligent-well-completions.md) — per-zone allocation context
- [Gas Lift Overview](gas-lift-overview.md), [Electric Submersible Pumps](electric-submersible-pumps.md), [Plunger Lift](plunger-lift.md) — artificial-lift / allocation interactions
- [Flow Assurance](flow-assurance.md) — line-pack and evaporation residual interactions
- [Choke Management](choke-management.md) — operating-point changes trigger allocation-factor recalibration

## Public references

- **API MPMS Chapter 20** — Manual of Petroleum Measurement Standards, Chapter 20 (Allocation Measurement). American Petroleum Institute. The publisher-canonical framework. See standards page for edition status.
- **Smith Jr., M.** — *Practical Industrial Flow Measurement*, Wiley 2007 (ISBN 978-0-470-04162-7). Practitioner reference for the measurement-side context within which allocation arithmetic operates.
- **Miller, R. W.** — *Flow Measurement Engineering Handbook*, 3rd edition, McGraw-Hill 1996 (ISBN 978-0-07-042366-4). Comprehensive metering reference; covers the meter-side uncertainty that bounds allocation accuracy.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover allocation, well-test reconciliation, and custody-transfer interactions.
- **SPE OnePetro allocation literature** — practitioner-level corpus on well-test design for allocation, multiphase-meter allocation duty, virtual-metering for allocation, and partner-allocation contractual frameworks.
- **Energy Institute (UK) HM Series** — the UK metering-standards counterpart to API MPMS; in some North-Sea operations the HM series is cited alongside API MPMS for allocation methodology.
