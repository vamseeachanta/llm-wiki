---
title: "ESP Sizing"
tags: [esp, sizing, tdh, ipr, motor-sizing, cable-sizing, vfd-selection]
sources:
  - api-rp-11s4
  - api-rp-11s2
added: 2026-05-14
last_updated: 2026-05-14
---

# ESP Sizing

## Scope

The iterative engineering workflow for sizing an ESP system — pump stages, motor, cable, VFD — to a specific well's inflow performance and target production rate. Sizing is **the most-leveraged design decision** for ESP economics: oversize → cycling inefficiency + accelerated wear; undersize → under-production + frequent workovers as reservoir declines.

## Workflow

### 1. Inflow performance

- **Productivity Index (PI)** = q / (P_r − P_wf) at target operating point
- **IPR curve** (Vogel for solution-gas drive, Fetkovich for tight reservoirs, composite for multi-phase)
- **Drawdown limit** — bubble-point or rock-mechanical-stability constraint sets minimum P_wf

### 2. Required total dynamic head (TDH)

TDH = vertical lift (well depth × fluid gradient) + friction loss in tubing + wellhead operating pressure − reservoir contribution to lift

The pump must produce TDH at the target rate.

### 3. Pump-stage count

From [API RP 11S2](../standards/api-rp-11s2.md) performance curves: each pump stage produces incremental head H_stage at design RPM. Required stages = TDH / H_stage. Typical stage counts 50-400 depending on depth and rate.

### 4. Motor sizing

Required motor horsepower = (TDH × rate × specific gravity) / (3960 × pump_efficiency) + service factor. Service factor typically 1.1-1.25.

Motor voltage / RPM selection from manufacturer catalog matched to pump stages × stage power.

### 5. Cable sizing

Cable cross-section (typically #6 to #1 AWG) sized to limit voltage drop to <5% from surface to motor at full-load current. Higher motor voltage → smaller cable → lower cost. Cable temperature rating must exceed motor-shroud-jacket-temperature service.

### 6. VFD selection

VFD kVA rating ≥ motor full-load kVA + headroom. Surface VFD also provides: soft-start (avoids inrush), real-time telemetry, frequency-adjustment for re-tune as reservoir declines.

## Re-sizing triggers (operational)

- Reservoir pressure decline shifts the IPR curve → new TDH and new rate target
- Water-cut increase shifts specific gravity → new motor sizing
- Free-gas at intake increases → gas separator + re-sizing
- The original pump operates outside its operating window → cavitation or downthrust signals re-sizing

## Public references

- **API RP 11S4** — [api-rp-11s4.md](../standards/api-rp-11s4.md). Sizing methodology.
- **API RP 11S2** — [api-rp-11s2.md](../standards/api-rp-11s2.md). Performance-curve testing.
- **Takacs 2017** ESP Manual — chapters 4-6 on sizing
- **Vogel (1968)** "Inflow Performance Relationship for Solution-Gas Drive Wells," JPT — IPR foundational paper

## Cross-references

- [Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Failure Modes](esp-failure-modes.md), [ESP Vendor Archetypes](esp-vendor-archetypes.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
