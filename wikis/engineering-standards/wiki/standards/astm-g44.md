---
title: "ASTM G44 — Standard Practice for Exposure of Metals and Alloys by Alternate Immersion in Neutral 3.5% Sodium Chloride Solution (bounded resolver)"
slug: astm-g44
tags: ["astm", "g-series", "corrosion", "stress-corrosion-cracking", "scc", "alternate-immersion", "nacl", "marine-simulation", "practice", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g44
publisher: ASTM
revision: "G44-99 (R2021) — publisher-current"
publisher_current_edition: "G44-99 (R2021)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0044-99r21.html
public_url: https://www.astm.org/g0044-99r21.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G44 — Alternate Immersion in 3.5% NaCl (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, immersion-cycle timing reproductions, or solution-formulation tables are included.
> **code_id:** `astm-g44` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.06 on Environmentally Assisted Cracking) &nbsp;•&nbsp; **revision:** G44-99 reapproved most recently as G44-99(R2021).

## Scope

ASTM G44 is the **environment-defining practice** for an alternate-immersion exposure regime in neutral 3.5% NaCl solution. It establishes a **wet/dry cycling schedule** intended to simulate the splash-zone, marine-atmospheric, or chloride-rich-industrial atmospheric environment that drives SCC and pitting in susceptible alloy systems. G44 specifies the test-rig configuration, solution composition, immersion-cycle timing, temperature, and the renewal/replenishment schedule for the test solution; it does **not** specify the specimen geometry — that is supplied by sister practices [astm-g38](astm-g38.md) (C-ring), [astm-g30](astm-g30.md) (U-bend), [astm-g39](astm-g39.md) (bent-beam), or product-specific tensile bars per [astm-g47](astm-g47.md).

The wet/dry cycling produces an **enrichment effect** as droplet evaporation concentrates surface chloride between immersions, simulating field exposure better than continuous immersion for atmospheric-marine and splash-zone applications.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G44 (early revisions) | superseded | 1970s/80s baseline. |
| G44-99 | active | 1999 revision; modern technical baseline. |
| G44-99 (R2005) | superseded | First reapproval cycle. |
| G44-99 (R2013) | superseded | Second reapproval cycle. |
| G44-99 (R2021) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

- **Solution composition** — neutral sodium chloride, mass-fraction basis, deionized-water solvent, pH range.
- **Immersion cycle schedule** — periodic-immersion / periodic-drying schedule with specified times for each phase.
- **Specimen rack and rotation** — rotating-rack or alternating-platform fixtures that move specimens between solution and air phases on the prescribed schedule.
- **Temperature control** — ambient-laboratory range; thermocouple and air-flow conditioning.
- **Solution renewal** — interval at which the bath is replaced to control pH drift and contamination.
- **Specimen orientation** — guidelines on specimen positioning relative to droplet drainage to ensure consistent wet-dry behavior.
- **Reporting** — exposure duration, cycle count, temperature record, solution-renewal log, post-exposure observations including time-to-cracking, pit-population, and corrosion-product appearance.

## Practitioner application

- **Aluminum SCC qualification** — the canonical exposure environment cited by [astm-g47](astm-g47.md) for SCC testing of 2XXX and 7XXX heat-treatable aluminum alloy products; the resulting time-to-failure data feeds [astm-g64](astm-g64.md) SCC-resistance classification.
- **High-strength steel SCC and HE screening** — alternate-immersion exposure of pre-stressed C-ring or U-bend specimens to evaluate Cl-SCC and chloride-driven hydrogen embrittlement of quench-and-tempered, maraging, and PH stainless steels.
- **Atmospheric-marine simulation** — surrogate for splash-zone, beach-side, or coastal-industrial exposure when full-scale outdoor exposure (per [astm-g50](astm-g50.md)) is not practical.
- **Coating qualification** — alternate-immersion endurance of coated steel or aluminum substrates to evaluate adhesion, blistering, and underfilm-corrosion behavior.
- **Stainless-steel CISCC screening** — supplemental environment for chloride-induced SCC of austenitic stainless steel, particularly when boiling MgCl2 ([astm-g36](astm-g36.md)) is too aggressive.

## Industry adoption

G44 is the **default alternate-immersion practice** across aluminum-aerospace, high-strength-steel, marine, and coating-qualification industries. Its 3.5% NaCl chemistry is the long-established marine-water surrogate used in lieu of natural seawater (which carries biological and trace-ion variability). G44-style exposure is invoked from aluminum-alloy product specifications, aerospace-fastener SCC qualification, and protective-coating durability programs. Industries that cannot tolerate the boiling-chloride severity of G36 use G44 as the milder, more representative chloride-SCC environment.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g44` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g44` as a substrate-gap slug — referenced from [astm-g47](astm-g47.md), [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md), and the atmospheric-marine corrosion cluster. This page closes that flag without reproducing any clause text, cycle-timing tables, or solution-formulation reproductions.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0044-99r21.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g47](astm-g47.md) — *SCC of 2XXX/7XXX Aluminum.* Primary downstream test method that prescribes G44 alternate-immersion as the exposure environment.
- [astm-g64](astm-g64.md) — *Classification of Resistance to SCC of Heat-Treatable Aluminum Alloys.* Consumes G47/G44-derived SCC time-to-failure data.
- [astm-g38](astm-g38.md) — *C-Ring Specimen Preparation.* Specimen geometry frequently exposed in G44 immersion cycles.
- [astm-g30](astm-g30.md) — *U-Bend Specimen Preparation.* Sheet/plate specimen geometry for G44 exposure.
- [astm-g39](astm-g39.md) — *Bent-Beam Specimen Preparation.* Threshold-stress specimen geometry for G44 exposure.
- [astm-g36](astm-g36.md) — *Boiling MgCl2 SCC Test.* More-aggressive sister chloride environment; G44 is the milder atmospheric-marine alternative.
- [astm-g50](astm-g50.md) — *Atmospheric Corrosion Tests on Metals.* Outdoor-exposure cousin; G44 is the laboratory-accelerated surrogate.
- [astm-g85](astm-g85.md) — *Modified Salt Spray (Fog) Testing.* Sister chloride-fog environment; G44 uses immersion cycles, G85 uses continuous fog.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; G44 is the laboratory chloride-SCC exposure for atmospheric-marine simulation.
- [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) — concept anchor; G44 exposure drives chloride-environment HE in high-strength steels.
- [atmospheric-corrosion](../concepts/atmospheric-corrosion.md) — concept anchor; G44 is the laboratory-accelerated marine-atmospheric simulation.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes a G44 environment parameter or accelerated-exposure factor.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0044-99r21.html
