---
title: "Drill-Stem Design"
tags: [drill-stem, tension, torque, collapse, bending, neutral-point, margin-of-overpull, buckling]
sources:
  - api-rp-7g
  - api-spec-5dp
added: 2026-05-13
last_updated: 2026-05-13
---

# Drill-Stem Design

## Scope

Engineering design of the drill stem — selecting drill-pipe grade, weight, and wall thickness to meet four load criteria (tension, torque, collapse, bending) with adequate design factors and margins of overpull. Parallel discipline to [casing-program-design.md](casing-program-design.md) but for the rotating drill stem instead of the cemented casing.

## Four design loads

1. **Tension** — drill-pipe weight in mud (buoyant) plus drill-collar / BHA weight below, plus surface overpull during stuck-pipe or fishing operations. Maximum at the surface end of the string.
2. **Torque** — rotary torque from the surface drive plus friction torque accumulated along the well path. Maximum at the surface end during rotating; significant at directional dogleg locations.
3. **Collapse** — when drill pipe is partially evacuated (e.g., during a riserless mud-recovery operation, or a kick where lighter formation fluid replaces mud column). External hydrostatic pressure tries to crush the pipe.
4. **Bending** — dogleg-severity-induced bending stress, additive to axial tension. Critical at dogleg landings and at the top of stiff BHA elements.

## Neutral point

The neutral point is the depth along the drill string where axial load transitions from tension (above) to compression (below). Drill pipe operated above the neutral point is in tension and stable; drill pipe operated below it is in compression and may buckle. Standard practice is to keep all drill pipe **above** the neutral point — compressive WOB is supplied by drill collars (heavier-wall elements designed for compression).

## Margin of overpull (MOP)

Difference between tensile-yield capacity at the top of the string and actual hanging weight in mud. Standard rig-floor rule of thumb: maintain ≥ 100,000 lbf MOP during routine drilling, more in critical-well or sticking-prone hole sections.

## Combined-load envelope

The von Mises stress combines tensile, torsional, and pressure-induced stresses into an equivalent stress compared against material yield. API RP 7G provides the combined-load envelope; modern torque-and-drag software (Landmark WellPlan, Halliburton ServicePoint, Drillbench) implements it numerically.

## Public references

- **API RP 7G** — [api-rp-7g.md](../standards/api-rp-7g.md). Design-limits framework.
- **API Spec 5DP** — [api-spec-5dp.md](../standards/api-spec-5dp.md). Material-properties source.
- **Bourgoyne et al.** Chapter 6 — drill-string design
- **Mitchell & Miska** — drill-string mechanics chapter
- **Robello Samuel** — *Drilling Engineering*, PennWell (ISBN 978-1-59370-100-6) — drill-string design depth

## Cross-references

- [Drill Pipe](drill-pipe.md), [Tool Joints](tool-joints.md), [Drill-Pipe Wear Classes](drill-pipe-wear-classes.md)
- Cross-domain to naval-architecture: drillship / MODU motion-compensator interaction with drill-stem dynamic loads is a coupling not covered here; see [`naval-architecture/concepts/seakeeping.md`](../../../naval-architecture/wiki/concepts/seakeeping.md) for the ship-motion side
