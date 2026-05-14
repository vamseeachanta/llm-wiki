---
title: "IADC PDC (Fixed-Cutter) Bit Code"
tags: [iadc, drill-bit, pdc, fixed-cutter, diamond, classification-code]
sources:
  - iadc-bit-classification
added: 2026-05-13
last_updated: 2026-05-13
---

# IADC PDC (Fixed-Cutter) Bit Code

## Scope

The 4-character IADC classification code for fixed-cutter drill bits (PDC and natural-diamond). Categorizes a bit by body material, cutter density, cutter size / type, and bit profile.

## Code structure

### Character 1 — Body type (letter)

- **M** — Matrix body (tungsten-carbide matrix, brazed PDC cutters)
- **S** — Steel body (machined steel, mechanically retained or brazed cutters)
- **D** — Diamond (natural-diamond impregnated matrix; rare in modern use)

### Character 2 — Cutter density (digit)

- 1-4 for PDC bits — 1 lowest density (more open cutter pattern), 4 highest density
- 6-8 for natural-diamond bits

### Character 3 — Cutter size / type (digit)

For PDC bits: 1 small cutter, 2 medium, 3 large, 4 oversize. For natural-diamond: encoding of stone size.

### Character 4 — Bit profile (digit)

Profile geometry — 1 flat, 2 short, 3 medium, 4 long, etc. Affects directional behavior and ROP.

## Worked examples

- **M-2-2-3** — matrix body, medium cutter density, medium cutter size, medium profile. Generic medium-formation PDC.
- **S-3-1-2** — steel body, high cutter density, small cutters, short profile. Aggressive small-cutter PDC for fast ROP in soft formation.
- **M-1-4-4** — matrix body, open cutter pattern, oversize cutters, long profile. Hard-formation PDC with maximum penetration force per cutter.

## Public references

- **SPE/IADC 23939** "IADC Dull Grading for PDC Drill Bits" (1992) — establishes the PDC bit-classification framework and the dull-grading equivalent
- **IADC Drilling Manual** — PDC classification chapter
- **Mitchell & Miska** Chapter 5 — fixed-cutter bit treatment

## Cross-references

- [Drill-Bit Types](drill-bit-types.md), [IADC Roller-Cone Code](iadc-roller-cone-code.md), [IADC Dull Grading](iadc-dull-grading.md)
- [Bit Selection](bit-selection.md), [Bit Hydraulics](bit-hydraulics.md)
- [IADC Bit Classification](../standards/iadc-bit-classification.md)
