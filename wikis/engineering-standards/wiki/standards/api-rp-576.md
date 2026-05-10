---
title: "API Recommended Practice 576 — Inspection of Pressure-Relieving Devices"
slug: api-rp-576
code_id: api-rp-576
publisher: API
revision: "4th ed (2017); current published edition. Earlier editions: 1st (1981), 2nd (2000), 3rd (2009)."
jurisdiction: "Industry recommended practice for refining, petrochemical, and offshore inspection and shop-test of pressure-relieving devices; consumed through owner-user mechanical-integrity programmes."
instrument_type: recommended-practice
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/recommended-practice-576
tags:
  - api
  - api-rp
  - pressure-relief
  - prv
  - rupture-disk
  - inspection-practice
  - mechanical-integrity
  - osha-psm
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Recommended Practice 576 — Inspection of Pressure-Relieving Devices

> **code_id:** `api-rp-576` · **publisher:** API · **revision:** 4th ed (2017); current published edition.

## Scope

API RP 576 is the **inspection-and-shop-test practice** for **pressure-relieving devices (PRDs)** in process service: spring-loaded pressure relief valves (PRVs), pilot-operated PRVs, balanced-bellows PRVs, rupture disks (forward-acting and reverse-buckling), pin-actuated devices, and the combination installations (rupture-disk-upstream-of-PRV, parallel-PRV) that protect refinery, petrochemical, and offshore process equipment from overpressure. The practice covers visual inspection, in-place testing where permitted, removal-and-shop-bench testing, set-pressure verification, leak-tightness verification (API 527), repair, refurbishment, and re-installation. RP 576 is the **execution-grade companion** to the design and sizing codes API Std 520 (sizing) and API Std 521 (system design) — first-class standards-page candidates not yet in the wiki; together they form the API pressure-relief code family.

RP 576 is **not** a code — it cannot be invoked as a compliance authority on its own; it is invoked **through** the owner-user's mechanical-integrity programme, which in US jurisdictions is itself driven by OSHA PSM 29 CFR 1910.119(j) and EPA RMP 40 CFR 68.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1981 | Original issue |
| 2nd ed | 2000 | Updated test-frequency guidance |
| 3rd ed | 2009 | Expanded RBI alignment for PRD interval-setting |
| 4th ed | 2017 | Current published edition; expanded pilot-operated and rupture-disk coverage |

Catalog presence: not currently on disk in `/mnt/ace/O&G-Standards/API/`; obtain via publisher catalog.

## Key sections

The headings below summarise the practice's structural backbone — clause text, acceptance tables, and worked test-bench procedures are **not reproduced** per metadata-only governance.

- **Inspection types.** Visual external (corrosion, plugging, leakage, mechanical damage, tampering); in-place leak test where service permits; shop-bench test on a calibrated test stand against a master gauge or transfer standard; teardown inspection of internals (disc, seat, nozzle, bellows, pilot, rupture-disk membrane).
- **Test frequency.** Default fixed intervals tied to service severity (clean / mild / severe / fouling); RBI-driven intervals as an alternative under owner-user programmes that conform to [api-rp-580](api-rp-580.md). Fouling and corrosive services demand shorter intervals; clean utility services tolerate longer intervals.
- **Set-pressure verification.** Pop-test on a calibrated bench; allowable tolerance per ASME BPVC Section I or VIII (typically ±3% of cold-differential test pressure for higher-pressure service, ±2 psi for low-pressure service). Out-of-tolerance valves are repaired or replaced.
- **Leak-tightness verification.** API 527 air or steam leak-test against the seat at 90% of set pressure for spring-loaded PRVs; bellows-balanced PRVs additionally bellows-leak-tested.
- **Rupture-disk inspection.** Visual examination for buckling, fatigue, corrosion, scoring, or evidence of pulsation damage; replacement cycles tied to manufacturer-specified service life and to owner-user fatigue analysis.
- **Pilot-operated PRV.** Pilot-section disassembly, pilot-supply-line filter inspection, dome-leakage check, pilot reset-pressure verification.
- **Combination installations.** Rupture-disk-upstream-of-PRV interspace pressure-monitoring and disk-replacement triggers; parallel-PRV staggered-set-pressure verification.
- **Records and traceability.** Test-stand calibration records, master-gauge traceability, repair-history file per device serial number, and disposition recommendation feeding the owner-user mechanical-integrity programme.

## Practitioner application

API RP 576 is the practice a relief-valve shop and an owner-user inspection group consult when planning and executing the in-service test, repair, and shop-bench programme for PRDs. RBI implementations under [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) cite RP 576 as the source of inspection-effectiveness factors for PRD damage-mechanism POF updating. Process safety management auditors verify RP 576 conformance as part of the PSM mechanical-integrity element.

## Industry adoption

Universally adopted in North American refining and petrochemical industries as the inspection-and-shop-test practice underpinning the PRD population. Widely cited internationally via owner-user programmes. Recognised by US OSHA PSM auditors and US EPA RMP auditors as the practice that defines the competent inspection-and-test standard for relieving devices.

## Why this page exists

W208 (iter-45) identified API RP 576 as a top-24 wikilink target with a substrate-gap cluster around inspection-domain concepts. The practice is heavily cited from concepts covering fitness-for-service, risk-based-inspection, and relief-system design, but lacked a first-class standards page until this resolver landed.

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. RP 576 is sold individually and in API Inspection Practices packages.

## Cross-references

- API Std 520 — *Sizing, Selection, and Installation of Pressure-Relieving Devices* (Pt 1 sizing, Pt 2 installation). Design-side companion to this inspection practice. Future first-class standards page candidate.
- API Std 521 — *Pressure-Relieving and Depressuring Systems.* System-design-side companion. Future first-class standards page candidate.
- [api-510](api-510.md) — pressure-vessel inspection code; the vessels protected by RP 576-inspected PRDs.
- [api-rp-572](api-rp-572.md) — inspection practices for pressure vessels; sister inspection practice.
- [api-rp-571](api-rp-571.md) — damage mechanisms affecting fixed equipment; corrosion mechanisms affecting PRD nozzles, seats, and bellows.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology and quantitative basis cited as alternative to default PRD test intervals.
- [api-std-579](api-std-579.md) — fitness-for-service framework; PRD-related FFS scenarios (set-pressure drift, bellows fatigue) consume RP 576 inspection data.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; PRDs are part of the piping mechanical-integrity scope when installed on protected piping.
- [api-653](api-653.md) / [api-std-653](api-std-653.md) — tank inspection code; atmospheric-tank vacuum/pressure relieving devices fall under RP 576 inspection scope.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS workflow.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI alternative interval-setting.
- Concept anchor for relief-system design (sizing and system-design context) — future concept-page candidate that this RP will route into.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes an RP 576 test-frequency interval, set-pressure tolerance, or PRD inspection-effectiveness factor.
