---
title: "ASTM G85 — Standard Practice for Modified Salt Spray (Fog) Testing (bounded resolver)"
slug: astm-g85
tags: ["astm", "g-series", "corrosion", "salt-spray", "salt-fog", "cyclic-corrosion", "coating-test", "atmospheric-corrosion", "practice", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g85
publisher: ASTM
revision: "G85-19 — publisher-current"
publisher_current_edition: "G85-19"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0085-19.html
public_url: https://www.astm.org/g0085-19.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G85 — Modified Salt Spray (Fog) Testing (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, annex-procedure reproductions, or solution-formulation tables are included.
> **code_id:** `astm-g85` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.05 on Laboratory Corrosion Tests) &nbsp;•&nbsp; **revision:** G85-19.

## Scope

ASTM G85 is the **family of modified salt-fog procedures** that extend the baseline neutral-salt-spray test (ASTM B117) toward more aggressive or more service-representative chloride-fog environments. The practice is organized as a series of **annexes**, each defining a distinct procedure: acidified salt fog (Annex A1, with acetic acid), cyclic acidified (Annex A2, CASS-like procedure with copper accelerant), seawater-acidified (Annex A3, with synthetic-seawater chemistry), SO2-salt-spray (Annex A4, sulfur-dioxide-augmented), and dilute-electrolyte cyclic fog (Annex A5).

G85 is the **accelerated-laboratory chloride-environment family** that complements G50 outdoor exposure and G44 alternate immersion: each addresses a different acceleration-vs-realism trade-off. G85 is invoked extensively by automotive, aerospace, and architectural-aluminum coating-qualification programs.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G85 (early revisions) | superseded | 1980s baseline annex set. |
| G85-09 | superseded | Late-2000s consolidation of annexes. |
| G85-11 | superseded | Mid-2010s revision. |
| G85-19 | **publisher-current** | Most recent revision as of this page. |

## Key sections

- **Annex A1 — Acetic-acid salt spray (AASS)** — neutral-salt-spray with acetic-acid acidification; widely used for decorative-electroplate qualification.
- **Annex A2 — Cyclic acidified salt spray (modified CASS)** — copper-accelerated acetic-acid salt spray; shorter-duration ranking of decorative coatings.
- **Annex A3 — Seawater-acidified salt spray (SWAAT)** — synthetic-seawater chemistry with acetic-acid acidification; aluminum-aerospace-coating qualification.
- **Annex A4 — SO2-salt-spray** — neutral-salt-spray with sulfur-dioxide injection; industrial-atmospheric simulation.
- **Annex A5 — Dilute-electrolyte cyclic fog** — wet/dry cycling at lower chloride concentrations; coating-blistering and underfilm-corrosion screening.
- **Cabinet-design requirements** — fog atomization, droplet-size distribution, exposure-zone temperature uniformity, and condensate-collection-rate calibration shared across annexes.
- **Specimen positioning** — orientation, spacing, and racking guidance to ensure uniform fog exposure across the cabinet workspace.
- **Reporting** — annex selected, exposure duration, post-exposure observations (rust appearance, blister density, scribe-creep distance for coated panels), and any required reference-specimen pass/fail comparison.

## Practitioner application

- **Coating qualification** — automotive, aerospace, and architectural-coating systems are routinely qualified against specific G85 annexes for accelerated rust-resistance and creep-from-scribe metrics.
- **Aluminum SWAAT** — Annex A3 is the standard accelerated test for aluminum-heat-exchanger fin/tube coatings, brazed-aluminum-radiator durability, and aerospace-aluminum coating systems.
- **Decorative plating** — Annex A1/A2 (AASS/CASS) screen decorative chromium, nickel, and brass coatings against pit and blister formation.
- **Industrial-atmospheric simulation** — Annex A4 SO2 augmentation simulates urban/industrial environments where SO2 acidifies the fog and accelerates atmospheric corrosion of carbon steel and zinc.
- **Scribe-creep evaluation** — coated panels with controlled scribe lines are exposed in G85 cabinets to measure underfilm-corrosion creep distance, a key coating-system durability metric.
- **Round-robin calibration** — G85 cabinets across testing laboratories are calibrated against reference-specimen mass loss and condensate collection rates to ensure inter-lab comparability.

## Industry adoption

G85 is **the** modified-salt-fog practice family across automotive, aerospace, architectural, marine, and infrastructure-coating industries. Each annex serves a specific industry need: A1/A2 for decorative plating, A3 for aluminum/aerospace, A4 for industrial-atmospheric, A5 for blister/underfilm-screening. G85 is invoked by reference from Big-3 automotive material specifications, aerospace OEM coating standards, and architectural-aluminum AAMA durability standards.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g85` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g85` as a substrate-gap slug — referenced from [atmospheric-corrosion](../concepts/atmospheric-corrosion.md), [coating-systems](../concepts/coating-systems.md), and the accelerated-corrosion-testing cluster. This page closes that flag without reproducing any clause text, annex-procedure tables, or solution-formulation reproductions.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0085-19.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g50](astm-g50.md) — *Atmospheric Corrosion Tests on Metals.* Outdoor-exposure reference against which G85 accelerated procedures are calibrated.
- [astm-g44](astm-g44.md) — *Alternate Immersion in 3.5% NaCl.* Sister chloride-environment laboratory test; G44 uses immersion cycles, G85 uses fog.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* Mass-loss cleaning conventions applied to G85 metallic specimens.
- [astm-g46](astm-g46.md) — *Examination and Evaluation of Pitting Corrosion.* Pitting examination companion when localized attack accompanies G85 exposure.
- [iso-9223](iso-9223.md) — *Corrosivity of atmospheres.* ISO classification linked indirectly via the accelerated-vs-outdoor calibration framework.
- [atmospheric-corrosion](../concepts/atmospheric-corrosion.md) — concept anchor; G85 is the laboratory accelerated chloride/SO2-fog family for atmospheric simulation.
- [coating-systems](../concepts/coating-systems.md) — concept anchor; G85 is invoked by coating-qualification protocols for rust-resistance and scribe-creep metrics.
- [galvanic-corrosion](../concepts/galvanic-corrosion.md) — concept anchor; coated-panel scribe-creep behavior in G85 reflects underfilm galvanic mechanisms.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G85 annex selection, exposure duration, or coating-creep acceptance threshold.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0085-19.html
