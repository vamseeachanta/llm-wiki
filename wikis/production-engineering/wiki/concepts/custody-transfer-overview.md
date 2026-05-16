---
title: "Custody Transfer Overview"
tags: [custody-transfer, lact-unit, fiscal-metering, api-mpms, metering-skid, proving, uncertainty-budget, allocation-anchor, royalty-measurement]
added: 2026-05-16
last_updated: 2026-05-16
---

# Custody Transfer Overview

## Scope

Custody transfer is the metering event at which legal and financial ownership of produced hydrocarbon (and increasingly, produced water, where it has commercial value) passes from one party to another. The custody-transfer meter is the **fiscal-grade** measurement event in a producing field — it is the meter that royalty payments, partner allocations, severance tax, and pipeline-tariff payments are computed against. Per-well allocation arithmetic (see [Production Allocation](production-allocation.md)) closes against custody-transfer meter readings as its measurement anchor.

This page introduces the custody-transfer measurement framework, walks the API MPMS chapter map at structural level, covers the LACT (Lease Automatic Custody Transfer) unit as the dominant onshore architecture and the metering-skid as the offshore counterpart, and frames the uncertainty budget that governs fiscal-grade measurement design and operation.

## Why custody-transfer measurement is structurally distinct

Custody-transfer measurement carries operational requirements that operational and allocation measurement do not:

- **Bilateral acceptance** — the meter result is binding on both parties (seller and buyer; or operator and partner; or operator and regulator). Both parties have right of inspection, calibration witness, and dispute resolution. The meter is operated under a documented procedure that both parties agree.
- **Traceable calibration** — the meter must be calibrated against a reference standard whose calibration is traceable to a national or international primary standard (NIST in the US, NPL in the UK, equivalents elsewhere). The chain of traceability is documented.
- **Periodic proving** — for liquid meters, the meter is periodically "proved" against a master meter or prover (typically a small-volume prover, a pipe prover, or a master meter) at the operating point. Proving frequency is contractual and is typically monthly for high-throughput meters, quarterly to annual for smaller meters.
- **Composition and density measurement** — gas custody-transfer requires continuous composition input (online chromatograph) for energy-content computation. Liquid custody-transfer requires density measurement (online densitometer, or sampling-based density determination per API MPMS Chapter 9) for mass-equivalent computation where required.
- **Sampling for chemistry** — automated sampling per API MPMS Chapter 8 captures composite samples across the custody-transfer batch for retrospective analysis of BS&W, salt content, and quality.
- **Uncertainty target** — the bilateral contract typically specifies an uncertainty target (commonly ±0.25% for liquid hydrocarbons, ±0.5-1.0% for gas, with tighter targets for some specific applications). The meter design, proving frequency, and procedure are sized to achieve the contract target.

The result is that custody-transfer meters are typically a different class of equipment (often more expensive, always more procedurally constrained) than the same-technology meter operated for operational or allocation duty.

## API MPMS — Manual of Petroleum Measurement Standards

The API Manual of Petroleum Measurement Standards (MPMS) is the practitioner-canonical multi-volume framework for fiscal-grade petroleum measurement. The MPMS is organised into chapters by topic area; the chapter map below covers the chapters most relevant to custody-transfer in production operations. The MPMS chapters are paywalled — paraphrased structurally here per the workspace paraphrase discipline; consult the publisher (api.org) for the current edition of each chapter.

| Chapter | Topic | Relevance to custody transfer |
|---|---|---|
| **Ch. 1** | Vocabulary | Definitions used across all chapters |
| **Ch. 2** | Tank Calibration | Calibration of storage tanks used in custody transfer (tank-gauging custody, increasingly displaced by inline metering) |
| **Ch. 3** | Tank Gauging | Tank-level measurement methodology |
| **Ch. 4** | Proving Systems | Meter-proving methodology (small-volume prover, pipe prover, master-meter prover) — the core of liquid custody-transfer integrity |
| **Ch. 5** | Metering | Liquid metering technology (positive displacement, turbine, Coriolis, ultrasonic) |
| **Ch. 6** | Metering Assemblies | The integrated metering-assembly design (pipe, valves, prover connection, sampling, density, temperature, pressure instrumentation) — LACT-unit and metering-skid architecture |
| **Ch. 7** | Temperature Determination | Temperature measurement for volume-correction |
| **Ch. 8** | Sampling | Automated sampling methodology — composite-sample capture for retrospective chemistry analysis |
| **Ch. 9** | Density Determination | Density measurement (laboratory hydrometer, online densitometer) |
| **Ch. 10** | Sediment and Water | BS&W measurement methodology |
| **Ch. 11** | Physical Properties Data | Volume correction factor tables; the CTL/CPL framework |
| **Ch. 12** | Calculation of Petroleum Quantities | Combined-quantity calculation procedures |
| **Ch. 13** | Statistical Aspects of Measurement and Sampling | Statistical-design framework for meter performance |
| **Ch. 14** | Natural Gas Fluids Measurement | Gas-stream measurement (orifice methodology per AGA Report 3, ultrasonic methodology per AGA 9, Coriolis methodology per AGA 11) |
| **Ch. 17** | Marine Measurement | Tanker-loading custody transfer (largely outside scope for upstream production) |
| **Ch. 19** | Evaporative Loss Measurement | Vapor-loss accounting |
| **Ch. 20** | Allocation Measurement | The framework that bridges custody-transfer measurement to per-well allocation arithmetic (see [API MPMS Chapter 20](../standards/api-mpms-ch-20.md), [Production Allocation](production-allocation.md)) |
| **Ch. 21** | Flow Measurement Using Electronic Metering Systems | Electronic flow-computer methodology — the EFM-based modern custody-transfer station |

The chapter map covers the **dominant** chapters; the MPMS contains additional chapters and sub-chapters. Operators specifying custody-transfer designs and procedures pin to specific chapter revisions in the contract.

## LACT unit — Lease Automatic Custody Transfer

The LACT unit is the dominant **onshore** custody-transfer architecture for crude oil. It is a pre-engineered metering and sampling skid that sits at the lease boundary (or at the pipeline tie-in for pipeline-sales custody) and that automatically meters, samples, and quality-checks the produced crude as it leaves the lease tankage:

- **Strainer** — removes solids upstream of metering
- **Air-eliminator** — removes entrained gas upstream of metering (degassing prior to the meter; gas-in-oil biases volume measurement)
- **BS&W monitor** — continuous water-cut measurement (capacitance, microwave, or density-based per [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md)) with a diversion valve that routes off-spec crude back to tankage when BS&W exceeds the contract limit
- **Sampler** — automated composite-sampler per API MPMS Chapter 8 capturing a representative sample across the custody-transfer batch
- **Meter** — typically a positive-displacement or Coriolis meter; positive-displacement (rotating-element) is the legacy LACT meter, Coriolis is increasingly dominant in new installations for its direct mass measurement and reduced proving sensitivity
- **Prover connection** — for periodic meter proving per API MPMS Chapter 4
- **Temperature, pressure, density instrumentation** — for volume-correction per API MPMS Chapter 11 (CTL/CPL framework)
- **Flow computer / EFM** — accumulates corrected volume, drives the diversion valve on BS&W exceedance, generates ticket reports per API MPMS Chapter 21
- **Backpressure valve / metering control valve** — maintains stable upstream pressure on the meter for measurement stability

LACT units are widely deployed onshore where lease-level fiscal measurement is required and the throughput justifies dedicated metering equipment. Smaller leases sometimes use truck-loading-at-tank custody transfer (truck-meter at the loading rack) with the same MPMS framework but without a dedicated LACT skid.

## Metering skid — offshore and pipeline-grade custody

Offshore production facilities and pipeline-tariff-grade onshore installations typically deploy a more elaborate **metering skid** that runs multiple meters in parallel (for redundancy and for proving), often with separate streams for oil-and-condensate vs water-and-emulsion, and that integrates with the facility ICSS (integrated control and safety system) for production-accounting handover:

- **Multi-run metering** — typically 2-to-4 parallel meter runs, one running as the duty meter while one is held as standby; meter-rotation policy moves the duty role across runs on a defined cadence
- **In-line prover** — a small-volume prover sits permanently in the skid for periodic in-situ proving, eliminating the need for an external prover truck
- **Ultrasonic or Coriolis primary measurement** — for high-throughput offshore liquid custody transfer, ultrasonic and Coriolis dominate over positive-displacement; for gas, ultrasonic (per AGA Report 9) and Coriolis (per AGA 11) increasingly dominate over orifice (per AGA Report 3) in new installations
- **Online densitometer + chromatograph** — continuous density and composition for high-accuracy mass-and-energy computation
- **Skid-mounted analyzers** — BS&W, salt content, H2S, CO2, and dewpoint analyzers for quality monitoring
- **EFM with full audit trail** — modern electronic flow computer with full timestamped record of every meter run, every proving event, every diversion, every alarm; per API MPMS Chapter 21

### Measurement vendor-citation discipline

Custody-transfer meter and skid-equipment vendors are cited by name and general capability only. Proprietary internals (calibration curves, signal-processing algorithms, accuracy spec sheets) are out of scope.

| Vendor | Allowed citation | Blocked citation |
|---|---|---|
| **Daniel (Emerson)** | "Daniel orifice and ultrasonic gas-meter family — practitioner-default for legacy and many new gas-custody installations" | Orifice-plate accuracy correction tables, ultrasonic transducer calibration curves |
| **Smith Meter (FMC Technologies)** | "Smith Meter positive-displacement and ultrasonic liquid-meter family — long-deployed in LACT-unit installations" | Positive-displacement rotor-clearance specifications, ultrasonic accuracy curves |
| **Krohne** | "Krohne ultrasonic and Coriolis meter family — independent vendor in the custody-transfer market" | Multi-path ultrasonic signal-processing internals, Coriolis tube-design specifications |
| **Sick Maihak / Sick** | "Sick gas-quality analyser and ultrasonic gas-meter family — widely deployed in gas-fiscal applications" | Analyser calibration internals, ultrasonic accuracy-spec transcriptions |
| **Yokogawa** | "Yokogawa flow-computer and analyser family — broad EFM and quality-measurement coverage" | EFM algorithm internals, analyser accuracy transcriptions |
| **Endress+Hauser** | "Endress+Hauser Coriolis and density-meter family — broad-coverage measurement vendor" | Proprietary density-temperature correction internals |

Vendor mentions are at "named at name + general capability" level only. The vendor-citation pattern matches Phase 4 production-engineering precedent in [Choke Sand Erosion](choke-sand-erosion.md) and [Well Integrity During Production](well-integrity-during-production.md).

## Uncertainty budget

The uncertainty budget for a custody-transfer meter is the sum (per uncertainty-propagation methodology — see [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md)) of contributions across the measurement chain:

- **Primary meter uncertainty** — the meter's intrinsic measurement uncertainty at the operating point (a function of meter technology, condition, and proving history)
- **Proving uncertainty** — the uncertainty of the prover and the proving procedure
- **Temperature measurement uncertainty** — propagated through the CTL (correction for temperature) factor per API MPMS Chapter 11
- **Pressure measurement uncertainty** — propagated through the CPL (correction for pressure) factor for compressible streams
- **Density measurement uncertainty** — propagated through volume-to-mass conversion where required
- **Composition measurement uncertainty** — propagated through energy-content computation for gas streams
- **Sampling uncertainty** — propagated through quality-correction (BS&W, salt content) calculations
- **Flow computer / EFM uncertainty** — typically small but not zero (round-off, integration interval, time-stamp accuracy)

The bilateral contract uncertainty target (commonly ±0.25% for liquid hydrocarbons, ±0.5-1.0% for gas) bounds the combined-uncertainty across this chain. Periodic proving demonstrates that the meter remains inside the target; out-of-tolerance proving results trigger meter recalibration, repair, or replacement.

## Cross-domain interactions

- **Production allocation** — custody-transfer meter is the closure reference for per-well allocation. Allocation uncertainty cannot be smaller than custody-transfer-meter uncertainty. See [Production Allocation](production-allocation.md).
- **Well-test reconciliation** — closure residual is the gap between the sum of well-test-derived theoretical contributions and the custody-transfer measured volume. See [Well Test and Reconciliation](well-test-and-reconciliation.md).
- **GOR and water-cut tracking** — BS&W is the custody-transfer-grade water-cut measurement; the custody-transfer meter's water-cut monitor is the QA gate on lease oil quality. See [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md).
- **Flow-measurement uncertainty** — custody-transfer uncertainty budget is the canonical worked example of GUM uncertainty propagation in production operations. See [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).
- **Flow assurance** — fluid-quality measurements at custody transfer (BS&W, salt, vapour pressure) reflect upstream flow-assurance performance. See [Flow Assurance](flow-assurance.md).
- **Choke management** — facility-export pressure (which the custody-transfer meter operates against) is set by downstream-pipeline pressure, which sets the operating envelope choke management has to respect. See [Choke Management](choke-management.md).

## Standards anchors

- [API MPMS Chapter 20](../standards/api-mpms-ch-20.md) — Allocation Measurement (the bridge from custody-transfer to per-well allocation)
- API MPMS Chapter 4 — Proving Systems
- API MPMS Chapter 5 — Metering (liquid)
- API MPMS Chapter 6 — Metering Assemblies (LACT and metering-skid architecture)
- API MPMS Chapter 8 — Sampling
- API MPMS Chapter 11 — Physical Properties Data (volume-correction factors)
- API MPMS Chapter 14 — Natural Gas Fluids Measurement (referenced for gas custody)
- API MPMS Chapter 21 — Electronic Metering Systems
- AGA Report 3 / Report 7 / Report 9 / Report 11 — natural-gas-measurement methodology, widely cited alongside MPMS Chapter 14 for gas custody
- ISO 5167 — Measurement of fluid flow by means of pressure differential devices (international counterpart to orifice methodology)
- ISO/IEC Guide 98-3 (GUM) — Guide to the Expression of Uncertainty in Measurement (consumed by [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md))

## Cross-references

- [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md)
- [API MPMS Chapter 20](../standards/api-mpms-ch-20.md) — allocation-measurement standards anchor
- [Choke Management](choke-management.md) — export-pressure context
- [Flow Assurance](flow-assurance.md) — fluid-quality context

## Public references

- **API MPMS** — Manual of Petroleum Measurement Standards, multiple chapters per the chapter map above (American Petroleum Institute, api.org).
- **AGA** — American Gas Association measurement reports (AGA Report 3 — Orifice Metering; AGA Report 7 — Turbine Metering; AGA Report 9 — Ultrasonic Metering; AGA Report 11 — Coriolis Metering for Natural Gas). The gas-measurement standards corpus widely cited alongside MPMS Chapter 14.
- **Smith Jr., M.** — *Practical Industrial Flow Measurement*, Wiley 2007 (ISBN 978-0-470-04162-7). Practitioner reference covering the metering technology families used in custody-transfer applications.
- **Miller, R. W.** — *Flow Measurement Engineering Handbook*, 3rd edition, McGraw-Hill 1996 (ISBN 978-0-07-042366-4). Comprehensive metering reference.
- **Spitzer, D. W. (ed.)** — *Industrial Flow Measurement*, 3rd edition, ISA 2005 (ISBN 978-1-55617-877-2). Industrial-grade metering reference covering proving, calibration, and custody-transfer practice.
- **Energy Institute (UK) HM Series** — UK metering-standards counterpart to API MPMS, used in North-Sea custody operations.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Production-operations chapters cover custody-transfer architecture.
- **SPE OnePetro custody-transfer literature** — practitioner corpus on LACT unit design, metering-skid retrofits, and ultrasonic-meter adoption.
- **NIST and NPL** — calibration-traceability references (US National Institute of Standards and Technology; UK National Physical Laboratory) for the primary-standards chain that custody-transfer calibration anchors to.
