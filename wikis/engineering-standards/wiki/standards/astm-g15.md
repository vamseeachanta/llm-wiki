---
title: "ASTM G15 — Standard Terminology Relating to Corrosion and Corrosion Testing (withdrawn 2010, historically referenced) (bounded resolver)"
slug: astm-g15
tags: ["astm", "g-series", "corrosion", "terminology", "withdrawn", "historical", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g15
publisher: ASTM
revision: "G15-08 (final active edition before withdrawal); WITHDRAWN 2010 — not replaced by a single successor; terminology distributed into individual G-series methods"
publisher_current_edition: "WITHDRAWN — no current edition"
status: withdrawn
withdrawn_year: 2010
jurisdiction: "ASTM jurisdiction (US-origin, global adoption while active)"
instrument_type: terminology
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0015.htm
public_url: https://www.astm.org/g0015.htm
publisher_catalog_url: https://www.astm.org/
---

# ASTM G15 — Standard Terminology Relating to Corrosion and Corrosion Testing (bounded resolver — WITHDRAWN 2010)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, term definitions, or alphabetical-list reproductions are included.
> **code_id:** `astm-g15` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals) &nbsp;•&nbsp; **revision:** G15-08 was the final active edition; the standard was **withdrawn in 2010** and was **not replaced by a single successor**. Terminology was redistributed into the terminology sections of individual G-series test methods. The local O&G-Standards catalog records G15 with **5 editions** spanning the active-revision lifetime.

## Status: withdrawn 2010

**ASTM G15 was officially withdrawn by ASTM in 2010 with no replacement document.** The decision reflected a publisher-strategy shift: rather than maintain a single corrosion-terminology umbrella, ASTM moved to embed term definitions directly inside the terminology sections of each G-series test method (G1, G3, G5, G31, G46, G48, G59, G102, G106, etc.). Modern G-series practices each carry their own canonical-term definitions for the procedures they specify.

**Implications for citing callers:**

- **Active engineering documents** should NOT cite ASTM G15 for terminology going forward. Cite the relevant G-series test method's terminology section (e.g., [astm-g3](astm-g3.md) §3 for sign-convention terms; [astm-g46](astm-g46.md) §3 for pitting-rating terms; [astm-g48](astm-g48.md) §3 for FeCl3-test terms).
- **Historical references** to ASTM G15 (in pre-2010 specifications, legacy CRA-qualification reports, archived MR0175 / TM0177 referenced documents, or older textbooks) are common and remain interpretable — the terminology was stable across the active-revision lifetime.
- **Calc-citation callers** that have hard-coded `code_id = astm-g15` from legacy artifacts should resolve against this page (which records the withdrawal status) rather than fail-closed; the resolver page exists precisely to prevent the calc-citation contract from breaking on legacy references.

## Scope (historical)

ASTM G15 was the **definitional substrate** for the ASTM G-series corrosion-and-corrosion-testing community: a single alphabetical reference of canonical terms, units, and conventions used across all G-series test methods. Term coverage included general-corrosion terms (`E_corr`, `i_corr`, `corrosion rate`, `passivation`, `transpassive`), localized-corrosion terms (`pitting`, `crevice`, `pit depth`, `pit density`, `repassivation potential`), stress-corrosion terms (`SCC`, `threshold stress intensity K_ISCC`, `time-to-failure`), galvanic terms (`galvanic series`, `polarization diagram`, `current distribution`), atmospheric-corrosion terms (`time-of-wetness`, `aerosol salinity`), and reference-electrode terms (SCE, SHE, Ag/AgCl, Cu/CuSO4 with their canonical offsets).

The standard was **invoked by reference** from virtually every other G-series practice and method during its active period (1960s through 2010); a calc-module emitting a G-series test result would cite "terminology per ASTM G15" alongside the procedural standard. After withdrawal, the same terminology is sourced from the relevant test-method's own terminology section.

## Revision history

The local O&G-Standards catalog records G15 with **5 distinct revisions** during its active lifetime — one of the highest revision-count standards in the corpus, reflecting steady terminology accretion as new test methods were added to the G-series:

| Edition | Status | Notes |
|---------|--------|-------|
| G15 (early revisions) | superseded | Original 1970s-era definitional substrate; alphabetical term list. |
| G15-93 family | superseded | Early-1990s update. |
| G15-99(a) family | superseded | Late-1990s consolidation pre-Y2K. |
| G15-04 | superseded | Mid-2000s consolidation; expanded SCC and pitting term coverage. |
| G15-08 | **final active edition** | Last revision before withdrawal. |
| G15 — withdrawn 2010 | **withdrawn — no replacement** | Per ASTM 2010 publisher-action; terminology embedded into individual G-series test methods. |

Local catalog file count for G15: 5 PDFs spanning the above editions (per [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md)).

## Key sections (historical)

The following are the terminology-substrate categories that appear across the active-period revisions (consult the on-disk PDFs for the alphabetical canonical list — clause-exact text is not reproduced here):

- **General corrosion terms** — corrosion potential, corrosion current, corrosion rate, polarization, Tafel slope, exchange current density, reference electrode.
- **Localized corrosion terms** — pitting, crevice corrosion, pit depth, pit density, induction time, repassivation potential, critical pitting temperature.
- **Stress-corrosion terms** — stress-corrosion cracking, hydrogen embrittlement, sulfide stress cracking, threshold stress intensity, time-to-failure, environment-assisted cracking.
- **Galvanic / dissimilar-metal terms** — galvanic series, galvanic couple, mixed-potential, polarization diagram, area ratio.
- **Atmospheric / outdoor-exposure terms** — time-of-wetness, atmospheric corrosion category, salinity deposition rate.
- **Cathodic-protection terms** — protection potential, polarization, current density, anode consumption rate (cross-referenced from the broader CP-engineering vocabulary).
- **Specimen and procedure terms** — coupon, specimen, exposure, pre-conditioning, cleaning, descaling, mass loss, post-test inspection.

## Practitioner application (historical and current)

- **Pre-2010 reports and specifications** routinely cite "terminology per ASTM G15" when reporting electrochemical, mass-loss, SCC, pitting/crevice, atmospheric, or galvanic test results. Calc modules consuming legacy data may encounter G15 references in upstream documents and should treat them as historically valid.
- **Post-2010 reports and specifications** should cite the relevant G-series test method's own terminology section. The terminology has not changed in substance; only the publisher-side organization has shifted.
- **Resolver-page role** — G15 retains a resolver page in this wiki specifically to handle legacy `code_id = astm-g15` references without breaking the calc-citation contract. The page records the withdrawal status and points callers at the modern in-method terminology sources.

## Industry adoption (historical)

While active (1970s–2010), G15 was **the** corrosion-terminology umbrella across academic, vendor, regulatory, and classification-society work. It was cited from API, ASME, NACE/AMPP, ISO, and DNV documents that used G-series test methods. Post-withdrawal, citing patterns have migrated to the in-method terminology sections, but G15 references remain prevalent in archived materials.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g15` under `.claude/rules/calc-citation-contract.md`. W204 audit V9 surfaced `astm-g15` as a substrate-gap slug — referenced from [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) (recommended-promotions list, item 10: definitional anchor) and from legacy citing patterns. The page anchors that link target, **flags the withdrawn status explicitly via the `status: withdrawn` and `withdrawn_year: 2010` frontmatter fields**, and redirects callers to the modern in-method terminology sources without reproducing any of the historical alphabetical term-list content.

## Where to find the full text

ASTM withdrawal-status catalog page: `https://www.astm.org/g0015.htm` (publisher records the withdrawal). Withdrawn standards may still be available for purchase from ASTM's withdrawn-standards archive. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`, `status`); they do not require body text.

## Cross-references

- [astm-g3](astm-g3.md) — *Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Carries the modern in-method terminology for sign conventions, reference electrodes, and polarization-curve descriptors that historically lived in G15.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss-method terminology now lives in G1's terminology section.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Pitting-and-pit-rating terminology now lives in G46.
- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Method-specific FeCl3 terminology now in G48.
- [astm-g16](astm-g16.md) — *Applying Statistics to Analysis of Corrosion Data.* Statistical terms (mean, standard deviation, confidence interval, censored data) for corrosion datasets.
- [astm-g59](astm-g59.md) — *Linear Polarization Resistance Measurements.* LPR-specific terminology.
- [astm-g102](astm-g102.md) — *Calculation of Corrosion Rates from Electrochemical Measurements.* Faraday and equivalent-weight terminology.
- [electrochemical-corrosion](../concepts/electrochemical-corrosion.md) — concept anchor for the kinetics-framework terminology that G15 historically codified.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor that places G15 in the historical-substrate role for corrosion-measurement vocabulary.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — calls resolving against `code_id = astm-g15` should record the withdrawal status alongside the citation; modern emitters should prefer the relevant in-method terminology source.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording G15 with 5 editions in the local catalog and the metadata-only extraction policy; flags G15 as a high-revision-count terminology anchor.
- Publisher catalog (withdrawal record): https://www.astm.org/g0015.htm
