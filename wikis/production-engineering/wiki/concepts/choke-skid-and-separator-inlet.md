---
title: "Choke Skid and Separator Inlet"
tags: [choke-skid, surface-choke, separator-inlet, slug-catcher, gas-knockout, production-choke, test-choke, surface-handover-boundary]
added: 2026-05-16
last_updated: 2026-05-16
---

# Choke Skid and Separator Inlet

## Scope

The choke skid is the integrated surface-piping assembly that carries the production choke (continuous-duty rate-control element) and the test choke (well-test routing element), along with the manifolds, actuators, instrumentation, and ESD interlocks that operationalise them. The separator inlet is the downstream-terminating event of the [Surface Handover Boundary](surface-handover-boundary.md) envelope — the line pressure, slug-flow conditioning, and gas-knockout staging at the separator inlet are the last in-scope elements before the surface-facility-engineering envelope (separator vessel design and downstream processing) takes over.

This page is the **hardware-and-installation companion** to the Phase 4 [Choke Management](choke-management.md) cluster. Where choke-management framed the choke as a hydraulic operating-point control device in well-deliverability terms (IPR/TPR/facility intersection), this page frames the choke as a piece of as-installed surface hardware living on a skid that carries it through fabrication, hydrostatic test, function test, operation, maintenance, and end-of-life replacement. Multiphase-flow physics is in [Multiphase Choke Modeling](multiphase-choke-modeling.md); sand-erosion physics is in [Choke Sand Erosion](choke-sand-erosion.md); the rate-ceiling envelope is in [Erosional Velocity](erosional-velocity.md).

## Choke skid as an assembled hardware envelope

A surface choke skid is not a single piece of equipment — it is an assembled piping skid carrying multiple chokes plus their support infrastructure:

### Production choke

- **Architectural family** — fixed-bore, adjustable, cage, or multistage per [Choke Types](choke-types.md). Adjustable chokes dominate modern surface installations; cage and multistage chokes appear in severe-service envelopes
- **Actuator** — manual hand-wheel (legacy), pneumatic (common), hydraulic (high-rate surface and subsea), electric (increasingly common); covered at the actuation-family level in [Choke Management](choke-management.md)
- **Trim metallurgy** — tungsten-carbide, ceramic, or stellite-class hardfacing per service-and-erosion requirements; the trim-material decision interacts with [Choke Sand Erosion](choke-sand-erosion.md)
- **Position feedback** — choke-position transducer for SCADA telemetry; load-bearing for the rate-control loop and for the bean-up audit trail

### Test choke

- **Function** — paired with the test-manifold routing per [Manifold Tie-In](manifold-tie-in.md); accommodates the well-test envelope which may differ from the steady-state production envelope (different rate, different drawdown target)
- **Architectural choice** — often a smaller-trim version of the production choke architecture, since well-tests typically constrain the well below its steady-state rate to fit the test-separator capacity

### Choke-skid manifold

- **Switching valves** — block-and-bleed isolation valves around each choke for in-service replacement; 3-way valves or paired valves for production / test routing
- **Header** — common discharge header downstream of the choke(s) routing to the separator inlet
- **Pressure-relief valves (PRV)** — overpressure protection per ASME Section VIII and the API RP 14C SAFE-chart logic

### Instrumentation

- **Upstream pressure / temperature** — flowing tubing-head pressure and temperature, capturing the choke-inlet condition
- **Downstream pressure / temperature** — choke-discharge line pressure (PSHL setpoint anchor per [API RP 14C](../standards/api-rp-14c.md)) and discharge temperature (Joule-Thomson cooling indicator)
- **Sand detection** — acoustic-sand-detector (ASD) or erosion-probe instrumentation downstream of the choke; trends sand-carryover for choke-trim-erosion management per [Choke Sand Erosion](choke-sand-erosion.md)
- **Position feedback** — choke-stem position transducer (for adjustable chokes)
- **Differential-pressure transmitter** — across-choke dP for choke-CV verification and for cross-checking against the multiphase choke model per [Multiphase Choke Modeling](multiphase-choke-modeling.md)

### Pressure-containing envelope and structural mount

- **Body pressure rating** — per API Spec 6A class designation (5K, 10K, 15K psi most common; 20K psi for HPHT)
- **NACE MR0175 / ISO 15156 qualification** — sour-service envelopes require qualified metallurgy across the body, trim, and seal surfaces
- **Structural skid mounting** — base frame with lift points, supports, and interface to the facility piping; for offshore, includes deck-tie-in details and motion / dynamic-load considerations

## Pre-commissioning and function test

The choke skid is pre-commissioned through the [Manifold Tie-In](manifold-tie-in.md)-side pre-commissioning sequence plus choke-specific function tests:

- **Hydrostatic pressure test** — full pressure test of the skid pipework
- **Choke-stroke function test** — actuator drives the choke through full open / full close strokes with position-feedback verification
- **ESD function test** — choke-bias-to-close on facility ESD signal verified per [API RP 14C](../standards/api-rp-14c.md) SAFE-chart entry; PSHL setpoint and trip-action verified
- **Sand-detector calibration** — ASD or erosion-probe instrumentation calibrated against the as-installed background
- **SCADA tag commissioning** — all choke-skid tags wired to the SCADA host per [Production SCADA Architecture](production-scada-architecture.md) and registered in the historian per [Production Data Historian Patterns](production-data-historian-patterns.md)

The function-test record is retained per the [API RP 14C](../standards/api-rp-14c.md) test-interval methodology and becomes part of the operating-life audit trail.

## Separator inlet conditions

The choke-skid discharge header terminates at the separator inlet. The separator-inlet condition is the in-scope-terminating event for this wiki; everything inside the separator vessel and downstream is reserved for the hypothetical future surface-facility-engineering wiki per [Surface Handover Boundary](surface-handover-boundary.md). The separator-inlet conditions that the choke-skid design must respect:

### Line pressure

- **Operating-pressure setpoint** — the separator operates at a fixed (or narrowly-banded) inlet pressure set by the downstream-process requirements (gas-treating dew-point control, oil-treating heat-input matching, water-handling capacity). The choke holds the wellhead at the pressure that gives this separator-inlet pressure for the well's rate
- **Operating envelope** — the separator-inlet pressure is the **constant-pressure boundary condition** for the choke; the choke acts to hold this boundary fixed as upstream conditions vary
- **Overpressure protection** — the separator vessel has its own pressure-relief valve sized per ASME Section VIII and the API RP 521 framework (downstream of separator inlet — surface-facility-engineering scope); but the choke-discharge PSHL trips per [API RP 14C](../standards/api-rp-14c.md) before the separator-PRV lifts in normal operation

### Slug-flow conditioning

Multiphase flow arriving at the separator inlet is rarely steady-state. Slug-flow conditioning is the in-scope discipline of structuring the separator-inlet piping to avoid imposing un-manageable slug events on the separator:

- **Slug-catcher** — a dedicated piping segment upstream of the separator that breaks slug-flow into smaller, more separator-tolerable transients. Two architectural classes: **harp-type slug-catchers** (multiple parallel pipes that distribute the slug across pipes) and **vessel-type slug-catchers** (a horizontal vessel that buffers the slug; structurally similar to a separator). Slug-catcher sizing is dominantly future-surface-facility-engineering scope; the production-engineering side is the operational use of the slug-catcher to manage flow-assurance-driven slug events
- **Inlet piping geometry** — straight-run requirements upstream of the separator inlet allow flow to partially stratify before separator entry, improving separation efficiency
- **Slug-flow detection** — slug-detection instrumentation (acoustic, gamma-densitometer, capacitance) at the choke-discharge header or at the separator inlet feeds the SCADA system; severe-slug events can trigger automated production-rate reduction via choke bias-down
- **Coupling with multiphase flow** — slug-flow regimes are characterised in [Flow Regime Maps](flow-regime-maps.md); slug-growth on long flowlines and risers is the dominant flow-assurance concern in subsea developments per [Flow Assurance](flow-assurance.md) (subsea-side of the cross-domain)

### Gas-knockout staging

- **Pre-separator gas-liquid distribution** — for high-gas-fraction streams, the inlet piping is designed to begin gas-liquid distribution before entry to the separator. This is partial separation conditioning, not full separation (which is the separator's job)
- **Inlet device** — the separator has an internal inlet device (vane, cyclone, half-pipe) that completes the gas-liquid disengagement; the inlet-device design is surface-facility-engineering scope, but the choke-skid output must be compatible with the inlet-device class chosen
- **Operating-envelope coupling** — choke-bean operating point sets the gas-liquid velocity ratio at the separator inlet; severe operating-point excursions (e.g. rapid bean-up after extended shut-in) can overwhelm the inlet device and reduce separation efficiency until equilibrium is re-established

## Choke-discharge erosional-velocity envelope

The choke-discharge piping is the canonical erosional-velocity-sized component in the [Erosional Velocity](erosional-velocity.md) framework. The choke-bean operating point sets the in-situ velocity in the choke-discharge line; the line must be sized so that the resulting velocity stays below the API RP 14E V_e ceiling (or the alternative-criterion ceiling chosen by the operator). Sand-laden service tightens the envelope materially; see [Choke Sand Erosion](choke-sand-erosion.md) for the sand-rate-aware framework.

## SCADA and historian integration

All choke-skid instrumentation feeds the production SCADA system per [Production SCADA Architecture](production-scada-architecture.md):

- **Choke position** — bean opening setpoint and feedback; supports operating-point optimisation, bean-up audit trail, and integrity-management (cumulative bean-up cycles)
- **Upstream / downstream pressure and temperature** — feeds the multiphase choke model (per [Multiphase Choke Modeling](multiphase-choke-modeling.md)) cross-check and the well-deliverability inference
- **Sand detection** — feeds the choke-trim erosion-rate management framework
- **ESD interlock state** — feeds the SAFE-chart audit trail per [API RP 14C](../standards/api-rp-14c.md)

The historian captures the choke-skid record at a sufficient sampling rate to support transient-event analysis (slug arrival, ESD slam-closure, bean-up step transitions); high-frequency capture for transient events with deadband-compressed capture for steady-state operation is the typical pattern per [Production Data Historian Patterns](production-data-historian-patterns.md).

## Maintenance and trim replacement

- **In-service trim erosion** — choke trim erosion is the dominant choke-skid maintenance driver; trim-replacement frequency is set by sand-rate, trim metallurgy, and rate per [Choke Sand Erosion](choke-sand-erosion.md). Surface-tree access makes trim-replacement a routine operation (lifting the choke insert through the bonnet); subsea access via intervention vessel makes subsea-choke-trim replacement a major event
- **Block-and-bleed for replacement** — the choke-skid manifold's block-and-bleed valves around each choke allow individual choke isolation for trim replacement without facility shutdown; the skid pattern is structured to support this
- **Spare parts inventory** — operators maintain trim-spare inventory matched to the expected service-life across the fleet; offshore facilities carry on-platform spare inventories for fast turnaround
- **Replacement-cycle SCADA capture** — each trim-replacement event registered in the historian per [Production Data Historian Patterns](production-data-historian-patterns.md) and the integrity-management record per [Integrity Monitoring](integrity-monitoring.md)

## Cross-domain interactions

- **Choke management** — operational framing of the choke as the rate-control surface across IPR/TPR/facility constraints. See [Choke Management](choke-management.md).
- **Choke types** — architectural family choice; trim materials and surface-vs-subsea envelope. See [Choke Types](choke-types.md).
- **Multiphase choke modeling** — Sachdeva / Perkins / Ashford-Pierce framework for the choke as a hydraulic operating-point element. See [Multiphase Choke Modeling](multiphase-choke-modeling.md).
- **Choke sand erosion** — sand-rate-aware trim-erosion management. See [Choke Sand Erosion](choke-sand-erosion.md).
- **Erosional velocity** — choke-discharge piping sizing per V_e criterion. See [Erosional Velocity](erosional-velocity.md).
- **Manifold tie-in** — the choke-skid sits between the manifold and the separator-inlet. See [Manifold Tie-In](manifold-tie-in.md).
- **API RP 14C** — ESD interlock coordination; PSHL setpoints; choke-bias-to-close on ESD. See [API RP 14C](../standards/api-rp-14c.md).
- **Well integrity during production** — choke-skid trim erosion and corrosion are operating-time integrity threats. See [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Corrosion Management](corrosion-management.md).
- **Flow assurance** — slug-flow conditioning is a flow-assurance-coupled discipline; hydrate formation in the choke discharge is a textbook flow-assurance failure mode. See [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md), [Flow Regime Maps](flow-regime-maps.md).
- **Production accounting** — choke-skid data feeds well-test reconciliation and allocation. See [Well Test and Reconciliation](well-test-and-reconciliation.md), [Production Allocation](production-allocation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md).
- **Regulatory reporting** — choke-discharge volumes feed regulatory reporting. See [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Production Allowable Rates](production-allowable-rates.md), [Gas Flaring Rules](gas-flaring-rules.md).
- **Production SCADA architecture** — choke-skid SCADA integration. See [Production SCADA Architecture](production-scada-architecture.md), [Production Data Historian Patterns](production-data-historian-patterns.md).

## Cross-references

- [Surface Handover Boundary](surface-handover-boundary.md), [Manifold Tie-In](manifold-tie-in.md), [Production SCADA Architecture](production-scada-architecture.md), [Production Data Historian Patterns](production-data-historian-patterns.md)
- [Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md), [Erosional Velocity](erosional-velocity.md)
- [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md), [Flow Regime Maps](flow-regime-maps.md)
- [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Corrosion Management](corrosion-management.md), [Intervention Triggers](intervention-triggers.md)
- [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md)
- [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Production Allowable Rates](production-allowable-rates.md), [Gas Flaring Rules](gas-flaring-rules.md)
- [Multi-Zone Completions](multi-zone-completions.md) — multi-zone surface-tie-in adjacency
- [API RP 14C](../standards/api-rp-14c.md), [API Spec 14A](../standards/api-spec-14a.md), [ISA-95](../standards/isa-95.md)

## Standards anchors

- **API Spec 6A** — Wellhead and Christmas Tree Equipment (body-pressure-class designations)
- **API Spec 12J** — Specification for Oil and Gas Separators (downstream-boundary standard; separator vessel design is reserved for future surface-facility-engineering wiki)
- **API RP 14C** — see [API RP 14C](../standards/api-rp-14c.md) — SAFE-chart methodology covering choke ESD interlocks
- **API RP 14E** — Design and Installation of Offshore Production Platform Piping Systems (erosional-velocity criterion; cross-link to engineering-standards)
- **ASME B31.3** — Process Piping (pressure-design code for skid piping)
- **ASME Section VIII** — Pressure Vessels (referenced for the separator vessel downstream of in-scope, but the boundary discipline matters)
- **NACE MR0175 / ISO 15156** — sour-service material qualification for choke body, trim, and seal metallurgy

## Public references

- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. Choke-skid and separator-inlet design chapters.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Surface-production chapters cover choke-skid hardware and separator-inlet conditioning.
- **Brill, J. P. & Mukherjee, H.** — *Multiphase Flow in Wells*, SPE Monograph Series Vol. 17, Society of Petroleum Engineers, 1999. Multiphase-flow context for choke and slug-flow at separator inlet.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, 2nd ed., Elsevier (ISBN 978-0-12-812622-5). Subsea choke and slug-catcher coverage from the subsea-side perspective.
- **Beggs, H. D.** — *Production Optimization Using Nodal Analysis*, 2nd ed., OGCI Publications, 2003 (ISBN 0-930972-14-7). Nodal-analysis framework for choke operating-point selection.
- **GPSA — Gas Processors Suppliers Association** — *Engineering Data Book* (multiple editions). Separator inlet conditioning and slug-catcher chapters; primarily future-surface-facility-engineering wiki territory.
- **SPE OnePetro choke-skid and slug-catcher literature** — practitioner corpus on choke-skid retrofits, brownfield choke replacements, slug-management strategies, and sand-aware choke operating practice.
