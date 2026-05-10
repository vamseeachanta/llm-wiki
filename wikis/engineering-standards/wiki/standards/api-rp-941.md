---
title: "API RP 941 — Steels for Hydrogen Service at Elevated Temperatures and Pressures in Petroleum Refineries and Petrochemical Plants"
slug: api-rp-941
code_id: api-rp-941
publisher: API
revision: "catalog copy: undated edition (`API_RP_941_Steels_for_Hydrogen_Service_at_Elevated_Temperatures.pdf`); current published edition is the 8th ed (2016, with subsequent reaffirmation/amendments)"
tags:
  - api
  - htha
  - high-temp-hydrogen-attack
  - nelson-curves
  - refinery
  - pressure-vessel-materials
  - hydroprocessing
  - cr-mo-steels
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_941_Steels_for_Hydrogen_Service_at_Elevated_Temperatures.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 941 — Steels for Hydrogen Service at Elevated Temperatures and Pressures in Petroleum Refineries and Petrochemical Plants

> **code_id:** `api-rp-941` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** catalog-latest copy (undated filename); 8th ed (2016, with subsequent reaffirmation/amendments) is the current published edition

## Scope

API RP 941 is the recommended practice that publishes the **Nelson curves**
— the empirical operating-window envelopes that define the
temperature × hydrogen-partial-pressure (T–pH₂) regions in which carbon
steel and the low-Cr–Mo alloy family can be used in elevated-temperature
hydrogen service without suffering **High-Temperature Hydrogen Attack
(HTHA)**. The practice specifies which alloy is qualified for which T–pH₂
window: plain carbon steel; the historical 0.5Mo carbon-Mo grade
(disqualified at 8th ed for new design); 1Cr–0.5Mo, 1.25Cr–0.5Mo,
2.25Cr–1Mo (and the V-modified 2.25Cr–1Mo–V), 3Cr–1Mo, 5Cr–0.5Mo, and
9Cr–1Mo. The standard is the foundational materials-selection reference
for **hydroprocessing units** — hydrotreater, hydrocracker,
naphtha hydrofiner, isomerization, catalytic-reforming hydrogen-recycle
loops — and for any pressure vessel, heat exchanger, or piping circuit
operating in hot hydrogen at refinery / petrochemical service
conditions.

RP 941 is the **operating-window source** that downstream programme
documents reference:

- [api-rp-571](api-rp-571.md) catalogues HTHA as a damage mechanism and points to
  RP 941 as the deep-dive reference for the Nelson-curve envelopes,
  alloy-by-alloy susceptibility, and detection guidance.
- [api-rp-581](api-rp-581.md) runs a dedicated HTHA damage-factor module (the
  POF input for RBI on hot-hydrogen circuits); RP 941's Nelson curves
  supply the safe-vs-attack boundary that the damage-factor algorithm
  evaluates at the equipment item's actual T and pH₂.
- [api-510](api-510.md) (pressure vessels) and [[api-std-570]] (piping) cite
  RP 941 as the technical reference behind in-service inspection of
  HTHA-exposed equipment, particularly for legacy 0.5Mo items.
- [api-std-579](api-std-579.md) / ASME FFS-1 Part 4 / Part 5 / Part 10 LMTD assessments
  invoke RP 941 when HTHA is the suspected mechanism for an in-service
  flaw.

RP 941 is also the substantive input behind the
[damage-mechanism-screening](../concepts/damage-mechanism-screening.md) concept page (HTHA primary reference)
and [risk-based-inspection](../concepts/risk-based-inspection.md) (Nelson-curve-based POF input for the
RP 581 HTHA damage factor).

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 4th ed | 1990 | not in catalog | Mid-life consolidation; carbon-Mo curve still treated as a first-class envelope. |
| 5th ed | 1997 | not in catalog | Editorial / curve-data updates following industry survey of in-service HTHA incidents reported through the 1990s. |
| 6th ed | 2004 | not in catalog | Further survey-data incorporation; 0.5Mo carbon-Mo curve retained but explicitly flagged as an active reassessment topic. |
| 7th ed | 2008 | not in catalog | Major revision after analysis of accumulated HTHA experience on 0.5Mo equipment; expanded inspection / detection guidance. |
| 8th ed | 2016 (with subsequent reaffirmation/amendments) | not in catalog | Definitive current edition. **Carbon-Mo (0.5Mo) curve disqualified for new construction** following the U.S. CSB analysis of the 2010 Tesoro Anacortes incident; new 2.25Cr–1Mo and 2.25Cr–1Mo–V envelopes added; advanced-UT (AUT) inspection methodology codified for in-service HTHA detection. |
| Catalog copy | undated (filename: `API_RP_941_Steels_for_Hydrogen_Service_at_Elevated_Temperatures.pdf`) | **catalog copy** | Filename does not encode an edition tag; consumers should treat the catalog copy as a historical reference and ground new design / RBI / FFS work on the publisher's current 8th edition. |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (undated filename) per the spinout's metadata-only
> policy; the **8th edition (2016)** is the publisher's current edition
> and is the appropriate citation for any new hot-hydrogen materials
> selection, RBI HTHA-damage-factor screening, or FFS assessment of
> suspected HTHA — the 8th-edition Nelson-curve set materially differs
> from pre-2016 editions in two ways that bind on calc outputs:
> (1) the carbon-Mo / 0.5Mo curve is no longer published as a
> design-qualification envelope, and (2) the V-modified 2.25Cr–1Mo–V
> envelope is a first-class alloy entry. Forward-adopt the publisher
> edition when a dated catalog copy lands.

## Key concepts

- **HTHA mechanism.** At elevated temperature in hydrogen-bearing
  service, atomic hydrogen permeates the steel and reacts with carbides
  in the microstructure to form methane (CH₄). Methane is
  insoluble in steel and accumulates at grain boundaries, generating
  internal pressure that nucleates voids; voids coalesce into fissures;
  fissures coalesce into through-thickness cracks. Damage frequently
  initiates at PWHT-degraded heat-affected zones (HAZ) where local
  carbide morphology is most susceptible, which is why HTHA failures
  typically present as brittle-mode cracking at or near welds rather
  than as uniform thinning. Initiation is driven by T and pH₂; the
  operating-window envelopes (Nelson curves) are the empirical bound
  derived from accumulated industry incident data.
- **Nelson curves — graphical convention.** Published as a family of
  alloy-specific curves with temperature on the x-axis (°F or °C) and
  hydrogen partial pressure on the y-axis (psia or MPa). For each
  alloy the curve is the experimentally-bounded envelope below which
  safe operation is supported by the industry incident record. The
  practice's design rule is: *operating point above the curve → HTHA
  risk; operating point below the curve → safe with engineering
  margin*. Vendors and licensors typically apply additional margin
  on top of the published curve; RP 941 itself states the curve as
  the survey-data envelope, not an analytic safety factor.
- **2016 8th-edition revisions (carbon-Mo and V-modified low-Cr).**
  The 8th edition removed the historical carbon-Mo (0.5Mo) curve
  from the design-qualification set for new construction following
  the post-Tesoro-Anacortes industry reassessment. Pre-2016 service
  histories in 0.5Mo equipment remain a primary in-service-inspection
  driver. The 8th edition also added a published curve for
  V-modified 2.25Cr–1Mo–V steel, recognising the alloy's superior
  HTHA resistance vs. the unmodified 2.25Cr–1Mo grade. The practical
  effect is that legacy plants with 0.5Mo equipment require an
  RBI-driven HTHA screening + materials-upgrade plan, and new
  hydroprocessor reactors increasingly specify 2.25Cr–1Mo–V over
  2.25Cr–1Mo on the same Nelson-curve basis.
- **Inspection methods.** HTHA is notoriously difficult to detect at
  early stages (sub-surface fissures, methane-void networks). RP 941
  catalogues the in-service inspection technique set: **advanced
  ultrasonic (AUT)** — phased-array UT and time-of-flight diffraction
  (TOFD) — as the primary high-resolution screening modality;
  **wet fluorescent magnetic-particle (WFMP)** for surface-breaking
  fissures at welds; and **replication metallography** (in-situ
  metallographic replicas) for microstructural confirmation. The
  combination is needed because no single technique reliably detects
  the full damage spectrum from incipient methane voids through
  through-wall cracking.

## Recent industry events

- **Tesoro Anacortes refinery, April 2010.** Catastrophic HTHA failure
  of a heat-exchanger nozzle in 0.5Mo carbon-Mo service in the
  refinery's naphtha hydrotreater unit; seven fatalities. The U.S.
  Chemical Safety Board's investigation — finalised in 2014 —
  identified the carbon-Mo alloy's published Nelson curve as
  non-conservative against the in-service incident record, and
  catalysed the 2016 8th-edition decision to remove the carbon-Mo
  envelope from the design-qualification set for new construction.
- **Operational consequence for legacy plants.** Refineries with
  pre-1990s 0.5Mo hot-hydrogen equipment — primarily early-vintage
  hydrotreaters and naphtha hydrofiners — now require an
  RBI-driven HTHA screening programme that inventories every 0.5Mo
  pressure vessel, heat exchanger, and piping circuit; ranks each
  item against current operating T and pH₂ vs. the 8th-edition
  Nelson framework (with carbon-Mo treated per the post-2016
  guidance); and maintains an inspection or upgrade-replacement
  plan keyed to the RBI POF estimate. The RP 581 HTHA damage factor
  is the quantitative engine for the ranking step.

## Cross-references

- **API RP 571 — Damage Mechanisms Affecting Fixed Equipment in the
  Refining Industry.** Catalogues HTHA as a damage mechanism within
  the uniform / localised metal-loss family and points to RP 941 as
  the deep-dive technical reference. RP 571 is the catalogue;
  RP 941 is the operating-window source. See [api-rp-571](api-rp-571.md).
- **API RP 581 — Risk-Based Inspection Methodology (quantitative).**
  Operates a dedicated HTHA damage-factor module; RP 941's Nelson
  curves supply the safe-vs-attack envelope that the damage-factor
  algorithm consults at each equipment item's operating T and pH₂.
  RP 941 is the POF input; RP 581 is the RBI computation. See
  [api-rp-581](api-rp-581.md).
- **API 510 — Pressure Vessel Inspection Code.** In-service
  inspection code for pressure vessels; cites RP 941 as the
  technical reference behind HTHA-aware inspection planning for
  hot-hydrogen pressure vessels (hydroprocessor reactors,
  hydrotreater feed-effluent exchangers, recycle compressors'
  associated drums). See [api-510](api-510.md).
- **API 570 — Piping Inspection Code.** In-service inspection code
  for process piping; cites RP 941 as the technical reference for
  HTHA-aware piping inspection in hydroprocessing circuits
  (reactor effluent piping, hydrogen-recycle piping, hot-feed lines).
  See [[api-std-570]].
- **API 579-1 / ASME FFS-1 — Fitness-for-Service.** When HTHA is the
  suspected mechanism for an in-service flaw, the FFS-Part-selection
  workflow invokes RP 941 alongside RP 571: Part 4 (general metal
  loss) and Part 5 (local metal loss) for thickness-based assessment
  of HTHA-thinned components; Part 10 (creep and high-temperature
  operation) for the long-term-mean-temperature and damage-driven
  remaining-life arguments most relevant to HTHA. See [api-std-579](api-std-579.md).
- **ASME BPVC Section II Part D — Materials Properties (allowable
  stresses).** Provides the design allowable-stress tables that
  pressure-vessel and piping codes consume. RP 941's hot-hydrogen
  alloy qualification operates in parallel with II-D's
  temperature-derated allowable stresses: II-D constrains the
  pressure-design envelope, RP 941 constrains the materials-selection
  envelope; both must be satisfied for hot-hydrogen service.
- **Nelson 1948 (historical foundation).** G. A. Nelson's 1948
  bulletin compiling refinery industry HTHA incident data was the
  original survey-derived envelope from which the modern RP 941
  curves descend. The Nelson 1948 bulletin and its mid-century
  successors are public-domain historical references; RP 941 is the
  current, industry-maintained, edition-versioned successor.
- **Damage-mechanism screening (concept).** RP 941 is the named
  primary reference for the HTHA mechanism in the screening
  workflow. See [damage-mechanism-screening](../concepts/damage-mechanism-screening.md).
- **Risk-Based Inspection (concept).** RP 941 is the operating-window
  source whose Nelson curves the RP 581 HTHA damage factor consults
  during quantitative POF estimation. See [risk-based-inspection](../concepts/risk-based-inspection.md).

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground hot-hydrogen-service materials-selection,
HTHA-screening, and Nelson-curve-derived calc outputs against this
practice. It also serves as the named link target from
[api-rp-571](api-rp-571.md) (damage-mechanism catalogue), [api-rp-581](api-rp-581.md) (RBI HTHA
damage factor), [api-510](api-510.md) / [[api-std-570]] (in-service inspection
codes), [api-std-579](api-std-579.md) (FFS HTHA assessments), and the
[damage-mechanism-screening](../concepts/damage-mechanism-screening.md) / [risk-based-inspection](../concepts/risk-based-inspection.md) concept
pages. **Metadata-only** per spinout 2026-05-05 governance: no Nelson
curve data, alloy-by-alloy T–pH₂ envelope tables, susceptible-grade
lists, inspection-procedure recipes, or post-incident-survey case
data are reproduced here.

## Where to find the full text

- Catalog copy (read-only, vendor-derivative; do NOT copy into git per
  spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_941_Steels_for_Hydrogen_Service_at_Elevated_Temperatures.pdf`
    — undated catalog copy; ground new work on the publisher's 8th
    edition (2016, with subsequent reaffirmation/amendments).
- API publisher catalog: <https://www.api.org/products-and-services/standards>

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  catalog rows matching `API RP 941`.
- Catalog provenance: on-disk copy at the path above under
  `/mnt/ace/O&G-Standards/API/Recommended-Practice/`. Filename does
  not encode an edition tag; treat the publisher 8th edition (2016)
  as the binding revision for new design / RBI / FFS work.
- Historical foundation: G. A. Nelson, *Steels for Hydrogen Service
  at Elevated Temperatures and Pressures in Petroleum Refineries and
  Petrochemical Plants* (industry bulletin, 1948 and successors) —
  the public-domain survey-data origin of the modern Nelson curves.
