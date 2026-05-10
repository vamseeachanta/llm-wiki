---
title: "LNG Project Lifecycle"
tags: [lng-projects, concept, lifecycle, fel, feed, fid, epc, commissioning, operations, decommissioning]
added: 2026-05-03
last_updated: 2026-05-09
sources: [concept-synthesis]
domain: lng-projects
cross_links:
  - ../concepts/lng-project-shapes.md
  - ../concepts/lng-regulatory-framework.md
  - ../concepts/lng-process-safety.md
  - ../concepts/lng-storage-tanks.md
  - ../concepts/lng-liquefaction-processes.md
  - ../../standards/ferc-18-cfr-153.md
  - ../../standards/phmsa-49-cfr-193.md
  - ../../standards/nfpa-59a.md
  - ../../standards/csa-z276.md
  - ../../standards/en-1473.md
  - ../../standards/api-std-625.md
  - ../../standards/igc-code.md
---

# LNG Project Lifecycle

## Scope

This page summarizes the canonical phase taxonomy used by LNG project developers and EPC contractors from initial conceptualization through operations and decommissioning. It is project-agnostic — no facility-specific narrative — and does **not** enumerate sanction thresholds, lender covenants, or specific commercial terms; those belong on the regulatory framework page or in project-bound source pages. Decision-gate criteria, financing-stage mechanics, and offtake-contract structuring are covered at concept depth here, not procedural depth. Decommissioning is summarized at the lifecycle level only; a dedicated future page is planned as the post-2050 cohort of decommissioned assets grows.

## Why a phased lifecycle governs LNG project economics

- **Cost certainty improves stepwise across phases** — Class 5 / Class 4 estimates at conceptualization (±50%), Class 3 at FEED (±10-20%), Class 2 / Class 1 at construction tender. Each phase reduces estimate uncertainty in exchange for accumulated front-end engineering spend. Sanction-grade cost certainty is the FEED-phase deliverable that gates FID.
- **Capex spend is back-loaded** — pre-FEED + FEED typically account for 1-3% of lifecycle capex; FID gating commitments (long-lead equipment, EPC mobilization) account for 5-10%; EPC execution captures 25-40% of lifecycle capex; commissioning + start-up captures 2-5%; the balance is operations-phase sustaining capex over the operating life.
- **Decision-gate concurrency is the timeline driver** — offtake contracts, financing close, and EPC bid evaluation must converge at FID. Misalignment of any one gate (offtake-buyer credit, lender covenants, EPC pricing) can slip FID by quarters or years. The 2020-2025 window saw multiple announced projects slip FID for offtake-contract reasons rather than engineering reasons.
- **Standards applicability is locked at FEED** — basis of design, code editions (NFPA 59A, EN 1473, CSA Z276, API Std 625, IGC Code), and exclusion-zone methodology are frozen at FEED and locked through EPC. Late-stage code updates require change-order management and can drive material rework. See [LNG Regulatory Framework](./lng-regulatory-framework.md).

## Pre-FEED — conceptualization and screening

- **Opportunity framing** — feed-gas resource assessment, market study (offtake-region demand and price-formation outlook), location screening (port access, exclusion-zone feasibility), and project-shape selection (greenfield / brownfield / FLNG / FSRU / mid-scale). See [LNG Project Shapes](./lng-project-shapes.md).
- **Permitting feasibility** — early engagement with siting authority (FERC for US export, national competent authority for EU, equivalents elsewhere). Resource Report 1 / equivalent prefiling material drafted; environmental baseline studies initiated.
- **Class 5 to Class 4 cost estimates** — order-of-magnitude (Class 5, ±50%) progressing to factored estimates (Class 4, ±30-50%) as concept matures.
- **Concept-screening deliverables** — capacity sizing, technology screening (process family, liquefaction-cycle selection, refrigerant supply, power source), and a go / no-go recommendation to enter FEED.

## FEED — front-end engineering design

- **Duration and intensity** — typically 12-18 months for greenfield onshore; 9-12 months for brownfield additions; 12-18 months for FLNG / FSRU. Multiple parallel FEED contractors are sometimes engaged for competitive front-end design.
- **Deliverables** — Class 3 cost estimate (±10-20%), frozen process basis of design, plot plan, equipment list, P&IDs, basis-of-design documents, environmental impact assessment package, and the procurement strategy.
- **Standards lock-in** — NFPA 59A / EN 1473 / CSA Z276 edition, API Std 625 tank-system selection (or EN 14620 equivalent), IGC Code edition (for floating shapes), and exclusion-zone methodology are all frozen at FEED. See [LNG Storage Tanks](./lng-storage-tanks.md) for tank-system-selection consequences.
- **Hazard evaluation at FEED** — full HAZOP, LOPA, and preliminary QRA. Outputs feed Resource Reports / EIA submissions and inform FID risk-tolerance review by lender / insurance markets. See [LNG Process Safety](./lng-process-safety.md).

## FID — final investment decision

- **Concurrency of three gates** — offtake-contract execution (long-term SPAs typically required for project finance), financing close (lender syndicate, ECA support, equity partners), and EPC contract award (lump-sum or convertible LSTK).
- **Offtake-contract structure** — historically 20-25 year long-term SPAs with destination flexibility increasingly common; tolling and equity-lifting structures supplement pure SPA arrangements. Contract-mix changes through the 2020s pulled offtake terms shorter (10-15 years more common) and pushed pricing-formula complexity higher.
- **Financing structures** — project finance (limited recourse) is the dominant structure for greenfield and FLNG; balance-sheet financing is more common for brownfield additions and FSRU charters. Export credit agency (ECA) participation is common in cross-border developments.
- **FID milestone formality** — board approval, commitment of long-lead equipment orders (compressors, cryogenic exchangers, gas turbines, GBS / hull modules for floating), and notice to proceed to EPC contractor.

## EPC execution

- **Duration scaled to shape** — onshore-greenfield EPC typically 4-5 years from FID to first cargo; brownfield 3-4 years; FLNG 3-4 years from FID; FSRU conversion 18-24 months; FSRU newbuild 30-36 months. See [LNG Project Shapes](./lng-project-shapes.md).
- **Capex accumulation** — 25-40% of lifecycle capex spent in this phase. Long-lead equipment delivery, modular fabrication, marine works, tankage, and utilities each have their own critical-path implications.
- **Code applicability through execution** — basis of design frozen at FEED is locked through EPC; engineering deviations require formal change-order management. Code updates that land during EPC execution are typically grandfathered, but jurisdiction and authority practice varies.
- **Class-society interface for floating shapes** — IACS member class society (ABS, DNV, BV, LR, KR, ClassNK, RINA, etc.) reviews and stamps the design package; type-approval surface for cargo containment system (membrane, Moss spherical, Type C). See [LNG Regulatory Framework](./lng-regulatory-framework.md).

## Commissioning, start-up, operations, decommissioning

- **Commissioning and start-up** — typically 9-12 months from mechanical completion to first cargo. Includes systems completion, dry / wet commissioning, refrigerant inventory loading, first cool-down, performance testing, and ramp to nameplate. OEM warranty period typically commences at substantial completion.
- **Operations** — steady-state production over a 20-30 year typical operating life; major turnarounds typically every 4-6 years for compressor / driver overhaul, exchanger inspection, and code-required tank in-service inspection (EEMUA Pub 147 cycles for terminal storage tanks).
- **Mid-life capacity creep and de-bottlenecking** — incremental upgrades (compressor rerates, exchanger replacements, train de-bottlenecking) routinely add 5-15% to nameplate over the operating life without full brownfield expansion.
- **Decommissioning** — the post-2050 era will see the first cohort of large LNG facilities reach end-of-life. Abandonment-in-place vs. removal is host-government and lease-terms driven. FLNG decommissioning interacts with the IMO offshore-decommissioning framework and class-society guidance for floating-unit recycling. A dedicated decommissioning concept page is a follow-up gap.

## Standards / References

- [FERC 18 CFR 153](../standards/ferc-18-cfr-153.md) — US LNG siting authority whose Resource Reports + NEPA review gate the FEED-to-FID phases for export terminals.
- [PHMSA 49 CFR 193](../standards/phmsa-49-cfr-193.md) — US LNG facility safety operations governing the commissioning-and-operations phases.
- [NFPA 59A](../standards/nfpa-59a.md) — design code that establishes the basis-of-design frozen at FEED and locked through EPC.
- [CSA Z276](../standards/csa-z276.md) — Canadian LNG production / storage / handling standard whose applicability is locked in at FEED for Canadian-jurisdiction projects.
- [EN 1473](../standards/en-1473.md) — European harmonized onshore LNG installation standard whose applicability is locked in at FEED for EU-jurisdiction projects.
- [API Std 625](../standards/api-std-625.md) — Tank Systems for Refrigerated Liquefied Gas Storage; tank-system selection (or EN 14620 equivalent) is locked in at the design phase.
- [IGC Code](../standards/igc-code.md) — IMO international gas-carrier code constraining the marine-side of EPC scope for floating shapes.
- US DOE Global LNG Fundamentals — public-domain primer on LNG project phasing: <https://www.energy.gov/fecm/global-lng-fundamentals>
- AACE International Recommended Practice 18R-97 — Cost-Estimate Classification System (Class 1 through Class 5): <https://web.aacei.org/>

## Recent industry experience

- **2020-2025 FID hesitancy** — the early-pandemic demand shock and subsequent inflation in long-lead equipment and EPC pricing slowed FID across multiple announced projects. Several greenfield projects slipped FID by 12-24 months while offtake portfolios reformed.
- **Post-Russia-Ukraine European demand pull** — the 2022 supply shock accelerated FID for several US Gulf Coast projects with European offtake. FSRU charters and conversions deployed within months as bridging capacity. The window also re-priced long-term offtake contracts upward.
- **US-Asia trade flow shifts** — Henry-Hub-indexed cargoes with destination flexibility increased the share of arbitrage-driven LNG flows; offtake-contract structures shifted from rigid long-term SPAs toward portfolio-aggregator models with shorter duration.
- **Permitting timing as critical path** — for US export, FERC and DOE export-authorization timelines have become a more visible critical-path item than EPC duration on multiple projects through the 2020s. Permitting reform debates and DOE export-pause / resumption cycles have introduced regulatory-timing risk into FEED-to-FID planning.
- **Methane-intensity gating at FID** — lender and offtake-buyer due diligence now routinely incorporates upstream methane intensity, EU Methane Regulation compliance pathway, and Subpart W reporting trajectory as FID-gating items alongside traditional cost / schedule / offtake review.

## Cross-references

- [LNG Project Shapes](./lng-project-shapes.md) — onshore vs. FLNG vs. FSRU phase-duration differences.
- [LNG Regulatory Framework](./lng-regulatory-framework.md) — standards bodies and regulators that gate each phase.
- [LNG Process Safety](./lng-process-safety.md) — hazard-evaluation cadence (HAZID at concept, HAZOP at FEED, QRA at FEED + pre-startup).
- [LNG Storage Tanks](./lng-storage-tanks.md) — tank-system-selection lock-in at FEED.
- [LNG Liquefaction Processes](./lng-liquefaction-processes.md) — process-family selection at conceptualization, locked at FEED.
- **Cross-wiki (asset-management)**: [Asset Lifecycle](../../../asset-management/wiki/concepts/asset-lifecycle.md) — broader asset-lifecycle framework; the LNG project lifecycle above maps onto the asset-management generic phases (concept → design → construct → operate → decommission) with LNG-specific gate criteria.
