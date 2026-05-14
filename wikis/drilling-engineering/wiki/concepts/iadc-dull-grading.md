---
title: "IADC Dull-Grading Code"
tags: [iadc, drill-bit, dull-grading, used-bit, trip-out, reason-pulled, offset-bit-analysis]
sources:
  - iadc-bit-classification
added: 2026-05-13
last_updated: 2026-05-13
---

# IADC Dull-Grading Code

## Scope

Standardized 8-character IADC code for recording the condition of a used drill bit at trip-out. Per SPE/IADC 23939, the dull-grading code captures inner cutting / outer cutting / dull characteristic / location / bearing seals / gauge / other dull / reason pulled. The code is recorded on the drilling-recap report, becomes part of the well's offset record, and feeds [bit selection](bit-selection.md) for subsequent wells.

## The 8-character format

| # | Character | Meaning |
|---|---|---|
| 1 | I — Inner cutting structure | 0-8 percentage of cutting-structure wear on inner 2/3 of bit |
| 2 | O — Outer cutting structure | 0-8 percentage of cutting-structure wear on outer 1/3 of bit |
| 3 | D — Dull characteristic | Letter code for predominant dull (BC broken cone, CC cracked cutter, LT lost teeth, etc.) |
| 4 | L — Location | Letter code for where on the bit the dull is concentrated (N nose, C cone, M middle, etc.) |
| 5 | B — Bearing seals | For roller-cone: 0-8 percentage of bearing life consumed. For PDC: "X" (not applicable). |
| 6 | G — Gauge | I (in-gauge) or measured undergauge in 1/16" increments |
| 7 | O — Other dull characteristic | Secondary dull characteristic code |
| 8 | R — Reason pulled | Letter code for trip-out reason (BHA, TD, HR hours, HP hole problem, etc.) |

## Worked example

`4-3-WT-A-7-I-NO-BHA` decodes as: 4/8 inner-structure wear, 3/8 outer-structure wear, predominant dull is worn teeth (WT), located on all rows (A), bearing 7/8 consumed, gauge in-gauge, no secondary dull (NO), pulled to change BHA (BHA).

## Why this matters for AI tender evaluation

Offset-well dull-grade records are exactly the structured data the [Papkov AI-agent prototype](../sources/papkov-2026-drilling-tender-ai-agent.md) needs to consume — the historical bit-performance record an operator has on a given formation that a bidder's claim of "we'll use a Smith MSi616" can be validated against. Bidder bit selection inconsistent with the offset dull-grade record (e.g., proposing a bit-life claim that exceeds the formation's empirical track record) is a flag.

## Public references

- **SPE/IADC 23939** "IADC Dull Grading for PDC Drill Bits" (1992) — primary authority for PDC dull grading
- **SPE-23938** "Roller Bit Dull Grading System" — companion paper for roller-cone bits
- **IADC Drilling Manual** — practitioner restatement

## Cross-references

- [Drill-Bit Types](drill-bit-types.md), [IADC Roller-Cone Code](iadc-roller-cone-code.md), [IADC PDC Code](iadc-pdc-code.md)
- [Bit Selection](bit-selection.md) — uses dull-grades as input
- [IADC Bit Classification](../standards/iadc-bit-classification.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — AI-tender-evaluation downstream consumer
