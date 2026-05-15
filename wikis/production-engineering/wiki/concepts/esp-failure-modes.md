---
title: "ESP Failure Modes"
tags: [esp, failure-mode, cable-failure, gas-lock, sand-erosion, scale]
sources:
  - api-rp-11s
  - api-rp-11s1
added: 2026-05-14
last_updated: 2026-05-14
---

# ESP Failure Modes

## Scope

The recurring failure-mode catalog for ESP systems. Aggregated from operator fleet-trend analysis + [API RP 11S1](../standards/api-rp-11s1.md) teardown-report data + [API RP 11S](../standards/api-rp-11s.md) operations-and-troubleshooting guidance. Mean run-life is 18-36 months in good service; specific failure modes drive that distribution.

## Major failure modes

### Cable failures (~30-40% of pulls)

The dominant workover trigger. Subcategories:

- **Cable splice failure** — at the motor pigtail-to-power-cable junction; thermal cycling + flexure
- **Cable mechanical damage** — clamp galling against tubing; running-in damage; pulling damage
- **Cable insulation breakdown** — high-temperature service degrades EPDM / Teflon insulation; eventually shorts to ground
- **Cable connector failure** — wellhead penetrator electrical-feed-through degradation

### Motor failures

- **Insulation breakdown** — stator winding insulation degrades from sustained over-temperature
- **Bearing failure** — debris ingress past seal section; or sustained downthrust
- **Single-phasing** — one phase opens; motor over-currents the others → cascade failure

### Pump failures

- **Stage wear from solids** — sand erodes impeller / diffuser surfaces; head degrades
- **Stage scale deposition** — Ba/Sr/Ca sulfate or carbonate scale on rotating elements; clearances close; lock-up
- **Gas lock** — high free-gas-fraction at intake collapses head; pump cavitates; thrust loads spike

### Seal-section failures

- **Bag rupture** — well fluid into motor oil → electrical short
- **Labyrinth flooding** — well fluid through pressure-equalization path
- **Thrust-bearing overload** — pump downthrust exceeds bearing capacity

### Free-gas-handling failures

- **Cavitation** — net positive suction head (NPSHA) drops below pump NPSHR; impeller pitting
- **Gas separator failure** — rotary separator throws gas out the bypass; if bypass plugs, gas re-enters intake

## Operational signatures (from VFD telemetry)

- **Steady current** + steady voltage = healthy
- **Current draw rising over time** = scale deposition or solids accumulation
- **Current draw falling** = head loss from worn stages or gas
- **Current oscillation** = gas slugging through intake
- **Sudden current spike** = mechanical bind / parted shaft
- **Voltage imbalance phase-to-phase** = single-phasing onset

## Cross-references

- [Electric Submersible Pumps](electric-submersible-pumps.md), [ESP Sizing](esp-sizing.md), [ESP Vendor Archetypes](esp-vendor-archetypes.md)
- [API RP 11S](../standards/api-rp-11s.md), [API RP 11S1](../standards/api-rp-11s1.md), [API RP 11S7](../standards/api-rp-11s7.md)
- [Artificial Lift Overview](artificial-lift-overview.md)
