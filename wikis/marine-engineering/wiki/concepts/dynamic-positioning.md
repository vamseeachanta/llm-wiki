---
title: "Dynamic Positioning"
tags: [dynamic-positioning, station-keeping, thrusters, controls, marine-operations]
sources:
  - committed-public-wiki-metadata
added: 2026-05-06
last_updated: 2026-05-06
---

# Dynamic Positioning

Dynamic positioning (DP) uses thrusters, power generation, sensors, control software, and operating procedures to maintain a vessel's position and heading without relying solely on passive mooring restraint.

## Engineering Role

DP is used where the vessel must maintain position during drilling, construction, inspection, intervention, loading, or other marine operations. Engineering work normally evaluates whether the vessel can hold position under the expected environment, what redundancy is needed, and what operational limits apply when equipment is degraded.

## System View

| Element | Purpose |
|---------|---------|
| Thrusters | Generate corrective force and moment |
| Power plant | Supplies thruster and control-system demand |
| Position references | Provide independent position measurements |
| Environmental sensors | Support feed-forward wind/current compensation and operator awareness |
| Control system | Allocates thrust and manages heading/position demand |
| Procedures | Define operating limits, degraded states, and emergency response |

## Public-Wiki Boundary

This page is a public overview and navigation point. It does not reproduce IMO, class-society, owner, or vendor DP rules, tables, equipment-class requirements, failure-mode matrices, or manuals.

## Related Pages

- [Station-Keeping](station-keeping.md)
- [Motions and Response Amplitude Operators](motions-rao.md)
- [OrcaFlex Solver](../../../engineering/wiki/entities/orcaflex-solver.md)
- [AQWA Solver](../../../engineering/wiki/entities/aqwa-solver.md)
- [LNG Berth Operability](lng-berth-operability.md)
