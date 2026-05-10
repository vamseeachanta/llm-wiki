---
title: "ASTM D4814 — Automotive Spark-Ignition Engine Fuel (Gasoline)"
slug: astm-d4814
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d4814
publisher: ASTM
revision: "2003 (latest in catalog); publisher-current edition is newer — see Edition history"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/d4814-24.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - gasoline
  - motor-fuel
  - spark-ignition
  - ethanol-blend
  - standards
---

# ASTM D4814 — Standard Specification for Automotive Spark-Ignition Engine Fuel

> **Standard identity (L0 prose).** `code_id`: astm-d4814 · `publisher`: ASTM · `revision`: 2003 (latest dated edition resident in `/mnt/ace/O&G-Standards/_catalog.json`; ASTM reissues D4814 on a roughly annual cadence and the publisher-current edition is newer than the catalog's 2003 copy — see *Edition history* below).

## Scope

ASTM D4814 is the **master U.S. specification for finished spark-ignition gasoline (motor fuel)** sold at retail for passenger cars and light-duty trucks running Otto-cycle engines. It is the gasoline-side companion to **[ASTM D975](astm-d975.md)** (diesel) within ASTM committee **D02** (Petroleum Products and Lubricants) and is the spec invoked by U.S. fuel-supply contracts, state weights-and-measures programs, and engine-OEM warranty fuel requirements.

D4814 covers the **entire finished-fuel property set** that determines automotive spark-ignition performance: volatility (cold-start and hot-fuel-handling), antiknock quality (octane), oxidation and storage stability, copper-strip corrosion, gum-forming tendency, sulfur, lead and manganese controls, and oxygenate (ethanol) content. It is structured around **eight Volatility Classes (AA, A, B, C, D, E, plus the dual-class transition months)** that are zone-mapped to U.S. states and months via the **EPA "Vehicle-Fuel Schedule"** to balance cold-start drivability in winter against hot-start vapor-lock and evaporative-emissions control in summer.

D4814 explicitly **allows up to 10 vol% ethanol (E10)** as an unlabeled component of any covered grade — meaning U.S. retail gasoline marked "ASTM D4814" may contain up to 10% ethanol without separate disclosure. Higher ethanol blends (**E15** through **E50**) for use in **flex-fuel vehicles and approved 2001+ light-duty vehicles** are covered by separate specifications (notably **ASTM D7794** and the state-by-state EPA E15 waiver framework), not D4814 itself. Pure denatured fuel ethanol (the E100 blendstock) is covered by **ASTM D4806**.

D4814 does **not** cover **aviation gasoline (avgas)** — that is **ASTM D910**; **diesel fuel** — **[ASTM D975](astm-d975.md)**; **kerosene/jet** — **ASTM D1655**; **racing or off-road methanol-fuel blends**; or fuel-additive specifications themselves. It is a finished-fuel specification, not an additive specification.

## Edition history

ASTM D4814 is reissued on a roughly annual cadence (often two letter-suffix reapprovals per calendar year for editorial errata). The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/D-Series/` (filename heuristic; D4814 is identified as **8 dated multi-edition filename hits + 1 root-level `D4814.PDF`** in the source-page audit):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| D 4814 – 00 | `D 4814 - 00  _RDQ4MTQTMDA_.pdf` | 2000 issue |
| D 4814 – 00 (variant) | `D 4814 - 00  _RDQ4MTQTMDBB.pdf` | 2000 reprint variant |
| D 4814 – 01 | `D 4814 - 01  _RDQ4MTQTMDE_.pdf` | 2001 issue |
| D 4814 – 01 (variant) | `D 4814 - 01  _RDQ4MTQTMDFB.pdf` | 2001 reprint variant |
| D 4814 – 02 | `D 4814 - 02  _RDQ4MTQTMDI_.pdf` | 2002 issue |
| D 4814 – 03 | `D 4814 - 03  _RDQ4MTQTMDM_.pdf` | 2003 issue |
| D 4814 – 03 (variant) | `D 4814 - 03  _RDQ4MTQTUKVE.pdf` | 2003 reapproval/errata variant (`_TUKVE` tag) |
| D 4814 – 03 (variant) | `D 4814 - 03  _RDQ4MTQ_.pdf` | 2003 short-tag variant — **latest dated edition in catalog** |
| D4814 (untagged) | `D4814.PDF` | Root-level untagged copy; edition unverified without OCR |

**9 catalog hits across at least 4 distinct dated editions (2000, 2001, 2002, 2003).** The 2003 edition is the latest in the catalog. ASTM has continued maintaining D4814 on annual reissue and the publisher-current edition is materially newer than 2003 — most importantly, the **Tier 3 sulfur cap (80 mg/kg, January 2017)** and the **modernization of the Driveability Index formula** post-date the catalog's 2003 copy. The **E10 (10 vol% ethanol) allowance** has been part of D4814 since the 1990s but was reinforced and re-cross-referenced (to D4806 and D5798) in editions later than the catalog snapshot. Resolvers needing the live edition should consult the publisher catalog directly. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key requirements

D4814 sets **numeric limits per Volatility Class** on the properties below and binds each property to a designated ASTM test method. The table captures the canonical property set; class-dependent numeric bands (RVP, distillation T10/T50/T90, V/L temperature, Driveability Index) vary by Volatility Class A through E and are detailed in *Volatility classes* below.

| Property | Test method | Limit |
|----------|-------------|-------|
| Distillation T10 / T50 / T90 / FBP (final boiling point) | **ASTM D86** | Class-dependent (see *Volatility classes*); FBP typically 225 °C max |
| Reid Vapor Pressure (RVP) | **ASTM D5191** (mini-method) / **D323** (legacy) | Class-dependent: **7.0 to 15.0 psi** by season + zone |
| Driveability Index (DI) | calculated from D86 distillation: `DI = 1.5·T10 + 3·T50 + T90 + 1.33·(vol% ethanol)` | Class-dependent (typically ≤ 1200–1250 at U.S. customary units) |
| V/L ratio temperature (`T(V/L=20)`) | **ASTM D5188** | Class-dependent (T at which vapor-to-liquid ratio = 20) |
| Sulfur | **ASTM D2622** (WD-XRF) / **D5453** (UV-fluorescence) | **80 mg/kg max** (EPA Tier 3, since Jan 2017); historical D4814 limits were higher |
| Antiknock Index (AKI) = (RON+MON)/2 | **ASTM D2700** (motor octane, MON) + **D2699** (research octane, RON) | Posted at retail: **87 / 89 / 91 / 93** typical (regular / mid-grade / premium / ultra-premium); D4814 itself does not set AKI minimums — minimums are set by state weights-and-measures and OEM specs |
| Existent gum, washed | **ASTM D381** | **5 mg/100 mL max** |
| Oxidation stability | **ASTM D525** | **240 min minimum** (induction period) |
| Copper-strip corrosion, 3 h @ 50 °C | **ASTM D130** | **No. 1 max** |
| Lead | **ASTM D3237** (atomic absorption) | "Lead-free" in U.S. retail since the 1990s; trace limit ≤ 0.013 g/L |
| Manganese (MMT additive control) | **ASTM D3831** | **≤ 2 mg Mn/L** under EPA waiver (otherwise prohibited) |
| Ethanol content | **ASTM D5599** (oxygenates by GC-OFID) / **D4815** (MTBE/ethers/alcohols by GC) | **≤ 10 vol% ethanol** (E10) for unlabeled D4814 fuel |
| Water tolerance (ethanol blends) | **ASTM D6422** (phase-separation temperature) | Reported per class (no cap; informational for cold-weather phase stability) |

**Key engineering notes on the limits.**

- **RVP (Reid Vapor Pressure) and the seasonal class system are the dominant drivability-and-emissions lever.** Winter classes (D, E) raise RVP up to 15.0 psi to volatilize enough fuel for cold-start; summer classes (AA, A) cap RVP at 7.0–9.0 psi to suppress evaporative emissions and tank-vent breathing losses that drive ozone-forming VOCs. Mis-zoned summer fuel in winter causes hard-start; mis-zoned winter fuel in summer causes vapor-lock and excessive evaporative emissions. **RVP is the single most regulated property in U.S. retail gasoline** under EPA 40 CFR Part 80.
- **Distillation curve (D86) governs cold-start, warm-up, and acceleration.** The T10 (10% recovered) point controls cold-start ease; T50 controls warm-up and short-trip drivability; T90 and FBP control combustion-chamber and engine-oil dilution. The empirical **Driveability Index** combines T10/T50/T90 with the ethanol-content correction `1.33·(vol% ethanol)` because ethanol's azeotropic distillation behavior makes a fuel "drive" worse than its T-points alone would predict at the same DI.
- **V/L ratio temperature (D5188)** is the temperature at which 1 mL of liquid fuel produces 20 mL of vapor at atmospheric pressure. It is the modern hot-fuel-handling indicator, replacing the older "vapor-liquid ratio at fixed temperature" formulations and correlating directly with hot-start, hot-restart, and hot-driveaway behavior.
- **Sulfur — Tier 3 (80 mg/kg max, Jan 2017)** brought U.S. retail gasoline into harmony with European EN 228 levels (10 mg/kg) for federal averaging. Tier 3 enables three-way-catalyst durability for stoichiometric SI engines and is a precondition for low-NOₓ combustion-strategy compliance with U.S. light-duty Tier 3 / SULEV30 emissions regulations. Sulfur quantitation is **D5453 (UV-fluorescence)** as the umpire method and **D2622 (WD-XRF)** for in-line and dispute resolution.
- **Antiknock Index (AKI = (RON+MON)/2)** is what U.S. retail pumps display ("octane rating"). D4814 does **not itself set a minimum AKI** — it certifies that whatever AKI is *posted* was measured by D2699 + D2700 against the primary reference fuels (PRFs). State weights-and-measures regulations (typically 87 minimum for "regular") and OEM warranty specifications (87 / 91 / 93 depending on engine compression ratio and turbo boost) set the *required* AKI. The European "RON-only" labeling convention (e.g., "95 RON" for U.S. ~91 AKI) is **not** D4814-compatible at retail.
- **Existent gum (D381, 5 mg/100 mL max)** caps the deposit-forming oxidized-hydrocarbon and oxidized-additive content in the as-delivered fuel; pairs with **oxidation stability (D525, 240 min min)** which forecasts the rate at which gum *will form* in storage. Both matter most for low-turnover retail (rural, marine, seasonal) and for fuel-injector and intake-valve cleanliness.
- **Copper-strip corrosion (D130, No. 1 max)** detects active sulfur (mercaptans, H₂S, elemental S) and free-acid contamination at levels below the bulk-sulfur cap. Fuels passing the 80 mg/kg sulfur limit can still fail D130 if the sulfur is present as active species.
- **Lead, manganese (MMT), and ethanol** are the three composition controls where D4814 enforces **U.S. fuel-policy choices**, not measurement uncertainty. Lead is "lead-free" by federal law since the 1990s phase-out; **manganese** (the antiknock additive **MMT — methylcyclopentadienyl manganese tricarbonyl**) is permitted only under EPA waiver at ≤ 2 mg Mn/L because of catalyst-poisoning concerns; **ethanol ≤ 10 vol%** caps the unlabeled E10 retail allowance, with E15 and E85 covered separately.

## Volatility classes

D4814's Volatility Class system is the spec's defining feature and the mechanism through which a single national gasoline specification accommodates U.S. climate variation from Phoenix in August to International Falls in January. **Eight classes** are defined — **AA, A, B, C, D, E**, plus **dual-class transition months** (typically AA/A, A/B, B/C, C/D, D/E) — and each class fixes a coordinated band on RVP, T10, T50, T90, and the V/L temperature.

| Volatility Class | Typical RVP (psi) | T50 distillation (°C) | V/L=20 temperature | Service window |
|------------------|-------------------|------------------------|---------------------|----------------|
| **AA** (lowest volatility) | 7.0–7.8 | higher | higher | Hot-summer Sun Belt (Phoenix, Houston, Miami) |
| **A** | 7.8–9.0 | | | Warm summer / shoulder season most of CONUS |
| **B** | 8.5–10.0 | | | Spring / fall transition |
| **C** | 9.0–11.5 | | | Cool fall and early winter |
| **D** | 10.0–13.5 | lower | lower | Winter most of CONUS |
| **E** (highest volatility) | 11.5–15.0 | lowest | lowest | Cold-winter Upper Midwest, Mountain West, Alaska |

The mapping of **state + month → required Volatility Class** is published by the **EPA "Vehicle-Fuel Schedule"** (referenced by D4814 Appendix X) and republished in revised form annually. Refiners and terminal operators stage seasonal transitions across **late-spring (winter → summer fuel)** and **mid-fall (summer → winter fuel)** windows; the late-spring transition is the more emissions-sensitive of the two because RVP cuts of 2–4 psi must be achieved across the U.S. fuel-distribution system in 4–6 weeks to meet the **June 1 federal summer-RVP enforcement date**.

The **dual-class transition months** in the EPA Schedule (e.g., "April: B or C" in a given state) allow refiners and terminals to draw down winter inventory without forcing a hard switch, but the *fuel at the pump* must meet whichever class is dispensed — terminals running mixed inventory must blend or label accordingly.

The **Driveability Index** correction `1.33·(vol% ethanol)` matters most for Class D and E winter fuels with E10 because ethanol's azeotrope with light hydrocarbons distorts the cold-start volatility envelope; ignoring the correction causes hard-start failures on winter E10 even when the T10 point alone would predict acceptable performance.

## Cross-references

D4814 sits at the convergence of the ASTM **D02 committee** (petroleum products and lubricants) and downstream U.S. regulation (EPA 40 CFR Part 80 RVP and sulfur, CARB Phase 3 RFG in California), engine-OEM material specifications, and parallel international gasoline specs.

**Upstream test-method standards (D4814 defers to these for the underlying procedure)**

- **[ASTM D86](astm-d86.md)** — Distillation of petroleum products at atmospheric pressure. The procedural anchor for T10, T50, T90, and FBP and for the Driveability Index calculation.
- **ASTM D5191** — Vapor pressure of petroleum products (mini-method). The modern procedural anchor for RVP, replacing the legacy **ASTM D323** (Reid method, manual bomb) for most regulatory and commercial use.
- **ASTM D5188** — Vapor-liquid ratio temperature determination. Procedural anchor for the V/L=20 temperature.
- **ASTM D2699** — Research octane number (RON) by knock-engine, light-load condition.
- **ASTM D2700** — Motor octane number (MON) by knock-engine, severe-load condition. Posted retail AKI is `(RON+MON)/2` — both methods must be run.
- **ASTM D2622** — Sulfur in petroleum products by WD-XRF.
- **ASTM D5453** — Sulfur in light hydrocarbons by UV-fluorescence (umpire at the 80 mg/kg Tier 3 level).
- **ASTM D381** — Gum content in fuels by jet evaporation (existent gum).
- **ASTM D525** — Oxidation stability of gasoline (induction-period method).
- **ASTM D130** — Detection of copper corrosion from petroleum products (copper-strip).
- **ASTM D3237** — Lead in gasoline by atomic absorption spectroscopy.
- **ASTM D3831** — Manganese in gasoline by atomic absorption spectroscopy.
- **ASTM D5599** — Determination of oxygenates in gasoline by GC and oxygen-selective flame ionization detection (O-FID).
- **ASTM D4815** — Determination of MTBE, ETBE, TAME, DIPE, tertiary-amyl alcohol and C₁ to C₄ alcohols in gasoline by GC.
- **ASTM D6422** — Water tolerance / phase-separation temperature for gasoline-ethanol blends.

**Adjacent fuel specifications (companion specs in the U.S. / international fuel-spec lattice)**

- **[ASTM D975](astm-d975.md)** — Standard Specification for Diesel Fuel Oils. Compression-ignition companion spec; explicitly out of D4814 scope.
- **ASTM D910** — Standard Specification for Aviation Gasolines (avgas). Spark-ignition aviation fuel; explicitly out of D4814 scope and using a different antiknock-rating scale (motor and supercharge methods).
- **ASTM D1655** — Standard Specification for Aviation Turbine Fuels (Jet A / Jet A-1).
- **ASTM D4806** — Standard Specification for Denatured Fuel Ethanol for Blending with Gasolines for Use as Automotive Spark-Ignition Engine Fuel. The **E100 blendstock spec** that the up-to-10 vol% ethanol allowance in D4814 must comply with before blending.
- **ASTM D5798** — Standard Specification for Ethanol Fuel Blends for Flexible-Fuel Automotive Spark-Ignition Engines (E51 to E83 — the spec colloquially called "E85").
- **ASTM D7794** — Standard Practice for Blending Mid-Level Ethanol Fuel Blends for Flexible-Fuel Automotive Spark-Ignition Engines (E16 to E50). Covers blends above the 10% D4814 unlabeled allowance and below the D5798 flex-fuel range.
- **ASTM D6751** — Biodiesel B100 spec; applies to the diesel-side fuel chain ([D975](astm-d975.md) → D6751 / D7467), not gasoline.
- **EN 228** — European Committee for Standardization (CEN) European unleaded-gasoline specification. The **EU-side parallel to D4814**; broadly similar property set but with **tighter sulfur (10 mg/kg vs. 80 mg/kg Tier 3)**, **RON-based octane labeling** (95 RON minimum for "Eurosuper", 98 RON for "Super Plus"), and **different volatility classes** (Class A through F, mapped by month rather than month + state). Cross-Atlantic gasoline trade routinely requires dual-spec attestation.
- **JIS K 2202** — Japanese gasoline specification.

**Downstream regulations and engine-OEM specs (call D4814 by reference)**

- **EPA 40 CFR Part 80** — U.S. federal gasoline regulation. Sets the sulfur cap (Tier 3, 80 mg/kg from January 2017), the **federal summer RVP standard** (the "1-psi waiver" for E10 in conventional-gasoline regions), and the **Reformulated Gasoline (RFG)** program for ozone-nonattainment metropolitan areas.
- **California Code of Regulations Title 13 / CARB Phase 3 Reformulated Gasoline (Phase 3 RFG)** — California-specific gasoline spec layered on top of D4814 with **tighter sulfur**, **lower RVP in summer**, **lower aromatics, olefins, and benzene caps**, and a **mandatory MTBE prohibition** (replaced by ethanol). California-grade gasoline is a distinct fungible product from CONUS D4814 and is priced separately at the wholesale rack.
- **EPA E15 misfueling rule (40 CFR Part 80, Subpart M)** — separately authorizes E15 sale for 2001-and-newer light-duty vehicles via a state-by-state waiver framework; E15 is **not** D4814-compliant and carries its own pump-labeling requirements.
- **OEM engine-manufacturer fuel specifications** — GM, Ford, Stellantis, Toyota, Honda, and others publish engine-specific fuel specs that use D4814 as the base spec and overlay **tighter octane minimums for turbocharged and high-compression engines** (often 91 AKI minimum and "Top Tier" detergent additization).
- **"Top Tier" detergent gasoline standard** — voluntary OEM-driven additive-package specification layered on top of D4814; not part of D4814 itself, but is the de facto premium-brand gasoline specification at major U.S. retail brands.

**Wiki cross-links**

- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest and bucket-purity audit; D4814 is identified there as one of the top-edition codes (8 dated filename hits) on the gasoline side, paired with D2699 and D2700 (octane methods) as the "gasoline anchor triad" within the D02 subcommittee.
- [ASTM D975 — Diesel Fuel Oils](astm-d975.md) — sibling first-class standards page on the compression-ignition side; demonstrates the same `wiki/standards/<code-id>.md` schema and frontmatter contract.
- [ASTM D86 — Distillation at atmospheric pressure](astm-d86.md) — primary upstream test method for D4814's distillation-curve requirements.
- [Fuel quality and specification](../concepts/fuel-quality-and-specification.md) — concept page in this wiki that forward-references D4814 in the U.S. spec family alongside D975, D1655, D396, and the biodiesel/ethanol blendstock chain.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution at calc time.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; 10,361 documents at `/mnt/ace/O&G-Standards/ASTM/D-Series/`. The source page identifies D4814 as one of the top-edition codes (8 dated filename hits) and lists it alongside D86, D975, D2699, and D2700 as a high-priority promotion candidate for per-code `wiki/standards/<code-id>.md` pages.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND filename matches /\bD[\s_]?4814\b/i` returns the 9 entries enumerated under *Edition history* (8 dated `D 4814 - YY  _RDQ4MTQ…pdf` hits across 4 distinct years 2000 / 2001 / 2002 / 2003, plus 1 root-level `D4814.PDF`).
- **Vendor PDFs (link-only; do NOT copy into git).** Latest dated edition in catalog: `/mnt/ace/O&G-Standards/ASTM/D-Series/D 4814 - 03  _RDQ4MTQTMDM_.pdf` and reapproval/reprint variants. Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — D4814 product page (search "D4814" at <https://www.astm.org>); current published edition is newer than the 2003 copy in the local catalog.
- **Regulatory anchors.** U.S. EPA 40 CFR Part 80 (federal gasoline sulfur Tier 3, RVP, RFG, E15 misfueling rule) and California Code of Regulations Title 13 / CARB Phase 3 Reformulated Gasoline (state-additional gasoline-fuel requirements).
