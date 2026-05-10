---
title: "LNG Cooldown + Commissioning Procedures"
tags: [lng-projects, concept, cooldown, commissioning, gas-up, gas-trial, first-cargo, drydock, thermal-shock, cryogenic-conditioning]
added: 2026-05-09
last_updated: 2026-05-10
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

### Multi-criteria comparison of the three scenarios

| Scenario | Frequency | Duration envelope | LNG consumed for cooldown | Class/insurance involvement | Critical-path exposure |
|---|---|---|---|---|---|
| New-ship gas-trial | Once per hull | Days; full Phase 1-4 cycle | Highest (full warm-tank cooldown) | Surveyor-witnessed; insurance milestone | First-cargo readiness on critical path |
| Post-drydock re-cooldown | Every 5 years (class survey) | 1-3 days, part-cooldown if heel retained | Medium | Surveyor-witnessed for sensitive procedures | Post-dock first-cargo on critical path |
| Maintained-cold (heel cargo) | Every voyage | Hours-to-days re-top-up of cargo | Lowest | Routine; no surveyor involvement | None (on-schedule) |

The decision to maintain cold via heel-cargo or to warm-up between voyages is dominated by the cost differential: heel-cargo carries an opportunity cost (lost cargo capacity + bunker fuel to carry the heel) but avoids the LNG, time, and class-witness overhead of a full warm-cooldown cycle.

## Phased cooldown protocol

- **Phase 1 — Inerting** — nitrogen purge to drive oxygen and any hydrocarbon residual below the class-required thresholds (typically <1% each, but verify against the ship's specific procedure). Class-required and witnessed. Phase 1 establishes the asphyxiation-risk envelope inside which Phase 2 then operates; entry-permit and gas-detector protocols are class-mandated.
- **Phase 2 — Gas-up** — introduce warm LNG vapor to displace nitrogen. SIGTTO guidance and IGC Code Chapter 17 prescribe minimum vapor-content + density curves so the tank atmosphere stays out of the flammable envelope. The gas-up density curve is engineered specifically to pass through the 5-15% methane-air flammable band quickly with controlled flow, so the residence time inside the flammable envelope is bounded.
- **Phase 3 — Cooldown** — gradual LNG liquid spray combined with vapor circulation reduces tank temperature at typically 5-10°C/hour. Membrane systems may have stricter restrictions (often <3°C/hr) for partial-fill regimes; consult the ship-specific manual. The spray pattern, head-pressure, and bypass-vapor circulation are tuned per containment family — Moss, membrane, and SPB each have distinct heat-transfer regimes inside the tank.
- **Phase 4 — Post-cooldown verification** — tank-temperature uniformity check, leak-test, and first-cargo-readiness sign-off by master and surveyor.

### Tank-type-specific cooldown variations

| Containment family | Typical cooldown ramp | Spray-pattern note | Key thermal-shock mode | Phase-4 verification focus |
|---|---|---|---|---|
| Moss spherical | ~5-10°C/hour | Internal spray header from tank top; symmetric distribution | Aluminum-sphere weld sensitivity | Sphere-skin temperature uniformity |
| Membrane (NO96, Mark III, Mark V) | ~3-5°C/hour for partial fill; up to ~10°C/hr for full | Multiple spray nozzles for distributed coverage | Invar (NO96) or stainless (Mark III) primary-barrier crack | Membrane-temperature uniformity + leak-test |
| SPB (IHI Self-supporting Prismatic) | ~5-8°C/hour | Distributed spray; prismatic geometry tolerant of non-uniformity | Aluminum primary-barrier weld sensitivity | Tank-temperature uniformity check |

The membrane-system tighter ramp constraint is the most important operational difference: in partial-fill regimes (typical of the post-cooldown low-fill state) the membrane can experience a temperature gradient that drives strain into the Invar or stainless primary barrier and propagates into a crack. The post-2010 generation of membrane procedures (GTT-issued) has tightened these ramps materially.

## Critical operational risks

- **Thermal-shock damage** — too-fast cooldown cracks Invar membrane (NO96 primary) or stainless (Mark III primary).
- **Roll-over precursor** — stratification during cooldown can prime later boil-off events; uniformity verification in Phase 4 is partly aimed at this.
- **Hydrocarbon-air explosion** — Phase 2 and Phase 3 must avoid the 5-15% LNG-air mix in any tank space; the gas-up density curves exist to traverse this envelope quickly with controlled flow.
- **Nitrogen asphyxiation** — Phase 1 and Phase 2 require gas-detector and entry-permit protocols; nitrogen is the dominant fatality mode in cooldown operations.

## Worked-cases (operational precedents)

- **Membrane cracking from accelerated cooldown** — class-of-event: a partial-fill cooldown that exceeds the GTT-prescribed ramp under operational pressure (e.g., charter-fixed delivery window) propagates a strain-induced crack in the Invar primary barrier. Repair requires drydock and partial-membrane replacement, an insurance-write-off-class loss event. Recurring teaching example for class-society survey training.
- **Roll-over precursor patterns** — class-of-event: composition-stratified storage, often after a heavier-than-average cargo is loaded over a lighter heel, drives a density gradient that can re-equilibrate spontaneously with rapid BOG release. The Phase-4 uniformity verification check exists specifically to catch the precursor pattern before first-cargo loading. The textbook precedent is the 1971 La Spezia rollover incident (Italy), which set the modern stratification-monitoring practice.
- **Gas-up-related N2 asphyxiation incidents** — class-of-event: low-O2 atmospheres inside or adjacent to tanks during Phase 1 and Phase 2 are the dominant fatality mode in cooldown operations. Every cooldown campaign has to enforce gas-detector use, two-person entry rules, and rescue-equipment readiness; the residual rate of incidents drove the SIGTTO and IMO publication of dedicated nitrogen-asphyxiation hazard guidance and the requirement for atmosphere-test before access to confined spaces.

## SIGTTO + class-society + GTT-specific guidance

- **SIGTTO** — best-practice cooldown procedures and gas-trial guidance for LNG carriers and terminals; the SIGTTO Liquefied Gas Handling Principles publication is the public-domain reference work.
- **GTT membrane-specific procedures** for NO96 / Mark III / Mark V — GTT issues per-hull operational manuals that include the full cooldown ramp curves, spray-rate envelopes, and class-acceptance criteria for the membrane systems. These are proprietary to the ship-and-shipowner combination; they are not duplicated in this public wiki by reference.
- **MOSS Maritime cooldown procedures** — sphere-specific; published guidance for spherical-tank cooldown ramps. Moss tanks, by virtue of the sphere geometry and aluminum primary structure, follow a different thermal-shock envelope than membrane systems.
- **Class procedures** — DNV, ABS, BV, LR, KR each maintain procedural rules for surveyor-witnessed first cooldowns and post-drydock re-cooldowns. The class-society procedural rule is what the surveyor uses to issue the cooldown sign-off; it is reconciled at the survey with the GTT or Moss vendor procedure for the specific containment system.
- **IGC Code Chapter 17** — international gas-carrier-code framework for cargo-tank gas-trial, cooldown, and gas-freeing on commissioning. IGC 17 is the public-domain treaty-level instrument that frames the class-society procedure.

## Drydock cycle

- **Tank warm-up** for drydock entry — typically 6-12 days; warming must be slow enough to avoid the same thermal-shock failure mode in reverse. The warm-up ramp is governed by the same vendor-specific envelope as the cooldown ramp — typically 3-5°C/hour for membrane and 5-10°C/hour for Moss spherical.
- **Tank inspection** during dock — leak-test and thermal-cycle inspection of primary and secondary barriers; opportunity to detect membrane fatigue. The inspection is the surveyor's window into accumulated micro-strain damage from the inter-drydock period.
- **Re-cooldown** post-dock — substantially faster than first-cooldown if some tanks retained heel; full Phase 1-4 cycle if fully warmed. Selective tank cooldown (some tanks fully warmed, others retained heel) is increasingly the operational default in mid-life class surveys, allowing inspection of the targeted tank or barrier without the LNG and time cost of a fleet-wide warm-up.

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
