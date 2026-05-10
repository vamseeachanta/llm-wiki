---
title: "API 579-1 / ASME FFS-1 — Fitness-For-Service"
slug: api-579-1-asme-ffs-1
code_id: api-579-1-asme-ffs-1
publisher: "API + ASME (joint)"
joint_publication: "API + ASME"
revision: "4th ed (2021); current published edition. Earlier editions: 1st (2000, issued as API RP 579), 2nd (2007, first joint API/ASME numbering), 3rd (2016)."
jurisdiction: "Joint API/ASME consensus standard for quantitative Fitness-for-Service assessment of in-service pressurised equipment; cited globally by refining, petrochemical, offshore, and pipeline owner-users; gates run/repair/replace decisions under in-service inspection codes API 510 / 570 / 653."
instrument_type: specification
supersedes: "API RP 579 (2000) — first edition issued under API-only numbering; superseded by joint API/ASME numbering from 2nd ed (2007) onward."
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
  - ./api-std-579.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/api-standard-579
tags:
  - api
  - asme
  - api-std
  - asme-ffs
  - fitness-for-service
  - ffs
  - integrity-management
  - brittle-fracture
  - crack-like-flaws
  - creep
  - joint-publication
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API 579-1 / ASME FFS-1 — Fitness-For-Service

> **Slug-canonicalisation note.** This page uses the canonical joint-numbering slug `api-579-1-asme-ffs-1`. The existing fuller treatment lives at [api-std-579](api-std-579.md) under the API-only legacy slug; both pages reference the same publisher document. Practitioners citing the joint API/ASME standard by its full designation should land here; practitioners citing the API-only short form land on [api-std-579](api-std-579.md).

> **code_id:** `api-579-1-asme-ffs-1` · **publisher:** API + ASME (joint) · **revision:** 4th ed (2021); current published edition.

## Scope

API 579-1 / ASME FFS-1 is the **joint API/ASME consensus standard for quantitative Fitness-for-Service (FFS) assessment** of in-service pressurised equipment — pressure vessels, piping, tankage, and selected pipeline components — where damage, flaws, or out-of-tolerance geometry have been identified during operation or inspection. The standard provides three tiered assessment levels: **Level 1** (screening with pre-tabulated acceptance criteria, suitable for inspector-grade evaluation), **Level 2** (engineering analysis using closed-form or simplified numeric methods), and **Level 3** (advanced analysis: detailed FEA, elastic-plastic fracture mechanics, probabilistic methods). Each damage mechanism is treated in a self-contained Part (brittle fracture, general / local metal loss, pitting, blisters / laminations, weld misalignment / shell distortion, crack-like flaws, creep, fire damage, dents / gouges) so an assessor can pick up the relevant Part without needing the full document. FFS outputs — remaining life, remaining strength factor (RSF), maximum allowable working pressure (MAWP), or accept/reject — feed directly into run / repair / replace and re-inspection-interval decisions under the in-service inspection codes ([api-510](api-510.md), [api-570](api-570.md), [api-653](api-653.md)) that gate FFS use.

## Revision history

| Edition | Year | Publisher numbering | Notes |
|---------|------|---------------------|-------|
| 1st ed | 2000 | API RP 579 | Original issue under API-only numbering |
| 2nd ed | 2007 | API 579-1 / ASME FFS-1 | First joint API/ASME numbering; major restructure into damage-mechanism Parts |
| 3rd ed | 2016 | API 579-1 / ASME FFS-1 | Expanded crack-like-flaw and creep coverage; alignment with damage mechanisms in [api-rp-571](api-rp-571.md) |
| 4th ed | 2021 | API 579-1 / ASME FFS-1 | Current published edition |

Catalog presence: 2016 (3rd ed) joint issue is on disk at `/mnt/ace/O&G-Standards/API/API_579-1_ASME_FFS-1_2016.pdf`; 2000 first edition fragments under `/mnt/ace/0000 O&G/0000 Codes & Standards/AS/API/API Recommended Practice/API RP 579/`. Current 2021 edition not on disk; obtain via API or ASME publisher catalog.

## Key sections

The headings below summarise the standard's structural backbone — clause text, screening curves, FAD diagrams, and acceptance tables are **not reproduced** per metadata-only governance.

- **Part 1 — Introduction.** Scope, organisation, terminology, units.
- **Part 2 — Engineering Assessment Procedure.** Eight-step workflow common to all damage mechanisms; Level 1 / 2 / 3 tiering; remaining-life and remediation logic.
- **Part 3 — Brittle Fracture.** MAT screening curves, Charpy exemption logic, toughness-based assessment — see [brittle-fracture](../concepts/brittle-fracture.md).
- **Part 4 — General Metal Loss.** Uniform thinning of pressure boundary; thickness-averaging methods.
- **Part 5 — Local Metal Loss.** Locally Thin Areas (LTA); river-bottom profile; Remaining Strength Factor (RSF) method.
- **Part 6 — Pitting.** Pit-couple and widely-scattered pitting; pitting charts; equivalent metal-loss treatment.
- **Part 7 — Blisters and Laminations.** Hydrogen-induced damage in carbon and low-alloy steels; HIC / SOHIC / blistering acceptance.
- **Part 8 — Weld Misalignment and Shell Distortion.** Out-of-roundness, peaking, banana / camber distortion; stress-concentration and fatigue-life effects.
- **Part 9 — Crack-like Flaws.** Failure Assessment Diagram (FAD); K-solutions; primary/secondary stress decomposition; reference-stress / Option 1, 2, 3 toughness inputs; parallel methodology to BS 7910 — see [engineering-critical-assessment](../concepts/engineering-critical-assessment.md).
- **Part 10 — Creep Damage and Creep-Fatigue.** High-temperature damage; Larson-Miller / Omega methods; damage-accumulation rules.
- **Part 11 — Fire Damage.** Heat Exposure I-VI zones; metallurgical assessment; post-fire mechanical-property degradation.
- **Part 12 — Dents, Gouges, Dent-Gouge Combinations.** Mechanical-damage assessment, primarily for pipe / pipeline components.
- **Annexes.** Stress analysis (linearisation, classification per ASME BPVC VIII-2), thickness data, residual-stress solutions, K-solutions, reference stress, fatigue curves, Charpy-to-K correlations, NDE acceptance, Compendium of Stress Intensity Factor Solutions.

## Practitioner application

API 579-1 / ASME FFS-1 is the standard cited by:
- **FFS assessors** producing remaining-life, RSF, or MAWP determinations on degraded equipment.
- **Owner-user inspectors** working under [api-510](api-510.md), [api-570](api-570.md), or [api-653](api-653.md) when inspection finds out-of-code condition that warrants quantitative engineering assessment instead of immediate repair.
- **RBI engineers** under [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) consuming FFS remaining-life outputs as POF inputs.
- **Welding engineers** invoking ECA per [engineering-critical-assessment](../concepts/engineering-critical-assessment.md) — Part 9 FAD methodology is the API-side counterpart to BS 7910.
- **Offshore structural engineers** working under [api-rp-2sim](api-rp-2sim.md) consuming FFS Part 9 crack-like-flaw assessment of fatigue cracks at tubular joints.

## Industry adoption

Universally adopted globally in refining, petrochemical, offshore, and pipeline industries as the consensus quantitative-FFS standard. Cited by US OSHA PSM auditors, EPA RMP audits, BSEE offshore-operator audits, and flag-state offshore regulators. Routinely cited in non-US jurisdictions alongside or in lieu of BS 7910; common engineering practice is to cross-check marginal Level 2 crack assessments against both standards.

## Why this page exists

W215 (iter-46) flagged the joint-numbering canonical slug `api-579-1-asme-ffs-1` as a missing first-class standards page despite heavy citation from concepts/{fitness-for-service, engineering-critical-assessment, risk-based-inspection, brittle-fracture}. This resolver provides the joint-numbering canonical entry point; the API-only legacy slug at [api-std-579](api-std-579.md) is the substantive landing page and remains canonical for citations that use the API-only short form. The joint_publication frontmatter field follows the W185 pattern for joint API/ASME standards.

## Where to find the full text

- API publisher catalog: <https://www.api.org/products-and-services/standards>
- ASME publisher catalog (FFS-1 numbering): <https://www.asme.org/codes-standards>
- Raw PDF (read-only, vendor-derivative; do NOT copy into git per spinout 2026-05-05 governance): `/mnt/ace/O&G-Standards/API/API_579-1_ASME_FFS-1_2016.pdf`
- Earlier 1st edition fragments: `/mnt/ace/0000 O&G/0000 Codes & Standards/AS/API/API Recommended Practice/API RP 579/`

## Cross-references

- [api-std-579](api-std-579.md) — API-only legacy-slug substantive page; primary content surface.
- [api-510](api-510.md) — pressure-vessel inspection code; gates FFS application for vessels.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; gates FFS application for piping.
- [api-653](api-653.md) / [api-std-653](api-std-653.md) — tank inspection code; gates FFS application for tanks.
- [api-rp-571](api-rp-571.md) — damage mechanisms; the credible-mechanism catalogue feeding FFS Part selection.
- [api-rp-572](api-rp-572.md) — pressure-vessel inspection practice; data-collection complement.
- [api-rp-578](api-rp-578.md) — PMI; verifies the alloy used in remaining-life calculations.
- [api-rp-2201](api-rp-2201.md) — hot-tapping; FFS gates hot-tap on degraded lines.
- [api-rp-2sim](api-rp-2sim.md) — offshore-structure SIM; consumes FFS Part 9 for tubular-joint crack assessment.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology; consumes FFS remaining-life outputs.
- [asme-bpvc-viii-2](asme-bpvc-viii-2.md) — design-by-analysis source for stress-classification and linearisation conventions reused by FFS-1 Annexes.
- [bs-7910](bs-7910.md) — UK FFS standard; parallel methodology for crack-like flaws (Part 9 ↔ BS 7910).
- [astm-e399](astm-e399.md) / [astm-e1820](astm-e1820.md) / [astm-e1921](astm-e1921.md) — fracture-toughness test methods feeding Part 9 toughness Options.
- [astm-a370](astm-a370.md) — Charpy-V test method feeding Part 3 brittle-fracture screening.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor; FFS workflow.
- [engineering-critical-assessment](../concepts/engineering-critical-assessment.md) — concept anchor; ECA / Part 9 FAD methodology.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor; RBI consumes FFS outputs.
- [brittle-fracture](../concepts/brittle-fracture.md) — concept anchor; Part 3 governs in-service brittle-fracture screening.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes an FFS-1 Part-specific acceptance value, RSF threshold, MAT screening curve, or FAD assessment-point coordinate.

**Cross-wiki (maritime-law)** *(where FFS methodology informs post-incident wreck-removal-decision frameworks)*

- [nairobi-wrc-2007](../../../maritime-law/wiki/standards/nairobi-wrc-2007.md) — **bidirectional bridge**: API 579-1 / ASME FFS-1 fitness-for-service methodology — Levels 1/2/3 tiered assessment, Remaining Strength Factor (RSF), Maximum Allowable Working Pressure (MAWP), remaining-life prediction, and Part 9 crack-like-flaw FAD analysis — provides the **structural-integrity decision-framework** that informs the **Nairobi WRC 2007 wreck-removal decision**: whether residual strength supports **safe relocation/refloat** vs **immediate in-place removal**. WRC Article 9 sets a coastal-state-defined "reasonable deadline" for owner-led removal; WRC Article 10 strict-liability cost-allocation is gated by the salvage/wreck-removal engineering plan, and that plan's run/repair/relocate calculus imports FFS frameworks (RSF for residual hull-girder capacity, Part 9 FAD for crack-like flaws in shell plating, Part 4/5 for general/local metal loss in wreck-affected pressure boundary). **Costa Concordia 2012** (€1.5 billion+ wreck-removal cost) used FFS-style residual-strength + structural-integrity analysis for the parbuckling-and-controlled-refloat sequence; the **MV Wakashio 2020** Mauritius wreck-removal sequence applied analogous FFS-style hull-girder-residual-capacity assessment to bow/stern-section retrieval decisions. The wreck-removal cost-benefit calculus (engineering-feasibility vs cost) shared between coastal-state authority, owner, and P&I insurer routes through FFS-grade engineering judgement — making the FFS-1 assessment doctrine a load-bearing input to the WRC liability and Wreck Removal Certificate insurance regime. Use the pairing for casualty-engineering digests that bridge in-place wreck residual-integrity assessment to WRC removal-vs-relocate liability allocation.
