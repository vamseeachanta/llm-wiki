---
title: "LNG Boil-Off Gas Management"
tags: [lng-projects, concept, bog, reliquefaction, vapor-handling, me-gi, me-ga, fsru, gcu]
added: 2026-05-03
last_updated: 2026-05-10
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

## Multi-criteria comparison of BOG handling options

The trade-off space across the five BOG routing options is multidimensional; capital cost alone is rarely the deciding factor once methane-emission accountability and lifetime cargo-recovery are priced in. The qualitative comparison below is the structure operators use during front-end engineering and during retrofit decisions on existing tonnage:

| Option | Capex | Opex | CO2 / methane impact | Cargo recovery | Regulatory acceptance |
|---|---|---|---|---|---|
| Reliquefaction | High | Medium (electrical draw) | Low (cargo returned to tank) | High (~70-90% delivered-LNG basis) | Strongly preferred under EU MR 2024/1787 and IMO MEPC frameworks |
| Fuel-gas use (DF engines) | Medium (compressor + vaporizer) | Low (offsets bunker fuel) | Engine-family-dependent (slip 0.2-3% by family) | Zero direct recovery; offsets fuel cost | Accepted; methane-slip mitigation now expected |
| GCU | Low-Medium | Low (only when active) | Combustion CO2; near-zero methane slip in spec | None | Accepted as backup; not as routine handler |
| Flare | Medium (cold-flare engineering) | Low (only when active) | Combustion CO2; slip if unstable | None | Permitted-only; routine flaring restricted under EU MR |
| Atmospheric vent | Lowest | Lowest | High methane (GWP ~80x CO2 over 20-year horizon) | None | Disfavored; routine venting effectively prohibited under EU MR 2024/1787 and EPA Subpart W |

The compounding effect — high methane GWP combined with regulatory pressure combined with cargo-recovery economics — has reversed the historic default: reliquefaction is now the baseline on new carriers ≳174k m³, with fuel-gas use as a parallel demand sink rather than the primary BOG destination.

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
- **DFDE (dual-fuel diesel-electric)** — first-generation DF on the 2005-2015 carrier wave, four-stroke medium-speed gen-sets feeding electric propulsion; methane slip is materially higher than later two-stroke designs, and DFDE tonnage now sits in a retrofit-or-rebuild decision under tightening methane-intensity reporting.
- **Steam-turbine legacy** — pre-2010 carriers used steam plants that consumed BOG directly in the boilers; lower thermal efficiency drove the migration to dual-fuel diesel propulsion.

### ME-GI vs ME-GA vs DFDE vs ST comparison

| Engine family | Cycle | Injection pressure | Compressor side | Methane slip | Thermal efficiency | Best-fit BOG architecture |
|---|---|---|---|---|---|---|
| ME-GI | Diesel | ~300 bar | HPC (high-pressure) | Low | Highest | Reliquefaction + HPC fuel-gas |
| ME-GA / X-DF | Otto | ~6-16 bar | LP only | Moderate-Higher | Slightly lower than ME-GI | Reliquefaction + LP fuel-gas (simpler integration) |
| DFDE 4-stroke | Otto | LP | LP only | Highest of the DF families | Lower than two-stroke DF | Fuel-gas + GCU; reliquefaction retrofit candidate |
| Steam turbine | Rankine | Boiler burner | None | Effectively combusted, no slip | Lowest | Direct fuel-gas only |

- See [LNG Vapor Handling](./lng-vapor-handling.md) on methane-slip mitigation across these engine families.

## Worked-cases (operator precedent)

- **CMA CGM JACQUES SAADE (2020)** and the nine-vessel CMA CGM 23,000-TEU container-ship series — among the first deep-sea container-ships to adopt LNG dual-fuel propulsion at large scale; the BOG-handling envelope on these vessels reflects fuel-tank-driven BOG (Type C pressure tanks) rather than membrane-cargo BOG, illustrating that dual-fuel adoption now extends well beyond the LNG-cargo trade.
- **ME-GI fleet adoption** — the post-2015 Korean-yard newbuild wave (HHI, SHI, DSME) adopted ME-GI as the dominant high-efficiency choice for 174k-180k m³ carriers, with HPC + reliquefaction as a paired-default architecture.
- **Reliquefaction retrofits** — projects such as the Bonny-trade modernization wave and Q-Max/Q-Flex partial-reliquefaction retrofits demonstrate the lifecycle case for adding reliquefaction capacity to mid-life tonnage; the payback case is dominated by methane-intensity reporting and cargo-recovery rather than capex offset alone.
- **FSRU regas BOG profile differences** — FSRU service produces a distinct BOG profile relative to point-to-point carrier service: regas duty creates a steady cold-vapor stream that integrates naturally into the regas loop, while standby duty reverts to the static-storage envelope. This bimodal profile shapes reliquefaction sizing on FSRU specifications.

## BOR baseline and recent improvement trends

- **NO96 baseline (2000-vintage)** — typical natural BOR ~0.15 percent/day; first-generation insulation thickness and Invar primary barrier set the baseline.
- **Mark III standard (2005-2015)** — ~0.12-0.13 percent/day; thicker insulation panel, polyurethane foam containment.
- **Mark III Flex / Mark III Flex+ (post-2015)** — design BOR pushed below ~0.085-0.10 percent/day; foam thickness optimization and improved primary-barrier-side insulation.
- **NO96 GW (post-2017)** — Glasswool variant of NO96 reduces BOR toward ~0.10 percent/day with reduced insulation-degradation risk relative to perlite-filled box predecessors.
- **Mark V (recent)** — design BOR target near or below 0.07 percent/day; a doubling-of-fuel-savings claim relative to the 2000-vintage NO96 baseline over a 20+ year asset life.

This BOR-improvement trend ties directly into the reliquefaction-vs-fuel-gas economic balance: as natural BOG generation drops, reliquefaction sizing decreases, and the marginal capex case for reliquefaction becomes easier to clear at lower BOR levels because cargo-recovery value scales with the absolute BOG stream that would otherwise vent or burn.

## Methane-slip and methane-emission regulatory pressure

- **EU Methane Regulation (Regulation (EU) 2024/1787)** — adopted 2024; mandates leak-detection-and-repair (LDAR) programs, restricts routine venting and flaring, and applies methane-intensity reporting to LNG imports into the EU. Effective date for LNG-import provisions is staged through 2027-2030.
- **EPA Greenhouse Gas Reporting Program Subpart W** — petroleum and natural-gas systems methane-emissions reporting in the US; LNG export terminals report under the Subpart-W framework with a 2024 amendment that tightened venting and flaring measurement requirements.
- **IMO MEPC.346(78)** and successor MEPC instruments — develop the marine-side methane-slip framework, including ship-energy-efficiency and carbon-intensity-indicator (CII) treatment for gas-fueled ships; the methane-slip-correction factor for dual-fuel engines is a live MEPC topic.
- **Customer-and-financier pressure** — carbon-intensity (CI) tagging on a per-cargo basis is increasingly tied to LNG SPA pricing; methane intensity at the production, transport, and discharge points is now a first-order commercial variable.

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
