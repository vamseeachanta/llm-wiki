---
title: "LNG Cargo Containment Systems"
tags: [lng-projects, concept, cargo-containment, lng-carrier, moss, membrane, gtt, no96, mark-iii, spb, ihi, type-approval]
added: 2026-05-09
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../../standards/igc-code.md
  - ../../standards/sigtto-mooring-equipment.md
  - ./lng-storage-tanks.md
  - ./lng-marine-transfer-systems.md
  - ./lng-boil-off-gas-management.md
---

# LNG Cargo Containment Systems

## Scope

This page is the **ship-side** companion to [`lng-storage-tanks.md`](./lng-storage-tanks.md), which covers terminal/onshore tank containment families. Here the subject is the cryogenic cargo-tank technologies installed aboard LNG carriers (LNGCs) and on FLNG/FSRU hulls. Page is concept-level synthesis — type-approval clause text, allowable-stress tables, sloshing-pressure design coefficients, and licensee royalty schedules are out of scope and are reserved for standards-page or vendor-spec authoring routes.

## Why containment systems matter

- **Cargo capacity = ship capacity** — volumetric efficiency of the containment system directly determines newbuild economics, since the rest of the hull (engines, accommodations, ballast) scales sub-linearly with cargo volume.
- **Cryogenic-thermal challenge** — LNG at roughly minus 162 degrees C interfacing with ambient steel hull structure forces the design to manage thermal contraction, low-cycle fatigue at fill/discharge transitions, and sloshing-impact loads simultaneously; all three are first-order engineering constraints, not residual concerns.
- **Type-approval gating** — the IMO IGC Code requires flag-state administration plus class-society type approval before any new cargo-containment system can carry LNG commercially. New families (or material substitutions inside an existing family) face multi-year qualification programs before they are bookable on a newbuild order.

## Three dominant containment families

### Moss-type (spherical)

- Kvaerner-Moss design originated in Norway around 1971; roughly 120-plus ships built historically across MOSS Maritime, IHI, and Korean yards under license.
- Self-supporting aluminum-alloy spheres (typically 4 or 5 spheres per ship) coupled to the hull via an equatorial skirt with a bottom dome free to contract thermally.
- **Pros**: structurally independent (no continuous secondary barrier required); partial-load operation tolerated without sloshing-damage concerns; sphere geometry is simple to inspect and the void space between sphere and hold is gas-detectable.
- **Cons**: lower volumetric efficiency for a given hull (historically about 125,000-145,000 m^3 for 4-sphere designs versus 145,000-180,000 m^3 for membrane on equivalent hulls); the spheres protrude above deck, producing the distinctive Moss silhouette that adds air-draft and beam-stability complications under bridges and at terminals; weight penalty from the aluminum spheres plus skirt arrangement.
- Fleet share has trended down as newbuild orders shifted toward membrane; Moss remains in service across a still-substantial operational fleet.

### Membrane (GTT NO96, Mark III, Mark V)

- GTT (Gaztransport & Technigaz) primary-plus-secondary membrane systems dominate newbuild orders — roughly 70 percent of the modern LNGC fleet by count.
- **NO96**: dual Invar (36 percent nickel) primary and secondary membranes; perlite-filled plywood-box insulation. The mature design (originating around 1969 from the Gaztransport lineage) handles thermal contraction through the low coefficient of thermal expansion of Invar rather than through corrugation.
- **Mark III**: stainless-steel corrugated primary membrane with a Triplex composite secondary; reinforced-polyurethane-foam insulation. Corrugations accommodate thermal contraction directly via geometric flexure.
- **Mark V**: composite primary with a GTT-developed secondary; hybrid insulation arrangement; rolled out as a more recent option in the GTT product line.
- **Pros**: roughly 10-15 percent higher volumetric efficiency than Moss for a given hull length and beam; flat deck profile eases air-draft and bridge clearances; lower lightship weight than Moss for equivalent capacity.
- **Cons**: secondary barrier is mandatory under IGC Code for membrane systems; partial-load sloshing damage is a recognized risk, so operating practice prefers fully-loaded or fully-discharged transits; GTT licensing royalty applies on every newbuild as a fixed per-cubic-metre fee and is a real line item in shipyard quotations.
- **GTT royalty model**: GTT licenses the design, materials specification, and engineering support to shipyards for a fixed per-cubic-metre fee payable on each newbuild. Pricing is commercially negotiated; historical industry-press references have placed it in single-digit US-dollars per cubic metre, but current rates are between GTT and the licensee yards.

### SPB (Self-Supporting Prismatic Type B)

- IHI (Japan) prismatic independent-tank design; rectangular/prismatic geometry rather than spherical.
- Small fleet — examples include the Polar Eagle and Polar Pacific (1993) plus a handful of later builds; total fleet remains in the single digits.
- **Pros**: structural independence of Moss combined with flat-deck profile of membrane; partial-load tolerance without sloshing restrictions; better stability and air-draft than Moss for equivalent capacity.
- **Cons**: IHI-only license historically limited yard competition; small operational fleet means narrower pool of crews and operators with hands-on experience; construction cost premium relative to membrane on a per-cubic-metre basis has kept order book thin.

## IGC Code type-approval framework

- The IGC Code (see [`standards/igc-code.md`](../standards/igc-code.md)) classifies cargo-tank designs as **Type A**, **Type B**, or **Type C** with separate provisions for **integrated (membrane) tanks**.
- **Type A** — prismatic or spherical independent tanks designed primarily by classical structural-strength rules; full secondary barrier generally required, though specific reductions are permitted under defined conditions.
- **Type B** — independent tanks qualified by enhanced fatigue and crack-propagation analysis (leak-before-failure logic); partial secondary barrier permitted. Common in LPG service; rarer in modern LNG.
- **Type C** — pressure-vessel tanks qualified to pressure-vessel rules; no secondary barrier required. Dominant in small-scale and LNG-as-fuel bunker tanks; not typical in large LNGC cargo service.
- **Membrane systems** — governed by separate IGC Code provisions for integrated tanks rather than by the A/B/C numerical taxonomy; primary plus continuous secondary barrier is the foundational requirement.
- Practical mapping for LNG: Moss spheres and SPB prismatic tanks are independent designs qualified under Type A or Type B provisions depending on the analysis basis; GTT NO96/Mark III/Mark V are integrated membrane systems qualified under the membrane-tank provisions.

## Sloshing analysis

- Membrane systems are the family most sensitive to partial-load sloshing — wave-induced cargo motion in a partially filled tank produces high-amplitude impact loads on the membrane and insulation.
- **Operating envelope** restrictions emerged: depending on tank geometry and route, intermediate fill levels (commonly cited bands roughly between 10 percent and 70 percent of tank height) are restricted under sustained sea conditions, with project-specific qualification work needed to extend the envelope.
- Qualification programs are maintained jointly by GTT and the major class societies (DNV, ABS, BV, LR), combining model-tank testing, CFD, and full-scale instrumentation.

## Containment systems and LNG composition

- Standard LNGC containment is qualified for typical LNG compositions (predominantly methane, with limited heavier-hydrocarbon and nitrogen content within trade-specification limits). Heavy-LNG or rich-LNG cargoes require checks against the original design basis for density and heat-leak assumptions.
- **LNG-as-fuel containment** (bunker tanks on non-LNG ships and on dual-fuel newbuilds) more commonly uses Type C pressure-vessel tanks for small capacities; larger bunker tanks may adopt Type B independent-tank designs as capacity scales upward.

## Future trends

- **Incremental GTT refinements** — variants such as NO96 GW, Mark III Flex, and other generation-on-generation updates have targeted higher allowable boil-off-gas handling, reduced insulation thickness, and improved partial-load tolerance.
- **Hybrid arrangements** — small but growing for FLNG and small-scale LNG, where tank geometry must adapt to non-tanker hulls and to non-traditional cargo profiles.
- **Cryogenic composites** — primary or secondary membranes in composite materials remain at research and qualification stage; no commercial deployments yet at LNGC scale.
- **Hydrogen-carrier transition** — KHI's spherical Type B tank design for liquefied hydrogen on the Suiso Frontier (2022) demonstrated that Moss-type spherical IP transfers in principle to even colder cryogenic service (around minus 253 degrees C), with substantial materials and insulation rework.

## Cross-references

- [IGC Code](../standards/igc-code.md) — IMO ship-construction code that governs type approval for all the systems above.
- [SIGTTO Mooring Equipment Guidelines](../standards/sigtto-mooring-equipment.md) — terminal-side mooring companion for the LNGC vessels these containment systems live on.
- [LNG Storage Tanks](./lng-storage-tanks.md) — terminal/onshore containment-family companion (sibling page).
- [LNG Marine Transfer Systems](./lng-marine-transfer-systems.md) — transfer-side interface that connects shipboard cargo tanks to terminal storage.
- [LNG Boil-Off Gas Management](./lng-boil-off-gas-management.md) — BOG generation interface; containment-family choice influences daily BOR and downstream BOG-handling sizing.
- [LNG Process Safety](./lng-process-safety.md) — containment-failure release scenarios and consequence categories that drive type-approval scrutiny.
