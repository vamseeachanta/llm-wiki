---
title: "Shut-In Procedures"
tags: [shut-in, hard-shut-in, soft-shut-in, sicp, sidpp, well-control]
sources:
  - api-rp-53
added: 2026-05-13
last_updated: 2026-05-13
---

# Shut-In Procedures

## Scope

The standard procedure for closing the BOP after kick detection and obtaining the pressure measurements that drive [well-control methods](well-control-methods.md). Two procedural variants — hard shut-in and soft shut-in — with operator-specified application.

## Hard shut-in

Sequence (driller-led at the choke manifold):

1. Stop pumps
2. Pick up off bottom (clear of bit)
3. Close annular preventer (or upper ram)
4. Close the choke
5. Notify well-site supervisor and toolpusher
6. Record pressures: SIDPP (shut-in drillpipe pressure) and SICP (shut-in casing pressure)

Hard shut-in closes the well **before** taking pressures. Faster well-shut-in but potentially higher peak pressure spike if the kick was already large.

## Soft shut-in

Same sequence but choke is left open initially (or partly open) — flow is directed through the choke before fully closing it. Allows pressure to bleed back through choke, smoother pressure rise.

Operator-policy decision: most modern operators specify hard shut-in (faster well control); soft shut-in is sometimes specified for shallow / soft-formation wells where rapid pressure spike could fracture formation.

## SICP and SIDPP

- **SIDPP — Shut-In DrillPipe Pressure** — measured at standpipe gauge; equals formation pressure minus hydrostatic of current mud column (assumed kick has not migrated past the bit). Drives kill-mud-weight calculation.
- **SICP — Shut-In Casing Pressure** — measured on the annulus side via the choke manifold; equals formation pressure minus annular column hydrostatic (mud + kick fluid).

The difference SICP − SIDPP indicates the kick volume / kick fluid density (the lighter the kick fluid, the larger the difference).

## After shut-in

- Compute kill mud weight from SIDPP
- Select well-control method (driller's vs wait-and-weight)
- Execute kill circulation per the chosen method
- Re-circulate, drill ahead

## Public references

- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md)
- **IADC WellCAP curriculum**

## Cross-references

- [Kick Detection](kick-detection.md), [Well-Control Methods](well-control-methods.md), [BOP Stack Overview](bop-stack-overview.md), [BOP Pressure Classes](bop-pressure-classes.md)
