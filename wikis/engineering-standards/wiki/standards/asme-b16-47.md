---
title: "ASME B16.47 — Large Diameter Steel Flanges (NPS 26 through NPS 60)"
slug: asme-b16-47
code_id: asme-b16-47
publisher: ASME
publisher_full: "American Society of Mechanical Engineers"
revision: "2020 (current edition); prior editions 1996, 2006, 2011, 2017"
jurisdiction: "US (referenced by B31 piping family, BPVC Section VIII); international by adoption"
instrument_type: standard
supersedes: "MSS SP-44 (Series A historical; merged into B16.47 Series A); API 605 (Series B historical; merged into B16.47 Series B)"
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.asme.org/codes-standards
public_url: https://www.asme.org/codes-standards
publisher_catalog_url: https://www.asme.org/codes-standards
tags:
  - asme
  - standards
  - flanges
  - large-diameter
  - piping-components
  - dimensional
  - process-piping
  - metadata-only
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# ASME B16.47 — Large Diameter Steel Flanges (NPS 26 through NPS 60)

**code_id:** `asme-b16-47` &nbsp;·&nbsp; **publisher:** ASME (American Society of Mechanical Engineers) &nbsp;·&nbsp; **revision:** ASME B16.47-2020

> Bounded metadata-only resolver page for downstream `Citation(...)` callers under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Page contains no dimensional tables, pressure-temperature ratings, bolt-circle diameters, or hub-thickness values from the source.

## Scope

ASME B16.47 is the consensus US dimensional and pressure-temperature-rating standard for **large-diameter steel pipe flanges from NPS 26 through NPS 60** in pressure classes 75, 150, 300, 400, 600, and 900. It is the upstream-size companion to [asme-b16-5](asme-b16-5.md), which covers NPS 1/2 through NPS 24. The standard codifies two parallel flange-dimension series:

- **Series A** — historically derived from MSS SP-44; thicker hub, larger overall outside diameter, generally heavier-pattern.
- **Series B** — historically derived from API Standard 605; thinner hub, smaller overall outside diameter, generally lighter-pattern.

Series A and Series B are **not interchangeable**: a Series A flange will not bolt up to a Series B flange of the same NPS and class. The standard governs flange dimensions, facing types (raised face, ring-type joint, flat face), bolt-hole pattern, hub geometry, marking, materials by reference to ASTM specifications, and pressure-temperature ratings by class.

## Revision history

- **Pre-1996** — large-diameter flanges governed separately by MSS SP-44 (Series A pattern) and API Standard 605 (Series B pattern).
- **ASME B16.47-1996** — first edition; consolidated SP-44 and API 605 as Series A and Series B inside a single ASME standard.
- **ASME B16.47-2006 / 2011 / 2017** — sequential revisions; rating-table updates, material-reference refresh, addendum harmonization.
- **ASME B16.47-2020** — current edition; consult ASME publications catalog for any subsequent reaffirmation/addenda.

## Key sections

Section structure (verify against the publisher copy in any normative work):

- **Scope and applicability** — NPS 26 through NPS 60, classes 75/150/300/400/600/900.
- **Series A dimensions** — heavier-pattern dimensional tables (descended from MSS SP-44).
- **Series B dimensions** — lighter-pattern dimensional tables (descended from API 605).
- **Pressure-temperature ratings** — by material group, by class.
- **Materials** — referenced ASTM specifications (forged, cast, plate-flange where applicable).
- **Facings** — raised face, ring-type joint (RTJ groove dimensions), flat face.
- **Marking** — flange identification scheme (size, class, material, series, manufacturer).
- **Tolerances** — dimensional tolerances on diameter, thickness, bolt circle, bolt-hole spacing.

## Practitioner application

- Process-piping designers and EPCs (Bechtel, Fluor, KBR, Worley, Jacobs, McDermott) specifying flanges on large-diameter process and utility piping for refineries, petrochemical complexes, LNG plants, gas-processing trains, and large-bore cooling-water systems.
- Pipeline EPCs specifying transmission-pipeline mainline-valve and fabricated-station piping flanges in the NPS 26–60 range.
- Piping-component vendors and forge shops fabricating large-diameter flanges to either Series A or Series B per project specification.
- Calc-module maintainers building flange-design and bolt-load calculation modules; flange dimensional inputs differ by series and must be source-tracked to the correct B16.47 series tables.

## Industry adoption

ASME B16.47 is the dominant US standard for steel-flange dimensions and ratings above NPS 24 and is widely adopted internationally on B31-code-jurisdiction projects. **Series A** is the more common selection on contemporary North American process and pipeline projects; **Series B** persists on legacy facilities and on projects with explicit API-605-lineage specifications. Project specifications must explicitly identify the series — the choice is not implicit and cannot be left ambiguous, since the two series are not interchangeable at the bolt-up flange. EN/ISO equivalents (PN-rated EN 1092-1 large-diameter flanges) are dimensionally distinct and not interchangeable with B16.47 flanges.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md` and substrate-fill landing for the wikilink in `asme-b16-5.md` referencing ASME B16.47. Surfaced as 1 of 5 ASME-process/RBI substrate-gap residuals after iter-50 W231 sweep; created under iter-51 W232 ASME-process/RBI substrate-fill batch. **Metadata-only** per spinout 2026-05-05 governance.

## Where to find the full text

ASME publications subscription required; ANSI catalog also lists the document. Vendor-derivative full text is **not** stored in this repo per spinout vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [asme-b16-5](asme-b16-5.md) — Pipe Flanges and Flanged Fittings NPS 1/2 through NPS 24; downstream-size companion.
- [asme-b16-34](asme-b16-34.md) — Valves, flanged, threaded, and welding end; consumes B16.47 facing/bolt-pattern data on large-bore valves.
- [asme-pcc-1](asme-pcc-1.md) — Guidelines for pressure-boundary bolted-flange joint assembly; assembly companion across B16.5 / B16.47 flange families.
- [asme-b31-1](asme-b31-1.md) — Power Piping; consumes B16.47 dimensional and rating data.
- [asme-b31-3](asme-b31-3.md) — Process Piping; consumes B16.47 dimensional and rating data.
- [asme-b31j](asme-b31j.md) — SIF and flexibility factors; sister-data input alongside B16.47 dimensions in pipe-stress-analysis component libraries.
- Calc citation contract: `.claude/rules/calc-citation-contract.md`

## Notes

- This page is **metadata-only**; no dimensional tables, pressure-temperature ratings, bolt-circle diameters, or hub-thickness values are reproduced from ASME B16.47. All technical descriptions above are paraphrased general engineering knowledge.
- For normative flange specification, cite the ASME-published edition directly (ASME B16.47-2020 or the current edition at time of citation), and identify Series A or Series B unambiguously.
- Substrate-fill resolver created under W232 iter-51 ASME-process/RBI batch (1 reference in `asme-b16-5.md`).
