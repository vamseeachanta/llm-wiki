---
title: "Directional Drilling"
tags: [directional, horizontal-well, build-rate, kick-off, dogleg-severity, anti-collision, survey]
sources:
  - api-rp-7g
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Directional Drilling

## Scope

Drilling a non-vertical well — building inclination from vertical, holding inclination through a target, and optionally dropping back. Directional drilling enables wells that reach targets offset laterally from surface location, horizontal wells in thin reservoirs, multilateral wells from a single surface, and pad-drilling fleets of wells from a common pad.

## Standard well profile shapes

### Build-and-hold (J-profile)

- Vertical → kick-off depth → build inclination at fixed build-rate (BR) → hold inclination through target
- Build rate typical 2-4°/100 ft (low-build) to 10-15°/100 ft (medium-radius)
- Simplest profile; routine development wells

### Build-hold-drop (S-profile)

- Build → hold → drop back to lower or vertical inclination
- Used to maintain bottomhole-position despite extended surface displacement

### Build-build (continuous-curvature horizontal)

- Build inclination continuously to 90° over the curve section
- Hold at 90° through the horizontal lateral
- Standard shale / horizontal-well shape

### Multilateral

- Single primary wellbore with one or more lateral branches from a common parent
- Junction designed per TAML (Technology Advancement of Multilateral) Level 1-6 classification

## Key directional parameters

- **Kick-off depth (KOP)** — TVD where directional drilling begins
- **Build rate (BR)** — rate of inclination change with measured depth, in °/100 ft
- **Inclination (α)** — angle from vertical
- **Azimuth (φ)** — compass direction of horizontal projection
- **Dogleg severity (DLS)** — combined inclination + azimuth change rate, in °/100 ft. Constrained by drill-string fatigue limits.
- **Tortuosity** — actual-vs-planned trajectory deviation

## Drill-stem-design implications

Directional drilling adds **bending stress** to the drill-stem combined-load envelope:

σ_bending = E × OD / (2 × R_curvature)

where R_curvature is derived from dogleg severity. Bending stress is additive to tension; for high-DLS sections, this drives drill-pipe-grade selection. See [drill-stem-design.md](drill-stem-design.md) and [api-rp-7g.md](../standards/api-rp-7g.md).

## Anti-collision

In pad-drilling fields with closely-spaced wellheads, **anti-collision analysis** verifies the planned trajectory's separation from adjacent existing wellbores at all depths. Standard tool: SCO (separation factor / center of curvature) tests.

## Surveying

- **MWD survey** — inclination + azimuth at survey stations during drilling (typically every stand connection)
- **Gyro survey** — independent survey using gyroscopic instrument; runs less frequently, used for verification
- **Multi-station analysis** — compensates for systematic survey errors across multiple stations

## Public references

- **API RP 7G** — [api-rp-7g.md](../standards/api-rp-7g.md) — geometry chapter
- **IADC Drilling Manual** — directional chapter
- **Bourgoyne et al.** Ch. 8 — directional drilling and deviation control
- **Inglis** *Directional Drilling* Springer 1987 (ISBN 0-86010-919-1) — practitioner-canonical

## Cross-references

- [BHA Design](bha-design.md), [Well Plan](well-plan.md), [Drill-Stem Design](drill-stem-design.md)
- [MWD/LWD Overview](mwd-lwd-overview.md) — surveying tools
- [Drilling Tender Evaluation](drilling-tender-evaluation.md), [Offset Well Analysis](offset-well-analysis.md), [IADC DDR Format](iadc-ddr-format.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
