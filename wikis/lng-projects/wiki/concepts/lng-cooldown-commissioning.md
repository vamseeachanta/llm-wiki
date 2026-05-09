---
title: "LNG Cooldown + Commissioning Procedures"
tags: [lng-projects, concept, cooldown, commissioning, gas-up, gas-trial, first-cargo, drydock, thermal-shock, cryogenic-conditioning]
added: 2026-05-09
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../../standards/igc-code.md
  - ../../standards/sigtto-mooring-equipment.md
  - ./lng-marine-transfer-systems.md
  - ./lng-process-safety.md
  - ./lng-cargo-containment-systems.md
  - ./lng-storage-tanks.md
  - ./lng-boil-off-gas-management.md
---

# LNG Cooldown + Commissioning Procedures

## Scope

This page is the operations-side companion to the cargo-containment design pages. It covers the staged thermal conditioning of LNG carrier cargo tanks before first cargo, the re-cooldown sequence after drydock, and the heel-cargo decision that avoids a full warm-up cycle between voyages. It does **not** restate vendor-specific membrane procedures (GTT NO96 / Mark III / Mark V), proprietary ramp-rate curves, or class-society sign-off clause text — those live in ship-specific operating manuals and class procedural rules.

## Why cooldown + commissioning matter

- **Thermal-shock risk** — ambient-temperature steel hitting -162°C without staged conditioning can crack membrane systems; membrane damage is typically an irreparable insurance loss event because Invar and stainless secondary barriers cannot be re-welded in place at scale.
- **Schedule sensitivity** — a typical full cooldown takes 12-24 hours; first-cargo loading windows depend on cooldown completion, nitrogen-purge verification, and LNG-vapor concentration sign-off, all of which sit on the critical path for delivery.
- **Insurance + class-society sign-off** — cooldown protocols are class-required and insurance-required artifacts; surveyors witness the first cooldown and the procedure becomes part of the ship's operating record.

## Three primary scenarios

- **New-ship gas-trial** (post-yard, pre-delivery) — full vapor-purge sequence from inert-gas → nitrogen → LNG vapor → first cargo. This is the longest cycle and is performed once per hull.
- **Post-drydock re-cooldown** (after warming for inspection or repair) — selective tank cooling, often on a partial-tank basis if some tanks retained heel.
- **Maintained-cold operation** — heel cargo retention between voyages avoids a full warm-up cycle and reduces re-cooldown time and LNG consumption.

## Phased cooldown protocol

- **Phase 1 — Inerting** — nitrogen purge to drive oxygen and any hydrocarbon residual below the class-required thresholds (typically <1% each, but verify against the ship's specific procedure). Class-required and witnessed.
- **Phase 2 — Gas-up** — introduce warm LNG vapor to displace nitrogen. SIGTTO guidance and IGC Code Chapter 17 prescribe minimum vapor-content + density curves so the tank atmosphere stays out of the flammable envelope.
- **Phase 3 — Cooldown** — gradual LNG liquid spray combined with vapor circulation reduces tank temperature at typically 5-10°C/hour. Membrane systems may have stricter restrictions (often <3°C/hr) for partial-fill regimes; consult the ship-specific manual.
- **Phase 4 — Post-cooldown verification** — tank-temperature uniformity check, leak-test, and first-cargo-readiness sign-off by master and surveyor.

## Critical operational risks

- **Thermal-shock damage** — too-fast cooldown cracks Invar membrane (NO96 primary) or stainless (Mark III primary).
- **Roll-over precursor** — stratification during cooldown can prime later boil-off events; uniformity verification in Phase 4 is partly aimed at this.
- **Hydrocarbon-air explosion** — Phase 2 and Phase 3 must avoid the 5-15% LNG-air mix in any tank space; the gas-up density curves exist to traverse this envelope quickly with controlled flow.
- **Nitrogen asphyxiation** — Phase 1 and Phase 2 require gas-detector and entry-permit protocols; nitrogen is the dominant fatality mode in cooldown operations.

## SIGTTO + class-society guidance

- **SIGTTO** — best-practice cooldown procedures and gas-trial guidance for LNG carriers and terminals.
- **GTT membrane-specific procedures** for NO96 / Mark III / Mark V — proprietary; ship-specific operational manuals ship with each hull.
- **MOSS Maritime cooldown procedures** — sphere-specific; published guidance for spherical-tank cooldown ramps.
- **Class procedures** — DNV, ABS, BV, LR, KR each maintain procedural rules for surveyor-witnessed first cooldowns and post-drydock re-cooldowns.

## Drydock cycle

- **Tank warm-up** for drydock entry — typically 6-12 days; warming must be slow enough to avoid the same thermal-shock failure mode in reverse.
- **Tank inspection** during dock — leak-test and thermal-cycle inspection of primary and secondary barriers; opportunity to detect membrane fatigue.
- **Re-cooldown** post-dock — substantially faster than first-cooldown if some tanks retained heel; full Phase 1-4 cycle if fully warmed.

## Heel cargo management

- **Heel cargo** = approximately 5,000-10,000 m³ retained LNG between voyages (carrier-size-dependent).
- Maintains tanks at near-cold temperature; avoids the cost of re-cooldown LNG, typically in the range of $50,000-200,000 per cycle including bunker fuel and lost cargo capacity.
- Operational decision balanced against the bunker-fuel cost of carrying the heel and the lost-deadweight of unsold cargo space.

## Future trends

- **Faster cooldown** — short-cycle small-scale LNG operators are pushing for compressed cooldown windows; research at GTT and class societies on revised ramp-rate envelopes.
- **AI-assisted cooldown supervision** — emerging at major LNG operators (Total, Shell, ExxonMobil) to optimize spray-rate vs. temperature uniformity in real time.
- **LNG-as-fuel cooldown** — bunker fuel-tank cooldown is procedurally simpler since volumes are small and Type C pressure tanks tolerate broader thermal envelopes than membrane cargo systems.

## Cross-References

- [IMO IGC Code](../standards/igc-code.md) — mandatory cooldown framework for international gas carriers
- [SIGTTO Mooring Equipment Guidelines](../standards/sigtto-mooring-equipment.md) — terminal-side context for first-cargo berthing
- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — thermal-shock susceptibility by containment-system type (membrane vs. Moss vs. SPB)
- [LNG Storage Tanks](./lng-storage-tanks.md) — onshore-tank companion (single-, double-, full-containment, in-ground) for terminal-side cooldown context
- [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md) — transfer-side companion at first cargo and re-loading
- [LNG Process Safety](./lng-process-safety.md) — cooldown-related hazards (rollover precursors, VCE envelope, nitrogen asphyxiation)
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — heel cargo retention and cooldown-phase BOG generation
