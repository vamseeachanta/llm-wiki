---
title: "LNG Boil-Off Gas Management"
tags: [lng-projects, concept, bog, reliquefaction, vapor-handling, me-gi, me-ga, fsru, gcu]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-marine-transfer-systems.md
  - ../concepts/lng-vapor-handling.md
  - ../concepts/lng-cargo-containment-systems.md
  - ../concepts/lng-process-safety.md
  - ../../standards/nfpa-59a.md
  - ../../standards/igc-code.md
  - ../../standards/en-1473.md
---

# LNG Boil-Off Gas Management

## Scope

This page summarizes how boil-off gas (BOG) is generated across LNG plants, storage tanks, carriers, and floating assets, and how the resulting cold-vapor streams are routed, reliquefied, consumed, or disposed of. It is the **economics-and-routing companion** to [LNG Vapor Handling](./lng-vapor-handling.md): the vapor-handling page covers the *physical operational envelope* (vapor-return arms, gas-up/gas-freeing, emergency relief, vent/flare actuation), while this page covers the *generation rates, routing economics, and reliquefaction-versus-fuel-versus-disposal trade-off*. The page does **not** restate compressor sizing curves, vendor reliquefaction-loop heat-balance tables, BOR-warranty clauses, or specific make-up gas balances — those live in vendor specifications or future standards-page authoring.

## Why BOG management matters

- **Cargo loss and revenue exposure** — every cubic metre of BOG vented or flared is cargo that does not reach the buyer. On a 174,000 m³ membrane carrier at 0.10 percent/day natural BOR, that is roughly 174 m³ liquid-equivalent per day; over a typical voyage the cumulative envelope is large enough that BOG routing is a first-order commercial decision, not an auxiliary-system afterthought.
- **Tank-pressure boundary control** — BOG generation directly drives the rate of pressure rise in cargo and storage tanks. If BOG removal (compression, reliquefaction, fuel-gas draw) cannot keep pace, the tank crosses into emergency-relief actuation. BOG management is therefore tied directly to the operational envelope described in [LNG Vapor Handling](./lng-vapor-handling.md).
- **Methane-emission accountability** — vented or flared BOG is now reported under the EU Methane Regulation (Regulation (EU) 2024/1787), the EPA Greenhouse Gas Reporting Program Subpart W, and IMO MEPC frameworks. Reliquefaction or fuel-gas use is increasingly preferred over routine venting for compliance, not just economics.
- **Engine-side fuel demand** — on dual-fuel LNG carriers, BOG availability and fuel-gas demand from the propulsion plant must be balanced. Mismatch (excess BOG vs. propulsion demand at low speed; insufficient BOG at high speed requiring forced vaporization) shapes the reliquefaction sizing decision.

## BOG generation rates

- **Membrane carriers** (GTT NO96, Mark III, Mark V) — typical design natural BOR is **0.10–0.15 percent of cargo by mass per day** at full load. Modern Mark III Flex and Mark V variants target the lower end.
- **Moss-type spherical carriers** — historically **0.15–0.20 percent/day**, reflecting the larger surface-to-volume ratio of multi-sphere arrangements relative to membrane prismatic geometry.
- **Forced vs. natural BOG** — natural BOG tracks heat ingress through insulation; forced BOG is additional vapor produced (by spraying liquid through a vaporizer) to satisfy fuel-gas demand when natural BOG falls short. Modern operating practice prefers reliquefaction of excess natural BOG over forced-BOG generation when propulsion demand is low.
- **Onshore terminal storage** — full-containment tanks typically design for daily BOR around **0.05–0.10 percent/day**, lower than carriers because the static insulation is thicker and there is no hull-girder thermal coupling. Pump churn, flash on filling, and ambient swing add to the steady-state base.
- **FSRU regas duty** — see the FSRU section below; regasification adds a duty-cycle BOG profile distinct from the static-storage envelope.
- **Fill-level and partial-load effects** — partial-fill operation increases sloshing-driven heat input and can shift the BOR materially upward; route and operating-envelope restrictions (especially on membrane carriers) interact with BOG-handling sizing.

## BOG routing options

- **Reliquefaction** — small refrigeration loop (typically a Brayton or mixed-refrigerant cycle) that compresses BOG, condenses it against a refrigerant, and returns liquid to the cargo or storage tank. Common on FSRUs, large modern LNG carriers (≳174k m³), and some onshore terminal expansions; sized against design BOR plus a margin for warm-cargo or partial-load excursions.
- **Fuel-gas use** — BOG is compressed and routed to dual-fuel propulsion engines, terminal utility boilers, or gas-turbine drivers. On carriers this is the dominant option historically; the dual-fuel-engine generation (ME-GI / ME-GA / X-DF) determines BOG-handling architecture, since high-pressure and low-pressure engines have different compressor and vaporizer requirements.
- **Gas-combustion unit (GCU)** — onboard combustor that destroys excess BOG that cannot be reliquefied or consumed by propulsion. GCUs replace the older atmospheric vent path on modern carriers; they preserve the safety function of disposal while burning rather than venting methane.
- **Flare** — terminal-side disposal route for surplus or upset BOG; cold-flare designs are tuned for cryogenic vapor combustion. See the flare-systems coverage in [LNG Vapor Handling](./lng-vapor-handling.md).
- **Atmospheric vent** — last-resort disposal in legacy installations and emergency-relief actuation; routine venting is increasingly disfavored under methane-emission regulation.

## Economic trade-off framework

- **Capital cost** — reliquefaction is capital-intensive: a typical onboard reliquefaction plant for a 174k m³ carrier represents tens of millions of US dollars in capex. Fuel-gas use adds compressor and vaporizer cost but reuses the propulsion plant. GCU adds combustor cost but no recovery value.
- **Operating cost** — reliquefaction consumes electrical power (typically megawatt-class draw) that itself comes from BOG fuel-gas burn or marine fuel; effective recovery efficiency on a delivered-LNG basis is in the rough range of 70–90 percent depending on cycle and ambient. Fuel-gas use has zero cargo-recovery efficiency but offsets marine fuel cost.
- **Methane-emission cost** — BOG vented or flared is increasingly priced via methane intensity factored into LNG cargo pricing, regulatory exposure under EU Methane Regulation 2024/1787, and operator ESG reporting. The carbon and methane price stack tilts the economics further toward reliquefaction.
- **Lifetime envelope** — over a 20–40 year asset life, the cumulative cargo recovered by reliquefaction (or the cumulative fuel cost offset by BOG fuel-gas use) is the comparison basis. Modern carrier specifications typically include reliquefaction as a baseline rather than an option, reversing the older default of fuel-gas-only.

## Carrier engine-side BOG handling

- **ME-GI (high-pressure dual-fuel two-stroke, MAN ES)** — injects BOG at roughly 300 bar; requires a high-pressure BOG compressor (HPC). Diesel-cycle combustion gives high efficiency and low methane slip. Common on modern Korean-built large carriers.
- **ME-GA (low-pressure dual-fuel two-stroke, MAN ES)** — injects BOG at roughly 16 bar; requires only a low-pressure compressor. Otto-cycle combustion has higher methane slip than ME-GI but lower compressor capex and opex; pairs well with onboard reliquefaction since the compressor side is simpler.
- **X-DF (Wärtsilä/WinGD low-pressure two-stroke)** — competing low-pressure dual-fuel architecture; similar BOG-handling envelope to ME-GA.
- **Dual-fuel four-stroke (steam-replacement retrofits and small-scale)** — older steam-turbine carriers retrofitted with four-stroke dual-fuel engines have intermediate methane-slip and BOG-handling profiles.
- **Steam-turbine legacy** — pre-2010 carriers used steam plants that consumed BOG directly in the boilers; lower thermal efficiency drove the migration to dual-fuel diesel propulsion.
- See [LNG Vapor Handling](./lng-vapor-handling.md) on methane-slip mitigation across these engine families.

## FSRU regas BOG profile

- **Regas duty cycle** — when an FSRU is sending out gas, the cargo pump and regasification duty effectively consumes cold liquid; BOG generated through heat ingress is typically reliquefied or sent into the regas loop to recover.
- **Idle / standby duty** — when the FSRU is moored without active sendout, BOG handling reverts to the static-storage envelope: reliquefaction or GCU disposal as fallback.
- **Cargo-receiving operations** — STS transfer to an FSRU adds a transient BOG load from vapor displacement; vapor-return arm or onboard reliquefaction handles the displaced vapor (see [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md)).
- **Sizing implication** — FSRU BOG-handling capacity is sized against the maximum of static, regas, and receiving cases; reliquefaction is now the dominant choice for new FSRU builds.

## Standards and references

- [NFPA 59A](../standards/nfpa-59a.md) — US LNG production/storage/handling design code governing onshore BOG handling and relief sizing.
- [IGC Code](../standards/igc-code.md) — IMO international gas-carrier code; Chapter 8 governs cargo-tank vent, relief, and BOG-handling on the carrier side.
- [EN 1473](../standards/en-1473.md) — European harmonized standard for onshore LNG installations including BOG-handling and relief design.
- SIGTTO BOG management guidance: <https://www.sigtto.org/publications>
- IACS class rules for gas carriers: <https://iacs.org.uk/>

## Future trends

- **Reliquefaction as default** — new LNG carrier specifications increasingly include onboard reliquefaction as a baseline rather than an option, reversing the older fuel-gas-only default.
- **Methane-slip mitigation on engine side** — ME-GI and emerging clean-Otto designs reduce engine-side methane emissions; combined with reliquefaction, the lifetime methane envelope of a modern carrier is materially below the 2010-vintage steam-turbine baseline.
- **Cold-energy recovery integration** — terminal-side regasification cold energy can drive Rankine-cycle power generation or air-separation precooling, recovering energy that would otherwise be lost in vaporization; sits at the boundary of BOG handling and process integration.
- **Methane-oxidation catalysts** — pilot-scale catalytic oxidation of vent and slip streams; not yet commercial at LNG-cargo scale but a plausible decarbonization path for residual methane that escapes capture.

## Cross-references

- [LNG Vapor Handling](./lng-vapor-handling.md) — physical-systems companion: vapor-return, gas-up/gas-freeing, emergency relief, flare and vent operations.
- [LNG Storage Tanks](./lng-storage-tanks.md) — primary onshore BOG source; tank insulation and rollover behavior set the static BOR envelope.
- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — ship-side containment whose family (Moss vs. membrane vs. SPB) sets the carrier daily BOR.
- [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md) — vapor-return path during ship-to-shore and ship-to-ship transfer interfaces with BOG balance.
- [LNG Process Safety](./lng-process-safety.md) — rollover and relief-system sizing tie BOG behavior to consequence-category release scenarios.
