---
title: "AFE — Authorization For Expenditure"
tags: [afe, well-cost, capex, dry-hole-cost, completion-cost, contingency, drilling-cost-estimate]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# AFE — Authorization For Expenditure

## Scope

The Authorization For Expenditure (AFE) is the cost-estimation and budgetary-approval document for a planned well. The AFE pairs with the [well plan](well-plan.md) as the financial counterpart to the engineering specification. AFE construction is one of the load-bearing data artifacts the [Papkov AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) operates on.

## Standard AFE structure

### Top-level cost split

- **Dry-hole cost** — drilling costs incurred regardless of well outcome (rig day-rate, fuel, casing, cement, services). Recovers nothing on a dry hole.
- **Completion cost** — incurred only on a productive well (production casing, perforating, completion equipment, well-testing). Discretionary on results.
- **Total well cost** = dry-hole + completion + contingency

### By-section breakdown (dry-hole)

Costs broken out per hole section:

- **Surface section** (e.g., 36" conductor → 26" surface)
- **Intermediate section(s)** (e.g., 17½" → 12¼")
- **Production section** (e.g., 8½" to TD)

Each section has line items: rig time × day-rate, casing material + freight + handling, cement + service, mud + chemicals, bits, drill-bit services (mud motors / RSS, MWD/LWD), miscellaneous services.

### Common line-item categories

- Rig day-rate × estimated days
- Mud cost (weight up, additives, hauling)
- Casing cost (per joint × joints, plus running services)
- Cement cost (per sack × volume, plus services)
- Bits and drilling services (per bit × count + service personnel)
- Directional services
- Mud logging
- Wireline logging
- Cementing
- Coiled tubing / wireline intervention
- Onshore base and logistics
- Supervisory and overhead

### Contingency

Typically 10-25% of base dry-hole cost — accounts for NPT events, unplanned scope, hole problems. Higher contingency for frontier wells; lower for routine development.

## Public references

- **IADC Drilling Manual** — AFE chapter and standard templates
- **Bourgoyne et al.** Ch. 11 — well-cost estimation
- **SPE well-cost-estimation literature** — open OnePetro library
- AFE templates published by operator-association references (no API spec — convention-driven)

## Cross-references

- [Well Plan](well-plan.md) — engineering counterpart
- [Offset Well Analysis](offset-well-analysis.md) — historical cost / time data input
- [Drilling Tender Evaluation](drilling-tender-evaluation.md) — AFE used to evaluate bids against
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — "AI agent generates technically rigorous RFPs from well plans and AFEs"
