---
title: "ASME B31.1 — Power Piping"
slug: asme-b31-1
tags: ["asme", "b31", "power-piping", "boiler-piping", "steam", "allowable-stress"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-b31-1
publisher: ASME
revision: "2007"
revision_source: "/mnt/ace/O&G-Standards/ASME/BS/ASME.B31.1.2007.pdf"
publisher_current_edition: "2024 (B31.1-2022 + most recent addenda; ~3-yr revision cycle)"
methodology_status: stale-as-of-publisher-cycle
verified_on: 2026-05-09
public_url: https://www.asme.org/codes-standards/find-codes-standards/b31-1-power-piping
sources:
  - /mnt/ace/O&G-Standards/ASME/BS/ASME.B31.1.2007.pdf
  - wikis/engineering-standards/wiki/sources/og-standards-asme.md
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links:
  - ../concepts/welding-procedures-and-acceptance.md
  - ../concepts/fatigue-design-and-assessment.md
  - ../concepts/creep-and-stress-rupture.md
  - asme-b31-3.md
---

# ASME B31.1 — Power Piping

> Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source PDF — publisher facts only.

## Scope

ASME B31.1 governs design, materials, fabrication, examination, testing, and operation of **steam-and-water systems** in fossil-fuel power-generation service and the non-nuclear-safety balance-of-plant of nuclear-power generating stations. The code addresses pressure piping that connects boilers, turbines, condensers, feedwater heaters, deaerators, heat-recovery steam generators, and the associated auxiliary systems within a power-station boundary.

The application domain distinguishes B31.1 from its sibling [ASME B31.3](asme-b31-3.md): power piping is the boiler-and-turbine envelope, while B31.3 covers process piping in petroleum refineries, chemical plants, and pharmaceutical facilities. Pipeline-transportation services (B31.4 liquids, B31.8 gas), refrigeration (B31.5), building services (B31.9), and hydrogen piping (B31.12) sit in their own B31 sections.

## Edition history

ASME B31.1 revises on an approximate three-year cycle. Editions present in the catalog and in the publisher's recent stream:

| Edition | Status |
|---------|--------|
| B31.1-2007 | Catalog copy on disk (`/mnt/ace/O&G-Standards/ASME/BS/ASME.B31.1.2007.pdf`) |
| B31.1-2014 | Superseded |
| B31.1-2018 | Superseded |
| B31.1-2020 | Superseded |
| B31.1-2022 | Most recent at publisher (verified via the public catalog URL above) |

Calc callers should treat the on-disk 2007 revision as **stale-as-of-publisher-cycle**: allowable-stress tables, branch-reinforcement rules, and weld examination categories have all received targeted edits across the 2014–2022 stream. The cross-cutting methodology backbone (pipe wall-thickness, expansion-stress range, support spacing, hydrotest acceptance) is structurally stable across editions but specific factors and tabulated values are not.

## Key sections

The 2007 table-of-contents structure (representative; not a clause-by-clause excerpt):

- **Materials** — listed materials and the link to ASME BPVC Section II Part D for allowable stresses across the temperature range, including the creep range.
- **Pressure design — straight pipe** — wall-thickness sizing under internal pressure (the Lamé / Barlow-style formulation tailored to the code's Y-coefficient and weld-joint efficiency `E`).
- **Pressure design — components** — branch reinforcement (area-replacement method), bends, miters, reducers, and flanges.
- **Flexibility & support** — expansion-stress range method (the B31.1 stress-range envelope, including SIFs and stress-intensification factors `i`), allowable-displacement stress, and tabulated support spacing for typical pipe sizes.
- **Valves and specialty components** — pressure-temperature ratings, safety and relief device requirements (cross-link to ASME OM-E2004 for in-service relief).
- **Fabrication, assembly, erection** — weld-end preparation, preheat and PWHT requirements, alignment tolerances.
- **Welding** — welding procedure qualification by reference to ASME BPVC Section IX, performance qualification, and code-specific filler-metal restrictions.
- **Examination** — visual, MT, PT, RT, UT acceptance criteria by category of fluid service and pressure class.
- **Hydrotest and leak test** — required test pressure, hold time, and acceptance.
- **Operation and maintenance** — in-service inspection requirements (less prescriptive than API 510 for vessels or API 570 for process piping, but mandated for the power-piping boundary; supplemental guidance from ASME OM stream).

## B31.1 vs. B31.3

The two sibling codes diverge most visibly in the categories of fluid service, the conservatism of the allowable-stress basis, and the granularity of stress-intensification factors:

| Aspect | B31.1 (power) | B31.3 (process) |
|--------|---------------|-----------------|
| Service envelope | Boiler + turbine + steam systems within a power station | Refining, petrochemical, chemical, pharmaceutical |
| Allowable-stress basis | Higher (smaller margin to UTS/yield) | Lower (more conservative) |
| Component categories | None — single set of rules across the code's scope | Category D / Normal / Category M (toxic) / High Pressure |
| Stress-intensification factors | Code-tabulated `i` per fitting type | Code-tabulated, more granular (and a more developed link to ASME B31J) |
| Expansion-stress method | Stress-range method | Stress-range method (parallel formulation) |
| Creep-range coverage | Yes — allowables drawn from BPVC II-D, including the [time-fraction creep approach](../concepts/creep-and-stress-rupture.md) referenced in the NB / B31.1 long-term-strength tables | Yes — same II-D source, applied within process-piping envelope |
| Welding qualification | BPVC Section IX | BPVC Section IX |
| In-service inspection | Code-mandated within power-piping boundary | Process-piping in-service governed by API 570 (B31.3 covers original construction and re-rating) |

The shared substrate is BPVC Section II Part D (allowable stresses) and BPVC Section IX (welding qualification); the divergence is in service domain and the resulting code-specific tables.

## Cross-references

- [ASME B31.3](asme-b31-3.md) — process piping sibling
- ASME B31.4 — liquid pipelines (transportation)
- ASME B31.5 — refrigeration piping
- ASME B31.8 — gas transmission and distribution
- ASME B31.9 — building services piping
- ASME B31.12 — hydrogen piping and pipelines
- ASME BPVC Section II Part D — allowable-stress source for all B31 codes
- ASME BPVC Section IX — welding and brazing qualification basis
- ASME BPVC Section I — Power Boilers (the boiler outlet is the B31.1 inlet; together they form the power-station pressure boundary)
- NB-23 (National Board Inspection Code) — companion in-service inspection / repair / alteration document for boiler and pressure-piping populations
- API RP 941 — high-temperature hydrogen attack (HTHA); cross-cutting concern for high-temperature B31.1 piping in hydrogen service
- Concept consumers in this wiki:
  - [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md)
  - [fatigue-design-and-assessment](../concepts/fatigue-design-and-assessment.md)
  - [creep-and-stress-rupture](../concepts/creep-and-stress-rupture.md) (B31.1 NB-3221 time-fraction creep approach)

## Sources

- Catalog source page: [og-standards-asme](../sources/og-standards-asme.md) — ASME slice metadata, 88 documents, B31.1 entry on the topical coverage map.
- Publisher catalog: https://www.asme.org/codes-standards/find-codes-standards/b31-1-power-piping (verify current edition before citing).
- Raw PDF (vendor-derivative; metadata-only extraction per spinout governance): `/mnt/ace/O&G-Standards/ASME/BS/ASME.B31.1.2007.pdf`. Do not copy into this repo.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` (workspace-hub) — defines how `digitalmodel` Citation instances resolve to this page.
