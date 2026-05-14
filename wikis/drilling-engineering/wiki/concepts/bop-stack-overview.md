---
title: "BOP Stack Overview"
tags: [bop, ram-preventer, annular-preventer, shear-ram, blind-ram, well-control, stack-arrangement]
sources:
  - api-spec-16a
  - api-rp-53
added: 2026-05-13
last_updated: 2026-05-13
---

# BOP Stack Overview

## Scope

The blowout-preventer (BOP) stack is the well-control hardware mounted on the wellhead during drilling — a vertical assembly of preventer elements that can close around or shear pipe to seal the well against uncontrolled fluid flow. The stack is the **single most important safety element** in drilling operations.

## Preventer types

- **Annular preventer** — donut-shaped rubber element compressed by a piston; seals around any size pipe (or open hole) in the bore. Primary first-response shut-in element. Brand-canonical names: Hydril GK / GL, Cameron Type DL.
- **Variable-bore ram (VBR)** — pair of opposing rams with curved-profile sealing element that accommodates a range of pipe diameters
- **Pipe ram** — opposing rams with fixed-bore curved sealing element matched to a specific OD (drill pipe, drill collar, casing). Multiple pipe rams in a stack for the well's full pipe-size inventory.
- **Shear ram** — opposing blade-style rams that shear through whatever is in the bore. Two variants:
  - **Blind shear ram** — shears AND seals the hole; the last-resort well-control element
  - **Casing shear ram** — shears heavy casing; doesn't seal (used to enable evacuation)
- **Blind ram** — solid rams that seal an open hole (no pipe in bore); largely superseded by blind-shear rams

## Stack arrangement (typical surface BOP)

Top to bottom:

1. Annular preventer (upper)
2. Variable-bore ram
3. Pipe ram (drill pipe OD)
4. Blind-shear ram
5. Pipe ram (drill collar OD) — sometimes
6. Wellhead connection

## Subsea BOP — additional complexity

Subsea BOPs (drillship / semi-sub) add:
- Lower marine riser package (LMRP) on top of the BOP stack — disconnect point for emergency riser disconnect
- Choke / kill lines plumbed through the stack to surface
- Hydraulic and MUX control lines via the marine riser umbilical

## Public references

- **API Spec 16A** — [api-spec-16a.md](../standards/api-spec-16a.md)
- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md)
- **IADC Drilling Manual** — well-control chapter
- **Bourgoyne et al.** Ch. 4

## Cross-references

- [BOP Pressure Classes](bop-pressure-classes.md), [BOP Control Systems](bop-control-systems.md), [Well-Control Methods](well-control-methods.md), [Shut-In Procedures](shut-in-procedures.md), [Kick Detection](kick-detection.md)
