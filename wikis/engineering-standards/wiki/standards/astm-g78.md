---
title: "ASTM G78 — Standard Guide for Crevice Corrosion Testing of Iron-Base and Nickel-Base Stainless Alloys in Seawater and Other Chloride-Containing Aqueous Environments (bounded resolver)"
slug: astm-g78
tags: ["astm", "g-series", "corrosion", "crevice-corrosion", "stainless-steel", "nickel-alloys", "seawater", "guide", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g78
publisher: ASTM
revision: "G78-20 — publisher-current"
publisher_current_edition: "G78-20"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: guide
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0078-20.html
public_url: https://www.astm.org/g0078-20.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G78 — Crevice Corrosion of Stainless and Ni-Base Alloys in Seawater (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, multi-crevice-assembly drawing reproductions, or initiation-time tabulations are included.
> **code_id:** `astm-g78` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.05 on Laboratory Corrosion Tests) &nbsp;•&nbsp; **revision:** G78-20.

## Scope

ASTM G78 is the **crevice-corrosion testing guide** for iron-base and nickel-base stainless alloys exposed to seawater and other chloride-containing aqueous environments. It complements [astm-g48](astm-g48.md) (FeCl3 ferric-chloride pitting and crevice test, the laboratory-accelerated screening method) by addressing the **service-relevant** chloride exposure: natural seawater (or filtered/synthetic seawater) at near-ambient temperature, where realistic crevice-corrosion behavior emerges over weeks-to-months timescales rather than the 24–72 hour FeCl3 screening exposure.

G78 is a **guide**, not a test method — it offers methodology recommendations without mandating a single procedure. Practitioners select the multi-crevice-former configuration, the seawater source, the temperature, the exposure duration, and the post-exposure metrics most relevant to their service application.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G78 (early revisions) | superseded | 1980s baseline. |
| G78-01 | superseded | Early-2000s consolidation. |
| G78-01 (R2012) | superseded | Reapproval cycle. |
| G78-20 | **publisher-current** | Most recent revision as of this page. |

## Key sections

- **Crevice former designs** — multiple-crevice-assembly (MCA) washers, segmented PTFE blocks, and cylindrical-on-flat geometries; tightening-torque guidance for reproducible crevice gaps.
- **Specimen preparation** — surface finish, cleaning, edge protection, and identification per [astm-g1](astm-g1.md) conventions.
- **Test environment** — natural seawater (with site-of-collection documentation), filtered seawater, synthetic seawater per [astm-d1141](astm-d1141.md), or chloride-bearing process waters; environment characterization (chloride, sulfate, dissolved oxygen, temperature, pH) recorded at exposure start, mid-point, and end.
- **Exposure duration** — typical 30/60/90 day intervals; longer durations (180+ days, 1 year) for ranking high-resistance Ni-base alloys.
- **Crevice-initiation criteria** — visual evidence of attack within the crevice footprint, weight-loss indicators, or [astm-g46](astm-g46.md)-style examination of post-test specimens.
- **Reporting** — crevice-former configuration, environment chemistry, exposure duration, fraction of crevice sites that initiated attack, and depth/area of attack at initiated sites.
- **Comparison to FeCl3** — guidance on relating G78 seawater results to G48 ferric-chloride screening outcomes for the same alloy.

## Practitioner application

- **Seawater-service material qualification** — evaluation of stainless and Ni-base alloys (316L, duplex 2205, super-duplex 2507, 6Mo super-austenitic, alloy 625, alloy C-276) for offshore-platform service-water systems, marine heat exchangers, FPSO topside piping, and seawater-injection systems.
- **Service-relevant ranking** — G78 produces alloy rankings closer to actual service performance than G48's accelerated FeCl3 ranking; alloys that fail G48 may still perform acceptably in cool seawater, and vice versa.
- **Long-term performance forecasting** — multi-month G78 exposures inform corrosion-allowance and inspection-interval decisions for chloride-service equipment.
- **Welded-joint qualification** — crevice-corrosion behavior of weldments (HAZ, weld metal, fusion line) under realistic seawater exposure, where heat-tint and sensitization effects may differ from base-metal performance.
- **Coating and gasket evaluation** — G78 exposures with controlled gasket / coating crevice configurations validate sealing-strategy choices for chloride-service flange and bolted-joint hardware.

## Industry adoption

G78 is the **default seawater-service crevice-corrosion testing guide** across offshore oil-and-gas, marine, naval, and chemical-process industries. It is invoked by reference from offshore-platform service-water material specifications, marine heat-exchanger design standards, and NACE/AMPP CRA-qualification practices. The G78 / G48 pair is the canonical service-vs-screening-test combination for chloride-environment crevice corrosion.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g78` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g78` as a substrate-gap slug — referenced from [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md), [astm-g46](astm-g46.md), and [astm-g48](astm-g48.md). This page closes that flag without reproducing any clause text, MCA-design figures, or initiation-time tabulations.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0078-20.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion in FeCl3.* Accelerated-screening sister method; G78 is the service-relevant seawater complement.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Examination workflow that consumes G78 post-exposure specimens.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Cleaning and mass-loss conventions applied to G78 specimens.
- [astm-g31](astm-g31.md) — *Laboratory Immersion Corrosion Testing of Metals.* Immersion-test foundation; G78 is the crevice-specific guide built on the same exposure platform.
- [astm-g123](astm-g123.md) — *SCC of Stainless Alloys in Boiling Acidified NaCl.* Sister chloride-environment SCC test method for stainless alloys.
- [astm-d1141](astm-d1141.md) — *Substitute Ocean Water Standard.* Synthetic-seawater formulation that G78 may invoke when natural seawater is unavailable.
- [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — concept anchor; G78 is the service-relevant crevice-corrosion test guide for chloride environments.
- [galvanic-corrosion](../concepts/galvanic-corrosion.md) — concept anchor; crevice-corrosion phenomenology overlaps galvanic deaeration cells in occluded geometries.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G78 environment parameter, exposure duration, or crevice-initiation criterion.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0078-20.html
