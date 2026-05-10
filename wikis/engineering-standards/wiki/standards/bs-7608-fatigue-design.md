---
title: "BS 7608 — Fatigue Design and Assessment of Steel Products"
slug: bs-7608-fatigue-design
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - bsi
  - standards
  - fatigue
  - sn-curves
  - weld-classification
  - palmgren-miner
  - structural
  - metadata-only
sources:
  - /mnt/local-analysis/workspace-hub/llm-wiki/wikis/engineering-standards/wiki/sources/og-standards-bsi.md
  - /mnt/ace/O&G-Standards/_catalog.json
code_id: bs-7608
publisher: BSI
publisher_full: "British Standards Institution"
revision: "2014"
jurisdiction: UK / international
extraction_policy: metadata-only
raw_copy_allowed: false
bs_doc_number: "BS 7608"
ledger_id: BS-7608
---

# BS 7608 — Guide to Fatigue Design and Assessment of Steel Products

**code_id:** `bs-7608` &nbsp;·&nbsp; **publisher:** BSI (British Standards Institution) &nbsp;·&nbsp; **revision:** 2014 — latest edition present in catalog.

> Bounded metadata page. Vendor PDFs do not enter this repo per spinout 2026-05-05 governance — only publisher facts (titles, document IDs, revision years, on-disk paths) are recorded here. Cite the publisher edition for normative use.

## Scope

BS 7608 is BSI's flagship guide for **S-N-based fatigue design and assessment of steel products**, including welded and non-welded details. Originally written to support the offshore oil-and-gas and structural-steel industries during the 1980s/1990s North Sea expansion, the standard has since been **widely adopted for non-pressure components** in cranes, bridges, lifting equipment, transmission towers, wind-turbine support structures, and general fabricated steelwork.

The guide covers:

- **S-N (Wöhler) curve methodology** for assessing fatigue endurance under constant- and variable-amplitude loading — based on nominal-stress, hot-spot-stress (structural-stress), or notch-stress approaches as appropriate to the detail.
- **Weld-detail classification** — every common welded joint geometry is binned into a discrete class (B, C, D, E, F, F2, G, W) that selects the applicable S-N curve. Curves are derived as **mean-minus-two-standard-deviations** of the underlying fatigue test database (~2.3% probability of failure on the design curve).
- **Mean-stress and stress-range treatment** — for as-welded joints the **stress-range-only basis** is used (welds carry tensile residual stress at yield, so mean stress is implicitly bounded); for stress-relieved or non-welded details a **maximum-stress / R-ratio correction** is permitted.
- **Plate thickness correction** — for plate thicknesses greater than 25 mm a thickness penalty `(t/25)^0.25` (or detail-specific exponent) is applied to the stress range, reflecting the size-effect on fatigue endurance.
- **Partial safety factors** — design factor on life (γ<sub>f</sub>) and factor on stress (γ<sub>s</sub>) calibrated to the consequence of failure and accessibility for inspection.
- **Palmgren-Miner linear damage accumulation** — variable-amplitude rainflow histograms summed via D = Σ(n<sub>i</sub>/N<sub>i</sub>) ≤ 1 (or a lower target for safety-critical details); guidance on stress-range cut-off below the constant-amplitude fatigue limit (CAFL).
- **Corrosion-fatigue knock-down** — distinct treatment for **in-air**, **seawater with adequate cathodic protection (CP)**, and **seawater free-corrosion** environments; CP curves typically apply a factor of ~2 reduction in life vs. air, free-corrosion removes the endurance limit entirely.

## Edition history

| Edition | Year | Catalog file | parent_root |
|---|---|---|---|
| 1993 (original) | 1993 — `Fatigue design & assessment of steel structures` (titled as Code of Practice in this lineage) | `BSI/BS_7608_(1993)_Fatigue_design_&_assessment_of_steel_structures.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 1993 with 1995 Amendment | 1993+1995 — same edition incorporating Amendment 1 | `BSI/BS_7608_(1993_with_1995_Amend)_Code_of_Practice_for_Fatigue_Design_and_Assessment_of_Steel_Structures.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| (untitled-revision file variant) | revision unspecified — alternate on-disk copy archived under `Spare/BSI Standards/` | `BSI/BS7608.pdf` | `/mnt/ace/O&G-Standards/BSI` |
| 2014 | 2014 — major revision; broadens title from "*… Steel Structures*" to "*… Steel Products*", incorporates updated weld-class data, refined thickness-correction exponents, and aligned partial-safety-factor framework | `BSI/BS_7608-2014.pdf` | `/mnt/ace/O&G-Standards/BSI` |

Notable lineage notes:

- The **1993** edition was issued as a **Code of Practice** with the scope "*Fatigue design and assessment of steel structures*". The **2014** revision broadened the scope title to "*… Steel Products*", reflecting wider non-structural adoption (lifting gear, machinery, transmission components).
- BS 7608 is one of the foundational data sources for the Eurocode 3 EN 1993-1-9 fatigue annex; the two share a common heritage via the European Convention for Constructional Steelwork (ECCS) fatigue working groups.

## Key sections / classes

The 2014 edition's normative structure covers the following working surfaces for downstream calc modules:

- **Weld-detail classes B → W.** Each joint geometry (plain plate, butt weld, transverse-load-carrying fillet, longitudinal-load-carrying fillet, cruciform, T-joint, weld-toe vs. weld-throat failure) maps to a **discrete class**:
  - **Class B** — highest endurance — plain machined / un-notched parent material.
  - **Class C** — automatic-process butt welds in plate, ground flush.
  - **Class D** — transverse butt welds, full-penetration, weld toe-failure.
  - **Class E** — load-carrying butt welds with backing strip / partial penetration.
  - **Class F** — fillet welds, weld-toe failure under transverse loading.
  - **Class F2** — fillet welds with greater stress-concentration severity.
  - **Class G** — non-load-carrying attachments and cruciform fillet welds.
  - **Class W** — load-carrying fillet welds where the weld throat is the failure path (failure mode is throat-shear rather than toe-bending).
- **S-N curve form.** Curves are bilinear log-log: a constant-amplitude fatigue limit (CAFL) at 10<sup>7</sup> cycles separates a higher-slope (m ≈ 3) finite-life regime from a lower-slope (m ≈ 5) variable-amplitude / cut-off regime. Design curves are **mean-minus-2σ** (~97.7% survival probability).
- **Stress basis.** *As-welded joints*: **stress range only** — welds carry tensile residual stresses at yield, so applied compressive minima do not reduce the effective range. *Stress-relieved or non-welded details*: maximum-stress R-ratio corrections permitted per the standard's tabulated rules.
- **Thickness correction.** For plate thicknesses *t* > 25 mm a stress-range correction `Δσ_corrected = Δσ_applied · (t/25)^k` is applied with **k ≈ 0.25** (default); detail-specific exponents are tabulated for selected joint classes.
- **Partial safety factors.** Design endurance life is computed as `N_design = N_curve / γ_f` with a complementary factor `γ_s` on the applied stress range. The (γ<sub>f</sub>, γ<sub>s</sub>) pair is selected from a matrix indexed by **consequence of failure** (low/medium/high) and **accessibility for inspection** (accessible/inaccessible).
- **Palmgren-Miner damage summation.** For variable-amplitude loading a rainflow stress-range histogram is summed as `D = Σ (n_i / N_i)` with target **D ≤ 1.0** (often reduced to 0.5 or lower for safety-critical or inaccessible details). Guidance is given for treating stress ranges below the CAFL — typically a slope-extension is applied rather than the cycles being discarded entirely.
- **Corrosion-fatigue environments.** Three environment cases are codified: **in-air**, **seawater with adequate cathodic protection (CP)**, and **seawater free-corrosion**. The seawater-CP curves apply a knock-down (~factor 2 on life) vs. in-air; the free-corrosion curves additionally **remove the endurance limit**, so all stress ranges contribute to damage indefinitely.

> Class letters and curve constants are normative within BS 7608:2014; verify against the publisher edition for normative work.

## Comparison with peers

BS 7608 sits at the centre of a family of S-N-based fatigue codes for steel:

| Code | Scope emphasis | Differentiator vs. BS 7608 |
|---|---|---|
| **[dnv-rp-c203](dnv-rp-c203.md)** — Fatigue design of offshore steel structures | Offshore platforms, jackets, risers, semi-submersibles | More granular weld-class set; **explicit seawater-with-CP and free-corrosion S-N curves** as separate published curves rather than environment factors; integrated hot-spot-stress / SCF library; default reference for North Sea offshore practice |
| **[aws-d1-1](aws-d1-1.md)** — Structural Welding Code (Steel) | US structural steel fabrication (buildings, bridges) | **Less classification depth** — fewer joint categories; fatigue provisions in Chapter 2 reference **AASHTO/AISC fatigue categories A–E′** rather than BS letter classes; in-air only (no marine environment treatment) |
| **[api-rp-2a-wsd](api-rp-2a-wsd.md)** — Fixed offshore platforms (WSD) | Offshore fixed-platform jackets | Fatigue annex uses **API X / X′ S-N curves** for tubular joints; thickness correction with API-specific exponent; closely aligned with BS 7608 conceptually but with platform-tubular focus |
| **EN 1993-1-9 (Eurocode 3, Fatigue)** | EU/CEN structural steel — buildings, bridges, towers | CEN-aligned counterpart to BS 7608; uses **detail-category numbers (e.g. 160, 140, 125, 112, 100, 90, 80, 71, 63, 56, 50, 45, 40, 36)** instead of BS letter classes — the number is the Δσ at 2×10<sup>6</sup> cycles in MPa. Fatigue test database and methodology are largely shared with BS 7608 (common ECCS heritage). |

The dominant practitioner choice is jurisdiction-driven: **DNV-RP-C203** for North Sea offshore, **API RP 2A-WSD** for Gulf-of-Mexico fixed platforms, **BS 7608** for UK / EU general steel fabrication and non-pressure components, **EN 1993-1-9** for CEN-mandated structural projects, and **AWS D1.1** for US structural construction.

## Cross-references

- [dnv-rp-c203](dnv-rp-c203.md) — DNV recommended practice for fatigue design of offshore steel structures; **parallel to BS 7608** with explicit seawater curves and a more granular tubular-joint classification. Practitioners often cross-validate BS 7608 results against DNV-RP-C203 for offshore applications.
- [api-rp-2a-wsd](api-rp-2a-wsd.md) — API RP 2A WSD fatigue annex for offshore platform tubular joints; uses API X / X′ S-N curves (BS 7608's structural counterpart for fixed-platform jacket fatigue).
- [api-std-1104](api-std-1104.md) — API 1104 pipeline construction code; **Annex A** (Alternative Acceptance Standards for Girth Welds) provides ECA-route fatigue assessment for pipeline girth welds — methodologically overlapping with BS 7608 for the linepipe segment.
- [bs-7910-flaw-assessment](bs-7910-flaw-assessment.md) — BS 7910's **Annex M** (fatigue crack growth) provides the fracture-mechanics counterpart to BS 7608's S-N approach; the two are **complementary** — BS 7608 is preferred for design assessment of typical details, BS 7910 Annex M is preferred where a known flaw size or crack-growth history exists.
- [aws-d1-1](aws-d1-1.md) — US structural welded-steel code with an in-air-only fatigue annex; less classification depth than BS 7608 but governs US-jurisdiction fabrications.
- **EN 1993-1-9** — Eurocode 3 Part 1-9 (Fatigue), the CEN-aligned counterpart to BS 7608. Detail-category numbers (160, 140, …, 36) are numerically the Δσ at 2×10<sup>6</sup> cycles; the underlying fatigue database is largely shared via the ECCS heritage. Cited in parallel for projects with both UK and CEN deliverables.

## Sources

- [og-standards-bsi](../sources/og-standards-bsi.md) — BSI publisher catalog page summarising the BSI slice of `/mnt/ace/O&G-Standards/`, including all on-disk BS 7608 edition variants.
- Catalog source: `/mnt/ace/O&G-Standards/_catalog.json` (catalog version 1.0.0).
- Publisher: BSI Knowledge — https://knowledge.bsigroup.com/ (search `BS 7608`).
- Calc-citation contract: `.claude/rules/calc-citation-contract.md` (workspace-hub) — governs how downstream digitalmodel calc modules emit `Citation` instances against this page.

## Notes

- This page is **metadata-only**; no clause text, figure, table, or S-N curve constant is reproduced from the BS 7608 PDFs. All technical descriptions above are paraphrased general engineering knowledge.
- For normative fatigue assessment work, cite the BSI-published edition directly (BS 7608:2014 or the current edition at time of citation).
- BS 7608 is **not** a pressure-equipment fatigue code — pressurised components should additionally be assessed under ASME BPVC VIII Div 2 Part 5, EN 13445-3 Clause 18, or PD 5500 Annex C as applicable.
- Concept-page consumers: [`concepts/fatigue-design-and-assessment.md`](../concepts/fatigue-design-and-assessment.md) and [`concepts/welding-procedures-and-acceptance.md`](../concepts/welding-procedures-and-acceptance.md) cross-reference this page for normative S-N-curve and weld-class background.
