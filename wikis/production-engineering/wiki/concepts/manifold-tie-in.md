---
title: "Manifold Tie-In"
tags: [production-manifold, test-manifold, tie-in, hot-tap, cold-tap, hydrostatic-test, pre-commissioning, gathering-manifold, subsea-manifold]
added: 2026-05-16
last_updated: 2026-05-16
---

# Manifold Tie-In

## Scope

The production manifold is the surface-piping junction at which fluid from multiple producing wells is gathered onto common production or test routes that feed the downstream separator-and-processing chain. The **tie-in** is the engineering and operational act of connecting a new (or returned) well into the manifold without disrupting (or with controlled disruption of) the production of other wells already routed through it.

This page covers manifold topology, tie-in specifications (hot-tap vs cold-tap, hydrostatic testing, pre-commissioning), the pressure-temperature-flow envelope the manifold must accommodate, and the multi-well manifold architecture differences between surface and subsea installations. It sits inside the [Surface Handover Boundary](surface-handover-boundary.md) envelope between the wellhead and the choke skid.

## Manifold topology

Production manifolds split into two functional types that often coexist in the same physical assembly:

### Production manifold (gathering manifold)

The production manifold gathers continuous-production flow from multiple wells onto a small number of (typically one or two) common production headers that route to the downstream choke skid and separator inlet. Architectural axes:

- **Number of inlet wells** — small surface manifolds may gather 2-6 wells; large platform manifolds may gather 20-40 wells; subsea drill-centre manifolds typically gather 4-12 wells per manifold module
- **Number of output headers** — single-header (all wells route to one production train) vs dual-header (low-pressure and high-pressure trains, allowing wells to be routed by tubing-head pressure regime)
- **Per-well isolation** — each inlet has a block valve (or two-block-and-bleed for fiscal-grade isolation) to allow individual well shut-in for workover, integrity-monitoring intervention, or facility maintenance
- **Per-well choke placement** — some architectures place a wellhead choke at each well and a header-level commingling point at the manifold; others place a unified choke skid downstream of the manifold and use the manifold for flow-routing only. The choice interacts with multiphase choke modelling and with the [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md) architecture decision

### Test manifold

The test manifold is the routing infrastructure that diverts a single well at a time onto a dedicated test separator (or onto a multiphase flow meter) for periodic well-test measurement. The well-test data is then folded back into the production-allocation arithmetic (see [Well Test and Reconciliation](well-test-and-reconciliation.md) and [Production Allocation](production-allocation.md)). Architectural elements:

- **Test header** — a common test-route header parallel to the production header(s); each well's inlet block has a 3-way valve or paired valves to switch routing
- **Test separator (or MPFM)** — a dedicated separator with its own gas / oil / water meters per [Custody Transfer Overview](custody-transfer-overview.md) measurement principles (but typically at lower accuracy than fiscal custody transfer), or a multiphase flow meter (MPFM) that meters per-phase without separation
- **Test scheduling** — each well rotated through the test manifold at a defined cadence (monthly is typical for stable wells; more frequent for wells with high allocation uncertainty or known-volatile production)

The same physical manifold assembly typically carries both production and test functions, with valve-switching infrastructure for routing.

## Tie-in specifications

A tie-in is the act of physically connecting a new piping branch (new well, returned-from-workover well, new sales-pipeline tap, new chemical-injection point) into an existing pressure-containing manifold. The two dominant tie-in modes:

### Cold-tap tie-in

The manifold is depressurised and isolated, the existing piping is cut or unbolted, and the new branch is welded or bolted in. The tie-in is then hydrostatic-tested and re-commissioned alongside the manifold.

- **Operational impact** — full manifold shutdown (and therefore production deferral on every well routed through it) for the duration of the tie-in plus the pre-commissioning sequence
- **When chosen** — when the tie-in is large (new header, new train), when other manifold maintenance is also planned (combining outages), or when hot-tap is not feasible (incompatible service envelope, regulatory restriction)
- **Hydrostatic test** — full pressure test of the manifold including the new branch after the tie-in; documented per ASME B31.3 or equivalent piping code

### Hot-tap tie-in

The new branch is welded onto the live (pressurised, in-service) manifold using a hot-tapping machine that drills a hole through the existing pipe wall after the new branch is sealed against the outside of the wall. The new branch is then valved and brought online without depressurising the manifold.

- **Operational impact** — no production deferral on existing wells routed through the manifold; the tie-in is a parallel activity
- **When chosen** — when the manifold cannot tolerate full shutdown (e.g. high-production facility with severe deferral cost; offshore facility where weather windows for shutdown are limited), when the tie-in is small relative to the existing manifold
- **Hot-tap qualification** — limited by the existing manifold's wall thickness, material (sour-service constraints, weldability), service envelope (temperature, internal corrosivity), and the hot-tapping vendor's qualified-procedure envelope. Sour service (NACE MR0175 / ISO 15156) and HPHT service constrain hot-tap practice tightly
- **Hot-tap procedure discipline** — pre-tap inspection (UT wall-thickness verification, internal-corrosion assessment), welder qualification per ASME IX, structural-fitting design per ASME B31.3, controlled-cooling protocols where heat-affected zone (HAZ) cracking is a sour-service risk

### Hydrostatic test and pre-commissioning

Both cold-tap and hot-tap tie-ins terminate in a pre-commissioning sequence that establishes the new tie-in's fitness-for-service:

- **Hydrostatic pressure test** — typically at 1.5x design pressure (per ASME B31.3 for piping; some service envelopes mandate higher) held for a defined duration with documented pressure-decay tolerance
- **Pressure-test medium** — water for most service (with appropriate corrosion-inhibitor dosing in sour or chloride-sensitive systems); nitrogen for systems where water cannot be tolerated (high-purity gas service, post-test drying constraints)
- **Pre-commissioning purge** — air or nitrogen purge to remove free water from the system before introducing produced fluid; CO2 or hydrocarbon-gas purge in sour service to avoid oxygen ingress
- **Function test** — valve-stroke verification, instrumentation calibration, SCADA-tag commissioning per [Production SCADA Architecture](production-scada-architecture.md), ESD interlock function-test per [API RP 14C](../standards/api-rp-14c.md) SAFE-chart methodology
- **Documented handover** — the tie-in is handed over to the operations team with a complete documentation package (pressure-test record, function-test record, isometric drawings, instrumentation list, ESD-logic verification)

The pre-commissioning sequence is a load-bearing operational discipline: a tie-in that bypasses or shortens the sequence ships with un-verified integrity, and the resulting in-service failures are over-represented in post-incident reviews of manifold-and-tie-in incidents.

## Pressure-temperature-flow envelope

The manifold must accommodate the union of operating envelopes across all wells routed through it:

- **Maximum operating pressure** — the highest flowing wellhead pressure across the well roster, plus the required margin for transient pressure events (slugging, choke-position changes, ESD slam-closure water-hammer). Drives manifold body-pressure rating per API Spec 6A class designations (5K, 10K, 15K, 20K psi)
- **Temperature envelope** — from the coldest operating condition (high-rate gas-condensate wells passing through severe Joule-Thomson cooling at the choke; ambient-air-cooled flowlines in winter operation) to the hottest (HPHT wells with reservoir temperatures over 300 °F at the wellhead; steam-flood injectors returning hot fluid)
- **Flow envelope** — minimum-flow turndown (low-rate stripper wells where multiphase velocity falls below the minimum needed for stable slug-flow regime) to maximum-flow (peak-rate wells, transient post-startup flow). Drives manifold-and-header sizing against the [Erosional Velocity](erosional-velocity.md) ceiling
- **Service envelope** — sweet vs sour (NACE MR0175 / ISO 15156 metallurgy in sour service), clean vs sand-laden (drives manifold-and-header trim against erosion), single-phase vs multiphase

The envelope is **not static across field life**: as wells deplete and as new wells are added, the manifold's accommodation envelope evolves. Manifold revamp (re-piping, re-rating, or replacement) is typically triggered when accumulated envelope-creep crosses the original design rating.

## Multi-well manifold architecture: surface vs subsea

### Surface manifold architecture

Surface manifolds (onshore wellsites, conventional offshore platforms) sit on the topsides accessible to operators and inspectors. Architectural patterns:

- **Open-skid manifolds** — piping mounted on a structural skid with operator-walkable access; the dominant onshore pattern
- **Enclosed-building manifolds** — manifolds inside a heated and ventilated building, common in cold-climate operations (Alaska, Canada, Russia) where freeze protection and operator-access in winter is critical
- **Modular pre-engineered skids** — repeatable manifold designs deployed across multiple wellsites for capital-cost reduction and operational standardisation; common in unconventional-shale operations with high well-count

Surface manifolds are inspectable, maintainable, and tie-in-accessible at modest cost. Hot-tap tie-ins are routine; cold-tap tie-ins coordinate with planned facility outages.

### Subsea manifold architecture

Subsea manifolds (subsea drill-centre architectures in deepwater operations) sit on the seabed and are accessed only via ROV or via intervention vessel. Architectural patterns:

- **Subsea drill-centre manifold (SDCM)** — gathers several subsea-tree producers onto a common subsea flowline that exports to the host facility (FPSO, fixed platform, semi-submersible). Internal piping, valves, and choke skids inside the manifold module
- **Pipeline End Manifold (PLEM)** — endpoint hardware at the host-facility end of the subsea flowline, providing tie-in for surface piping
- **Pipeline End Termination (PLET)** — endpoint hardware at the subsea end of a flowline, providing tie-in to subsea trees or jumpers

Subsea manifold tie-in is dominantly **cold-tap with vessel-and-ROV intervention** — hot-tap on a pressurised subsea manifold is technically possible but operationally rare and reserved for high-value cases. New-well tie-in to an existing subsea manifold is planned as a major operation involving intervention vessel mobilisation, dedicated jumper fabrication, and host-facility-side shutdown coordination.

Subsea manifolds carry their own integrity-monitoring concerns: external corrosion in seawater (cathodic-protection-system design and inspection), internal corrosion in produced-fluid service, hydrate-formation risk in cold-seabed environment, and access difficulty for inspection and intervention. The subsea-side hardware design is dominantly marine-engineering scope (cross-link to marine-engineering subsea hardware coverage); the production-engineering side is the operational use of the manifold for flow routing and well-test scheduling.

## SCADA and historian integration

Manifold instrumentation feeds the production SCADA system per [Production SCADA Architecture](production-scada-architecture.md):

- **Header pressures and temperatures** — production-header and test-header pressure and temperature at the manifold; key inputs to well-deliverability monitoring
- **Per-well isolation-valve position** — block-valve and 3-way-valve position feedback; allows SCADA to verify the as-routed state of the manifold matches the operator-commanded state
- **Per-well choke position** — where wellhead chokes are present, position feedback per [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md) discipline
- **Test-manifold routing state** — which well is currently routed to test; consumed by the well-test scheduler and by allocation arithmetic

The historian captures the manifold-state record alongside the rate-and-pressure record per [Production Data Historian Patterns](production-data-historian-patterns.md), supporting retrospective production-accounting reconstruction and incident-investigation needs.

## Cross-domain interactions

- **Choke management** — manifold tie-in pre-dates the choke skid in the flow path; the choke-skid design assumes a specific manifold-outlet envelope. See [Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md).
- **Well test and reconciliation** — test-manifold routing is the per-well test gating; allocation arithmetic depends on the test-manifold's measurement quality. See [Well Test and Reconciliation](well-test-and-reconciliation.md), [Production Allocation](production-allocation.md).
- **Well integrity during production** — manifold internal corrosion and external corrosion are operating-time integrity threats coupled with the well-side integrity discipline. See [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Corrosion Management](corrosion-management.md).
- **Flow assurance** — manifold geometry interacts with slug-flow management (severe slugging at the manifold inlet of a multi-well gathering header is a known flow-assurance failure mode); hydrate-formation risk inside the manifold during cooldown or restart events; see [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md).
- **Erosional velocity** — manifold-and-header sizing is bounded by [Erosional Velocity](erosional-velocity.md) at the high-rate condition; sand-laden service is especially constraining.
- **Multi-zone completions** — multi-zone surface tie-in interacts with manifold per-zone routing where zones report independently to the manifold (some advanced architectures); see [Multi-Zone Completions](multi-zone-completions.md).
- **Marine-engineering** — subsea manifold hardware design is marine-engineering scope; cross-link to the marine-engineering subsea-hardware coverage.
- **API RP 14C** — manifold valves participate in the facility ESD logic per [API RP 14C](../standards/api-rp-14c.md) SAFE-chart methodology.

## Cross-references

- [Surface Handover Boundary](surface-handover-boundary.md) — router for the wellhead-to-separator-inlet envelope
- [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md) — downstream of the manifold
- [Production SCADA Architecture](production-scada-architecture.md), [Production Data Historian Patterns](production-data-historian-patterns.md) — manifold data flow
- [Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md) — Phase 4 choke cluster
- [Erosional Velocity](erosional-velocity.md) — sizing ceiling
- [Well Integrity During Production](well-integrity-during-production.md), [Integrity Monitoring](integrity-monitoring.md), [Corrosion Management](corrosion-management.md), [Intervention Triggers](intervention-triggers.md) — manifold integrity coupling
- [Flow Assurance](flow-assurance.md), [Hydrate Management](hydrate-management.md) — manifold slug-and-hydrate risk
- [Well Test and Reconciliation](well-test-and-reconciliation.md), [Production Allocation](production-allocation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md) — measurement and accounting coupling
- [Multi-Zone Completions](multi-zone-completions.md) — multi-zone surface tie-in adjacency
- [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Gas Flaring Rules](gas-flaring-rules.md), [Production Allowable Rates](production-allowable-rates.md) — regulatory consumers of manifold data
- [API RP 14C](../standards/api-rp-14c.md) — ESD interlock context for manifold valves

## Standards anchors

- **API Spec 6A** — Wellhead and Christmas Tree Equipment (pressure-class designations used in manifold body rating)
- **API Spec 12J** — Specification for Oil and Gas Separators (boundary standard at separator-inlet)
- **API RP 14E** — Design and Installation of Offshore Production Platform Piping Systems (erosional-velocity criterion; cross-link to engineering-standards)
- **API RP 14C** — see [API RP 14C](../standards/api-rp-14c.md) — manifold-valve ESD coordination
- **ASME B31.3** — Process Piping (pressure-design code most commonly cited for production-piping design and hydrostatic test)
- **ASME IX** — Welding and Brazing Qualifications (welder qualification for tie-in welding)
- **NACE MR0175 / ISO 15156** — sour-service material qualification for manifold metallurgy and tie-in weld procedures
- **API RP 1107** — Pipeline Maintenance Welding Practices (referenced for in-service hot-tap procedures on pipeline-grade systems)

## Public references

- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. Surface-production manifold-and-tie-in chapters.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Surface-production chapters cover manifold topology and tie-in practice.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, 2nd ed., Elsevier (ISBN 978-0-12-812622-5). Subsea manifold, PLEM, PLET coverage; the comprehensive reference for the subsea side of manifold architecture.
- **Bai, Y. & Bai, Q.** — *Subsea Pipelines and Risers*, Elsevier 2005 (ISBN 978-0-08-044566-3). Subsea pipeline tie-in and hot-tap practice.
- **Bahadori, A.** — *Natural Gas Processing: Technology and Engineering Design*, Elsevier 2014 (ISBN 978-0-08-099971-5). Surface gathering and manifold sections.
- **ASME B31.3** — Process Piping code; the canonical hydrostatic test and weld-qualification reference for production piping.
- **SPE OnePetro manifold and tie-in literature** — practitioner corpus on hot-tap procedure development, subsea manifold tie-back operations, brownfield manifold revamps, and high-density unconventional-shale gathering systems.
