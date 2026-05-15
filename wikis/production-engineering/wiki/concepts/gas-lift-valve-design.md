---
title: "Gas Lift Valve Design"
tags: [gas-lift, valve, ipo, ppo, bellows, spring, dome-pressure]
sources:
  - api-spec-11v1
  - api-rp-11v2
added: 2026-05-14
last_updated: 2026-05-14
---

# Gas Lift Valve Design

## Scope

Engineering design of the gas-lift valve — the mechanical element that controls when and how much gas enters the tubing at each valve depth. Per [API Spec 11V1](../standards/api-spec-11v1.md), two primary actuation types (IPO and PPO), two primary force-source families (bellows-charged and spring-loaded), and several specialty variants.

## IPO vs PPO

- **Injection-Pressure-Operated (IPO)** — bellows or spring resists valve opening; rising casing-annulus (injection-side) pressure overcomes the resistance and opens the valve. Most common type; ~80%+ of installations.
- **Production-Pressure-Operated (PPO)** — bellows resists from below; rising tubing-side production pressure opens the valve. Used for specific unloading sequences and as backup; ~20% or less.

## Bellows vs spring

- **Bellows-charged** — sealed bellows pressurized with nitrogen sets the opening threshold. Temperature affects bellows pressure → temperature correction needed in design.
- **Spring-loaded** — mechanical spring sets opening threshold. Temperature-insensitive but more rigid response curve. Used in high-temperature service where bellows-gas charge would shift unpredictably.

## Dome pressure and spread

- **Dome pressure** (PD) — the nitrogen-charge pressure inside the bellows at downhole temperature. Sets the opening pressure threshold.
- **Spread** — the difference between opening and closing pressures. Spread × cycle frequency drives the gas-injection rate variability.

## Side-pocket vs tubing-retrievable mandrels

- **Side-pocket mandrel (SPM)** — mandrel built into tubing; valves are wireline-retrievable from the side pocket without pulling tubing. Standard for modern gas-lift installations.
- **Tubing-retrievable** — valves are part of the tubing string; require pulling tubing for valve change. Older installations and very-deep wells.

## Dummy valves

Blank "dummy" valves are installed in mandrels where active valves aren't yet needed (during initial completion). They're swapped for active valves later via wireline as the well's lift requirements evolve.

## Cross-references

- [Gas Lift Overview](gas-lift-overview.md), [Gas Lift Valve Spacing](gas-lift-valve-spacing.md), [Gas Lift Troubleshooting](gas-lift-troubleshooting.md)
- [API Spec 11V1](../standards/api-spec-11v1.md), [API RP 11V2](../standards/api-rp-11v2.md)

## Public references

- **Takacs 2005** *Gas Lift Manual* — valve-design chapters
- **API RP 11V6** + **API Spec 11V1** + **API RP 11V2**
