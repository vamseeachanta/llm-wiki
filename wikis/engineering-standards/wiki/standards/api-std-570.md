---
title: "API Standard 570 — Piping Inspection Code: In-service Inspection, Rating, Repair, and Alteration of Piping Systems"
slug: api-std-570
code_id: api-std-570
publisher: API
revision: "4th ed (2024); current published edition. Earlier editions: 1st (1993), 2nd (1998), 3rd (2016)."
jurisdiction: "Industry standard for refining, petrochemical, and offshore in-service piping inspection; widely cited by US OSHA PSM mechanical-integrity programmes (29 CFR 1910.119) and by flag-state offshore regimes for topsides piping."
instrument_type: specification
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/standard-570
tags:
  - api
  - api-std
  - piping
  - in-service-inspection
  - integrity-management
  - rbi-host
  - ffs-gate
  - inspection-trilogy
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Standard 570 — Piping Inspection Code

> **Slug-canonicalisation note.** This page uses the `api-std-NNN` canonical slug form (matching siblings [api-std-579](api-std-579.md), [api-std-1104](api-std-1104.md), [api-std-2rd](api-std-2rd.md)). The existing fuller treatment lives at [api-570](api-570.md) under a legacy slug; both pages reference the same publisher document. Practitioners should treat [api-570](api-570.md) as the substantive landing page and this resolver as the canonical-slug entry point.

> **code_id:** `api-std-570` · **publisher:** API · **revision:** 4th ed (2024)

## Scope

API Standard 570 is the **owner-user inspection code** governing in-service inspection, rating, repair, and alteration of metallic piping systems in process and refining plants. It applies to piping originally designed and constructed under [asme-b31-3](asme-b31-3.md) (Process Piping) and, by analogy, sister B31 piping codes — once the system has been placed in service. API 570 is the piping companion to [api-510](api-510.md) (pressure vessels) and [api-653](api-653.md) (atmospheric storage tanks): together the three codes form the **API in-service inspection trilogy** that owner-user organisations cite as the authoritative basis for fixed-equipment integrity programmes in refining and petrochemicals.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1993 | Original issue |
| 2nd ed | 1998 | Addenda 1–3 published 1999–2003 |
| 3rd ed | 2016 | Major revision; expanded RBI integration with [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) |
| 4th ed | 2024 | Current published edition |

Catalog presence: legacy on-disk copies (1998 + 2001 + 2006-addenda editions) are referenced from [api-570](api-570.md). Current edition not on disk; obtain via publisher catalog.

## Key sections

- **Inspection programme governance.** Owner-user written inspection programme, inspector qualification, inspection records, repair/alteration approval workflow.
- **Classification of piping systems.** Class 1 (highest consequence) through Class 3 (lowest); class drives default inspection intervals.
- **Inspection intervals.** Default half-life or fixed-interval rules; explicit RBI alternative per [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md).
- **Thickness measurement and Condition Monitoring Locations (CMLs).** CML selection, UT-thickness practice (cross-routes to [api-rp-574](api-rp-574.md) and [api-rp-577](api-rp-577.md) for execution-grade practice).
- **Corrosion-rate calculation and remaining life.** Long-term and short-term corrosion rates (LTCR/STCR); the larger governs — see [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md).
- **Repair and alteration rules.** Permitted welding procedures, hot-tap rules, NDE acceptance for in-service repairs.
- **Pressure testing and re-rating.** When pressure testing is required after repair vs. when re-rating by calculation suffices.

Clause text, acceptance tables, and worked examples are **not reproduced** per metadata-only governance.

## Practitioner application

API 570 is the code an owner-user cites when defending an in-service piping inspection programme to a regulator (US OSHA, BSEE, EPA RMP) or to a third-party auditor. It is also the code a fitness-for-service ([api-std-579](api-std-579.md)) assessor cites when documenting how the inspection data feeding the FFS analysis was collected and qualified. RBI implementations under [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) explicitly cite §6 of API 570 as their authority to deviate from default fixed intervals.

## Industry adoption

Cited by reference in US OSHA Process Safety Management (29 CFR 1910.119(j)) for mechanical-integrity programmes covering process piping. Adopted as the de-facto inspection standard for refinery and petrochemical piping in North America and widely referenced internationally via owner-user programmes.

## Why this page exists

W208 (iter-45) identified API 570 as a top-24 wikilink target with a substrate-gap cluster around inspection-domain concepts. This page provides a canonical-slug entry point ([api-std-570](api-std-570.md)) aligned with the [api-std-579](api-std-579.md) / [api-std-1104](api-std-1104.md) sibling convention, while the substantive content remains at the legacy-slug page [api-570](api-570.md).

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. API 570 is sold individually and in API Inspection Codes packages. Legacy on-disk editions are recorded in the [og-standards-api](../sources/og-standards-api.md) source page; current edition not in repo (vendor-derivative deny-list per spinout 2026-05-05 governance).

## Cross-references

- [api-570](api-570.md) — legacy-slug full page; substantive scope, edition history, and practitioner detail.
- [api-510](api-510.md) — pressure-vessel inspection code; sibling in the inspection trilogy.
- [api-653](api-653.md) / [api-std-653](api-std-653.md) — atmospheric storage tank inspection code; sibling in the inspection trilogy.
- [api-rp-572](api-rp-572.md) — inspection practices for pressure vessels (companion practice to [api-510](api-510.md)).
- [api-rp-574](api-rp-574.md) — inspection practices for piping system components (companion practice to this code).
- [api-rp-576](api-rp-576.md) — inspection of pressure-relieving devices.
- [api-rp-577](api-rp-577.md) — welding inspection and metallurgy.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology and quantitative basis cited as alternative to default intervals.
- [api-std-579](api-std-579.md) — fitness-for-service framework consuming API 570 inspection data.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS workflow.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI alternative interval-setting.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor for LTCR/STCR rate calculation.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes an API 570 inspection-interval, CML-spacing, or remaining-life value.
