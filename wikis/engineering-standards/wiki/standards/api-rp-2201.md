---
title: "API Recommended Practice 2201 — Safe Hot Tapping Practices in the Petroleum and Petrochemical Industries"
slug: api-rp-2201
code_id: api-rp-2201
publisher: API
revision: "6th ed (2018); current published edition. Earlier editions: 1st (1955), 2nd (1969), 3rd (1985), 4th (1995), 5th (2003)."
jurisdiction: "Industry recommended practice for in-service hot-tapping and isolation of pressurised piping and equipment in refining, petrochemical, and pipeline service; cited by US OSHA PSM, EPA RMP, and pipeline-operator integrity programmes."
instrument_type: recommended-practice
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/recommended-practice-2201
tags:
  - api
  - api-rp
  - hot-tap
  - in-service-welding
  - line-stop
  - isolation
  - safe-work-practices
  - welding-on-pressurized-equipment
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Recommended Practice 2201 — Safe Hot Tapping Practices

> **code_id:** `api-rp-2201` · **publisher:** API · **revision:** 6th ed (2018); current published edition.

## Scope

API RP 2201 is the **safe-work practice for hot tapping** — the technique of welding a branch fitting onto, and then drilling through, a pressurised in-service piping or vessel wall to add a new connection without taking the system out of service. The practice covers the full hot-tap workflow: candidate-line evaluation (pressure, temperature, fluid, wall thickness, deposit / scale conditions), fitting design and pressure rating, in-service welding qualification per [api-std-1104](api-std-1104.md) Appendix B (or analogous welding-procedure rules), tap-machine selection and operation, coupon retrieval, pressure testing, and the related **line-stop** technique used to isolate sections downstream of a hot tap. RP 2201 is the safety-and-procedure complement to the welding-procedure rules in [api-std-1104](api-std-1104.md) Appendix B (pipelines) and to in-service welding rules in ASME B31 codes — RP 2201 says **whether and how** to do the work, not the specific weld parameters.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1955 | Original issue |
| 2nd ed | 1969 | Refinery and pipeline coverage broadened |
| 3rd ed | 1985 | Updated welding qualification linkage |
| 4th ed | 1995 | Expanded line-stop coverage |
| 5th ed | 2003 | Burnthrough-risk methodology added |
| 6th ed | 2018 | Current published edition; expanded burnthrough risk-screening, hot-tap on thin-wall and high-pressure pipelines, alignment with [api-std-1104](api-std-1104.md) Appendix B |

Catalog presence: not currently on disk in `/mnt/ace/O&G-Standards/API/`; obtain via publisher catalog.

## Key sections

The headings below summarise the practice's structural backbone — clause text, burnthrough-risk tables, and procedure templates are **not reproduced** per metadata-only governance.

- **Hot-tap candidate evaluation.** Pressure, temperature, fluid composition (flammability, toxicity, hydrogen content, sour-service), wall thickness, internal-deposit and scale conditions, prior-damage and fitness-for-service screening per [api-std-579](api-std-579.md).
- **Burnthrough risk.** Heat-affected-zone weakening risk during in-service welding; minimum-wall criteria, heat-input limits, and analytical / FEA screening for thin-wall lines.
- **Hydrogen-cracking risk.** In-service welding cools fast under flowing process fluid — accelerated cooling rates can produce hard, crack-susceptible HAZ microstructures; controls per [api-std-1104](api-std-1104.md) Appendix B and welding-procedure qualification.
- **Fitting design.** Branch-fitting types (saddle, weld-o-let, full-encirclement reinforcement sleeve), pressure rating, materials.
- **Welding procedure.** Welder qualification, procedure qualification (PQR), in-service-welding-specific procedure controls; cross-route to [api-rp-577](api-rp-577.md) for welding inspection.
- **Tap machine and coupon retrieval.** Tap-machine selection by pressure / size class; coupon retention to prevent loose-coupon ingress; pressure-testing the new connection.
- **Line-stop technique.** Use of a hot-tap-installed line-stop fitting and plugging head to isolate a section of pipe for repair without full system shutdown.
- **Personnel safety.** Hot-work permits, fire-watch, gas testing, ignition-source control, evacuation criteria.
- **Prohibited services.** Services where hot-tapping is prohibited or requires special engineering review — e.g., oxygen, ethylene, hydrogen above HTHA threshold, certain monomers, dead-leg / no-flow conditions that defeat heat-sink assumptions.

## Practitioner application

API RP 2201 is the practice cited by:
- **Maintenance and turnaround engineers** evaluating whether a planned tie-in can be hot-tapped vs requiring a full shutdown.
- **Pipeline integrity engineers** authorising in-service welding repairs on pipelines under [api-std-1104](api-std-1104.md) Appendix B.
- **In-service welding contractors** qualifying procedures and operators for hot-tap work.
- **Process safety engineers** screening hot-tap proposals against PSM management-of-change requirements (OSHA 29 CFR 1910.119).
- **FFS assessors** working under [api-std-579](api-std-579.md) when a hot-tap is proposed on a degraded line; the FFS evaluates whether the line has the remaining wall to tolerate the hot-tap heat input.

## Industry adoption

Universally adopted in North American refining, petrochemical, and pipeline industries as the safe-work-practice authority for in-service welding and hot-tapping. Cited by US OSHA PSM auditors, EPA RMP audits, and pipeline-operator integrity-management programmes (49 CFR 192 / 195) as the credible practice for hot-tap work on pressurised piping.

## Why this page exists

W215 (iter-46) flagged API RP 2201 as a missing API inspection-domain slug cross-referenced from concepts/{welding-procedures-and-acceptance, fitness-for-service} but lacking a first-class standards page. This resolver closes the substrate gap and gives in-service welding, FFS, and turnaround-planning workflows a citation target.

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. RP 2201 is sold individually.

## Cross-references

- [api-std-1104](api-std-1104.md) — pipeline welding code; Appendix B governs in-service welding-procedure qualification used by hot-tap work.
- [api-rp-577](api-rp-577.md) — welding inspection and metallurgy; companion inspection practice.
- [api-rp-578](api-rp-578.md) — material verification (PMI); applies to verifying that the fitting matches the line alloy before hot-tap weld is made.
- [api-510](api-510.md) — pressure-vessel inspection code; hot-tap on a vessel is governed by 510 repair-and-alteration rules.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; hot-tap on process piping is governed by 570 repair-and-alteration rules.
- [api-rp-572](api-rp-572.md) — pressure-vessel inspection practice; companion in-service inspection practice.
- [api-std-579](api-std-579.md) / [api-579-1-asme-ffs-1](api-579-1-asme-ffs-1.md) — fitness-for-service framework; FFS screens hot-tap candidates with prior wall loss.
- [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md) — concept anchor for welding-procedure qualification, including in-service welding.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS screening of hot-tap candidates.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes an RP 2201 burnthrough-risk threshold or minimum-wall criterion.
