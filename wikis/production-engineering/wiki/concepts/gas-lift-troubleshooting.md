---
title: "Gas Lift Troubleshooting"
tags: [gas-lift, troubleshooting, multipointing, heading, instability, valve-failure]
sources:
  - api-rp-11v6
added: 2026-05-14
last_updated: 2026-05-14
---

# Gas Lift Troubleshooting

## Scope

The operational diagnostic catalog for gas-lift wells. Gas lift is operationally more sensitive than rod pump or ESP for unstable wells — multipointing, heading, valve failures, and surface-pressure variability are the recurring trouble modes. Diagnosis usually starts with surface gauges + pressure / temperature surveys.

## Multipointing

Two or more valves open simultaneously when only the operating valve should be open. Causes inefficient gas use (gas enters at higher depth than needed) and unstable production. Signs:

- Wellhead pressure cycling
- Production rate oscillation
- Higher gas-injection-rate than design

Fix: redesign valve depths and pressures, or change-out problematic valves via wireline.

## Heading

Production cycles between high-flow and low-flow states with stable injection. Caused by fluid-level oscillation between valves. Signs:

- Tubing-head pressure (THP) cycling between 100-200 psi peaks
- Visible production-rate variation at separator

Fix: choke adjustment, gas-rate trim, valve-pressure adjustment.

## Valve failures

- **Valve stuck open** — gas continuously bypasses; high gas-injection rate vs production rate
- **Valve stuck closed** — well moves operating point shallower (lower production), or worse, stops producing
- **Valve seat leak** — slow loss of gas-pressure containment

Diagnosis via wireline tags (mechanical position-confirm) or flowing pressure surveys.

## Surface-pressure instability

Compressor variability, suction-pressure drift, manifold imbalance across a multi-well battery — all surface causes that manifest as downhole instability. Fix at the surface: tune compressor; balance manifold.

## Diagnostic instrumentation

- **Surface gauges** — THP, casing pressure, gas-injection rate, production rate
- **Flowing pressure survey** — wireline pressure tool measuring annulus pressure vs depth; identifies which valve is operating
- **Memory gauges** — long-duration pressure recording for post-pull analysis
- **Permanent downhole gauge (PDHG)** — real-time downhole pressure / temperature (specialty installation)

## Cross-references

- [Gas Lift Overview](gas-lift-overview.md), [Gas Lift Valve Design](gas-lift-valve-design.md), [Gas Lift Valve Spacing](gas-lift-valve-spacing.md)
- [API RP 11V6](../standards/api-rp-11v6.md)

## Public references

- **Takacs 2005** *Gas Lift Manual* — troubleshooting chapter
- **Brown 1977** Vol 1 — diagnostic methodology
- **SPE OnePetro** gas-lift-instability literature
