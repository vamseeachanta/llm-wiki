---
title: "Bit Selection"
tags: [drill-bit, bit-selection, offset-bit-analysis, rop, cost-per-foot, formation-hardness]
sources:
  - iadc-bit-classification
added: 2026-05-13
last_updated: 2026-05-13
---

# Bit Selection

## Scope

Engineering workflow for choosing the drill bit for each hole section of a well — given offset-well dull-grade records, formation expectation, BHA constraints, and contractor inventory. This is the workflow the [Papkov founding-source AI-agent prototype](../sources/papkov-2026-drilling-tender-ai-agent.md) is designed to automate for drilling-tender evaluation.

## Inputs

1. **Formation expectation** — lithology, hardness (UCS or compressive strength), abrasivity, interbed pattern from the offset-well log and core data
2. **Offset-well dull-grade history** — IADC dull codes from prior wells in the same field. The empirical record of which bit types performed how on this formation.
3. **BHA constraints** — bit-shank connection size, gauge protection requirements, motor or rotary-steerable compatibility, weight-on-bit envelope
4. **Hole-section geometry** — diameter, length, dogleg severity, expected hours
5. **Bit inventory** — what the operator has on the rig or in the warehouse; what the bidder offers

## Decision rubric

- **Cost-per-foot (CPF)** — the load-bearing metric: CPF = (bit-cost + rig-cost × hours) / footage drilled. Compare CPF across bit candidates against the offset record.
- **Predicted bit life** — from offset dull-grade hours-on-bit pattern, projected onto the current well's section length
- **Risk of unscheduled trip** — bits with marginal predicted life force an unscheduled trip if they fail; cost the rig-time downside into the CPF
- **Hydraulics fit** — see [Bit Hydraulics](bit-hydraulics.md); the bit must operate inside the rig's pump capacity and the hole's HSI requirement

## Offset-bit-record analysis

The core technique: pull every dull-grade from every offset well in the field, cluster by formation interval, identify the bit IADC-code (or specific manufacturer model) that produced the best CPF on each interval, and pick that bit for the planned well. Bidder proposals are evaluated against this record — a proposed bit-life claim must be consistent with the empirical offset distribution.

The [Papkov founding source](../sources/papkov-2026-drilling-tender-ai-agent.md) AI-agent prototype automates this workflow at scale across many wells and bidders.

## Common selection mistakes

- **Day-rate optimization over total cost** — picking the cheapest bit when the rig-cost dominates makes total well-cost worse
- **Manufacturer-claim acceptance** — bit-life claims from bit-manufacturer marketing exceed empirical offset performance frequently; trust the dull-grade record
- **Ignoring interbed structure** — formation-average hardness hides high-abrasion thin layers; the bit must survive the worst interval, not just the average

## Public references

- **Bourgoyne et al.** Chapter 5 — bit selection methodology
- **Mitchell & Miska** Chapter 5 — modern bit selection
- **SPE bit-selection literature** — extensive OnePetro paper library

## Cross-references

- [IADC Dull Grading](iadc-dull-grading.md) — the offset-data structure consumed
- [Drill-Bit Types](drill-bit-types.md), [IADC Roller-Cone Code](iadc-roller-cone-code.md), [IADC PDC Code](iadc-pdc-code.md)
- [Bit Hydraulics](bit-hydraulics.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — AI-tender-evaluation downstream consumer
