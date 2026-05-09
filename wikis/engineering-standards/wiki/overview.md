---
domain: engineering-standards
created: 2026-04-28 19:24 UTC
last_updated: 2026-05-09
---

# Overview: Engineering Standards

This wiki indexes the engineering-standards substrate for the offshore / oil & gas / structural-engineering knowledge base. Source pages are metadata-first per the vendor-PDF firewall (spinout 2026-05-05): only publisher facts (titles, document IDs, revision years, file paths) live here; raw vendor PDFs remain at the private `/mnt/ace/O&G-Standards/` mount.

## Scope

The corpus snapshot (catalog version 1.0.0, generated 2025-12-25, ingested 2026-05-09) spans publisher slices from API, DNV, ABS, ASME, BSI, ASCE, ISO, ASTM (5 sub-series), OnePetro paper-aggregator, and a minor-publishers roll-up (AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME). Curated `wiki/standards/<code-id>.md` pages (per #2615 path-routing decision) carry the publisher-agnostic per-document write-ups; this overview focuses on the publisher-level catalog roll-up.

## Publisher coverage matrix

Source pages by publisher (all metadata-first, ingested 2026-05-09 unless noted). Document counts from `_catalog.json` filesystem walk; "in-scope" filters out misfiled / mis-shelved entries where applicable.

### Major publishers

| Publisher | Source page | Docs | Scope |
|-----------|-------------|------|-------|
| API | [og-standards-api](sources/og-standards-api.md) | 574 (~2.59 GB) | Largest publisher slice; RP 2A, Spec 5L/6A/6D, Spec 17 subsea family, MPMS measurement; 1977-2016 with 1995-2012 peak |
| DNV | [og-standards-dnv](sources/og-standards-dnv.md) | 100 | Offshore structures, pipelines (OS-F101), risers (OS-F201), mooring (OS-E301); cited by digitalmodel calc citations |
| ABS | [og-standards-abs](sources/og-standards-abs.md) | 6 | American Bureau of Shipping classing rules; offshore installations, FPSO, fatigue, dynamic positioning |
| ASME | [og-standards-asme](sources/og-standards-asme.md) | 88 | BPVC sections, B31 piping (.3/.4/.8), B16 flanges/valves, PCC-1, fitness-for-service; not in catalog `by_organization` enum (filesystem-walk only) |
| BSI | [og-standards-bsi](sources/og-standards-bsi.md) | 80 | British Standards; BS 7910 (fracture), BS EN ISO 13628 family (subsea), drill-through equipment |
| ISO | [og-standards-iso](sources/og-standards-iso.md) | 308 raw / ~112 in-scope | 19900-series (offshore), 13628 (subsea), 15156 (sour-service), 14224 (RAM); ~196 raw entries misclassified as personal/legal |
| ASCE | [og-standards-asce](sources/og-standards-asce.md) | 32 token-matched (4 standards + 28 committee artifacts) | Wind/seismic loads (ASCE 7), COPRI marine renewable energy |

### ASTM sub-series

| Sub-series | Source page | Docs | Scope |
|------------|-------------|------|-------|
| A (Iron & Steel) | [og-standards-astm-a-series](sources/og-standards-astm-a-series.md) | 2,147 across ~655 A-numbers | Plate, pipe, tube, fasteners, castings, rebar; metallurgical substrate for ASME/API/DNV; 1960-2008 |
| D (Petroleum/Polymers/Soils) | [og-standards-astm-d-series](sources/og-standards-astm-d-series.md) | 10,361 | Largest single committee bucket; petroleum products (D02), soils (D18) carry O&G load; 1953-2004 |
| E (Test Methods/NDE/Fracture) | [og-standards-astm-e-series](sources/og-standards-astm-e-series.md) | 3,531 (3,559 catalog) | Fracture mechanics, NDE, fatigue, metallography |
| G (Corrosion) | [og-standards-astm-g-series](sources/og-standards-astm-g-series.md) | 316 (307 in-scope) | Cathodic protection, sour-service exposure tests, electrochemistry |
| Top-level (B/C/F/other) | [og-standards-astm-top-level](sources/og-standards-astm-top-level.md) | 9,136 | Loose ASTM documents not filed under A/D/E/G; B (non-ferrous), C (cement/concrete), F (fasteners) |

### Aggregators and minor publishers

| Source page | Docs | Scope |
|-------------|------|-------|
| [og-standards-onepetro](sources/og-standards-onepetro.md) | 94 | OnePetro paper aggregator (SPE-operated; OTC/SPE/AAPG/SEG/IADC/SPWLA); papers, not standards |
| [og-standards-minor-publishers](sources/og-standards-minor-publishers.md) | 41 aggregate | Roll-up: AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME (each <20 docs threshold) |

### Earlier source pointers (DORIS / Elements)

| Source page | Added | Scope |
|-------------|-------|-------|
| [elements-doris-codes-specs](sources/elements-doris-codes-specs.md) | 2026-04-28 | Elements drive DORIS codes/specs corpus pointer |
| [doris-codes-specs-faceted-index](sources/doris-codes-specs-faceted-index.md) | 2026-04-29 | Faceted metadata index over DORIS corpus |
| [doris-techstreet-drop](sources/doris-techstreet-drop.md) | 2026-04-29 | Licensed-aggregator drop pointer |
| [doris-company-specs](sources/doris-company-specs.md) | 2026-04-29 | Confidential company/client specs pointer |
| [doris-deepstar](sources/doris-deepstar.md) | 2026-04-29 | DeepStar/JIP deliverables pointer |

## Catalog hygiene

Cross-cutting issues flagged across the iter-8/iter-9 ingest:
- ASME, AWS, NACE, IEC, HSE missing from `_catalog.json` `statistics.by_organization` enum (filesystem-walk recovery used).
- ISO top-level dump contains ~196 misfiled personal/business documents amid ~112 legit ISO standards.
- ASTM has ~1,000+ documents misfiled across series-boundary directories.
- OCR coverage across the 25,537-document ASTM substrate is <1% — full-text search not viable without an OCR sweep.

## Relationship to `wiki/standards/`

The `sources/` pages above are publisher-level catalog summaries. Per-document standards write-ups (with `code_id`, `publisher`, `revision` frontmatter) live under `wiki/standards/` — see [index.md](index.md) §Standards for the curated standards-page list (DNV-OS-F101, API RP 2A-WSD, ASME B31.3, etc.).
