---
title: "Bit Hydraulics"
tags: [drill-bit, bit-hydraulics, hsi, jet-velocity, nozzle, mud-pump]
sources:
  - iadc-bit-classification
added: 2026-05-13
last_updated: 2026-05-13
---

# Bit Hydraulics

## Scope

The hydraulics of mud flow through the drill-bit nozzles — jet velocity, hydraulic horsepower per square inch (HSI), pressure drop, and the role of these in cleaning the bit face and lifting cuttings into the annulus. Bit hydraulics is the most-leveraged operational variable for ROP: a well-hydrauliced bit drills faster on the same WOB / RPM than a poorly-hydrauliced one.

## Key parameters

### Jet velocity (V_n)

Velocity of mud exiting the bit nozzles. Calculated from total flow rate and total nozzle flow area:

V_n = Q / A_t

where Q is flow rate and A_t is total nozzle area. Higher V_n = better bit-face cleaning. Typical V_n 250-450 ft/s for soft-medium formations.

### Hydraulic horsepower per square inch (HSI)

The most-cited bit-hydraulics metric:

HSI = HP_bit / A_bit

where HP_bit is hydraulic horsepower delivered through the bit nozzles and A_bit is the bit cross-section area. HSI guidelines (paraphrased from Bourgoyne):

- HSI > 5 hp/in² — well-cleaned in soft formations; supports high ROP
- HSI 2.5-5 hp/in² — moderate cleaning; routine operations
- HSI < 2.5 hp/in² — risk of bit-balling / cuttings accumulation; low ROP

### Nozzle sizing

Standard nozzle sizes are 1/32" increments (e.g., 12/32", 14/32", 16/32"). Bit body typically accepts 3 nozzles (tricone) or 4-7 nozzles (PDC). Equal-sized nozzles is the default; asymmetric sizing tunes cleaning to specific cutter regions.

### Pump constraint

Bit hydraulics is bounded by the rig's mud-pump capacity (max pressure × flow). Higher HSI requires more pump pressure or larger flow rate; both are bounded by rig specification (API Spec 7K covered mud-pump ratings — see [api-spec-7k](../standards/api-spec-7k.md)).

## Optimization

The standard optimization is to maximize HSI subject to:
- Mud-pump max pressure rating
- Mud-pump max flow rate
- Pressure-drop budget across surface lines, drill string, bit, and annulus
- Minimum annular velocity for hole cleaning

Modern software (NOV's MaxROP, Halliburton's Drillworks, etc.) solves this numerically. Hand calculations per the Bourgoyne formulas remain useful for first-cut estimates.

## Public references

- **Bourgoyne et al.** Chapter 5 — bit hydraulics and nozzle sizing
- **Mitchell & Miska** — bit-hydraulics treatment
- **API Spec 7K** — [api-spec-7k.md](../standards/api-spec-7k.md) — mud-pump rating context

## Cross-references

- [Bit Selection](bit-selection.md), [Drill-Bit Types](drill-bit-types.md)
- [IADC Roller-Cone Code](iadc-roller-cone-code.md), [IADC PDC Code](iadc-pdc-code.md)
- [API Spec 7K](../standards/api-spec-7k.md)
