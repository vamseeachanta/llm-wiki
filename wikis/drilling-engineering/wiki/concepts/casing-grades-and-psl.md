---
title: "Casing Grades and Product Specification Levels"
tags: [casing, grades, psl, h40, j55, k55, n80, l80, p110, q125, sour-service]
sources:
  - api-spec-5ct
added: 2026-05-13
last_updated: 2026-05-13
---

# Casing Grades and Product Specification Levels

## Scope

Steel-grade families used for casing and tubing, plus the API Product Specification Level (PSL) framework that conditions the manufacturing-quality requirements on top of grade. Grade fixes minimum yield, ultimate, and elongation; PSL fixes how rigorously those properties are demonstrated.

## API grade families (paraphrased from textbook restatement)

- **H40, J55, K55** — low-strength general-service grades. H40 oldest, K55 highest yield in this tier.
- **N80** — workhorse 80 ksi yield grade. Type 1 (carbon-steel, less expensive) and Type Q (quenched-and-tempered, more uniform).
- **L80** — 80 ksi yield with sour-service qualification (controlled hardness in HAZ); subdivided into Type 1, Type 9Cr, Type 13Cr (the chromium types are corrosion-resistant alloys for sweet-CO2 or mild-sour service).
- **C90, T95** — sour-service grades between L80 and P110 in strength.
- **P110** — high-strength 110 ksi grade, **not generally sour-service qualified** in baseline form. Most common production-string grade for non-sour wells.
- **Q125** — 125 ksi grade for HPHT applications.
- **Q-series proprietary** — higher-strength proprietary grades (e.g., V-150 equivalents, V&M S-135 equivalents) used for casing in extreme-depth wells.

Detailed minimum-yield, ultimate, elongation, hardness limits, and chemistry restrictions per grade live in API Spec 5CT tables — see [api-spec-5ct.md](../standards/api-spec-5ct.md) for the authoritative reference; specific values are not transcribed here per the vendor-derivative deny-list.

## Product Specification Levels

PSL conditions the manufacturing-quality requirements on top of the grade designation:

- **PSL-1** — baseline. Routine casing for ordinary well construction.
- **PSL-2** — adds Charpy V-notch impact testing on full body, hardness control on HAZ for sour-service grades, stricter NDE coverage.
- **PSL-3** — full-body NDE, supplementary chemistry restrictions, mill traceability requirements, additional documentation. Specified for HPHT, deep sour, or critical-well applications.

Not every grade is available at every PSL — for example, K55 PSL-3 is uncommon because the grade is rarely used in critical service; L80 Type 1 and P110 are commonly available at PSL-3 because they often see critical-service deployment.

## Sour-service framing

For H2S service, the operator specifies the grade against NACE MR0175 / ISO 15156 hardness limits — typical sour-service-qualified grades are L80 (Type 1 or Type 13Cr), C90, T95. P110 in baseline form is generally not sour-qualified; some manufacturers offer sour-modified P110 variants under proprietary trade names.

## Public references

- **API Spec 5CT** 10th Edition — see [api-spec-5ct.md](../standards/api-spec-5ct.md)
- **Bourgoyne et al.** Chapter 7 — grade and weight selection
- **NACE MR0175 / ISO 15156** — sour-service material requirements (engineering-standards/ scope)
- **Lyons handbook** — casing-grade comparison tables

## Cross-references

- [Casing Program Design](casing-program-design.md) — how grade interacts with the four design loads
- [Casing Shoe Track](casing-shoe-track.md)
- [API Spec 5CT](../standards/api-spec-5ct.md)
