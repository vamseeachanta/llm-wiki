---
title: "BHA Design"
tags: [bha, bottomhole-assembly, drill-collar, hwdp, stabilizer, mud-motor, rss, mwd]
sources:
  - api-rp-7g
  - api-spec-7-1
added: 2026-05-13
last_updated: 2026-05-13
---

# BHA Design

## Scope

The Bottomhole Assembly (BHA) is the lower portion of the drill string from the bit upward to the drill pipe — comprising drill collars (weight-on-bit), HWDP (transition), stabilizers / reamers (gauge control), MWD/LWD tools (data), motor or rotary-steerable system (directional control), and ancillary subs. BHA design is a per-section engineering decision that ties bit selection, drilling parameters, formation expectations, and trajectory into one assembled tool string.

## BHA component inventory

### Bit

See [drill-bit-types.md](drill-bit-types.md), [bit-selection.md](bit-selection.md), [bit-hydraulics.md](bit-hydraulics.md).

### Bit sub / motor or RSS

- **Bit sub** — direct adapter for rotary drilling
- **Mud motor (PDM — positive displacement motor)** — downhole hydraulic motor providing bit rotation independent of drill-string rotation; used for sliding directional drilling
- **Rotary-steerable system (RSS)** — downhole tool steering the bit while the drill string rotates; faster directional drilling, less stuck-pipe risk

### MWD / LWD

See [mwd-lwd-overview.md](mwd-lwd-overview.md). Inclination / azimuth / toolface measurements + formation evaluation logs.

### Stabilizers and reamers

- **Stabilizers** — wear-resistant near-bit and string elements maintaining wellbore gauge
- **Reamers** — fixed or expandable; enlarge hole diameter behind bit (in-hole) or rough out gauge

### Drill collars

- **Heavy steel** — provides weight-on-bit; placed at bottom of BHA
- **Non-magnetic** (Monel / Inconel) — placed around MWD tools to avoid magnetic interference
- See [API Spec 7-1](../standards/api-spec-7-1.md)

### Heavyweight Drill Pipe (HWDP)

- Transition element between drill collars and drill pipe
- Reduces stress concentration; see [drill-stem-design.md](drill-stem-design.md)
- Can carry compression in deviated wells

### Subs and crossovers

- Connect different-thread or different-OD components
- Float subs (one-way valves) prevent fluid backflow

## BHA design principles

1. **Weight-on-bit budget** — sum of drill-collar weight + HWDP compressive capacity must exceed required WOB with margin
2. **Neutral-point location** — keep above drill-collar / HWDP transition (compression zone)
3. **Buckling-tendency** — calculated per API RP 7G; sized to avoid buckling-induced fatigue
4. **Stabilizer placement** — drives drift / build / drop tendency (positive / negative / packed-hole configurations)
5. **MWD / LWD placement** — usually 30-60 ft from bit for near-bit measurements; back farther for formation evaluation

## Pendulum / building / packed-hole BHAs

- **Pendulum BHA** — minimal stabilization above bit; drops angle (tends toward vertical)
- **Building BHA** — fulcrum near-bit stabilizer; tends to build angle
- **Packed-hole BHA** — multiple closely-spaced stabilizers; tends to hold angle
- **RSS-based** — replaces classic stabilizer-driven directional control with active steering

## Public references

- **API RP 7G** — [api-rp-7g.md](../standards/api-rp-7g.md). Drill-stem and BHA design.
- **API Spec 7-1** — [api-spec-7-1.md](../standards/api-spec-7-1.md). Component specs.
- **Bourgoyne et al.** Ch. 6 (drill string) + Ch. 8 (directional drilling)
- **Inglis** *Directional Drilling* Springer 1987 (ISBN 0-86010-919-1)

## Cross-references

- [Drill-Stem Design](drill-stem-design.md), [Tool Joints](tool-joints.md), [Drill-Bit Types](drill-bit-types.md), [Bit Selection](bit-selection.md), [MWD/LWD Overview](mwd-lwd-overview.md), [Directional Drilling](directional-drilling.md)
- [Well Plan](well-plan.md), [Offset Well Analysis](offset-well-analysis.md), [Drilling Tender Evaluation](drilling-tender-evaluation.md), [IADC DDR Format](iadc-ddr-format.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
