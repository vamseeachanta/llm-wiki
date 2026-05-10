---
title: "ASTM G47 — Standard Test Method for Determining Susceptibility to Stress-Corrosion Cracking of 2XXX and 7XXX Aluminum Alloy Products (bounded resolver)"
slug: astm-g47
tags: ["astm", "g-series", "corrosion", "stress-corrosion-cracking", "scc", "aluminum", "2xxx", "7xxx", "test-method", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g47
publisher: ASTM
revision: "G47-20 — publisher-current"
publisher_current_edition: "G47-20"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0047-20.html
public_url: https://www.astm.org/g0047-20.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G47 — SCC Susceptibility of 2XXX and 7XXX Aluminum Alloy Products (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, applied-stress-level tables, or pass/fail acceptance reproductions are included.
> **code_id:** `astm-g47` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.06 on Environmentally Assisted Cracking) &nbsp;•&nbsp; **revision:** G47-20.

## Scope

ASTM G47 is the **alloy-and-product-specific SCC test method** for 2XXX (Al-Cu) and 7XXX (Al-Zn-Mg-Cu) heat-treatable aluminum alloy products in plate, extrusion, forging, and rod/bar form. It combines the alternate-immersion environment of [astm-g44](astm-g44.md) with specimen geometries prepared per [astm-g38](astm-g38.md) (C-ring), [astm-g30](astm-g30.md) (U-bend), [astm-g39](astm-g39.md) (bent-beam), or short-transverse tensile bars to evaluate susceptibility to chloride-driven SCC.

The method addresses the principal aluminum-aerospace SCC concern: **short-transverse-grain-direction SCC** in plate, extrusion, and forging product forms, where elongated grain structure produces dramatically lower SCC resistance in the through-thickness direction than in the longitudinal or long-transverse directions. G47 results feed the SCC-resistance classification ratings codified in [astm-g64](astm-g64.md).

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G47 (early revisions) | superseded | 1970s/80s baseline. |
| G47-98 | superseded | Late-1990s consolidation. |
| G47-98 (R2004) | superseded | First reapproval cycle. |
| G47-11 | superseded | Mid-2010s revision. |
| G47-20 | **publisher-current** | Most recent revision as of this page. |

## Key sections

- **Specimen selection by product form** — short-transverse direction tensile bars for plate/extrusion/forging; C-ring per [astm-g38](astm-g38.md) for rod and bar; geometry guidance for thinner sheet products.
- **Applied stress levels** — sustained-stress fractions of the alloy's specified minimum yield strength; multiple stress levels permit threshold-stress estimation.
- **Test environment** — alternate-immersion in 3.5% NaCl per [astm-g44](astm-g44.md) for the prescribed exposure duration.
- **Replicate count** — minimum specimen count per stress level per product orientation for statistical confidence.
- **Pass/fail criteria** — time-to-cracking observation; complete-no-failure-after-exposure-duration acceptance; performance versus reference specimens.
- **Examination** — visual and metallographic inspection for SCC initiation and propagation; pairing with [astm-g46](astm-g46.md) examination workflow when pitting accompanies SCC.
- **Reporting** — alloy + temper + product-form provenance, applied stress level, exposure duration, time-to-failure for each replicate, and the resulting classification rating per [astm-g64](astm-g64.md).

## Practitioner application

- **Aluminum-aerospace alloy qualification** — the canonical SCC qualification test for 7050, 7075, 7475, 2024, 2124, 2219 plate, extrusion, and forging products in T6, T73, T74, T76, T77 tempers.
- **Temper selection guidance** — comparative G47 testing across temper variants (e.g., 7075-T6 vs. T73 vs. T76) drives the temper-selection compromise between strength and SCC resistance for high-stress aerospace structural applications.
- **Product-form qualification** — aerospace OEM specifications routinely require G47 testing of new alloy/temper/product-form combinations before service introduction.
- **SCC-resistance rating assignment** — G47 results are the input substrate for SCC-resistance classification per [astm-g64](astm-g64.md), which assigns A/B/C/D ratings used in alloy-selection design guides.
- **Process-control for heat-treaters** — periodic G47 testing of production heats verifies that aging treatments achieve the temper's nominal SCC-resistance characterization.

## Industry adoption

G47 is **the** SCC qualification test for high-strength heat-treatable aluminum alloys across aerospace, defense, and structural-aluminum industries. It is invoked by reference from MMPDS, AMS, and aerospace OEM material specifications; from MIL-spec aluminum-alloy procurement documents; and from SCC-resistance classification protocols. The G47 / G44 / G38–G39 / G64 stack is the canonical aluminum-SCC test cascade.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g47` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g47` as a substrate-gap slug — referenced from [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) and the aluminum-alloys cluster. This page closes that flag without reproducing any clause text, applied-stress tables, or acceptance-criterion content.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0047-20.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g64](astm-g64.md) — *Classification of Resistance to SCC of Heat-Treatable Aluminum Alloys.* Downstream classification scheme that consumes G47 results.
- [astm-g44](astm-g44.md) — *Alternate Immersion in 3.5% NaCl.* Environment-specifying practice that G47 invokes by reference.
- [astm-g38](astm-g38.md) — *C-Ring Specimen Preparation.* Specimen geometry for rod and bar product forms in G47 testing.
- [astm-g30](astm-g30.md) — *U-Bend Specimen Preparation.* Specimen geometry for thin-section product forms in G47 testing.
- [astm-g39](astm-g39.md) — *Bent-Beam Specimen Preparation.* Threshold-stress specimen geometry for G47 testing.
- [astm-g129](astm-g129.md) — *Slow Strain Rate Testing.* Active-strain-rate alternative for aluminum-alloy SCC characterization.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Examination companion when pitting accompanies G47 SCC observations.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; G47 is the canonical aluminum-alloy SCC test method.
- [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) — concept anchor; aluminum SCC mechanisms include chloride-driven hydrogen embrittlement contributions.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G47 applied-stress level or pass/fail criterion for aluminum-alloy SCC qualification.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0047-20.html
