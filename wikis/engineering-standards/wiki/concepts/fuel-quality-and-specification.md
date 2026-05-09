---
title: "Fuel Quality and Specification"
slug: fuel-quality-and-specification
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - fuel-quality
  - gasoline
  - diesel
  - jet-fuel
  - heating-oil
  - biodiesel
  - refining
  - downstream
sources:
  - standards/astm-d86.md
  - standards/astm-d445.md
  - standards/astm-d975.md
  - standards/astm-d1655.md
---

# Fuel Quality and Specification

> First-class concept page anchoring the petroleum-products sub-domain inside this wiki. Cross-walks the property-method-spec lattice that governs commercial fuels in the U.S. and (via parallel ISO / EN / DEF STAN paths) internationally. This page is the petroleum-products counterpart to the metallurgy-and-corrosion concept set already present (sour service, brittle fracture, fitness-for-service); it is the trunk from which fuel-specific spec, biofuels, marine-bunker, and SAF concept pages will be added.

## What is fuel quality?

**Fuel quality** is the set of measurable physical, chemical, and combustion properties of a refined hydrocarbon (or hydrocarbon-equivalent) product that determine its fitness for an intended end-use — most commonly a reciprocating engine (gasoline, diesel, marine), a gas turbine (aviation, power generation), or a burner (heating oil, residual fuel). Quality is not a single number; it is a **multi-property envelope** binding ~10–15 measurements that together describe how the fuel will store, transport, atomise, ignite, burn, and leave deposits.

Quality is enforced through **commercial specifications** — fuel-grade documents that fix numeric limits per property and bind them to specific ASTM (or ISO / EN / DEF STAN) test methods. The spec is the contractual-and-regulatory surface between buyer and seller: a refinery cannot ship "diesel" to a U.S. on-road customer; it ships "ASTM D975 Grade No. 2-D S15", and every shipment carries a certificate of analysis showing measured values for every property in the spec slate. The principal U.S. specs are:

- **D4814** — automotive spark-ignition (gasoline)
- **D975** — diesel fuel oils (the master U.S. diesel spec)
- **D1655** — civil aviation turbine fuels (Jet A / Jet A-1)
- **D396** — fuel oils (heating fuel No. 1 through residual No. 6)
- **D6751** — neat biodiesel (B100)
- **D7467** — biodiesel blends (B6–B20)
- **D7566** — synthetic-blend aviation fuels (SAF redesignation pathway into D1655)

The spec layer is **what** must be true; the test-method layer (D86, D445, D93, D613, D5453, etc.) is **how** to measure it.

## The "13 properties" canon

Across the major fuel-spec lattice, a recurring core of properties governs nearly every grade. Different specs tighten, loosen, or omit individual rows, but the conceptual matrix is stable:

| Property | What it captures | Typical method |
|----------|------------------|-----------------|
| Volatility | Distillation curve, vapor pressure, flash point | D86, D5191 (DVPE), D93 (PMcc) |
| Density / API gravity | Mass per unit volume at 15 °C / 60 °F | D1298 (hydrometer), D4052 (digital) |
| Viscosity | Kinematic viscosity at 40 °C / 100 °C | D445, D7042 (Stabinger) |
| Cetane / Octane | Compression-ignition / spark-ignition combustion quality | D613 (cetane), D2700 (MON), D2699 (RON) |
| Sulfur | Total mass / ppm | D2622 (WD-XRF), D5453 (UV-fl), D4294 (ED-XRF) |
| Aromatics / Olefins / Saturates | Hydrocarbon-class composition | D3239, D1319 (FIA), D5186 (SFC) |
| Cold-flow | Pour, cloud, CFPP, freezing point | D97 (pour), D2500 (cloud), D6371 (CFPP), D2386/D5972 (freeze) |
| Stability | Oxidation, thermal | D525 (gasoline induction), D873 (jet potential), D3241 (jet thermal/JFTOT) |
| Cleanliness | Particulates, water, gum | D2709 (BS&W), D5304 (storage stability), D381 (existent gum) |
| Lubricity | Boundary-friction wear protection | D6079 (HFRR), D7688 |
| Acid number | Total / strong acid | D664, D974, D3242 (jet) |
| Specific energy | Heating value | D240 (bomb calorimeter), D4868 (calculated) |
| Other | Color, copper-strip corrosion | D156 (Saybolt color), D130 (Cu-strip) |

These 13 rows cover essentially every property cited by D4814 / D975 / D1655 / D396 / D6751 / D7467. Application-specific properties (smoke point and naphthalenes for jet, MMT and ethanol content for gasoline, flash and pour for residual fuel, FAME content for biodiesel-blend disclosure) are layered on top of this core.

## Why specs converge on D86 + D445

Two test methods underpin nearly every fuel spec in the catalog: **D86 (atmospheric distillation)** and **D445 (kinematic viscosity)**. The reason is mechanistic:

- **Volatility (the D86 distillation curve)** directly governs the front-end / mid-range / tail-end behaviour of the fuel in service. Front-end (T10) controls vapor pressure, vapor-lock, and cold-start; mid-range (T50) controls warm-up driveability and cetane behavior; tail-end (T90 / FBP) controls heavy-end deposit-formation potential, particulates, and injector fouling. Every reciprocating engine and burner is designed against an assumed boiling-range envelope, and D86 is the universal way to measure it.
- **Viscosity (D445)** directly governs **fuel-injection-system and atomisation behaviour**. Too low and the high-pressure pump loses lubrication and metering precision; too high and atomisation degrades, fuel-air mixing suffers, and emissions and deposits rise. For residual fuels (D396 No. 4 / 5 / 6) viscosity also governs **whether the fuel will pump at all** at storage and pre-heat temperatures.

Most other properties in a fuel spec are **application-specific tightenings or exclusions** of the same physics framework: cetane number is a combustion-kinetics tightening relevant only to compression-ignition fuels; freezing point is a cold-flow tightening relevant only to high-altitude jet fuel; smoke point is a particulate-tendency tightening relevant only to turbine combustion; HFRR lubricity is a boundary-friction tightening that became necessary only after hydrodesulfurization (ULSD) stripped natural lubricity components. The volatility-and-viscosity backbone is universal; everything else is layered.

## Specification family

The major commercial fuel specifications, grouped by end-use, with their cross-jurisdictional parallels:

- **Gasoline (motor / spark-ignition)** — **ASTM D4814** (U.S.), **EN 228** (EU), CARB Phase 3 (California overlay), Tier-3 EPA federal standards. Governs RON / MON / AKI octane, RVP / DVPE volatility class (Class A through Class E by season and region), distillation T10 / T50 / T90, sulfur (≤10 ppm Tier-3), oxygenate content (ethanol up to E10 / E15 / E85), olefins, aromatics, benzene, lead (banned).
- **Diesel (compression-ignition, on-road / off-road)** — **ASTM D975** (U.S., master spec), **EN 590** (EU), Indian BIS IS 1460. Governs flash, cloud, sulfur (S15 ULSD / S500 / S5000 tiers), distillation T90, viscosity, cetane number, carbon residue, lubricity (HFRR ≤ 520 µm post-ULSD).
- **Jet (civil aviation turbine)** — **ASTM D1655** (Jet A U.S. domestic, Jet A-1 international), **DEF STAN 91-091** (UK MoD international Jet A-1), **AFQRJOS** (IATA joint-operator quality bulletin reconciling D1655 ∪ DEF STAN 91-091), **ASTM D7566** (SAF blends redesignated into D1655).
- **Jet (military)** — **MIL-DTL-83133** (JP-8, U.S. Air Force kerosene with FSII / SDA / CI-LI additive package), **MIL-DTL-5624** (JP-5 high-flash naval / JP-4 legacy wide-cut, retired).
- **Heating / distillate fuel oil** — **ASTM D396** Grades No. 1 (light kerosene-range) and No. 2 (middle distillate, near-diesel) for residential / commercial heating burners.
- **Residual fuel oil (industrial / power / marine)** — **ASTM D396** Grades No. 4 / 5 / 6 (industrial heavy fuel oils) and **ISO 8217** (marine bunker fuels — distillate grades DMA / DMB / DMZ and residual grades RMA through RMK). Governs viscosity at 50 °C or 100 °C, density, sulfur (now MARPOL-bound at 0.5 % m/m globally per IMO 2020 outside ECAs, 0.1 % m/m inside ECAs), water, cat-fines (Al + Si), pour, flash, hydrogen sulfide, stability, total sediment.
- **Aviation gasoline (piston-engine)** — **ASTM D910** (100LL leaded avgas; long-running phase-out roadmap to unleaded G100UL / UL94 / UL91 alternatives).
- **Biodiesel** — **ASTM D6751** (neat B100 blend stock for middle-distillate fuels), **ASTM D7467** (B6–B20 blends), **EN 14214** (EU FAME spec). Governs methyl-ester purity, free and total glycerin, cold-soak filtration, oxidation stability (Rancimat), monoglycerides, water and sediment.

## Regulatory layer

Above the commercial-spec layer sits a regulatory layer that pins specific spec requirements (or imposes additional ones) by jurisdiction and end-use:

- **U.S. EPA 40 CFR Part 80** — federal fuel quality regulation. Subpart I mandates ULSD (15 ppm S) for on-highway diesel since 2006 and non-road diesel since 2010 (locking the D975 S15 tier into the regulated marketplace). Tier-3 motor-vehicle program (effective 2017–2025 phase-in) caps gasoline sulfur at 10 ppm annual average. Renewable Fuel Standard (RFS) sets blending obligations for biofuels.
- **California Code of Regulations Title 13 / CARB Phase 3** — California-specific gasoline and diesel additional requirements (lower aromatics, T90 caps, MTBE prohibition since 2003, Predictive Model compliance for refiner blends).
- **EU AFID (Alternative Fuels Infrastructure Directive)** and the **Fuel Quality Directive** — EU framework for fuel quality, biofuel mandates, and sulfur caps, downstream of EN 228 (gasoline) and EN 590 (diesel).
- **Tier-3 vehicle / fuel programs** — coupled OEM-and-fuel rule packages that tighten both vehicle emissions and the fuel quality the vehicles must run on (so SCR / DPF aftertreatment is not poisoned by sulfur).
- **IMO MARPOL Annex VI** — international marine sulfur cap. The **2020 global cap of 0.50 % m/m** (down from the historical 3.50 %) reshaped the residual-fuel and bunker market overnight; **0.10 % m/m** applies inside designated Emission Control Areas (ECAs: Baltic, North Sea, U.S. / Canada, U.S. Caribbean ECA). Compliance is met through low-sulfur fuel oil (LSFO / VLSFO / ULSFO), distillate marine gas oil, or scrubber-equipped vessels burning HSFO.
- **EU SAF mandate (ReFuelEU Aviation)** — sustainable-aviation-fuel blending obligation rising from 2 % in 2025 to 70 % by 2050 at EU airports; enforces D7566-compliant SAF blending into D1655 jet at refueling.

## Standards

First-class standards pages in this wiki referenced by this concept:

- [ASTM D86](../standards/astm-d86.md) — atmospheric distillation; the universal volatility method, called normatively by every U.S. downstream-fuel specification.
- [ASTM D445](../standards/astm-d445.md) — kinematic viscosity; the universal viscosity method, called normatively by D396, D975, D1655, D6751, D7467, SAE J300, and ISO 8217 (via ISO 3104).
- [ASTM D975](../standards/astm-d975.md) — diesel fuel oils; the master U.S. spec for compression-ignition fuels, defining the S15 / S500 / S5000 sulfur-tier lattice and the 1-D / 2-D / 4-D volatility classes.
- [ASTM D1655](../standards/astm-d1655.md) — civil aviation turbine fuels (Jet A / Jet A-1); the U.S.-civil-aviation jet spec, paired with DEF STAN 91-091 internationally and with D7566 for SAF redesignation.

Also referenced in this concept page but **not yet first-class standards pages** in this wiki — flagged as future-promotion candidates as the petroleum-products sub-domain matures:

- **ASTM D4814** — automotive spark-ignition engine fuel (gasoline).
- **ASTM D396** — fuel oils (heating fuel No. 1 / No. 2; residual fuel No. 4 / No. 5 / No. 6).
- **ASTM D6751** — biodiesel B100 blend stock.
- **ASTM D7467** — biodiesel blends B6–B20.
- **ASTM D7566** — aviation turbine fuel containing synthesised hydrocarbons (SAF).
- **ISO 8217** — marine fuels (distillate DMA / DMB / DMZ; residual RMA–RMK).
- **EN 590** — European diesel parallel to D975 (cetane ≥ 51, CFPP-graded cold-flow).
- **EN 228** — European gasoline parallel to D4814.
- **DEF STAN 91-091** — UK MoD international Jet A-1.
- **MIL-DTL-83133** — U.S. military JP-8.

## Related concepts

Forward-link to other concept pages that should anchor this sub-domain as it grows (these are placeholder wikilinks; targets to be created as the petroleum-products body of pages expands):

- [[refining-economics]] — how the volatility-cut and sulfur-tier choices on the spec side drive crude-slate selection, hydrotreater capacity, and refinery margin.
- [[fuel-stability]] — oxidation, thermal, and storage stability mechanisms (and the D525 / D873 / D3241 / D5304 method family that tracks them).
- [[engine-emissions-regulation]] — the coupled vehicle-and-fuel rule packages (Tier-3, Euro 6, MARPOL Annex VI, ReFuelEU) that pin spec limits to public-health and climate targets.

## Source materials

- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest underlying the D86 / D445 / D975 / D1655 standards pages this concept cross-walks. Identifies the highest-citation downstream-fuel specs (D86, D396, D445, D975, D1655) as the priority promotion candidates that anchor the petroleum-products sub-domain.
