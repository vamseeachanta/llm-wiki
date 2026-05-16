---
title: "Porosity"
tags: [porosity, rock-properties, formation-evaluation, core-analysis, log-analysis, petrophysics]
added: 2026-05-16
last_updated: 2026-05-16
sources:
  - tiab-donaldson-petrophysics-4e-2015
  - cosentino-integrated-reservoir-studies-2001
  - schlumberger-log-interpretation-charts
cross_links:
  - drilling-engineering/concepts/formation-evaluation-basics.md
  - drilling-engineering/concepts/mwd-lwd-overview.md
---

# Porosity

## Scope

**Porosity** (φ) is the foundational rock-storage property: the fraction of a rock's bulk volume that is occupied by void space (pore space). It is the upstream variable for every reservoir-engineering volumetric calculation: hydrocarbon-in-place, recovery factor, and producible-reserves estimation all start with porosity. This page is one of the two founding concept pages for the reservoir-engineering wiki's formation-evaluation foundation scope; the other is [permeability](permeability.md), which covers rock transport rather than rock storage.

## Definition

Porosity is defined as the void volume divided by the bulk volume of a rock sample. As a fraction it is dimensionless and ranges from 0 to 1; as a percentage it ranges from 0% to 100%. Petrophysical convention reports porosity both ways and the reader is expected to read units from context.

The **bulk volume** is the total external volume of the rock sample (matrix + pores). The **pore volume** is the void space within the bulk volume. The **grain volume** (or **matrix volume**) is the bulk volume minus the pore volume.

## Types

Porosity is decomposed along several orthogonal axes; a single reservoir interval typically has values reported on more than one axis.

### Total vs effective porosity

- **Total porosity** counts every void in the rock, including isolated (non-connected) pores and pores that cannot contribute to fluid flow.
- **Effective porosity** counts only the **connected** pore network — the pores that can hold producible fluid and through which fluid can move toward a wellbore.

Effective porosity is always less than or equal to total porosity. For clean sandstones the gap is small (a few porosity-percentage units). For shales, vuggy carbonates, and certain volcanic / diagenetically-altered rocks the gap can be very large; total porosity can be high while effective porosity is near zero (shales are the canonical example).

Effective porosity is the value used in reservoir volumetric calculations.

### Primary vs secondary porosity

- **Primary porosity** is the void space created at the time of sediment deposition — the original pore network between grains.
- **Secondary porosity** is created after deposition by diagenetic processes (dissolution, fracturing, dolomitization, etc.) that either enlarge or destroy primary pores.

Primary porosity is dominant in clastic reservoirs (sandstones); secondary porosity often dominates in carbonate reservoirs, where dissolution of soluble minerals and dolomitization can substantially modify (in either direction) the original pore network.

### Pore-network geometry

- **Intergranular porosity** — pore space between grains. Dominant in clean sandstones.
- **Intercrystalline porosity** — pore space between crystals. Common in crystalline carbonates and dolomites.
- **Fracture porosity** — pore space within fractures (natural or induced). Always a small fraction of bulk volume (typically < 1-2%) but can dominate flow because fractures concentrate connected void space along high-permeability planes.
- **Vug porosity** — pore space in dissolution cavities (vugs) larger than the surrounding grain or crystal framework. Common in carbonates. Vugs may or may not be connected to the surrounding pore network; isolated vugs contribute to total but not effective porosity.

Real reservoirs typically combine multiple geometries. Carbonate reservoirs in particular are often characterized as **dual-porosity** (matrix + fracture) or **triple-porosity** (matrix + fracture + vug) systems, and reservoir-engineering deliverability calculations for such reservoirs treat the geometries as coupled but distinct populations.

## Measurement

Porosity is measured by two broad approaches: **core analysis** (direct measurement on a rock sample retrieved from the well) and **log analysis** (indirect inference from a wireline or LWD tool response). Well-test analysis can also constrain porosity-thickness product (φh) but is more commonly used for permeability-thickness product (kh); see [permeability](permeability.md).

### Core analysis

Direct measurement on a physical sample. Considered the ground-truth reference against which log-derived porosity is calibrated. Two principal lab methods:

- **Helium pycnometry** — a known volume of helium gas is allowed to expand from a calibrated reference chamber into the chamber containing the rock sample. Helium is used because its small molecular size lets it access nearly all connected pores at room conditions, and because it does not adsorb appreciably on rock surfaces at room conditions. The measured pressure drop yields the grain volume; bulk volume is measured separately (calliper, immersion, or mercury displacement), and effective porosity follows. This is the modern industry standard for effective porosity on plugs.
- **Immersion (Archimedes) methods** — bulk volume is determined by buoyancy in a non-wetting fluid (typically mercury or, for routine work, a hydrocarbon that does not penetrate the pore network). Grain volume is determined by a follow-up measurement after the pore network is filled with a known fluid. Older method; less precise than helium pycnometry but still seen in legacy datasets.

Core porosity is typically reported as **routine core analysis** (effective porosity on cleaned, dried plugs at ambient conditions) or **special core analysis (SCAL)** (porosity at simulated reservoir net-confining stress, sometimes with formation-brine-saturated measurement). SCAL porosity is lower than routine porosity for stress-sensitive rocks because the pore network compresses under net-confining stress.

### Log analysis

Indirect inference from a wireline or LWD tool. The four principal porosity-sensitive log families:

- **Density log (RHOB)** — measures bulk density via gamma-ray scattering. Porosity is derived from the density equation φ_D = (ρ_matrix − ρ_bulk) / (ρ_matrix − ρ_fluid). Requires assumptions about matrix density (a function of lithology) and fluid density (a function of pore-fluid type). Density-log porosity is the most widely used wireline porosity in clastic reservoirs.
- **Neutron log (NPHI)** — measures hydrogen-atom concentration via neutron-thermalization counts. Calibrated to read porosity directly in a known lithology (typically limestone-equivalent in modern tools). Reads high in shales because of bound water in clay minerals; reads low in gas zones because of low hydrogen index of gas. The neutron-density crossplot exploits the opposite-direction gas response of the two tools to identify gas-bearing intervals.
- **Sonic log (DT)** — measures compressional-wave transit time. Porosity is derived by the Wyllie time-average equation or the Raymer-Hunt-Gardner equation (named here; structural relationships only — Wyllie is a linear interpolation between matrix transit time and fluid transit time; Raymer-Hunt-Gardner is an empirical alternative for unconsolidated formations). Sonic-derived porosity is less affected by borehole washout than density-derived porosity, making it the porosity log of choice in poor-borehole-quality wells.
- **Nuclear magnetic resonance (NMR)** log — measures relaxation-time distributions of hydrogen-nucleus spins in pore fluids. Unique among porosity logs in that NMR can decompose porosity into bound-water fraction (clay-bound + capillary-bound) and free-fluid fraction (movable hydrocarbon + free water). The free-fluid fraction is approximately effective porosity for clean rocks. NMR is the modern formation-evaluation tool for shaly sands and complex lithologies where density and neutron alone are insufficient.

Vendor wireline-service-company log-interpretation charts (Schlumberger *Log Interpretation Charts* is the historical industry reference; cited here by name with the access-discipline note that proprietary chart-curve transcriptions are NOT reproduced in this wiki) provide the cross-plotting templates used to combine multiple porosity-log responses for lithology-determined porosity.

## Typical ranges

Porosity values vary widely by lithology and by reservoir maturity (compaction, cementation, dissolution history). The following ranges are practitioner heuristics for *effective porosity* in the producing-interval depth window; they are NOT design values and should be replaced with site-specific core measurements when available.

| Lithology / reservoir class | Typical effective porosity range |
|---|---|
| Clean, well-sorted sandstone (shallow, lightly compacted) | 20 - 30% |
| Clean sandstone (moderate depth, moderate compaction) | 15 - 25% |
| Shaly sandstone | 5 - 25% (wide range, strongly shale-content-dependent) |
| Tight sandstone (deep, well-cemented) | 3 - 10% |
| Carbonates (limestone / dolomite, matrix porosity) | 1 - 30% (very wide range, dominated by diagenetic history) |
| Carbonates (fracture porosity, fractures only) | < 0.1 - 2% (bulk-volume basis) but locally much higher in fracture cores |
| Shales (effective porosity for hydrocarbon storage) | < 1 - 10% (often < 5% in mature source rocks; total porosity is higher) |

Carbonate ranges are deliberately wide because diagenesis (dolomitization, dissolution, cementation, recrystallization) can take a single original primary porosity and increase or decrease it by an order of magnitude over geologic time. Carbonate-reservoir characterization is correspondingly more dependent on integrated core-log-test analysis than clastic-reservoir characterization.

## Connectivity vs storage framing

Porosity quantifies **storage** (how much void space exists) but does NOT quantify **transport** (whether fluid in that void space can move toward a wellbore). The transport question is answered by [permeability](permeability.md), which depends not only on the amount of pore space but on how the pores are connected (pore-throat geometry, tortuosity, the size distribution of pore-connecting throats).

This is the fundamental scope-distinction at the foundation of formation evaluation:

- Two rocks can have identical porosity but order-of-magnitude-different permeability if their pore networks differ in connectivity.
- A vuggy carbonate with isolated vugs has high total porosity, lower effective porosity, and potentially very low permeability.
- A fractured tight sandstone has low matrix porosity but can have high effective producibility because the fractures provide high-permeability transport pathways connecting otherwise-isolated matrix porosity.

Reservoir-engineering volumetrics consume **effective porosity** (the storage capacity for movable hydrocarbon); reservoir-engineering deliverability consumes **permeability** (the transport rate). The hydrocarbon-in-place calculation uses effective porosity weighted by net pay thickness; the deliverability calculation uses kh (permeability-thickness product). Both inputs are required for any reserves-and-production forecast.

## Standards anchors

- **API RP 40 — Recommended Practices for Core Analysis** — the canonical practitioner reference for routine and special core analysis methodology. Covers sample handling, cleaning, drying, and the helium-pycnometry / immersion / SCAL porosity protocols. *Standards-page revision metadata to be verified at Wave-5 publish time*; default `revision: "verify-at-publish-time"` until confirmed. (See `wiki/standards/api-rp-40.md` when authored — not in this founding session.)

## Public references

Textbook citations below are cited by **name + ISBN only**. These textbooks are NOT ingested into this repository per the plan #40 license-fail-closed posture; readers consult their own licensed copies.

- **Tiab & Donaldson** — *Petrophysics: Theory and Practice of Measuring Reservoir Rock and Fluid Transport Properties*, 4th edition (Gulf Professional Publishing, 2015, ISBN 978-0-12-803188-9). Public textbook reference for the full core-and-log porosity methodology stack.
- **Cosentino** — *Integrated Reservoir Studies* (Editions Technip, 2001, ISBN 978-2-7108-0797-7). Public textbook reference for the integrated geological-petrophysical workflow that combines porosity, lithology, and saturation determinations.
- **Schlumberger** — *Log Interpretation Charts* (vendor publication, periodically updated). Industry-historical reference for cross-plotting templates used to combine multiple porosity-log responses. Cited by name with access-discipline note: proprietary chart-curve transcriptions are NOT reproduced in this wiki; readers consult their own licensed editions.

## Cross-references

Within this wiki:

- [Permeability](permeability.md) — the rock-transport counterpart to porosity; together they form the foundational rock-property pair this wiki is founded on.
- [Gamma-ray log interpretation](./gamma-ray-log-interpretation.md) — lithology indicator that feeds porosity-log matrix-density and matrix-transit-time assumptions. *(Wave 3 — page does not yet exist; placeholder forward-reference.)*
- [Formation tops](./formation-tops.md) — stratigraphic correlation surface that determines which intervals' porosity is integrated into net-pay volumetrics. *(Wave 3 — page does not yet exist; placeholder forward-reference.)*

To other wikis:

- [drilling-engineering/concepts/formation-evaluation-basics.md](../../../drilling-engineering/wiki/concepts/formation-evaluation-basics.md) — the well-construction-time framing of formation evaluation. Reservoir-engineering's porosity page is the reservoir-side complement: drilling-engineering covers "what does the LWD tool tell me while I'm still drilling and steering?"; this page covers "what does the openhole / LWD log tell me about the rock as a reservoir storage substrate?"
- [drilling-engineering/concepts/mwd-lwd-overview.md](../../../drilling-engineering/wiki/concepts/mwd-lwd-overview.md) — the sensor systems that produce the LWD-derived porosity measurements this page interprets.
