---
title: "ASTM A923 — Standard Test Methods for Detecting Detrimental Intermetallic Phase in Duplex Austenitic/Ferritic Stainless Steels (bounded resolver)"
slug: astm-a923
tags: ["astm", "a-series", "duplex-stainless", "intermetallic-phases", "sigma-phase", "chi-phase", "metallography", "impact-test", "corrosion-test", "test-method", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-a923
publisher: ASTM
revision: "A923-14 (R2022) — publisher-current"
publisher_current_edition: "A923-14 (R2022)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-a-series.md
  - https://www.astm.org/a0923-14r22.html
public_url: https://www.astm.org/a0923-14r22.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM A923 — Detection of Intermetallic Phases in Duplex Stainless Steels (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, etch-recipe formulations, or pass/fail micrograph reproductions are included.
> **code_id:** `astm-a923` &nbsp;•&nbsp; **publisher:** ASTM International (Committee A01 — Steel, Stainless Steel and Related Alloys; Subcommittee A01.14 on Methods of Corrosion Testing) &nbsp;•&nbsp; **revision:** A923-14 reapproved most recently as A923-14(R2022). The standard is also referenced as IIW Doc. IX-2200-XX in international weldment-qualification literature.

## Scope

ASTM A923 is the **detrimental-intermetallic-phase detection** standard for duplex austenitic/ferritic stainless steels (UNS S31803/S32205 standard duplex, S32750 super-duplex, S32760 super-duplex, S32550 25Cr duplex, etc.). It comprises **three independent test methods** that together provide a tiered screening-and-confirmation cascade:

- **Method A — Sodium hydroxide etch (rapid screening)** — electrolytic etch reveals intermetallic phases (sigma σ, chi χ, secondary austenite γ₂, nitrides) as dark-staining features against the duplex matrix; rapid pass/fail screening for production lots.
- **Method B — Charpy impact toughness test (mechanical confirmation)** — sub-size or full-size Charpy V-notch testing at a specified low temperature; intermetallic-phase content correlates with toughness loss; quantitative confirmation of phase precipitation.
- **Method C — Ferric chloride pitting corrosion test (corrosion confirmation)** — exposure to FeCl3 solution similar to [astm-g48](astm-g48.md) Method A; intermetallic-phase content correlates with reduced critical-pitting-temperature performance.

A923 addresses the principal duplex-stainless concern: improper heat-treatment, slow cooling through the 600–1000 °C "sigma window," or weld-procedure non-conformance produces intermetallic phases (especially sigma) that **simultaneously** degrade toughness, ductility, and pitting/crevice resistance. The three methods together confirm that a duplex heat or weldment is free of detrimental phases at the levels that matter for service.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| A923-01 | superseded | Original 2001 publication; codified the three-method cascade. |
| A923-08 | superseded | Mid-2000s consolidation. |
| A923-14 | active | 2014 revision; modern technical baseline. |
| A923-14 (R2022) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

- **Method A — NaOH etch screening** — electrolyte composition (sodium hydroxide concentration), applied potential/current density, etch duration, and acceptance criterion (no detrimental phases evident, or quantitative pass/fail by intermetallic-phase area fraction).
- **Method B — Charpy impact** — specimen size and orientation, test temperature (typically -40 °C or -46 °C for standard duplex; lower for super-duplex), minimum acceptable absorbed energy.
- **Method C — Ferric chloride corrosion** — solution composition and temperature similar to [astm-g48](astm-g48.md) Method A but at a controlled lower temperature; mass-loss or visual-pit acceptance criterion.
- **Specimen selection** — guidance on sampling base metal, weld metal, and HAZ for weldment qualification; mid-thickness vs. surface sampling for plate.
- **Method-selection guidance** — Method A as production-screen, Method B for mechanical-property confirmation, Method C for corrosion-property confirmation; programs may invoke any combination.
- **Reporting** — alloy + heat-treatment provenance, sampling location, method(s) applied, pass/fail outcome, and accompanying microstructural / mechanical / corrosion data.

## Practitioner application

- **Duplex-stainless plate qualification** — mill-product release tests confirm absence of detrimental phases from solution-anneal-and-quench heat treatment.
- **Welded-joint qualification** — Method A or A+B applied to weld and HAZ in WPS qualification per API RP 582, NORSOK M-601, and project-specific welding specifications; ensures weld procedure produced acceptable duplex microstructure without sigma precipitation.
- **PWHT / stress-relief gate** — duplex stainless steels generally cannot tolerate PWHT in the sigma window; A923 testing of PWHT mockups confirms whether a planned heat treatment compromises the duplex microstructure.
- **Heat exchanger duplex tube qualification** — Method A or A+C applied to tube-form duplex products and tube-to-tubesheet weldments for sour-service or chloride-process heat exchangers.
- **Service-failure forensics** — A923 testing of failed duplex components retroactively confirms whether intermetallic-phase precipitation contributed to the failure mechanism.
- **Sour-service compliance gate** — required by [iso-15156](iso-15156.md) Part 3 and material-supplementary standards for duplex-stainless qualification in sour service.

## Industry adoption

A923 is the **canonical duplex-stainless intermetallic-phase detection standard** across oil-and-gas, chemical-process, pulp-and-paper, and marine industries. It is invoked by reference from API, NORSOK, NACE/AMPP, and ISO duplex-stainless welding and material specifications; from NORSOK M-601 and M-630 welding-qualification documents; and from project-specific duplex-stainless procurement specifications worldwide. International weldment-qualification practice (IIW guidance) treats A923 Method A as the de facto duplex-weld microstructure-screening reference.

## Why this page exists

This page is the citation resolver target for `code_id = astm-a923` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-a923` as a substrate-gap slug — referenced from [sour-service-materials](../concepts/sour-service-materials.md), [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md), [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md), and the duplex-stainless qualification cluster. This page closes that flag without reproducing any clause text, etch-recipe formulations, or pass/fail micrograph content.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/a0923-14r22.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Method C of A923 is the FeCl3 corrosion-confirmation companion test, sharing solution chemistry with G48.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Pitting examination workflow that consumes A923 Method C post-exposure specimens.
- [astm-g123](astm-g123.md) — *SCC of Stainless Alloys in Boiling Acidified NaCl.* Sister stainless-alloy chloride-environment test; A923 is pre-screening to confirm alloy condition before committing to G123 exposure.
- [astm-a370](astm-a370.md) — *Test Methods and Definitions for Mechanical Testing of Steel Products.* Charpy-impact-test methodology framework that A923 Method B builds on.
- [iso-15156](iso-15156.md) — *Petroleum and natural gas industries — Materials for use in H2S-containing environments.* ISO/MR0175 sour-service envelope that requires A923 testing for duplex-stainless qualification.
- [sour-service-materials](../concepts/sour-service-materials.md) — concept anchor; A923 is the intermetallic-phase qualification gate for duplex/super-duplex sour-service materials.
- [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md) — concept anchor; A923 Method A is the de facto duplex-weld microstructure-screening reference for WPS qualification.
- [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — concept anchor; A923 Method C confirms duplex-alloy CPT-relevant condition.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; A923 microstructure confirmation precedes duplex-alloy SCC qualification.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes an A923 method-selection rule, Charpy-toughness threshold, or pass/fail criterion for duplex-stainless qualification.

## Sources

- og-standards-astm-a-series — parent source page recording the ASTM A-series corpus and the metadata-only extraction policy (forward-adopted; create when promoted).
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/a0923-14r22.html
