---
title: "Mud Properties"
tags: [mud-property, density, rheology, fluid-loss, pv, yp, gel-strength, herschel-bulkley]
sources:
  - api-rp-13b-1
  - api-rp-13b-2
added: 2026-05-13
last_updated: 2026-05-13
---

# Mud Properties

## Scope

The operational properties of drilling mud measured on the rig floor — density, rheology, fluid loss, pH, content checks — and their roles in well control and hole cleaning.

## Core properties

### Density (mud weight)

- **What** — mass per volume of mud, in ppg (pounds per gallon) or sg
- **Why** — sets bottomhole hydrostatic pressure against formation pore pressure (kick prevention) and fracture pressure (lost-circulation prevention)
- **Measured by** — mud balance (rig floor)
- **Operating range** — 8.5 ppg (water) to 19+ ppg (heavy weighted mud)

### Rheology (viscosity model)

The mud-flow behavior under shear stress, measured by rotational rheometer (Fann 35 or equivalent). Three rheology models in common use:

- **Bingham plastic** — two parameters: plastic viscosity (PV) and yield point (YP). Simplest model.
- **Power-law** — flow-behavior index n and consistency index K. Better fit for shear-thinning muds.
- **Herschel-Bulkley** — three-parameter; combines yield-stress with power-law. Best fit for modern muds; standard in HPHT well design.

### Gel strength

10-second and 10-min static gel strength measured on the Fann 35. The mud's ability to suspend cuttings and weighting material when circulation stops; too high gels cause connection-pressure surges and lost circulation; too low gels cause barite sag.

### Fluid loss

- **API filtrate** — low-pressure low-temperature (100 psi room temp) filter-press volume in 30 min
- **HTHP filtrate** — high-pressure high-temperature (typically 300-400 °F, 500 psi differential)
- Controls filter-cake build-up and formation-fluid invasion

### pH and alkalinity

- pH 9-11 typical for WBM (alkaline for corrosion control + lignosulfonate function)
- OBM is alkaline (lime-buffered); pH not directly meaningful

## Why these matter for well design

Mud-weight selection drives kick-tolerance, kill-mud weight, and lost-circulation margin. Rheology drives ECD ([ecd-and-pressure-management.md](ecd-and-pressure-management.md)) and hole-cleaning capability ([hole-cleaning.md](hole-cleaning.md)). Fluid-loss control protects the formation against fluid invasion.

## Public references

- **API RP 13B-1** — [api-rp-13b-1.md](../standards/api-rp-13b-1.md), **API RP 13B-2** — [api-rp-13b-2.md](../standards/api-rp-13b-2.md)
- **Caenn et al.** 2017 — practitioner reference
- **Bourgoyne et al.** Ch. 2

## Cross-references

- [Drilling-Fluid Types](drilling-fluid-types.md), [Mud System Equipment](mud-system-equipment.md), [ECD and Pressure Management](ecd-and-pressure-management.md), [Hole Cleaning](hole-cleaning.md)
