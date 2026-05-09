---
title: "API Std 579-1 / ASME FFS-1 — Fitness-for-Service"
slug: api-std-579
code_id: api-std-579-asme-ffs-1
publisher: "API + ASME (joint)"
revision: "3rd ed (2016) latest in catalog; 4th ed published 2021 by API/ASME"
tags:
  - api
  - asme
  - standards
  - fitness-for-service
  - ffs
  - brittle-fracture
  - fatigue
  - creep
  - integrity-management
  - metadata-only
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/API_579-1_ASME_FFS-1_2016.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API Std 579-1 / ASME FFS-1 — Fitness-for-Service

> **code_id:** `api-std-579-asme-ffs-1` &nbsp;·&nbsp; **publisher:** API + ASME (joint) &nbsp;·&nbsp; **revision:** 3rd ed (2016) — catalog latest; 4th ed (2021) is the current published edition

## Scope

API 579-1 / ASME FFS-1 is the joint API/ASME consensus standard for quantitative
Fitness-for-Service (FFS) assessment of in-service pressurised equipment
(pressure vessels, piping, tankage) where damage, flaws, or out-of-tolerance
geometry have been detected during operation or inspection. The standard
provides three tiered assessment levels — **Level 1** (screening with
pre-tabulated acceptance criteria, suitable for inspector-grade evaluation),
**Level 2** (engineering analysis using closed-form or simplified numeric
methods), and **Level 3** (advanced analysis: detailed FEA, elastic-plastic
fracture mechanics, probabilistic methods) — applied per damage-mechanism part:
brittle fracture, general and local metal loss, pitting,
hydrogen blisters and laminations, weld misalignment / shell distortion,
crack-like flaws, creep damage, fire damage, and dents / gouges /
dent-gouge combinations. FFS outputs a remaining-life or remaining-strength
factor that informs run / repair / replace and inspection-interval decisions
under the in-service inspection codes (API 510, 570, 653) that gate its use.

## Edition history

| Edition | Year | Publisher numbering |
|---------|------|---------------------|
| 1st ed (issued as RP 579) | 2000 | API RP 579 |
| 2nd ed (joint API/ASME) | 2007 | API 579-1 / ASME FFS-1 |
| 3rd ed | 2016 | API 579-1 / ASME FFS-1 — **catalog copy** |
| 4th ed (current) | 2021 | API 579-1 / ASME FFS-1 |

> Catalog file: `/mnt/ace/O&G-Standards/API/API_579-1_ASME_FFS-1_2016.pdf` is the
> 2016 (3rd ed) joint issue. Earlier 2000 first edition is also represented
> in the catalog as a fragment set under
> `/mnt/ace/0000 O&G/0000 Codes & Standards/AS/API/API Recommended Practice/API RP 579/`
> (per-section PDFs `Sect_01.pdf` … `Sect_11.pdf` plus `Append_a.pdf` … `Append_i.pdf`).

## Key parts

FFS-1 is organised by damage mechanism. Each part defines applicability,
required input data, and the Level 1 / 2 / 3 assessment procedure for that
mechanism.

- **Part 1 — Introduction.** Scope, organisation, terminology, units.
- **Part 2 — Fitness-for-Service Engineering Assessment Procedure.** Eight-step
  assessment workflow common to all damage mechanisms; Level 1 / 2 / 3 tiering;
  remaining-life and remediation logic.
- **Part 3 — Brittle Fracture.** Minimum allowable temperature (MAT) screening
  curves, Charpy impact-energy criteria, exemption logic. Inputs: material
  toughness data per ASTM E399 / E1820 / E1921 and Charpy data per ASTM A370.
- **Part 4 — General Metal Loss.** Uniform thinning of pressure boundary;
  thickness averaging methods.
- **Part 5 — Local Metal Loss.** Localised thinning (LTA — locally thin areas);
  river-bottom profile, RSF (Remaining Strength Factor) method.
- **Part 6 — Pitting.** Pit-couple and widely-scattered pitting; pitting
  charts, equivalent metal-loss treatment.
- **Part 7 — Blisters and Laminations.** Hydrogen-induced damage in
  carbon and low-alloy steels; HIC / SOHIC / blistering acceptance.
- **Part 8 — Weld Misalignment and Shell Distortion.** Out-of-roundness,
  peaking, banana / camber distortion, weld offset; stress concentration
  and fatigue-life effects.
- **Part 9 — Crack-like Flaws.** Failure Assessment Diagram (FAD)
  methodology; stress intensity factor solutions; primary/secondary stress
  decomposition; reference stress / Option 1, 2, 3 toughness inputs;
  parallel methodology to BS 7910.
- **Part 10 — Creep Damage and Creep-Fatigue.** High-temperature damage
  (above creep threshold per material); Larson-Miller / Omega methods;
  damage-accumulation / time-fraction rules.
- **Part 11 — Fire Damage.** Heat-exposure zones (Heat Exposure I–VI),
  metallurgical assessment, post-fire mechanical-property degradation.
- **Part 12 — Dents, Gouges, and Dent-Gouge Combinations.** Mechanical
  damage; dent-only, dent + gouge, and dent + crack assessments;
  primarily applied to pipe and pipeline components.
- **Annexes.** Stress analysis (linearisation, classification per ASME
  BPVC VIII-2), thickness data, residual stress solutions, K-solutions,
  reference stress, fatigue curves, Charpy-to-K correlations, NDE
  acceptance, Compendium of Stress Intensity Factor Solutions.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher facts
(`code_id`, `publisher`, `revision`) so fail-closed citation resolution can
ground integrity-assessment outputs against this standard. **Metadata-only**
per spinout 2026-05-05 governance: no clause text, formulas, screening
curves, or FAD diagrams reproduced here.

## Where to find the full text

- Raw PDF (read-only, vendor-derivative; do NOT copy into git per #2482):
  `/mnt/ace/O&G-Standards/API/API_579-1_ASME_FFS-1_2016.pdf`
- Earlier 1st edition (per-section fragments):
  `/mnt/ace/0000 O&G/0000 Codes & Standards/AS/API/API Recommended Practice/API RP 579/`
- API publisher catalog: <https://www.api.org/products-and-services/standards>
- ASME publisher catalog (FFS-1 numbering): <https://www.asme.org/codes-standards>

## Cross-references

- **BS 7910** — *Guide to methods for assessing the acceptability of flaws
  in metallic structures* (BSI). Parallel UK FFS standard for crack-like
  flaws; FFS-1 Part 9 and BS 7910 share the FAD methodology lineage but
  differ on K-solution catalogues, residual-stress treatment, and
  reference-stress option numbering. Common practice: cross-check
  marginal Level 2 crack assessments against both.
- **ASTM E399** — Linear-elastic plane-strain fracture toughness K_Ic test.
  Input to FFS-1 Part 9 toughness Option 1.
- **ASTM E1820** — Elastic-plastic fracture toughness J_Ic / J–R curve test.
  Input to FFS-1 Part 9 toughness Option 2 / 3 (J-based).
- **ASTM E1921** — Master Curve / reference-temperature T₀ for ferritic
  steels in transition regime. Input to FFS-1 Part 3 brittle-fracture
  exemption logic.
- **ASTM A370** — Mechanical-property test methods for steel products
  (tensile, Charpy V-notch). Source of Charpy energy data feeding
  FFS-1 Part 3 MAT screening.
- **API 510** — Pressure Vessel Inspection Code (in-service). Gates FFS-1
  application for pressure vessels; FFS is invoked when 510 inspection
  finds out-of-code condition.
- **API 570** — Piping Inspection Code (in-service). Gates FFS-1
  application for process piping.
- **API 653** — Tank Inspection, Repair, Alteration, and Reconstruction.
  Gates FFS-1 application for atmospheric / low-pressure storage tanks.
- **ASME BPVC VIII Div 2** — Design-by-analysis source for the stress
  classification and linearisation conventions reused by FFS-1 Annexes.
  See [[asme-bpvc-viii-2]].
- **API RP 581** — Risk-Based Inspection Technology. Consumes FFS-1
  remaining-life outputs as the consequence/probability inputs to
  RBI interval setting.

## Sources

- Source page: [[og-standards-api]](../sources/og-standards-api.md) —
  catalog row `Std 579 / 579-1 (joint with ASME FFS-1) | Fitness-for-Service | 2007, 2016`.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json`
  (entries matching `579`).
