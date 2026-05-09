---
title: "ASTM D396 — Fuel Oils"
slug: astm-d396
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d396
publisher: ASTM
revision: "2002 (latest in catalog); publisher-current edition is newer — see Edition history"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/d0396-21.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - fuel-oil
  - heating-oil
  - residual-fuel
  - marine-fuel
  - standards
---

# ASTM D396 — Standard Specification for Fuel Oils

> **Standard identity (L0 prose).** `code_id`: astm-d396 · `publisher`: ASTM · `revision`: 2002 (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json`; ASTM reissues D396 on a roughly annual-to-biennial cadence and the publisher-current edition is newer than the catalog's 2002 copy — see *Edition history* below).

## Scope

ASTM D396 is the **U.S. specification for fuel oils used in fuel-burning equipment** — the heating, industrial-process, and steam-generation counterpart to D975 (diesel for compression-ignition engines) and D1655 (kerosene for aviation gas turbines). It defines **six commercial grades** spanning the full distillate-to-residual continuum, distinguished by **boiling range, viscosity, and pre-burner preheat requirement**:

- **No. 1** — light distillate, low viscosity. Designed for **vaporizing-pot and atomizing burners** without preheat. Typical service: kerosene-style space heaters, vaporizing-burner domestic furnaces, and small commercial appliances where the fuel must vaporize under ambient or near-ambient conditions.
- **No. 2** — middle distillate, the **default U.S. domestic heating-oil grade**. Used in pressure-atomizing burners in residential and small-commercial furnaces and boilers. Chemically overlapping with No. 2-D diesel from D975 — the same refinery cut, with different additive packages and (historically) different sulfur and dye specifications. Also widely used as a **fishing-fleet and small-marine diesel substitute** where a D975 spec is not contractually required.
- **No. 4** (*often "No. 4 (Light)"*) — light residual blend or heavy distillate. For **industrial burners with limited preheat capability** — process heaters and small steam plants where the fuel handling system can warm the fuel to ~25–40 °C but not to the heavy-residual atomization range.
- **No. 5 (Light)** — light end of the heavy residual range. Used in **commercial-scale steam boilers** (hospital, college campus, small industrial) with **modest preheat** (~50–60 °C) for atomization.
- **No. 5 (Heavy)** — heavier residual; the dividing grade between commercial and utility-scale combustion. Used in **utility steam boilers and large industrial plants** with **steam-traced fuel-oil systems** preheating to ~70–80 °C.
- **No. 6** — the heaviest residual grade, commonly known as **bunker C** (and historically as "Navy Special" in certain naval-fueling specs). Used in **utility-scale boilers, large-marine slow-speed diesel engines (when blended down or homogenised), and process-industry heat-input applications** where the fuel system can preheat to **50–100 °C for pumping and 80–120 °C for atomization**. Without preheat, No. 6 is solid or near-solid at room temperature.

D396 cross-cuts the diesel (D975), kerosene (D3699), and aviation kerosene (D1655) specs **by application, not by chemistry**. The same refinery distillate cut may meet D396 No. 2 (heating), D975 No. 2-D (on-road diesel), and D3699 (kerosene) on physical properties while differing in sulfur, lubricity additive, dye, and certification — i.e., the spec invoked at point of sale is determined by **end use** (heating burner vs. compression-ignition engine vs. lamp fuel vs. jet engine), not by the underlying hydrocarbon chemistry. D396 is **not** a fuel-injection or compression-ignition specification — combustion in a D396-served device is **flame-front combustion in a burner**, not the spray-and-autoignition combustion of a diesel engine — so D396 omits the cetane-number and lubricity limits that define D975 and instead emphasizes **flash, pour, viscosity (cold-flow and atomization), and ash/sediment** as the property set that governs reliable burner operation.

## Edition history

ASTM D396 is reissued on a roughly annual-to-biennial cadence. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/D-Series/`:

| Edition | Catalog filename(s) | Notes |
|---------|---------------------|-------|
| D 396 – 98 | `D_396_-_98_RDM5NI05OA_.pdf` | 1998 issue |
| D 396 – 02 | `D_396_-_02_RDM5NG_.pdf`, `D_396_-_02_RDM5NI0WMG_.pdf`, `D_396_-_02_RDM5NI1SRUQ_.pdf` | 2002 issue — **latest dated edition in catalog** (three reprint/tag variants) |

**4 catalog hits across 2 distinct dated editions (1998, 2002).** The 2002 edition is the latest in the catalog. ASTM has continued maintaining D396 on roughly annual reissue and the publisher-current edition is materially newer than 2002 — most importantly, the **biodiesel-blend allowance was added to D396 in the 2008–2010 revision window** (permitting up to 5 vol% biodiesel meeting D6751 in any D396 grade, mirroring the parallel D975 amendment), and the **sulfur tiers for No. 1 and No. 2 grades were tightened in successive editions** to reflect EPA non-road and heating-oil sulfur regulations (notably the EPA non-road heating-oil 500 ppm cap effective 2014 in the U.S. Northeast). Resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key requirements

D396 sets **numeric limits per grade** on the properties below and binds each property to a designated ASTM test method. The table reproduces canonical limits across all six grades; values shown are typical published limits — **fail-closed citation resolution must hit the publisher-current edition for compliance work**, since several limits (notably sulfur and pour point) have moved across recent revisions.

| Property | Test method | No. 1 | No. 2 | No. 4 | No. 5 (Light) | No. 5 (Heavy) | No. 6 |
|----------|-------------|-------|-------|-------|---------------|---------------|-------|
| Flash point | **ASTM D93** (Pensky-Martens) | 38 °C min | 38 °C min | 55 °C min | 55 °C min | 55 °C min | 60 °C min |
| Pour point | **ASTM D97** | −18 °C max | −6 °C max | −6 °C max | report | report | report |
| Kinematic viscosity at 40 °C | **ASTM D445** | 1.3–2.1 cSt | 1.9–3.4 cSt | 5.5–24.0 cSt | 24–58 cSt (light end of residual) | report (typically >50 cSt @ 40 °C) | report (typically >200 cSt @ 40 °C) |
| Carbon residue, on 10 % distillation residue | **ASTM D524** (Ramsbottom) | 0.15 mass% max | 0.35 mass% max | report | report | report | report |
| Sulfur | **ASTM D2622** (WD-XRF) / **D5453** (UV-fluorescence) | 0.50 mass% max (or grade-spec sulfur tier) | 0.50 mass% max (or grade-spec sulfur tier) | grade-spec | grade-spec | grade-spec | grade-spec |
| Distillation, 90 % recovered | **ASTM D86** | 288 °C max | 282–338 °C | n/a (residual) | n/a (residual) | n/a (residual) | n/a (residual) |
| Water and sediment | **ASTM D2709** (distillates) / **D1796** (residual) | 0.05 vol% max | 0.05 vol% max | 0.50 vol% max | 1.00 vol% max | 1.00 vol% max | 2.00 vol% max |
| Ash | **ASTM D482** | n/a | n/a | 0.05 mass% max | 0.10 mass% max | 0.15 mass% max | report |

**Key engineering notes on the limits.**

- **Flash point** is **safety-driven**, not performance-driven, and aligns with U.S. and international fuel-storage and bunkering fire codes. The ladder from 38 °C (No. 1/No. 2 distillates) up to 60 °C (No. 6 residual) reflects the increasing heavy-end content as grade number rises — heavier residual fractions inherently have higher flash, but the spec also has to protect against light-end contamination during refinery blending, which would silently lower flash and create a fire hazard in heated storage tanks.
- **Pour point** is the property that governs **whether the fuel will flow on its own at storage temperature**. The −18 °C No. 1 limit makes No. 1 the **outdoor-storage grade** in cold climates; No. 2's −6 °C limit aligns with conditioned-basement domestic storage; No. 4 / No. 5 / No. 6 carry "report" rather than a numeric cap because heavy fuels are **assumed to require heated storage and steam-traced lines** at any practical ambient — the buyer specifies a maximum pour point against the actual storage and pipework temperature, not against a generic spec floor.
- **Viscosity** is the dominant property governing **atomization quality at the burner**. Distillate grades No. 1 and No. 2 atomize at storage temperature with no preheat (which is why their viscosity windows are narrow — 1.3–2.1 and 1.9–3.4 cSt at 40 °C). Residual grades No. 4 / No. 5 / No. 6 must be heated before atomization to bring viscosity down into the 15–50 cSt range that pressure-atomizing nozzles require — the **viscosity-vs-temperature curve** of the as-supplied fuel determines the **fuel-oil heater set-point** in the combustion equipment. A fuel-oil control system reading viscosity in real time (per **ASTM D445** or in-line viscometer) is the modern industrial best practice for residual-grade burners.
- **Carbon residue** caps **deposit-forming heavy-end content** in distillate grades. The 0.15 / 0.35 mass% limits for No. 1 / No. 2 mirror the D975 No. 1-D / No. 2-D limits exactly — the spec families recognise that a fuel with high carbon residue will coke vaporizing burner surfaces and clog atomizing nozzles. Residual grades report rather than cap because residual fuels inherently carry significant carbon-residue load (often 10–18 mass%) and the burner system must be designed for it.
- **Sulfur** has been the **moving compliance limit across D396's recent edition history**. The 0.50 mass% (5,000 ppm) cap shown above is the **historical baseline** for No. 1 and No. 2 in the 2002 catalog edition; the publisher-current edition incorporates **sulfur tiers** (notably an "ultra-low-sulfur heating oil" path mirroring the D975 ULSD provisions) to align with EPA non-road and U.S. Northeast state heating-oil sulfur regulations. Compliance work must cite the **edition-current sulfur tier**, not the historical 0.50 mass% baseline.
- **Distillation 90 % recovered** is enforced only on the distillate grades No. 1 and No. 2 — residual grades are not characterized by atmospheric-pressure distillation since they would not distil completely at D86 conditions. The 288 °C / 282–338 °C windows for No. 1 / No. 2 closely mirror D975 No. 1-D / No. 2-D — confirming that **D396 No. 2 and D975 No. 2-D draw from the same refinery middle-distillate cut**.
- **Water and sediment** caps loosen by an order of magnitude across the grade range — 0.05 vol% for distillates, up to 2.00 vol% for No. 6 — reflecting the operational reality that heavy residual fuels are stored heated and routinely carry water and sludge that must be settled and decanted, not eliminated, in normal service. The **BS&W (basic sediment and water)** measurement for residual grades uses **D1796 (centrifuge)**, distinct from the **D2709 centrifuge method** used for distillates.
- **Ash** is enforced only on residual grades, where ash is dominated by **vanadium and sodium content** from crude-source contamination. Vanadium drives high-temperature corrosion of superheater tubes in utility boilers; sodium drives slag bonding to furnace walls. The ash limits (0.05–0.15 mass%) are **upper-bound housekeeping limits** — utility purchase specs commonly tighten these substantially with vanadium and sodium element-specific limits via **ASTM D5708** (ICP-AES on residual fuels).

## Application

The grade-to-application mapping that drives D396 specification at point of sale:

| Grade | Typical use |
|-------|-------------|
| **No. 1** | Vaporizing-pot burners, kerosene-style space heaters, small commercial vaporizing-burner appliances, outdoor-stored fuel in cold climates (relies on −18 °C pour point). |
| **No. 2** | **Domestic heating-oil** (the U.S. residential and light-commercial standard); pressure-atomizing burners in residential furnaces, boilers, and water heaters; **fishing-fleet and small-marine diesel substitute** where a D975 contract spec is not required. |
| **No. 4** | Industrial process-heat burners (process heaters, small kilns, asphalt-plant heaters) with **limited preheat capability** — fuel handled in unheated or trace-heated lines, atomized after a modest in-line warmer. |
| **No. 5 (Light)** | Hospital, university, and commercial-campus steam-and-hot-water boilers; medium-size industrial plant boilers with **modest fuel preheat (~50–60 °C)** for atomization. |
| **No. 5 (Heavy)** | Utility-scale and large-industrial steam boilers with **larger preheat (~70–80 °C)**; sits at the boundary between commercial and utility fuel handling. |
| **No. 6** | **Bunker C marine fuel** for slow-speed marine diesel engines (often blended-down for engines, or homogenised at the engine room); **utility-scale and large-industrial boilers** with full steam-traced fuel systems preheating to **50–100 °C for pumping and 80–120 °C for atomization**. |

The **commercial relevance** of D396 has shifted markedly across grades over the past two decades:

- **No. 1 and No. 2** remain the **active commercial spec** for U.S. domestic heating-oil distribution (the "home heating oil" market, especially in the U.S. Northeast). Annual U.S. consumption is in the billions of gallons; D396 No. 2 is the contractual basis for that distribution.
- **No. 4 and No. 5** have **declined in U.S. commercial use** as utility steam plants and industrial boilers have converted to natural gas under price-and-emissions pressure. They retain commercial relevance in legacy utility boiler fleets and in process-industry applications without natural-gas access.
- **No. 6 / bunker C** is **largely superseded for marine bunker fuel by ISO 8217**, the international marine fuel specification that adds cat-fines, hydrogen-sulfide, oxidation-stability, and aluminium-plus-silicon limits absent from D396 No. 6. ISO 8217 grades **RMG-380** and **RMG-180** (the most-traded heavy fuel oils for shipping) **broadly correspond to D396 No. 6** by viscosity and density but are the contractual instrument used in actual marine bunker transactions. **Post-MARPOL Annex VI 2020 sulfur cap (0.50 mass% global, 0.10 mass% in ECA zones), the residual-fuel marine market has bifurcated into VLSFO (very-low-sulfur fuel oil) and HFO-with-scrubber paths** — both transacted under ISO 8217, not D396.

## Cross-references

D396 sits at the convergence of the ASTM **D02 committee** (petroleum products and lubricants), the U.S. heating-oil distribution market, and the international marine-fuel and biofuel-blend lattices.

**Upstream test-method standards (D396 defers to these for the underlying procedure)**

- **ASTM D86** — Distillation of petroleum products at atmospheric pressure. Procedural anchor for the 90 % recovered limits on distillate grades No. 1 and No. 2.
- **ASTM D93** — Flash point by Pensky-Martens closed-cup. Procedural anchor for the flash-point minima across all six grades.
- **ASTM D97** — Pour point of petroleum products. Procedural anchor for the pour-point limits on No. 1 and No. 2.
- **ASTM D445** — Kinematic viscosity of transparent and opaque liquids. Procedural anchor for the 40 °C kinematic viscosity windows; pairs with **ASTM D2161** for kinematic-to-Saybolt conversion still cited in some legacy residual-fuel contracts.
- **ASTM D524** — Ramsbottom carbon residue. Procedural anchor for the carbon-residue caps on No. 1 and No. 2.
- **ASTM D2622** — Sulfur in petroleum products by WD-XRF. One of two umpire methods for the sulfur caps.
- **ASTM D5453** — Sulfur in light hydrocarbons by UV-fluorescence. Companion umpire method, particularly favored at the low end of the sulfur range as ULS-heating-oil tiers came online.
- **ASTM D4294** — Sulfur in petroleum products by ED-XRF. Field-portable companion to D2622 / D5453 used at delivery and load-out.
- **ASTM D5708** — Trace elements (V, Ni, Fe) in residual fuels by ICP-AES. Companion test for vanadium-and-sodium ash content in No. 5 / No. 6 utility-fuel purchase specs.
- **ASTM D2709** — Water and sediment in middle-distillate fuels. Procedural anchor for the BS&W cap on No. 1 and No. 2.
- **ASTM D1796** — Water and sediment in fuel oils by centrifuge (residual fuels). Procedural anchor for the BS&W caps on No. 4 / No. 5 / No. 6.
- **ASTM D482** — Ash from petroleum products. Procedural anchor for the ash limits on residual grades.

**Adjacent fuel specifications (companion specs in the U.S. / international fuel-spec lattice)**

- **ASTM D975** — Standard Specification for Diesel Fuel Oils. **Sibling D02 specification** — same refinery cut for No. 2-D as for D396 No. 2, different end-use spec (compression-ignition engines vs. burners) with different sulfur tier, lubricity, and cetane requirements. See [astm-d975](astm-d975.md).
- **ASTM D3699** — Standard Specification for Kerosine. Companion spec for kerosene used in lamps and heaters; chemically overlaps with D396 No. 1 but is the spec invoked for non-burner kerosene-fueled service.
- **ASTM D1655** — Standard Specification for Aviation Turbine Fuels (Jet A / Jet A-1). Companion spec for aviation-grade kerosene; explicitly out of D396 scope but draws from the same kerosene cut as D396 No. 1 with much tighter contamination, freeze-point, and thermal-stability limits.
- **ISO 8217** — Petroleum products — fuels (class F) — specifications of marine fuels. **The international successor to D396 No. 6 for marine bunker contracts.** ISO 8217 residual grades (RMA, RMB, RMD, RME, RMG, RMK at increasing viscosity) and distillate grades (DMA / MGO, DMB, DMZ) are the actual transacted spec for international bunker fuel; D396 No. 6 retains domestic-U.S. utility relevance but is no longer the dominant marine-fuel contract.
- **ASTM D6751** — Standard Specification for Biodiesel Fuel Blend Stock (B100) for Middle Distillate Fuels. Defines neat biodiesel; the up-to-5 vol% biodiesel allowance in current D396 editions must comply with D6751 before blending.
- **ASTM D7467** — Standard Specification for Diesel Fuel Oil, Biodiesel Blend (B6 to B20). Covers blends with biodiesel content above the 5 % unlabeled allowance — the parallel framework for heating-oil biodiesel blends ("Bioheat" in the U.S. Northeast residential market) draws on this companion spec.

**Downstream regulations**

- **MARPOL Annex VI** — IMO regulation on sulfur emissions from ships. The **2020 global sulfur cap (0.50 mass%)** and **ECA-zone cap (0.10 mass%)** displaced D396 No. 6 / bunker C from international marine bunker contracts; current bunker fuel transacts under **ISO 8217** with explicit MARPOL-conforming sulfur grades (VLSFO at 0.50 % S, ULSFO at 0.10 % S).
- **EPA non-road and heating-oil sulfur regulations** (40 CFR Part 80 and state-level Northeast U.S. regulations) — drove the introduction of low-sulfur and ultra-low-sulfur tiers into D396 No. 1 / No. 2 across the 2010–2018 edition window.

**Wiki cross-links**

- [Fuel quality and specification](../concepts/fuel-quality-and-specification.md) — concept page that places D396 inside the ASTM fuels-spec family alongside D975, D1655, D3699, D6751, D7467.
- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest and bucket-purity audit; D396 is identified there as the **#2 promotion candidate** by O&G-engineering frequency-of-citation (after D86 and ahead of D445, D975).
- [ASTM D975 — Diesel Fuel Oils](astm-d975.md) — sibling D02 specification page; demonstrates the same `wiki/standards/<code-id>.md` schema and frontmatter contract that this page satisfies.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution at calc time.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; 10,361 documents at `/mnt/ace/O&G-Standards/ASTM/D-Series/`. The source page lists D396 as **#2 promotion candidate** to a per-code `wiki/standards/<code-id>.md` page after D86, on the basis of its anchor role in HFO/MGO bunker-quality specification.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND filename matches /\bD[\s_]?396\b/i` returns the 4 entries enumerated under *Edition history* (1 dated 1998 hit + 3 dated 2002 reprint variants).
- **Vendor PDFs (link-only; do NOT copy into git).** Latest dated edition in catalog: `/mnt/ace/O&G-Standards/ASTM/D-Series/D_396_-_02_RDM5NI0WMG_.pdf` and reprint variants. Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — D396 product page (search "D396" at <https://www.astm.org>); current published edition is newer than the 2002 copy in the local catalog and incorporates the post-2002 sulfur-tier and biodiesel-blend amendments described under *Edition history*.
- **Regulatory anchors.** IMO MARPOL Annex VI (international marine fuel sulfur regulation, 2020 global cap) and U.S. EPA 40 CFR Part 80 / state-level U.S. Northeast heating-oil sulfur regulations.
