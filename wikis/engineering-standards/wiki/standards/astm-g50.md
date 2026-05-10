---
title: "ASTM G50 — Standard Practice for Conducting Atmospheric Corrosion Tests on Metals (bounded resolver)"
slug: astm-g50
tags: ["astm", "g-series", "corrosion", "atmospheric-corrosion", "outdoor-exposure", "test-site", "practice", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g50
publisher: ASTM
revision: "G50-20 — publisher-current"
publisher_current_edition: "G50-20"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0050-20.html
public_url: https://www.astm.org/g0050-20.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G50 — Atmospheric Corrosion Tests on Metals (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, exposure-rack drawing reproductions, or environment-classification reproductions are included.
> **code_id:** `astm-g50` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.04 on Atmospheric Corrosion) &nbsp;•&nbsp; **revision:** G50-20.

## Scope

ASTM G50 is the **outdoor-atmospheric-exposure practice** for metals and alloys: it codifies the test-site selection, exposure-rack design, specimen mounting, environment characterization, and exposure-duration conventions that produce comparable atmospheric-corrosion datasets across geographic locations and decades. G50 is the **non-accelerated reference** that companion accelerated tests ([astm-g44](astm-g44.md) alternate immersion, [astm-g85](astm-g85.md) modified salt spray) are validated against.

The practice is the methodological foundation for the long-running atmospheric-corrosion test programs that produced the corrosion-rate datasets underpinning [iso-9223](iso-9223.md) corrosivity-category classifications and the multi-decade Kearny / Point Reyes / Panama Canal / Daytona Beach atmospheric exposure records.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G50 (early revisions) | superseded | 1970s baseline. |
| G50-76 | superseded | Original published revision. |
| G50-10 | superseded | Mid-2010s consolidation. |
| G50-20 | **publisher-current** | Most recent revision as of this page. |

## Key sections

- **Test-site classification** — rural, urban, industrial, marine-coastal, marine-offshore, tropical, and arid environment categories with characterization-data requirements (chloride deposition, SO2, time-of-wetness, ambient temperature, humidity).
- **Exposure-rack design** — rack-frame material, specimen-tilt angle (typically 30° from horizontal facing south in the Northern Hemisphere), specimen-spacing requirements, and isolator design to prevent galvanic interaction between dissimilar specimens.
- **Specimen preparation** — specimen dimensions, surface finish, identification marking, edge protection, and pre-exposure mass and dimension recording.
- **Specimen mounting** — insulator clips, fastener materials, and rack-grid layouts that prevent mechanical-damage or galvanic-cross-contamination during multi-year exposure.
- **Environment monitoring** — co-located sensors and witness samples for chloride deposition rate, SO2 concentration, time-of-wetness, and temperature/humidity logging.
- **Exposure duration and removal schedule** — staged removal at 6, 12, 24, 60, and 120 month intervals to construct the corrosion-rate-vs-time curve and identify the steady-state long-term corrosion rate (LTCR).
- **Post-exposure analysis** — cleaning per [astm-g1](astm-g1.md), mass-loss measurement, and pitting examination per [astm-g46](astm-g46.md) when localized attack accompanies uniform corrosion.

## Practitioner application

- **Long-term corrosion-rate (LTCR) determination** — multi-year G50 exposures provide the LTCR datasets that calibrate finite-life equipment design (atmospheric-storage tanks, structural steel, transmission tower lattice, building envelope).
- **ISO 9223 corrosivity-category validation** — G50-derived first-year corrosion rates of standard reference metals (carbon steel, zinc, copper, aluminum) classify a test site into ISO 9223 categories C1 (very low) through CX (extreme).
- **Coating durability assessment** — G50 outdoor exposure of coated panels is the field-validation reference against which accelerated-coating-tests (UV, salt spray, cyclic) are calibrated.
- **Material selection for atmospheric service** — comparative G50 datasets across alloys (CS, weathering steel, galvanized, aluminum, stainless) inform specification for outdoor-service infrastructure.
- **Marine atmospheric calibration** — coastal G50 sites are the calibration substrate for chloride-deposition models that drive offshore atmospheric and splash-zone corrosion-allowance calculations.

## Industry adoption

G50 is the **default outdoor-atmospheric-exposure practice** across infrastructure, automotive, building-envelope, transmission-and-distribution, defense, and aerospace industries. The Point Reyes (CA), Kearny (NJ), Panama Canal Zone, Daytona Beach (FL), and Limestone (NY) test sites operated under G50-style protocols for decades and produced the foundational atmospheric-corrosion datasets cited throughout the corrosion-engineering literature. International atmospheric-corrosion programs (ISOCORRAG, MICAT) operated G50-aligned protocols.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g50` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g50` as a substrate-gap slug — referenced from [atmospheric-corrosion](../concepts/atmospheric-corrosion.md) and the long-term-corrosion-rate cluster. This page closes that flag without reproducing any clause text, rack-drawing reproductions, or environment-classification tables.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0050-20.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss cleaning protocol applied to G50-exposed specimens.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Examination companion when localized attack accompanies G50 atmospheric exposure.
- [astm-g44](astm-g44.md) — *Alternate Immersion in 3.5% NaCl.* Laboratory-accelerated marine-atmospheric simulation; G50 is the field-reference baseline.
- [astm-g85](astm-g85.md) — *Modified Salt Spray (Fog) Testing.* Laboratory-accelerated chloride-fog companion; calibrated against G50 outdoor exposure.
- [iso-9223](iso-9223.md) — *Corrosion of metals and alloys — Corrosivity of atmospheres.* ISO classification (C1–CX) populated by G50-style first-year corrosion rates.
- [atmospheric-corrosion](../concepts/atmospheric-corrosion.md) — concept anchor; G50 is the foundational outdoor-exposure practice for atmospheric corrosion data.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor; G50 produces the LTCR substrate for atmospheric-service rate models.
- [coating-systems](../concepts/coating-systems.md) — concept anchor; G50 outdoor exposure validates accelerated-coating-test durability claims.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes a G50 environment classification, exposure-duration convention, or LTCR-from-mass-loss conversion.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0050-20.html
