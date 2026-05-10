---
title: "API Standard 653 — Tank Inspection, Repair, Alteration, and Reconstruction"
slug: api-std-653
code_id: api-std-653
publisher: API
revision: "6th ed (2024); current published edition. Earlier editions: 1st (1991), 2nd (1995), 3rd (2001) + 2003 Addendum, 4th (2009), 5th (2014)."
jurisdiction: "Industry standard for refining, petrochemical, terminal-storage, and pipeline-tankage in-service tank inspection; cited by US EPA SPCC (40 CFR 112) and several state above-ground-storage-tank programmes."
instrument_type: specification
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/standard-653
tags:
  - api
  - api-std
  - atmospheric-tanks
  - above-ground-storage
  - in-service-inspection
  - integrity-management
  - rbi-host
  - ffs-gate
  - inspection-trilogy
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Standard 653 — Tank Inspection, Repair, Alteration, and Reconstruction

> **Slug-canonicalisation note.** This page uses the `api-std-NNN` canonical slug form (matching siblings [api-std-579](api-std-579.md), [api-std-1104](api-std-1104.md), [api-std-2rd](api-std-2rd.md)). The existing fuller treatment lives at [api-653](api-653.md) under a legacy slug; both pages reference the same publisher document. Practitioners should treat [api-653](api-653.md) as the substantive landing page and this resolver as the canonical-slug entry point.

> **code_id:** `api-std-653` · **publisher:** API · **revision:** 6th ed (2024)

## Scope

API Standard 653 establishes the **in-service inspection, repair, alteration, and reconstruction** rules for **welded above-ground steel atmospheric storage tanks** that were originally designed to **API Standard 650** or its predecessors in the **API 12 series** (API 12A, 12B, 12C, 12D, 12F field- and shop-welded tanks). It is the post-construction integrity counterpart to API 650 in the same way that [api-510](api-510.md) is the in-service counterpart to ASME BPVC VIII for pressure vessels and [api-570](api-570.md) is the in-service counterpart to [asme-b31-3](asme-b31-3.md) for process piping. Together the three codes are the **API inspection trilogy**.

Scope inclusions: welded carbon-steel and stainless-steel atmospheric tanks storing hydrocarbons, chemicals, or water at near-atmospheric internal pressure; tanks built to API 650 (current) or to the older API 12 series. Out of scope: pressure vessels (use [api-510](api-510.md)) and tanks operating at pressures above the API 650 atmospheric ceiling.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1991 | Original issue |
| 2nd ed | 1995 | Updated bottom-inspection and settlement provisions |
| 3rd ed | 2001 + 2003 Addendum | On-disk catalog edition |
| 4th ed | 2009 | Major revision; RBI alignment |
| 5th ed | 2014 | Expanded floor-plate evaluation |
| 6th ed | 2024 | Current published edition |

Catalog presence: 3rd ed (2001) + 2003 Addendum on disk per [api-653](api-653.md). Current edition not on disk; obtain via publisher catalog.

## Key sections

- **Suitability for service.** Required when an existing tank is being returned to service after a major change in product, hydrostatic head, or service severity.
- **Brittle-fracture screening.** Mandatory low-temperature evaluation for tanks built to pre-1987 API 650 editions; cross-routes to [brittle-fracture](../concepts/brittle-fracture.md).
- **Inspection intervals.** External (5-year default), internal (10-year or RBI-driven), bottom (driven by corrosion-rate evidence, MFL/UT scan results, and remaining-bottom-thickness calculation).
- **Bottom-plate evaluation.** Minimum-thickness rules for primary and annular bottom plates; floor-scan MFL acceptance criteria; under-tank corrosion-rate calculation.
- **Shell evaluation.** Minimum-thickness rules per shell course; settlement evaluation (planar tilt, edge settlement, bottom dishing).
- **Repair and alteration rules.** Welded repair procedures, hot-tap rules, replacement-bottom installation, lifting and re-foundationing.
- **Reconstruction.** Rules for relocating and re-erecting an existing tank at a new site; full re-qualification path.

Clause text, acceptance tables, and worked examples are **not reproduced** per metadata-only governance.

## Practitioner application

API 653 is the code a tank owner-user cites when defending an in-service tank inspection programme to a regulator (US EPA SPCC, state ASTI programmes, BSEE for offshore terminal storage), to insurance underwriters, or to a third-party auditor. The companion practice API RP 575 (*Inspection Practices for Atmospheric and Low-Pressure Storage Tanks* — future first-class standards page candidate) provides execution-grade inspection-method guidance. Coating-system condition feeds bottom and shell corrosion-rate inputs — cross-route to [coating-systems](../concepts/coating-systems.md). RBI implementations under [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) explicitly cite §6 of API 653 as their authority to deviate from default fixed intervals.

## Industry adoption

Cited by reference in US EPA SPCC (40 CFR 112.8(c)(6)) for above-ground bulk-storage container integrity testing. Several US state above-ground-storage-tank (AST) programmes adopt API 653 directly. Globally adopted as the de-facto standard for atmospheric-tank in-service inspection via owner-user programmes; widely cited in pipeline tankage, terminal storage, and refinery storage-tank yards.

## Why this page exists

W208 (iter-45) identified API 653 as a top-24 wikilink target with a substrate-gap cluster around inspection-domain concepts. This page provides a canonical-slug entry point ([api-std-653](api-std-653.md)) aligned with the [api-std-579](api-std-579.md) / [api-std-1104](api-std-1104.md) sibling convention, while the substantive content remains at the legacy-slug page [api-653](api-653.md).

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. Legacy on-disk 3rd ed (2001) + 2003 Addendum recorded in the [og-standards-api](../sources/og-standards-api.md) source page; current edition not in repo (vendor-derivative deny-list per spinout 2026-05-05 governance).

## Cross-references

- [api-653](api-653.md) — legacy-slug full page; substantive scope, edition history, and practitioner detail.
- [api-510](api-510.md) — pressure-vessel inspection code; sibling in the inspection trilogy.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; sibling in the inspection trilogy.
- [api-rp-572](api-rp-572.md) — inspection practices for pressure vessels.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology and quantitative basis cited as alternative to default intervals.
- [api-std-579](api-std-579.md) — fitness-for-service framework consuming API 653 inspection data.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS workflow.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI alternative interval-setting.
- [coating-systems](../concepts/coating-systems.md) — concept anchor for tank-coating condition driving corrosion-rate inputs.
- [brittle-fracture](../concepts/brittle-fracture.md) — concept anchor for low-temperature screening of pre-1987 tanks.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes an API 653 minimum-thickness, settlement-tolerance, or inspection-interval value.
