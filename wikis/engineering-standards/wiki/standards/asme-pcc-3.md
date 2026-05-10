---
title: "ASME PCC-3 — Inspection Planning Using Risk-Based Methods"
slug: asme-pcc-3
code_id: asme-pcc-3
publisher: ASME
publisher_full: "American Society of Mechanical Engineers"
revision: "2022 (current edition); prior editions 2007, 2017"
jurisdiction: "US (cross-referenced with API RBI publications); international by adoption"
instrument_type: standard
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.asme.org/codes-standards
public_url: https://www.asme.org/codes-standards/find-codes-standards/pcc-3-inspection-planning-using-risk-based-methods
publisher_catalog_url: https://www.asme.org/codes-standards
tags:
  - asme
  - standards
  - rbi
  - inspection-planning
  - post-construction
  - fixed-equipment
  - risk-based
  - metadata-only
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# ASME PCC-3 — Inspection Planning Using Risk-Based Methods

**code_id:** `asme-pcc-3` &nbsp;·&nbsp; **publisher:** ASME (American Society of Mechanical Engineers) &nbsp;·&nbsp; **revision:** 2022

> Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, likelihood-of-failure tables, consequence-of-failure factors, or example RBI calculation tables from the source.

## Scope

ASME PCC-3 is the ASME Post-Construction Committee standard for **risk-based inspection (RBI) planning** of fixed pressure-containing equipment in process plants — pressure vessels, piping, atmospheric and low-pressure storage tanks, heat exchangers, boilers (where applicable), and pressure-relief devices. It is one of the three pillars of the ASME Post-Construction Code (PCC) family, alongside [asme-pcc-1](asme-pcc-1.md) (bolted-flange joint assembly) and ASME PCC-2 (repair of pressure equipment).

The standard provides a publisher-neutral methodology framework for RBI: goal-setting, screening, qualitative / semi-quantitative / quantitative analysis pathways, damage-mechanism identification, likelihood-of-failure (POF) and consequence-of-failure (COF) determination, risk ranking, inspection-plan development, evergreen documentation, and management-of-change for the RBI process. Methodology is broadly aligned with — and is the ASME-side counterpart to — [api-rp-580](api-rp-580.md) (RBI principles) and [api-rp-581](api-rp-581.md) (quantitative RBI methodology), with PCC-3 emphasising a code-neutral methodology framework rather than API-specific formulae.

## Revision history

- **ASME PCC-3-2007** — first edition; risk-based inspection planning for fixed equipment.
- **ASME PCC-3-2017** — second edition; alignment refresh with API RP 580/581 and PCC-2 repair scope.
- **ASME PCC-3-2022** — current edition; incorporates evergreen-process clarifications and updated damage-mechanism cross-references.

## Key sections

Section structure (verify against the publisher copy in any normative work):

- **Introduction and scope** — applicability to fixed equipment; exclusions (rotating machinery, structural steel, transmission pipelines).
- **Planning and team formation** — RBI team composition (inspection, materials, process, mechanical, reliability).
- **Data and information collection** — equipment inventory, design basis, operating history, prior inspection record.
- **Damage-mechanism identification** — corrosion, cracking, mechanical, metallurgical, environmental degradation; cross-references to [api-rp-571](api-rp-571.md).
- **Likelihood-of-failure determination** — qualitative / semi-quantitative / quantitative approaches; degradation-rate and condition-confidence inputs.
- **Consequence-of-failure determination** — safety, environmental, business-interruption, repair-cost categorization.
- **Risk ranking** — matrix or numerical risk values; thresholds for inspection-priority assignment.
- **Inspection plan development** — task selection, interval setting, NDE technique selection, coverage assignment.
- **Evergreen RBI** — re-assessment triggers, MOC for RBI, documentation lifecycle.
- **Roles and responsibilities** — owner-user, inspector, RBI analyst, jurisdictional authority interfaces.

## Practitioner application

- Refining and petrochemical operators running plant-wide RBI programs; PCC-3 is the publisher-neutral methodology citation when API RP 580/581 cannot be normatively invoked.
- Mechanical-integrity engineers in process facilities outside the API RP 580/581 ecosystem (e.g., chemical plants, specialty-chemicals sites, fertilizer facilities).
- Risk and reliability consultancies (DNV, ABS Group, Lloyd's Register, Equity Engineering, Bechtel, Bureau Veritas) executing RBI programs for owner-operators and benchmarking against PCC-3.
- Regulatory and jurisdictional authorities accepting PCC-3-based RBI plans as a methodology framework alongside API-RP-580/581 deliverables.

## Industry adoption

ASME PCC-3 is the standard publisher-neutral RBI methodology citation in the US process-industry mechanical-integrity community, complementing the API-specific RBI publications. It is recognized internationally where ASME post-construction standards have been adopted as part of jurisdictional pressure-equipment regulations or operator MI programs. RBI practitioners commonly cite both PCC-3 (methodology framework) and API RP 580/581 (procedure) within the same RBI plan to satisfy both publisher families' framing.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md` and substrate-fill landing for the wikilink in `api-rp-580.md` referencing ASME PCC-3. Surfaced as 1 of 5 ASME-process/RBI substrate-gap residuals after iter-50 W231 sweep; created under iter-51 W232 ASME-process/RBI substrate-fill batch. **Metadata-only** per spinout 2026-05-05 governance.

## Where to find the full text

ASME publications subscription required; ANSI catalog also lists the document. Vendor-derivative full text is **not** stored in this repo per spinout vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [api-rp-580](api-rp-580.md) — API RBI principles; methodologically aligned API-side counterpart.
- [api-rp-581](api-rp-581.md) — API quantitative RBI methodology; detailed-procedure companion to PCC-3 framework.
- [api-rp-571](api-rp-571.md) — damage-mechanism reference cross-cited from PCC-3.
- [asme-pcc-1](asme-pcc-1.md) — Pressure-boundary bolted-flange joint assembly; sister PCC-family standard.
- [api-510](api-510.md) — Pressure-vessel inspection code; jurisdictional code that consumes RBI inspection-plan output.
- [api-570](api-570.md) — Piping inspection code; jurisdictional code consuming RBI inspection-plan output.
- [api-653](api-653.md) — Tank inspection code; jurisdictional code consuming RBI inspection-plan output.
- [dnv-rp-g101](dnv-rp-g101.md) — DNV offshore-topsides RBI; international peer to PCC-3 + API RP 580/581 for offshore facilities.
- [Risk-Based Inspection (RBI)](../concepts/risk-based-inspection.md) — concept page on RBI paradigm.
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Notes

- This page is **metadata-only**; no clause text, likelihood-of-failure tables, consequence-of-failure factors, or example RBI calculation tables are reproduced from ASME PCC-3. All technical descriptions above are paraphrased general engineering knowledge.
- For normative RBI work, cite the ASME-published edition directly (ASME PCC-3-2022 or the current edition at time of citation).
- Substrate-fill resolver created under W232 iter-51 ASME-process/RBI batch (1 reference in `api-rp-580.md`).
