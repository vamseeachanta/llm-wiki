---
title: "Pump Cards and Dynamometer Analysis"
tags: [rod-pump, pump-card, dynamometer, gas-interference, fluid-pound, gas-lock, parted-rods]
sources:
  - api-rp-11l
added: 2026-05-13
last_updated: 2026-05-13
---

# Pump Cards and Dynamometer Analysis

## Scope

The pump-card and dynamometer-card analysis technique for diagnosing sucker-rod-pumping system performance. Cards plot polished-rod load (surface card) or plunger-equivalent load (downhole card) vs position over one pumping cycle. Card shape diagnoses pump performance and reveals the four classic operational problems.

## Card types

- **Surface card (dynamometer card)** — measured directly at the polished rod. Load vs position. Read on the rig at the dynamometer.
- **Downhole card (pump card)** — computed from the surface card via the wave-equation transform (Gibbs 1963 method). Shows the load-vs-position relationship at the plunger after the rod-string dynamics have been deconvolved.

The downhole card is the diagnostic instrument because it shows what's happening at the pump regardless of rod-string transients.

## Ideal card shape

A well-operating rod pump produces a nearly-rectangular downhole card:

- Upstroke: load increases sharply at top-of-stroke (traveling-valve closes, plunger lifts column above)
- Top dead center: load = column weight on plunger
- Downstroke: load drops sharply at bottom (traveling-valve opens, plunger descends through fluid in barrel)
- Bottom dead center: load ≈ 0 (plunger free-falling through fluid)

## Classic failure-mode signatures

### Gas interference

Compressible-gas slip in the pump barrel produces a card with **rounded corners** instead of sharp transitions — the plunger compresses gas at top of stroke before the traveling-valve closes, then expands gas at bottom before standing-valve opens. Productivity loss proportional to the compressed-gas fraction.

### Fluid pound

Pump cavity not full of fluid at start of upstroke — plunger free-falls onto incomplete fluid column producing a sharp impact load and a card with a **delayed load-pickup at top of stroke**. Causes accelerated rod and pump damage; classic over-pumping symptom.

### Gas lock

Pump barrel completely filled with gas, not fluid — both valves close, no fluid moves. Card flattens out at zero load throughout. Requires stopping the unit and venting / bleeding.

### Parted rods

Sucker-rod string broken downhole. Surface card shows essentially zero load (only the polished-rod weight) and a static load pattern. Confirmed by pulling rods.

## Modern instrumentation

- Surface dynamometer — load cell on polished rod, position sensor on horsehead
- Wave-equation software (RodStar, QRod, SROD, Lufkin SAM) computes downhole cards in real time
- Automated card-pattern recognition triggers alarms for the failure modes above

## Public references

- **Gibbs, S.G.** (1963), "Predicting the Behavior of Sucker Rod Pumping Systems," JPT
- **Takacs 2003** *Sucker-Rod Pumping Manual* — dynamometer-card pattern catalog
- **Brown, K.E.** (1980) *The Technology of Artificial Lift Methods*, Vol 2a — pump-card analysis

## Cross-references

- [Sucker-Rod Pumping Overview](sucker-rod-pumping-overview.md), [API 11L Design Charts](api-11l-design-charts.md), [Sucker Rods and Tapered Strings](sucker-rods-and-tapered-strings.md), [Artificial-Lift Method Selection](artificial-lift-method-selection.md)
