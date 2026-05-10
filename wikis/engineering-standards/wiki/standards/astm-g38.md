---
title: "ASTM G38 — Standard Practice for Making and Using C-Ring Stress-Corrosion Test Specimens (bounded resolver)"
slug: astm-g38
tags: ["astm", "g-series", "corrosion", "stress-corrosion-cracking", "scc", "c-ring", "specimen-preparation", "practice", "metadata-only"]
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
code_id: astm-g38
publisher: ASTM
revision: "G38-01 (R2021) — publisher-current"
publisher_current_edition: "G38-01 (R2021)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: practice
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0038-01r21.html
public_url: https://www.astm.org/g0038-01r21.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G38 — Standard Practice for Making and Using C-Ring Stress-Corrosion Test Specimens (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, machining-detail dimensions, or stress-equation reproductions are included.
> **code_id:** `astm-g38` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals; Subcommittee G01.06 on Environmentally Assisted Cracking) &nbsp;•&nbsp; **revision:** G38-01 reapproved most recently as G38-01(R2021).

## Scope

ASTM G38 is the **specimen-preparation practice** for the C-ring SCC specimen — a circumferentially-machined ring sectioned to allow controlled diametral compression or tension, producing a hoop-stress field on either the outer (compression-loaded) or inner (tension-loaded) surface. C-rings are the canonical specimen for SCC testing of **tubing, pipe, rod, and bar product forms** where the curved geometry naturally lends itself to ring extraction. G38 is the sister practice to [astm-g30](astm-g30.md) (U-bend, sheet/plate) and [astm-g39](astm-g39.md) (bent-beam, sheet/plate); together they cover the principal constant-deflection SCC specimen geometries.

Like G30 and G39, G38 is a **specimen-preparation practice**, not an environment-specifying test method. It defines geometry, machining tolerances, surface finish, the loading bolt/fixture, and the stress-calculation equations that relate diametral deflection to surface hoop stress. The corrosive environment, exposure time, temperature, and acceptance criteria are supplied by the citing test-method or product specification.

## Revision history

| Edition | Status | Notes |
|---------|--------|-------|
| G38 (early revisions) | superseded | 1970s/80s baseline. |
| G38-01 | active | 2001 revision; modern technical baseline. |
| G38-01 (R2013) | superseded | First reapproval cycle. |
| G38-01 (R2021) | **publisher-current** | Most recent reapproval cycle as of this page. |

## Key sections

- **Specimen geometry** — outside diameter, wall thickness, ring height, and slot dimensions sized to the parent tubing/pipe stock.
- **Machining and surface preparation** — final-pass surface finish, edge-radius requirements, and avoidance of cold-work artifacts that would bias SCC initiation.
- **Loading configurations** — (a) **outer-surface tension** via diametral compression (squeeze loading); (b) **outer-surface compression** via diametral tension (spread loading). Most SCC programs use the outer-surface-tension configuration.
- **Stress calculation** — diametral-deflection-to-hoop-stress equations parameterized by ring thickness, mean radius, and elastic modulus; with elastic-plastic correction notes for stresses approaching the proof stress.
- **Loading hardware** — bolt-and-nut assemblies, insulator washers (to break galvanic couples in conductive electrolytes), and fixture materials compatible with the test environment.
- **Stress measurement and verification** — strain-gauge calibration of representative specimens prior to environment exposure.
- **Reporting** — alloy + heat-treat + product-form provenance, applied stress level (% of proof stress), environment, exposure duration, time-to-cracking and crack-location observations.

## Practitioner application

- **Sour-service tubing qualification** — C-rings are the canonical SCC specimen for OCTG, line pipe, and downhole-tubing material qualification under [iso-15156](iso-15156.md) sour-service envelopes; tubing curvature is preserved without flattening artifacts.
- **CRA tubing screening** — duplex, super-duplex, and nickel-base CRA tubing-grade qualification programs use C-rings in CO2/H2S/Cl⁻ autoclave exposures.
- **Threshold-stress determination** — multiple C-rings at graded applied-stress fractions establish the threshold-stress envelope for a given alloy/environment combination.
- **Component-form proof** — C-rings preserve the **manufactured surface** of the tubing OD or ID, enabling assessment of mill-scale, surface roughness, or surface cold-work effects that flat specimens cannot reproduce.
- **Aluminum SCC qualification** — C-rings of aluminum-alloy bar/rod stock are the specimen geometry cited by [astm-g47](astm-g47.md) (2XXX/7XXX SCC test) and consistent with [astm-g64](astm-g64.md) classification.

## Industry adoption

G38 is **the** preparation practice for C-ring SCC specimens across tubing-product SCC testing programs in oil-and-gas, aerospace, refining, and chemical-process industries. It is invoked by reference from sour-service material qualification protocols, NACE/AMPP test methods (where C-ring is the chosen geometry), and aerospace alloy-qualification documents. C-ring specimens machined and stress-calculated outside the G38 framework are routinely flagged in CRA-qualification reviews.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g38` under `.claude/rules/calc-citation-contract.md`. W215 audit V10 iter-46 surfaced `astm-g38` as a substrate-gap slug — referenced from [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md), [sour-service-materials](../concepts/sour-service-materials.md), and the engineering-critical-assessment cluster. This page closes that flag without reproducing any clause text, machining-detail dimensions, or stress-equation derivations.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0038-01r21.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g30](astm-g30.md) — *U-Bend Stress-Corrosion Test Specimen Preparation.* Sister specimen-preparation practice for sheet/plate; G38 is the tubing/pipe analog.
- [astm-g39](astm-g39.md) — *Bent-Beam (4-point) Stress-Corrosion Test Specimen Preparation.* Threshold-stress sibling; flat-specimen geometry for plate/sheet forms.
- [astm-g36](astm-g36.md) — *Boiling Magnesium Chloride SCC Test.* Environment-specifying method that frequently consumes C-ring geometry per G38.
- [astm-g44](astm-g44.md) — *Alternate Immersion in 3.5% NaCl.* Atmospheric-marine simulation environment that pairs with C-ring specimens for aluminum and high-strength steel SCC.
- [astm-g47](astm-g47.md) — *SCC of 2XXX/7XXX Aluminum.* Aluminum-alloy SCC test method that uses C-ring specimens prepared per G38 (alongside tensile bars).
- [astm-g64](astm-g64.md) — *Classification of Resistance to SCC of Heat-Treatable Aluminum Alloys.* Classification consumes G47 results which use G38 specimens.
- [astm-g129](astm-g129.md) — *Slow Strain Rate Testing.* Active-strain-rate alternative to constant-deflection C-ring testing.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — concept anchor; C-ring is the canonical tubing/pipe SCC specimen geometry.
- [sour-service-materials](../concepts/sour-service-materials.md) — concept anchor; OCTG and line-pipe sour-service qualification uses C-ring per G38.
- [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) — concept anchor; C-rings are used in HE/HISC qualification of high-strength steels and CRAs.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes a G38 stress-equation parameter or specimen-geometry constraint.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page recording the ASTM G-series corpus and the metadata-only extraction policy.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0038-01r21.html
