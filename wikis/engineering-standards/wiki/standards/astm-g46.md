---
title: "ASTM G46 — Standard Guide for Examination and Evaluation of Pitting Corrosion (bounded resolver)"
slug: astm-g46
tags: ["astm", "g-series", "corrosion", "pitting", "examination", "rating-chart", "pit-depth", "guide", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g46
publisher: ASTM
revision: "G46-94 (R2018) — publisher-current; local catalog holds G46 with 1 edition"
publisher_current_edition: "G46-94 (R2018)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: guide
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0046-94r18.html
public_url: https://www.astm.org/g0046-94r18.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G46 — Standard Guide for Examination and Evaluation of Pitting Corrosion (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, rating-chart figure reproductions, pit-density-class numerics, or photographic-reference reproductions are included.
> **code_id:** `astm-g46` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.05 on Laboratory Corrosion Tests) &nbsp;•&nbsp; **revision:** G46-94 reapproved most recently as G46-94(R2018). The local O&G-Standards catalog records G46 with **1 edition** in the corpus.

## Scope

ASTM G46 is the **examination-and-evaluation guide** for pitting corrosion: it codifies the post-exposure inspection workflow that turns a pitted coupon, ILI-detected feature, or in-service-inspected component face into a **quantitative pit-depth + pit-density + pit-morphology dataset** suitable for engineering analysis. G46 is the cited examination-and-rating reference of [astm-g48](astm-g48.md) (FeCl3 pitting/crevice test), [astm-g31](astm-g31.md) (immersion testing), [astm-g1](astm-g1.md) (mass-loss reporting when pits accompany the result), [ampp-sp0775](ampp-sp0775.md) (field-coupon pit reporting), and [api-rp-571](api-rp-571.md) damage-mechanism descriptions of pitting attack.

G46 is a **guide**, not a test method — it does not specify a corrosive environment or exposure protocol. It tells the analyst **how to examine** a pitted surface once exposure is complete. The guide carries:

- A **standard rating chart (Figure 2 in the practice)** with pit-density (A1 / A2 / A3 / A4 / A5), pit-size (B1 / B2 / B3 / B4 / B5), and pit-shape categories that allow visual comparison of a coupon face to a canonical reference image and the assignment of an alphanumeric pit-rating descriptor.
- Procedures for **maximum pit depth** measurement (metallographic cross-section, micrometer-depth-gauge probe, optical depth-of-field profiling, laser surface scanning, or X-ray tomography for thicker sections).
- Procedures for **pit-density** count over the exposed area.
- A taxonomy of **pit shape** (narrow-deep, elliptical, wide-shallow, subsurface, undercutting, horizontal, vertical-grain).
- Reporting requirements that pair the maximum, average, and 10-deepest-pit statistics with the pit-density count and the rating-chart category.

## Revision history

The local O&G-Standards catalog records G46 with **1 edition** in the corpus, reflecting a stable post-1994 publisher cycle:

| Edition | Status | Notes |
|---------|--------|-------|
| G46 (early revision) | superseded | 1970s/80s-era examination-guide baseline. |
| G46-94 | active | 1994 revision; the modern technical baseline. |
| G46-94 (Reapproved 2005) | superseded | First reapproval cycle. |
| G46-94 (Reapproved 2018) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

The following are the examination anchors that the guide prescribes (consult the on-disk PDF or publisher catalog for clause-exact text and rating-chart figures):

- **Pre-examination preparation** — mechanical / chemical cleaning per [astm-g1](astm-g1.md) to remove corrosion product without removing significant base metal; surface drying; specimen identification.
- **Visual examination** — overall photographic record at low magnification; identification of pitted regions vs. uniform-corrosion regions vs. crevice-attack regions; comparison to the **standard rating chart (Figure 2)**.
- **Pit density count** — count of distinct pits per unit exposed area (typically per cm² or per dm²); reporting bin categories A1 (lowest density) through A5 (highest density).
- **Pit size and area** — measurement of pit major-axis dimension; reporting bin categories B1 (smallest) through B5 (largest); area-weighted summation for pitted-area-fraction calculation.
- **Pit shape taxonomy** — narrow-and-deep, elliptical, wide-and-shallow, subsurface (mouth narrower than body), undercutting, horizontal microstructural, vertical microstructural.
- **Pit depth measurement** — three principal methods: (a) **metallographic cross-section** through the pit (gold-standard for accuracy, destructive); (b) **micrometer-depth-gauge probe** with a fine-tipped indicator (rapid, non-destructive, less accurate); (c) **optical / laser depth-of-field profiling** (rapid, non-destructive, surface-only — cannot resolve undercut or subsurface pits).
- **Statistical reporting** — maximum pit depth, mean pit depth, 10-deepest-pit summary; pair with extreme-value-statistics tail extrapolation per [astm-g16](astm-g16.md) for inspection-population analyses.
- **Reporting** — required elements: rating-chart category, maximum and mean pit depth, pit-density count, pit shape, pit-area fraction, photographs, and the cleaning-method provenance per G1.

## Practitioner application

- **CRA pitting screening (downstream of G48)** — every G48 result requires a G46 examination workflow: rating-chart comparison, pit-density count, maximum-pit-depth measurement, and shape taxonomy. A G48 result reporting only mass loss without G46 examination data is incomplete.
- **Mass-loss test pitting reporting** — [astm-g1](astm-g1.md) cleaning + [astm-g31](astm-g31.md) immersion datasets that show non-uniform attack require G46 examination to disambiguate uniform-rate from localized-attack components.
- **Field-coupon pit analysis** — [ampp-sp0775](ampp-sp0775.md) field coupons are examined per G46; pit-depth and pit-density populations feed [astm-g16](astm-g16.md) extreme-value statistics for remaining-life forecasts.
- **In-service inspection** — UT pit-depth measurements, ILI pipeline run features, and storage-tank-floor MFL data are summarized using G46 vocabulary even when the underlying measurement is non-destructive and not coupon-based.
- **Fitness-for-service** — G46-derived maximum-pit-depth values feed [api-std-579](api-std-579.md) Part 5 pitting-assessment calc modules; the Part 5 inputs (P, depth, length, width, density) are G46-vocabulary-anchored.
- **Damage-mechanism documentation** — [api-rp-571](api-rp-571.md) pitting-attack descriptions reference G46 for the examination-and-rating substrate.

## Industry adoption

G46 is the **default pitting-examination reference** across refining, oil-and-gas, marine, power, chemical-process, and infrastructure industries. It is the cited examination companion of every G-series localized-corrosion test method (G48, G78, G150) and of every field-coupon and in-service inspection workflow that reports pit-depth populations. A pitted-coupon test report that omits the G46 rating-chart category and the maximum / mean pit-depth summary is regularly flagged in reviewer comments at classification societies (DNV, ABS, BV) and refining inspection programs.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g46` under `.claude/rules/calc-citation-contract.md`. W204 audit V9 surfaced `astm-g46` as a substrate-gap slug — referenced from [astm-g1](astm-g1.md), [astm-g31](astm-g31.md), [astm-g48](astm-g48.md), [astm-g102](astm-g102.md), [ampp-sp0775](ampp-sp0775.md), and the [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) concept page (which explicitly flagged G46 as "future-ingest"). This page closes that flag without reproducing any clause text, rating-chart figures, or photographic-reference content.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0046-94r18.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Primary upstream test method; G48 Method B explicitly invokes G46 for pit and crevice rating.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss baseline that pairs with G46 examination when localized attack accompanies the gravimetric result.
- [astm-g31](astm-g31.md) — *Laboratory Immersion Corrosion Testing of Metals.* Immersion-test substrate; G46 examination required when pitting accompanies uniform attack.
- [astm-g16](astm-g16.md) — *Applying Statistics to Analysis of Corrosion Data.* Extreme-value (Gumbel) tail extrapolation of G46-measured pit-depth populations.
- [astm-g102](astm-g102.md) — *Calculation of Corrosion Rates from Electrochemical Measurements.* Faraday-derived rate is uniform-corrosion equivalent; G46 pit-depth data must be reported alongside whenever localized attack is suspected.
- [astm-g78](astm-g78.md) — *Crevice Corrosion in Seawater.* Sister localized-corrosion test method that consumes G46 examination workflow.
- [ampp-sp0775](ampp-sp0775.md) — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Field-coupon pit-depth and pit-density reporting per G46.
- [api-rp-571](api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Pitting-attack mechanism descriptions reference G46.
- [api-std-579](api-std-579.md) — *API 579-1 / ASME FFS-1 Fitness-for-Service.* Part 5 pitting-assessment input parameters use G46 vocabulary.
- [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — concept anchor; G46 closes the explicit "future-ingest" flag.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor; G46 is the localized-attack examination companion to the rate-measurement methods.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI workflows that consume G46-vocabulary inspection populations.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G46 rating-chart category, pit-density bin threshold, or pit-shape taxonomy term.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording G46 with 1 edition and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0046-94r18.html
