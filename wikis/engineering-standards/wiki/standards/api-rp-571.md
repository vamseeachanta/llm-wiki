---
title: "API RP 571 — Damage Mechanisms Affecting Fixed Equipment in the Refining Industry"
slug: api-rp-571
code_id: api-rp-571
publisher: API
revision: "1st ed (2003) — catalog latest; 3rd ed (2020, with subsequent reaffirmation/amendments) is the current published edition"
tags:
  - api
  - damage-mechanisms
  - refining-corrosion
  - htha
  - sulfidation
  - rbi-input
  - integrity-management
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_571_1st_Ed_(2003)_Damage_Mechanisms_Affecting_Fixed_Equipment_in_the_Refining_Industry.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 571 — Damage Mechanisms Affecting Fixed Equipment in the Refining Industry

> **code_id:** `api-rp-571` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** 1st ed (2003) — catalog latest; 3rd ed (2020) is the current published edition

## Scope

API RP 571 is the recommended-practice **catalogue of damage mechanisms**
encountered in fixed equipment in refining and petrochemical service —
pressure vessels, piping, heat exchangers, fired heaters, reactors,
storage tanks, and associated process equipment. For each mechanism the
practice provides a consistent technical entry covering description,
susceptible materials, critical operating and environmental factors,
appearance and morphology of damage, prevention and mitigation options,
inspection and monitoring techniques, and related mechanisms.

RP 571 is **methodology-free**: it is a reference compendium, not a
programme document. It does not prescribe how to prioritise inspection,
how to compute risk, or how to set inspection intervals. Instead it is
the **technical-content anchor** that downstream programme documents
reference:

- [[api-rp-580]] (qualitative RBI) names RP 571 in its damage-mechanism
  identification step.
- [[api-rp-581]] (quantitative RBI) builds its damage-factor models on
  the mechanisms catalogued here.
- [[api-std-579]] / ASME FFS-1 cross-references RP 571 mechanism
  descriptions when characterising the flaw type that drives a
  fitness-for-service assessment.
- The in-service inspection codes [[api-510]] (pressure vessels),
  [[api-std-570]] (piping), and [[api-std-653]] (storage tanks) cite
  RP 571 as the technical reference behind their damage-mechanism
  awareness requirements.

RP 571 is also the substantive input that supports the [[risk-based-inspection]]
concept page (mechanism catalogue feeding screening) and
[[corrosion-rate-measurement]] (typical rate ranges and morphology
guidance per mechanism).

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 1st ed | 2003 | **catalog copy** (`API_RP_571_1st_Ed_(2003)_Damage_Mechanisms_Affecting_Fixed_Equipment_in_the_Refining_Industry.pdf`) | Inaugural edition; established the per-mechanism technical-entry template and the family-level grouping that subsequent editions retained. |
| 2nd ed | 2011 | not in catalog | Expanded mechanism roster (additional cracking and high-temperature mechanisms); revised susceptible-materials and critical-factor sections; aligned cross-references with the API 581 2nd-edition (2008) damage-factor models. |
| 3rd ed | 2020 (with subsequent reaffirmation/amendments) | not in catalog | Current published edition; further expanded HTHA guidance after the post-Tesoro-Anacortes industry reassessment of carbon-steel HTHA susceptibility, and re-aligned with the API 581 3rd-edition (2016) quantitative methodology. |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (1st ed, 2003) per the spinout's metadata-only policy;
> the 3rd edition (2020) is the publisher's current edition and is the
> appropriate citation for new RBI, FFS, or inspection work — particularly
> for any HTHA-related screening, where the 3rd-edition guidance materially
> updates carbon-steel susceptibility treatment relative to the 2003
> Nelson-curve framing. Forward-adopt the publisher edition when a more
> recent catalog copy lands.

## Damage-mechanism catalogue

RP 571 organises mechanisms into families. The grouping below is the
functional structure used across editions; specific section numbering
shifts between the 1st, 2nd, and 3rd editions and the mechanism roster
expands edition-over-edition.

| Family | Representative mechanisms |
|--------|---------------------------|
| **Mechanical / metallurgical** | Brittle fracture, mechanical fatigue, thermal fatigue, creep and stress rupture, dissimilar-metal weld (DMW) cracking, refractory damage, temper embrittlement, 885 °F (475 °C) embrittlement, sigma-phase embrittlement, spheroidisation, graphitisation. |
| **Uniform / localised metal loss** | Galvanic corrosion, erosion and erosion-corrosion, oxidation, **sulfidation** (high-temperature S attack, with and without H2), **high-temperature hydrogen attack (HTHA)** governed by the Nelson curves, **corrosion-under-insulation (CUI)**, microbiologically-influenced corrosion (MIC), soil-side corrosion. |
| **High-temperature corrosion** | Naphthenic-acid corrosion (NAC), fuel-ash corrosion, metal dusting, decarburisation, carburisation, nitriding. |
| **Environmentally-assisted cracking** | Chloride stress-corrosion cracking (Cl-SCC) of austenitic stainless steel, caustic SCC, amine SCC, polythionic-acid SCC (PASCC), carbonate SCC, ammonia SCC, sulfide SCC, hydrogen blistering, hydrogen-induced cracking (HIC) and stress-oriented HIC (SOHIC) — the latter overlapping with sour-service damage covered by [[ampp-mr-0175-pt1]]. |
| **Aqueous corrosion** | CO2 (sweet) corrosion, H2S sour-service aqueous corrosion, dew-point corrosion (acid-dewpoint, water-dewpoint), atmospheric corrosion, cooling-water corrosion. |

The catalogue is the substrate that downstream programmes screen against:
RP 580's per-item *active damage-mechanism list* is built by walking the
RP 571 catalogue against the materials, process, and operating-history
data for a given equipment item.

## Format

Each mechanism in RP 571 follows a consistent technical-entry template.
The template structure is invariant across mechanisms and editions and is
the feature that makes RP 571 usable as a screening reference rather than
as ad-hoc literature:

1. **Description** — physical and chemical mechanism; what is happening
   to the metal.
2. **Materials affected** — alloy families and specific grades known to
   be susceptible.
3. **Critical factors** — temperature, partial pressures, fluid
   composition, stress state, time, microstructure / heat-treatment, weld
   metallurgy, and other variables that govern initiation and rate.
4. **Affected units or equipment** — where in the refinery the mechanism
   typically appears (e.g., crude unit overhead, FCC reactor, hydroprocessing
   reactor effluent, sour-water stripper, amine regenerator).
5. **Appearance or morphology of damage** — what the as-found damage
   looks like at scale (uniform thinning, pitting, cracking pattern,
   bulging, scaling, blistering) — the inspection-evidence side of the
   mechanism.
6. **Prevention and mitigation** — materials selection, process control,
   chemical injection, design change, monitoring, operational limits.
7. **Inspection and monitoring** — recommended techniques (UT, RT, MT,
   PT, ECT, AET, replication, hardness traversing) with an indication of
   effectiveness for the mechanism's morphology — the input that anchors
   RP 580 inspection-effectiveness grading.
8. **Related mechanisms** — cross-references to other RP 571 entries
   when mechanisms co-occur, compete, or are commonly confused.
9. **References** — pointer to publisher, NACE/AMPP, ASTM, and academic
   literature underlying the entry.

The template is what allows an RBI team or FFS analyst to compare two
candidate mechanisms (e.g., HTHA vs creep, or Cl-SCC vs PASCC) on the
same axes, rather than re-deriving the comparison from primary literature
each time.

## Cross-references

- **API RP 580 — Risk-Based Inspection (qualitative).** Names RP 571 as
  the damage-mechanism reference invoked during RBI screening and POF
  estimation. RP 580 is the methodology, RP 571 is the technical content.
  See [[api-rp-580]].
- **API RP 581 — Risk-Based Inspection Methodology (quantitative).**
  Builds its damage-factor models (thinning DF, SCC DF, HTHA DF, brittle-
  fracture DF, fatigue DF, etc.) on the mechanism descriptions in
  RP 571. See [[api-rp-581]].
- **API 510 — Pressure Vessel Inspection Code.** In-service inspection
  code for pressure vessels; cites RP 571 as the technical reference for
  damage-mechanism identification underlying inspection planning. See
  [[api-510]].
- **API 570 — Piping Inspection Code.** In-service inspection code for
  process piping; cites RP 571 as the technical reference for damage-
  mechanism identification. See [[api-std-570]].
- **API 653 — Tank Inspection, Repair, Alteration, and Reconstruction.**
  In-service inspection code for atmospheric / low-pressure storage
  tanks; cites RP 571 (with the bottom-side / soil-side and CUI
  mechanisms most relevant for tanks). See [[api-std-653]].
- **API 579-1 / ASME FFS-1 — Fitness-for-Service.** RP 571's per-mechanism
  morphology and critical-factor descriptions feed the FFS Part selection:
  Part 3 (brittle fracture), Part 4 (general metal loss), Part 5 (local
  metal loss), Part 6 (pitting), Part 7 (blisters and HIC/SOHIC),
  Part 8 (weld misalignment / shell distortion), Part 9 (crack-like
  flaws — Cl-SCC, caustic SCC, amine SCC, PASCC, sulfide SCC),
  Part 10 (creep and high-temperature operation, including HTHA),
  Part 11 (fire damage), Part 12 (dent / gouge / dent-gouge),
  Part 13 (laminations), Part 14 (fatigue). See [[api-std-579]].
- **AMPP/NACE MR0175 — Sour-service materials.** Overlaps with the RP 571
  sour-service damage entries (sulfide SCC, HIC, SOHIC) on the materials-
  selection side. See [[ampp-mr-0175-pt1]] / [[ampp-mr-0175-pt2]] /
  [[ampp-mr-0175-pt3]].
- **Risk-Based Inspection (concept).** RP 571 is the named damage-
  mechanism catalogue input behind the qualitative-and-quantitative RBI
  workflow. See [[risk-based-inspection]].
- **Corrosion-rate measurement (concept).** RP 571 surfaces typical
  rate ranges, governing factors, and morphology guidance per mechanism;
  these are the inputs against which CML thinning trends are interpreted.
  See [[corrosion-rate-measurement]].
- **Pitting and crevice corrosion (concept).** Several RP 571 entries
  (Cl-SCC pit-initiation, MIC, under-deposit attack) are the source
  material for the morphology and susceptibility content on
  [[pitting-and-crevice-corrosion]].

## Cross-wiki bridges

- [MARPOL 73/78](../../../maritime-law/wiki/standards/marpol-73-78.md)
  (maritime-law) — **bidirectional bridge**: API RP 571's damage-
  mechanism catalogue (corrosion, cracking, erosion, mechanical and
  high-temperature mechanisms) is the technical-content reference for
  MARPOL incident-investigation root-cause analysis on tanker hull,
  cargo-tank, and slop-tank failures. MARPOL **Annex I (oil)** and
  **Annex II (noxious liquid substances in bulk)** inspection regimes
  — particularly the IOPP/NLS certificate survey programme and the
  double-hull tanker fitness-for-service evaluation under MEPC.95(46)
  — overlap directly with RP 571 entries for sour-water corrosion,
  CO2 corrosion, sulfide stress cracking, naphthenic-acid corrosion,
  microbiologically-influenced corrosion (MIC), and erosion-corrosion
  in cargo-handling and ballast-water circuits. Cargo-tank atmospheric
  corrosion under Annex I crude-oil-washing residues, Annex II
  category-X/Y prewash-cycle attack on tank linings, and slop-tank
  bottom-side MIC are the highest-frequency RP 571 mechanism hits in
  the casualty record (Erika 2000, Prestige 2002, Hebei Spirit 2007
  all involved hull-integrity damage mechanisms catalogued in RP 571).
  Use this pairing when authoring incident-investigation digests that
  bridge regulatory non-conformance findings to mechanism-level
  metallurgical evidence.
- [LNG Process Safety](../../../lng-projects/wiki/concepts/lng-process-safety.md)
  (lng-projects) — **bidirectional bridge**: API RP 571's damage-
  mechanism catalogue is the technical-content reference for LNG
  incident-investigation root-cause analysis whenever a hazard
  scenario on the LNG-process-safety page (RPT, rollover-driven
  relief-system overpressure, cryogenic-shock secondary-barrier
  brittle fracture, vapour-cloud-dispersion ignition, BOG-compressor
  rapid-cycling fatigue) is traced back to a fixed-equipment failure
  mode. Highest-yield mechanism mappings: cryogenic-shock + warm-cold
  cycling on 9 % Ni inner tanks (RP 571 brittle-fracture and thermal-
  fatigue entries — feeding the FFS-Part-3/Part-14 selection); BOG
  compressor and reliquefaction skid mechanical and thermal fatigue
  (mechanical-fatigue + thermal-fatigue entries); cryogenic-piping
  cold-spot CUI on warm-cold cycling sections (CUI entry); amine-unit
  caustic SCC on acid-gas-removal trains feeding the liquefaction
  cold box (caustic-SCC + amine-SCC entries); flare-tip and waste-heat-
  recovery oxidation / sulfidation on regen-gas circuits (oxidation +
  sulfidation entries). LNG operators applying API RP 580 / 581 RBI to
  liquefaction-train fixed equipment consume the RP 571 catalogue
  through the same screening logic refining operators use; the
  process-safety hazard-scenario list on the lng-projects page is the
  *consequence-side* counterpart that closes the loop between mechanism
  catalogue, RBI screening, and QRA frequency aggregation. Use this
  pairing when authoring liquefaction-train RBI plans, FERC / EN 1473
  Resource Reports that need mechanism-level credibility for the
  fixed-equipment leak-frequency inputs, or post-incident root-cause
  reports that must reconcile regulator findings with metallurgical
  evidence.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground refining-damage-mechanism-derived screening,
materials-selection, and rate-band outputs against this practice. It
also serves as the technical-content anchor for [[api-rp-580]] /
[[api-rp-581]] RBI screening, the FFS-Part-selection cross-reference
for [[api-std-579]], and the link target from the [[risk-based-inspection]]
and [[corrosion-rate-measurement]] concept pages.
**Metadata-only** per spinout 2026-05-05 governance: no clause text,
mechanism descriptions, susceptible-materials lists, critical-factor
tables, morphology images, prevention/mitigation prescriptions,
inspection-technique recipes, or rate-range tables are reproduced here.

## Where to find the full text

- Catalog copy (read-only, vendor-derivative; do NOT copy into git per
  spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_571_1st_Ed_(2003)_Damage_Mechanisms_Affecting_Fixed_Equipment_in_the_Refining_Industry.pdf`
    — 1st edition (catalog latest)
- API publisher catalog: <https://www.api.org/products-and-services/standards>

## Sources

- Source page: [[og-standards-api]](../sources/og-standards-api.md) —
  catalog rows matching `API RP 571` (1st ed 2003).
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` (entry
  `id: 27199`, `organization: API`, `doc_type: RP`, `doc_number: 571`);
  on-disk copy enumerated in the *Where to find the full text* section
  above.
