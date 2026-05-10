---
title: "ASME BPVC Section VIII Division 3 — Alternative Rules for Construction of High Pressure Vessels (bounded summary)"
slug: asme-bpvc-viii-3
tags: ["asme", "bpvc", "standards", "pressure-vessels", "high-pressure", "hpht", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-bpvc-viii-3
publisher: ASME
revision: "2023 (publisher-current edition)"
publisher_current_edition: "2023"
jurisdiction: "ASME jurisdiction (US-origin, global adoption)"
instrument_type: specification
supersedes: None
methodology_status: "unknown"
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - https://www.asme.org/codes-standards/bpvc-standards
public_url: https://www.asme.org/codes-standards/bpvc-standards
publisher_catalog_url: https://www.asme.org/codes-standards/find-codes-standards
---

# ASME BPVC Section VIII Division 3 — Alternative Rules for Construction of High Pressure Vessels (bounded summary)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, design formulas, allowable stresses, fatigue curves, or fracture-mechanics tables are reproduced.
> **code_id:** `asme-bpvc-viii-3` &nbsp;•&nbsp; **publisher:** ASME &nbsp;•&nbsp; **revision:** publisher-current 2023 (two-year BPVC cycle).

## Scope

BPVC Section VIII Division 3 provides **alternative rules for the construction of high-pressure vessels** operating above the upper-pressure threshold at which Division 1 (design-by-rule) and Division 2 (design-by-analysis) cease to apply. The Division 3 floor is conventionally **≈ 10,000 psi / 70 MPa internal design pressure**, although the code text governs the precise applicability boundary. Below this threshold, Division 1 or Division 2 are the applicable references; above it, Division 3 is the only ASME route. Division 3 is the high-pressure companion to Division 1 ([asme-bpvc-viii-1](asme-bpvc-viii-1.md)) and Division 2 ([asme-bpvc-viii-2](asme-bpvc-viii-2.md)).

The Division 3 framework is **mandatorily fracture-mechanics-based**: minimum-thickness rules in Division 1 / Division 2 are insufficient at the design-stress levels accessible in Division 3, so the design route requires explicit linear-elastic fracture-mechanics or elastic-plastic-fracture-mechanics qualification, leak-before-break demonstration, fatigue-crack-growth life prediction, and a fracture-toughness floor on the materials of construction. Service envelopes addressed include autofrettaged forgings, layered or wire-wound vessels, isostatic-press housings, and high-pressure-tubing equipment.

## Revision history

- **1997 — Division 3 introduced** as a new BPVC subsection split from prior Division 1 / Division 2 high-pressure provisions. Introduction was driven by recognition that Section VIII design-by-rule and design-by-analysis margins underpredicted brittle-fracture and fatigue-crack-growth risk at very high pressures and stresses.
- **2004, 2007, 2010, 2013, 2015, 2017, 2019, 2021, 2023 editions** — Modern two-year ASME BPVC code-cycle revisions; the publisher-current edition at the time of this page is the 2023 edition.
- No edition is on disk in the local catalog — Division 3 is **publisher-portal-only** for this wiki; calc-callers needing edition-specific clause text must procure the document from the ASME catalog.

## Key sections

The Division 3 contents are organized into Articles paralleling but distinct from Division 1 / Division 2. Consult the on-disk procured PDF for clause-exact contents — this page records only the design-substrate inventory:

- **General requirements** — scope, certification, units, application boundary.
- **Materials requirements** — permitted material specifications, fracture-toughness minimums, hardness limits, condition restrictions.
- **Design** — linear-elastic and elastic-plastic stress analysis at the high-pressure stress levels; primary, secondary, and peak stress categorization with margins tighter than Division 2.
- **Fracture-mechanics evaluation** — mandatory K_Ic, J-integral, or CTOD qualification; fatigue-crack-growth (Paris-law) life prediction; reference flaw size; leak-before-break demonstration where credited.
- **Fabrication** — autofrettage, wire-wound, layered, and forged-monobloc construction routes; welding restrictions; PWHT.
- **Examination** — full volumetric and surface NDE; flaw-acceptance criteria tied back to the fracture-mechanics design basis.
- **Pressure testing** — hydrostatic acceptance with stricter strain-and-deformation criteria than Divisions 1/2.
- **Marking and stamping** — Division 3 nameplate requirements.

## Practitioner application

- **Hyperbaric and isostatic-press equipment** — material consolidation presses, hot-isostatic-press (HIP) chambers, cold-isostatic-press (CIP) chambers operating at 100-300 MPa.
- **Polyethylene reactors** — high-pressure polyolefin (LDPE) tubular and autoclave reactors operating at 200-300 MPa.
- **Hydrogen high-pressure storage and dispensing** — H2 storage cylinders and tube-trailer vessels at 35-90 MPa working pressure (interfaces with [asme-b31-12](asme-b31-12.md) for piping) for fuel-cell and refueling-station service.
- **Ammonia and methanol synthesis loops** — selected high-pressure stages where Division 2 cannot accommodate the design pressure.
- **Wellhead-and-tree pressure-control equipment** — HPHT (high-pressure / high-temperature) wellhead service above the 15,000 psi rating where API Spec 6A intersects ASME pressure-vessel rules; sour-service variants additionally bind to [iso-15156](iso-15156.md) / [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) materials qualification.
- **Defense, aerospace, and research-pressure equipment** — high-pressure gas storage, propellant test cells, hyperbaric test chambers.

## Industry adoption

Division 3 is the **only ASME route** for vessels above the Division 2 ceiling; selection is mandatory rather than economic. Owner-operator specifications in the HPHT subsea, hyperbaric, and HP-polymerization sectors invoke Division 3 by reference. Outside the ASME jurisdiction, **PD 5500** (UK), **EN 13445** (European), **AD 2000** (German), and the Chinese **GB 150** carry partly-overlapping high-pressure annexes; cross-jurisdictional harmonization is incomplete. The **API HPHT design protocol** (API 17TR8 and the API HPHT design verification analysis methodology) layers above Division 3 for offshore HPHT subsea pressure-control equipment.

## Why this page exists

This page is the citation resolver target for downstream calc and qualification modules under the calc-citation contract at `.claude/rules/calc-citation-contract.md`. Division 3 is referenced from [[asme-bpvc-viii-1]] and [[asme-bpvc-viii-2]] as the upper-pressure boundary that delegates above the ~10,000 psi / 70 MPa threshold; W201 audit (iter-43) surfaced unmatched `asme-bpvc-viii-3` slug across multiple Division 1 / 2 cross-references. This page anchors that link target without reproducing any code text, formulas, fracture-mechanics tables, or fatigue-crack-growth curves.

The on-disk corpus lacks Division 3 — calc-callers needing the document must procure it from the ASME catalog. The page is intentionally **metadata-only** until and unless a vendor-cleared edition lands on the `/mnt/ace/O&G-Standards/` mount.

## Where to find the full text

ASME BPVC catalog (registration required): `https://www.asme.org/codes-standards/find-codes-standards`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [[asme-bpvc-viii-1]] — sister Section VIII Division 1 (design-by-rule pressure vessels); upstream pressure-range neighbor below the Division 3 floor.
- [[asme-bpvc-viii-2]] — sister Section VIII Division 2 (design-by-analysis pressure vessels); upstream pressure-range neighbor below the Division 3 floor; Division 3 inherits Division 2 stress-categorization conventions where applicable.
- [[asme-bpvc-ii-d]] — material allowable stresses; Division 3 sources its allowable values from the same Section II-D table set, with high-pressure-specific reductions and toughness floors.
- [[asme-bpvc-ix]] — welding, brazing, and fusing qualifications; Division 3 fabrication invokes Section IX WPS/PQR/WPQ qualification.
- [[asme-b31-12]] — Hydrogen Piping and Pipelines; high-pressure H2 piping that connects to Division-3 vessels uses B31.12 material-performance factors.
- [[iso-15156]] / [[ampp-mr-0175-pt2]] / [[ampp-mr-0175-pt3]] — sour-service materials qualification overlay for HPHT-sour service.
- [[api-spec-6a]] — wellhead and tree equipment; HPHT-rated 6A equipment intersects Division 3 pressure-vessel rules.
- [[engineering-critical-assessment]] (concept) — fracture-mechanics-based acceptance route mandatory under Division 3.
- [[fitness-for-service]] (concept) — in-service flaw evaluation; FFS Part 9 (crack-like flaws) is the in-service counterpart to Division 3 design-time fracture mechanics.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
