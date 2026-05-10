---
title: "ASME B31.3 — Process Piping (bounded summary)"
tags: ["asme", "standards", "piping", "metadata-only"]
added: 2026-05-02
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-b31-3
publisher: ASME
revision: "2012"
revision_source: "/mnt/ace/O&G-Standards/ASME/ASME B31.3 - Process Piping/ASME B31.3 2012 - Processing Piping.pdf"
publisher_current_edition: "2024/2026 cycle"
methodology_status: "stale-as-of-publisher-cycle"
verified_on: 2026-05-02
public_url: https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping
sources:
  - /mnt/ace/O&G-Standards/ASME/ASME B31.3 - Process Piping/ASME B31.3 2012 - Processing Piping.pdf
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASME B31.3 — Process Piping (bounded summary)

## Scope

ASME B31.3 governs design, materials, fabrication, examination, and testing for piping systems carrying process fluids in petroleum refineries, chemical plants, pharmaceutical, textile, paper, semiconductor, and cryogenic-process plants and related installations. It establishes minimum engineering requirements for pressure piping outside the boiler and pipeline-transportation scopes covered by other B31 sections, and is the workhorse code for process-plant interconnect, process-unit-internal piping, utility piping, and balance-of-plant pressure piping in onshore and topsides-offshore process facilities.

## B31 family scoping

B31.3 is one section of the ASME B31 *Code for Pressure Piping* family. Section selection is by service:

- **B31.1 — Power Piping.** Steam, condensate, boiler-feedwater, BOP-steam-and-water for electric-utility and industrial power-plant applications. Higher allowable-stress design margin and a stricter examination basis than B31.3; selected when the piping is downstream of a Section I boiler.
- **B31.3 — Process Piping.** Refinery, petrochem, chemical, pharma, semiconductor, cryogenic — the present page.
- **B31.4 — Pipeline Transportation Systems for Liquids and Slurries.** Crude, refined products, NGLs, anhydrous ammonia, slurries — pipeline-transportation scope outside plant fences.
- **B31.5 — Refrigeration Piping and Heat Transfer Components.** HVAC chilled-water, refrigerant, and heat-transfer-fluid piping; small-diameter low-pressure scope.
- **B31.8 — Gas Transmission and Distribution Piping Systems.** Natural-gas pipeline-transportation outside plant fences; companion to B31.4 on the gas side.
- **B31.9 / B31.11 / B31.12** — building-services, slurry-transportation, hydrogen-piping companions.

The B31.3-vs-B31.1 boundary inside a plant is the conventional fence between the steam-utility scope (B31.1) and the process scope (B31.3); the B31.3-vs-B31.4 / B31.8 boundary is the plant-fence (in-plant = B31.3, transportation = B31.4 / B31.8).

## Revision history

- **B31.1 origin (1935)** — The original *Code for Pressure Piping* covered all pressure-piping scopes in one document.
- **B31.3 separation (1959)** — Process Piping (then numbered ANSI B31.3) carved out from the unified B31 code as the refining-and-chemical-plant scope grew distinct.
- **B31.3-1980** — First post-ANSI ASME-branded edition of the modern Process Piping scope.
- **Three-year publication cycle (1980s–2010s)** — Editions issued on roughly a three-year cadence (1996, 1999, 2002, 2004, 2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022).
- **2012 — On-disk artifact edition.** The reference revision held in the catalog.
- **2018 — B31J coupling.** ASME B31J (*Stress Intensification Factors for Metallic Piping Components*) was incorporated as the mandatory SIF basis, replacing the legacy Appendix-D chart approach in subsequent editions; B31.3 calls B31J directly for SIF and flexibility-factor data on the post-2018 cycle.
- **2024 / 2026 cycle** — Currently active publisher edition; the on-disk 2012 SIF chart approach is approximately 14 years stale and the SIF methodology is now B31J-based rather than Appendix-D-chart-based.

The on-disk 2012 artifact lags the publisher's currently active 2024 / 2026 cycle. Calc callers MUST treat the on-disk 2012 SIF approach as **stale-as-of-publisher-cycle** and confirm the citing calc is not silently relying on the retired Appendix-D-chart methodology.

## Key sections

B31.3 is organised as a part-and-chapter structure:

- **Chapter I — Scope and Definitions** — applicability, fluid-service categories, designer responsibility.
- **Chapter II — Design** — design conditions, design criteria, pressure design of components (Part 2: cylindrical, branch reinforcement, blanks, bolted-flange joints), flexibility analysis (Part 3: thermal-expansion stress, displacement-stress range, allowable stress range), pipe supports (Part 4), specific piping systems (Part 5: jacketed, instrument).
- **Chapter III — Materials** — listed and unlisted materials, low-temperature requirements (Charpy-V impact-test exemption curves, often referencing the ASME Section II Part D framework), high-temperature requirements, severe-cyclic materials.
- **Chapter IV — Standards for Piping Components** — dimensional standards (ASME B16 family), materials standards (ASTM cross-references), bolting standards.
- **Chapter V — Fabrication, Assembly, and Erection** — welding, brazing, soldering, bending and forming, heat treatment, joint preparation.
- **Chapter VI — Inspection, Examination, and Testing** — inspection-vs-examination distinction, examination percentages by fluid-service category, NDE technique selection, leak-testing.
- **Chapter VII — Nonmetallic Piping** — separate framework for thermoplastic, thermoset, and lined piping.
- **Chapter VIII / IX / X (Service-specific chapters)** — Category-M (severe-toxic), High-Pressure, and High-Purity scope expansions on the base Chapter II–VI rules.
- **Mandatory and Non-Mandatory Appendices** — allowable-stress tables (Appendix A), required references, sample calculations, listed-component dimensions, severe-cyclic notes.

## Fluid-service categories

B31.3 sorts piping into fluid-service categories, each with its own examination percentage and design-rule modifiers:

- **Normal Fluid Service** — the default scope; the bulk of refinery / petrochem / chemical-plant piping.
- **Category D Fluid Service** — non-flammable, non-toxic, non-damaging service operating below specific pressure / temperature thresholds (relaxed examination).
- **Category M Fluid Service** — severe-toxic service (single exposure to a small quantity capable of causing serious irreversible harm); stricter examination, materials, leak-testing, and design margin.
- **Severe Cyclic Service** — service in which displacement-stress range or operating-cycle count produces fatigue exposure beyond the Normal range; tighter design + examination requirements.
- **High-Pressure Fluid Service** — Chapter IX scope; service above the conventional Normal-pressure ceiling, with its own fatigue and fracture-mechanics requirements.
- **High-Purity Fluid Service** — Chapter X scope; semiconductor, pharmaceutical, and high-purity-process piping with internal-surface-finish, weld-protrusion, and dead-leg controls.

The choice of fluid-service category is a **designer responsibility** — the code does not assign category by fluid alone — and drives examination percentage, leak-testing requirement, and material acceptance.

## Examination requirements

B31.3 distinguishes between **inspection** (owner / authorised-inspector verification that the work meets the code) and **examination** (NDE applied to specific welds and components by qualified personnel). The required examination set spans:

- **Visual examination** — 100% of accessible welds in most categories; the baseline acceptance technique.
- **Radiographic testing (RT)** — film or digital radiography of butt welds; required percentage rises with fluid-service category (Normal: percentage spot RT; Severe Cyclic and Category M: full RT).
- **Ultrasonic testing (UT)** — phased-array UT (PAUT) and time-of-flight diffraction (TOFD) are increasingly accepted in lieu of RT under the post-2010 editions.
- **Magnetic-particle examination (MT)** — surface and near-surface flaws on ferromagnetic materials.
- **Liquid-penetrant examination (PT)** — surface flaws on non-ferromagnetic and ferromagnetic materials when MT is impractical.
- **Hardness testing** — required on PWHT'd carbon-steel and low-alloy welds in specified services.

The examination percentage by category (5%, 10%, 100%) is the mechanism by which fluid-service severity scales the as-built confidence in weld integrity.

## Flexibility analysis

Flexibility analysis is the B31.3 design check that the piping accommodates **thermal-expansion stress** and **displacement-stress range** without overloading components or supports. The analysis evaluates:

- **Displacement-stress range `S_E`** vs the allowable stress range `S_A` (a function of cold-allowable, hot-allowable, and operating-cycle count `N`).
- **Sustained stresses** (weight + pressure) vs the hot-allowable stress.
- **Occasional stresses** (wind, seismic, slug, surge) under the occasional-load allowance.
- **Stress Intensification Factors (SIFs)** at fittings, branch connections, and welded geometries — historically from Appendix D charts, now from ASME B31J on the post-2018 cycle.
- **Flexibility factors `k`** that scale bending-element stiffness for elbows, miters, and bends.
- **Pipe-support spacing, support type** (rigid, spring-can, constant-effort), and **anchor / restraint placement** to control thermal-expansion movement and protect connected equipment-nozzle loads against API 610 (pump), API 617 (compressor), API 660 (heat-exchanger), and similar nozzle-load limits.

Pipe-support engineering is the practical companion: B31.3 defines the stress-acceptance criteria; the pipe-support standard (MSS-SP-58, MSS-SP-69, MSS-SP-89) and the operator's pipe-support spec govern the hardware selection.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source. Downstream callers wire B31.3 stress-check constants through this page rather than parsing the source PDF. The on-disk revision lags the publisher's currently active 2024/2026 cycle by approximately 14 years; the methodology for Stress Intensification Factor (SIF) calculation changed across that gap (the simplified Appendix-D chart approach is no longer the mandatory route in the current cycle, having been superseded by an ASME B31J based method). Calc callers MUST treat the on-disk 2012 SIF approach as stale-as-of-publisher-cycle and confirm the citing calc is not silently relying on the retired methodology.

## Where to find the full text

- Raw PDF: `/mnt/ace/O&G-Standards/ASME/ASME B31.3 - Process Piping/ASME B31.3 2012 - Processing Piping.pdf` (read-only, vendor-derivative; do not copy into git per #2482)
- Publisher catalog: https://www.asme.org/codes-standards/find-codes-standards/b31-3-process-piping
- Internal callers: `digitalmodel/src/digitalmodel/` modules referencing `ASME B31.3` / `ASMEB313` symbols (process-piping stress checks)

## Cross-references

- [[asme-bpvc-ii-d]] — allowable stresses sourced upstream
- [[asme-bpvc-ix]] — welding qualification basis
- [[asme-b16-5]] — flange-rating cross-link
- [[asme-b31j]] — SIF and flexibility-factor data set (post-2018 mandatory replacement for legacy Appendix-D charts)
- [[asme-bpvc-viii-1]] — pressure-vessel design-by-rule companion at the inlet / outlet vessel-nozzle boundary
- [[api-std-570]] — process-piping in-service inspection code that uses B31.3 as the new-construction basis and authorises RBI per RP 580 / RP 581 for alternative inspection intervals
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)

## Cross-wiki bridges

- [IGC Code](../../../lng-projects/wiki/standards/igc-code.md)
  (lng-projects) — **bidirectional bridge**: ASME B31.3 is the
  process-piping substrate-code that the IGC Code imports by reference
  for hydrocarbon-process piping aboard gas carriers. IGC Chapter 5
  (Process Pressure Vessels and Liquid, Vapour, and Pressure Piping
  Systems) and Chapter 7 (Cargo Pressure / Temperature Control) flow
  cargo-handling and reliquefaction-plant piping design pressures,
  classifications, and stress-analysis requirements into B31.3 (and
  B31.5 for refrigeration-circuit piping); IGC Ch.16 (Use of Cargo as
  Fuel) extends the same delegation to LNG-fuelled main-engine fuel
  gas piping. Cargo-tank cryogenic loading + vapor-return + spray-line
  piping on LNG/LPG carriers consume B31.3 SIF, allowable-stress, and
  flexibility-analysis rules through this delegation. Class-society
  gas-carrier rules (ABS, DNV, LR, BV, ClassNK) implement IGC by
  invoking B31.3 for the auxiliary and cargo-piping scope rather than
  publishing parallel piping rules.
- [IBC Code](../../../lng-projects/wiki/standards/ibc-code.md)
  (lng-projects) — **bidirectional bridge**: ASME B31.3 is also the
  process-piping substrate code for the IMO IBC Code (Construction and
  Equipment of Ships Carrying Dangerous Chemicals in Bulk), the
  chemical-tanker counterpart to the IGC Code. IBC Chapter 5 (Cargo
  Transfer — piping, manifolds, cargo pumps, segregation between
  incompatible cargoes) and Chapter 7 (Cargo Temperature Control) import
  B31.3 by reference for chemical-tanker cargo-handling, heating, and
  cooling piping in the same way that IGC Chapters 5 and 7 do for
  liquefied-gas carriers. The IBC + IGC parallel — both invoking B31.3
  as the substrate process-piping code — is the engineering reason
  class-society chemical-tanker rules (ABS, DNV, LR, BV, ClassNK, KR,
  RINA, CCS) do not publish parallel piping methodologies. Severe-toxic
  Type-1 chemical-tanker cargoes (Chapter 17 categorisation) typically
  trigger Category-M Fluid Service under B31.3, raising examination
  percentage to 100 %, narrowing material-acceptance criteria, and
  imposing stricter leak-testing — a delegation IBC Chapter 6 (Materials
  of Construction) and Chapter 14 (Personnel Protection) consume rather
  than re-derive. Use this pairing when authoring chemical-tanker
  cargo-piping FFS, RBI, or new-construction reviews where IBC ship-type
  drives the B31.3 fluid-service category.
