---
title: "LNG Storage Tanks"
tags: [lng-projects, concept, storage, containment, cryogenic, full-containment, double-containment, single-containment, in-ground, membrane, rollover, rpt]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-boil-off-gas-management.md
  - ../concepts/lng-process-safety.md
  - ../concepts/lng-cargo-containment-systems.md
  - ../concepts/lng-vapor-handling.md
  - ../../standards/nfpa-59a.md
  - ../../standards/api-std-625.md
  - ../../standards/csa-z276.md
  - ../../standards/en-1473.md
---

# LNG Storage Tanks

## Scope

This page summarizes the canonical taxonomy of **onshore and terminal-side** LNG storage containment systems — the static cryogenic tanks that buffer cargo between marine arrivals and downstream sendout (regas, liquefaction-train feed, truck-loading). It is the **terminal-side counterpart** to [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md), which covers the ship-side containment families (Moss, GTT membrane, SPB) installed on LNG carriers and FLNG/FSRU hulls. Page is concept-level — it does **not** restate clause-level design rules, allowable-stress tables, foundation heave limits, exclusion-zone formulas, or vendor-specific construction details; those live in standards-page authoring under [NFPA 59A](../standards/nfpa-59a.md), [API Std 625](../standards/api-std-625.md), [CSA Z276](../standards/csa-z276.md), [EN 1473](../standards/en-1473.md), and EN 14620.

## Why storage tank choice matters

- **Plot-plan and exclusion-zone footprint** — single, double, and full-containment tanks have materially different exclusion-zone footprints under NFPA 59A, EN 1473, and CSA Z276 deterministic methodology. Containment-category choice can be the deciding factor in whether a brownfield expansion fits its property line.
- **Permitting risk and schedule** — full-containment is the industry-default for new onshore terminals worldwide; double-containment and single-containment installations face escalating permitting friction and increased likelihood of regulator-imposed remediation or restriction at the next major-modification trigger.
- **Project capex and schedule envelope** — full-containment concrete outer tank construction is typically a 24–36 month critical-path activity that anchors terminal schedule. Containment choice and foundation type drive both capex and schedule float.
- **Inspection and life-extension regime** — different containment families have different in-service inspection burdens (EEMUA 147/159, API 625 chapters), affecting lifetime opex and overhaul scheduling.

## Onshore tank-type taxonomy

### Single-containment

- A single primary inner container holds the cryogenic liquid; the outer wall (often steel) is a weather and insulation enclosure that is **not** designed to hold liquid or vapor on a primary-tank failure.
- An external bund or impoundment area is required to contain a primary-tank release.
- **Status**: rarely used for new construction; surviving installations are pre-1990s and increasingly under regulatory pressure at major-modification trigger points.

### Double-containment

- Primary inner tank plus a structural outer wall capable of holding the liquid inventory on a primary-tank failure. The outer wall is **not** vapor-tight: vapor release in a primary-tank failure is to atmosphere or to a vent system.
- Reduces but does not eliminate the external bund requirement; smaller exclusion-zone footprint than single-containment but larger than full-containment for equivalent inventory.
- **Status**: occasionally selected for jurisdictions or sites where the cost-and-schedule premium of full-containment is not warranted; uncommon in modern major-project newbuilds.

### Full-containment

- Primary inner tank (typically 9 percent nickel steel — ASTM A553 — or alternatively post-tensioned concrete) plus a self-supporting concrete outer tank designed to hold both the liquid inventory **and** the vapor envelope on a primary-tank failure.
- Smallest exclusion-zone footprint of the above-grade families; the prevailing industry-default for new onshore terminals worldwide.
- Typical above-grade full-containment tank inventory: **135,000–200,000 m³** with a small population of larger 220,000–270,000 m³ designs at modern terminals.
- The dominant family in service at modern import, export, and peakshaving terminals.

### In-ground (sub-grade)

- Concrete tank set below grade level; the surrounding earth augments thermal isolation and (depending on design) provides additional containment in a release scenario.
- Favored in seismically active urban-adjacent sites (Japan, Korea, Taiwan), where setback distance is constrained and seismic mass advantages of the in-ground configuration matter.
- Smaller exclusion-zone footprint at grade than equivalent above-grade full-containment, at the cost of significantly higher excavation and dewatering capex.

### Membrane (terminal-side)

- Thin metallic membrane primary container backed by load-bearing insulation, with an external concrete outer barrier. Engineering analogous to the GTT NO96 / Mark III shipboard membrane families covered in [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md), adapted for static onshore service.
- Limited but growing onshore population — installed at peakshaving and small-scale terminals where membrane construction speed advantages relative to 9% Ni inner-tank welding apply.

## Capacity and design code mapping

- **Typical onshore inventory range**: 135,000–200,000 m³ per full-containment tank, with terminal-block totals up to ~1,000,000 m³ at large export sites (multiple tanks).
- **NFPA 59A** ([../standards/nfpa-59a.md](../standards/nfpa-59a.md)) — US-jurisdiction primary standard; governs containment-category selection, exclusion-zone calculation, and relief-system sizing.
- **API Std 625** ([../standards/api-std-625.md](../standards/api-std-625.md)) — Tank Systems for Refrigerated Liquefied Gas Storage; the umbrella tank-system standard whose containment-category taxonomy (single / double / full / membrane) this page mirrors.
- **CSA Z276** ([../standards/csa-z276.md](../standards/csa-z276.md)) — Canadian LNG production / storage / handling standard; Clause 5 governs onshore tank containment.
- **EN 1473** ([../standards/en-1473.md](../standards/en-1473.md)) — European harmonized standard for onshore LNG installations; Clause 7 delegates cryogenic tank design to EN 14620 (the EU parallel to API 625).
- **API 620 (Annex Q / R)** — alternative US route for low-temperature storage tanks under specific service conditions.

## Moss-vs-membrane terminal applications

- **Moss-type spherical tanks** are a *ship-side* family (see [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md)) and are not typical terminal-side construction. Onshore terminals have historically not used spherical Moss-type containment because the volumetric efficiency and footprint penalty of multiple spheres on a fixed plot are prohibitive vs. the full-containment cylindrical concrete tank.
- **Onshore membrane** is a niche choice where construction speed advantages outweigh the licensing royalty; the dominant onshore family remains 9% Ni inner-tank with concrete outer-tank full-containment construction.

## Rollover prevention

- **Rollover** — a stratified-tank density inversion in which a denser bottom layer suddenly mixes with a lighter top layer, releasing boil-off vapor in excess of the relief-system capacity (canonical 1971 La Spezia / Panigaglia incident).
- **Mitigations** are operational: routine density-and-composition monitoring, controlled top/bottom filling sequencing for cargoes of differing composition, tank-level recirculation pumping, and modern thermal-and-density profiling lances.
- **Relief sizing** is verified against the credible rollover-vapor generation rate, not just nominal boil-off; this is part of NFPA 59A and EN 1473 storage-tank design. See [LNG Process Safety](./lng-process-safety.md) for the rollover scenario in the broader release-scenario catalog.

## Tank instrumentation

- **Level / temperature / density (LTD) gauges** — multi-point instrumentation along the tank height to detect stratification before rollover conditions develop.
- **Primary-tank cooldown thermocouples** — embedded during construction to track inner-tank cooldown rate during commissioning (see [LNG Cooldown + Commissioning Procedures](./lng-cooldown-commissioning.md)) and to provide ongoing temperature distribution data in service.
- **Bottom-heating system** (for in-ground and many full-containment tanks) — electrical heating to prevent frost-heave of the foundation under prolonged cryogenic service.
- **Annular-space monitoring** — gas-detection in the perlite-insulated or vacuum annular space between inner and outer tanks; a primary leak indicator.
- **Pressure / vacuum relief valves** — see emergency-relief actuation in [LNG Vapor Handling](./lng-vapor-handling.md).

## Common failure modes

- **Rollover** — covered above; the canonical operational hazard.
- **Hydrate formation** — water ingress into cargo (from incoming feed gas or from atmospheric moisture during commissioning) can form solid methane hydrates that block instrumentation and small-bore piping; commissioning gas-up sequences explicitly target water removal.
- **Rapid Phase Transition (RPT)** — physical (non-combustion) explosion when LNG contacts water; less consequential for onshore terminals than for marine transfer (see [LNG Process Safety](./lng-process-safety.md) for the cross-cutting scenario).
- **Inner-tank brittle fracture** — cryogenic embrittlement of the surrounding hull, deck, or grade slab in a primary-tank-leak scenario; first-order design driver for material selection (9 percent nickel steel for above-grade primary tanks).
- **Foundation heave** — frost penetration through inadequate bottom-heating; can cause foundation distortion and inner-tank stress.

## Future trends

- **Larger single-tank capacity** — 220,000–270,000 m³ designs are now in service; further scale-up faces practical concrete-construction and 9% Ni weldment limits.
- **In-ground revival** — seismic and exclusion-zone advantages drive renewed interest in sub-grade tanks for select sites despite the capex premium.
- **Onshore membrane growth** — modular construction speed favors membrane for time-to-market projects in select markets.
- **Terminal-cold-energy recovery** — recovering cold energy at regas terminals via Rankine cycles or air-separation precooling sits at the boundary of storage-tank operation and process integration.
- **Hydrogen-carrier crossover** — many LNG storage-tank techniques are precedent-baseline for liquid-hydrogen storage; methodology is being adapted for the next-generation cryogenic-fuel terminal.

## Cross-references

- [LNG Cargo Containment Systems](./lng-cargo-containment-systems.md) — ship-side counterpart (Moss, GTT membrane, SPB).
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — operational vapor-return and reliquefaction interface; storage tanks are the primary onshore BOG source.
- [LNG Process Safety](./lng-process-safety.md) — rollover, RPT, pool fire, and exclusion-zone scenarios that drive containment-category selection.
- [LNG Vapor Handling](./lng-vapor-handling.md) — emergency relief, vent-mast, and flare interfaces with the storage-tank pressure boundary.
- [LNG Cooldown + Commissioning Procedures](./lng-cooldown-commissioning.md) — initial-cooldown and gas-up sequences for new and re-entered tanks.
