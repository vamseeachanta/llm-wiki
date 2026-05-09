---
title: "ASTM D975 — Diesel Fuel Oils"
slug: astm-d975
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d975
publisher: ASTM
revision: "2004 (latest in catalog); publisher-current edition is newer — see Edition history"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/d0975-25.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - diesel
  - fuel-spec
  - ulsd
  - standards
---

# ASTM D975 — Standard Specification for Diesel Fuel Oils

> **Standard identity (L0 prose).** `code_id`: astm-d975 · `publisher`: ASTM · `revision`: 2004 (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json`; ASTM reissues D975 on a roughly annual-to-biennial cadence and the publisher-current edition is newer than the catalog's 2004 copy — see *Edition history* below).

## Scope

ASTM D975 is the **master U.S. specification for diesel fuel oils** for compression-ignition (Diesel-cycle) engines. It defines **seven grades** of distillate and residual-blend diesel, distinguished along two axes — **volatility/viscosity class** and **sulfur tier**:

- **Volatility/viscosity classes**
  - **No. 1-D** — light distillate; lowest viscosity and lowest cloud point; for high-speed engines in cold climates and for service requiring frequent speed/load changes (transit buses, rail switchers in winter).
  - **No. 2-D** — middle distillate; the default on-road and off-road grade across the U.S.; higher energy density and higher cetane than No. 1-D, but higher cold-flow risk.
  - **No. 4-D** — heavier distillate / residual blend; for low- and medium-speed engines under sustained load (stationary power, marine auxiliary, rail mainline locomotives in some service).
- **Sulfur tiers** (overlaid on each volatility class)
  - **S15** — Ultra-Low-Sulfur Diesel (**ULSD**), 15 ppm sulfur maximum. Mandatory for U.S. on-highway use since 2006 and for non-road use since 2010 under EPA 40 CFR Part 80; required for engines with after-treatment (DPF, SCR) that is sulfur-poisoned by higher-sulfur fuel.
  - **S500** — 500 ppm sulfur maximum. Permitted for some legacy off-road, locomotive, and marine service in transition windows; effectively phased out for most regulated U.S. service.
  - **S5000** — 5000 ppm sulfur maximum. Only permitted in unregulated service (some heating-oil-adjacent industrial and mining applications); essentially equivalent to historical "regular" diesel before sulfur regulation.

The seven graded combinations sanctioned by D975 are: **No. 1-D S15, No. 1-D S500, No. 2-D S15, No. 2-D S500, No. 2-D S5000, No. 4-D, and No. 4-D (legacy).** D975 is the master spec invoked by U.S. on-road, off-road, non-road, locomotive, marine (in conjunction with marine-specific specs), and stationary-engine fuel contracts. It defers to ASTM **test methods** (D86 distillation, D93 flash, D445 viscosity, D613 cetane, D5453 / D2622 sulfur, etc.) for **how** each property is measured, while D975 itself fixes **the numeric limits** on each property by grade.

D975 does **not** cover **biodiesel B100** (covered by **ASTM D6751**), **biodiesel blends B6–B20** (covered by **ASTM D7467**), **aviation jet fuel** (covered by **ASTM D1655**), or **heating fuel oils** (covered by **ASTM D396**). It does, however, allow up to **5 vol% biodiesel (B5)** as an unlabeled component in any D975 grade — meaning U.S. retail diesel pumps marked "ASTM D975" may contain up to 5% biodiesel without separate disclosure.

## Edition history

ASTM D975 is reissued on a roughly annual-to-biennial cadence. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/D-Series/` (filename heuristic; D975 is identified as **9 multi-edition filename hits + 1 root-level `D975.PDF`** in the source-page audit):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| D 975 – 98 | `D_975_-_98_RDK3NS05OEJFMQ_.pdf` | 1998 issue |
| D 975 – 00 | `D_975_-_00_RDK3NS0WMA_.pdf` | 2000 issue |
| D 975 – 01 | `D_975_-_01_RDK3NS0WMQ_.pdf`, `D_975_-_01_RDK3NS0WMUE_.pdf` | 2001 issue (two reprint variants) |
| D 975 – 02 | `D_975_-_02_RDK3NS0WMG_.pdf` | 2002 issue |
| D 975 – 03 | `D_975_-_03_RDK3NS0WMW_.pdf` | 2003 issue |
| D 975 – 04 | `D_975_-_04_RDK3NQ_.pdf`, `D_975_-_04_RDK3NS0WNA_.pdf`, `D_975_-_04_RDK3NS1SRUQ_.pdf` | 2004 issue — **latest dated edition in catalog** (three reprint/tag variants) |
| D975 (untagged) | `D975.PDF` | Root-level untagged copy; edition unverified without OCR |

**10 catalog hits across at least 6 distinct dated editions (1998, 2000, 2001, 2002, 2003, 2004).** The 2004 edition is the latest in the catalog. ASTM has continued maintaining D975 on roughly annual reissue and the publisher-current edition is materially newer than 2004 — most importantly, the **S15 (ULSD) tier was added to D975 in the 2004–2007 revision window** to align with EPA 40 CFR Part 80, and the **B5 biodiesel allowance was incorporated in the 2008–2010 window**. Resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key requirements

D975 sets **numeric limits per grade** on the properties below and binds each property to a designated ASTM test method. The table below captures the canonical limits for No. 1-D and No. 2-D (the two most-cited grades); No. 4-D limits are looser on viscosity and distillation and are not reproduced here. Sulfur is shown for the **S15 (ULSD)** tier; the S500 and S5000 tiers raise the sulfur limit to 500 ppm and 5000 ppm respectively while leaving the other limits unchanged.

| Property | Test method | No. 1-D limit | No. 2-D limit |
|----------|-------------|---------------|---------------|
| Flash point | **ASTM D93** (Pensky-Martens closed-cup) | 38 °C min | 52 °C min |
| Cloud point | **ASTM D2500** / **D5773** (automatic) | report (region/season-dependent) | report (region/season-dependent) |
| Water and sediment | **ASTM D2709** | 0.05 vol% max | 0.05 vol% max |
| Sulfur (S15 / ULSD) | **ASTM D5453** (UV-fluorescence) / **D2622** (WD-XRF) | 15 ppm (mass) max | 15 ppm (mass) max |
| Distillation, 90 % recovered | **ASTM D86** | 288 °C max | 282–338 °C |
| Kinematic viscosity at 40 °C | **ASTM D445** | 1.3–2.4 cSt | 1.9–4.1 cSt |
| Cetane number | **ASTM D613** | 40 min | 40 min |
| Carbon residue, on 10 % distillation residue | **ASTM D524** (Ramsbottom) | 0.15 mass% max | 0.35 mass% max |
| Ash | ASTM D482 | 0.01 mass% max | 0.01 mass% max |
| Copper-strip corrosion, 3 h @ 50 °C | ASTM D130 | No. 3 max | No. 3 max |
| Lubricity, HFRR wear scar @ 60 °C | ASTM D6079 / D7688 | 520 µm max | 520 µm max |

**Key engineering notes on the limits.**

- **Flash point** is the lowest temperature at which fuel vapor will ignite under the prescribed test conditions; D975's 38 °C / 52 °C minima are **safety-driven**, not performance-driven, and align with U.S. and international fuel-handling fire codes for distillate fuels.
- **Cloud point** is reported (not capped numerically by D975 itself) because the acceptable cloud point is **regional and seasonal** — D975 Appendix X3 provides a tenth-percentile minimum-ambient-temperature map for the U.S. that buyers and sellers use to specify season-and-location-appropriate cloud-point limits at point of sale.
- **Sulfur — the dominant compliance lever post-2006.** The S15 tier (15 ppm max) is what U.S. on-road consumers actually receive; meeting it requires hydrodesulfurization at the refinery and segregated storage and distribution to prevent cross-contamination from higher-sulfur stocks. Sulfur quantitation is performed routinely by **D5453 (UV-fluorescence)** as the umpire method and **D2622 (WD-XRF)** or **D4294 (ED-XRF)** for in-line and field measurement; all three are cross-correlated.
- **Distillation 90 % recovered** is the temperature at which 90 vol% of the fuel has distilled per **D86**. The 282–338 °C window for No. 2-D is what defines "middle distillate" — narrower than gasoline (D86 90 % ~165–180 °C) and well below heavy fuel oil. Both ends of the range matter: the lower bound prevents excessive light-end content (flash, vapor-lock); the upper bound prevents heavy-end carry-over that drives carbon residue, particulates, and injector deposits.
- **Kinematic viscosity** governs **fuel-injection-system behavior** — too low and the high-pressure pump loses lubrication and metering precision; too high and atomization degrades, fuel-air mixing suffers, and emissions rise. The 1.9–4.1 cSt window for No. 2-D is the design space for which modern common-rail and unit-injector systems are calibrated.
- **Cetane number** (D613) is the **ignition-delay quality** of the fuel under standardized engine-test conditions — higher cetane shortens ignition delay and improves cold-start, idle smoothness, and combustion noise. D975's 40-min floor for both No. 1-D and No. 2-D is a **legacy floor**; OEM engine specifications and many state regulations (notably California) require **cetane ≥ 50** in practice. The cetane index (D976 / D4737) is a calculated proxy from density and distillation that buyers use as a fast-look quality check, but the cetane *number* (D613, engine test) is the umpire.
- **Carbon residue** on the 10 % distillation bottoms (Ramsbottom, D524) caps the **deposit-forming heavy-end content** of the fuel. The No. 2-D limit (0.35 mass% max) is looser than No. 1-D (0.15 mass% max) because No. 2-D has a heavier boiling-range tail by design.
- **Lubricity (HFRR wear scar, 520 µm max)** was added to D975 in the 2005–2007 ULSD-rollout window. **Hydrodesulfurization to 15 ppm S strips the natural sulfur- and nitrogen-containing lubricity components from diesel**, so post-ULSD fuels require additised lubricity restorers to protect rotating-component fuel-system parts (high-pressure pumps, injectors). The 520 µm HFRR wear scar limit is the industry's empirical floor for protecting common-rail equipment.

## Cross-references

D975 sits at the convergence of the ASTM **D02 committee** (petroleum products and lubricants) and downstream U.S. regulation (EPA 40 CFR Part 80), engine-OEM material specifications, and parallel international diesel specs. Its upstream and downstream relationships:

**Upstream test-method standards (D975 defers to these for the underlying procedure)**

- **ASTM D86** — Distillation of petroleum products at atmospheric pressure. The procedural anchor for the 90 % recovered point and for the full distillation curve reported on every D975 fuel certificate.
- **ASTM D445** — Kinematic viscosity of transparent and opaque liquids. Procedural anchor for the 40 °C kinematic viscosity limit.
- **ASTM D93** — Flash point by Pensky-Martens closed-cup. Procedural anchor for the flash-point minimum.
- **ASTM D613** — Cetane number of diesel fuel oil (engine test). Procedural anchor for the cetane minimum; companion calculated proxy is **ASTM D976 / D4737** (cetane index from density and distillation).
- **ASTM D2622** — Sulfur in petroleum products by WD-XRF. One of two umpire methods for the S15/S500/S5000 sulfur limits.
- **ASTM D5453** — Sulfur in light hydrocarbons by UV-fluorescence. Companion umpire method for the sulfur limits, particularly favored at the 15 ppm ULSD level.
- **ASTM D4294** — Sulfur in petroleum products by ED-XRF. Field-portable companion to D2622 / D5453 used for in-line and load-port verification.
- **ASTM D524** — Ramsbottom carbon residue. Procedural anchor for the carbon-residue cap on the 10 % distillation residue.
- **ASTM D2709** — Water and sediment in middle-distillate fuels. Procedural anchor for the BS&W 0.05 vol% cap.
- **ASTM D2500 / D5773** — Cloud point (visual / automatic). Procedural anchor for cloud-point reporting.
- **ASTM D6079 / D7688** — Lubricity by High-Frequency Reciprocating Rig (HFRR). Procedural anchor for the 520 µm wear-scar lubricity limit.

**Adjacent fuel specifications (companion specs in the U.S. / international fuel-spec lattice)**

- **ASTM D6751** — Standard Specification for Biodiesel Fuel Blend Stock (B100) for Middle Distillate Fuels. Defines neat biodiesel quality; the up-to-5 vol% biodiesel allowance in D975 must comply with D6751 before blending.
- **ASTM D7467** — Standard Specification for Diesel Fuel Oil, Biodiesel Blend (B6 to B20). Covers blends with biodiesel content above the 5 % D975 unlabeled allowance and up to 20 %.
- **ASTM D396** — Standard Specification for Fuel Oils. Covers heating fuel oils (No. 1, 2, 4, 5, 6); some grades overlap chemically with D975 grades but differ in spec limits and intended service.
- **ASTM D1655** — Standard Specification for Aviation Turbine Fuels. Companion spec for jet fuel (Jet A / Jet A-1); explicitly out of D975 scope.
- **ASTM D4814** — Standard Specification for Automotive Spark-Ignition Engine Fuel (gasoline). Companion spec for spark-ignition engines.
- **EN 590** — European Committee for Standardization (CEN) European diesel-fuel specification. The **EU-side parallel to D975**; broadly similar in property set but tighter on cetane (51 min vs. 40 min) and density, with different cold-flow grading (CFPP-based seasonal grades vs. D975's cloud-point reporting). Cross-Atlantic fuel trade routinely requires dual-spec attestation.
- **ISO 8217** — Petroleum products — fuels (class F) — specifications of marine fuels. Marine bunker spec; D975 grades intersect ISO 8217's distillate marine grades (DMA, DMB, DMZ) but the marine spec adds cat-fines, hydrogen-sulfide, and stability limits absent from D975.

**Downstream regulations and engine-OEM specs (call D975 by reference)**

- **EPA 40 CFR Part 80, Subpart I** — U.S. on-highway and non-road diesel sulfur regulation. Mandates the S15 (ULSD) tier of D975 for on-road since 2006 and non-road since 2010.
- **California Code of Regulations Title 13** — California-specific diesel-fuel additional requirements (lower aromatics, higher cetane).
- **OEM engine-manufacturer fuel specifications** — Cummins, Caterpillar, Detroit Diesel, and others publish engine-specific fuel specs that use D975 as the base spec and overlay tighter limits (typically cetane ≥ 50, sulfur ≤ 15 ppm regardless of regulatory tier, stricter cold-flow).

**Wiki cross-links**

- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest and bucket-purity audit; D975 is identified there as the **#4 promotion candidate** by O&G-engineering frequency-of-citation (after D86, D396, D445).
- [ASTM A370](astm-a370.md) — sibling first-class standards page in this wiki; demonstrates the same `wiki/standards/<code-id>.md` schema and frontmatter contract that this page satisfies.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution at calc time.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; 10,361 documents at `/mnt/ace/O&G-Standards/ASTM/D-Series/`. The source page identifies D975 as one of the top-edition codes (9 dated filename hits) and ranks it as the **#4 promotion candidate** to a per-code `wiki/standards/<code-id>.md` page after D86, D396, and D445.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND filename matches /\bD[\s_]?975\b/i` returns the 10 entries enumerated under *Edition history* (9 dated `D_975_-_YY_…pdf` hits across 6 distinct years 1998 / 2000 / 2001 / 2002 / 2003 / 2004, plus 1 root-level `D975.PDF`).
- **Vendor PDFs (link-only; do NOT copy into git).** Latest dated edition in catalog: `/mnt/ace/O&G-Standards/ASTM/D-Series/D_975_-_04_RDK3NS0WNA_.pdf` and reprint variants. Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — D975 product page (search "D975" at <https://www.astm.org>); current published edition is newer than the 2004 copy in the local catalog.
- **Regulatory anchor.** U.S. EPA 40 CFR Part 80, Subpart I (on-highway and non-road diesel sulfur) and California Code of Regulations Title 13 (state-additional diesel-fuel requirements).
