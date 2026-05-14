---
title: "Hole Cleaning"
tags: [hole-cleaning, cuttings-transport, annular-velocity, deviated-well, horizontal-well]
sources:
  - api-rp-13b-1
added: 2026-05-13
last_updated: 2026-05-13
---

# Hole Cleaning

## Scope

The process of lifting drilled cuttings from the bit face up the annulus and out of the well — and the design parameters (annular velocity, mud rheology, pipe rotation) that determine whether cuttings actually get out. Hole-cleaning failure causes pack-off, stuck pipe, and lost wells; it's the dominant non-productive-time (NPT) cause in extended-reach drilling.

## Three regime taxonomy by inclination

- **Vertical (0-30°)** — gravity assists; annular velocity alone usually sufficient
- **Intermediate / deviated (30-60°)** — most challenging regime; cuttings form beds on the low side of the annulus; cleaning requires high annular velocity + pipe rotation + good rheology
- **Horizontal (60-90°)** — beds form stable; pipe rotation critical; sometimes specialty additives (oil-wetting agents in OBM) help

## Annular velocity

Annular velocity = pump flow rate / annular cross-sectional area

Higher AV lifts cuttings better. Typical operational targets: 100-150 ft/min in vertical, 200+ ft/min in deviated/horizontal.

## Pipe rotation effect

Rotating drill pipe **breaks up cuttings beds** and re-suspends them into the active flow. Rotary drilling cleans better than sliding (motor-only) drilling at the same flow rate. The transition from rotary to sliding mode is a known stuck-pipe risk point.

## Cuttings transport ratio (CTR)

CTR = (annular velocity − cuttings slip velocity) / annular velocity

A theoretical measure; CTR ≈ 1 means efficient transport, CTR < 0.5 means poor transport. Slip velocity is the gravity-driven settling velocity opposing the upward flow.

## When hole cleaning fails

- **Pack-off** — cuttings accumulate around the bit / BHA, stopping circulation. Stuck-pipe event.
- **Stuck pipe (differential)** — mud cake sticks the drill pipe to permeable formation
- **Wellbore instability** — caving / sloughing increases the cuttings load beyond the cleaning capacity

## Public references

- **API RP 13B-1** — [api-rp-13b-1.md](../standards/api-rp-13b-1.md). Mud-property context.
- **Bourgoyne et al.** Ch. 5 and Ch. 6 — hole-cleaning regime analysis
- **Caenn et al.** 2017 — hole-cleaning correlations and operational guidance

## Cross-references

- [Mud Properties](mud-properties.md), [Drilling-Fluid Types](drilling-fluid-types.md), [ECD and Pressure Management](ecd-and-pressure-management.md), [Bit Hydraulics](bit-hydraulics.md)
- [Drill-Stem Design](drill-stem-design.md) — drag and torque also degrade with poor hole cleaning
