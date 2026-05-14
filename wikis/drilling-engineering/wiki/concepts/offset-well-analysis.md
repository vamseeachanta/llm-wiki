---
title: "Offset Well Analysis"
tags: [offset-well, bit-performance, rop, npt, mud-weight, fishing-job, historical-data]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Offset Well Analysis

## Scope

Mining historical-well data from offset wells (wells drilled in the same field or analog field) to inform planning of a new well. Offset analysis is the empirical foundation that turns rules-of-thumb into operator-specific design decisions and is the **single most valuable input** to drilling-tender evaluation.

The [Papkov AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) explicitly operates on "verifiable offset data" — offset wells are the source of that data.

## Data extracted from offsets

### Drilling performance

- **Bit performance** — IADC code, run hours, footage drilled, dull grade per offset well per section. See [iadc-dull-grading.md](iadc-dull-grading.md), [bit-selection.md](bit-selection.md).
- **ROP profile** — feet/hour vs depth; identifies hard / soft / chert / shale intervals
- **WOB / RPM history** — operator-set drilling parameters used historically
- **NPT events** — non-productive time by category (mechanical, formation, weather, etc.)

### Geological / formation

- **Formation tops** — measured depths per formation interface
- **Mud weight log** — actual mud weight vs depth (proxy for pore pressure)
- **Lost-circulation events** — depths and volumes lost
- **Kick events** — depths, severity, fluid type, kill weight

### Mechanical

- **Casing-setting depths** — actual vs planned
- **Cement-job quality** — CBL/VDL results per casing string
- **BHA assemblies** — what worked, what failed
- **Fishing history** — what was lost, what was recovered, time spent

### IADC DDR

Daily Drilling Reports per offset well — see [iadc-ddr-format.md](iadc-ddr-format.md). The DDR is the canonical data structure for capturing all of the above per-day per-well.

## Why offset analysis dominates planning

- **Cost estimating** — historical days-per-section is more reliable than first-principles time estimation
- **Bit selection** — offset CPF (cost-per-foot) winners point to the right bit type for each interval
- **Mud weight schedule** — offset MW log is the best predictor of pore-pressure profile
- **NPT mitigation** — offset NPT events predict what to plan for

## Connection to AI tender evaluation

A bidder's claims (predicted ROP, days-per-section, bit life, mud-system cost) must be **consistent with offset experience**. A bidder predicting 2x the historical ROP for this formation should be flagged. The AI agent automates this consistency check at scale across all bidders.

## Public references

- **IADC Drilling Manual** — offset-well-analysis chapter
- **Bourgoyne et al.** Ch. 11 — historical-cost-based estimation
- **SPE OnePetro** — offset-well-analysis methodology papers

## Cross-references

- [Well Plan](well-plan.md), [AFE](afe-authorization-for-expenditure.md), [Drilling Tender Evaluation](drilling-tender-evaluation.md), [IADC DDR Format](iadc-ddr-format.md), [BHA Design](bha-design.md)
- [Bit Selection](bit-selection.md), [IADC Dull Grading](iadc-dull-grading.md) — Phase 1 cross-references
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — "AI agent evaluates bids against verifiable offset data"
