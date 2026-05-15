---
title: "Power Fluid Systems"
tags: [power-fluid, jet-pump, hydraulic-piston-pump, surface-pump, separator, treatment]
added: 2026-05-14
last_updated: 2026-05-14
---

# Power Fluid Systems

## Scope

The surface-side power-fluid handling that supports both [jet pump](jet-pump.md) and [hydraulic piston pump](hydraulic-piston-pump.md) artificial-lift methods. Power fluid is the working fluid pumped from surface to drive the downhole pump — quality matters greatly because contamination damages nozzles (jet pump) or valves and seals (hydraulic piston pump).

## Power fluid sources

### Produced-fluid power fluid (most common)

- Use clean separated oil from the well's own production
- Loop: produced fluid → separator → cleanup (gun barrel / filter) → power-fluid surface pump → downhole → mixed with new produced fluid → back to separator
- Self-contained; no external supply needed

### Supplied power fluid (specialty)

- External clean fluid (often refined oil or specialty fluid) used as power fluid
- Higher cost but ensures power-fluid quality is independent of produced-fluid issues
- Used for asphaltene-bearing crude (where produced fluid would deposit in pumps) or sour service (where H2S in produced fluid attacks pump materials)

## Surface equipment

- **Cleanup tank / gun barrel** — gravity separator removes solids and water from produced fluid before power-fluid pump
- **Surface power-fluid pump** — high-pressure positive-displacement pump (typically multi-plex) delivering 3,000-5,000 psi to the downhole pump
- **Power-fluid manifold** — distributes to multiple wells on a battery
- **Production separator** — gas / oil / water 3-phase separator at the return-side
- **Surface storage** — oil + water tanks for off-take

## Power-fluid quality requirements

- **Solids**: typically < 5 ppm at pump intake (jet pump throat erodes faster with solids)
- **Water cut**: < 1% for jet pump (water-in-oil emulsion changes performance); < 5% for hydraulic piston pump
- **BS&W (basic sediment and water)**: combined < 5%
- **Pressure stability**: surface pump must deliver stable pressure within ± 5% for consistent downhole operation

## Common operational issues

- **Power-fluid contamination** → nozzle erosion (jet) or piston-valve damage (hydraulic-piston)
- **Surface pump cavitation** → downhole pump starvation → production loss
- **Manifold imbalance** across multi-well batteries → uneven well performance
- **Pressure fluctuation** from surge phenomena → downhole pump-cycling instability

## Cross-references

- [Jet Pump](jet-pump.md), [Hydraulic Piston Pump](hydraulic-piston-pump.md)
- [Artificial Lift Overview](artificial-lift-overview.md)

## Public references

- **Brown 1980** *Technology of Artificial Lift Methods* Vol 2b — power-fluid systems chapters
- **Lyons handbook** — artificial-lift section
- **API RP 11AR** — Recommended Practice for Care and Use of Subsurface Pumps (covers some power-fluid handling guidance for hydraulic-lift specifically) — verify revision at next ingest pass
