---
title: "API RP 574 — Inspection Practices for Piping System Components"
slug: api-rp-574
code_id: api-rp-574
publisher: API
revision: "catalog latest is 2nd ed (1998); current published edition is 4th ed (2016)"
tags:
  - api
  - piping-inspection
  - ndt
  - cml
  - ut-thickness
  - rbi-input
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_574_(1998).pdf
  - /mnt/ace/O&G-Standards/API/Specifications/API_574_RP_Inspection_Practices_for_Piping_System_Components_(1998).pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 574 — Inspection Practices for Piping System Components

> **code_id:** `api-rp-574` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** catalog holds 1998 (2nd ed) copies; current published edition is 4th ed (2016). 3rd ed published 2009.

## Scope

API RP 574 is the **inspector-grade practice companion** to [[api-570]] (the
piping inspection code). It documents recommended practices for the
**inspection methods and frequencies** applied to the components that make up
process piping systems — straight pipe, valves, flanges, fittings, bolting,
supports and hangers, expansion joints, flexible hose, and the welded
joints that connect them. Where API 570 is the **owner-user code** that
sets policy (classification, intervals, who is responsible), RP 574 is the
**field-execution practice guide** that tells inspectors and NDE examiners
how to actually find wall loss, cracking, and mechanical damage on those
components.

The recommended practice covers, in particular: NDE method selection
(visual external/internal, UT thickness, RT, MT, PT, eddy current, AET
acoustic-emission, IR thermography); CML (Condition Monitoring Location)
selection on a piping circuit; thickness-measurement protocols (UT spot
versus scan, comparison against retiring thickness `T_min`, statistical
sampling for buried piping); the choice between **off-stream** (shutdown,
piping isolated and depressurized) and **on-stream** (live, with personnel
protection requirements) inspection windows; and the **content of the
inspection report** that records findings against API 570 acceptance
criteria. RP 574 is **not** a code — it cannot be invoked as a compliance
authority on its own; it is invoked **through** API 570, API 510, or the
owner-user's written inspection programme.

## Edition history

| Edition | Year | Status / catalog presence |
|---------|------|----------------------------|
| 1st ed | 1990 | Original issue (not in catalog) |
| 2nd ed | 1998 | Catalog: `API_RP_574_(1998).pdf` and `API_574_RP_Inspection_Practices_for_Piping_System_Components_(1998).pdf` |
| 3rd ed | 2009 | Major revision — expanded NDE method coverage and CML guidance (not in catalog) |
| 4th ed | 2016 | Current published edition (not in catalog) |

> **Catalog vs. published.** The catalog under `/mnt/ace/O&G-Standards/API/`
> holds only 2nd-ed (1998) copies. The current published edition (4th ed,
> 2016) is API's normative reference and should be cited directly from the
> publisher for any compliance-grade assessment. Practitioners working
> against the catalog edition should expect material gaps in modern NDE
> coverage (PAUT, guided-wave UT, pulsed eddy current for through-insulation
> screening) versus 3rd / 4th ed text.

## Key sections

The headings below summarise the practice's structural backbone — clause
text, NDE acceptance tables, and CML-spacing tabulations are **not
reproduced** per metadata-only governance.

- **Inspection types.** RP 574 enumerates the inspection modalities used
  on piping components and the situations each is appropriate for:
  - **Visual inspection** — external (insulation status, supports,
    coatings, leakage, mis-alignment, vibration evidence) and internal
    (where access permits — valves, large-bore manifolds, exchanger
    piping during T/A).
  - **Ultrasonic thickness (UT)** — the workhorse for general wall-loss
    monitoring; spot readings at CMLs and area scans where localised
    thinning is suspected.
  - **Radiographic testing (RT)** — profile RT for thinning detection
    on small-bore piping and through-insulation imaging on insulated
    runs; weld RT for fabrication and repair verification.
  - **Magnetic-particle (MT) and liquid-penetrant (PT)** — surface and
    near-surface flaw detection on welds, fittings, and dressed
    repair sites.
  - **Eddy-current testing (ET)** — surface cracking on non-magnetic
    alloys, heat-exchanger tubes, and through-insulation screening
    (pulsed ET).
  - **Acoustic-emission testing (AET)** — global-coverage screening for
    actively growing flaws under controlled pressurisation; flags
    locations for follow-up UT/RT.
  - **Infrared (IR) thermography** — refractory degradation,
    insulation under-jacket water ingress (CUI screening), and
    process flow-pattern verification.

- **CML selection.** Condition Monitoring Locations are the points on a
  piping circuit where wall thickness is measured on a recurring schedule
  per API 570 intervals. RP 574's CML-selection guidance prioritises:
  - **High-corrosion zones** flagged by the corrosion-control document
    or process-corrosion model,
  - **Dead legs** (stagnant accumulation, microbial corrosion under
    deposits),
  - **Injection points** (chemical injection, water washing, additive
    or steam injection — turbulent local mixing produces a downstream
    erosion-corrosion zone typically extending 12 pipe diameters),
  - **Soil-air interfaces** (atmospheric corrosion at coating
    transitions, accelerated by chloride and moisture),
  - **Mixing tees** (flow-induced and thermal-fatigue cracking at the
    branch radius),
  - **Pump-discharge T-junctions** and other **velocity-elevated
    zones** (cavitation, flow-induced erosion),
  - **Insulation-jacketing transitions and supports** (CUI risk).

- **Thickness-measurement protocols.** RP 574 distinguishes:
  - **UT spot readings** at fixed CMLs — repeatable point measurement,
    trended across inspections to derive long-term and short-term
    corrosion rates per API 570.
  - **UT area scans** — used when spot readings flag thinning, to
    bound the extent of the affected zone and locate the minimum
    remaining wall.
  - **`T_min` comparison** — measured thickness compared against the
    retiring thickness derived from the construction code's
    pressure-design equation (B31.3 etc.); excursion below `T_min`
    triggers the API 570 → API 579-1 fitness-for-service gate.
  - **Statistical sampling for buried piping** — where excavation cost
    precludes 100% coverage, a representative sample of dig-and-inspect
    points combined with above-grade techniques (close-interval
    potential survey, guided-wave UT, IR for shallow burial) supports
    a defensible remaining-life assessment.

- **Off-stream vs. on-stream inspection.** Off-stream inspection (T/A
  windows) provides full access for internal visual, RT setup, and
  bolted-joint disassembly; on-stream inspection (live piping) covers
  the longer span between turnarounds and is constrained by personnel
  protection, hot-surface access, and through-insulation methods. CML
  scheduling balances both windows.

- **Interval-setting.** Two routes are sanctioned:
  - **Table-based intervals** per API 570 piping-classification ceilings
    and the half-remaining-life rule, or
  - **Risk-based intervals** per [[api-rp-580]] / [[api-rp-581]].
  RP 574 supplies the inspection-method effectiveness inputs that the
  RBI study consumes — see *Inspection-effectiveness factors* below.

- **Inspection-effectiveness factors A–E.** RP 574 underpins the
  effectiveness scoring used by API 581 RBI: a **Highly Effective (A)**
  inspection identifies expected damage with high probability across
  the susceptible inventory; **Usually Effective (B)**, **Fairly
  Effective (C)**, and **Poorly Effective (D)** scale down with
  reduced coverage, less-sensitive method, or partial CML count;
  **Ineffective (E)** corresponds to no useful damage information.
  Method selection (UT spot vs. scan vs. AUT, MT vs. WFMP, RT vs.
  PAUT) and coverage fraction together determine the letter grade,
  which in turn shrinks (or fails to shrink) the RBI probability of
  failure.

- **Inspection report content.** RP 574 prescribes the minimum content
  of the inspection record: circuit identification, drawing reference,
  CML map and thickness readings, NDE method and procedure used,
  inspector and examiner identification with certifications, findings
  against API 570 acceptance criteria, photographs and sketches of
  significant findings, and recommended follow-up actions
  (re-inspection interval, repair, FFS routing).

## Special-equipment guidance

RP 574 attaches inspection focus to the dominant degradation mechanism
for each component class. The table below summarises the practice-grade
guidance used by inspectors when planning a circuit walk-down.

| Component | Typical mechanisms | Inspection focus |
|-----------|-------------------|------------------|
| Straight pipe runs | General corrosion + erosion at bends | UT thickness on outside-bend extrados |
| Dead legs | Stagnant accumulation + microbial corrosion (MIC) | Targeted UT + flush sampling |
| Injection points | Localised erosion-corrosion downstream of the injection nozzle | Downstream UT scan within 12 pipe diameters |
| Mixing tees | Flow-induced + thermal-fatigue cracking at the branch radius | UT + WFMP at branch radii |
| Pump suction / discharge | Cavitation + erosion + vibration-induced fatigue | Vibration monitoring + UT |
| Buried piping | External soil-side corrosion + coating breakdown | Excavation + IR + GBT-equivalent (guided-wave / close-interval potential) |
| Soil-air interfaces | Atmospheric + galvanic corrosion at coating transitions | Visual + UT below grade after coating removal |
| Insulated runs (CUI risk) | Corrosion under insulation at jacket joints / supports | Pulsed eddy current + IR + selective insulation removal |
| Valves | Internal erosion of trim, body wall thinning at high-velocity ports | Internal visual at T/A + UT body-wall |
| Flanged joints + bolting | Bolt corrosion, gasket creep, flange-face wear | Visual + bolt MT + flange-face inspection at disassembly |

## Cross-references

- **[[api-570]]** — *Piping Inspection Code* (parent code). RP 574 is
  the inspector-grade practice guide invoked by API 570 to execute the
  inspection programme that API 570 mandates.
- **[[api-rp-580]]** — *Risk-Based Inspection*. Methodology framework
  for the RBI alternative to table-based intervals; consumes RP 574's
  inspection-effectiveness factors A–E.
- **[[api-rp-581]]** — *Risk-Based Inspection Methodology*. Quantitative
  RBI calculation that grounds probability-of-failure on RP 574 method
  effectiveness and CML coverage inputs.
- **[[api-rp-571]]** — *Damage Mechanisms Affecting Fixed Equipment in
  the Refining Industry*. The damage-mechanism catalogue that RP 574's
  CML and method-selection guidance maps against (which mechanism is
  expected → which NDE method finds it).
- **[[api-510]]** — *Pressure Vessel Inspection Code*. Sibling code;
  RP 572 is the analogous practice guide for vessels (pressure-vessel
  inspection), with the same RP 574 ↔ API 570 relationship.
- **[[api-653]]** — *Tank Inspection, Repair, Alteration, and
  Reconstruction*. Sibling inspection code for atmospheric storage
  tanks.
- **[[api-std-579]]** — *API 579-1 / ASME FFS-1, Fitness-for-Service*.
  Invoked when RP 574 thickness measurements show `T_min` excursion
  on a CML that API 570 categorises as out-of-code; the FFS standard
  produces the quantitative remaining-life and re-inspection
  determination.
- **[[corrosion-rate-measurement]]** — concept-page consumer; RP 574
  specifies the CML thickness-measurement methods (UT spot vs. scan,
  RT profile, frequency, statistical sampling) that feed long-term
  and short-term corrosion-rate calculations.
- **[[risk-based-inspection]]** — concept-page consumer; RP 574
  supplies the inspection-effectiveness factor inputs (A–E) that the
  RBI methodology under API 580/581 turns into probability-of-failure
  reductions.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground piping-integrity outputs (CML thickness reads,
inspection-effectiveness scores, T_min excursion flags) against this
practice. **Metadata-only** per spinout 2026-05-05 governance: no
clause text, NDE acceptance tables, or CML-spacing tabulations
reproduced here.

## Where to find the full text

- Raw PDFs (read-only, vendor-derivative; do NOT copy into git per #2482):
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_574_(1998).pdf` — 2nd ed (1998)
  - `/mnt/ace/O&G-Standards/API/Specifications/API_574_RP_Inspection_Practices_for_Piping_System_Components_(1998).pdf` — 2nd ed (1998), filename-variant copy
- Publisher catalog: <https://www.api.org/products-and-services/standards>
- Practitioner usage: invoked through API 570 inspection programmes; not
  cited as a standalone compliance authority.

## Sources

- Source page: [[og-standards-api]](../sources/og-standards-api.md) — catalog
  row `RP 574 | Inspection Practices for Piping System Components | (2 editions)`
  per the inspection-RP cluster (`510, 570, 572, 574, 576, 578, 580, 581, 582`).
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` — entries
  `API/Recommended-Practice/API_RP_574_(1998).pdf` and
  `API/Specifications/API_574_RP_Inspection_Practices_for_Piping_System_Components_(1998).pdf`.
