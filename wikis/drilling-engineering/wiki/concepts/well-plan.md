---
title: "Well Plan"
tags: [well-plan, drilling-program, targets, trajectory, casing-program, mud-program, time-cost-estimate]
sources:
  - iadc-drilling-manual
added: 2026-05-13
last_updated: 2026-05-13
---

# Well Plan

## Scope

The **engineering well plan** — the controlled document that captures all design decisions for a planned well: surface and bottomhole targets, planned trajectory, casing program, mud program, BHA selections per hole section, cementing program, well-control philosophy, and time-and-cost estimate. The well plan is the primary input to drilling-tender RFP construction and the document a [Papkov-style AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) consumes to evaluate bids.

## Standard contents

1. **Well objective** — exploration / appraisal / development / injection / disposal
2. **Surface location** — coordinates, surface pad geometry, surface restrictions
3. **Targets** — primary and secondary, TVD / TVDSS, lateral coordinates, target tolerance
4. **Trajectory** — kick-off depth, build rate, hold inclination, drop-off (if any), turn azimuth — see [directional-drilling.md](directional-drilling.md)
5. **Casing program** — see [casing-program-design.md](casing-program-design.md); setting depths, grades, weights, connections
6. **Mud program** — fluid type per section, density schedule, rheology targets — see [drilling-fluid-types.md](drilling-fluid-types.md) and [mud-properties.md](mud-properties.md)
7. **BHA design per section** — bit selection, drill collar / HWDP weights, motor / RSS, MWD/LWD — see [bha-design.md](bha-design.md)
8. **Cementing program** — slurry density, volume, top-of-cement targets per section — see [primary-cementing.md](primary-cementing.md)
9. **Well-control philosophy** — BOP rating, kick tolerance, MAASP per section — see [well-control-methods.md](well-control-methods.md)
10. **AFE** — see [afe-authorization-for-expenditure.md](afe-authorization-for-expenditure.md)
11. **Risk register** — hole problems, NPT events expected, mitigation plans
12. **Schedule** — time per section, total spud-to-RR estimate

## Anchored on offset wells

A well plan derives heavily from [offset-well-analysis.md](offset-well-analysis.md) — historical performance of nearby wells (bit-life, ROP, mud-weight events, NPT) directly informs the planned-well sizing and risk profile.

## Public references

- **IADC Drilling Manual** — well-planning chapter
- **Bourgoyne et al.** Ch. 1 (drilling-engineering overview) + Ch. 11 (well-cost estimation)
- **Mitchell & Miska** well-planning chapter
- **Robello Samuel** *Drilling Engineering* PennWell — well-plan template content

## Cross-references

- All Papkov-AI-consumer-pack pages: [afe-authorization-for-expenditure.md](afe-authorization-for-expenditure.md), [offset-well-analysis.md](offset-well-analysis.md), [drilling-tender-evaluation.md](drilling-tender-evaluation.md), [iadc-ddr-format.md](iadc-ddr-format.md), [bha-design.md](bha-design.md), [directional-drilling.md](directional-drilling.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
