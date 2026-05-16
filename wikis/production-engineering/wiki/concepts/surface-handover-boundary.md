---
title: "Surface Handover Boundary"
tags: [surface-handover, scope-edge, manifold-inlet, choke-skid, separator-inlet, pe-surface-facility-boundary, production-engineering]
added: 2026-05-16
last_updated: 2026-05-16
---

# Surface Handover Boundary

## Scope

This page is the **router** for the surface-handover boundary cluster — the operational and engineering edge at which production-engineering scope hands off to surface-facility (topsides) engineering. It is the structural analog at the upstream-vs-surface boundary to what [Well Integrity During Production](well-integrity-during-production.md) is at the construction-vs-operation boundary: a deliberate, named scope-edge that frames where this wiki's coverage stops and where a sibling discipline picks up.

The boundary runs **from the wellhead through the production manifold through the surface choke skid and terminates at the separator inlet**. Everything inside that envelope is production-engineering scope and is covered in this wiki. Everything downstream of the separator inlet — separator vessel design, gas treatment, oil-water separation internals, glycol dehydration, amine sweetening, compression, export-pipeline interface, and refinery-side processing — is **reserved for a hypothetical future surface-facility-engineering wiki** and is **explicitly OUT OF SCOPE** for this wiki.

## CRITICAL: scope-edge — what this wiki covers vs reserves

The phrase "surface facility" spans a much larger envelope than production-engineering owns. The producing well delivers fluid to a surface flowline, which gathers to a manifold, which routes through a choke skid, which feeds a separator that begins the surface-processing chain. The production-engineering discipline owns the **wellhead-to-separator-inlet** envelope; the surface-facility-engineering discipline owns the **separator-vessel and downstream-processing** envelope.

- **IN SCOPE (this wiki)** — wellhead, wing/master valves, surface safety valve (SSV), surface piping from the wellhead to the manifold, production and test manifolds, surface choke skid (production choke + test choke + manifolds + actuators), separator inlet conditions (line pressure, velocity envelope, slug-flow conditioning at the slug-catcher), production-SCADA and historian architecture that monitors all of the above.
- **OUT OF SCOPE (reserved for surface-facility-engineering)** — separator vessel sizing (Bell-Whitaker / Stewart-Arnold separator-sizing frameworks, three-phase residence-time design, demister-pad sizing), gas treatment (glycol dehydration, amine sweetening, mercury removal, dewpoint control), oil treating (heater-treaters, free-water knockouts, electrostatic coalescers), produced-water treatment, compression and gas-lift compression sizing, export-pipeline metering downstream of the LACT (the LACT-itself is in scope per [Custody Transfer Overview](custody-transfer-overview.md) as the production-engineering-side fiscal closure event), refinery-side processing, LNG-train front-end.
- **OUT OF SCOPE (separate domain — cybersecurity)** — IEC 62443, ISA/IEC 62443, NIST SP 800-82 cybersecurity coverage for industrial control systems. See [Production SCADA Architecture](production-scada-architecture.md) for the scope-edge framing on cybersecurity.

The boundary is **spatial** (where the fluid is in the surface-processing chain) rather than **temporal** (which is how the [Well Integrity During Production](well-integrity-during-production.md) boundary against drilling-engineering is framed).

## Why the boundary matters operationally

The PE-vs-surface-facility boundary is load-bearing for several reasons that mirror the construction-vs-operation boundary on the upstream side:

- **Engineering disciplines differ** — production-engineering owns reservoir-coupled flow control, well-deliverability matching, multiphase choke modelling, and SCADA-and-historian architecture that streams operational data back to reservoir-management. Surface-facility-engineering owns vessel-sizing thermodynamics, separation hydrodynamics, mass-transfer engineering for gas treating, rotating-equipment sizing for compression, and process-safety engineering for downstream-vessel ESD.
- **Data sources differ** — production-engineering data sources are wellhead pressure / temperature / rate, choke position, manifold tags, separator-inlet conditions. Surface-facility-engineering data sources are separator levels and inter-stage pressures, gas-treating residual-content analysers, compressor performance maps, export-meter data. The two share the historian (see [Production Data Historian Patterns](production-data-historian-patterns.md)) but instrument the historian with different tag families.
- **Time-scales differ** — production-engineering decisioning operates on the well-by-well operating-point timescale (minutes to days). Surface-facility-engineering decisioning operates on the facility-throughput timescale (hours to weeks) and the front-end engineering and design (FEED) timescale (months).
- **Standards anchors differ** — production-engineering anchors are API 11 series (artificial lift), API 14 series (production-facility safety systems and topsides piping — overlap zone), API 17 series (subsea production systems), API MPMS (custody-transfer measurement). Surface-facility-engineering anchors are GPSA Engineering Data Book (downstream-processing handbook), API Std 521 (pressure-relieving systems), API Std 650 (storage-tank design), API Spec 12J (oil-and-gas separators specifications — boundary standard), API Std 661 (air-cooled heat exchangers), API RP 14J (hazard-analysis for offshore production facilities — boundary standard), and the GPSA + Campbell + Arnold-Stewart textbook corpus.

The boundary is **explicit** in this wiki because conflating the two scopes produces engineering and operational confusion. Operators who treat production-engineering as a sub-discipline of surface-facility-engineering miss the well-deliverability framing that is this wiki's core; operators who treat surface-facility-engineering as a sub-discipline of production-engineering miss the vessel-sizing-and-thermodynamics framing that the future surface-facility-engineering wiki will own.

## The surface-handover envelope

The fluid path through the in-scope envelope:

1. **Wellhead and Christmas tree** — covered indirectly across [Choke Management](choke-management.md), [Choke Types](choke-types.md), and [Well Integrity During Production](well-integrity-during-production.md). The wellhead is the upstream boundary of this envelope.
2. **Wellhead-to-manifold flowline** — surface piping from the wellhead to the production manifold. Subsea wells deliver fluid via jumper-and-flowline architecture (cross-domain with marine-engineering subsea hardware); surface wells deliver via topsides piping.
3. **Production and test manifolds** — covered in [Manifold Tie-In](manifold-tie-in.md). The manifold gathers multiple wells onto common production or test routes; tie-in specifications, hot-tap vs cold-tap, and pre-commissioning hydrostatic testing are addressed there.
4. **Surface choke skid** — covered in [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md). The choke skid carries the production choke (continuous duty) and the test choke (well-test duty), with manifolds for switching between them.
5. **Separator inlet** — the downstream boundary. Line pressure, slug-flow conditioning, and gas-knockout staging at the separator inlet are covered as the scope-terminating event in [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md).
6. **Production SCADA and historian** — the data-architecture overlay that spans the entire envelope and feeds production-engineering decisioning. See [Production SCADA Architecture](production-scada-architecture.md) and [Production Data Historian Patterns](production-data-historian-patterns.md).

## Bridge to Phase 4 choke management

The surface-choke skid is a **direct bridge** to the Phase 4 choke-management cluster ([Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md)). The choke-management cluster framed the choke as a hydraulic operating-point control device in well-deliverability terms; [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md) frames the choke as a piece of surface-piping hardware living on a skid that carries it through hydrostatic test, pre-commissioning, function-test, and ESD-coordination — the as-installed counterpart to the as-modelled view.

The [Erosional Velocity](erosional-velocity.md) framework similarly straddles the boundary: the erosional-velocity criterion bounds rate from above for the **entire** wellhead-to-separator-inlet envelope. The criterion is applied to choke-discharge piping (per the Phase 4 framing), to manifold tie-in headers, and to the separator-inlet line that terminates this envelope. The criterion is one of the few engineering tools that spans the entire surface-handover envelope.

## SCADA and historian overlay

Production SCADA architecture and the historian are not single-component pieces of equipment — they are an architectural overlay that touches every piece of in-scope hardware:

- **Wellhead instrumentation** — pressure / temperature / position sensors feeding the RTU/PLC at the well or well-pad
- **Manifold instrumentation** — header pressures / temperatures, choke positions, valve-position feedback
- **Choke-skid instrumentation** — choke position, upstream / downstream pressure, discharge temperature, sand-detection (acoustic or erosion-probe based)
- **Separator-inlet instrumentation** — inlet pressure / temperature, slug-detection, inlet-gas-cut indication
- **PLC / SCADA host** — orchestrates the above into the operator-facing console and the historian feed
- **Historian** — captures the operating record for trending, allocation feedback, regulatory reporting, and integrity-management feedback

The SCADA and historian overlay is covered in [Production SCADA Architecture](production-scada-architecture.md) and [Production Data Historian Patterns](production-data-historian-patterns.md). The standards anchor is [ISA-95](../standards/isa-95.md).

## Cross-domain interactions

- **Drilling-engineering** — wellhead-and-Christmas-tree as-built specification originates in well-construction (cross-link to drilling-engineering [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) for production-casing-and-wellhead pressure-rating context).
- **Marine-engineering** — subsea production hardware (subsea trees, jumpers, flowlines, subsea manifolds) straddles marine-engineering and production-engineering. The subsea-side hardware design is marine-engineering scope; the production-engineering side is the operational use of the hardware (choke-control logic, slug-arrival management on the riser).
- **Naval-architecture** — FPSO topsides scope is naval-architecture-side for the host vessel, with the production-process equipment on the topsides crossing into surface-facility-engineering scope. This wiki covers the well-tubing-to-manifold-inlet boundary; FPSO topsides processing equipment beyond the separator inlet is reserved for surface-facility-engineering.
- **Engineering-standards** — API Spec 6A (wellhead and tree equipment), API Spec 12J (oil-and-gas separators — boundary standard at the downstream edge of this envelope), API RP 14J (hazard analysis for production facilities — boundary standard), API Std 521 (pressure-relieving systems — downstream from separator).
- **Surface-facility-engineering (FUTURE)** — separator vessel sizing, gas treating, oil treating, water treating, compression, export-pipeline interface. Reserved for hypothetical future wiki.

## Cross-references

- [Manifold Tie-In](manifold-tie-in.md) — production-manifold topology and tie-in specifications
- [Choke Skid and Separator Inlet](choke-skid-and-separator-inlet.md) — surface choke skid hardware and separator-inlet conditions
- [Production SCADA Architecture](production-scada-architecture.md) — SCADA topology and ISA-95 mapping
- [Production Data Historian Patterns](production-data-historian-patterns.md) — historian write/read/tag patterns
- [Choke Management](choke-management.md), [Choke Types](choke-types.md), [Multiphase Choke Modeling](multiphase-choke-modeling.md), [Choke Sand Erosion](choke-sand-erosion.md) — Phase 4 choke cluster (operational framing the hardware here implements)
- [Erosional Velocity](erosional-velocity.md) — rate-ceiling criterion across the envelope
- [Well Integrity During Production](well-integrity-during-production.md) — operating-time integrity of the wellhead-and-tree (scope-edge sister page on the upstream boundary)
- [Production Allocation](production-allocation.md), [Well Test and Reconciliation](well-test-and-reconciliation.md), [GOR and Water-Cut Tracking](gor-and-water-cut-tracking.md), [Custody Transfer Overview](custody-transfer-overview.md), [Flow-Measurement Uncertainty](flow-measurement-uncertainty.md) — production-accounting cluster that consumes SCADA + historian data
- [Federal Production Reporting](federal-production-reporting.md), [State Production Reporting](state-production-reporting.md), [Gas Flaring Rules](gas-flaring-rules.md), [Production Allowable Rates](production-allowable-rates.md) — regulatory-reporting cluster that consumes historian data
- [Multi-Zone Completions](multi-zone-completions.md) — multi-zone surface tie-in coupling
- Drilling-engineering: [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) — production-casing-and-wellhead context
- Marine-engineering: [Corrosion Control](../../../marine-engineering/wiki/concepts/corrosion-control.md) — adjacent for subsea hardware corrosion (the in-water boundary)
- Naval-architecture: FPSO topsides (cross-reference only; deep-link reserved for future surface-facility-engineering wiki)

## Standards anchors

- **API Spec 6A** — Wellhead and Christmas Tree Equipment (upstream-boundary standard)
- **API Spec 12J** — Specification for Oil and Gas Separators (downstream-boundary standard at the separator-inlet edge)
- **API RP 14C** — see [API RP 14C](../standards/api-rp-14c.md) — safety-system methodology covering the entire envelope
- **API RP 14E** — Design and Installation of Offshore Production Platform Piping Systems (erosional-velocity criterion; cross-link to engineering-standards)
- **API RP 14J** — Recommended Practice for the Design and Hazards Analysis for Offshore Production Facilities (boundary standard — overlap with future surface-facility-engineering wiki)
- **ISA-95** — see [ISA-95](../standards/isa-95.md) — Enterprise-Control System Integration; control-hierarchy framework for the SCADA-and-historian overlay

## Public references

- **Arnold, K. & Stewart, M.** — *Surface Production Operations*, Volume 1 (Design of Oil Handling Systems and Facilities), 3rd ed., Gulf Professional Publishing (Elsevier), ISBN 978-0-7506-7853-7. The practitioner-canonical surface-production reference; covers the entire wellhead-through-export envelope. The production-engineering-side material is in scope for this wiki; the separator-vessel-and-downstream material is reserved for future surface-facility-engineering coverage.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Surface-production chapters provide the textbook framing for the wellhead-to-separator-inlet envelope.
- **GPSA — Gas Processors Suppliers Association** — *Engineering Data Book* (multiple editions; gpsamidstreamsuppliers.org). Comprehensive downstream-processing reference; primarily future-surface-facility-engineering-wiki territory, cited here as the boundary reference.
- **Campbell, J. M.** — *Gas Conditioning and Processing*, Volumes 1 and 2 (multiple editions; PetroSkills). The classical downstream-processing reference; surface-facility-engineering territory.
- **Bai, Y. & Bai, Q.** — *Subsea Engineering Handbook*, 2nd ed., Elsevier (ISBN 978-0-12-812622-5). Subsea-side hardware reference covering jumpers, flowlines, and manifolds at the marine-engineering / production-engineering boundary.
- **SPE OnePetro surface-production literature** — extensive corpus on wellhead operations, manifold design, choke-skid retrofits, and separator-inlet conditioning.
