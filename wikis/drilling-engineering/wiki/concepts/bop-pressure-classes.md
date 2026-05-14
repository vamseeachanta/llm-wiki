---
title: "BOP Pressure Classes"
tags: [bop, rwp, 5k, 10k, 15k, 20k, hpht, pressure-class]
sources:
  - api-spec-16a
added: 2026-05-13
last_updated: 2026-05-13
---

# BOP Pressure Classes

## Scope

The Rated Working Pressure (RWP) class of a BOP — the maximum pressure the preventer is qualified to seal against. RWP class is a primary bid-evaluation dimension: a BOP rated below the well's worst-case shut-in surface pressure (SISP) is non-compliant for that well regardless of price.

## API Spec 16A RWP classes

- **2,000 psi (2K)** — shallow / low-pressure historical; largely retired
- **3,000 psi (3K)** — moderate-pressure conventional onshore
- **5,000 psi (5K)** — common offshore moderate-pressure
- **10,000 psi (10K)** — workhorse modern offshore deepwater
- **15,000 psi (15K)** — HPHT (high-pressure, high-temperature) applications
- **20,000 psi (20K)** — frontier HPHT; ultra-deep subsea HPHT-frontier wells

## Selecting RWP for a well

Operator selects RWP class to exceed:

1. **Worst-case shut-in surface pressure** — formation pore pressure at TD minus column hydrostatic at the lightest credible mud weight (kick scenario)
2. **Casing-test pressure** — the maximum pressure applied during casing pressure testing
3. **Regulatory margin** — typically 10-20% above maximum expected, per BSEE / HSE / PSA requirements

## Why RWP class is a bid-evaluation flag

A bidder offering a 5K BOP for a 15K HPHT well is technically non-compliant. The [Papkov-style AI tender-evaluation agent](../sources/papkov-2026-drilling-tender-ai-agent.md) would flag this immediately by comparing well's worst-case SISP against the bidder's BOP RWP class. Practitioner reality: this kind of mismatch happens — sometimes accidentally (bidder pulled an old fleet-status doc), sometimes deliberately (bidder offering an under-rated rig hoping operator accepts a non-conforming bid).

## Public references

- **API Spec 16A** — [api-spec-16a.md](../standards/api-spec-16a.md). Primary authority.
- **API RP 53** — [api-rp-53.md](../standards/api-rp-53.md). Operational test pressure context.
- **Bourgoyne et al.** Ch. 4

## Cross-references

- [BOP Stack Overview](bop-stack-overview.md), [BOP Control Systems](bop-control-systems.md), [Well-Control Methods](well-control-methods.md)
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md)
