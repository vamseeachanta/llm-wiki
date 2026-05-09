---
title: "O&G Papers catalog — OnePetro"
slug: og-standards-onepetro
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/OnePetro
ingested: 2026-05-09
tags: ["og-standards-ingest", "onepetro", "papers", "conference", "publisher-catalog", "otc", "spe", "marine-renewable-energy", "mooring-integrity"]
---

# O&G Papers catalog — OnePetro

> Metadata-first source page for the OnePetro slice of the O&G-Standards consolidated library at `/mnt/ace/O&G-Standards/OnePetro/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, paper IDs, conference years, file paths) are recorded here.
>
> **Framing note**: OnePetro is the SPE-operated paper-aggregation service that hosts content from SPE, OTC (Offshore Technology Conference), AAPG, SEG, IADC, SPWLA and other societies — it is *not* itself a publisher of standards. This catalog page is therefore framed as a **paper catalog** rather than a standards catalog, and the directory contains a mix of conference papers, paper-submission working files (abstracts, copyright forms, OASIS confirmations), author-contact spreadsheets, and a small number of cross-referenced standards (AISC, ASME, AWS, ANSI/ASQ, DNV).

## Summary

OnePetro folder is in practice a 2014–2015 OTC paper-submission working directory anchored on a Marine Renewable Energy (MRE) special-session organized through ASCE/COPRI, plus an adjacent mooring-integrity track (papers OTC-25134, OTC-25273, OTC-26035) and a sparse set of older OTC papers (OTC-3902 Stahl 1980, OTC-7325, OTC-8494 1997 Code Conflicts, OTC-13109 SCR fatigue 2001, OTC-23161 ZIG WIV) and SPE papers (SPE-163884). The 94 catalog entries break down roughly as: ~32 OTC conference papers (final + draft form), ~9 SPE papers, ~9 MRE special-session abstracts/keynotes (`SS_Marine_Renewable_Energy_*` + `OTC_2015_*`), ~26 paper-submission working files (OASIS Online Abstract Submission System receipts, paper-information forms, copyright transfer forms, author-contact spreadsheets, OTC grids and revision histories), and 6 cross-referenced standards (AISC SPEC 360 2nd & 3rd Ed, ASME B16.48, AWS A5.10, ANSI/ASQ Z1.9, SAE AMS 4931D, DNV OS-J103 floating wind turbines). Modal year is 2015 (driven by the OTC-2015 special-session prep wave); span is 1985–2015 by filename year, 1999–2015 by `modified_date`.

## Metadata

| Field | Value |
|-------|-------|
| id | og-standards-onepetro |
| publisher | OnePetro (SPE-operated aggregation service for OTC, SPE, AAPG, SEG, IADC, SPWLA, etc.) |
| document_count | 94 |
| total_size_bytes | 134,806,358 |
| total_size_mb | 134.8 |
| extension_breakdown | .pdf: 49, .docx: 26, .doc: 11, .xlsx: 8 |
| sub_category_breakdown | All 94 docs at top level (no subfolders) |
| year_range | 1985–2015 by filename year (modal 2015); 1999–2015 by file modified_date |
| top_year_buckets | 2015: 11, 2001: 1, 2005: 1, 2010: 1, 2008: 1, 1999: 1, 1985: 1, 2011: 1, 1997: 1 |
| modified_date_span | 1999-12-07 to 2015-08-05 |
| primary_societies | OTC (~32 papers), SPE (~9 papers), ASCE/COPRI (MRE special-session co-organizer) |
| working_file_share | High — ~26 of 94 files are submission-pipeline artefacts (abstracts, copyright forms, OASIS confirmations, grids) rather than published papers |
| parent_root | /mnt/ace/O&G-Standards/OnePetro |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db (6.8 GB sqlite) |
| raw_source_policy | link-only; do not copy raw bulk data into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md (E13) |

## Topical coverage map

Papers grouped by primary society and theme. Identifiable paper IDs shown; working files (abstracts, OASIS confirmations, etc.) summarized in aggregate.

### OTC (Offshore Technology Conference) — published papers

| Paper ID | Subject (from filename) | Form |
|----------|-------------------------|------|
| OTC-3902 | Stahl — Design Methodology for Offshore Platform | PDF |
| OTC-5468 | (subject not in filename) | PDF |
| OTC-7325-MS | (subject not in filename) | PDF |
| OTC-8494 (OTC1997-8494) | Code Conflicts | PDF |
| OTC-13109 (OTC2001-13109) | SCR Fatigue at Low KC | PDF |
| OTC-15OTC-P-1865-OTC | (2015 conference paper P-1865) | PDF |
| OTC-23161 | ZIG WIV (vortex-induced vibration) | PDF |
| OTC-25108-MS | Probability — Haverty | PDF |
| OTC-25134-MS | Mooring Integrity Management — A State of the Art Review | PDF (2 copies, draft + final) |
| OTC-25273-MS | Mooring Failures and Pre-emptive Replacement | PDF |
| OTC-25960 | Design Procedures for Marine Renewable Energy Foundations | DOC |
| OTC-25992-MS | (Draft Review) | DOCX |
| OTC-26035-MS | Mooring Systems | DOC + DOCX (draft) |
| OTC-26055 | Keynote Address | DOCX (2 copies) |

### OTC 2015 — Marine Renewable Energy ASCE/COPRI Special Session (working files)

This special session is the densest single theme in the catalog. Working files include:

- `15OTC_Grid` (3 versions: 11.24.14, FINAL, MissingPapers-2)
- `15OTC_AuthorInformation` (2 copies)
- `15otc_cfp_web.pdf` (call-for-papers)
- `2015_Special_OTC_Session.pdf`
- `OTC_2015_COPRI_MRE_Special_Session_Rv1` through `Rv5` (5 revision DOCX)
- `SS_Marine_Renewable_Energy_*` series: Mooring, Foundations Design, Risk and Reliability, Inspection of Facilities, Keynote 1 (2 copies, one IM-approved)
- Abstract drafts: `OTC_2015_Abstract_-_Wave_Energy_-_R2.docx`, `OTC_2015_Abstract_-_In-Stream_Hydrokinetic_-_v3.docx`
- `KeynoteAddressOTC-MRE_2014.docx`
- `OTECforOTC2013Abstract.doc`

### SPE (Society of Petroleum Engineers) — published papers

| Paper ID | Subject (from filename) |
|----------|-------------------------|
| SPE-163884-MS | (subject not in filename) |
| (8 additional SPE-classified files; subject lines not always parseable from filenames alone) | |

### Mooring & riser integrity (theme cluster, primarily OTC)

- `WhyGoodMooringSystemsGoBad.pdf`
- `Lecture_77_-_Floating_Vessel_Moorings_–_Vulnerability_&_Integrity_(David_Brown).pdf`
- `Attachment_12_-_RG_2_Mooring_Update.pdf`
- `Geotechnical_Aspects_of_Submarine_Cables.pdf`
- `Senanayake_Monopile_ASCE_OTC_Special_Sessions_1-Oct-14.xlsx`
- `Design_of_Large_Diameter_Monopiles_under_Lateral_Loads_in_Normally_to_Lightly_Overconsolidated_Clay.docx` (2 copies)
- `tidal_turbulence_spectra_from_a_compliant_mooring.pdf`
- `Devlin_Browne_UW_Inspection_Abstract_25Jan2012.doc`

### Author-track files (named author drafts; OTC-2015 special-session contributors)

- `a1508_7_Alany.docx`, `a1553_10_Senanayake.docx`, `a1865_1_Sevens/Stevens.doc/.pdf`, `a1895_1_VanZweiten.docx/.pdf`, `a1983_4_McCall_WECs.pdf`, `a2155_4_Stewart_Keynote.docx`, `a2157_1_Stewart_Mooring.docx`
- `Bob_Stevens_Design_Procedures.doc`
- `Stahl,_OTC_3902,_Design_Methodology_for_Offshore_Platform_C.pdf`
- `Pierson,_Jr.,_W.J.,_et_al,_1964_-_a_Proposed_Spectral_Form_.pdf` (foundational JONSWAP-precursor reference, filename year 1964 but file modified later)
- `Kamijo,_K,_et_al,_1985_-_Performance_of_Small_High_Speed_Cr.pdf`

### Submission-pipeline working files (not paper content)

- `26035_Paper_Information_Form.pdf`, `26055_Paper_Information_Form.pdf` (paper-info forms)
- `26035_Transfer_of_Copyright_Form.pdf`, `26055_Transfer_of_Copyright_Form.pdf` (copyright transfer)
- `OASIS_26055_Subission_-_Notification_System.pdf`
- `Oasis,_The_Online_Abstract_Submission_System_-_Confirmation*.pdf` (5 confirmations: generic + Jack + mooring)
- `Author_Contact_Information(2.18.15).xlsx`
- `Instructions_for_Submitting_an_Abstract_Online_OTC_05_17_2013.pdf` (2 copies)
- `OIA_at_OTC.pdf`
- `ASCE_OTC_Special_Sessions_1-Oct-14.xlsx`
- `OTC_Paper_Submission_-_Wave_Energy.pdf`

### Cross-referenced standards (not OnePetro publications, filed alongside)

| Document | Purpose in folder |
|----------|-------------------|
| AISC SPEC 360 2nd Ed (2005), 3rd Ed (2010) | Structural-steel-buildings reference for OTC papers |
| ASME B16.48-1997 | Steel line blanks / spectacle blinds |
| AWS A5.10 (1999) | Bare aluminium and aluminium-alloy welding electrodes |
| ANSI-ASQ Z1.9 (2008) | Sampling procedures for inspection by variables |
| SAE AMS 4931D (2011) | Aerospace material specification |
| DNV OS-J103 (2013-06) | Floating wind turbines (cross-cut to MRE special session) |
| `rpt001-3_Deep_Water_Drilling_Riser_Integ_Manag_-_Part_1_Inspection_-_Nov_1997.doc` | Deepwater drilling-riser integrity-management report |

## Verification

- Document count cross-checked against `_catalog.json` `statistics.by_organization.OnePetro = 94`
- All 94 documents are at top level (no subfolders), per `organizations.OnePetro.General = 94`
- Society/conference classification is **inferred** from filename patterns, not from the catalog itself — `_catalog.json` does not record paper-society metadata. Counts are approximate (~32 OTC, ~9 SPE, ~26 working files, etc.) and will reclassify as the deep-extraction queue (#2536) parses paper bodies and copyright pages.
- The catalog mixes finished papers and submission-pipeline drafts — readers must not treat every PDF as a published OnePetro reference. Working files (`Oasis_*`, `*_Information_Form*`, `*_Copyright_Form*`, `*_Author*`, `*_Grid*`, `*_Special_Session_Rv*.docx`) are administrative artefacts.
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any OnePetro files flagged as DRM-protected
- `_inventory.db` provides per-page OCR text for all PDFs (consume via SQLite, do not copy into wiki)

## Recommended follow-ups

1. **Society-level reclassification**: file a hygiene issue against `_catalog.json` to add a `society` field (OTC, SPE, AAPG, SEG, IADC, SPWLA) for OnePetro entries. Filename heuristics get most of the way there (`OTC[-_ ]\d{4,5}` → OTC; `SPE[-_ ]\d{4,7}` → SPE), but published-paper metadata (DOI, conference name, conference year) needs a deep-extraction pass.
2. **Concept-page cross-references** (high-leverage):
   - **Mooring integrity** — papers OTC-25134, OTC-25273, OTC-26035, plus `WhyGoodMooringSystemsGoBad.pdf` and David Brown's vulnerability-&-integrity lecture form a coherent mooring-integrity reading list. Consider a `concepts/mooring-integrity-management.md` page citing them.
   - **Marine Renewable Energy** — the OTC-2015 special-session bundle (mooring, foundations, risk/reliability, inspection, wave energy, in-stream hydrokinetic, tidal turbulence) is unusually complete for an MRE-engineering reading list. Consider a `concepts/marine-renewable-energy-engineering.md` cross-link.
   - **SCR fatigue** — OTC2001-13109 (SCR Fatigue at Low KC) cross-links to DNV RP-F204 (already covered in `og-standards-dnv`) and the riser-VIV concept space (OTC-23161 ZIG WIV).
3. **Per-paper standards/ pages: NO**. OnePetro entries are conference papers, not standards — they belong on `concepts/` or `entities/` pages cited as references, not in `wiki/standards/`. The standards-page schema (code_id, publisher, revision) does not apply.
4. **Submission-pipeline filtering**: when constructing reading lists from this catalog, filter out the ~26 administrative working files (Oasis confirmations, copyright forms, paper-information forms, author-contact spreadsheets, conference grids, special-session revisions). These are valuable provenance for the OTC-2015 MRE special session but not engineering content.
5. **Cross-referenced standards relocation**: the AISC, ASME, AWS, ANSI/ASQ, SAE, DNV files filed under `OnePetro/` are misclassified — they belong under their own publisher folders. Flag for catalog-hygiene reclassification alongside the ISO top-level pollution issue.
