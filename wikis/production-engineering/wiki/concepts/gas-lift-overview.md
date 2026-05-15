---
title: "Gas Lift Overview"
tags: [gas-lift, artificial-lift, continuous-flow, intermittent, valve-spacing, unloading]
sources:
  - api-rp-11v6
  - api-spec-11v1
added: 2026-05-14
last_updated: 2026-05-14
---

# Gas Lift Overview

## Scope

Gas lift uses high-pressure gas injected down the annulus, entering production tubing through gas-lift valves at controlled depths, to reduce the fluid column density. Reservoir pressure then lifts the lighter column to surface. **No moving downhole parts** — the valves themselves are the only mechanical elements, and they have long mean-time-to-failure compared with rod-string or ESP systems.

## Operating principle

1. High-pressure gas enters the casing-tubing annulus from surface compressor
2. Gas pressurizes annulus; tubing-fluid column is lighter
3. Gas-lift valves in side-pocket mandrels along the tubing string open in sequence (top to bottom) during **unloading**, then settle to a single operating valve in continuous-flow mode
4. Gas enters the tubing through the operating valve and mixes with produced fluid
5. The aerated column has lower bulk density → reservoir pressure pushes the column to surface

## Two operating modes

### Continuous-flow

- Steady gas injection through the operating valve
- Common for moderate-rate wells (200-10,000+ bbl/d)
- Operating valve at the deepest depth where the gas-pressure budget allows

### Intermittent

- Gas slug injected periodically; lifts a fluid slug; cycle repeats
- For low-rate wells (< 500 bbl/d) where continuous-flow can't sustain stable lift
- Cycle time per well typically 10-90 minutes

## Strengths and weaknesses

| Strength | Weakness |
|---|---|
| No moving downhole parts | Requires high-pressure gas source + surface compression |
| Excellent gas-handling tolerance (intake gas is a non-issue) | Lower efficiency at very-low rate |
| Works in deviated and horizontal wells | Gas-lift valve workovers when valves fail (less frequent than ESP) |
| Long mean-time-to-failure | Multipointing / heading instabilities require diagnosis |
| Depth effectively unlimited (subject to gas-pressure budget) | Operationally more sensitive than rod-pump for unstable wells |

## Cross-references

- [Gas Lift Valve Design](gas-lift-valve-design.md), [Gas Lift Valve Spacing](gas-lift-valve-spacing.md), [Gas Lift Troubleshooting](gas-lift-troubleshooting.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
- [API RP 11V6](../standards/api-rp-11v6.md), [API RP 11V2](../standards/api-rp-11v2.md), [API Spec 11V1](../standards/api-spec-11v1.md)
- Drilling-engineering cross-link: [Artificial-Lift Method Selection](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md)

## Public references

- **Takacs, Gabor** — *Gas Lift Manual*, PennWell 2005 (ISBN 0-87814-805-1)
- **Brown, Kermit E.** — *The Technology of Artificial Lift Methods*, Vol 1 PennWell 1977
- **API RP 11V6** — design reference
- **SPE OnePetro gas-lift literature**
