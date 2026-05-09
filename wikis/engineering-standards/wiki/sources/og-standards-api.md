---
title: "O&G Standards catalog — API"
slug: og-standards-api
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/API
ingested: 2026-05-09
tags:
  - og-standards-ingest
  - api
  - api-spec
  - api-rp
  - api-std
  - api-bull
  - api-tr
  - api-mpms
  - standards
  - publisher-catalog
  - upstream
  - downstream
  - pipelines
  - drilling
  - production
  - subsea
  - measurement
---

# O&G Standards catalog — API

> Metadata-first source page for the API slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/API/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

The American Petroleum Institute (API) is the principal U.S. petroleum standards body, publishing specifications, recommended practices, standards, bulletins, technical reports, and the Manual of Petroleum Measurement Standards (MPMS) that govern upstream drilling and production, subsea hardware, line pipe, pressure vessels, refinery and downstream equipment, fuels-and-lubricants quality, and custody-transfer measurement. With **574 documents (~2.59 GB)** in this catalog, API is the largest publisher slice — roughly 5.7× DNV's 100-document footprint — and its codes (e.g., RP 2A, Spec 5L, Spec 6A/6D, RP 14E, the Spec 17 subsea family, MPMS) are the most heavily cross-referenced normative anchors in DNV-OS, ABS, ISO 19900-series, NORSOK, and BSEE/30-CFR-250 traffic across the broader engineering-standards corpus. The slice spans publication years **1977–2016** with strongest coverage of 1995–2012 — the era when API consolidated offshore practice (RP 2A-WSD), launched the subsea Spec 17 family (17D/17E/17J/17K), and modernized line-pipe and wellhead specs (Spec 5L 42nd–44th editions, Spec 6A 19th–20th editions).

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-api |
| publisher | American Petroleum Institute (API) |
| document_count | 574 |
| total_size_bytes | 2,715,558,037 |
| total_size_mb | 2,589.8 |
| extension_breakdown | .pdf: 517, .doc: 29, .docx: 18, .xls: 9, .xlsx: 1 |
| sub_category_breakdown (catalog `doc_type`) | RP: 152, STD: 136, TR: 7, General/uncoded: 279 |
| sub_category_breakdown (filename heuristic) | RP: 170, Spec: 74, Std: 51, Bull: 15, TR: 7, Bare-code (e.g., 6A/5L/2N): 125, Unclassified: 132 |
| unique_codes_detected | ~240 distinct API code identifiers (filename heuristic) |
| publication_year_range (from filenames) | 1977–2016 |
| modified_date_range | 1997-04 – 2019 |
| top_modified_year_buckets | 2011: 142, 2004: 101, 2012: 49, 2000: 43, 2014: 37, 2010: 33, 2002: 31, 2007: 24 |
| top_publication_years (filename-derived) | 2001: 33, 1997: 21, 2000: 20, 1998: 19, 1996: 18, 1995: 17, 2003: 15, 1994: 14 |
| parent_root | /mnt/ace/O&G-Standards/API |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text/API (224 OCR text files) |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite, per-page text for all PDFs) |
| drm_protected_count_for_api | 0 (zero `/API/` paths flagged in `drm_protected_files.txt`) |
| content_hash_duplicates_within_api | 0 groups (every API file has a unique content_hash) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Series breakdown

API document numbering follows several parallel series. The catalog's `doc_type` field is conservatively populated (RP / STD / TR only — the rest fall to "General"); the filename heuristic below recovers a fuller picture.

| Series | Detected docs | Catalog `doc_type` | Topical scope |
|--------|---------------|--------------------|---------------|
| **RP** (Recommended Practice) | 170 | 152 | Engineering practice — offshore platforms (RP 2-series), subsea systems (RP 17-series), drilling (RP 7-series, RP 16-series), production operations (RP 14-series), inspection/integrity (RP 510, 570, 572, 574, 576, 578, 580, 581, 582), pressure relief (RP 520/521), fuels handling (RP 1604, 1632, 2003), pipelines (RP 1102, 1110, 1111). Largest single bucket. |
| **Spec / Specification** | 74 | (rolled into General by catalog `doc_type`) | Hardware-procurement specs — line pipe (Spec 5L, 5CT, 5UE), wellheads & trees (Spec 6A, 6D, 6AF, 8A, 8C), drilling equipment (Spec 7, 7K, 16A), subsea (Spec 17D, 17E, 17J, 17K). Highest dollar-weight per page in offshore EPC procurement. |
| **Std / Standard** | 51 | 136 | Cross-cutting standards — welding (Std 1104), tanks (Std 650, 653), heat exchangers (Std 661), pumps (Std 610), valves (Std 526, 527, 594, 599, 600, 602, 603), inspection (Std 510, 570). Heavily downstream/refinery-leaning relative to RP/Spec. |
| **Bull / Bulletin** | 15 | (in General) | Interim guidance documents — e.g., Bull 2INT-MET (interim metocean), Bull 2INT-EX (interim exposure), Bull 2INT-DG (interim damaged), Bull 2U (stability of stiffened cylindrical shells), Bull 2V (flat plate structures), Bull 2N (planning, designing, constructing structures and pipelines for arctic conditions). Often precursors to RP-grade material. |
| **TR** (Technical Report) | 7 | 7 | Background research / methodology — e.g., TR 17TR1, TR 17TR2 (subsea evaluation methodology), TR 5C3 (calculations for casing/tubing). |
| **MPMS** (Manual of Petroleum Measurement Standards) | scattered (chapters, see Topical map) | (in General) | Custody-transfer measurement — Chapters 1–22 cover terminology, tank gauging, proving systems, temperature/density determination, sampling, statistics. Distinct numbering scheme (Ch.X.Y). |
| **Bare-code / no series tag** | 125 | (in General) | Filenames like `6A_e20_Errata_1.pdf`, `2RD_2nd_ed_Unlocked.pdf`, `5L_2004.pdf` — same documents as the named-series, but stored without the `Spec/RP/Std` prefix. Series can be inferred from the alphanumeric code shape (e.g., `6A` ⇒ Spec, `2A` ⇒ RP). |
| **Unclassified / structural** | 132 | (in General) | Errata, addenda, ballot drafts, JIP reports, conference papers, and structural sections (`Sect_01.pdf`, `append_*.pdf`, `cover.pdf`, `TITLPAGE.PDF`) that were extracted from a parent compilation rather than catalogued as standalone codes. Cleanup candidate per duplicate/structural-fragment review. |

> **Coverage caveat.** The 279 catalog-`doc_type=General` documents and the 132 filename-heuristic Unclassified bucket overlap heavily — both reflect the same underlying gap in the catalog's normalisation pass. A future ingest improvement should reconcile filename → canonical code-id (e.g., `2A_SIM_JIP_Final_Report.pdf` → `RP 2A SIM`) before downstream consumers ground on this slice.

## Topical coverage map

Representative API codes detected in the catalog, with edition coverage parsed from filenames. The full detected set is ~240 codes; this table surfaces the ~50 most-significant entries by document count, file-size weight, multi-edition coverage, or downstream cross-reference frequency. Edition tags include catalog-derived years and explicit edition markers (`e1`, `2ed`, `1st Ed`).

| Code | Subject | Editions present (catalog) |
|------|---------|----------------------------|
| RP 2A-WSD | Planning, Designing, and Constructing Fixed Offshore Platforms — Working Stress Design | 1997, 2000, 2005, 2007, 2014, 21st ed, 22nd ed |
| RP 2A-LRFD | Planning, Designing, and Constructing Fixed Offshore Platforms — LRFD | (multiple editions; included under detected `RP 2ALFRD`) |
| RP 2GEO | Geotechnical and Foundation Design Considerations | 1st ed, 2011, 2014 |
| RP 2MET | Derivation of Metocean Design and Operating Conditions | 1st ed, 2008, 2010, 2014 |
| RP 2SK | Design and Analysis of Stationkeeping Systems for Floating Structures | 1996, 2005, 2007, 2nd ed, 3rd ed (+ 2008 Addendum) |
| RP 2SM | Design, Manufacture, Installation, and Maintenance of Synthetic Fiber Ropes for Offshore Mooring | 1st ed, 2001, 2007 |
| RP 2RD | Design of Risers for FPS and TLPs | 1998, 1st ed, 2009 |
| RP 2T | Planning, Designing, and Constructing Tension Leg Platforms | 1987, 1997, 1st ed, 2010, 2nd ed, 3rd ed |
| RP 2I | In-service Inspection of Mooring Hardware for Floating Structures | 3 editions |
| RP 2X | Recommended Practice for Ultrasonic and Magnetic Examination of Offshore Structural Fabrication | 1996, 3rd ed |
| RP 2Z | Preproduction Qualification for Steel Plates for Offshore Structures | 1998, 3rd ed |
| Spec 2B | Fabrication of Structural Steel Pipe | 2001 |
| Bull 2N | Planning, Designing, and Constructing Structures and Pipelines for Arctic Conditions | (4–6 docs incl. Errata, Print) |
| Bull 2U | Stability Design of Cylindrical Shells | 2000, 2004, 2nd ed, 3rd ed |
| Bull 2V | Design of Flat Plate Structures | 2nd ed (2000) |
| Bull 2INT-MET | Interim Guidance — Metocean Conditions in the Gulf of Mexico (post-Katrina/Rita) | 2007 |
| Bull 2INT-EX | Interim Guidance — Exposure Categories | 2007 |
| Bull 2INT-DG | Interim Guidance — Assessment of Existing Offshore Structures for Damaged/Degraded | 2007 |
| Spec 5L | Specification for Line Pipe | 1999, 2000, 2004, 2007, 2012, 42nd ed, 43rd ed, 44th ed |
| Spec 5CT | Casing and Tubing | 2005, 2011, 8th ed, 9th ed |
| RP 5UE | Field Inspection of New Casing, Tubing, and Plain-end Drill Pipe | 1st ed, 2002, 2005, 2009, 2nd ed |
| Spec 6A | Wellhead and Christmas Tree Equipment | 1999, 2003, 2004, 2011, 17th ed, 19th ed, 20th ed (with multiple Addenda 1–3 and Errata 1–6) |
| Spec 6D | Specification for Pipeline Valves (also adopted as ISO 14313) | (multiple editions; Annex F + 2 errata sets) |
| Spec 6AF | Capabilities of API Flanges Under Combinations of Load | 1995, 2008, 2nd ed |
| Spec 7 | Drill Stem Elements | 1st ed, 2001, 2006, 2008, 2009, 2011, 40th ed |
| Spec 7K | Drilling and Well-Servicing Equipment | 2016 (5th ed) |
| RP 7G | Drill Stem Design and Operating Limits | 16th ed, 1998, 2000, 2009 |
| Spec 8A | Drilling and Production Hoisting Equipment | 13th ed |
| Spec 8C | Drilling and Production Hoisting Equipment (PSL 1 and PSL 2) | 1997, 2003, 3rd ed, 4th ed |
| RP 14C | Analysis, Design, Installation, and Testing of Safety Systems for Offshore Production Facilities | 2001, 2007, 7th ed |
| RP 14E | Design and Installation of Offshore Production Platform Piping Systems | 1991 (5th ed) |
| RP 14J | Design and Hazards Analysis for Offshore Production Facilities | 2001, 2nd ed |
| RP 16Q | Design, Selection, Operation, and Maintenance of Marine Drilling Riser Systems | 1993, 1st ed, 2015 |
| Spec 16A | Drill-through Equipment | (multiple editions) |
| RP 17A | Design and Operation of Subsea Production Systems — General Requirements and Recommendations | 1996, 2nd ed |
| RP 17B | Recommended Practice for Flexible Pipe | 1998, 2002, 2008, 2014, 2nd ed, 4th ed, 5th ed |
| Spec 17D | Design and Operation of Subsea Production Systems — Subsea Wellhead and Tree Equipment | 1992, 1993, 1996, 1st ed, 2011, 2nd ed |
| Spec 17E | Specification for Subsea Umbilicals | 2003, 2010, 3rd ed, 4th ed |
| RP 17G | Design and Operation of Completion/Workover Riser Systems | 1995, 1st ed, 2006, 2nd ed |
| Spec 17J | Specification for Unbonded Flexible Pipe | 1996, 1st ed, 2002, 2008, 2009, 2010, 2014, 2nd ed, 3rd ed, 4th ed |
| Spec 17K | Specification for Bonded Flexible Pipe | 1st ed, 2001, 2005, 2nd ed |
| TR 17TR1 / 17TR2 | Subsea Production Systems — evaluation methodology and verification | 1st ed, 2003 |
| RP 75 | Recommended Practice for Development of a Safety and Environmental Management Program (SEMS) | 1998, 1999, 2004, 2008, 2nd ed, 3rd ed |
| Std 1104 | Welding of Pipelines and Related Facilities | 1999, 2001, 2005, 19th ed, 20th ed |
| RP 1102 | Steel Pipelines Crossing Railroads and Highways | 1993 |
| RP 1110 | Pressure Testing of Steel Pipelines for the Transportation of Gas, Petroleum Gas, Hazardous Liquids, Highly Volatile Liquids, or Carbon Dioxide | 1991, 1997 |
| RP 1111 | Design, Construction, Operation, and Maintenance of Offshore Hydrocarbon Pipelines (Limit-State Design) | 1998, 1999, 2009, 2011, 3rd ed, 4th ed |
| Std 1163 | In-line Inspection Systems Qualification | 1st ed (2005) |
| RP 1632 | Cathodic Protection of Underground Petroleum Storage Tanks and Piping | 1996 |
| RP 2201 | Procedures for Welding or Hot Tapping on Equipment in Service | 1995 |
| Std 510 | Pressure Vessel Inspection Code: In-service Inspection, Rating, Repair, and Alteration | 2001 |
| Std 570 | Piping Inspection Code: In-service Inspection, Rating, Repair, and Alteration of Piping Systems | 2001, 2006 |
| RP 572 | Inspection Practices for Pressure Vessels | (2 editions) |
| RP 576 | Inspection of Pressure-relieving Devices | (2 editions) |
| RP 578 | Material Verification Program for New and Existing Alloy Piping Systems | 1996, 1999 |
| RP 582 | Welding Guidelines for the Chemical, Oil, and Gas Industries | 2001 |
| Std 526 | Flanged Steel Pressure-relief Valves | 2002 |
| RP 520 (Pt I/II) | Sizing, Selection, and Installation of Pressure-relieving Devices | 1994, 2000 |
| Std 579 / 579-1 (joint with ASME FFS-1) | Fitness-for-Service | 2007, 2016 |
| RP 581 | Risk-Based Inspection Technology | 2008 |
| Std 650 | Welded Steel Tanks for Oil Storage | 2001, 2003, 2007 |
| Std 661 | Air-Cooled Heat Exchangers for General Refinery Service | 2002 |
| Std 610 | Centrifugal Pumps for Petroleum, Petrochemical, and Natural Gas Industries | (current ed in catalog) |
| Std 602 | Compact Steel Gate Valves | 1998 |
| Std 2RD | Dynamic Risers for Floating Production Systems | 2nd ed |
| MPMS Ch. 1–22 (selected) | Manual of Petroleum Measurement Standards — terminology, tank gauging, dynamic measurement, proving, sampling, statistics, calculations | catalog hits scattered across `MPMS *` filenames |

> **Reading the editions column.** Multiple year tags (e.g., `Spec 5L: 1999, 2000, 2004, 2007, 2012`) reflect distinct catalog files — separate edition PDFs, not duplicate hashes (the content-hash duplicate count within `/API/` is **zero**). Edition markers like `42nd ed` co-exist with year tags because both appear independently in filenames.

## Verification

- **Document count cross-check.** `_catalog.json statistics.by_organization.API = 574`; on-disk `find /mnt/ace/O&G-Standards/API -type f -name '*.pdf' | wc -l = 507` (+ 57 non-PDF Office artefacts; full extension breakdown above). `ls /API/` returns 146 visible entries (top-level), with the residual 428 in subdirectories — the catalog is the source of truth.
- **Catalog `doc_type` vs. filename heuristic.** Catalog reports `RP: 152, STD: 136, TR: 7, General: 279`; filename heuristic recovers `RP: 170, Spec: 74, Std: 51, Bull: 15, TR: 7, Bare: 125, Unclassified: 132`. The gap is the 279 General bucket — primarily Specs and Bulletins that the catalog's `doc_type` did not normalise. Future improvement: a code-id resolver pass.
- **DRM check.** `grep -c '^/mnt/ace/O&G-Standards/API' drm_protected_files.txt = 0` — no API PDFs are flagged DRM-protected (in contrast to some other publishers in the corpus). All API PDFs in the catalog are openable for OCR/extraction.
- **OCR coverage.** `_ocr_text/API/` contains **224 OCR text files** (vs. 517 PDFs), so OCR coverage stands at ~43%. Gap is the OCR-extraction backlog (#2536). The `_inventory.db` SQLite file (6.8 GB) holds per-page text for all extracted PDFs and is the read-API for retrieval — never copy contents into the wiki repo.
- **Within-API hash duplicates.** Zero (`content_hash` collisions within the API set = 0 groups). `_duplicate_report.html` (143 KB, project-wide) covers cross-publisher and within-publisher duplicates; the API slice is clean of byte-for-byte copies. **Implication**: any apparent edition-redundancy (e.g., 6 separate `6A_e20_Errata_*.pdf` files) is real distinct content (separate errata documents), not file-management noise.
- **Structural-fragment artefacts.** ~125 of the 132 Unclassified entries are extracted sub-sections from a parent document (`Sect_01.pdf`, `append_*.pdf`, `Page 64 Metric Table 6.2 cont.pdf`, `cover.pdf`, `TITLPAGE.PDF`, `BKCOV.PDF`, etc.) plus draft/ballot artefacts (`Ballot 3468 Comments…xls`). These should not be promoted to per-code standards/ pages — they are working-paper traces, not standalone publications.
- **Publication-year vs. modified-year split.** Filename-derived publication years span **1977–2016**; filesystem `modified_date` spans **1997-04 – 2019** (the modal modified-year peak in 2011 reflects a bulk re-organisation, not a publication wave). Always trust filename year over `modified_date` when sourcing edition info.

## Recommended follow-ups

1. **Per-code `wiki/standards/<code-id>.md` promotion targets.** Codes already present in `wiki/standards/` (audited 2026-05-09):
   - `api-rp-2a-wsd.md`, `api-rp-2geo.md`, `api-rp-2met.md`, `api-rp-2sk.md`
   - `api-rp-1111.md`, `api-rp-14e.md` (planned), `api-rp-16q.md`, `api-rp-17b.md`
   - `api-spec-5l.md`, `api-spec-17j.md`, `api-std-2rd.md`, `api-17e.md`
   - **Highest-priority promotions still missing** (multi-edition + heavy downstream cross-reference):
     - **Spec 6A** (wellhead and tree, 7 docs in catalog spanning 1999–2011 + 6 errata) — the most cross-referenced API spec in subsea-tree work; merits its own page above the bare `api-spec-6a.md` slot.
     - **Spec 6D** (pipeline valves; ISO 14313 dual-numbered) — first-class procurement reference for pipelines and topsides.
     - **Spec 17D / 17E / 17K** — completes the Spec 17 subsea family (17J already promoted). 17E (umbilicals) and 17D (subsea wellheads/trees) are heavily referenced from DNV-OS-F101/F201.
     - **MPMS chapters** — measurement-standard pages do not yet exist; downstream / midstream cross-reference lattice (custody transfer, allocation) cannot ground without them. Candidate first pages: MPMS Ch.4 (Proving Systems), Ch.5 (Metering), Ch.11 (Physical Properties), Ch.14 (Natural Gas Measurement).
     - **Std 1104** (pipeline welding) — multi-edition (19th, 20th) and the canonical citation for pipeline welder qualification.
     - **Std 650** (storage tanks) — refinery / midstream tank-design anchor.
     - **Std 579 / 579-1** (FFS) — joint API/ASME, the definitive in-service integrity assessment standard; already shows 2007 + 2016 editions in catalog.
     - **RP 14E** — sizing of two-phase production piping (erosional velocity); the most cited single equation in offshore production design, currently planned but not yet present.
2. **Topical concept-page cross-links.** Cross-reference this source page from existing or new concept pages for: fixed-platform design (RP 2A-WSD), metocean (RP 2MET + Bull 2INT-MET), stationkeeping (RP 2SK), flexibles (RP 17B + Spec 17J/17K), drilling risers (RP 16Q), pipeline limit-state design (RP 1111), pipeline welding (Std 1104), pressure-vessel inspection (Std 510, RP 572, RP 581), and custody-transfer measurement (MPMS family — needs new concept page).
3. **Cross-publisher reference graph.** API codes are anchors for DNV-OS-F101 (cites Spec 5L, Spec 6D, Std 1104), ABS Guide for Building and Classing FPSOs (cites RP 2A, RP 2T, RP 17B), ISO 19900-series (ISO 19902 ↔ RP 2A-WSD, ISO 14313 ↔ Spec 6D), NORSOK U-001/U-002 (cites Spec 17 family). A `comparisons/api-iso-cross-reference.md` table would compress that lattice into one page.
4. **Catalog hygiene actions** (out-of-scope for this page; for the ingest-loop owner):
   - **Code-id normalisation**: write a resolver that maps the 279 catalog-`doc_type=General` entries to their canonical API code (`5L`, `6A`, `2A-WSD`, etc.) so the catalog's by-doc-type breakdown matches reality.
   - **Structural-fragment quarantine**: move ~125 extracted sub-sections (`Sect_*.pdf`, `append_*.pdf`, `Page NN…pdf`, `cover.pdf`) into a `_fragments/` sibling folder, leaving the API/ root populated only with whole-document publications.
   - **Errata stitching**: 6 separate `6A_e20_Errata_*.pdf` files belong together; emit a per-edition manifest (e.g., `Spec 6A 20th ed = Base + Addenda 1–3 + Errata 1–6`) for retrieval-side join.
   - **OCR backlog**: 224/517 PDFs OCR-coverage = ~43%. Top RP/Spec gaps should be enqueued in #2536 ahead of bulk-fragment OCR.
5. **Citation-contract pilot extension.** The mooring-design pilot at `digitalmodel/src/digitalmodel/orcaflex/mooring_design.py` cites DNV-OS-E301; extending the same pattern to API-anchored modules (e.g., RP 14E erosional-velocity, Spec 5L hydrostatic-test, Spec 6A pressure-test) would be the natural next step once the per-code standards/ pages above are populated with #2471-shape frontmatter.
