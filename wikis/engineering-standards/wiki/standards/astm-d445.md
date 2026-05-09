---
title: "ASTM D445 — Kinematic Viscosity of Transparent and Opaque Liquids"
slug: astm-d445
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d445
publisher: ASTM
revision: latest
revision_in_catalog: "2004 (latest in /mnt/ace/O&G-Standards/_catalog.json — publisher continues to maintain D445; current published edition is newer)"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/d0445-24.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
  - /mnt/ace/O&G-Standards/ASTM/D-Series/D_445_-_04_RDQ0NQ_.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - viscosity
  - kinematic-viscosity
  - fuel-quality
  - lubricants
  - standards
---

# ASTM D445 — Standard Test Method for Kinematic Viscosity of Transparent and Opaque Liquids (and the Calculation of Dynamic Viscosity)

> **Standard identity (L0 prose).** `code_id`: astm-d445 · `publisher`: ASTM · `revision`: latest (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json` is the 2004 issue under filename `D 445 - 04  _RDQ0NQ__.pdf`; ASTM continues to maintain D445 on a roughly biennial reapproval cadence — see *Edition history* below).

## Scope

ASTM D445 specifies the **measurement of kinematic viscosity (ν)** of transparent and opaque Newtonian liquids using **calibrated glass-capillary viscometers**. It is the foundational kinematic-viscosity method on which most of the world's fuel-quality and lubricant-grading specifications hang:

- The measured quantity is **kinematic viscosity ν in mm²/s** (numerically identical to the legacy unit **centistokes, cSt**: 1 mm²/s = 1 cSt).
- The procedure measures the **time required for a fixed volume of liquid to flow under gravity** through a calibrated glass-capillary viscometer held at a tightly controlled bath temperature; ν is computed by multiplying the efflux time (in seconds) by the viscometer's calibration constant (in mm²/s²).
- Dynamic (absolute) viscosity μ in mPa·s (= cP) is **calculated downstream** as μ = ν × ρ, where ρ is the liquid density at the same test temperature (D445's title carries "and the Calculation of Dynamic Viscosity" precisely to authorise this calculation step from a single measurement).
- Coverage spans approximately **0.4 mm²/s to >100,000 mm²/s** (Newtonian regime), bracketing the full range from very-light hydrocarbons (kerosene-range fuels at 40°C) up through heavy residuals and gear oils.
- D445 prescribes **bath temperature control**, with the most-cited test temperatures being **40 °C and 100 °C** for petroleum lubricants (the two anchor points for the SAE J300 engine-oil grading lattice and the ASTM D2270 viscosity-index calculation), and **−20 °C** and other sub-ambient points for jet fuel and cold-flow specs.
- The standard distinguishes **transparent** liquids (where the meniscus is read directly through the glass) from **opaque** liquids (where the meniscus is read against a backlit timing mark or by reverse-flow viscometer geometry); this latter case extends D445 cleanly to dark crudes, residuals, and used lubricants where direct meniscus observation would fail.

D445 does **not** specify acceptance criteria — those live in the product specification (D396 fuel oils, D975 diesel, D1655 jet, D6751 biodiesel, SAE J300 engine oils, etc.). D445 specifies **how** the viscosity is measured and **what** is reported, so that any of those specs is interpretable against a single fixed measurement protocol. This makes D445 the most-cited test method in the entire D02 (Petroleum Products and Lubricants) subcommittee bucket.

## Edition history

ASTM D445 is reissued on a roughly biennial cadence with frequent year-only reapproval revisions in between. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following D445 editions (filename heuristic, true matches only):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| D 445 (undated) | `D445.PDF` | Pre-2000 issue, modified date 1999-02-25; specific edition year not encoded in filename |
| D 445 – 97 | `D 445 - 97  _RDQ0NS05NW__.pdf` | 1997 issue |
| D 445 – 01 | `D 445 - 01  _RDQ0NS0WMQ__.pdf` | 2001 issue |
| D 445 – 03 | `D 445 - 03  _RDQ0NS0WMW__.pdf` | 2003 issue |
| D 445 – 04 | `D 445 - 04  _RDQ0NQ__.pdf` | 2004 issue — **latest in catalog** |

**5 catalog files across 4 dated editions plus one undated pre-2000 issue (1997, 2001, 2003, 2004 plus D445.PDF).** The publisher's currently-active edition is newer than the catalog's 2004 copy (ASTM continues to reapprove D445 at the D02 committee); resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

D445 has been continuously maintained by ASTM Committee D02 (Petroleum Products and Lubricants), Subcommittee D02.07 on Flow Properties, since the early 1950s; the procedure has remained substantively stable across editions, with revisions principally tightening repeatability/reproducibility statements, expanding the approved-viscometer list, and clarifying opaque-liquid handling.

## Key sections

D445 is organised into a body covering the universal capillary-viscometry procedure followed by an annex enumerating the approved viscometer designs and their calibration constants. The headings below follow the long-stable structure carried across the editions present in the catalog (section numbers shift slightly across editions but the topic structure is stable):

- **Apparatus — calibrated glass capillary viscometers.** D445 approves a family of glass-capillary viscometer designs, each calibrated against certified reference materials traceable to a master viscometer. The principal designs called out by name include:
  - **Cannon-Fenske routine** (modified Ostwald, U-tube, transparent liquids) — the workhorse for light-to-medium fuels and oils.
  - **Cannon-Fenske opaque** (reverse-flow geometry) — for residual fuels, used oils, dark crudes where direct meniscus observation through the upper bulb would fail.
  - **Ubbelohde** (suspended-level, transparent) — single-bulb design with a vented sidearm that decouples efflux time from sample volume; preferred for high-precision lubricant work.
  - **BS/IP/U** (British Standards / Institute of Petroleum, U-tube) — the European-style equivalent of Cannon-Fenske.
  - **BS/IP/RF** (British Standards / Institute of Petroleum, reverse-flow) — the European-style opaque-liquid analogue.
  - **Zeitfuchs cross-arm**, **Atlantic**, **Pinkevitch**, and several other less-common geometries — also approved when calibrated to the master-viscometer lineage.

  Each viscometer carries an etched **calibration constant C in mm²/s²** assigned by the supplier and verifiable against a certified reference fluid. Viscometers must be selected so that the efflux time falls within the design's specified range (typically 200–1000 s for standard designs; minimum efflux time is set to keep kinetic-energy and surface-tension corrections negligible).

- **Bath temperature control.** D445 requires a constant-temperature bath capable of holding the test temperature to **±0.02 °C over the immersed length of the viscometer** (older editions) tightening to **±0.02 °C across the full range from −20 °C to 100 °C** (newer editions). The most-cited test temperatures are **40 °C and 100 °C** for petroleum lubricants — these are the two anchor points for the SAE J300 engine-oil grading lattice and for the D2270 viscosity-index calculation. **Sub-ambient temperatures (−20 °C and below)** apply to jet fuel (D1655) and cold-climate distillate-fuel work; **higher temperatures up to 150 °C** apply to high-temperature high-shear (HTHS) lubricant testing in companion methods.

- **Efflux-time measurement.** The sample is charged into the viscometer, equilibrated at bath temperature for the prescribed minimum hold time (typically 30 minutes for a 40 °C test, longer for sub-ambient work), then drawn up to the upper timing mark. The sample is released and the **time for the meniscus to fall between the upper and lower timing marks** is measured to the nearest 0.1 s using an electronic timer or stopwatch. **Two efflux-time determinations** are made consecutively on the same charge; if the two times agree within the standard's "determinability" criterion (a fraction of a percent), they are averaged to produce the reported time.

- **Calculation.** Kinematic viscosity is computed as **ν = C × t**, where C is the viscometer constant (mm²/s²) and t is the average efflux time (s). The result is reported in **mm²/s to four significant figures** for ν < 100 mm²/s and to a comparable relative precision at higher viscosities. **Dynamic viscosity μ in mPa·s is computed as μ = ν × ρ × 10⁻³** (when ρ is in kg/m³) or simply **μ = ν × ρ** (when ρ is in g/cm³), with the density measured at the same test temperature by D1298, D4052 (digital density meter), or an equivalent method.

- **Repeatability and reproducibility (precision statements).** D445 carries a precision-and-bias section reporting **repeatability** (within-laboratory, single operator, same equipment, replicate determinations on the same sample) and **reproducibility** (between-laboratory) for the principal product classes — base oils, formulated lubricants, distillate fuels, residual fuels, biodiesel. The numeric r and R values vary by product class and viscosity range; modern editions express these as fractions of the result (e.g., r = 0.0013 × ν for base oils at 40 °C) so that absolute tolerance scales with viscosity.

- **Viscosity range coverage.** The combined approved-viscometer set covers the kinematic-viscosity range from approximately **0.4 mm²/s** (at the lower bound, where capillary-viscometer kinetic-energy corrections become significant) to **>100,000 mm²/s** (at the upper bound, where extended efflux times exceed 1000 s and a larger-bore viscometer must be selected). The standard emphasises that **non-Newtonian liquids fall outside the scope** — D445 measures kinematic viscosity at a single shear rate (set by the capillary geometry and the sample density), and shear-thinning or shear-thickening fluids must be characterised by other methods (D2983 cold-cranking simulator, D4683 HTHS tapered-bearing, D7042 Stabinger oscillating-piston).

## Related calculations

A small family of companion calculation methods is anchored to D445's measured ν:

- **ASTM D2270 — Viscosity Index (VI).** Computes the dimensionless viscosity index from **ν at 40 °C and ν at 100 °C** (both measured per D445). VI is the principal lubricant-quality figure of merit indicating how the kinematic viscosity changes with temperature; higher VI = flatter ν–T curve. SAE J300 engine-oil grades implicitly require VI through their dual-temperature ν envelopes, and base-oil group classifications (API Group I/II/III/IV/V) are defined in terms of VI thresholds.
- **ASTM D2161 — Conversion of kinematic viscosity to Saybolt Universal Viscosity (SUV) and Saybolt Furol Viscosity (SFV).** Provides the conversion table from mm²/s to seconds-Saybolt, allowing legacy-spec compliance for product specifications still written in Saybolt units. D2161 is a calculation/lookup method only; the underlying measurement is always D445.
- **Dynamic viscosity μ = ν × ρ.** D445 explicitly authorises calculation of dynamic viscosity from the measured kinematic viscosity and an independently-measured density at the same temperature. Density is sourced from D1298 (hydrometer) or D4052 (digital density meter); the same temperature-control bath used for D445 commonly also services the D4052 instrument.

## Application

D445-measured kinematic viscosity is the **viscosity-of-record** for nearly every petroleum-products specification in the U.S. and (via ISO 3104) internationally. Specifications that cite D445 directly:

- **ASTM D396 — Standard Specification for Fuel Oils.** Grades No. 1 through No. 6 fuel oil are differentiated by viscosity envelopes at 40 °C and 100 °C measured per D445. The heavier grades (No. 4–No. 6) use 100 °C as the principal grading point because their 40 °C viscosities exceed the practical Cannon-Fenske range.
- **ASTM D975 — Standard Specification for Diesel Fuel Oils.** Specifies kinematic viscosity at 40 °C per D445: Grade No. 1-D Sxx ranges 1.3 to 2.4 mm²/s, **Grade No. 2-D Sxx ranges 1.9 to 4.1 mm²/s**, Grade No. 4-D ranges 5.5 to 24.0 mm²/s. The 1.9–4.1 mm²/s window for No. 2-D is the single most-cited viscosity range in U.S. diesel custody-transfer.
- **ASTM D1655 — Standard Specification for Aviation Turbine Fuels (Jet A / Jet A-1).** Specifies a **maximum kinematic viscosity at −20 °C** measured per D445 (8.0 mm²/s for Jet A and Jet A-1 in current editions). The sub-ambient test point is critical for high-altitude cold-soak fuel-system performance.
- **ASTM D6751 — Standard Specification for Biodiesel Fuel Blend Stock (B100).** Specifies kinematic viscosity at 40 °C per D445 in the range 1.9 to 6.0 mm²/s. Biodiesel viscosity is typically higher than petroleum diesel, and the upper bound is set to maintain injector-spray atomisation behaviour comparable to petroleum diesel.
- **SAE J300 — Engine Oil Viscosity Classification.** The dual-temperature SAE-grade lattice (e.g., 5W-30, 10W-40, 15W-50, 0W-20) is built on **D445 measurements at 100 °C** for the high-temperature side and a constellation of low-temperature methods (D2602, D5293) for the W-grade side. Every multi-grade engine oil sold in the U.S. carries a J300 grade traceable through D445.
- **ISO 3104 — Petroleum products — Transparent and opaque liquids — Determination of kinematic viscosity and calculation of dynamic viscosity.** The international parallel to D445; the two standards are technically equivalent within their stated precision and are commonly cross-cited in dual-jurisdiction product specifications. ISO 3104 is the citation of choice in EN-590 (European diesel), EN-228 (European gasoline), MARPOL Annex VI bunker quality, and IMO Sulphur 2020 fuel-handling.

D445 is also the upstream measurement for **API MPMS Chapter 11.4.1** (viscosity correlations and corrections for custody-transfer applications), for **lubricant base-oil group classifications** (API 1509 base-oil interchange), and for nearly every refinery's product-quality dashboard.

## Cross-references

D445 sits at the convergence of the ASTM **D02 committee** (Petroleum Products and Lubricants) and the international ISO TC 28 (Petroleum products and related products of synthetic or biological origin). Its upstream and downstream relationships:

**Companion calculation and conversion methods**
- **ASTM D2161** — Conversion of kinematic viscosity to Saybolt Universal/Saybolt Furol viscosity. Pure calculation/lookup method anchored to D445's measured ν.
- **ASTM D2270** — Calculating viscosity index from kinematic viscosity at 40 °C and 100 °C. Both ν values are D445 measurements.

**Alternative viscosity measurement methods (cross-cited)**
- **ASTM D7042** — Dynamic viscosity and density of liquids by Stabinger viscometer (and the calculation of kinematic viscosity). Oscillating-piston / U-tube-density alternative that measures dynamic viscosity and density simultaneously, then back-calculates kinematic viscosity. Modern D7042 results are routinely cross-checked against D445 and are accepted as alternates in many product specs (with explicit cross-method bias statements).
- **ASTM D2983** — Apparent viscosity at low temperatures by Brookfield viscometer. Used for non-Newtonian gear oils and ATFs at sub-ambient temperatures where D445's Newtonian assumption breaks down.
- **ASTM D4683 / D5481** — High-temperature high-shear (HTHS) viscosity at 150 °C and 1 MPa shear stress. Captures the non-Newtonian shear-thinning behaviour of polymer-thickened multigrade engine oils that D445 cannot resolve at its single (low) shear rate.
- **ISO 3104** — International parallel to D445 (technically equivalent within stated precision).

**Custody-transfer and correlation references**
- **API MPMS Chapter 11.4.1** — Viscosity-correction factors for petroleum products in custody transfer. Anchored to D445-measured ν at standard reference conditions, with temperature- and pressure-correction tables for tank-truck, pipeline, and marine-bunker measurement.

**Wiki cross-links**
- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest and bucket-purity audit; D445 listed there as **#3 promotion candidate** in the D02-petroleum block (4-edition catalog presence; pairs with D2161).
- [ASTM A370](astm-a370.md) — sibling ASTM standard on the steel-mechanical-testing side (A370 + D445 are both A/D-series test-method anchors that sit upstream of dozens of product specs).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; 10,361 documents at `/mnt/ace/O&G-Standards/ASTM/D-Series/`, of which **5 catalog files across 4 dated editions plus one undated pre-2000 issue** are D445. D445 is identified there as a **top-tier promotion candidate** (#3 in the D02-petroleum priority list) for `wiki/standards/<code-id>.md`.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND filename matches /^D[\s_]?445[^0-9]/i OR filename == 'D445.PDF'` returns the 5 entries enumerated under *Edition history*.
- **Vendor PDFs (link-only; do NOT copy into git).** Latest dated edition in catalog: `/mnt/ace/O&G-Standards/ASTM/D-Series/D_445_-_04_RDQ0NQ_.pdf` (2004 issue). Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — D445 product page (search "D445" at <https://www.astm.org>).
