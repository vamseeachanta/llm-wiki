---
title: "Atmospheric Corrosion"
slug: atmospheric-corrosion
domain: engineering-standards
tags:
  - atmospheric-corrosion
  - weathering
  - ISO-9223
  - cor-cor-c-x
  - marine-environment
  - time-of-wetness
  - coatings
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - ../standards/api-rp-571.md
---

# Atmospheric Corrosion

> Concept anchor for the external-corrosion damage family that occurs on metallic surfaces exposed to ambient air rather than to continuous immersion or to moisture trapped under insulation. Bidirectional with [api-rp-571](../standards/api-rp-571.md) (mechanism catalogue, §4 loss-of-thickness), [api-rp-574](../standards/api-rp-574.md) (in-service inspection — atmospheric CMLs), and [api-rp-583](../standards/api-rp-583.md) (the CUI-specialised RP, distinct but adjacent). Routes upstream from [damage-mechanism-screening](damage-mechanism-screening.md) and downstream into [corrosion-rate-measurement](corrosion-rate-measurement.md) and [risk-based-inspection](risk-based-inspection.md).

## What is atmospheric corrosion?

**Atmospheric corrosion** is **time-of-wetness-driven aqueous corrosion** of metal surfaces in air, accelerated by airborne contaminants (Cl⁻, SO2, NOx) and modulated by temperature, humidity, dust, and biocatalysis. It is distinguished from [corrosion-under-insulation](corrosion-under-insulation.md) (CUI — moisture trapped beneath thermal insulation, fireproofing, or weather-protection cladding) and from underground / seawater immersion service by the dominance of an **intermittent thin-film electrolyte** rather than a continuous bulk-electrolyte volume.

The corrosion cell forms each time the surface temperature drops below the dew point or rainfall / spray deposits a film. The film is electrochemically active for as long as it persists; once it evaporates the cell suspends. Year-on-year metal loss is therefore the integral of many short wet excursions, not a steady-state immersion rate. Two surfaces in identical air may corrode at very different rates because of micro-environmental differences (orientation, drainage, dust loading, shading) that change how long each holds water.

## ISO 9223 corrosivity categories

The International Organization for Standardization classifies atmospheric corrosivity in six categories on the basis of measured first-year mass loss of standard reference specimens. The numbers below are **first-year carbon-steel** rates per ISO 9223:2012 Annex C; subsequent-year rates are typically lower because the steady-state rust scale provides a partial barrier.

| Category | Environment | Typical 1st-year carbon-steel rate |
|---|---|---|
| **C1** | Indoor heated, low humidity | <1.3 μm/yr |
| **C2** | Indoor temperate / outdoor rural | 1.3–25 μm/yr |
| **C3** | Outdoor urban, mild industrial | 25–50 μm/yr |
| **C4** | Coastal mild + heavy industrial | 50–80 μm/yr |
| **C5** | Coastal heavy / industrial + chloride | 80–200 μm/yr |
| **CX** | Tropical-marine / extreme | >200 μm/yr (offshore splash zones) |

Project-specific assignment of an ISO 9223 category is made either by **on-site measurement** (1-year reference-specimen exposure per ISO 9226, or chloride / SO2 deposition surveys per ISO 9225) or by **classification-from-environment** using the Annex B environmental-parameter tables when measurements are impractical.

## Driver factors

The atmospheric corrosion rate is the product of how long the surface is wet and how aggressive the electrolyte is during each wetting. Five factors dominate:

- **Time of wetness (TOW)** — hours per year that the metal surface holds an electrolyte film, operationally defined as hours above ~80 % RH at the metal surface (a proxy for unsaturated-air condensation onto a contaminated surface). Coastal and tropical climates routinely hit **4 000 – 6 000 h/yr** (>50 % of total time); arid inland sites can be below 1 000 h/yr. ISO 9223 Annex B classifies TOW into five bands (τ1–τ5).
- **Salinity (Cl⁻ deposition)** — marine and coastal sites accumulate chloride aerosol on exposed surfaces. **ISO 9225 wet-candle and dry-plate methods** quantify deposition as **mg Cl⁻ /m²/day**; the resulting deposition class (S0–S3) feeds directly into the ISO 9223 corrosivity-category derivation. Chloride lowers the relative humidity at which the surface film deliquesces, lengthens TOW for any given climate, and breaks down passive films on stainless and aluminum.
- **SO2 / acid pollutants** — industrial-area corrosion accelerator. SO2 dissolves into the surface film and oxidises to sulfuric acid, dropping the local pH on the metal surface during each wet excursion ("acid rain on the metal scale"). ISO 9225 deposition class P0–P3 by mg SO2 /m²/day. Modern flue-gas desulphurisation has reduced SO2 in many regions; NOx and ammonia have grown as dominant pollutants in others, with their own deposition surveys.
- **Temperature** — corrosion-reaction kinetics roughly **double per ~10 °C** above the dew-point threshold. Temperature also governs the effective TOW (a surface that stays warm enough to evaporate dew is wet for fewer hours per year than a colder surface in the same atmosphere) and the morphology of the rust scale (warmer climates favour more protective rust phases on weathering steels).
- **Solar exposure + UV** — direct solar load degrades organic coatings (chalking, embrittlement, blister formation) on a different timescale from the base-metal corrosion below. UV does not directly drive metal loss, but it modulates effective TOW via thermal cycling (a sun-baked surface dries faster after rain) and accelerates the failure of the protective barrier the coating provides.

Secondary modifiers include **dust deposition** (dust holds moisture against the surface and traps deliquescent salts), **biocatalysis** (algal / fungal films change surface chemistry), and **orientation** (skyward-facing horizontal surfaces collect more pollutant deposit and water than vertical or downward-facing surfaces and corrode faster in the same atmosphere).

## Where it bites in O&G

Atmospheric corrosion is the dominant external damage mechanism on uninsulated equipment exposed to weather, and a non-trivial side-mechanism on insulated equipment whenever the jacket has lapsed. The table below names the typical credible-mechanism flag a refining or offshore screening pass should expect:

| Equipment | Mechanism focus |
|---|---|
| Storage tank exterior (shell + roof) | C3–C5; coatings + cathodic protection of bottom; soil-air interface band is a localised hot-spot |
| Refinery offsite piping (uninsulated) | C3–C5; coatings dominate; UT thickness mapping at coating-defect zones |
| Offshore topsides external | C5–CX; coatings + sacrificial-anode CP + 316L hardware; splash-zone is the worst band |
| Onshore pipeline ROW (above-grade segments) | C2–C3; coatings + ROW management; soil-air interface at riser daylighting is the inspection focus |
| LNG / cryogenic CUI-margin equipment | Wet-dry cycle on cold surface (CISCC risk on austenitic SS where insulation jacket has lapsed) |
| Pipe-rack supports | Crevice + galvanic between support and pipe shoe; dirt-trap geometry holds water |
| Anchor-bolt + foundation interface | Dirt-trap geometry + soil-side moisture wicking; classic atmospheric corrosion failure mode at base-plate / grout interface |

The offshore topsides splash zone deserves separate treatment in any defensible screening pass: it is simultaneously CX (or worse) atmospheric exposure, a wet-dry-cycled chloride concentrator, and a mechanically-loaded fatigue zone — none of the three damage stories on its own captures the actual integrity threat.

## Mitigation hierarchy

The mitigation menu is ordered roughly by cost-effectiveness and by the design phase at which each option is normally available:

- **Protective coatings** — the workhorse defence. Pipeline and offshore practice covers **3LPE** (3-layer polyethylene), **FBE** (fusion-bonded epoxy), **TSA** (thermal-sprayed aluminum, also sacrificial under coating holidays), and **epoxy** (zinc-rich primer + epoxy mid-coat + polyurethane top-coat for external structural steel). Coating selection is governed by the operating-T-vs-coating-class matrix in the relevant external-corrosion RP and by the corrosivity category from ISO 9223.
- **Galvanizing** — small-component blanket option (handrails, grating, ladders, structural fasteners). Hot-dip galvanized layers provide both barrier and sacrificial protection; rule-of-thumb life in C3 atmospheres is decades, dropping in C5 / CX to single-digit years.
- **Weathering steel (Corten)** — viable in intermediate corrosivity categories (C2–C3 with periodic full drying) where the protective-rust patina forms and stabilises. Corten is **not** recommended in chloride-laden marine atmospheres or in continuously-wet TOW-τ4 / τ5 microenvironments, where the patina either does not form or detaches.
- **CRA upgrade** — cost-driven last resort for components where coating + maintenance cannot hold the corrosion budget. 316L hardware on offshore topsides is a common compromise (stainless for the small bolts and fittings that drive disproportionate inspection cost, carbon steel for the bulk structure under coating + CP).
- **Cathodic protection** — for above-grade soil-air-interface segments and for the buried portions of partially-buried installations. ICCP for buried onshore pipelines, sacrificial-anode for tank bottoms and for splash-zone bands of offshore structures. See [cathodic-protection](cathodic-protection.md) for the design framework.
- **Insulation + jacketing** — used only where insulation is required for thermal reasons (energy conservation, personnel protection, process control); never installed for atmospheric-corrosion-control alone, because trapped moisture under a failed jacket is more aggressive than the atmospheric exposure it was meant to replace. See [corrosion-under-insulation](corrosion-under-insulation.md) for the cousin mechanism.
- **Maintenance** — recurring cleaning to remove salt and dust deposits, periodic re-painting of weathered coatings, prompt isolation of leaks (process leaks accelerate atmospheric corrosion of nearby equipment by depositing aggressive species), and active drainage of dirt-trap geometry (pipe shoes, base plates, structural channels).

## Inspection

Atmospheric-corrosion inspection is dominated by visual surveys, supplemented by quantitative thickness mapping and coating-condition rating against published photographic standards:

- **Visual surveys** — the front-line technique; covers full equipment surface and detects coating breakdown, blistering, rust staining, and dirt-trap accumulation. Output is a coating-condition rating per ISO 4628 or ASTM D610.
- **UT thickness mapping at coating-defect zones** — quantitative wall-loss measurement at flagged locations; CML practice per [api-rp-574](../standards/api-rp-574.md) for piping circuits, with CMLs preferentially placed at known coating-defect-prone geometries (welds, supports, low points).
- **Coating-condition surveys per ISO 4628 and ASTM D610** — standardised photographic-grade rating of rust, blistering, cracking, flaking, and chalking. Translates qualitative visual into a defensible numeric grade for re-coat planning.
- **Cathodic-protection effectiveness surveys** — for tank bottoms, soil-air-interface segments, and any component where CP is part of the atmospheric-corrosion control strategy. Structure-to-electrolyte potential surveys and current-density measurements; see [cathodic-protection](cathodic-protection.md).
- **Dust-deposition mapping** — at high-Cl⁻ sites (coastal refineries, offshore topsides, marine terminals), mg Cl⁻ /m²/day measurements per ISO 9225 inform whether the assigned ISO 9223 corrosivity category remains valid and whether re-coat intervals need to shorten.

## Standards

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Atmospheric corrosion is covered in §4 (loss-of-thickness mechanisms) with affected materials, critical factors, and inspection guidance. Anchor reference for refining-and-petrochem screening.
- [api-rp-574](../standards/api-rp-574.md) — *Inspection Practices for Piping System Components.* Source for CML practice and UT-thickness conventions on uninsulated atmospheric-exposure piping.
- [api-rp-583](../standards/api-rp-583.md) — *Corrosion Under Insulation and Fireproofing.* CUI-specialised standard, **distinct from but adjacent to** atmospheric corrosion; the wet-dry-cyclic mechanism family overlaps but the inspection and mitigation toolkits diverge. Cross-linked here so the screening engineer reaches the right RP for the actual exposure condition.

Adjacent international standards (not yet wiki-resolved; flagged for future-promotion candidates as the corpus grows):

- **ISO 9223** — *Corrosion of metals and alloys — Corrosivity of atmospheres — Classification, determination and estimation.* Defines the C1 – CX corrosivity-category framework that anchors this page. Future first-class standards page candidate.
- **ISO 9224** — *Corrosion of metals and alloys — Corrosivity of atmospheres — Guiding values for the corrosivity categories.* Companion to ISO 9223; provides long-term corrosion-rate guiding values per category. Future first-class standards page candidate.
- **ISO 9225** — *Corrosion of metals and alloys — Corrosivity of atmospheres — Measurement of environmental parameters affecting corrosivity of atmospheres.* TOW, chloride, and SO2 deposition measurement methods. Future first-class standards page candidate.
- **ISO 9226** — *Corrosion of metals and alloys — Corrosivity of atmospheres — Determination of corrosion rate of standard specimens for the evaluation of corrosivity.* Reference-specimen exposure and mass-loss procedure that calibrates the ISO 9223 categories. Future first-class standards page candidate.
- **ASTM G50** — *Standard Practice for Conducting Atmospheric Corrosion Tests on Metals.* US-side parallel to ISO 9226. Future first-class standards page candidate.
- **ASTM G84** — *Standard Practice for Measurement of Time-of-Wetness on Surfaces Exposed to Wetting Conditions as in Atmospheric Corrosion Testing.* Operational definition of TOW used to populate the ISO 9223 τ classes. Future first-class standards page candidate.
- **ASTM D610** — *Standard Practice for Evaluating Degree of Rusting on Painted Steel Surfaces.* Photographic-grade rust rating consumed by coating-condition surveys. Future first-class standards page candidate.
- **NACE / AMPP SP0198** — *Control of Corrosion Under Thermal Insulation and Fireproofing Materials.* CUI-adjacent guidance; covers the atmospheric / CUI boundary where insulation jackets fail and the underlying surface transitions from a CUI to an atmospheric-corrosion regime.

## Related concepts

- [cathodic-protection](cathodic-protection.md) — companion control technique for the buried and submerged portions of partially-buried installations and for tank bottoms; the boundary between atmospheric corrosion and CP-controlled corrosion is the soil-air interface, which is the worst location for both.
- [corrosion-rate-measurement](corrosion-rate-measurement.md) — the rate-of-loss metric that drives remaining-life calculations on atmospheric-exposure equipment; ISO 9223 first-year rates anchor the corrosion-rate band an operator should expect to see at CMLs in each corrosivity category.
- [damage-mechanism-screening](damage-mechanism-screening.md) — atmospheric corrosion is one of the loss-of-thickness mechanisms enumerated in API RP 571 §4; presence of uninsulated wetted-air-exposure surfaces is the screening trigger.
- [corrosion-under-insulation](corrosion-under-insulation.md) — sibling mechanism on the wet-dry-cyclic spectrum. CUI is atmospheric corrosion's cousin: same physics (intermittent thin-film electrolyte on a metallic surface), different geometry (insulation jacket holds the moisture against the surface for far longer than the open atmosphere does), and a different inspection toolkit (insulation-removal + UT or PEC / RT through the jacket, vs. direct visual + UT for atmospheric exposure).
- [galvanic-corrosion](galvanic-corrosion.md) — atmospheric exposure amplifies galvanic ranking by extending TOW around dissimilar-metal joints (bolted base-plates, dissimilar-metal flanges, support-shoe-to-pipe contacts). The galvanic series in marine atmospheric exposure is similar but not identical to the immersed-seawater series, and the area-ratio rule from [galvanic-corrosion](galvanic-corrosion.md) applies with the same force.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — parent source page for the API slice of the local catalog; anchors the API RP 571 §4, RP 574, and RP 583 references underpinning this concept page.
