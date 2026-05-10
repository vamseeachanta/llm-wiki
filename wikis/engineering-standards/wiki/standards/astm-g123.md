---
title: "ASTM G123 — Standard Test Method for Evaluating Stress-Corrosion Cracking of Stainless Alloys with Different Nickel Content in Boiling Acidified Sodium Chloride Solution (bounded resolver)"
slug: astm-g123
tags: ["astm", "g-series", "corrosion", "stress-corrosion-cracking", "scc", "stainless-steel", "boiling-nacl", "nickel-content", "test-method", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g123
publisher: ASTM
revision: "G123-00 (R2021) — publisher-current"
publisher_current_edition: "G123-00 (R2021)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0123-00r21.html
public_url: https://www.astm.org/g0123-00r21.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G123 — SCC of Stainless Alloys in Boiling Acidified NaCl (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, solution-formulation tables, or alloy-ranking-curve reproductions are included.
> **code_id:** `astm-g123` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.06 on Environmentally Assisted Cracking) &nbsp;•&nbsp; **revision:** G123-00 reapproved most recently as G123-00(R2021).

## Scope

ASTM G123 is the **chloride-SCC ranking test method** for stainless alloys spanning a nickel-content range from low-Ni austenitic (304/316 family at ~8–13% Ni) through intermediate-Ni austenitic-ferritic (duplex 22/25% Cr) to high-Ni superaustenitic and Ni-base alloys (alloy 800/825/625/C-276). The method exposes pre-stressed specimens to **boiling acidified sodium chloride solution** (acidified to a controlled low pH with HCl or H2SO4) and records time-to-cracking as a function of nickel content, providing the comparative-resistance dataset that motivates the **Copson-curve** style ranking of austenitic SCC resistance versus alloy nickel content.

G123 is the laboratory-accelerated method that bridges the severe boiling-MgCl2 screening of [astm-g36](astm-g36.md) (which fails most austenitics rapidly and provides limited differentiation among high-Ni alloys) and field-relevant chloride exposures (which require months-to-years to differentiate intermediate-resistance alloys). The acidified-NaCl chemistry is more service-relevant than MgCl2 while still being aggressive enough to produce rankable failure times within practical exposure durations.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G123-00 | active | Original 2000 publication. |
| G123-00 (R2005) | superseded | First reapproval cycle. |
| G123-00 (R2015) | superseded | Second reapproval cycle. |
| G123-00 (R2021) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

- **Solution composition** — boiling sodium chloride at a specified concentration, acidified with HCl or H2SO4 to a controlled low pH; pH and chloride concentration controlled and monitored throughout exposure.
- **Apparatus** — boiling-flask reflux condenser configuration with controlled boiling temperature, similar to the [astm-g36](astm-g36.md) apparatus but at the lower NaCl-system boiling point.
- **Specimen geometry** — typically U-bend per [astm-g30](astm-g30.md) or bent-beam per [astm-g39](astm-g39.md), with C-ring per [astm-g38](astm-g38.md) acceptable for tubing-form alloys.
- **Test duration and inspection schedule** — extended exposures (often 100+ hours) with intermediate inspection points to capture time-to-cracking for higher-resistance alloys.
- **Failure criteria** — visual evidence of macrocracks, optical-microscopy confirmation of SCC at exposed surfaces, or full-section fracture; time-to-failure recorded for each replicate.
- **Reference-alloy ranking** — comparative ranking against reference alloys (typically 304/316 at one end and a high-Ni reference at the other) to anchor the relative-resistance scale.
- **Reporting** — alloy chemistry (especially Ni content), heat-treat state, applied stress level, environment chemistry/temperature, time-to-failure for each replicate, fracture mode (transgranular / intergranular / mixed), and the resulting Ni-content-resistance ranking.

## Practitioner application

- **Stainless-alloy SCC qualification for chloride process service** — ranking 304/316/317/904L/duplex/super-duplex/super-austenitic/Ni-base alloys for petrochemical, refining, and chemical-process equipment exposed to chloride-bearing process streams (acidified condensate, salt-laden hydrocarbon streams).
- **Copson-curve construction** — G123 datasets across an alloy series populate Cu-Ni Copson-style charts that show time-to-failure vs. nickel content, anchoring the engineering rule-of-thumb that austenitic SCC resistance reaches a minimum near 8–10% Ni and improves substantially above 30% Ni.
- **Heat-exchanger material selection** — G123 ranking informs alloy choice for chloride-bearing process-side fluid in shell-and-tube and plate heat exchangers where MgCl2 ranking would be over-conservative.
- **Sour-service supplemental screening** — for chloride-bearing sour environments where ISO 15156 selection rules require SCC qualification beyond the boiling-MgCl2 baseline, G123 provides the chloride-acidified data point.
- **Welded-joint qualification** — base-metal vs. weld-metal vs. HAZ comparison under acidified-NaCl exposure highlights sensitization-driven and heat-tint-driven SCC susceptibility.

## Industry adoption

G123 is the **default acidified-NaCl chloride-SCC ranking method** for stainless-alloy material selection across petrochemical, refining, chemical-process, and pulp-and-paper industries. It is invoked by reference from material-selection guides for chloride-bearing process service and from CRA-qualification protocols where MgCl2 boiling tests provide insufficient differentiation. The G123 / G36 pair is the canonical chloride-SCC test combination for stainless and Ni-base alloys.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g123` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g123` as a substrate-gap slug — referenced from [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) and the stainless-alloy chloride-SCC cluster. This page closes that flag without reproducing any clause text, solution-formulation tables, or alloy-ranking-curve content.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0123-00r21.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g36](astm-g36.md) — *Boiling Magnesium Chloride SCC Test.* Sister chloride-SCC method; G123 is the milder, more service-relevant acidified-NaCl complement.
- [astm-g30](astm-g30.md) — *U-Bend Specimen Preparation.* Specimen geometry frequently used in G123 testing.
- [astm-g39](astm-g39.md) — *Bent-Beam Specimen Preparation.* Threshold-stress specimen geometry alternative for G123.
- [astm-g38](astm-g38.md) — *C-Ring Specimen Preparation.* Tubing-form specimen geometry for G123 testing.
- [astm-g129](astm-g129.md) — *Slow Strain Rate Testing.* Active-strain-rate alternative SCC characterization method.
- [astm-g78](astm-g78.md) — *Crevice Corrosion in Seawater.* Sister chloride-environment test; G78 addresses crevice/pit attack while G123 addresses SCC.
- [astm-a923](astm-a923.md) — *Detection of Detrimental Intermetallics in Duplex Stainless.* Pre-screening companion that flags alloy-condition issues before committing to G123 SCC exposure.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; G123 is a chloride-SCC ranking method for stainless alloys with Ni-content-resistance correlation.
- [sour-service-materials](../concepts/sour-service-materials.md) — concept anchor; G123 supplements MR0175/MR0103 SCC qualification for chloride-bearing sour environments.
- [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — concept anchor; chloride-SCC and chloride-localized-attack share environmental drivers.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G123 environment parameter, time-to-failure threshold, or Ni-content-resistance correlation.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0123-00r21.html
