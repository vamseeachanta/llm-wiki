---
title: "API RP 581 — Risk-Based Inspection Methodology"
slug: api-rp-581
code_id: api-rp-581
publisher: API
revision: "2nd ed (2008, catalog latest); 4th ed (2025) is the current published edition"
tags:
  - api
  - rbi
  - quantitative
  - integrity-management
  - inspection-effectiveness
  - damage-factor
  - cof
  - pof
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 581 — Risk-Based Inspection Methodology

> **code_id:** `api-rp-581` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** 2nd ed (2008, catalog latest); 4th ed (2025) is the current published edition

## Scope

API RP 581 is the **quantitative** Risk-Based Inspection (RBI) methodology
for refining and petrochemical pressurised assets — vessels, piping
circuits, tankage, exchangers, and pressure-relieving devices — operated
under the in-service inspection codes [api-510](api-510.md), [api-std-570](api-std-570.md), and
[api-std-653](api-std-653.md). It is the engineered sibling of [api-rp-580](api-rp-580.md): where
RP 580 sets the **programme requirements** (governance, team competence,
documentation, re-evaluation triggers) that any RBI study must satisfy,
RP 581 supplies the **calibrated equations, look-up tables, damage-factor
formulas, and consequence-of-failure (COF) models** that turn those
programme requirements into a numeric `risk = POF × COF` ranking for
each asset. The methodology is organised in three parts: (I) inspection
planning workflow and interfaces with the inspection codes; (II)
**Determination of Damage Factors** — per-mechanism POF modifiers
covering thinning, environmental cracking, HTHA, sulfidation, brittle
fracture, mechanical fatigue, creep, and others; (III) **Consequence of
Failure** — flammable / toxic release modelling, hole-size selection,
atmospheric dispersion, and jet / pool / fireball / BLEVE energetic
event models. RP 581 also tabulates the **inspection-effectiveness
factors** (categories A–E, inherited from RP 580) that adjust POF based
on the technique, extent, and frequency of prior inspections. The output
is a per-asset POF (events/year), per-asset COF (consequence area in
ft² and / or $/event), and a $/year financial-risk ranking that drives
the RBI inspection plan. This is the document most production RBI
software packages implement under the hood; operator-specific
calibrations layer on top.

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 1st ed (Base Resource Document, BRD) | 2000 | not in catalog | Original "Base Resource Document" issued under the API RBI joint-industry project; introduced the POF × COF + damage-factor + inspection-effectiveness framework. |
| 2nd ed | 2008 | **catalog copy** (per `og-standards-api.md`, row "RP 581 \| Risk-Based Inspection Technology \| 2008") | Re-issued as a Recommended Practice (re-titled *Risk-Based Inspection Technology*); expanded damage-factor catalogue, refined COF models, added internal CUI / SCC mechanisms. |
| 3rd ed | 2016 | not in catalog | Significant overhaul of the COF Level 1 / Level 2 split; expanded fluid-property tables; revised brittle-fracture and HTHA modules; aligned with the 2014 edition of API RP 571 damage-mechanisms catalogue and the 2016 edition of API RP 941 (Nelson curves). |
| 4th ed | 2025 (current) | not in catalog | Current published edition; updates to damage-factor calibrations and COF models reflecting field-experience data accumulated through the 2010s, and re-aligned with the latest editions of [api-rp-571](api-rp-571.md) and [api-std-579](api-std-579.md). |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (2nd ed, 2008) per the spinout's metadata-only
> policy; the 4th edition (2025) is the publisher's current edition and
> is the appropriate citation for new RBI work. Damage-factor formulas
> and COF models have evolved across editions — operators should not
> mix editions inside a single RBI study.

## Key parts

RP 581's structure is stable across editions, organised in three parts.

- **Part I — Inspection Planning Methodology.** The workflow: asset
  registration, fluid and operating-condition data capture, damage-
  mechanism screening (delegating to [api-rp-571](api-rp-571.md) for mechanism
  identification), POF computation per Part II, COF computation per
  Part III, risk ranking, and inspection-plan optimisation against the
  operator's risk-acceptance threshold. This part defines the
  interfaces with [api-510](api-510.md) (vessels), [api-std-570](api-std-570.md) (piping), and
  [api-std-653](api-std-653.md) (tanks) — RP 581 does not replace those codes, it
  feeds the alternative interval-setting route they each permit.
- **Part II — Determination of Damage Factors.** Per-mechanism POF
  modifiers. Each damage mechanism has its own sub-part with: (a) a
  screening logic identifying when the mechanism applies, (b) a
  damage-state model (susceptibility level, rate or growth law),
  (c) a base damage factor as a function of damage state and time
  since last inspection, and (d) an inspection-effectiveness modifier
  that reduces the damage factor as effective inspections accumulate.
  The aggregate damage factor combines across mechanisms; a generic
  failure frequency (the industry-baseline component-failure rate
  from operator and JIP data) is multiplied by the aggregate damage
  factor to give the asset's POF.
- **Part III — Consequence of Failure Methodology.** Calibrated
  consequence models for flammable and toxic releases. Includes
  hole-size selection (a discrete set of release scenarios — typically
  ¼″, 1″, 4″, and rupture — weighted by frequency), release-rate
  computation (choked / sub-sonic, liquid / vapour / two-phase),
  atmospheric dispersion (Pasquill stability classes), and energetic-
  event modelling (jet fire, pool fire, BLEVE, vapour cloud explosion,
  flash fire, toxic-cloud lethality). COF is expressed as a
  consequence area (ft² of personnel-affected zone for personnel-
  safety risk) and / or as a financial figure ($/event for
  business-impact risk). Part III offers a Level 1 (look-up-table)
  and Level 2 (compositional, more rigorous) treatment.

## Damage-factor catalogue

Part II quantifies the following damage-mechanism categories. Each is
addressed by its own sub-clause with screening logic, damage-state
model, and inspection-effectiveness modifier.

- **Thinning.** General and localised metal loss; the most common
  damage factor. Calibrated against measured corrosion rate and
  remaining wall.
- **Thinning combined with cracking.** Coupled mechanism for assets
  experiencing both wall loss and environmental cracking; aggregate
  damage state combines the two contributions.
- **External corrosion and Corrosion-Under-Insulation (CUI).** External
  metal loss on insulated and uninsulated equipment; CUI is the
  dominant external-thinning mechanism for moderate-temperature
  insulated piping and vessels and has its own dedicated screening
  logic (insulation type, operating-temperature window, age, water
  ingress).
- **External Stress-Corrosion Cracking (External SCC).** Including
  external chloride SCC under insulation on austenitic stainless.
- **Internal Stress-Corrosion Cracking (Internal SCC).** Including
  chloride SCC, caustic SCC, amine cracking, carbonate SCC, sulfide-
  stress cracking (SSC) / hydrogen-induced cracking (HIC) per the
  sour-service umbrella, and polythionic-acid SCC on austenitic
  stainless during shutdowns / start-ups.
- **High-Temperature Hydrogen Attack (HTHA).** Methane-driven
  decarburisation and fissuring of carbon and low-alloy steels in
  hot hydrogen service; screened against [api-rp-941](api-rp-941.md) Nelson-curve
  operating envelopes.
- **Brittle Fracture.** Low-toughness failure mode; screened against
  minimum-pressurisation-temperature (MPT) curves and Charpy data;
  damage factor reflects the gap between operating temperature and
  the ductile-to-brittle transition.
- **Mechanical Fatigue.** Cyclic-loading damage in piping (vibration,
  pressure cycling) and vessels (thermal, pressure); damage factor
  combines audible / visual fatigue indicators with cycle count.
- **Creep.** High-temperature time-dependent damage; damage factor
  evaluates time-to-rupture against operating-temperature and stress
  history (Larson–Miller parameter framing).
- **Sulfidation.** High-temperature sulfur-driven corrosion in hot
  hydrocarbon-with-sulfur service (crude / vacuum / FCC / hydroprocessing);
  the modified McConomy curves give the rate baseline.
- **Polythionic-Acid SCC.** Austenitic-stainless cracking during
  shutdowns when sulfide scales react with moisture and oxygen;
  damage factor combines material susceptibility with shutdown
  protection (neutralising wash, dry purge).
- **Amine Cracking, Caustic SCC, Carbonate SCC.** Environmental-cracking
  mechanisms specific to amine-treating, caustic, and carbonate
  service respectively; each with its own susceptibility-vs-temperature
  / concentration screening.

The catalogue is normative — RP 581 expects every credible damage
mechanism on the asset to be addressed, with a default damage factor
of zero only when the mechanism has been screened out with documented
basis. New mechanisms (e.g., refining-feedstock-shift mechanisms)
are introduced edition-by-edition.

## Inspection-effectiveness factors

POF is reduced as effective inspections accumulate evidence that the
asset's damage state is bounded. RP 581 inherits the
inspection-effectiveness category definitions from [api-rp-580](api-rp-580.md):

| Category | Effectiveness | Typical example |
|----------|--------------|-----------------|
| **A** | Highly Effective | 100 % volumetric examination by an appropriate method, e.g. full UT scan with calibrated standards on a thinning circuit, or PAUT mapping with crack-detection sensitivity on an SCC-susceptible weld. |
| **B** | Usually Effective | Substantial coverage by an appropriate method, e.g. ~75 % UT scan, ILI run with sized anomalies, or extensive WFMT on welds for SCC. |
| **C** | Fairly Effective | Partial coverage by an appropriate method, e.g. ~50 % spot UT, sample WFMT, partial RT. |
| **D** | Poorly Effective | Minimal coverage by an appropriate method, e.g. visual + isolated UT spots, or technique not well matched to the dominant mechanism. |
| **E** | Ineffective | No inspection, or inspection method does not detect the mechanism (e.g. visual-only against internal SCC). |

Each damage factor sub-clause in Part II tabulates the POF
multiplier as a function of (damage state, number of inspections at
each effectiveness category, time since last inspection). The
multiplier asymptotes downward as A- and B-rated inspections
accumulate; D and E inspections do not reduce — and may not stop the
growth of — the damage factor over time. This is the load-bearing
mechanism by which RBI rewards better inspections with longer
intervals: an A-rated inspection on a thinning circuit can
multiplicatively reduce the damage factor, lengthening the RBI
inspection interval, while a sequence of E-rated inspections leaves
the damage factor unchanged.

## Cross-references

- **[api-rp-580](api-rp-580.md)** — *Risk-Based Inspection* (qualitative /
  programme-requirements sibling). RP 580 defines the governance,
  team competence, documentation, and re-evaluation requirements that
  every RBI study must satisfy. RP 581 supplies the quantitative
  engine; RP 580 supplies the programme. An RP 581 calculation
  without an RP 580-conformant programme around it is not a
  sanctioned RBI deliverable.
- **[api-510](api-510.md) / [api-std-570](api-std-570.md) / [api-std-653](api-std-653.md)** — In-service
  inspection codes that **permit** RBI as the alternative
  interval-setting route to their table-based / half-life intervals.
  RP 581 is the methodology those codes invoke when an owner-user
  elects the RBI route.
- **[api-std-579](api-std-579.md)** — *Fitness-for-Service* / ASME FFS-1. Called
  when RP 581's POF computation surfaces a flaw exceeding the
  inspection-code acceptance threshold; the FFS verdict
  (run / repair / replace / re-rate / re-inspect) feeds back into
  the next RBI cycle's POF and inspection plan, closing the
  RBI ↔ FFS loop documented in [fitness-for-service](../concepts/fitness-for-service.md) and
  [risk-based-inspection](../concepts/risk-based-inspection.md).
- **[api-rp-571](api-rp-571.md)** — *Damage Mechanisms Affecting Fixed Equipment
  in the Refining Industry*. The catalogue of damage-mechanism
  metallurgical and chemical descriptions that RP 581's Part II
  damage factors quantify. RP 581 expects mechanism identification
  per RP 571 as the upstream screening step.
- **[api-rp-941](api-rp-941.md)** — *Steels for Hydrogen Service at Elevated
  Temperatures and Pressures in Petroleum Refineries and
  Petrochemical Plants*. The Nelson curves; the screening reference
  for RP 581's HTHA damage factor.
- **ASME PCC-3** — *Inspection Planning Using Risk-Based Methods*.
  Parallel RBI methodology with broader equipment-class scope; an
  alternative to RP 581 in some operator and regulator regimes.
  Future first-class standards page candidate.
- **[dnv-rp-g101](dnv-rp-g101.md)** — *Risk-Based Inspection of Offshore Topsides
  Static Mechanical Equipment*. The offshore-topsides analogue;
  parallel methodology with offshore-specific consequence and
  inspection-access calibrations. Several flag-state regimes
  reference DNV-RP-G101 in lieu of API RP 581 for offshore topsides.
- **[risk-based-inspection](../concepts/risk-based-inspection.md)** — Concept page; describes the
  RBI methodology generically and routes into RP 581 as the
  quantitative implementation.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground RBI quantitative outputs (POF, COF, damage
factors, inspection-effectiveness multipliers) against this code. It
is also the forward-reference target from [risk-based-inspection](../concepts/risk-based-inspection.md)
for the quantitative methodology and from [api-510](api-510.md) / [api-std-570](api-std-570.md)
/ [api-std-653](api-std-653.md) for the alternative interval-setting route. **Metadata-
only** per spinout 2026-05-05 governance: no clause text, damage-factor
formulas, COF coefficients, hole-size frequency tables, fluid-property
look-ups, or inspection-effectiveness multipliers are reproduced here.

## Where to find the full text

- API publisher catalog: <https://www.api.org/products-and-services/standards>
- Catalog index for the on-disk vendor PDFs is enumerated in
  [og-standards-api](../sources/og-standards-api.md); per spinout
  2026-05-05 governance, vendor PDFs live on the private vendor mount
  and are not committed to this repo.

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  catalog row `RP 581 | Risk-Based Inspection Technology | 2008`.
