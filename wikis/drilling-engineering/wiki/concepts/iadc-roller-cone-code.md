---
title: "IADC Roller-Cone Bit Code"
tags: [iadc, drill-bit, roller-cone, tricone, classification-code]
sources:
  - iadc-bit-classification
added: 2026-05-13
last_updated: 2026-05-13
---

# IADC Roller-Cone Bit Code

## Scope

The 4-character IADC classification code for roller-cone (tricone) drill bits per SPE-23937-MS. Codes a bit's intended formation class, structure type within the class, bearing / gauge feature, and special features into a compact label that crosses manufacturer lines.

## Code structure

### Character 1 — Formation series (1-8)

Soft (1) to hard / abrasive (8). Increasing number = harder formation:

- 1 — Soft (mudstone, shale)
- 2 — Soft, gummy
- 3 — Medium-soft
- 4 — Medium
- 5 — Medium-hard
- 6 — Hard
- 7 — Very hard
- 8 — Very hard / abrasive

### Character 2 — Formation type within series (1-4)

Sub-classification within the series. Higher digit = harder sub-formation.

### Character 3 — Bearing / gauge feature (1-7)

- 1-3 — Open-roller bearing (1 standard, 2 air-cooled, 3 gauge-protected)
- 4-5 — Sealed-roller bearing
- 6-7 — Sealed-friction (journal) bearing

### Character 4 — Special features (letter, optional)

- A — Air-cooled
- B — Special bearing
- C — Center jet
- D — Deviation control
- E — Extended jet
- G — Extra gauge protection
- H — Horizontal application
- J — Jet deflection
- L — Lugged
- M — Motor application
- S — Standard steel-tooth
- T — Two-cone
- W — Enhanced cutting structure
- X — Chisel insert
- Y — Conical insert
- Z — Other insert

## Worked examples

- **1-1-7** — soft formation, standard sub-class, sealed-friction journal bearing. Modern routine soft-formation tricone.
- **5-3-7-M** — medium-hard formation type 3, sealed journal, configured for motor application.
- **8-4-5-G** — very hard / abrasive formation type 4, sealed-roller, extra gauge protection.

## Public references

- **SPE-23937-MS** "The IADC Roller Bit Classification System," SPE/IADC Drilling Conference 1992 — primary authority
- **IADC Drilling Manual** — practitioner restatement
- **Bourgoyne et al.** Chapter 5 — worked-example tabulations

## Cross-references

- [Drill-Bit Types](drill-bit-types.md), [IADC PDC Code](iadc-pdc-code.md), [IADC Dull Grading](iadc-dull-grading.md)
- [Bit Selection](bit-selection.md), [Bit Hydraulics](bit-hydraulics.md)
- [IADC Bit Classification](../standards/iadc-bit-classification.md)
