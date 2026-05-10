---
title: "ASTM A335 — Seamless Ferritic Alloy-Steel Pipe for High-Temperature Service"
slug: astm-a335
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-a335
publisher: ASTM
revision: "2003 (latest in catalog) / latest at publisher"
revision_source: /mnt/ace/O&G-Standards/_catalog.json
verified_on: 2026-05-09
public_url: https://www.astm.org/a0335_a0335m-23.html
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-astm-a-series.md
  - /mnt/ace/O&G-Standards/ASTM/A-Series/A_335___A_335M___03__;QTMZNS9BMZM1TQ__.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
tags:
  - astm
  - a-series
  - high-temperature-pipe
  - p11
  - p22
  - p91
  - p92
  - cr-mo
  - power-plant
  - refinery
---

# ASTM A335 / A335M — Standard Specification for Seamless Ferritic Alloy-Steel Pipe for High-Temperature Service

> **Standard identity (L0 prose).** `code_id`: astm-a335 · `publisher`: ASTM · `revision`: 2003 (latest edition resident in `/mnt/ace/O&G-Standards/_catalog.json`; ASTM continues to maintain A335 on a roughly biennial cadence — current published edition at the publisher is newer than the catalog copy, see *Edition history* below).

## Scope

ASTM A335 / A335M covers **seamless ferritic alloy-steel pipe** intended for **high-temperature service** in fossil-fuel and nuclear power generation, refining, and petrochemical fabrication. The specification defines a family of grades — **P1, P2, P5, P5b, P5c, P9, P11, P12, P15, P21, P22, P23, P24, P36, P91, P92, P122** — spanning carbon-molybdenum (C-Mo) chemistry through low-chrome and intermediate-chrome Cr-Mo alloys to the modern modified 9–12 % Cr martensitic creep-strength-enhanced ferritic (CSEF) grades. Pipe is furnished hot-finished or cold-drawn; nominal pipe sizes are common to ASME B36.10. Each grade has its own controlled chemistry, heat-treatment regime, mechanical-property minima, and Charpy/hardness/NDE requirements.

A335 does not specify acceptance criteria for end-product service — those are imposed by the consumer code (ASME BPVC II-A for allowable stress, ASME B31.1 / B31.3 for piping design, API 530 for fired-heater tubes, API 934-A/E for hydroprocessing reactors). A335 specifies **what the pipe is** and **how it is qualified**, so that downstream pressure-design codes can tabulate allowable stress against a fixed chemistry-and-heat-treat envelope.

## Edition history

ASTM A335 / A335M is reissued on a roughly biennial cadence with intermediate "a", "b" letter-revisions when grade additions land between full reissues (P91 was added in the 1990s, P92 and P122 in the early 2000s, P23/P24 around the same window). The local O&G-Standards catalog (`_catalog.json`, generated 2025-12-25) holds the following editions under `ASTM/A-Series/` (filename heuristic, organization=ASTM, regex `\bA[\s_]?0*335\b`):

| Edition | Catalog filename | Notes |
|---------|------------------|-------|
| A 335 / A 335M – 00 | `A_335_A_335M_00_;QTMZNS0WMA__.pdf` | 2000 issue |
| A 335 / A 335M – 02 | `A_335_A_335M_02_;QTMZNS0WMG__.pdf` | 2002 issue |
| A 335 / A 335M – 02 | `A_335_A_335M_02_;QTMZNS9BMZM1TS1SRUQ_.pdf` | 2002 issue (reprint variant — `…REDLINE` token in encoded suffix) |
| A 335 / A 335M – 03 | `A_335_A_335M_03_;QTMZNS9BMZM1TQ__.pdf` | 2003 issue — **latest in catalog** |

**4 catalog files across 3 distinct editions (2000, 2002, 2003).** The publisher's currently-active edition is newer than the catalog's 2003 copy; resolvers needing the live edition should consult the publisher catalog directly. Per spinout 2026-05-05 governance, vendor PDFs do not enter this repo — only the metadata above is recorded.

## Grade summary

The table below summarizes the principal alloy families covered by A335. Maximum-design-temperature numbers reflect typical ASME BPVC II-A allowable-stress cutoffs and industry practice for the grade; actual permissible service temperature for a specific component is set by the consumer code (BPVC, B31.1, B31.3, API 530, API 934-A) and may be lower than the metallurgical limit.

| Grade | Composition (nominal) | Indicative max-T design service |
|-------|----------------------|-------------------------------|
| **P1** | C–0.5Mo | 538 °C |
| **P2** | 0.5Cr–0.5Mo | 540 °C |
| **P5** | 5Cr–0.5Mo | 593 °C |
| **P9** | 9Cr–1Mo | 593 °C |
| **P11** | 1.25Cr–0.5Mo–Si | 593 °C (refinery hydrofiner workhorse) |
| **P12** | 1Cr–0.5Mo | 580 °C |
| **P22** | 2.25Cr–1Mo | 593 °C (refinery + power-plant workhorse) |
| **P23** | 2.25Cr–1.6W–V (modern Cr-Mo-W) | 600 °C+ |
| **P91** | 9Cr–1Mo–V–Nb–N (modified martensitic, CSEF) | 600–650 °C (modern supercritical power + reformer service) |
| **P92** | 9Cr–1.8W–0.5Mo–V–Nb–N | 600–650 °C (next-generation USC steam) |
| **P122** | 12Cr–0.4Mo–2W–Cu–V–Nb–N (Japan-developed) | 620 °C |

Grades P5b / P5c / P15 / P21 / P36 / P24 are also covered but are less prevalent in offshore / refining / power procurement than the workhorses listed above.

## Why each grade matters

**P11 and P22 are the refinery / lower-temperature power-plant workhorses.** P11 (1.25Cr-0.5Mo-Si) covers naphtha hydrofiners, lower-temperature process piping, and the cooler legs of fired-heater furnace runs. P22 (2.25Cr-1Mo) dominates hydroprocessing reactor effluent and feed piping; for the reactor shell itself, the V-modification — 2.25Cr-1Mo-V per **API 934-A** — supersedes plain P22, but the unmodified P22 still rules adjacent transfer piping. P22 also fills the boiler-water-wall and primary-superheater niche in subcritical and lower-supercritical steam generators.

**P91 dominates modern supercritical and ultra-supercritical (USC) power-plant superheater + reheater + main-steam piping.** Introduced in the 1980s-90s as a creep-strength-enhanced ferritic (CSEF) replacement for the older 9Cr-1Mo P9, the V/Nb/N additions deliver ~50 % higher allowable stress at 600 °C, allowing thinner-wall steam piping for the same pressure rating and a corresponding reduction in thermal-fatigue crack initiation at attachments. P91 also appears in petrochemical reformer outlet manifolds and high-temperature transfer piping. The grade is **PWHT-sensitive** — improper post-weld heat treatment causes Type IV cracking in the fine-grain heat-affected zone — and several published USC-plant failures trace to PWHT non-compliance rather than parent-metal defects.

**P92 and P122 are the next-generation grades** for ~620 °C USC service, with stronger tungsten alloying displacing some of the molybdenum in P91 for higher creep rupture strength, but with similar Type-IV PWHT sensitivity and (for P122) cost-of-chromium implications.

**Older plants still operate P5 / P9 fired-heater tubes** (5Cr-0.5Mo and 9Cr-1Mo). For these, end-of-life is set by **API 530** creep-life remaining-life assessment using minimum-wall-temperature monitoring and the Larson-Miller parameter; A335 sets the as-procured envelope, but operating-life management is a consumer-code responsibility — see [creep-and-stress-rupture](../concepts/creep-and-stress-rupture.md).

## Mechanical and chemical requirements

A335 specifies the following property and qualification envelopes (numerical values vary by grade; consult the standard's grade-specific tables for exact limits):

- **Tensile properties.** Per-grade minimum yield strength, minimum tensile strength, and minimum elongation in 2 inches / 50 mm. Tested per [ASTM A370](astm-a370.md) — typically a longitudinal round specimen from the pipe wall.
- **Hardness.** Maximum hardness limits on the pipe body (Brinell HBW), with grade-specific caps tightened for the modified martensitic grades (P91/P92/P122) where over-hardness signals incomplete tempering and carries a stress-corrosion / sulfide-stress-cracking penalty in service.
- **Charpy V-notch impact.** Required for thicker-wall pipe and at lowest design temperature for grades intended for operation across a transition-temperature regime; specimen geometry and reporting per [ASTM A370](astm-a370.md) §9.
- **Chemistry.** Per-grade elemental envelopes for C, Mn, P, S, Si, Cr, Mo, Ni, Cu, V, Nb, W, N, Al, B, Ti — depending on grade. **P + S impurity limits are critical for the 1Cr–9Cr grades**: residual P, Sn, Sb, As (the "tramps") promote temper-embrittlement (J-factor and X-factor) that consumes Charpy reserve during decades-long service exposure. See [temper-embrittlement](../concepts/temper-embrittlement.md) for J-factor / X-factor formulas and consumer-code (API 934-A) limits that supplement the A335 chemistry envelope for hydroprocessing service.
- **Heat treatment + tempering.** Each grade has a mandated heat-treatment condition (annealed, normalized-and-tempered, or quench-and-tempered for the martensitic CSEF grades). PWHT temperatures and hold times are **grade-specific and rigorous** — particularly for P91/P92/P122 where sub-AC1 PWHT is the only acceptable post-weld treatment and over-tempering during repair welding ruins the grade's high-temperature creep performance.
- **NDE.** Either **hydrostatic test** OR **non-destructive electric (UT or eddy-current) examination** per ASTM E213 / E309 / E570 — purchaser election. Each pipe length is examined for body and seam integrity.
- **Hydrogen-charging considerations.** A335 grades P5–P22 are common in services where atomic hydrogen ingress occurs (hydrofiners, hydrocrackers, hydrotreaters). The chrome/moly chemistry resists **high-temperature hydrogen attack (HTHA)** per the partial-pressure/temperature operating-envelope curves in [API RP 941](api-rp-941.md); see [htha-nelson-curves](../concepts/htha-nelson-curves.md) for the Nelson-curve methodology that governs grade selection between A335 P11 / P22 / P22-V / P5 / P9 in hydroprocessing service.

## Cross-references

A335 sits at the convergence of the ASTM A-committee material-supply chain and several downstream pressure-design + fitness-for-service codes:

**Upstream test-method standard**
- **[ASTM A370](astm-a370.md)** — Mechanical testing of steel products. The qualifying test method for tension, Charpy, and hardness on every A335 grade.

**Sibling product specifications (paired with A335 in fabrication procurement)**
- **ASTM A832** — Standard specification for stainless and alloy-steel pressure-vessel plates, alloyed, V-modified normalized & tempered (covers the 2.25Cr-1Mo-V plate that pairs with A335 P22 piping for hydroprocessing reactor shells).
- **ASTM A234 / A234M** — Piping fittings of wrought carbon and alloy steel for moderate-to-high-temperature service. WP1 / WP11 / WP22 / WP91 fittings pair with the corresponding A335 P-grade pipe.
- **ASTM A213 / A213M** — Seamless ferritic / austenitic alloy-steel boiler/superheater/heat-exchanger tubes. T-grades (T11, T22, T91, T92, T122) are the **tube** equivalents of the A335 P-grades for the same alloys.

**Downstream pressure-design + fitness-for-service consumers**
- **ASME BPVC Section II Part A — Ferrous Material Specifications** — republishes A335 as **SA-335 / SA-335M** and tabulates allowable stress for each P-grade against design temperature in the BPVC II-D stress tables that B31.1 and B31.3 consume.
- **ASME B31.1 — Power Piping** — invokes SA-335 for main-steam, hot-reheat, cold-reheat, and high-temperature feedwater piping in fossil-fuel boilers; PWHT and notch-toughness rules layered on top of A335.
- **ASME B31.3 — Process Piping** — invokes A335 for high-temperature process services in refining and petrochemical fabrication; B31.3 imposes its own PWHT, hardness, and impact-test rules over A335 for sour, hydrogen, and creep-range services.
- **API 530 — Calculation of Heater-Tube Thickness in Petroleum Refineries** — primary consumer for **A335 P5, P9, P22 fired-heater tubes** (and the A213 equivalents). Minimum-wall design and creep-life remaining-life assessment use Larson-Miller curves keyed to the A335 grade chemistry — see [creep-and-stress-rupture](../concepts/creep-and-stress-rupture.md).
- **API 934-A — Materials and Fabrication of 2.25Cr-1Mo-¼V, 3Cr-1Mo, 3Cr-1Mo-¼V Steel Heavy-Wall Pressure Vessels for High-Temperature, High-Pressure Hydrogen Service** — augments A335 P22 with V-modification and tightened tramp-element limits for hydroprocessing reactor service; ties to **temper-embrittlement** + **HTHA** controls.
- **API RP 941 — Steels for Hydrogen Service at Elevated Temperatures and Pressures in Petroleum Refineries and Petrochemical Plants** — the Nelson-curve standard that governs A335 grade selection (P5 / P9 / P11 / P22 / P22-V) in hydrogen partial-pressure / temperature space; see [htha-nelson-curves](../concepts/htha-nelson-curves.md).
- **[API 570](api-570.md)** — In-service inspection / repair / alteration of piping; covers in-service creep + temper-embrittlement + HTHA inspection of A335 piping circuits.

**Wiki concept-page consumers**
- [creep-and-stress-rupture](../concepts/creep-and-stress-rupture.md) — Larson-Miller / Orr-Sherby-Dorn parameters used for end-of-life assessment of A335 P5 / P9 / P22 / P91 in fired-heater and main-steam service.
- [temper-embrittlement](../concepts/temper-embrittlement.md) — J-factor and X-factor controls layered on A335 P22 chemistry for heavy-wall hydroprocessing reactor service.
- [htha-nelson-curves](../concepts/htha-nelson-curves.md) — Nelson-curve grade-selection methodology that governs the choice between A335 P11 / P22 / P22-V / P5 / P9 in hydrogen service.

**Wiki cross-links**
- [O&G Standards catalog — ASTM A-Series](../sources/og-standards-astm-a-series.md) — multi-edition coverage manifest for the A-Series slice.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — frontmatter contract (`code_id`, `publisher`, `revision`) this page satisfies for fail-closed citation resolution.

## Sources

- **Source page (this wiki).** [O&G Standards catalog — ASTM A-Series](../sources/og-standards-astm-a-series.md). Catalog manifest for the entire ASTM A-Series slice (2,147 documents at `/mnt/ace/O&G-Standards/ASTM/A-Series/`); A335 is identified there as part of the deep multi-edition pipe-steel cluster (A53, A106, A312, A333, A335, A376, A789, A790) and is a high-priority promotion candidate by power-plant + refinery cross-reference fan-in.
- **Catalog manifest (read-only).** `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0, generated 2025-12-25) — filtered with `organization == 'ASTM' AND relative_path startswith 'ASTM/A-Series/' AND filename matches /\bA[\s_]?0*335\b/i` returns the 4 entries enumerated under *Edition history*.
- **Vendor PDFs (link-only; do NOT copy into git).** Latest edition in catalog: `/mnt/ace/O&G-Standards/ASTM/A-Series/A_335_A_335M_03_;QTMZNS9BMZM1TQ__.pdf` (2003 issue). Per spinout 2026-05-05 governance and `.claude/rules/calc-citation-contract.md` deny-list, vendor-derivative PDFs remain at their `/mnt/ace/` location and are not republished here.
- **Publisher catalog.** ASTM International — A335 / A335M product page (search "A335" at <https://www.astm.org>).
