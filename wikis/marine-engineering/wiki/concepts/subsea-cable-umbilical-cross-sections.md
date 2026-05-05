---
title: "Subsea Cable and Umbilical Cross-Sections"
tags: [offshore-wind, subsea, umbilical, cable, pipeline, cross-section, oil-and-gas]
sources:
  - offshore-cable-umbilical-cross-section-recon-2026-04-26
added: 2026-04-26
last_updated: 2026-04-26
---

# Subsea Cable and Umbilical Cross-Sections

This page captures the first-pass taxonomy for offshore wind and oil & gas cross-section families that should be modeled in `digitalmodel` and surfaced as engineering/GTM knowledge.

## Cross-section families

| Family | Typical industry use | Typical cross-section stack-up | Engineering parameters to capture |
|---|---|---|---|
| Offshore wind inter-array power cable | Turbine-to-turbine and turbine-to-offshore-substation links, commonly 33 kV or 66 kV AC | Three power cores. Each core has stranded Cu or Al conductor, conductor screen, XLPE or EPR insulation, insulation screen, metallic screen/sheath. Assembly has polypropylene filler/packing, fibre optic unit, armour bedding, helical armour wires, and outer serving/sheath. Dynamic versions generally need two armour layers rather than one. | voltage class, conductor material and area, insulation material/thickness, screen/sheath type, fibre count, armour material/layers, static vs dynamic duty, OD, mass, bend radius, axial/torsional stiffness, fatigue resistance |
| Offshore wind export cable — HVAC | Offshore substation to shore. Larger than array cables, often 132-275 kV AC depending project architecture | Same core architecture as array cable but with larger conductors and thicker insulation; generally three-core HVAC submarine cable plus fillers, fibre optic cable, armour, and serving/sheath. | voltage, conductor area, conductor losses, thermal rating, burial/soil thermal assumptions, sheath bonding, armour loss, route segmentation, landfall transition |
| Offshore wind export cable — HVDC | Long-distance/high-power export from offshore converter platform to shore converter | Usually single-core cable pair or pole arrangement, with conductor, screens, XLPE or mass-impregnated insulation, metallic sheath/screen, bedding, armour, outer serving. | polarity/return arrangement, conductor area, insulation system, sheath/screen, cable pair spacing, thermal rating, converter interface, repair/joint strategy |
| Oil & gas electro-hydraulic umbilical | Control and chemical delivery from host to subsea trees/manifolds | Bundle of steel tubes or thermoplastic hoses for hydraulic/chemical service, electrical power/signal cables, fibre optics, fillers, bedding, armour, and outer sheath. | tube/hose count and OD, pressure rating, fluid compatibility, electrical cores, fibre count, minimum bend radius, axial/torsional stiffness, crush resistance, fatigue duty, termination hardware |
| Oil & gas power/optical or hybrid umbilical | Subsea boosting, ESP, controls, all-electric subsea, long step-outs | Low/medium-voltage power cores plus optical core, sometimes with hydraulic/chemical tubes; galvanized steel armour wires, helically wound; customer-specific packing and installation constraints. | power core voltage/current, optical count, optional service tubes, thermal interactions, armour, installation tension, hang-off and dynamic section fatigue |
| Subsea rigid pipeline / flowline | Oil, gas, water injection, export, infield flowlines | Steel line pipe, optional internal lining/cladding or CRA, external anti-corrosion coating such as FBE/3LPE/3LPP, optional thermal insulation such as 5LPP/GSPP, optional concrete weight coating with reinforcement for on-bottom stability and mechanical protection; field joints and anode pads interrupt the regular stack-up. | OD, wall thickness, material grade, design pressure/temperature, corrosion allowance, insulation U-value, coating thickness/density, submerged weight, route stability, free-span/VIV interface, CP/anode interface |
| Flexible pipe / dynamic riser | Floating production, dynamic risers, jumpers where flexibility is required | Unbonded layered pipe concept: inner carcass/liner, pressure sheath, pressure armour, tensile armour, outer sheath. | bore, pressure rating, layer materials, collapse/pressure capacity, axial/torsional stiffness, bend radius, fatigue, annulus monitoring |

## Offshore wind assessment

- Array cables are now commonly moving from 33 kV toward 66 kV to reduce electrical losses and array strings, but the cross-section remains a three-core submarine power cable plus fibre optic and armour package.
- The Guide to a Floating Offshore Wind Farm reports typical 66 kV AC conductor cross-sectional areas in the 150-1000 mm² range with about 13 mm insulation; Prysmian's 66 kV example includes 3x800 mm² aluminium conductors and integrated optical element.
- Export cables scale up the same architecture: the Guide reports a typical 220 kV AC conductor range of 800-2000 mm² with about 23 mm insulation, and a 320 kV DC conductor range of 1000-2500 mm² with about 25 mm insulation.
- Static cables can use a single armour layer and polypropylene yarn serving; dynamic floating-wind cables usually require additional fatigue design and often two armour layers plus polymer outer sheath.

## Oil & gas assessment

- Umbilicals are not simply “small cables”; they are multi-service engineered bundles. A typical O&G umbilical mixes hydraulic/chemical tubes or hoses, electrical power/signal cables, and fibre optics under armour and sheath.
- Steel tube umbilicals are common for deepwater/high-pressure chemical or hydraulic service; thermoplastic umbilicals are common in smaller/lower-pressure or specific flexibility cases.
- Rigid pipelines and flowlines are pressure-containment structures first; their cross-sections are governed by pressure, collapse, corrosion, thermal insulation, coating, concrete-weight stability, and field-joint/anode details.
- Flexible pipes/risers are layered mechanical systems and should not be reduced to equivalent solid cylinders when fatigue, bend radius, collapse, or torsion are in scope.

## Modeling implications for digitalmodel

1. Use a **family + layer** schema, not one generic circular section. Each family needs ordered layers/components with material, geometry, density, stiffness, and service role.
2. Separate **electrical/thermal/hydraulic function** from **mechanical section properties**. Cable ampacity and umbilical hydraulic service are not the same as axial/bending/torsional stiffness.
3. Carry **static vs dynamic duty** explicitly. Dynamic offshore wind cables and floating production umbilicals need fatigue, hang-off, bend stiffener, and minimum-bend-radius metadata.
4. Include **manufacturing/installation descriptors**: armour layer count, lay angle, bedding/filler, outer sheath, field joint, anode pad, and concrete coating discontinuities.
5. Treat vendor catalog dimensions as reference examples, not universal defaults. The library should store provenance and allow project-specific overrides.

## Related pages

- [Pipeline Integrity](../entities/pipeline-integrity.md)
- [OrcaFlex VIV Analysis](../entities/orcaflex-viv-analysis.md)
- [Cathodic Protection System](cathodic-protection-system.md)
- [Subsea Cable, Umbilical, and Pipeline Cross-Section Reconnaissance](../sources/offshore-cable-umbilical-cross-section-recon-2026-04-26.md)
