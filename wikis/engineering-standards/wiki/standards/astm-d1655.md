---
title: "ASTM D1655 — Aviation Turbine Fuels (Jet A / Jet A-1)"
slug: astm-d1655
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-d1655
publisher: ASTM
revision: latest
revision_source: /mnt/ace/O&G-Standards/_catalog.json (latest in catalog: 2003; ASTM publishes a newer revision — see *Edition history*)
verified_on: 2026-05-09
public_url: https://www.astm.org/d1655.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-d-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - d-series
  - d02
  - jet-fuel
  - aviation
  - jet-a
  - jet-a1
  - fuels
  - standards
---

# ASTM D1655 — Standard Specification for Aviation Turbine Fuels

> **Standard identity (L0 prose).** `code_id`: astm-d1655 · `publisher`: ASTM · `revision`: latest. The latest edition resident in the local O&G-Standards catalog is **2003**; ASTM continues to maintain D1655 with a current published edition newer than the catalog snapshot — see *Edition history* below. This page documents the long-stable property-and-method structure that has carried across editions; numeric limits cited reflect the long-stable consensus values typical of the modern editions and **must be re-verified against the current publisher edition before any acceptance decision**.

## Scope

ASTM D1655 is the **specification for civilian aviation turbine fuels** — the kerosene-cut jet fuels burned by commercial turbofan and turboprop engines. It defines two grades:

- **Jet A** — the U.S. domestic grade, with a **freezing point ≤ −40 °C**.
- **Jet A-1** — the international grade, with a **freezing point ≤ −47 °C** (lower freeze point enables long-haul polar routes where wing-tank fuel can cold-soak).

Both grades share the same flash point, distillation, density, viscosity, sulfur, smoke point, acid number, gum, and thermal-stability requirements; the **freezing point alone** is the principal grade-distinguishing limit. D1655 is the **fuels specification** — it states acceptance limits and points at the test methods used to measure each property; the test methods themselves live in the broader D02 catalog (D86, D445, D93, D2622, D5453, etc.).

D1655 is the civilian counterpart to two adjacent specifications:

- **MIL-DTL-83133** — U.S. military **JP-8** (kerosene-grade jet with mandatory FSII icing inhibitor, corrosion inhibitor / lubricity improver, and static dissipator additive packages — chemically very close to Jet A-1 with required additives).
- **DEF STAN 91-091** — UK MoD / international **Jet A-1** specification, used by most non-U.S. fuel suppliers. The IATA Guidance Material on Aviation Fuel Quality Control aligns the D1655 and DEF STAN 91-091 limits so that international hydrant-fueling at airports converges on a single fungible product (commonly billed as "Jet A-1 to ASTM D1655 / DEF STAN 91-091 / IATA GM").

D1655 covers **petroleum-derived kerosene only**. Synthesized hydrocarbon (SAF) blendstocks — Fischer-Tropsch SPK, HEFA-SPK, ATJ-SPK, etc. — are specified by **ASTM D7566**; once a D7566-compliant synthetic blend is meter-verified to meet all D1655 limits, it may be **redesignated** as D1655 jet fuel for downstream distribution. This redesignation pathway is the single load-bearing seam between civilian SAF policy and the legacy D1655 distribution / hydrant-fueling infrastructure.

## Edition history

ASTM D1655 is reissued frequently (often annually) as additive packages and analytical-method allowances are tightened. The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds **7 PDFs** under `ASTM/D-Series/` matching the D1655 prefix (filename heuristic):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| D 1655 – 00 | `D_1655_-_00_RDE2NTUTMDBB.pdf` | 2000 issue (variant A) |
| D 1655 – 00 | `D_1655_-_00_RDE2NTUTMDBC.pdf` | 2000 issue (variant B — likely errata or reprint) |
| D 1655 – 01 | `D_1655_-_01_RDE2NTUTMDE_.pdf` | 2001 issue |
| D 1655 – 02 | `D_1655_-_02_RDE2NTUTMDI_.pdf` | 2002 issue |
| D 1655 – 03 | `D_1655_-_03_RDE2NTU_.pdf` | 2003 issue (base) |
| D 1655 – 03 | `D_1655_-_03_RDE2NTUTMDM_.pdf` | 2003 issue (variant — likely errata/reapproval) |
| D 1655 – 03 | `D_1655_-_03_RDE2NTUTUKVE.pdf` | 2003 issue (variant with `TUKVE` suffix — possible base-vs-errata pairing per source-page note) |

**7 catalog files across 4 distinct year-codes (2000, 2001, 2002, 2003).** The ASTM publisher-current edition is newer than the 2003 catalog snapshot; numerical limits, additive-package allowances, and SAF-redesignation provisions have evolved (especially after D7566 was first issued in 2009). Resolvers needing the live edition must consult the ASTM publisher catalog. Per spinout governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Key requirements

D1655 organises acceptance limits as a **property → test-method → limit** matrix. The property set has been long-stable; the table below lists the load-bearing properties and the long-stable consensus limits, with all **method allowances** recognised by D1655 (D1655 typically permits any of several alternative methods for a given property, with the methods cross-correlated):

| Property | Method (D1655 cites any of) | Limit |
|----------|------------------------------|-------|
| Flash point | D56 / D93 / D3828 | 38 °C min |
| Density at 15 °C | D1298 / D4052 | 775–840 kg/m³ |
| Distillation, 10 % recovered | D86 | 205 °C max |
| Distillation, final boiling point (FBP) | D86 | 300 °C max |
| Freezing point | D2386 / D5972 / D7153 / D7154 | Jet A: −40 °C max; Jet A-1: −47 °C max |
| Kinematic viscosity at −20 °C | D445 | 8.0 cSt max |
| Sulfur, total mass % | D1266 / D2622 / D4294 / D5453 | 0.30 max |
| Smoke point | D1322 | 25 mm min (or 18 mm min with naphthalenes ≤ 3.0 vol % by D1840) |
| Acid number, mg KOH/g | D3242 | 0.10 max |
| Existent gum, mg/100 mL | D381 | 7 max |
| Thermal stability (JFTOT, 260 °C, 2.5 h) | D3241 | ΔP ≤ 25 mmHg; tube deposit rating ≤ 3 (no Peacock or Abnormal) |

Notes on the matrix:

- **Method choice is operator-elective** within each property's allowed list. Refiners typically run the cheapest/fastest in-spec method for routine release (e.g., D4294 ED-XRF for sulfur, D5972 automated freezing point) and reserve referee methods (D2622 WD-XRF, D2386 manual freezing point) for dispute resolution.
- **Smoke point alternative.** A jet fuel meeting smoke point ≥ 25 mm is unconditionally compliant; a fuel with smoke point 18–24 mm is compliant only if its **naphthalenes content** by **ASTM D1840** is ≤ 3.0 vol %. This dual-path clause accommodates Middle-East / heavily hydrotreated kerosene streams whose smoke point sits below 25 mm but whose aromatic profile is acceptable.
- **Thermal stability (JFTOT, D3241)** is the single most operationally consequential limit — it predicts deposit formation in fuel-oil heat exchangers, fuel nozzles, and afterburner manifolds. Failures here have grounded fuel batches even when every other property is compliant.
- D1655 also carries limits on **water reaction (D1094), copper strip corrosion (D130), electrical conductivity (D2624) when SDA is added, additive concentrations** (FSII / SDA / antioxidant / metal deactivator / corrosion-inhibitor-and-lubricity-improver), and **filtration / particulate / undissolved water at delivery** — those are not enumerated in this overview table.

## Application

D1655 governs **civil aviation turbine fuel only**. The specification is the contractual basis for fuel sold into commercial-aviation hydrant systems at airports worldwide; every batch leaving a refinery on a Jet A or Jet A-1 ticket must be certified to a D1655-compliant test slate. Downstream of the refinery, D1655 quality is preserved through the distribution chain via:

- **Fungible pipeline movement** of Jet A / Jet A-1 alongside other middle distillates, with on-receipt re-test before injection into airport hydrant systems.
- **Airport hydrant fueling**, where the fuel handed to the aircraft must meet D1655 at the wing tip — the IATA Guidance Material on Aviation Fuel Quality Control prescribes the recheck cadence at each transfer hand-off.
- **Bonded into-plane delivery**, where the into-plane company tests the fuel against D1655 limits (typically a reduced-slate "release" check: appearance, density, FSII content, conductivity, particulate, water) before each refueling.

The **IATA Guidance Material** (formally: IATA Aviation Fuel Quality Requirements for Jointly Operated Systems — "AFQRJOS") is the operational glue: it issues a single jointly-recognised quality bulletin that **converges D1655 (Jet A-1 limits) with DEF STAN 91-091**, so that international hydrant operators do not need to maintain dual specs at multiplex airports. AFQRJOS limits are the **most-stringent of D1655 or DEF STAN 91-091** at every line item, so a fuel meeting AFQRJOS is unconditionally compliant with both source specs.

D1655 does **not** apply to:

- Military jet fuels (governed by MIL-DTL-83133 for JP-8 and MIL-DTL-5624 for JP-4 / JP-5).
- General-aviation piston-engine avgas (governed by **ASTM D910**).
- Wide-cut Jet B / JP-4-equivalent fuel (covered by **ASTM D6615** for civilian use).
- Sustainable Aviation Fuel (SAF) blendstocks prior to redesignation (governed by **ASTM D7566**).

## Cross-references

D1655's normative network spans the D02 fuels-and-lubricants test-method catalog (upstream, for measurement procedures) and the international fuels-spec ecosystem (sideways, for grade-equivalence):

**Upstream test-method standards (D1655 invokes for property measurement)**

- **ASTM D86** — Distillation of petroleum products at atmospheric pressure (10 %, 50 %, 90 %, FBP recovery temperatures).
- **ASTM D445** — Kinematic viscosity of transparent and opaque liquids (used at −20 °C for jet).
- **ASTM D93** — Pensky-Martens closed-cup flash point (referee for jet flash).
- **ASTM D56** — Tag closed-cup flash point (alternate, for low-flash distillates).
- **ASTM D3828** — Small-scale closed-cup flash point (rapid screening).
- **ASTM D1266** — Older lamp-method total sulfur (largely supplanted by D2622 / D4294 / D5453 but still cited).
- **ASTM D2622** — Sulfur by wavelength-dispersive XRF (referee).
- **ASTM D4294** — Sulfur by energy-dispersive XRF (rapid release).
- **ASTM D5453** — Sulfur by UV fluorescence (low-level, sub-ppm capable).
- **ASTM D3241** — Thermal-oxidation stability of aviation turbine fuels (the JFTOT test) — single-purpose method for jet thermal stability.
- **ASTM D2386 / D5972 / D7153 / D7154** — Freezing point of aviation fuels (manual cooling-bath, automated phase-transition, automated fiber-optic, and automated laser-method variants — D1655 accepts all four, with cross-correlation rules for dispute resolution).
- **ASTM D1322** — Smoke point of kerosene and aviation turbine fuel.
- **ASTM D1840** — Naphthalene hydrocarbons in aviation turbine fuels by UV spectrophotometry (smoke-point dual-path companion).
- **ASTM D3242** — Acid number of aviation turbine fuels.
- **ASTM D381** — Existent gum in fuels by jet evaporation.
- **ASTM D1298** — Density / relative density / API gravity by hydrometer.
- **ASTM D4052** — Density of liquids by digital densitometer (oscillating U-tube).

**Adjacent fuels specifications (cross-walk)**

- **ASTM D7566** — Standard Specification for Aviation Turbine Fuel Containing Synthesized Hydrocarbons (SAF). Once a D7566 blend meets D1655's full slate, it is redesignated as D1655 fuel for distribution. The seam between civilian SAF policy and legacy hydrant infrastructure runs through this redesignation rule.
- **DEF STAN 91-091** — UK MoD Defence Standard for Turbine Fuel, Aviation Kerosene Type, Jet A-1. The international parallel to D1655's Jet A-1 grade; AFQRJOS reconciles both.
- **MIL-DTL-83133** — U.S. military JP-8 (kerosene jet with required FSII / SDA / corrosion-inhibitor additive package; chemically close to Jet A-1).
- **MIL-DTL-5624** — U.S. military JP-5 (high-flash naval jet) and JP-4 (legacy wide-cut, largely retired).
- **IATA Guidance Material on Aviation Fuel Quality Control (AFQRJOS)** — Joint-operator-system bulletin that takes the most-stringent limit from D1655 ∪ DEF STAN 91-091 at each property; the de-facto international Jet A-1 quality bulletin.
- **ASTM D6615** — Standard Specification for Jet B Wide-Cut Aviation Turbine Fuel (cold-weather wide-cut civilian counterpart to D1655).
- **ASTM D910** — Standard Specification for Aviation Gasolines (piston-engine avgas; not a turbine fuel — included here for boundary clarity).

**Wiki cross-links**

- [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md) — multi-edition coverage manifest and recommended-promotion list (D1655 is **promotion #5** of 15).
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution from downstream calc modules.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM D-Series](../sources/og-standards-astm-d-series.md). Catalog manifest for the entire ASTM D-Series slice; D1655 is identified there as a **#5 promotion candidate** for `wiki/standards/<code-id>.md` (anchor spec for jet-fuel custody-transfer; 7 editions in catalog).
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND relative_path startswith 'ASTM/D-Series/' AND filename matches /\bD[\s_]?1655\b/i` returns the 7 entries enumerated under *Edition history*.
- **Vendor PDFs (link-only; do NOT copy into git).** Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their private-vendor-mount location and are not republished here. The catalog filename pattern `D_1655_-_YY_RDE2NTU…pdf` is the resolution key.
- **Publisher catalog.** ASTM International — D1655 product page (search "D1655" at <https://www.astm.org>). The publisher catalog carries the live edition; this page documents the long-stable property structure and must be reverified against the live edition before being used as the basis for any acceptance decision.
