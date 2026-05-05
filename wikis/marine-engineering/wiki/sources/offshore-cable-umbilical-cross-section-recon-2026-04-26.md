---
title: "Subsea Cable, Umbilical, and Pipeline Cross-Section Reconnaissance"
tags: [source, offshore-wind, subsea, umbilical, pipeline, cable, cross-section]
sources:
  - guide-floating-offshore-wind-array-cable-core
  - guide-floating-offshore-wind-array-cable-outer
  - guide-floating-offshore-wind-export-cable-core
  - guide-floating-offshore-wind-export-cable-outer
  - prysmian-66kv-submarine-cable-systems
  - sut-subsea-umbilical-systems
  - prysmian-power-optical-umbilicals
  - dnv-st-f101
  - vallourec-line-pipe-coating-solutions
  - octal-concrete-weight-coating
added: 2026-04-26
last_updated: 2026-04-26
---

# Subsea Cable, Umbilical, and Pipeline Cross-Section Reconnaissance

## Source set

| Source | URL | Evidence captured |
|---|---|---|
| Guide to a Floating Offshore Wind Farm — Array cable core | https://guidetofloatingoffshorewind.com/guide/b-balance-of-plant/b-1-cables/b-1-1-array-cable/b-1-1-1-array-cable-core/ | Array cable core consists of conductor, screens, insulation, and sheathing; conductor may be stranded copper or aluminium; most subsea offshore-wind cables use XLPE, with EPR also used; typical 66 kV AC conductor area 150-1000 mm² and about 13 mm insulation. |
| Guide to a Floating Offshore Wind Farm — Array cable outer | https://guidetofloatingoffshorewind.com/guide/b-balance-of-plant/b-1-cables/b-1-1-array-cable/b-1-1-2-array-cable-outer/ | Three-core cable uses polypropylene filler/packing; polypropylene string bedding; helical metal armour wires; dynamic cables require two armour layers versus one for static cables; at least one fibre optic cable is integrated, typically 48 strands. |
| Guide to a Floating Offshore Wind Farm — Export cable core | https://guidetofloatingoffshorewind.com/guide/b-balance-of-plant/b-1-cables/b-1-2-export-cable/b-1-2-1-export-cable-core/ | Export cable core has same components as array cable core; HVAC/HVDC export cables typically use XLPE; typical 220 kV AC conductor area 800-2000 mm² with about 23 mm insulation; typical 320 kV DC conductor area 1000-2500 mm² with about 25 mm insulation. |
| Guide to a Floating Offshore Wind Farm — Export cable outer | https://guidetofloatingoffshorewind.com/guide/b-balance-of-plant/b-1-cables/b-1-2-export-cable/b-1-2-2-export-cable-outer/ | Export cable outer has same components/materials as array cable outer: armour wire, fibre optic cable, polypropylene yarn/serving. |
| Prysmian — 66 kV Submarine Cable Systems for Offshore Wind | https://www.prysmian.com/sites/default/files/atoms/files/66_kV_Submarine_Cable_Systems_for_Offshore_Wind.pdf | Typical 66 kV offshore wind design includes conductor, conductor screen, insulation screen, individual Cu-tape screen on each phase, fibre optic unit, armour bedding, armouring; qualification example includes 66 kV 3x800 mm² aluminium plus fibre optic. |
| SUT — Subsea Umbilical Systems | https://sut-us.org/pages_data/files/SUT-SAC-16-Umbilicals_637302480461195015.pdf | Umbilicals are bundles of tubes and cables; provide hydraulic power, electrical power and communications; examples include thermoplastic umbilicals, steel tube electro-hydraulic umbilicals, high-voltage hybrid umbilicals, fibre optics, power, hydraulic supply tubes, and dynamic-umbilical design concerns. |
| Prysmian — Power / Optical Umbilicals | https://www.prysmian.com/sites/default/files/business_markets/markets/downloads/datasheets/Power_-_Optical_Umbilicals.pdf | Power/optical umbilicals used for subsea power feed, control, distribution, communications; comprise low/medium-voltage power cores and optical core; use helically wound galvanized steel armour wire. |
| DNV-ST-F101 Submarine Pipeline Systems | https://www.dnv.com/energy/standards-guidelines/dnv-st-f101-submarine-pipeline-systems/ | Provides internationally acceptable framework for submarine pipeline systems through lifecycle phases; includes line pipe specification, material selection/corrosion control, and corrosion, insulation and weight coating specifications. |
| Vallourec — Line Pipe Coating Solutions | https://solutions.vallourec.com/oil-gas/plp/our-solutions/line-pipe-coating-solutions/ | Pipeline coatings include FBE, 3LPE/3LPP anti-corrosion systems; 3-layer systems include FBE base, adhesive co-polymer middle layer, and PE/PP outer layer; thermal insulation options include 5LPP and glass syntactic polypropylene. |
| Octal — Concrete Weight Coating Pipe | https://www.octalsteel.com/concrete-coated-pipe/ | Concrete weight coating is external concrete over steel pipe to provide negative buoyancy and mechanical protection; typical process starts with external anti-corrosion coating, reinforcement placement, concrete application, curing, and joint weighing; common concrete thickness range 25-200 mm. |

## Synthesis

The industry has four separable but adjacent cross-section modeling needs:

1. **Electrical submarine cables** for offshore wind: layered electrical insulation/armour systems with strong thermal/electrical coupling.
2. **Subsea umbilicals** for O&G controls and subsea power: packed bundles of tubes, hoses, electrical cores, and fibre optics with fatigue-sensitive dynamic variants.
3. **Rigid pipelines/flowlines**: pressure-containing steel pipe with external corrosion/insulation/concrete layers and discontinuities at field joints/anodes.
4. **Flexible pipes/risers**: multilayer mechanical systems where layer architecture governs collapse, bend, fatigue, and torsion.

## Immediate knowledge gaps

- Need vendor catalog exemplars with full dimensions/OD/mass/bend radius for array/export cables, steel tube umbilicals, thermoplastic umbilicals, and power umbilicals.
- Need standards map: API 17E/17J/17B, DNV-ST-F101, DNV-RP-F106/F102, IEC/CIGRE submarine cable references, and offshore wind cable design guidance.
- Need a computable schema and example JSON/YAML fixtures for section families and layers.

## Related pages

- [Subsea Cable and Umbilical Cross-Sections](../concepts/subsea-cable-umbilical-cross-sections.md)
- [Pipeline Integrity](../entities/pipeline-integrity.md)
- [Cathodic Protection System](../concepts/cathodic-protection-system.md)
