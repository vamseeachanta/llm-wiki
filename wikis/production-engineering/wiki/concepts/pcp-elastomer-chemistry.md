---
title: "PCP Elastomer Chemistry"
tags: [pcp, elastomer, nbr, hnbr, fkm, aromatic-content, swelling]
sources:
  - api-spec-11w
added: 2026-05-14
last_updated: 2026-05-14
---

# PCP Elastomer Chemistry

## Scope

The elastomer stator is the **load-bearing reliability element** of a PCP system — it forms one half of the sealed cavity that pumps fluid. Elastomer-fluid compatibility determines whether the stator swells, hardens, softens, or chemically degrades in service. Selecting the right elastomer family for the produced fluid is the most-leveraged PCP design decision.

## Major elastomer families

### NBR — Nitrile Butadiene Rubber

- Most common general-purpose elastomer
- Handles most water-cuts and low-aromatic oils
- Cost-effective; broad service envelope
- **Limitation**: aromatic hydrocarbons (BTEX) cause swelling

### HNBR — Hydrogenated Nitrile Butadiene Rubber

- Hydrogenated NBR; higher temperature rating + better chemical resistance
- Standard for higher-aromatic-content fluids
- Higher cost than NBR; longer service life in tough environments

### FKM (Viton) — Fluoroelastomer

- Highest chemical resistance among standard elastomers
- Handles high-aromatic-content, H2S, CO2, methanol
- Highest cost; specialty applications

### EPDM — Ethylene Propylene Diene Monomer

- Excellent steam and hot-water resistance
- Limited oil resistance — used in steam-flood produced water service
- Rare for general PCP service

## Compatibility framework

Selection rule: identify the dominant fluid challenge (aromatic content, water cut, H2S, CO2, temperature, sand content), then map to the elastomer family with the best service record. Vendors publish compatibility charts; operator should verify against produced-fluid analysis.

## Common failure modes

- **Swelling** — elastomer absorbs hydrocarbons; cavities tighten; rotor binds
- **Hardening** — chemical aging or high-temperature reduces elasticity; cavity gap opens; flow loss
- **Softening** — chemical degradation reduces interference; flow loss; eventual extrusion
- **Chunking** — physical erosion from solids; cavity geometry destroyed

## Cross-references

- [Progressing-Cavity Pumps](progressing-cavity-pumps.md), [PCP Heavy-Oil Application](pcp-heavy-oil-application.md)
- [API Spec 11W](../standards/api-spec-11w.md)

## Public references

- **Brown 1980** *Technology of Artificial Lift Methods* Vol 2b
- **SPE OnePetro** elastomer-failure papers
- **Vendor compatibility charts** (NOV, Weatherford, Halliburton ALS) — proprietary, consulted at design time but not transcribed
