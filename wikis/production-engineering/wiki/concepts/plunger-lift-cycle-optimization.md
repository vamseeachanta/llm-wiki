---
title: "Plunger Lift Cycle Optimization"
tags: [plunger-lift, cycle-time, foss-gaul, surface-controller, glr]
added: 2026-05-14
last_updated: 2026-05-14
---

# Plunger Lift Cycle Optimization

## Scope

Optimizing plunger-lift cycle timing is the most-leveraged operational variable. Too-frequent cycling = plunger arrives at surface before liquid slug accumulates → low production efficiency. Too-infrequent cycling = liquid backs up onto formation, reducing inflow → lower total production. The Foss-Gaul method is the classic design framework; modern surface controllers automate the trade-off.

## The Foss-Gaul method (1965)

Foss and Gaul published the canonical plunger-lift design curve relating minimum required gas-liquid-ratio (GLR) to:
- Well depth
- Tubing size
- Plunger weight + friction
- Required production rate

The curve identifies the **minimum-GLR threshold** below which plunger lift fails (plunger doesn't reach surface). Operators design around this threshold with safety margin.

## Cycle-time tuning parameters

- **Shut-in time** — time the motor valve stays closed allowing tubing pressure to build. Longer = more plunger-driving pressure but more liquid accumulation.
- **Afterflow time** — time gas flows through choke after plunger arrival. Longer = more gas production but liquid re-accumulates.
- **Total cycle time** = shut-in + afterflow + plunger travel up + plunger drop

## Modern surface controllers

Programmable logic controllers (PLCs) or specialty plunger-lift controllers automate cycle tuning based on real-time sensors:

- **Tubing-head pressure** at end of shut-in
- **Plunger arrival detection** (magnetic sensor or pressure spike at surface)
- **Slug-arrival flow meter** signal
- **Casing-pressure trend**

Controllers adjust cycle timing automatically as well conditions evolve (reservoir depletion shifts GLR; controller adapts).

## Common operational issues

- **Plunger fails to surface** — GLR dropped below threshold; need to extend shut-in or switch lift method
- **Plunger arrives too fast** (slug undersized) — shorten shut-in
- **Plunger drop fails** — afterflow rate too high or plunger trapped at restriction
- **Plunger destruction** — extreme surface arrival; reduce gas rate or add lubricator dampers

## Cross-references

- [Plunger Lift](plunger-lift.md), [Plunger Lift Equipment](plunger-lift-equipment.md)
- [Artificial Lift Overview](artificial-lift-overview.md)

## Public references

- **Foss, D.L. & Gaul, R.B.** (1965), "Plunger Lift Performance Criteria with Operating Experience — Ventura Avenue Field," *Drilling and Production Practice*, API — the foundational reference
- **Brown 1977** Vol 1
- **SPE OnePetro** modern plunger-lift optimization literature
- **Vendor surface-controller documentation** (Ferguson Beauregard, Multi Products, Inc.) — consulted at install time
