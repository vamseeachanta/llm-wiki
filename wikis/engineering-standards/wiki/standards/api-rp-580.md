---
title: "API RP 580 — Risk-Based Inspection"
slug: api-rp-580
code_id: api-rp-580
publisher: API
revision: "2nd ed (2009) — catalog latest; 3rd ed (2016, reaffirmed/amended) is the current published edition"
tags:
  - api
  - rbi
  - qualitative
  - integrity-management
  - inspection-prioritization
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Specifications/API_RP_580_1st_Ed_(2002)_Risk-Based_Inspection.pdf
  - /mnt/ace/O&G-Standards/API/Specifications/API_RP_580_2nd_Ed_(2009)_Risk-Based_Inspection.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 580 — Risk-Based Inspection

> **code_id:** `api-rp-580` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** 2nd ed (2009) — catalog latest; 3rd ed (2016) is the current published edition

## Scope

API RP 580 is the recommended practice that defines the minimum content of a
**qualitative** Risk-Based Inspection (RBI) programme for fixed equipment in
process plants — pressure vessels, piping, atmospheric and low-pressure
storage tanks, pressure-relief devices, and heat exchangers. It is the
methodology and framework document: it specifies *what an RBI programme must
contain* (team, scope, data, screening, POF/COF estimation, risk ranking,
inspection planning, re-evaluation) without prescribing the numerical
algorithms used to compute probability and consequence. The companion
document [api-rp-581](api-rp-581.md) supplies the **quantitative** implementation —
specific damage-mechanism probability models, COF release-and-impact
calculations, and risk-matrix scoring tables — that satisfies the RP 580
framework for owner-users who choose a quantitative route.

API RP 580 is the **methodology gate** that authorises in-service inspection
codes to substitute risk-derived intervals for table-based intervals: it is
explicitly named as the alternative-interval route in [api-510](api-510.md) (pressure
vessels), [api-std-570](api-std-570.md) (piping), and [api-std-653](api-std-653.md) (storage tanks).
A risk-based interval that does not flow from an RP 580-conformant programme
is not a sanctioned interval under those codes. RP 580 does not itself
authorise inspection — the host code (510 / 570 / 653) does — but it is the
upstream methodology constraint on the host code's RBI route.

RP 580 is **methodology-only** and does not address: design-by-rule
construction (ASME BPVC), fitness-for-service disposition of as-found
findings (which is delegated to [api-std-579](api-std-579.md) when RBI surfaces flaws),
or damage-mechanism technical content (which is referenced out to
[api-rp-571](api-rp-571.md)).

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 1st ed | 2002 | **catalog copy** (`API_RP_580_1st_Ed_(2002)_Risk-Based_Inspection.pdf`) | Inaugural edition; established the qualitative RBI framework and the 12-element minimum-content list. |
| 2nd ed | 2009 | **catalog copy** (`API_RP_580_2nd_Ed_(2009)_Risk-Based_Inspection.pdf`) | Catalog latest; tightened team-competency requirements and added inspection-effectiveness category guidance (A–E). |
| 3rd ed | 2016 (with subsequent reaffirmation/amendments) | not in catalog | Current published edition; aligned with the API 581 3rd-edition (2016) quantitative methodology and updated cross-references to API 510/570/653 RBI clauses. |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (2nd ed, 2009) per the spinout's metadata-only policy;
> the 3rd edition (2016) is the publisher's current edition and is the
> appropriate citation for new RBI work. Forward-adopt the publisher edition
> when a more recent catalog copy lands.

## Key sections

API RP 580 is organised around the **minimum content of an RBI programme**
rather than around specific algorithms. The functional structure below is
consistent across editions; section numbers shift between the 1st, 2nd, and
3rd editions.

### Minimum RBI programme elements

RP 580 enumerates the elements that an RBI programme must contain in order
to be conformant. The list is commonly summarised as twelve elements:

1. Management systems for maintaining documentation, personnel
   qualifications, data requirements, and analysis updates.
2. Documented RBI methodology selection (qualitative, quantitative, or
   semi-quantitative) and stated assumptions.
3. Scope-of-study definition (boundary, equipment list, time horizon).
4. Data and information collection (design, operating, inspection,
   maintenance, process, damage history).
5. Damage-mechanism identification and screening (referencing
   [api-rp-571](api-rp-571.md)).
6. Probability-of-failure (POF) estimation per damage mechanism.
7. Consequence-of-failure (COF) estimation across release scenarios and
   impact categories.
8. Risk determination (POF × COF on a documented matrix or numerical scale).
9. Risk management (acceptance criteria, mitigation alternatives,
   inspection-plan development).
10. Inspection planning (technique, coverage, frequency, effectiveness
    target).
11. Other risk-mitigation activities beyond inspection (process change,
    metallurgy upgrade, monitoring, equipment replacement).
12. Re-assessment, documentation, and roles & responsibilities (closing
    the loop on plan execution and drift).

### Team competencies

RP 580 requires a multi-disciplinary RBI team. Minimum competencies named
in the practice are:

- **Corrosion / materials engineer** — damage-mechanism identification,
  rate estimation, susceptibility screening.
- **Inspection specialist** — inspection-history interpretation,
  technique selection, effectiveness grading.
- **Process / operations engineer** — process-condition history, upset
  exposure, operating-window awareness.
- **Plant operator** — field knowledge of as-installed configuration,
  past leaks, monitoring access, and operational reality versus design
  intent.
- **RBI facilitator / analyst** — methodology custodian, data integrator,
  analysis owner.
- **Risk-analyst / engineer (for quantitative routes)** — POF and COF
  modelling per [api-rp-581](api-rp-581.md) when the quantitative route is selected.

The team requirement is structural: a single-discipline RBI exercise (a
corrosion engineer running RBI without inspection or operations input) is
non-conformant under RP 580.

### Data quality requirements

RP 580 makes data quality a first-class programme element. Required data
classes include design and construction records (drawings, MDR, materials,
PWHT history), operating data (pressures, temperatures, flow regimes,
upset history), process-fluid composition and contaminants (water, H2S,
chlorides, amines, sulphur, naphthenic acids), inspection history (CML
locations, thickness records, NDE findings, repair history), and
maintenance records. The practice requires the analyst to record data
**confidence / uncertainty** and to propagate that uncertainty into the
POF estimate; assumptions made in the absence of data must be documented
so they can be reviewed and revisited in re-assessment cycles.

### Damage-mechanism identification and screening

RP 580 directs the team to screen the equipment population against the
catalogue of damage mechanisms in [api-rp-571](api-rp-571.md) (*Damage Mechanisms
Affecting Fixed Equipment in the Refining Industry*). Each item is
evaluated for credible mechanisms as a function of materials, process,
environment, and operating history. The output is a per-item **active
damage-mechanism list** that anchors the POF estimate.

### Probability-of-failure (POF) inputs

POF inputs span the damage-mechanism families encountered in process
plants:

- **General / uniform corrosion** — rate-based, with thickness margin
  to retirement-limit / `t_min` driving probability.
- **Local corrosion** — under-deposit, dead-leg, mix-point, injection-
  point, soil-side; spatially heterogeneous and inspection-coverage-
  sensitive.
- **Pitting / localised attack** — chloride pitting in austenitic
  stainless, microbiological influenced corrosion (MIC), galvanic.
- **Cracking** — stress-corrosion cracking (chloride-SCC, caustic-SCC,
  amine-SCC, sulphide-SCC, polythionic-acid SCC), HIC / SOHIC, hydrogen
  embrittlement.
- **Fatigue** — mechanical fatigue (vibration, thermal cycling,
  pressure cycling), corrosion-fatigue.
- **Creep / high-temperature damage** — creep, creep-fatigue
  interaction, high-temperature hydrogen attack (HTHA), graphitisation,
  spheroidisation, sigma-phase embrittlement.
- **Brittle fracture** — low-temperature toughness, post-PWHT
  embrittlement.
- **Mechanical / external** — external corrosion under insulation
  (CUI), atmospheric corrosion, soil-side, mechanical damage from
  third-party impact or maintenance.

Each mechanism contributes to a POF score (qualitative band or
quantitative frequency, depending on the route) and modulates with
inspection effectiveness (see below).

### Consequence-of-failure (COF) inputs

COF inputs span the impact categories that follow from a credible release:

- **Flammable consequence** — release rate, ignition probability,
  flash / pool / jet fire footprints, explosion overpressure.
- **Toxic consequence** — toxic-release dispersion (H2S, ammonia, HF,
  chlorine), occupied-area exposure.
- **Environmental consequence** — soil and water contamination, regulatory
  reporting thresholds, clean-up cost.
- **Business interruption / production loss** — downtime, lost-production
  cost, supply-chain knock-on, repair / replacement cost, regulatory
  shutdown risk.

The COF estimate is unit- and location-specific: the same equipment item
in a remote location and in a densely-occupied refinery yields different
COF bands.

### Risk-matrix and category-band conventions

RP 580 sanctions both **risk-matrix** representations (typically 5×5,
with POF and COF each banded into five categories — labelled 1–5 or
A–E depending on the operator's convention) and **iso-risk numerical
bands** (when the quantitative RP 581 route produces a continuous risk
value). The practice does not mandate a specific matrix size or band
labelling — those are owner-user decisions documented in the programme
description — but it requires that risk acceptance criteria, inspection-
planning thresholds, and mitigation triggers be tied to the chosen matrix
in writing.

### Inspection-effectiveness categories

RP 580 grades inspection effectiveness on a five-tier scale, **A through
E**:

| Category | Label | Meaning |
|----------|-------|---------|
| A | Highly effective | Inspection identifies the active damage mechanism with very high confidence at the relevant scale. |
| B | Usually effective | Identifies the mechanism in most cases; modest residual uncertainty. |
| C | Fairly effective | Detects the mechanism in a substantial fraction of cases; moderate residual uncertainty. |
| D | Poorly effective | Limited ability to detect the mechanism; significant residual uncertainty. |
| E | Ineffective | Does not credibly detect the mechanism; treated as no inspection for POF purposes. |

The effectiveness of past inspections **modifies the POF estimate**:
a Category-A inspection compresses the credible POF band more than a
Category-D inspection. The future inspection plan is structured around
the effectiveness category needed to bring projected risk below the
acceptance threshold within the planning horizon.

### Updating rules

RP 580 requires re-assessment on a documented cadence and on **trigger
events**: process change, materials change, new damage-mechanism
discovery, post-inspection finding that contradicts the prior POF
assumption, repair / alteration, change in COF (e.g., change in inventory,
ignition source, or occupancy), or expiration of the planning horizon.
The plan-execute-reassess loop is the core programmatic discipline that
distinguishes RBI from a one-time risk study.

## Cross-references

- **API RP 581 — Risk-Based Inspection Methodology.** The quantitative
  sibling: provides damage-factor models, generic-failure-frequency tables,
  release-and-consequence calculations, and a risk-matrix scoring engine
  that satisfies the RP 580 framework. RP 580 = framework / qualitative;
  RP 581 = numerical implementation. See [api-rp-581](api-rp-581.md).
- **API 510 — Pressure Vessel Inspection Code.** Authorises RBI per
  RP 580 / RP 581 as the alternative to table-based intervals for
  pressure vessels. See [api-510](api-510.md).
- **API 570 — Piping Inspection Code.** Authorises RBI per RP 580 /
  RP 581 as the alternative to table-based intervals for process piping.
  See [api-std-570](api-std-570.md).
- **API 653 — Tank Inspection, Repair, Alteration, and Reconstruction.**
  Authorises RBI per RP 580 / RP 581 as the alternative to table-based
  intervals for atmospheric / low-pressure storage tanks. See
  [api-std-653](api-std-653.md).
- **API 579-1 / ASME FFS-1 — Fitness-for-Service.** Invoked when an RBI
  inspection plan surfaces an out-of-tolerance flaw (metal loss below
  `t_min`, crack-like flaw, distortion). RBI sets the *when and how* of
  inspection; FFS sets the *what to do with the finding*. See
  [api-std-579](api-std-579.md).
- **API RP 571 — Damage Mechanisms Affecting Fixed Equipment in the
  Refining Industry.** The damage-mechanism catalogue that anchors
  RP 580's screening and POF estimation. RP 580 §damage-mechanism
  identification calls RP 571 directly. See [api-rp-571](api-rp-571.md).
- **ASME PCC-3 — Inspection Planning Using Risk-Based Methods.** Parallel-
  scope industry standard from ASME on RBI inspection-planning programmes
  for pressure equipment. PCC-3 and RP 580 are mutually recognised
  alternatives in many jurisdictions; both define a documented
  programme with the same conceptual elements (team, data, screening,
  POF, COF, risk, plan, reassess), with PCC-3 emphasising pressure-
  equipment scope and RP 580 the broader process-plant population.
  See [[asme-pcc-3]].
- **DNV-RP-G101 — Risk-Based Inspection of Offshore Topsides Static
  Mechanical Equipment.** Offshore-topsides RBI recommended practice
  from DNV; conceptually parallel to RP 580 with adaptations for
  offshore process equipment, weight-cost, and helideck-occupancy COF
  considerations. See [dnv-rp-g101](dnv-rp-g101.md).
- **Risk-Based Inspection (concept).** [risk-based-inspection](../concepts/risk-based-inspection.md) —
  the concept page that names RP 580 as the qualitative methodology
  document and RP 581 as the quantitative implementation.

## Cross-wiki bridges

- [ISM Code — International Safety Management Code](../../../maritime-law/wiki/concepts/ism-code.md)
  (maritime-law) — **bidirectional bridge**: API RP 580's qualitative
  RBI methodology and risk-matrix framework (POF × COF banding,
  inspection-effectiveness categories A–E, plan-execute-reassess loop)
  feed the SOLAS-Ch.IX-mandated Safety Management System risk-assessment
  obligation that ISM Code Part A imposes on operators. ISM Code §1.2.2.2
  (objectives — "establish safeguards against all identified risks")
  and §7 (development of plans for shipboard operations addressing key
  shipboard operations concerning safety) are the SMS clauses where a
  vessel-operator's pressure-equipment RBI programme — when the vessel
  carries fixed equipment within RP 580's scope (e.g., FPSO process
  trains, gas-carrier cargo-handling pressure vessels, MODU process
  modules) — supplies the risk-assessment substrate. Offshore-platform
  RBI programmes operating under flag-state classification (DNV, ABS,
  LR, BV, ClassNK class rules + IACS UR Z17 ISM-implementation
  guidance) routinely run RP 580 / RP 581 as the engineering-substrate
  methodology while the SMS document records the management-system
  envelope around it. The treaty regime carries no numeric POF / COF
  rules; ISM delegates to engineering-standards substrates like RP 580
  for the technical risk-assessment content.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground RBI-derived inspection-interval and risk-ranking
outputs against this practice. It also serves as the upstream-methodology
anchor for [api-510](api-510.md), [api-std-570](api-std-570.md), and [api-std-653](api-std-653.md) when those
codes invoke their RBI alternative-interval route, and as the link
target from the [risk-based-inspection](../concepts/risk-based-inspection.md) concept page.
**Metadata-only** per spinout 2026-05-05 governance: no clause text,
methodology tables, risk-matrix templates, POF / COF formulas, or
inspection-effectiveness checklists are reproduced here.

## Where to find the full text

- Catalog copies (read-only, vendor-derivative; do NOT copy into git per
  spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/API/Specifications/API_RP_580_2nd_Ed_(2009)_Risk-Based_Inspection.pdf`
    — 2nd edition (catalog latest)
  - `/mnt/ace/O&G-Standards/API/Specifications/API_RP_580_1st_Ed_(2002)_Risk-Based_Inspection.pdf`
    — 1st edition (2002)
- API publisher catalog: <https://www.api.org/products-and-services/standards>

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  catalog rows matching `API RP 580` (1st ed 2002, 2nd ed 2009).
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` (entries
  matching `RP 580` / `RP_580`); on-disk copies enumerated in the
  *Where to find the full text* section above.
