---
title: "API Recommended Practice 572 — Inspection Practices for Pressure Vessels"
slug: api-rp-572
code_id: api-rp-572
publisher: API
revision: "4th ed (2016); current published edition. Earlier editions: 1st (1980), 2nd (2001), 3rd (2009)."
jurisdiction: "Industry recommended practice for refining, petrochemical, and offshore in-service pressure-vessel inspection execution; consumed through owner-user programmes anchored on API 510."
instrument_type: recommended-practice
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/recommended-practice-572
tags:
  - api
  - api-rp
  - pressure-vessels
  - inspection-practice
  - ndt
  - cml
  - ut-thickness
  - rbi-input
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Recommended Practice 572 — Inspection Practices for Pressure Vessels

> **code_id:** `api-rp-572` · **publisher:** API · **revision:** 4th ed (2016); current published edition.

## Scope

API RP 572 is the **inspector-grade practice companion** to [api-510](api-510.md) (the pressure-vessel inspection code). It documents recommended practices for the **inspection methods, frequencies, and reporting** applied to fixed pressure vessels in process service — towers, drums, reactors, heat exchangers, separators, accumulators, and the welded internals (trays, supports, distributors, baffles, refractory, weld-overlay cladding) that those vessels contain. Where [api-510](api-510.md) is the **owner-user code** that sets policy (classification, intervals, who is responsible), RP 572 is the **field-execution practice guide** that tells inspectors and NDE examiners how to actually find wall loss, cracking, mechanical damage, and internal degradation on those vessels. RP 572 is **not** a code — it cannot be invoked as a compliance authority on its own; it is invoked **through** [api-510](api-510.md) or the owner-user's written inspection programme.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1980 | Original issue |
| 2nd ed | 2001 | Updated NDE method coverage |
| 3rd ed | 2009 | Expanded RBI alignment, internal-attachment guidance |
| 4th ed | 2016 | Current published edition; expanded PAUT, guided-wave UT, and through-insulation screening |

Catalog presence: not currently on disk in `/mnt/ace/O&G-Standards/API/`; obtain via publisher catalog.

## Key sections

The headings below summarise the practice's structural backbone — clause text, NDE acceptance tables, and CML-spacing tabulations are **not reproduced** per metadata-only governance.

- **Inspection types.** External and internal visual; UT thickness (spot and scan); RT (radiographic); MT (magnetic particle); PT (liquid penetrant); ECT (eddy current); AET (acoustic emission); IR thermography; PAUT (phased-array UT); guided-wave UT; pulsed eddy current for through-insulation screening.
- **Vessel classification and inspection scope.** Inspection scope tied to vessel classification under [api-510](api-510.md); high-consequence vessels demand wider CML coverage and tighter NDE acceptance.
- **Internal attachments.** Tray supports, downcomers, distributor headers, weld-overlay cladding integrity, refractory anchor system condition, and cyclone-separator wear in fluid catalytic cracking service.
- **CML selection and thickness measurement.** Condition Monitoring Location selection on shell, heads, nozzles, and circumferential/longitudinal welds; UT-thickness practice and statistical sampling for buried sections.
- **Damage-mechanism-specific inspection.** Inspection method targeted at the credible damage mechanism — CUI under insulation, HTHA in hot-hydrogen service, sulfidation in high-temperature crude/vacuum service, hydrogen blistering and HIC in wet-H2S service. Cross-route to [api-rp-571](api-rp-571.md).
- **Inspection windows.** Off-stream (shutdown, vessel isolated and depressurized, internal entry permitted under confined-space rules) versus on-stream (live, with personnel-protection requirements).
- **Inspection report content.** Required content of the inspection report that records findings against [api-510](api-510.md) acceptance criteria, including disposition recommendations.

## Practitioner application

API RP 572 is the practice an inspector or NDE technician consults when planning the field-execution of an [api-510](api-510.md) inspection. It is also the practice an FFS ([api-std-579](api-std-579.md)) assessor cites when documenting how the inspection data feeding the FFS analysis was collected. RBI implementations under [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) cite RP 572 as the authoritative source for inspection-method effectiveness factors that go into POF updating.

## Industry adoption

Universally adopted in North American refining and petrochemical industries as the inspection-execution practice underpinning API 510 programmes. Widely cited internationally via owner-user programmes. Recognised by US OSHA PSM auditors as the practice that defines a competent inspection-execution standard.

## Why this page exists

W208 (iter-45) identified API RP 572 as a top-24 wikilink target with a substrate-gap cluster around inspection-domain concepts. The practice is heavily cited from concepts/{fitness-for-service, risk-based-inspection} but lacked a first-class standards page until this resolver landed.

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. RP 572 is sold individually and in API Inspection Practices packages.

## Cross-references

- [api-510](api-510.md) — pressure-vessel inspection code; this RP is its execution-grade companion.
- [api-rp-571](api-rp-571.md) — damage mechanisms affecting fixed equipment; the credible-mechanism catalogue that targets RP 572 inspection-method selection.
- [api-rp-574](api-rp-574.md) — inspection practices for piping system components; piping-side sibling of this RP.
- [api-rp-576](api-rp-576.md) — inspection of pressure-relieving devices; PRV-side sibling of this RP.
- [api-rp-577](api-rp-577.md) — welding inspection and metallurgy; weld-quality complement.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology and quantitative basis consuming RP 572 inspection-effectiveness factors.
- [api-std-579](api-std-579.md) — fitness-for-service framework consuming RP 572 inspection data.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; trilogy-sibling.
- [api-653](api-653.md) / [api-std-653](api-std-653.md) — tank inspection code; trilogy-sibling.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS workflow.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI alternative interval-setting.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes an RP 572 inspection-effectiveness factor or NDE detection threshold.
