---
title: "ASTM G48 — Pitting and Crevice Corrosion Tests in FeCl3"
slug: astm-g48
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g48
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - pitting
  - crevice
  - ferric-chloride
  - cra
  - stainless-steel
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G48 — Standard Test Methods for Pitting and Crevice Corrosion Resistance of Stainless Steels and Related Alloys by Use of Ferric Chloride Solution

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g48` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals) &nbsp;•&nbsp; **revision:** latest publisher edition (current ASTM G48 carries the year-suffix and reapproval cycle posted at the publisher catalog; the local on-disk corpus runs G48-99, G48-00, and G48-03 — see Edition history below).

## Scope

ASTM G48 specifies six related laboratory test methods that use acidified ferric chloride (FeCl3) solution to rank the **pitting** and **crevice corrosion** resistance of stainless steels, nickel-base alloys, cobalt-base alloys, and other corrosion-resistant alloys (CRAs):

- **Method A — Ferric chloride pitting test.** Total-immersion pitting screen at a fixed temperature (commonly 22 °C or 50 °C as specified by the user). Output is mass loss and pit depth/morphology after a fixed exposure (typically 72 hours).
- **Method B — Ferric chloride crevice test.** Same chemistry as Method A but with cylindrical PTFE or rubber-block crevice formers attached to the specimen. Output is mass loss plus a crevice attack rating per the procedural guidance of ASTM G46 (pit examination/rating).
- **Method C — Critical pitting temperature (CPT) test for nickel-base and chromium-bearing alloys.** Step-temperature exposure of an unshielded specimen until pitting initiates. Output is the **CPT** — the lowest temperature at which stable pitting is observed under the standard exposure window.
- **Method D — Critical crevice temperature (CCT) test for nickel-base and chromium-bearing alloys.** Same step-temperature framework as Method C but with crevice formers. Output is the **CCT** — the lowest temperature at which crevice attack initiates.
- **Method E — Refined CPT determination.** Procedural refinement of Method C with more rigorous specimen preparation and temperature-step controls.
- **Method F — Refined CCT determination.** Procedural refinement of Method D with the analogous tightening of crevice-former geometry and temperature-step controls.

The test methods are screening / ranking procedures: they produce comparative numbers (mass loss, pit depth, CPT, CCT) but do not by themselves specify acceptance criteria. **Acceptance limits are application-specific and are set by the specifying body** (project specification, materials standard, or end-user specification — e.g., NORSOK MDS, an oil company materials spec, or an EPC contract). G48 is heavily used for **material qualification of stainless and Ni/Co-base alloys destined for sour, chloride-rich environments** (subsea production hardware, sour-gas piping, seawater-injection systems, topsides instrumentation tubing).

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **four G48 PDFs spanning three distinct editions** (the 00 designation appears as two separately-hashed files — likely a re-scanned or differently-collated copy of the same edition):

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G48-99 | `G_48_-_99_RZQ4LTK5QQ_.pdf` | 1 file | 1999 reapproval / revision |
| G48-00 | `G_48_-_00_RZQ4LTAW.pdf`, `G_48_-_00_RZQ4LVJFRA_.pdf` | 2 files | 2000 revision (two catalog copies, distinct content hashes) |
| G48-03 | `G_48_-_03_RZQ4.pdf` | 1 file | 2003 revision |
| G48 (current) | not on disk | — | The publisher-current ASTM G48 edition is later than 2003 (multiple reapprovals have been issued in the post-2003 cycle); calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher catalog year-token sweep done for the [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) source page recorded G48 with **4 editions** in the catalog; that count matches the four file rows above. The wider G-series source page also notes G48 as a multi-edition code warranting a per-revision history table.

## Key parameters

The following are the procedural anchors that recur across the methods (consult the on-disk PDFs for clause-exact text — this page records only the design-of-test substrate):

| Parameter | Value / specification |
|-----------|----------------------|
| Test solution (Methods A, B) | **6.0 % w/w FeCl3 · 6H2O** in reagent water (≈ 100 g FeCl3·6H2O per 900 mL water) |
| Test solution (Methods C–F) | **6.0 % FeCl3 + 1.0 % HCl** acidified variant for the temperature-stepped CPT/CCT methods |
| Standard exposure duration | **72 hours** for Methods A/B; methods C–F use **24 hours per temperature step** |
| Standard test temperatures | Method A/B: typically 22 °C or 50 °C (specifier's choice); Methods C–F: stepped, commonly 5 °C steps |
| Surface finish | **Wet-ground to 600-grit SiC** (or finer) immediately before exposure; no passivation prior to test |
| Specimen geometry | Coupon ~25 mm × 50 mm × 2–6 mm thick (Methods A, C, E); Methods B, D, F add a cylindrical or multiple-crevice-assembly former held against the surface with a controlled load |
| Crevice former | PTFE cylindrical block (older revisions) or 12-tooth multiple-crevice-assembly washer (later revisions) — the specifying body picks the geometry |
| Solution-to-area ratio | Minimum solution volume per unit specimen area is specified to keep solution chemistry near-constant during exposure |
| Post-test inspection | Mass loss (mg/cm²); maximum and average **pit depth** (per [astm-g46](astm-g46.md) examination/rating practice); crevice attack index; visual photographs |
| Result reporting | Mass loss, pit depth distribution, CPT (Methods C, E), CCT (Methods D, F); pass/fail is **NOT** defined by G48 itself |

**Acceptance criteria are application-specific.** Common project-spec thresholds in offshore practice include "no pitting / no crevice attack at 50 °C in Method B" for 22Cr duplex hardware, and "CCT ≥ 35 °C by Method F" for 25Cr super-duplex subsea components — but those numbers come from the **specifying body's** materials data sheet (e.g., NORSOK MDS D44/D45/D55/D57 for super-duplex), not from G48 itself.

## Cross-references

- [astm-g46](astm-g46.md) — *Standard Guide for Examination and Evaluation of Pitting Corrosion.* Method B explicitly invokes G46 for pit and crevice attack rating. Mandatory companion for any G48 result-reporting workflow.
- [[astm-g78]] — *Standard Guide for Crevice Corrosion Testing of Iron-Base and Nickel-Base Stainless Alloys in Seawater and Other Chloride-Containing Aqueous Environments.* Closer to in-service flowing-seawater conditions; complementary to G48's static-immersion FeCl3 ranking.
- [asme-b16-34](asme-b16-34.md) / piping-class workflows — not a direct G48 caller but downstream consumer of CRA qualification evidence.
- [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) (and its alias [iso-15156-3](iso-15156-3.md) / NACE MR0175-3) — sour-service materials selection for CRAs. Project specs implementing MR0175-3 routinely cite G48 Method B/CCT thresholds as the qualification evidence for 22Cr and 25Cr duplex grades and for nickel-base alloys (UNS N06625 / N08825 / N06022 / N06059 / N06200) destined for sour service.
- [dnv-rp-f112](dnv-rp-f112.md) — *Design of Duplex Stainless Steel Subsea Equipment Exposed to Cathodic Protection.* RP-F112 cites G48 Method A and CCT-by-Method-F results as part of the duplex qualification evidence package for SS subsea components subject to CP.
- [[astm-a923]] — *Standard Test Methods for Detecting Detrimental Intermetallic Phase in Duplex Austenitic/Ferritic Stainless Steels.* Method C of A923 is itself a ferric-chloride corrosion test; G48 is the broader CRA-screening parent and A923 Method C is the duplex-intermetallic-detection specialization. The two are routinely reported together for duplex weld procedure qualification.
- [api-spec-6a](api-spec-6a.md) — *Wellhead and Christmas Tree Equipment.* Subsea wellhead CRA components (cladding, weld overlays, solid CRA forgings) are commonly qualified with G48 Method A or Method B at a project-specified temperature; the G48 acceptance value flows in through the supplemental requirements (PSL/PR uplift) clauses or through a cited NORSOK MDS.
- Concept anchor: [pitting-and-crevice-corrosion](../concepts/pitting-and-crevice-corrosion.md) — landing page for the G46/G48/G78 cluster.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G48-derived CPT, CCT, or pass/fail temperature.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the four-edition presence, the catalog file paths, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0048-11r15.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per #2482):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_48_-_99_RZQ4LTK5QQ_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_48_-_00_RZQ4LTAW.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_48_-_00_RZQ4LVJFRA_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_48_-_03_RZQ4.pdf`
