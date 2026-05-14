---
title: "Tool Joints"
tags: [tool-joint, makeup-torque, nc-connection, pac-connection, double-shoulder, proprietary]
sources:
  - api-spec-5dp
  - api-rp-7g
added: 2026-05-13
last_updated: 2026-05-13
---

# Tool Joints

## Scope

The threaded connection elements at each end of a drill-pipe joint — pin and box — and the makeup-torque, sealing, and fatigue characteristics that govern their use. Tool joints are integral-upset on modern drill pipe (forged into the pipe end before threading); the connection thread profile is selected separately from the pipe body grade.

## API connection families

- **NC connections** — Numbered Connection family (NC-26, NC-31, NC-38, NC-40, NC-46, NC-50, NC-56, NC-77). The numeral encodes the makeup pitch diameter in tenths of an inch (NC-50 has 5.0" pitch diameter).
- **Internal Flush (IF)** — older family, largely superseded; appears in pre-1980s vintage equipment.
- **Full Hole (FH)** — older family; still common in fishing-tool and slim-hole work.
- **Slim Hole (SH)** — small-OD reduced-section connections for low-clearance applications.

## PAC and proprietary

Beyond the API connections, proprietary high-torque / high-fatigue connections dominate critical-well and ERD applications:

- **Grant Prideco XT** family — double-shoulder; widely used in deep / directional
- **Hydril Wedge** — wedge-thread profile
- **Hunting H-90** — high-torque proprietary
- **Vallourec VAM TOP DRILL** — premium connection

Proprietary connections are licensed; performance data is in the licensor's catalog (proprietary, not citable here verbatim).

## Makeup torque

Each connection has a recommended makeup-torque range — too low risks washout / leak; too high risks galling and stress overload. API RP 7G publishes makeup-torque tables for the API connection families; proprietary connections carry licensor-specified torques.

## Double-shoulder vs single-shoulder

Standard API connections engage the threads only (single-shoulder). Double-shoulder connections (most proprietary, plus some API XT- variants) add a secondary torque-bearing shoulder on the pin nose. The secondary shoulder increases torsional capacity ~30-60% and is the reason ERD and high-torque mud-motor applications prefer proprietary.

## Public references

- **API RP 7G** — [api-rp-7g.md](../standards/api-rp-7g.md). Makeup-torque tables for API connections.
- **API Spec 5DP** — [api-spec-5dp.md](../standards/api-spec-5dp.md). Tool-joint dimension requirements for API drill pipe.
- **API Spec 7-1** — [api-spec-7-1.md](../standards/api-spec-7-1.md). Subs and crossover connections.
- **Bourgoyne et al.** Chapter 6 — tool-joint geometry tabulations

## Cross-references

- [Drill Pipe](drill-pipe.md), [Drill-Stem Design](drill-stem-design.md), [Drill-Pipe Wear Classes](drill-pipe-wear-classes.md)
