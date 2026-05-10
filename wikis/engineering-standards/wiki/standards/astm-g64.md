---
title: "ASTM G64 — Standard Classification of Resistance to Stress-Corrosion Cracking of Heat-Treatable Aluminum Alloys (bounded resolver)"
slug: astm-g64
tags: ["astm", "g-series", "corrosion", "stress-corrosion-cracking", "scc", "aluminum", "heat-treatable", "classification", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g64
publisher: ASTM
revision: "G64-99 (R2020) — publisher-current"
publisher_current_edition: "G64-99 (R2020)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: classification
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0064-99r20.html
public_url: https://www.astm.org/g0064-99r20.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G64 — Classification of SCC Resistance for Heat-Treatable Aluminum Alloys (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, rating-table reproductions, or alloy-specific resistance assignments are included.
> **code_id:** `astm-g64` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.06 on Environmentally Assisted Cracking) &nbsp;•&nbsp; **revision:** G64-99 reapproved most recently as G64-99(R2020).

## Scope

ASTM G64 is the **classification-and-rating standard** that organizes alloy/temper/product-form combinations of heat-treatable aluminum alloys into discrete SCC-resistance categories (typically labeled A through D, where A is highest resistance and D is highest susceptibility). It is the **downstream consumer** of [astm-g47](astm-g47.md) test data: G47 measures, G64 classifies. The classification is alloy-, temper-, product-form-, and grain-orientation-specific; the same alloy in different tempers or different product orientations may carry different G64 ratings.

G64 is a **classification standard**, not a test method. It does not specify any test procedure of its own; it consumes G47 (and historically allied) test results and assigns the resistance rating used by aerospace and defense material-selection guides.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G64 (early revisions) | superseded | 1970s/80s baseline classification. |
| G64-99 | active | 1999 revision; modern technical baseline. |
| G64-99 (R2004) | superseded | First reapproval cycle. |
| G64-99 (R2013) | superseded | Second reapproval cycle. |
| G64-99 (R2020) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

- **Classification scheme** — A/B/C/D rating ladder with definitional thresholds expressed in terms of resistant-to-failure stress fractions and orientation conditions.
- **Rating table by alloy/temper/product-form/orientation** — alphabetic ratings indexed by AA alloy designation (2024, 2124, 2219, 7050, 7075, 7475, etc.), temper (T6, T73, T74, T76, T77, etc.), product form (plate, extrusion, forging, sheet, rod/bar), and grain orientation (longitudinal L, long-transverse LT, short-transverse ST).
- **Caveats and limitations** — environment dependency (G64 ratings derive from G44 alternate-immersion in 3.5% NaCl; other environments may produce different rankings), thickness dependency for plate, and qualifier notes for specific alloy/temper combinations.
- **Reference test method invocation** — explicit reference to [astm-g47](astm-g47.md) as the test method whose results populate the classification.
- **Application guidance** — selection-guide notes for designers using ratings to evaluate alloy/temper/orientation choices for sustained-load aerospace structural applications.

## Practitioner application

- **Aerospace alloy/temper selection** — designers choose between e.g. 7075-T6 (B/D rating depending on orientation) and 7075-T73 (A/B/A) for sustained-tensile-load structural applications, accepting a strength penalty in exchange for SCC immunity.
- **Short-transverse direction restriction** — G64 ST ratings flag the alloy/temper combinations whose short-transverse SCC resistance is too low for ST-direction sustained-stress applications; many 7XXX-T6 plates carry "D" ST ratings prohibiting use in that orientation.
- **Alloy substitution analysis** — when a legacy alloy/temper carries a poor G64 rating, candidate substitutes are screened against the same rating table for resistance, strength, and cost trade-offs.
- **Material-specification authoring** — aerospace OEM specifications cite G64 ratings as a procurement-and-acceptance basis for SCC-critical structural items.
- **Service-failure forensics** — investigators of in-service aluminum SCC failures consult G64 ratings of the failed alloy/temper/orientation as part of root-cause analysis for compatibility with the load-stress and environment field.

## Industry adoption

G64 is the **canonical SCC-resistance classification reference** across aerospace, defense, and structural-aluminum industries worldwide. It is invoked by reference from MMPDS, AMS, and aerospace OEM material specifications; from MIL-spec aluminum-alloy procurement documents; and from temper-selection design guides published by alloy producers (Alcoa, Rio Tinto, Constellium). The G47 / G44 / G64 stack is the canonical aluminum-SCC test-and-rating cascade.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g64` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g64` as a substrate-gap slug — referenced from [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md), [astm-g47](astm-g47.md), and the aluminum-alloys cluster. This page closes that flag without reproducing any clause text, rating-table content, or alloy-specific resistance assignments.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0064-99r20.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g47](astm-g47.md) — *SCC of 2XXX/7XXX Aluminum.* Upstream test method whose results populate the G64 classification.
- [astm-g44](astm-g44.md) — *Alternate Immersion in 3.5% NaCl.* Environment cited indirectly via G47; defines the chloride-SCC ranking basis.
- [astm-g38](astm-g38.md) — *C-Ring Specimen Preparation.* Specimen geometry for rod/bar SCC testing feeding G64 classification.
- [astm-g30](astm-g30.md) — *U-Bend Specimen Preparation.* Specimen geometry for sheet/plate SCC testing.
- [astm-g39](astm-g39.md) — *Bent-Beam Specimen Preparation.* Threshold-stress specimen geometry alternative.
- [astm-g129](astm-g129.md) — *Slow Strain Rate Testing.* Active-strain-rate alternative SCC characterization method.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; G64 is the canonical aluminum-alloy SCC-resistance classification.
- [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) — concept anchor; aluminum SCC mechanisms include chloride-driven HE contributions.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes a G64 alloy/temper/orientation rating threshold or selection-guide rule.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0064-99r20.html
