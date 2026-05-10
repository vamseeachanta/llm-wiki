---
title: "LNG Marine Transfer Systems"
tags: [lng-projects, concept, marine, transfer, jetty, ship-to-ship, fsru, flng, loading-arms, esd, mbc, qcdc, sigtto, ocimf]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-project-shapes.md
  - ../concepts/lng-regulatory-framework.md
  - ../concepts/lng-vapor-handling.md
  - ../concepts/lng-cargo-containment-systems.md
  - ../concepts/lng-process-safety.md
  - ../../standards/sigtto-mooring-equipment.md
  - ../../standards/igc-code.md
  - ../../standards/nfpa-59a.md
  - ../../standards/phmsa-49-cfr-193.md
---

# LNG Marine Transfer Systems

## Scope

This page surveys the marine-side **transfer interfaces** between LNG carriers, jetties, FSRUs, FLNG units, ship-to-ship lighter operations, and small-scale truck/barge loading. It covers transfer-interface taxonomy, loading-arm types, emergency shutdown logic, manifold and vapor-return architecture, and operational-envelope considerations (drift, tide, current, ship-shore link). Page is concept-level — it does **not** restate jetty design clauses, mooring-load envelopes, specific environmental operability thresholds, or hose-burst-test rated working pressures; those live in standards-page authoring under [SIGTTO](../standards/sigtto-mooring-equipment.md), OCIMF MEG4, [NFPA 59A](../standards/nfpa-59a.md), and the [IGC Code](../standards/igc-code.md). Tandem mooring is named here by reference and is fully covered in the marine-engineering wiki — this page does not duplicate that content.

## Why marine transfer matters

- **Throughput chokepoint** — marine transfer is typically the throughput-limiting step at import and export terminals; jetty availability, weather windows, and turnaround time set effective annual capacity below the rated nameplate.
- **Highest-consequence operating envelope** — ship-shore transfer is the operational regime where the highest-volume cryogenic transfer rates intersect human-occupied jetty structures, which is why ESD logic, vapor-return, and emergency-disconnect architecture receive intense regulatory and class-society scrutiny.
- **Ship-shore-link contractual envelope** — the SIGTTO ship-shore-link agreement, OCIMF MEG4, and ICS guidance define the procedural and contractual interface between carrier and terminal. Operational deviation from that envelope (e.g., transferring outside agreed environmental limits) carries direct safety, insurance, and contractual exposure.
- **Marine-side release scenarios** — RPT (rapid phase transition) and pool fire on water are most consequential for marine transfer scenarios (see [LNG Process Safety](./lng-process-safety.md)); transfer-system design directly addresses the precursor failure modes.

## Transfer-interface taxonomy

### Conventional jetty + marine loading arms

- Fixed berth with hard-arm (Chiksan-style) loading arms; the dominant onshore configuration for both import and export terminals.
- Typical arrangement: 3 or 4 liquid arms plus 1 vapor-return arm at a dedicated LNG berth.
- Berth occupancy: a typical 174,000 m³ unloading is on the order of 12 hours from arrival to departure, including pre-cooldown, transfer, and disconnect; export loading is comparable.

### Ship-to-ship (STS)

- Side-by-side carrier-to-FSRU or carrier-to-carrier transfer; constrained by sea-state and fender envelope. Common in FSRU-served import markets where a permanent jetty is impractical or where staged transfer to a smaller distribution carrier is required.
- SIGTTO STS guidance covers approach, fender-deployment, mooring-line plan, transfer-rate ramping, and emergency-disconnect protocols.

### FSRU regas operation

- Moored FSRU regasifies cargo into a downstream pipeline; the FSRU itself acts as the marine-side terminal, and incoming carriers transfer to the FSRU via STS or via a dedicated jetty arrangement.
- BOG profile differs from a static-storage terminal — see [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) FSRU section.

### FLNG offloading

- Typically side-by-side at sheltered locations or tandem at exposed ones. Tandem mooring offloading geometry is named by reference here; the engineering coverage is in the marine-engineering wiki.
- Offloading window is set by relative motion between FLNG and shuttle carrier; sea-state limits drive a real availability penalty vs. fixed-jetty operation.

### Truck-to-ship (LBVR, small-scale)

- LNG bunkering and small-scale LNG distribution use truck or barge sources to fuel LNG-fueled ships at port; covered by ISO 20519 and related guidance.

## Loading-arm types

- **Chiksan-style hard arms** — articulated swivel-jointed cryogenic loading arms; the dominant configuration for jetty-based carrier loading and unloading. Designed to accommodate vessel motion (tide, list, surge, sway) within an operating envelope; outside envelope triggers ESD logic.
- **Emergency Release System (ERS)** — integrated into the loading-arm design, the ERS provides a powered-and-tested emergency disconnect at a dedicated coupling point on the arm. Activation isolates the carrier and terminal sides via paired Emergency Release Couplings (ERCs) so the arm can retract safely.
- **Cryogenic flexible hoses** — fully composite or vacuum-insulated cryogenic hoses; used at FSRU/STS service, in offshore tandem-offloading systems, and increasingly in small-scale LNG-bunker operations where hard arms are impractical. Flexible-hose maturity has increased substantially over the past decade.
- **Hybrid arrangements** — some FLNG and STS configurations combine cryogenic flexible hoses for the primary cargo path with a hard-arm or rigid-quick-connect arrangement for vapor return.

## Emergency Shutdown and Emergency Disconnect

- **ESD-1 (cargo-flow stop)** — controlled shutdown of cargo-pump and shore-side flow, with all valves driven to a defined safe-state. Triggered by deviation outside operational envelope (pressure/flow excursion, vapor-return loss, communication-link failure, low/high tank level). Detection-to-isolation target on the order of seconds.
- **ESD-2 (cargo-flow stop with arm decoupling preparation)** — cargo-flow stop plus arming of the ERS/ERC for a powered emergency disconnect. The ESD-1/ESD-2 ladder is a SIGTTO best-practice convention rather than a single global standard; carrier and terminal ESD systems must be cross-tested against the ship-shore-link agreement before transfer.
- **Emergency Release Coupling (ERC)** — paired powered coupling on the loading arm; on activation each half closes and the arm separates with both ends sealed. Re-arming and re-coupling after activation is a controlled procedure, not a routine operation.
- **Marine Breakaway Coupling (MBC)** — passive emergency-release device on cryogenic flexible hoses; activates on excessive tension or pull. Used in STS and offshore service where arm-style ERS is not applicable.
- **Quick-Connect/Disconnect Coupler (QCDC)** — manifold-side coupling for STS and offshore service; allows fast connection and disconnection within an environmental-window-driven operating envelope.

## Manifolds, vapor-return, and connection protocols

- **Carrier manifold** — standardized to OCIMF / SIGTTO manifold-position guidance to allow carrier-to-terminal interoperability across the global fleet.
- **Vapor-return architecture** — every cubic metre of LNG transferred displaces roughly an equivalent volume of warm vapor that must be returned to the source tank or otherwise disposed of. The vapor-return arm and pressure-balance system are loading prerequisites; failure of the vapor-return path triggers cargo-flow shutdown. See [LNG Vapor Handling](./lng-vapor-handling.md) for the broader vapor-balance scope.
- **Ship-shore-link (SSL)** — fiber-optic or pneumatic communications link carrying ESD trip signals, mooring-load data, and operational telemetry between carrier and terminal. SSL availability is a transfer-prerequisite and an SSL fault is an immediate ESD trigger.
- **Connection protocols** — SIGTTO LNG-terminal/carrier guidance, OCIMF MEG4, and ICS Tanker Safety Guide define the procedural envelope for connection, leak-test, ramp-up, steady-state, and disconnect.

## Operational envelope considerations

- **Drift, tide, current, surge** — relative motion between carrier and jetty (or between two ships in STS) drives the loading-arm or hose operating envelope. Outside envelope: ESD-1 → ESD-2 → ERC activation ladder.
- **Wind and wave** — agreed environmental-window limits in the ship-shore agreement; exceedance triggers transfer-stop. STS and tandem operations have tighter limits than fixed jetties.
- **Vessel-motion monitoring** — real-time mooring-line load monitoring, position-keeping, and arm-envelope monitoring feed the ESD interlocks.
- **Cooldown management** — pre-transfer cooldown of arms, hoses, and shore-side piping is part of the transfer sequence (see [LNG Cooldown + Commissioning Procedures](./lng-cooldown-commissioning.md)).
- **Compatibility study** — every new carrier-terminal pairing requires a documented compatibility study addressing manifold reach, mooring-line geometry, fender contact, and ESD inter-operability before first transfer.

## Standards and references

- [SIGTTO Mooring Equipment Guidelines](../standards/sigtto-mooring-equipment.md) — LNG terminal/carrier mooring practice for transfer operations.
- [IGC Code](../standards/igc-code.md) — IMO international gas-carrier code governing manifold and cargo-transfer interfaces on the carrier side.
- [NFPA 59A](../standards/nfpa-59a.md) — Chapter 12 marine activities at LNG facilities (transfer-area design and operation).
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations including marine transfer-area incident reporting.
- OCIMF MEG4 (Mooring Equipment Guidelines, 4th edition): <https://www.ocimf.org/>
- SIGTTO LNG/LPG terminal and transfer guidance: <https://www.sigtto.org/publications>
- ICS Tanker Safety Guide (Liquefied Gas): <https://www.ics-shipping.org/>

## Future trends

- **Cryogenic flexible-hose maturity** — full-cryogenic flexible hoses are now a credible primary alternative to hard arms in select STS and offshore service, expanding the transfer-window envelope.
- **Standardized small-scale LNG bunkering** — ISO 20519 and related guidance have driven repeatable LNG-bunkering practice at major ports, enabling LNG-fueled-ship growth.
- **Tandem-offloading FLNG growth** — tandem offloading at exposed FLNG sites is a maturing operating mode with active class-society and SIGTTO guidance development.
- **Methane-emission reduction at transfer** — vapor-return capture (vs. atmospheric venting) is now baseline; emerging emphasis on quantifying and minimizing methane release during connect/disconnect transients.
- **Autonomous and remote-monitored connection** — pilot deployments of camera-and-laser-assisted connection and remote-monitored vapor-return performance; not yet at full automation but tightening the operational envelope.

## Cross-references

- [LNG Project Shapes](./lng-project-shapes.md) — how the transfer interface differs by project shape (export, import, FSRU, FLNG, small-scale).
- [LNG Regulatory Framework](./lng-regulatory-framework.md) — standards bodies governing marine transfer.
- [LNG Vapor Handling](./lng-vapor-handling.md) — vapor-return arm and ship-shore vapor-balance interface during transfer.
- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — ship-side containment that connects to the terminal via the transfer interface.
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — BOG balance during transfer operations.
- [LNG Process Safety](./lng-process-safety.md) — RPT and pool-fire-on-water scenarios most consequential for marine transfer.
- **Cross-wiki (marine-engineering)**: [LNG Transfer System Envelope](../../../marine-engineering/wiki/concepts/lng-transfer-system-envelope.md) — engineering-detail companion (similar slugs / titles; shared SIGTTO + FSRU + LNG vocabulary).
- **Cross-wiki (marine-engineering)**: [LNG Marine Terminal Engineering](../../../marine-engineering/wiki/concepts/lng-marine-terminal-engineering.md) — terminal-engineering companion (shared jetty + STS + SIGTTO vocabulary).
