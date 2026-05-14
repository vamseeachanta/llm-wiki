---
title: "Drilling Tender Evaluation"
tags: [drilling-tender, rfp, bid-evaluation, technical-fit, day-rate, total-well-cost, contractor-evaluation]
sources:
  - iadc-drilling-manual
  - linkedin-papkov-2026-drilling-tender-ai-agent
added: 2026-05-13
last_updated: 2026-05-13
---

# Drilling Tender Evaluation

## Scope

The bid-evaluation framework operators apply to drilling-service tenders. **This page is the integration anchor for the Papkov-AI-agent consumer pack** — it explicitly names the data artifacts (well plan, AFE, offset-well analysis, IADC DDR, BHA design, technical specifications across rigs / casing / drill pipe / drill bit / drilling fluids / cementing / BOP / etc.) that an AI tender-evaluation agent consumes to score bids.

Direct citation: [Papkov (2026) Drilling-Tender AI Agent](../sources/papkov-2026-drilling-tender-ai-agent.md) — the founding source identified the gap this concept page addresses.

## Bid-evaluation dimensions

### Technical fit

- Does the bidder's rig spec match the well's worst-case requirements?
  - Drilling-depth rating ≥ planned TD
  - Hookload rating ≥ heaviest casing weight (with margin)
  - BOP rating ≥ worst-case SISP (see [bop-pressure-classes.md](bop-pressure-classes.md))
  - Mud-pump output sufficient for required hydraulics (see [bit-hydraulics.md](bit-hydraulics.md))
  - Drill-pipe wear class adequate for critical service (see [drill-pipe-wear-classes.md](drill-pipe-wear-classes.md))

### Contractor capability

- Experience with similar formations / depths / environments
- Crew certifications (WellCAP, IWCF)
- Equipment maintenance record
- HSE statistics (TRIR, LTIR, spill incidents)

### Day-rate vs total-well-cost

- Lowest day-rate bid is rarely lowest total-well-cost
- Predicted operating performance (ROP, NPT) drives well duration
- Total well cost = (day-rate × predicted days) + materials + services
- Bidder's predicted-days claim must be defensible against offset history

### Offset-record consistency

The load-bearing AI-agent function from [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md):

- Bidder bit-selection consistency with offset CPF winners
- Bidder predicted-days consistency with offset days-per-section
- Bidder mud-system cost consistency with offset mud-consumption rates
- Bidder BHA-and-bit configuration consistency with offset successes

## Common bid-pathology signatures

The kinds of inconsistencies the Papkov AI agent flags:

- **Under-rated equipment** — BOP RWP below worst-case SISP; rig hookload below casing weight
- **Optimistic time estimates** — predicted ROP above offset 90th percentile
- **Stale fleet docs** — bidder cites a rig spec inconsistent with current vessel condition
- **Method-vs-scope mismatch** — proposing CT when wireline suffices (see [well-intervention-methods.md](well-intervention-methods.md))
- **Missing critical service** — bid omits a required service (e.g., MWD on a directional well)

## Public references

- **IADC Drilling Manual** — drilling-services-procurement chapter
- **Papkov (2026)** — [linkedin-papkov-2026-drilling-tender-ai-agent](../sources/papkov-2026-drilling-tender-ai-agent.md)
- **Bourgoyne et al.** Ch. 11 — economics and contractor-selection context

## Cross-references

- [Well Plan](well-plan.md), [AFE](afe-authorization-for-expenditure.md), [Offset Well Analysis](offset-well-analysis.md), [IADC DDR Format](iadc-ddr-format.md), [BHA Design](bha-design.md), [Directional Drilling](directional-drilling.md)
- [Bit Selection](bit-selection.md), [Drill-Pipe Wear Classes](drill-pipe-wear-classes.md), [BOP Pressure Classes](bop-pressure-classes.md) — Phase 1/2 cross-references
- **Founding source**: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
