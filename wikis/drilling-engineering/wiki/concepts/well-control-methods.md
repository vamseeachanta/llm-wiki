---
title: "Well-Control Methods"
tags: [well-control, drillers-method, wait-and-weight, concurrent-method, kick-killing]
sources:
  - api-rp-53
added: 2026-05-13
last_updated: 2026-05-13
---

# Well-Control Methods

## Scope

The kick-killing methods — procedures for circulating formation fluid (a kick) out of the wellbore and replacing it with heavier mud (kill mud) to restore pressure balance against the formation. Three classic methods plus variants are taught in WellCAP / IWCF certification.

## The three classic methods

### Driller's method

Two-circulation method. **First circulation** at original mud weight: circulate the kick (gas, brine, or oil influx) out of the wellbore via the choke. **Second circulation** at kill mud weight: replace wellbore contents with kill-weight mud.

- Pros: Simple, robust, well-understood
- Cons: Two full circulations; higher annular pressures during gas migration

### Wait-and-weight (engineer's) method

One-circulation method. Weight up the active mud to kill-weight BEFORE starting circulation. Circulate kill mud in while killing the kick simultaneously.

- Pros: One circulation; lower peak choke pressures; lower peak annular pressures
- Cons: Slower start (mud must be weighted before circulation); requires accurate kill-weight calculation

### Concurrent method

Hybrid — start circulating immediately at original weight, weight up the mud during circulation. Largely deprecated in favor of driller's or wait-and-weight; introduces variable kill-weight and harder pressure control.

## Kill-weight calculation

Kill mud weight = current mud weight + (shut-in drillpipe pressure / 0.052 / TVD)

where 0.052 converts ppg-feet to psi. SIDPP (shut-in drillpipe pressure) is measured at the standpipe gauge after shut-in.

## Kill sheet

Standard well-control practice uses a kill-sheet calculator (paper form or rig-floor software) that pre-computes:

- Kill mud weight
- Initial circulating pressure (ICP)
- Final circulating pressure (FCP)
- Pump-strokes-to-bit and pump-strokes-to-surface
- Pressure-step schedule for the wait-and-weight method

## Public references

- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md). Integrated BOP-system context.
- **IADC WellCAP curriculum** — well-control training canonical source
- **IWCF** — international well-control forum certification
- **Bourgoyne et al.** Ch. 4

## Cross-references

- [Kick Detection](kick-detection.md), [Shut-In Procedures](shut-in-procedures.md), [BOP Stack Overview](bop-stack-overview.md), [BOP Pressure Classes](bop-pressure-classes.md)
