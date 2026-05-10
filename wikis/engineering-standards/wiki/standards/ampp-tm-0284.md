---
title: "AMPP TM21284 (NACE TM-0284) — HIC Test for Pipeline & Pressure Vessel Steels"
slug: ampp-tm-0284
tags: ["ampp", "nace", "hic", "hydrogen-induced-cracking", "sour-service", "c-steel", "standards", "test-method", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: ampp-tm-0284
legacy_code_id: nace-tm-0284
publisher: AMPP (formerly NACE International)
legacy_publisher: "NACE International"
revision: not-on-disk
revision_source: "n/a — TM-0284 is a catalog gap on /mnt/ace/O&G-Standards/ as of 2026-05-09"
verified_on: 2026-05-09
public_url: https://store.ampp.org/
sources: []
extraction_policy: metadata-only
raw_copy_allowed: false
nace_doc_number: "TM 0284"
ampp_doc_number: "TM21284"
---

# AMPP TM21284 (NACE TM-0284) — HIC Test for Pipeline & Pressure Vessel Steels

## Scope

Laboratory test method for evaluating carbon and low-alloy steel plates, pipe, forgings, and tubular product forms for resistance to **hydrogen-induced cracking (HIC)** under wet H2S sour-service exposure. The method is stress-independent: unstressed coupons are immersed in an H2S-saturated aqueous test solution for a fixed exposure period, after which metallographic sectioning and crack measurement yield three quantitative ratios that characterize HIC susceptibility:

- **CLR (Crack Length Ratio)** — sum of crack lengths divided by section width, expressed as a percent.
- **CTR (Crack Thickness Ratio)** — sum of crack thicknesses divided by specimen thickness, expressed as a percent.
- **CSR (Crack Sensitivity Ratio)** — sum of (crack length × crack thickness) divided by (section width × specimen thickness), expressed as a percent.

These three ratios are computed per inspected section, averaged per specimen, and averaged per heat. TM-0284 prescribes the procedure but does **not** set acceptance limits; acceptance criteria are imposed by the application standard or the purchaser-supplier contract (see [Acceptance criteria](#acceptance-criteria)).

The method is the test-procedure companion to [ampp-tm-0177](ampp-tm-0177.md) (sulfide stress cracking) within the AMPP/NACE sour-service qualification family, and is the qualification basis cited by [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) / [iso-15156](iso-15156.md)-2 for HIC-resistant carbon and low-alloy steels.

## Edition history

TM-0284 has been revised multiple times since first publication in 1984. Editions known to exist (publisher record, not on-disk):

| Edition | Year | Publisher | Notes |
|---------|------|-----------|-------|
| 1984 | 1984 | NACE | Original publication establishing CLR/CTR/CSR framework. |
| 1996 | 1996 | NACE | Solution-A / Solution-B clarifications. |
| 2003 | 2003 | NACE | Updated specimen-preparation and metallographic-evaluation guidance. |
| 2011 | 2011 | NACE | Editorial revision; alignment with MR0175 / ISO 15156 referencing language. |
| 2016 | 2016 | NACE | Most recent NACE-branded edition prior to AMPP rebrand. |
| TM21284 | post-2021 | AMPP | Document number renumbered to AMPP TM21284 after the 2021 NACE-to-AMPP merger; technical content preserved by AMPP under document-number continuity policy (publisher portal `https://store.ampp.org/`). |

**On-disk status:** TM-0284 is a catalog gap. A scan of `/mnt/ace/O&G-Standards/_catalog.json` and a filename heuristic across the `NACE/`, `Unknown/`, and full tree (filename pattern `*0284*`, `*tm0284*`, `*tm-0284*`, `*tm21284*`, `*hic*`) on 2026-05-09 returned no match; the only `*0284*` filename hits are unrelated photo files in the ISO Jack-Up subtree. The on-disk NACE coverage at `/mnt/ace/O&G-Standards/NACE/` is limited to MR 0175, TM 0177-96, and four conference papers. Until a TM-0284 edition is added to the catalog, downstream calc citations referencing this code must wait for `revision_source` to be populated. The `legacy_code_id` field bridges the 2021 NACE-to-AMPP rebrand so calc sites still using the legacy `nace-tm-0284` spelling resolve to this canonical page.

## Test specifics

The procedural detail below is the standardized test outline at the level needed for downstream consumers to understand citations; the operative numbers (solution recipes, dimensional tolerances, sectioning offsets) must be read from the source PDF and are not reproduced here.

**Specimen sampling.** Three specimens per heat are extracted from the rolling direction of the parent product, oriented transverse to the rolling direction (the maximum-elongation orientation for MnS-inclusion-driven HIC nucleation), at the **mid-thickness** location of the plate or pipe wall (where solidification segregation bands concentrate hydrogen-trap sites). Coupon dimensions and surface-finish requirements are specified in the standard.

**Test solutions.** Two standardized aqueous environments are defined:
- **Solution A** — synthetic seawater proxy: ~5% NaCl + ~0.5% acetic acid, H2S-saturated at room temperature and ambient pressure. The historical "standard severity" environment.
- **Solution B** — synthetic seawater proxy referenced to natural seawater chemistry, H2S-saturated. Generally regarded as a less-aggressive comparator to Solution A for some product forms; used when application-specific.

The exact recipes, pH targets, gas-saturation procedure, and test-vessel sizing rules are normative content of the standard and are not reproduced here.

**Exposure.** Coupons are immersed for **96 hours** at room temperature and ambient pressure with continuous H2S sparging maintained throughout the test.

**Post-test evaluation.** Each specimen is sectioned at three positions along its length — at **1/4, 1/2, and 3/4** of the gauge length — yielding three metallographic sections per specimen and nine sections per heat (3 specimens × 3 sections). Each section is polished and examined under metallographic magnification; the lengths and through-thickness extents of all detected cracks are measured.

**Calculation.** Per the formulas referenced in [Scope](#scope), CLR, CTR, and CSR are computed for each section, averaged across the three sections of a specimen to yield per-specimen ratios, and averaged across the three specimens to yield per-heat ratios. The per-heat ratios are the values typically reported on a Material Test Report (MTR) and matched against contractual acceptance criteria.

## Acceptance criteria

**TM-0284 itself does not impose acceptance limits.** It defines only the procedure for generating CLR/CTR/CSR. Acceptance thresholds are imposed by the **specifying body** — typically the application standard, the purchaser specification, or the EPC contract.

**Common contractual limits** seen in sour-service pipeline and pressure-vessel procurement (per-heat averages):

| Ratio | Typical limit | Use |
|-------|---------------|-----|
| CLR | ≤ 15% | Maximum allowable crack length per section. |
| CTR | ≤ 5% | Maximum allowable through-thickness crack extent. |
| CSR | ≤ 2% | Combined length × thickness sensitivity. |

These thresholds are illustrative and must be verified against the project specification — some severe-sour applications tighten CLR to ≤ 10% or CSR to ≤ 1%, and some less-severe applications relax them. The point of contractual specification is normative; this page is not.

**Application-standard pointers.**
- [iso-15156](iso-15156.md) / NACE MR0175-2 (carbon and low-alloy steels) cites TM-0284 as the qualification test method for HIC-resistance demonstration. Acceptance thresholds in MR0175-2 are read directly from the source.
- [api-spec-5l](api-spec-5l.md) (line pipe) Annex H prescribes sour-service line-pipe testing including HIC qualification per TM-0284, with acceptance values defined in Annex H tables.
- DNV-OS-F101 (submarine pipeline systems, sour-service supplementary requirements) references TM-0284 as the HIC-resistance qualification test.
- API 5LD (CRA-clad and CRA-lined pipe) references TM-0284 for the carbon-steel backing layer where applicable.

## Cross-references

- [ampp-tm-0177](ampp-tm-0177.md) — Sulfide stress cracking (SSC) test method (uniaxial tension, bent-beam, C-ring, DCB). The complementary stressed-specimen test in the same sour-service qualification family.
- [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md) — General principles for selection of cracking-resistant materials in H2S-containing environments (Part 1 fitness-assessment caller).
- [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) — Cracking-resistant carbon and low-alloy steels and the use of cast irons (the primary application standard consuming TM-0284 outputs for C-steel sour-service qualification).
- [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) — Cracking-resistant CRAs and other alloys (less-frequent TM-0284 caller; CRA HIC concerns are typically handled by other tests).
- [iso-15156](iso-15156.md) — ISO-published harmonized version of MR 0175; TM-0284 is referenced identically.
- [api-spec-5l](api-spec-5l.md) — Line pipe specification; sour-service Annex H sets HIC acceptance limits referencing TM-0284.
- DNV-OS-F101 — Submarine pipeline systems; sour-service supplementary requirements reference TM-0284 (no standards page yet in this wiki).
- API 5LD — CRA-clad / CRA-lined pipe specification; references TM-0284 for the carbon-steel backing where sour service applies (no standards page yet in this wiki).
- [Concept: sour-service-materials](../concepts/sour-service-materials.md) — HIC chapter that consumes this page as a normative test-method reference.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Sources

- [O&G Standards catalog — minor publishers](../sources/og-standards-minor-publishers.md) — TM-0284 is a recognized gap in the on-disk NACE coverage; this source page records the scan-and-not-found outcome of the 2026-05-09 catalog filter (`0284`, `tm-0284`, `tm21284`, `hic` filename heuristics).
- [O&G Standards catalog — ISO](../sources/og-standards-iso.md) — for the ISO 15156 application standard that consumes TM-0284 outputs.
- Publisher portal (current edition): `https://store.ampp.org/` — registration required for purchase. No raw text or numeric thresholds copied from the publisher source into this repository per the spinout vendor-PDF firewall.
