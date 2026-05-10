---
title: "API Std 1104 — Welding of Pipelines and Related Facilities"
slug: api-std-1104
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: api-std-1104
publisher: API
revision: "20e-2005-with-errata-2001-and-19e-1999"
tags:
  - api
  - welding
  - pipelines
  - ndt
  - weld-acceptance
sources:
  - /mnt/ace/O&G-Standards/API/Standards/API_STD_1104_20th_Ed._(2005)_Welding_of_Pipelines_and_Related_Facilities.pdf
  - /mnt/ace/O&G-Standards/API/Standards/API_STD_1104_19th_Ed._(1999)_Welding_of_Pipeline_and_Related_Facilities_ERRATA_1.pdf
  - /mnt/ace/O&G-Standards/API/Standards/API_1104_(2005)_Welding_of_Pipelines_&_Related_Facil.pdf
  - /mnt/ace/O&G-Standards/API/Standards/API_1104_Welding_of_Pipelines_1999.pdf
  - /mnt/ace/O&G-Standards/API/api-_1104_errata_2001.pdf
  - /mnt/ace/O&G-Standards/API/api.1104.1999.pdf
  - /mnt/ace/O&G-Standards/API/[Welding]_Welding_Of_Pipelines_And_Related_Facilities_-_Api_Standard_1104_(Ebook,_86_Pages).pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API Std 1104 — Welding of Pipelines and Related Facilities

> **L0 prose (citation-contract anchors):** code_id = `api-std-1104`; publisher = `API`; revision = `20e-2005-with-errata-2001-and-19e-1999`. The wiki indexes editions present in the local library; consumers must pin a specific edition in their `Citation` revision string.

## Scope

API Std 1104 is the canonical North American standard for the **arc and oxyacetylene welding of carbon and low-alloy steel piping** used in compression, pumping, and transmission of crude petroleum, petroleum products, fuel gases, carbon dioxide, and nitrogen, and where applicable distribution systems. It governs:

- **Welding procedure specifications** (WPS) and procedure qualification records (PQR) for shop and field welds.
- **Welder qualification** — performance qualification by destructive (mechanical) and bend testing on test coupons.
- **Production weld acceptance** under either workmanship (Section 9) or alternative (Annex / Appendix A) acceptance criteria, applied to single- and double-jointed girth welds, fillet welds, and tie-ins.
- **Non-destructive examination (NDE)** of welds — radiographic (RT), ultrasonic (UT), magnetic particle (MT), liquid penetrant (PT), and visual.
- **Repair welding** of weld defects in new construction and tie-ins, including limits on repair attempts and requalification of repair procedures.
- **In-service welding** for hot-tap and repair-sleeve welds onto pressurized pipelines (Appendix B), covering procedure qualification accounting for accelerated cooling and hydrogen-cracking risk.

The standard is publisher-agnostic to construction code (ASME B31.4, B31.8), and is invoked normatively by 49 CFR 192/195, CSA Z662 (for cross-border consistency), DNV-OS-F101 (Section 12 references) and most pipeline EPC general specifications.

## Edition history

Editions present in the local catalog (`/mnt/ace/O&G-Standards/_catalog.json`, parent_root `/mnt/ace/O&G-Standards/API`):

| Edition | Year | Catalog filename | Notes |
|---------|------|------------------|-------|
| 19th ed | 1999 | `API_1104_Welding_of_Pipelines_1999.pdf` (id 27383); `api.1104.1999.pdf` (id 321) | Base 19th edition; introduced consolidated Appendix A (alternative acceptance / ECA) treatment. |
| 19th ed Errata 1 | 2001 | `API_STD_1104_19th_Ed._(1999)_Welding_of_Pipeline_and_Related_Facilities_ERRATA_1.pdf` (id 27479); `api-_1104_errata_2001.pdf` (id 27336) | Errata published 2001 against the 19th edition. |
| 20th ed | 2005 | `API_STD_1104_20th_Ed._(2005)_Welding_of_Pipelines_and_Related_Facilities.pdf` (id 27478); `API_1104_(2005)_Welding_of_Pipelines_&_Related_Facil.pdf` (id 27348) | 20th edition; expanded Appendix B (in-service welding), updated UT/AUT acceptance language. |
| Excerpt / 86-page ebook | undated | `[Welding]_Welding_Of_Pipelines_And_Related_Facilities_-_Api_Standard_1104_(Ebook,_86_Pages).pdf` (id 379) | Extract; not a primary edition reference. |

> The publisher-current edition (21st ed and later, plus reaffirmation/addenda) is **not** in the local catalog. Consumers needing the latest revision must obtain it from the API store and update this page's `revision` field accordingly. Filename year is more reliable than `modified_date` (per the API source-page verification note).

## Key sections

The section numbering below tracks the 20th-edition structure (1999 19th edition is structurally similar with renumbered annexes); pin the edition in any downstream `Citation` you emit.

- **Welding procedure qualification (Section 5).** Essential variables (base material, filler classification, joint design, position, electrical characteristics, preheat/interpass, post-weld heat treatment) define the WPS envelope. PQR is established by destructive testing of a qualification coupon with mechanical-test specimen acceptance per Section 5.6.
- **Welder qualification (Section 6).** Performance qualification by destructive testing — tensile, nick-break, root-bend, face-bend, and side-bend specimens removed from a test weld. Bend-test acceptance: no crack or other open defect exceeding **1/8 in (3.2 mm)** in any direction may be present in the weld metal or between weld and fusion zone after bending; certain edge cracks of limited length are excepted. Renewal of qualification is on a periodic schedule plus on change of essential variable.
- **NDE methods and acceptance (Section 9 — workmanship; Section 11 — radiography & UT operations).** Radiographic (RT) interpretation against discontinuity-class limits (porosity, slag inclusions, incomplete penetration, incomplete fusion, cracks, undercut, burn-through). Ultrasonic testing (UT) — both manual pulse-echo and Automated UT (AUT) for mechanized welds — with separate acceptance windows. MT and PT cover surface and near-surface flaws; visual is universal. Section 9 prescribes **workmanship-based** acceptance limits keyed to flaw type, length, and aggregated length per weld length.
- **Alternative acceptance criteria — Engineering Critical Assessment (Appendix A).** Permits flaw acceptance by **fitness-for-purpose / fracture-mechanics** assessment instead of workmanship limits, when justified by toughness testing (CTOD), stress analysis, and material-property characterisation. Appendix A is the recognised North American hook into ECA methods detailed in **BS 7910** (UK) and conceptually aligned with **API 579-1 / ASME FFS-1** for in-service flaws. Required inputs: applied stress (axial + bending + residual), CTOD or J-integral toughness at the lowest service temperature, and a flaw-sizing tolerance from the chosen NDE method (typically AUT). Use is conditional on operator/owner acceptance and on the WPS having been qualified to produce welds with toughness compatible with the assessment.
- **Repair welds (Section 10).** Acceptable repair limits, removal of defective metal, requalification of the repair procedure, and a cap on repeated repair attempts at the same location.
- **In-service welding (Appendix B).** Procedure qualification for welding onto pipe in service — accounts for accelerated heat extraction by flowing product, with hydrogen-cracking control via low-hydrogen consumables, controlled heat input, and bead-temper sequencing. Companion to **API RP 2201** (procedures for hot-tapping equipment in service). Critical inputs: pipe wall thickness, carbon equivalent, flow rate, and product.
- **Mechanical testing of weld coupons (Sections 5/6 + Annex).** Tensile, nick-break, and bend specimens; mechanical testing is performed per **ASTM A370** procedures with specimen geometry called out in API 1104.

## Cross-references

External standards linked normatively or by common practice:

- **API Spec 5L** — Specification for Line Pipe. Defines base-material chemistry, mechanical properties (PSL 1 / PSL 2), and supplementary requirements that constrain API 1104 procedure qualification (CE limits, toughness). See [api-spec-5l](api-spec-5l.md).
- **API Spec 5LX / 5LD** — historical line-pipe specs (5LX folded into 5L); 5LD covers **CRA-clad and CRA-lined line pipe**, where API 1104 is supplemented by clad-specific welding qualification requirements.
- **ASME BPVC Section IX** — Welding, Brazing and Fusing Qualifications. The companion code for pressure-vessel and process-piping welding; many shop welds on pipeline-adjacent facilities (compressor stations, pump stations) qualify to BPVC-IX while line-pipe girth welds qualify to API 1104. Operators commonly maintain dual-qualification matrices.
- **ASTM A370** — Standard Test Methods and Definitions for Mechanical Testing of Steel Products. Governs tensile, bend, and notch-toughness specimen prep and testing referenced from API 1104 mechanical-test acceptance.
- **AWS D1.1** — Structural Welding Code — Steel. Governs structural attachments (supports, anchors, riser clamps) on or near a pipeline; API 1104 governs the pressure-containing girth weld and AWS D1.1 governs the structural weld at the same facility.
- **BS 7910** — Guide on methods for assessing the acceptability of flaws in metallic structures. The detailed ECA methodology referenced from Appendix A alternative acceptance criteria.
- **API 579-1 / ASME FFS-1** — Fitness-For-Service. The in-service counterpart to Appendix A — used when a flaw is detected post-construction, or when re-rating is required. Catalog editions: 2007, 2016 (per [og-standards-api](../sources/og-standards-api.md)). Conceptually overlapping with Appendix A but applied at a different lifecycle stage.
- **API RP 2201** — Procedures for Welding or Hot Tapping on Equipment in Service. Operational companion to API 1104 Appendix B.
- **ASME B31.4 / B31.8** — Pipeline Transportation Systems for Liquids and Slurries / Gas Transmission and Distribution Piping Systems. The construction codes that invoke API 1104 normatively for welding and NDE.
- **49 CFR 192 / 195** — US PHMSA pipeline safety regulations. Cite API 1104 directly as the qualification basis for personnel and procedures on jurisdictional pipelines.

Internal cross-links in this wiki:

- [api-spec-5l](api-spec-5l.md) — companion line-pipe material specification (planned/present per source-page).
- [api-rp-1111](api-rp-1111.md) — limit-state design of offshore hydrocarbon pipelines (uses API 1104 weld qualification by reference).
- [api-rp-14e](api-rp-14e.md) — production-piping sizing (planned); shares the 49-CFR-195 jurisdictional surface.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — standards-derived constants from API 1104 (e.g., the 1/8 in / 3.2 mm bend-test crack limit) require a `Citation` instance pinning `code_id=api-std-1104` and the specific `revision`.

## Sources

- Source-page summary: [O&G Standards catalog — API](../sources/og-standards-api.md). API 1104 is listed in the topical-coverage map at row "Std 1104 — Welding of Pipelines and Related Facilities — 1999, 2001, 2005, 19th ed, 20th ed".
- Catalog: `/mnt/ace/O&G-Standards/_catalog.json` (filtered: `organization=API`, `filename ~ /1104/i` — 8 documents).
- Publisher catalog: <https://www.api.org/products-and-services/standards>.

> **Vendor-PDF firewall.** Per spinout 2026-05-05 governance and `wikis/engineering-standards/CLAUDE.md` raw-policy, the underlying PDFs are **not** copied into this repo. The catalog file paths above are private-mount references only; consumers must obtain a licensed copy from API to read clause text. This wiki page records publisher facts (titles, edition years, document IDs, file paths, structural section pointers) — **no clause text, no equations, no figures** are reproduced here.
