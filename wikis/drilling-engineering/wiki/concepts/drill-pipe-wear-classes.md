---
title: "Drill-Pipe Wear Classes"
tags: [drill-pipe, wear-class, new, premium, class-2, class-3, inspection]
sources:
  - api-rp-7g-2
added: 2026-05-13
last_updated: 2026-05-13
---

# Drill-Pipe Wear Classes

## Scope

The wear-class assignment system for used drill pipe — New, Premium, Class 2, Class 3. Class is determined by remaining wall thickness (measured by ultrasonic inspection per [API RP 7G-2](../standards/api-rp-7g-2.md)); design-limit values (tensile yield, torsional yield, collapse) are derated from the new-pipe values by class.

## The four classes (paraphrased from API RP 7G-2)

- **New** — never used; 100% nominal wall throughout. Full new-pipe design limits apply.
- **Premium** — 80% or greater minimum remaining wall. Standard for well-maintained drilling-contractor fleets.
- **Class 2** — 70% or greater minimum remaining wall. Acceptable for moderate-severity wells but with derated limits.
- **Class 3** — 55% or greater minimum remaining wall. Slim-hole and shallow-well use only; many operators prohibit Class 3 in critical service.

(Exact wall-percentage thresholds from API RP 7G-2 — confirm at next ingest pass.)

## Derating

Tensile, torsional, and collapse capacities derate roughly in proportion to remaining wall — Premium ≈ 80% of new, Class 2 ≈ 70%, Class 3 ≈ 55%. API RP 7G publishes the exact derating tables; do not approximate for design.

## Inspection-driven assignment

Wear class is assigned at the third-party inspection facility per the RP 7G-2 procedure. The inspection certificate accompanies each pipe back to the rig and is the design input for drill-stem-design calculations on subsequent wells. Mixed-class strings — running Premium and Class 2 together — are typically prohibited; the entire string is designed at the worst class present.

## Practical impact

For [Papkov-style tender evaluation](../sources/papkov-2026-drilling-tender-ai-agent.md), the drill-pipe wear-class is a critical bid dimension: a contractor offering only Class 2 pipe for a critical well is technically non-compliant even if the bid is cheapest. Wear-class verification against the bid is exactly the kind of inconsistency-flagging the Papkov AI-agent prototype is designed to automate.

## Public references

- **API RP 7G-2** — [api-rp-7g-2.md](../standards/api-rp-7g-2.md). Inspection procedure and class definitions.
- **API RP 7G** — [api-rp-7g.md](../standards/api-rp-7g.md). Derating tables.
- **Bourgoyne et al.** Chapter 6 — drill-string design with used pipe

## Cross-references

- [Drill Pipe](drill-pipe.md), [Drill-Stem Design](drill-stem-design.md), [Tool Joints](tool-joints.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
