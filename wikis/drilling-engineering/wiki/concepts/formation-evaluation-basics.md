---
title: "Formation Evaluation Basics"
tags: [formation-evaluation, gamma-ray, resistivity, density, neutron, sonic, petrophysics]
sources:
  - api-rp-7l
added: 2026-05-13
last_updated: 2026-05-13
---

# Formation Evaluation Basics

## Scope

The fundamental open-hole / cased-hole logging measurements used to characterize subsurface formations — what each measurement responds to, how it's interpreted, and the basic petrophysical inferences it enables. Standard introductory taxonomy; detailed petrophysics belongs to a future reservoir-engineering domain.

## Standard log inventory

### Gamma ray (GR)

- Measures natural gamma-ray emission from formation
- High GR = shale (potassium-rich clay minerals)
- Low GR = clean sandstone or carbonate
- Used for lithology identification and shale-fraction estimation

### Resistivity

- Measures electrical resistivity of formation
- High resistivity = hydrocarbon-saturated or carbonate
- Low resistivity = water-saturated or shaly
- Multiple depths of investigation (shallow, medium, deep) distinguish flushed zone from virgin zone

### Bulk density (RHOB)

- Measures formation bulk density via gamma-gamma attenuation
- Combined with neutron porosity → porosity and gas-presence

### Neutron porosity (NPHI)

- Measures hydrogen-index of formation (responds to fluid in pore space)
- Combined with density → porosity and gas-effect

### Sonic (DT)

- Measures compressional / shear travel time
- Porosity (after lithology correction)
- Mechanical properties (acoustic impedance)

### Caliper

- Measures borehole diameter vs depth
- Identifies washout / breakout sections

## Basic interpretation workflow

1. **Lithology from GR** + density-neutron crossover → sandstone vs shale vs carbonate
2. **Porosity from density-neutron** (corrected for lithology)
3. **Water saturation from resistivity** (Archie equation: Sw = (a·Rw / (φ^m · Rt))^(1/n))
4. **Net pay** — depth interval where all four indicators (lithology, porosity, Sw, permeability proxy) meet operator cutoffs

## Scope-edge

Detailed petrophysical methodology (advanced log interpretation, NMR logs, image logs, multi-mineral analysis) is reservoir / petrophysics territory. This page is the drilling-engineering-side introduction enabling tool-selection and bid-evaluation decisions during well planning.

## Public references

- **Asquith & Krygowski** *Basic Well Log Analysis* AAPG Methods in Exploration No. 16 (ISBN 978-0-89181-667-9) — practitioner-canonical introductory reference
- **Bourgoyne et al.** Ch. 9
- **Schlumberger Log Interpretation Charts** (public reference) — quick-look interpretation

## Cross-references

- [Wireline Overview](wireline-overview.md), [MWD/LWD Overview](mwd-lwd-overview.md), [Well Intervention Methods](well-intervention-methods.md)
