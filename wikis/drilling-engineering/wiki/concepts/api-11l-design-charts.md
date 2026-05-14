---
title: "API 11L Design Charts"
tags: [rod-pump, api-rp-11l, design-charts, pprl, mprl, gearbox-torque, sp-s, wrf-skr, fo-skr]
sources:
  - api-rp-11l
added: 2026-05-13
last_updated: 2026-05-13
---

# API 11L Design Charts

## Scope

The set of correlation charts in API RP 11L that predict the key sucker-rod-pumping design outputs (plunger stroke Sp, peak polished-rod load PPRL, minimum polished-rod load MPRL, peak gearbox torque PT, surface hydraulic horsepower) from three nondimensional input groups. The 11L charts are the foundational sizing tool for conventional Class I beam-pumping units.

## Three nondimensional input groups

- **Sp / S** — ratio of plunger stroke to polished-rod stroke. Accounts for sucker-rod string compliance; below 1.0 because the rod string stretches.
- **Wrf / Skr** — weight of fluid on the plunger divided by static rod-string stretch. Captures fluid load relative to rod compliance.
- **Fo / Skr** — fluid load divided by static rod-string stretch. Captures peak dynamic loading.

## Predicted outputs

- **Plunger stroke** (Sp) — actual plunger displacement, less than polished-rod stroke S because of rod stretch
- **Peak polished-rod load (PPRL)** — maximum load on polished rod during upstroke. Sets pumping-unit rating.
- **Minimum polished-rod load (MPRL)** — minimum load during downstroke. Sometimes negative (rods buckle) for over-pumped wells.
- **Peak gearbox torque (PT)** — maximum gearbox torque demand. Sets gearbox rating.
- **Hydraulic horsepower at the surface** — surface power required to drive the system.

## Validity envelope

The 11L correlations assume:
- Conventional Class I geometry beam-pumping unit
- Reasonably regular operating conditions (no severe gas interference, fluid pound)
- Within the empirical-fit range of the original 11L data set

Outside this envelope — Mark II units, RotaFlex, hydraulic long-stroke, irregular operations — the **Gibbs wave-equation solver** (1963) is the modern method, implemented in commercial software (RodStar, QRod, SROD).

## Public references

- **API RP 11L** 4th Edition (June 1988) — [api-rp-11l.md](../standards/api-rp-11l.md). Primary authority for the charts.
- **Gibbs, S.G.** (1963), "Predicting the Behavior of Sucker Rod Pumping Systems," *Journal of Petroleum Technology* — the wave-equation foundation paper.
- **Takacs 2003** *Sucker-Rod Pumping Manual* — worked-example application of the 11L charts.

## Cross-references

- [Sucker-Rod Pumping Overview](sucker-rod-pumping-overview.md), [Pump Cards and Dynamometer](pump-cards-and-dynamometer.md), [Sucker Rods and Tapered Strings](sucker-rods-and-tapered-strings.md)
- [API RP 11L](../standards/api-rp-11l.md)
