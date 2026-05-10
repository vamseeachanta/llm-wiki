---
title: "ASTM G16 — Standard Guide for Applying Statistics to Analysis of Corrosion Data (bounded resolver)"
slug: astm-g16
tags: ["astm", "g-series", "corrosion", "statistics", "data-analysis", "extreme-value", "guide", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g16
publisher: ASTM
revision: "G16-13 (R2019) — publisher-current; local catalog holds G16 with 2 editions"
publisher_current_edition: "G16-13 (R2019)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: guide
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0016-13r19.html
public_url: https://www.astm.org/g0016-13r19.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G16 — Standard Guide for Applying Statistics to Analysis of Corrosion Data (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, statistical-formula reproductions, distribution tables, or worked-example numerics are included.
> **code_id:** `astm-g16` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals) &nbsp;•&nbsp; **revision:** G16-13 reapproved most recently as G16-13(R2019). The local O&G-Standards catalog records G16 with **2 editions** in the corpus.

## Scope

ASTM G16 is the **statistical-methods guide** for the corrosion-engineering community: it codifies how to design corrosion experiments, summarize replicate-coupon datasets, fit distributions to corrosion-rate and pit-depth data, propagate measurement uncertainty into engineering outputs, and apply **extreme-value statistics** (Gumbel / generalized extreme value) to maximum-pit-depth datasets — the load-bearing application for remaining-life forecasts on tanks, pipelines, vessels, and offshore structures.

G16 is a **guide**, not a test method or practice — it does not specify how to make a corrosion measurement. Instead, it tells the analyst **what to do with the numbers** once measurements have been made by [astm-g1](astm-g1.md) (mass loss), [astm-g31](astm-g31.md) (immersion), [astm-g48](astm-g48.md) (pitting/crevice), [astm-g59](astm-g59.md) (LPR), [astm-g102](astm-g102.md) (rate calc), [ampp-sp0775](ampp-sp0775.md) (field coupons), or any other measurement chain. The output is an **engineering-grade statistical summary**: mean, standard deviation, confidence interval, distribution-fit hypothesis test, outlier-detection result, censored-data-handling decision, and (where applicable) extreme-value tail-extrapolation for the worst-case pit, the worst-case CR coupon, or the worst-case time-to-failure.

The **extreme-value statistics** application is the highest-impact use of G16 in offshore and refining practice: when 30 storage-tank-floor coupons or 50 pipeline corrosion-monitoring coupons are inspected for **maximum pit depth**, the deepest-pit-of-the-population follows a Gumbel (Type-I extreme-value) distribution, **not** a normal distribution. Extrapolating the Gumbel fit to a target return-period (e.g., the deepest pit expected on a 1,000 m² tank floor over a 20-year design life) gives an actionable remaining-life input that a normal-distribution fit would systematically under-predict.

## Revision history

The local O&G-Standards catalog records G16 with **2 distinct revisions** in the corpus, reflecting two major editorial cycles since original publication:

| Edition | Status | Notes |
|---------|--------|-------|
| G16 (early revision) | superseded | Pre-1995 statistical-guide baseline. |
| G16-95 family | superseded | Mid-1990s update. |
| G16-13 | active | Modern revision incorporating updated extreme-value-statistics treatment and censored-data-handling guidance. |
| G16-13 (Reapproved 2019) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

The following are the analytical anchors that the guide prescribes (consult the on-disk PDF or publisher catalog for clause-exact text and worked-example numerics):

- **Experiment design** — replicate-coupon planning, blocking, randomization, and sample-size guidance for detecting a specified difference in corrosion rate or pit depth at a target confidence level.
- **Descriptive statistics** — mean, standard deviation, median, range, and quartile summaries for replicate corrosion-rate, mass-loss, and pit-depth datasets.
- **Distribution fitting** — normal distribution for corrosion rates from replicate coupons (typically valid); log-normal for some mass-loss datasets; **Gumbel (Type-I extreme-value)** for maximum-pit-depth populations; generalized-extreme-value (GEV) where the Gumbel fit fails.
- **Hypothesis testing** — t-test, F-test, ANOVA for comparing two or more alloy / environment / treatment groups.
- **Confidence intervals and tolerance limits** — confidence interval on the mean, prediction interval on a future observation, tolerance interval on a stated proportion of the population.
- **Outlier detection** — Dixon's Q-test, Grubbs' test, or graphical methods; censored-data handling for "no detect" pit observations or specimens that survived the test envelope.
- **Extreme-value tail extrapolation** — Gumbel-paper plotting position formulas, parameter estimation (method of moments, maximum likelihood), and return-period extrapolation for worst-case pit-depth on inspection populations.
- **Reporting** — required elements: distribution type assumed, parameter estimates with standard errors, goodness-of-fit test result, sample size, censoring handling, and confidence-level statement.

## Practitioner application

- **Storage-tank-floor inspection** — UT or magnetic-flux-leakage pit-depth measurements across hundreds to thousands of inspection points; Gumbel-fit extrapolation to floor-area / return-period gives the worst-expected pit depth that drives the next inspection interval and any patch-plate / floor-replacement decisions.
- **Pipeline ILI runs** — ILI-reported pit-depth populations are extrapolated to "deepest defect not yet detected" via extreme-value statistics; G16 is the methodology backbone.
- **CRA-coupon qualification** — replicate G48 / G31 / G36 specimens are summarized per G16; pass/fail criteria typically expressed as a tolerance limit on the population (e.g., "95th percentile mass loss ≤ X mg/cm²").
- **Online-monitoring data fusion** — LPR + ER + coupon data combined per [ampp-sp0775](ampp-sp0775.md); G16 anchors the statistical-comparison step that reconciles continuous-monitoring rates with periodic coupon rates.
- **Remaining-life forecasts** — corrosion-rate distribution parameters propagate into Monte Carlo or first-order-second-moment fitness-for-service calcs (per [api-rp-579](api-std-579.md) Part 4 / 5); G16 governs the input-parameter statistical summary.
- **Censored-data handling** — coupons exposed for less than the full duration, removed for unrelated reasons, or showing "below-detection" pit depth all require G16's censored-data treatment to avoid biasing the population estimate.

## Industry adoption

G16 is the **default statistical-methods reference** for corrosion-engineering data analysis across refining, oil-and-gas, marine, power, chemical-process, and infrastructure industries. It is referenced from API RP 579 (fitness-for-service Part 4 corrosion-rate inputs and Part 5 pitting analysis), API 510 / 570 / 653 (in-service inspection planning that consumes coupon-data summaries), AMPP/NACE SP0775 (field-coupon analysis), and DNV / ABS classification-society guidance for coupon-based-corrosion-rate qualification of CRA selections. A corrosion-data summary that omits the distribution-fit assumption and the goodness-of-fit test result is regularly flagged in reviewer comments at regulators and classification societies.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g16` under `.claude/rules/calc-citation-contract.md`. W204 audit V9 surfaced `astm-g16` as a substrate-gap slug — referenced from [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) (recommended-promotions list, item 8: statistical-methodology anchor) and from broader citing patterns in fitness-for-service and remaining-life-forecasting workflows that consume G-series mass-loss, pit-depth, or rate datasets. The page anchors that link target without reproducing any clause text, statistical formulas, distribution tables, or worked-example numerics.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0016-13r19.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Replicate-coupon mass-loss data are summarized per G16; G1 is the upstream measurement substrate.
- [astm-g31](astm-g31.md) — *Laboratory Immersion Corrosion Testing of Metals.* Replicate-coupon datasets from G31 immersion tests consumed by G16.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Maximum-pit-depth populations from G46 examination are the load-bearing input for G16's extreme-value tail extrapolation.
- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Replicate-coupon mass-loss + pit-depth data from G48 consumed by G16.
- [astm-g59](astm-g59.md) — *LPR Measurements.* Continuous-monitoring rate data summarized per G16.
- [astm-g102](astm-g102.md) — *Calculation of Corrosion Rates from Electrochemical Measurements.* G102 rates from a population of measurements are summarized per G16 distribution-fit machinery.
- [ampp-sp0775](ampp-sp0775.md) — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* Field-coupon population analysis cites G16 statistical methods.
- [api-std-579](api-std-579.md) — *API 579-1 / ASME FFS-1 Fitness-for-Service.* Part 4 corrosion-rate inputs and Part 5 pitting analysis consume G16 statistical summaries.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI workflows that consume G16-summarized inspection populations.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor for the measurement-methodology cluster; G16 is the statistical-treatment companion to the measurement standards.
- [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — concept anchor for pitting analysis; G16 extreme-value tail extrapolation is the statistical backbone.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G16-derived distribution assumption, plotting-position formula, or extreme-value-extrapolation parameter.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording G16 with 2 editions and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0016-13r19.html
