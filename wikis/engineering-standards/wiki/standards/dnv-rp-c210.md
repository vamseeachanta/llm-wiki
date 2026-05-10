---
title: "DNV-RP-C210 — Probabilistic Methods for Planning of Inspection for Fatigue Cracks in Offshore Structures"
slug: dnv-rp-c210
code_id: dnv-rp-c210
publisher: DNV
publisher_full: "Det Norske Veritas"
revision: "2021-09 (current edition)"
jurisdiction: international (offshore)
instrument_type: recommended-practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.dnv.com/energy/standards-guidelines/dnv-rp-c210-probabilistic-methods-for-planning-of-inspection-for-fatigue-cracks-in-offshore-structures/
public_url: https://www.dnv.com/energy/standards-guidelines/dnv-rp-c210-probabilistic-methods-for-planning-of-inspection-for-fatigue-cracks-in-offshore-structures/
publisher_catalog_url: https://www.dnv.com/energy/standards-guidelines/
tags:
  - dnv
  - standards
  - probabilistic-fatigue
  - inspection-planning
  - rbi
  - offshore
  - reliability
  - metadata-only
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# DNV-RP-C210 — Probabilistic Methods for Planning of Inspection for Fatigue Cracks in Offshore Structures

**code_id:** `dnv-rp-c210` &nbsp;·&nbsp; **publisher:** DNV (Det Norske Veritas) &nbsp;·&nbsp; **revision:** 2021-09

> Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no clause text, reliability-equation reproductions, or POD-curve detail; cite the DNV-published edition for normative use. Vendor PDFs do not enter this repo per spinout 2026-05-05 governance.

## Scope

DNV-RP-C210 is the DNV recommended practice covering **probabilistic methods for planning fatigue-crack inspection campaigns on offshore structures**. It provides the reliability-based inspection (RBI) methodology that translates a deterministic fatigue analysis (typically per [dnv-rp-c203](dnv-rp-c203.md)) into an inspection schedule optimised against probability-of-failure (POF) targets, probability-of-detection (POD) curves of available NDT methods, and consequence-of-failure (COF) cost models.

The recommended practice covers reliability formulation of the fatigue-crack limit state combining S-N curve uncertainty, Miner's rule scatter, environmental-loading uncertainty, and stress-concentration-factor model error; probability-of-detection (POD) curve catalogues for the principal offshore NDT methods (MPI, eddy current, ACFM, ultrasonic, flooded-member detection); Bayesian updating of POF following inspection campaigns with no-find or find-and-repair outcomes; cost-benefit optimisation of inspection-schedule sequences against target reliability and operational-availability constraints; and structure-specific application to fixed jacket platforms, jack-ups, semisubmersible MODUs, FPSOs, and floating production-system tendon systems.

## Comparison with API RP 580/581 and BS 7910 Annex N

DNV-RP-C210 is the offshore-fatigue specialisation in a wider RBI ecosystem alongside the API process-equipment RBI codes [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) and the [bs-7910](bs-7910.md) Annex N probabilistic FAD route:

| Dimension | DNV-RP-C210 | API RP 580/581 | BS 7910 Annex N |
|---|---|---|---|
| Asset class | Offshore steel structures (fatigue-driven) | Process equipment (corrosion + fatigue + cracking) | Generic flaw-bearing components |
| Damage mechanism | Fatigue cracks (welded joints, hot-spots) | Multi-mechanism (corrosion, cracking, HTHA, etc.) | Crack-like flaws (FAD-based) |
| Reliability methodology | FORM/SORM + Bayesian inspection updating | Damage-factor + qualitative-to-quantitative ladder | FORM/SORM + FAD-based |
| POD treatment | Method-specific POD curves (MPI / EC / ACFM / UT / FMD) | Method-specific POD per damage class | FORM input distribution |
| NDT calibration | Subsea-environment-aware (water-clarity, vessel access) | Onshore + topside refinery context | Generic |
| Output | Risk-ranked inspection schedule per detail | Risk-ranked inspection schedule per equipment item | POF estimate per flaw |

DNV-RP-C210 is purpose-built for fatigue-crack inspection planning on welded offshore steel structural details, which is a different scope from the multi-mechanism process-equipment RBI of API 580/581 and the generic flaw-assessment scope of BS 7910 Annex N. Practitioners running an integrated offshore platform integrity-management programme typically use DNV-RP-C210 for jacket/topside-structural-fatigue inspection planning, [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) for topside process-equipment inspection planning, and [bs-7910](bs-7910.md) for any specific FFS findings flagged during inspection.

## Edition history

- **DNV-RP-C210:2015** — first edition issued, consolidating earlier DNV ad-hoc reliability-based-inspection guidance into a recommended practice.
- **DNV-RP-C210:2019** — second edition; updated POD curve catalogue, expanded to floating-structure tendon and mooring applications.
- **DNV-RP-C210:2021-09** — current edition at time of writing.

Consult the DNV catalog (https://www.dnv.com/energy/standards-guidelines/) for any subsequent amendments before normative citation.

## Key sections (informative pointer)

The 2021-09 edition's section structure is the working surface for most calc modules:

- **Section 1-2** — General; references; terms and abbreviations.
- **Section 3** — Reliability formulation of the fatigue-crack limit state.
- **Section 4** — Inspection planning methodology; cost-benefit optimisation.
- **Section 5** — Probability of detection (POD) curves for offshore NDT methods.
- **Section 6** — Bayesian updating; no-find / find / repair outcome treatment.
- **Section 7** — Application to specific offshore structure types.
- **Annexes** — Worked examples; reference reliability indices; POD-curve fitting parameters; cost-model templates.

> Section numbers are stable within DNV-RP-C210:2021-09; verify against the publisher edition for normative work.

## Practitioner application

- Offshore-platform integrity-management engineers planning multi-year inspection campaigns on fixed jacket platforms (e.g., North Sea, Gulf of Mexico, Bohai, Brazilian Basin assets).
- FPSO / FLNG / FSRU integrity-management teams planning hull and topside-structure inspection schedules under reliability-based optimisation.
- Floating production system (semisubmersible, tendon, mooring) inspection-planning specialists pairing DNV-RP-C210 reliability output with [dnv-os-e301](dnv-os-e301.md) mooring-integrity provisions and [api-rp-2mim](api-rp-2mim.md) mooring-integrity-management practice.
- Class societies — DNV, ABS, BV, LR — accepting DNV-RP-C210-based reliability arguments in lieu of prescriptive periodic inspection where the asset-specific reliability case demonstrates equivalent or superior coverage.
- Offshore EPCs preparing inspection-and-monitoring philosophy documents for greenfield-platform deliverables, where DNV-RP-C210 provides the design-stage RBI framework.

## Cross-references

- [dnv-rp-c203](dnv-rp-c203.md) — DNV deterministic fatigue-design RP; supplies the S-N curves, hot-spot stress methodology, and SCF catalogue that DNV-RP-C210 wraps in a reliability framework.
- DNV-OS-C401 — DNV offshore-structures fabrication-and-testing standard (resolver-page TBD); the inspection-method specification and acceptance criteria DNV-RP-C210 plans against during construction.
- [api-rp-2a-wsd](api-rp-2a-wsd.md) — API fixed-platform planning/design code; DNV-RP-C210 is the RBI complement on API-RP-2A-designed platforms.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — API process-equipment RBI codes; complementary scope (process equipment vs. structural-fatigue).
- [bs-7910](bs-7910.md) — UK fitness-for-service code; Annex N is the parallel UK reliability-based FAD route.
- [bs-7608](bs-7608.md) — UK fatigue-design code; complementary deterministic-fatigue substrate when offshore-onshore mixed projects span both jurisdictions.
- [dnv-os-e301](dnv-os-e301.md) — DNV position-mooring code; mooring-line fatigue inspection planning per DNV-RP-C210 reliability framework.
- [Fatigue Design and Assessment](../concepts/fatigue-design-and-assessment.md) — concept page on deterministic-fatigue substrate underlying DNV-RP-C210.
- [Risk-Based Inspection (RBI)](../concepts/risk-based-inspection.md) — concept page on RBI methodology; DNV-RP-C210 is the offshore-fatigue specialisation.
- [Fitness-for-Service (FFS)](../concepts/fitness-for-service.md) — concept page on FFS; DNV-RP-C210 inspection findings feed FFS evaluation per [bs-7910](bs-7910.md) / [api-579-1-asme-ffs-1](api-579-1-asme-ffs-1.md).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Where to find the full text

DNV catalog: https://www.dnv.com/energy/standards-guidelines/dnv-rp-c210-probabilistic-methods-for-planning-of-inspection-for-fatigue-cracks-in-offshore-structures/. Vendor-derivative full text is **not** stored in this repo per workspace-hub vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Notes

- This page is **metadata-only**; no clause text, reliability equations, POD-curve fits, or cost-model parametrisations are reproduced from the DNV-RP-C210 PDFs. All technical descriptions above are paraphrased general engineering knowledge.
- For normative offshore-platform inspection-planning work, cite the DNV-published edition directly (DNV-RP-C210:2021-09 or the current edition at time of citation).
- Substrate-fill resolver created under W215 iter-46 ECA/fracture cluster gap-closure (W212 V10 P1b).
