---
title: "O&G Standards catalog — DNV"
slug: og-standards-dnv
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/DNV
ingested: 2026-05-09
tags: ["og-standards-ingest", "dnv", "standards", "publisher-catalog", "offshore", "pipelines", "risers", "mooring"]
---

# O&G Standards catalog — DNV

> Metadata-first source page for the DNV slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/DNV/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

DNV (Det Norske Veritas) catalog covers offshore-standards (OS), recommended-practices (RP), classification-notes (CN), offshore-service-specifications (OSS), and guidelines. The 100 deduplicated catalog entries span pipelines (OS-F101 across 6 editions 2000–2013), dynamic risers (OS-F201, RP-F204, RP-F205, RP-F206), position mooring (OS-E301), structural fatigue (RP-C203 across 4 editions), environmental loads (RP-C205), cathodic protection (RP-B401, RP-F103), free-spanning pipelines (RP-F105), corroded pipelines (RP-F101), on-bottom stability (RP-F109), pipeline coating (RP-F102, RP-F106), risk-based inspection (RP-G101), and offshore wind structures (OS-J101). The 1984–2016 publication-date span captures the evolution of DNV's offshore practice through the modern deepwater era.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-dnv |
| publisher | DNV (Det Norske Veritas) |
| document_count | 100 |
| total_size_bytes | 222,142,721 |
| total_size_mb | 222.1 |
| extension_breakdown | .pdf: 99, .xlsx: 1 |
| sub_category_breakdown | RP (Recommended Practices): ~48, OS (Offshore Standards): ~16, CN (Classification Notes): ~5, OSS (Offshore Service Specs): ~5, Guidelines: ~3, residual unsorted: ~23 |
| year_range | 1981–2016 (modal years 2009–2012) |
| top_year_buckets | 2012: 30, 2011: 17, 2009: 14, 2010: 8, 2014: 5 |
| parent_root | /mnt/ace/O&G-Standards/DNV |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

DNV codes referenced by document ID, with edition coverage in this catalog:

| Code | Subject | Editions present |
|------|---------|------------------|
| OS-F101 | Submarine Pipeline Systems | 2000, 2007, 2008, 2010, 2012, 2013 |
| OS-E301 | Position Mooring | 2008, 2010 |
| OS-F201 | Dynamic Risers | 2001, 2010 |
| OS-J101 | Offshore Wind Turbine Structures | 2007 |
| OSS-006 | Submarine Pipeline Systems (rules) | 1981 |
| OSS-101 | Offshore Drilling and Support Units | 2009, 2011 |
| OSS-300 | Risk-Based Verification | 2004, 2011 |
| OS-304 | Risk-Based Verification of Offshore Structures | 2006 |
| RP-A203 | Qualification of New Technology | 2001, 2011 |
| RP-B401 | Cathodic Protection Design | 1993, 2005 (w/2008 amendments), 2011 |
| RP-C203 | Fatigue Design of Offshore Steel Structures | 2000, 2005, 2008, 2011 |
| RP-C205 | Environmental Conditions and Environmental Loads | 2007, 2010 |
| RP-C206 | Fatigue Methodology of Offshore Ships | 2010 |
| RP-E102 | Recertification of BOPs and Well Control Equipment | 2010 |
| RP-F101 | Corroded Pipelines | 2004, 2010 |
| RP-F102 | Pipeline Field Joint Coating and Field Repairs | 2003, 2011 |
| RP-F103 | Cathodic Protection of Submarine Pipelines (Galvanic Anodes) | 2003, 2010 |
| RP-F105 | Free Spanning Pipelines | 2002, 2006 |
| RP-F106 | Factory-Applied External Pipeline Coating | 2003, 2011 |
| RP-F108 | Fracture Control for Pipeline Installation | 2006 (w/2009 update) |
| RP-F109 | On-Bottom Stability Design of Submarine Pipelines | 2007, 2011 |
| RP-F110 | Global Buckling of Submarine Pipelines | 2007 |
| RP-F112 | Stainless Steel Subsea Equipment under Cathodic Protection | 2006 (DRAFT), 2008 |
| RP-F116 | Integrity Management of Submarine Pipeline Systems | 2009 |
| RP-F201 | Design of Titanium Risers (3rd Ed) | 2001 |
| RP-F202 | Composite Risers | 2010 |
| RP-F203 | Riser Interference | 2009 |
| RP-F204 | Riser Fatigue | 2004, 2005, 2010 |
| RP-F205 | Global Performance Analysis of Deepwater Floating Structures | 2004, 2010 |
| RP-F206 | Riser Integrity Management | 2006 (DRAFT), 2008 |
| RP-G101 | Risk-Based Inspection of Offshore Topsides Static Mechanical Equipment | 2010 |
| RP-H101 | Risk Management in Marine and Subsea Operations | 2003 |
| RP-H102 | Marine Operations During Removal of Offshore Installations | 2004 |
| RP-O401 | Safety and Reliability of Subsea Systems | 1985 |
| CN-30.1 | Buckling Strength Analysis | 1984, 2004 |
| CN-30.2 | Fatigue Strength Analysis for Mobile Offshore Units | 1984 |
| CN-30.6 | Structural Reliability Analysis of Marine Structures | 1992 |
| CN-30.7 | Fatigue Assessment of Ship Structures | (year unspecified) |

## Verification

- Document count cross-checked against `_catalog.json` `statistics.by_organization.DNV = 100`
- Sub-category counts derived from `relative_path` parsing; residual `~23` are unsorted top-level files awaiting reclassification
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any DNV files flagged as DRM-protected
- `_inventory.db` provides per-page OCR text for all PDFs (consume via SQLite, do not copy into wiki)

## Recommended follow-ups

1. **Per-code standards/ pages**: codes with multi-edition coverage (OS-F101, RP-C203, RP-B401, RP-F101, RP-F204) warrant a `wiki/standards/dnv-<code-id>.md` page consolidating revision history. OS-E301 already has prior treatment via #2590.
2. **Topical concept pages**: cross-link this source into existing concepts/ for fatigue (RP-C203), environmental loads (RP-C205), pipeline integrity (RP-F101/F116), riser analysis (RP-F204/F205), and cathodic protection (RP-B401/F103).
3. **Edition-history index**: a comparison table showing which DNV codes have been superseded by DNV-GL or DNV (post-rebrand) revisions would close the version-tracking gap.
