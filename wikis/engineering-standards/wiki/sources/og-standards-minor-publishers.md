---
title: "O&G Standards catalog — minor publishers (AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME)"
slug: og-standards-minor-publishers
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - /mnt/ace/O&G-Standards/MIL
  - /mnt/ace/O&G-Standards/NEMA
  - /mnt/ace/O&G-Standards/Norsok
  - /mnt/ace/O&G-Standards/SNAME
  - /mnt/ace/O&G-Standards/Unknown
ingested: 2026-05-09
tags: ["og-standards-ingest", "aws", "nema", "mil", "nace", "iec", "hse", "norsok", "sname", "standards", "publisher-catalog", "minor-publishers", "consolidated"]
---

# O&G Standards catalog — minor publishers (AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME)

> Metadata-first roll-up source page for eight low-footprint publishers in the consolidated O&G-Standards library at `/mnt/ace/O&G-Standards/`. Generated 2026-05-09 from `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25).
> **Vendor PDFs do not enter this repo** per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, file paths) are recorded here.

## Summary

This page consolidates eight low-footprint publishers — **AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME** — that together account for only **41 documents (~681 MB)** in the catalog. A single roll-up beats eight near-empty per-publisher pages: each individual publisher carries 1–9 documents, well below the ~20-doc split-out threshold used elsewhere in this wiki. Four of the eight (**AWS, NACE, IEC, HSE**) are not first-class organizations in the consolidator — they live inside the Unknown bucket and were extracted here by filename pattern, which is itself evidence the Unknown bucket needs a reclassification pass (see [Unknown bucket](#unknown-bucket-629-docs) below).

## Aggregate metadata

| Field | Value |
|-------|-------|
| id | og-standards-minor-publishers |
| publishers covered | AWS, NEMA, MIL, NACE, IEC, HSE, Norsok, SNAME |
| document_count (aggregate) | 41 |
| total_size_bytes | 680,995,561 |
| total_size_mb | 681.0 |
| extension_breakdown | .pdf: 41 |
| parent_roots | `/mnt/ace/O&G-Standards/MIL`, `/mnt/ace/O&G-Standards/NEMA`, `/mnt/ace/O&G-Standards/Norsok`, `/mnt/ace/O&G-Standards/SNAME`, `/mnt/ace/O&G-Standards/Unknown` (AWS, NACE, IEC, HSE all live under `Unknown/`); 1 AWS doc filed under `API/`, 1 under `OnePetro/` |
| catalog_source | /mnt/ace/O&G-Standards/_catalog.json |
| catalog_classification | AWS, NACE, IEC, HSE: **not** top-level orgs in catalog `statistics.by_organization` — extracted here by filename regex from the Unknown bucket. NEMA, MIL, Norsok, SNAME: first-class top-level orgs |
| ocr_text_root | /mnt/ace/O&G-Standards/_ocr_text |
| inventory_db | /mnt/ace/O&G-Standards/_inventory.db |
| raw_source_policy | link-only; do not copy raw PDFs into git/wiki raw folders |
| extract_priority | metadata-only (per #2536 deep-extraction queue) |
| ingest_loop | docs/sessions/2026-05-08-llm-wiki-completeness-loop.md |

## Per-publisher breakdown

### AWS (American Welding Society)

- **Doc count:** 9 (extracted from Unknown bucket by `^AWS\s` filename pattern; 1 also filed under `API/`, 1 under `OnePetro/`)
- **Size:** ~465 MB (largest of the eight, dominated by D1.1 scanned editions)
- **Year range:** 1999–2010
- **Parent roots:** `/mnt/ace/O&G-Standards/Unknown`, `/mnt/ace/O&G-Standards/API`, `/mnt/ace/O&G-Standards/OnePetro`
- **Representative docs:**
  - AWS D1.1 (2006, 2009, 2010) — Structural Welding Code – Steel (multiple editions, both Scanned and Searchable copies)
  - AWS D1.2 (2003) — Structural Welding Code – Aluminum
  - AWS A2.4 (2007) — Standard Symbols for Welding, Brazing, and NDE
  - AWS A5.10 (1999) — Spec for Bare Aluminum & Aluminum-Alloy Welding Electrodes & Rods

### NEMA (National Electrical Manufacturers Association)

- **Doc count:** 4 (top-level org); **note:** 2 of the 4 are mis-filed wave-kinematics papers (Gudmestad, Pawsey) that landed in `NEMA/` despite no NEMA content
- **Size:** ~24 MB (NEMA 250 PDF accounts for 23 MB)
- **Year range:** 1983–2008
- **Parent root:** `/mnt/ace/O&G-Standards/NEMA`
- **Representative docs:**
  - NEMA 250 (2008) — Enclosures for Electrical Equipment (1000 V Maximum)
  - Material Damping of Free Hanging Pipes — Theoretical and Experimental Studies *(mis-filed)*
  - Gudmestad, O.T. et al — Regular Wave Kinematics *(mis-filed; should move to a wave-kinematics concept page)*

### MIL (US Military Standards / DoD)

- **Doc count:** 7 (top-level org); 2 are mis-filed offshore-research papers (Miller 1985, Valenchon 2000)
- **Size:** ~165 MB (MIL-5G/5J aerospace metallic-materials handbooks dominate)
- **Year range:** 1987–2003
- **Parent root:** `/mnt/ace/O&G-Standards/MIL`
- **Representative docs:**
  - MIL-HDBK-5G extract (1994), MIL-HDBK-5J (2003) — Metallic Materials and Elements for Aerospace Vehicle Structures
  - MIL-HDBK-217F (1991) — Reliability Prediction of Electronic Equipment
  - MIL-S-23009C (1987) — Steel Forgings, Alloy, High Yield Strength (HY-80 and HY-100)

### NACE (National Association of Corrosion Engineers)

- **Doc count:** 5 (extracted from Unknown bucket by `^NACE\s` and `^TM\d{4}` patterns)
- **Size:** ~3.7 MB
- **Year range:** 1995–2009
- **Parent root:** `/mnt/ace/O&G-Standards/Unknown`
- **Representative docs:**
  - NACE MR-0175 (1995) — Sulfide Stress Cracking Resistant Metallic Materials for Oilfield Equipment
  - NACE MR-0175 Pt 1 / Pt 2 / Pt 3, 2nd Ed (2009) — General principles, carbon/low-alloy steels, CRAs
  - TM0177-96 — H₂S Cracking Test Procedures

### IEC (International Electrotechnical Commission)

- **Doc count:** 4 (extracted from Unknown bucket by `^IEC\s\d` pattern; excludes IEC 61400 wind reference embedded in a longer filename)
- **Size:** ~0.8 MB (text-only PDFs)
- **Year range:** 1982–2004
- **Parent root:** `/mnt/ace/O&G-Standards/Unknown`
- **Representative docs:**
  - IEC 60038 6th Ed (1983) — Standard Voltages
  - IEC 60092 3rd Ed (2004) — Insulating materials for shipboard and offshore units
  - IEC 60228 3rd Ed (2004) — Conductors of insulated cables
  - IEC 60304 3rd Ed (1982) — Standard colours for low-frequency cable insulation

### HSE (UK Health and Safety Executive)

- **Doc count:** 2 (extracted from Unknown bucket by `^HSE\s` pattern)
- **Size:** ~4.9 MB
- **Year range:** 1999–2001
- **Parent root:** `/mnt/ace/O&G-Standards/Unknown`
- **Representative docs:**
  - HSE OTH 01015 (2001) — Steel
  - HSE OTH 92390 (1999) — Background to New Fatigue Guidance for Steel Joints and Connections in Offshore Structures

### Norsok (Norwegian petroleum-industry standards)

- **Doc count:** 9 (top-level org)
- **Size:** ~14.6 MB
- **Year range:** 1994–2010
- **Parent root:** `/mnt/ace/O&G-Standards/Norsok`
- **Representative docs:**
  - Norsok N-001 — Structural design (4th Ed 2004, 7th Ed 2010)
  - Norsok N-004 — Design of Steel Structures (1st Ed 1998, 2nd Ed 2004)
  - Norsok M-001 4th Ed (2004) — Materials selection
  - Norsok M-501 — Surface Preparation and Protective Coating (4th Ed 1999, 5th Ed 2004)
  - Norsok M-710 — Qualification of non-metallic sealing materials
  - Norsok D-SR-022 (1994) — BOP, Diverter and Drilling Riser System

### SNAME (Society of Naval Architects and Marine Engineers)

- **Doc count:** 1 (top-level org — by far the smallest)
- **Size:** ~2.1 MB
- **Year range:** unspecified in filename
- **Parent root:** `/mnt/ace/O&G-Standards/SNAME`
- **Representative doc:**
  - SNAME 5-5 and 5-5A Rev 3 (Panel Member copy) — guidance for site-specific assessment of jack-up units (T&R Bulletin family)

## Unknown bucket (629 docs)

The catalog reports `statistics.by_organization.Unknown = 629` — these are documents the consolidator's organization classifier could not auto-route. They live under `/mnt/ace/O&G-Standards/Unknown/`. After extracting AWS / NACE / IEC / HSE by filename regex (20 docs), **611 residual Unknown docs remain.**

A random sample of 10 residual filenames (seed=2026) gives a flavour of what is in this bucket:

- `ASME B16.5-2013.pdf` — ASME flange standard (publisher = **ASME**, missing from top-level orgs)
- `asme.b31.8.2003.pdf` — ASME B31.8 gas-pipeline transmission code
- `ASME B16.33 - 2002.pdf` — ASME B16.33 manual gas valves
- `ASME B16 10 F TO F VALVES.pdf` — ASME B16.10 face-to-face valve dimensions
- `ASCE_7-05_Minimum_Design_Loads_for_buildings_and_other_Struc.pdf` — ASCE-7 (publisher = **ASCE**, missing)
- `Part1OffshoreCorrigenda-Feb14.pdf` — likely an LR / IACS / Class corrigendum
- `Vandiver, J.K., 1998 - Research Challenges in the Vortex-In.pdf` — academic VIV paper, not a standard
- `Wave,_Tidal_and_Floating_Offshore_Wind_Energy_Companies_(2010)(1).xls` — industry directory, not a standard
- `4Subsea_ PSA-Norway_Flexibles-rev5.pdf` — vendor / regulator report
- `Houston Codes and Standards Priority List.xlsx` — internal spreadsheet, metadata only

**Three obvious classification gaps surface immediately:**

1. **ASME** — many ASME B16/B31 codes are sitting in Unknown without a top-level org bucket. ASME would likely become the second- or third-largest publisher after a reclassification pass.
2. **ASCE** — minor but distinct (ASCE-7 design loads).
3. **Mixed non-standard content** — academic papers, industry directories, and internal spreadsheets are lumped in with standards. A second-pass classifier should split documents into `standard | paper | report | internal` before assigning a publisher.

**Status:** flagged `needs-reclassification`. Do not ingest the Unknown bucket exhaustively here — it would dilute this page beyond its consolidated-minor-publisher purpose.

## Verification

- Aggregate document count cross-checked: AWS(9) + NEMA(4) + MIL(7) + NACE(5) + IEC(4) + HSE(2) + Norsok(9) + SNAME(1) = **41**, matching the per-publisher selectors run against `_catalog.json`
- Catalog top-level orgs reconciled: NEMA(4) + MIL(7) + Norsok(9) + SNAME(1) = 21 first-class entries; AWS/NACE/IEC/HSE (20) extracted from Unknown bucket
- Unknown bucket count cross-checked: catalog `statistics.by_organization.Unknown = 629`; residual after extracting AWS/NACE/IEC/HSE = 611
- DRM status: see `/mnt/ace/O&G-Standards/drm_protected_files.txt` for any minor-publisher files flagged DRM-protected
- OCR text: `_inventory.db` (sqlite) provides per-page OCR text for all PDFs in this catalog (consume via SQLite, do not copy into wiki)
- **This combined page is intended to be split** if any of the eight publishers grow past ~20 documents in a future catalog refresh — see split-out triggers below

## Recommended follow-ups

1. **Per-publisher split-out triggers** — promote any of these eight publishers to its own `wiki/sources/og-standards-<publisher>.md` page when its document count exceeds **20**. Most likely candidates near term: AWS (already 9, well-worn welding codes get added often) and Norsok (9, active Norwegian standard family). NEMA / MIL / NACE / IEC / HSE / SNAME stay consolidated indefinitely unless catalog grows.
2. **Unknown bucket reclassification pass** — a single regex-classifier pass over the 611 residual Unknown filenames would lift out at least **ASME** (likely 50+ docs) and **ASCE** as new top-level orgs, and rescue the remaining AWS/NACE/IEC/HSE entries from being filename-pattern-only. Track as a follow-up issue.
3. **Mis-filed paper rescue** — 4 documents in NEMA/ and MIL/ are mis-filed academic papers (Gudmestad, Pawsey, Miller 1985, Valenchon 2000); these belong on a wave-kinematics or riser-dynamics concept page, not in publisher catalogs.
4. **Concept-page cross-links worth noting:**
   - **NACE MR-0175** — already targeted in W4-A of the prior loop for a corrosion / sour-service concept page; this source page is its catalog anchor.
   - **AWS D1.1** — feeds any future welding-code concept page; cross-link from structural-welding entries.
   - **Norsok N-004** — feeds offshore-steel-structures concept page alongside DNV OS-C101 and ISO 19902.
   - **HSE OTH 92390** — feeds the fatigue-guidance lineage (DNV RP-C203, API 2A-WSD fatigue commentary).
5. **Edition-history index** — Norsok N-001 (4th→7th), N-004 (1st→2nd), and M-501 (4th→5th) all show edition coverage worth a small comparison table once a per-publisher Norsok page is split out.
