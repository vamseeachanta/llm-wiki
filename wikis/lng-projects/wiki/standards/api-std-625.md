---
title: "API Std 625 — Tank Systems for Refrigerated Liquefied Gas Storage"
slug: api-std-625
code_id: api-std-625
publisher: API
revision: "latest-in-catalog"
jurisdiction: "US (referenced internationally)"
tags:
  - api
  - lng-storage-tank
  - refrigerated-tank
  - full-containment
  - double-containment
  - single-containment
  - civil-engineering
  - mechanical-engineering
added: 2026-05-09
last_updated: 2026-05-09
sources:
  - https://www.api.org/products-and-services/standards
domain: lng-projects
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links: []
---

# API Std 625 — Tank Systems for Refrigerated Liquefied Gas Storage

> **code_id:** `api-std-625` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** latest-in-catalog &nbsp;·&nbsp; **jurisdiction:** US (referenced internationally)

## Scope

API Std 625 is the umbrella tank-system standard for **refrigerated cryogenic
liquefied-gas storage** — primarily LNG, but also liquid nitrogen, liquid
oxygen, liquid hydrogen, ethylene, ethane, propane, and butane service. It
specifies materials, design, fabrication, examination, and testing of the
**tank system** as an integrated package: primary container, secondary
container, outer shell, foundation, insulation, and connected piping. It
does not stand alone — it pulls together and coordinates the application of
constituent design codes that each cover a part of the system: **API Std
620** (large welded low-pressure tanks — typically the outer steel tank
where used), **API Std 650** (welded steel atmospheric tanks — adjacent
non-cryogenic service), **ACI 376** (concrete cryogenic tanks — the
post-tensioned-concrete outer wall and dome of full-containment and
membrane tanks), and **BS EN 14620** (the European parallel cryogenic
tank standard set). It is the design-code companion to LNG-facility
codes — **NFPA 59A**, **CSA Z276**, and **EN 1473** — which define
facility-level safety requirements but defer the tank-system design
to API 625 (or the EU EN 14620 equivalent).

This page is a **metadata-only resolver** entry: it identifies the code,
publisher, edition, and key concepts so downstream consumers (calc modules,
project specifications, regulatory crosswalks) can pin to a specific
revision per the Citation contract. It does not reproduce clauses,
formulas, or tables from the API-published text.

## Edition history

| Edition | Year | Notable |
|---------|------|---------|
| 1st     | 2010 | First issue; codified the umbrella-standard role coordinating API 620, ACI 376, and the tank-type taxonomy that NFPA 59A then began to reference |
| 2nd     | 2018 | Strengthened seismic-design and impact-loading provisions; updated cross-references to current API 620 and ACI 376 editions |
| 3rd     | current | Latest published edition — ongoing coordination with NFPA 59A, ACI 376, and EN 14620 revisions; pin to specific year/addendum at citation time |

## Key concepts

- **Tank-system architecture.** Four containment categories — *single*,
  *double*, *full*, and *membrane* — each defined by which physical
  envelope plays the role of *primary* container (always holds liquid in
  normal operation), *secondary* container (holds liquid if the primary
  fails), and *outer shell* (weather and vapor envelope). API 625
  prescribes which loadings each component must withstand for each
  category.
- **Containment-failure modes and design loadings.** Every tank component
  must be checked against: hydrostatic head from full liquid contents,
  cryogenic-temperature material behaviour and thermal-contraction loads,
  roof live and dead loads, seismic ground motion (operating-basis and
  safe-shutdown level), wind loads, impact loads (vapor-cloud overpressure
  and adjacent jet- or pool-fire thermal flux), and insulation-failure
  scenarios (loss of perlite vacuum, wet insulation, partial collapse of
  annular insulation).
- **Concrete-and-steel composite tanks** are the dominant configuration
  for modern full-containment LNG service: a **post-tensioned concrete**
  outer wall and dome, a **9 % nickel steel** inner tank (ASTM A553 or
  A841), and an annular insulation system typically of **expanded perlite**
  with glass-wool or corkboard liners against the inner tank. This
  configuration delivers the structural load path, cryogenic-toughness
  requirement, and thermal-isolation budget that the standard expects of
  full-containment service.
- **Membrane tanks** (GTT-licensed: **NO 96**, **Mark III**, **Mark V**)
  use a thin cryogenic membrane — Invar (NO 96) or stainless (Mark III,
  Mark V) — bonded inside an insulated **post-tensioned concrete** outer.
  The design is derived from LNG-carrier cargo-containment systems and is
  now common at modern onshore terminals; API 625 recognises membrane
  containment as a fourth category alongside single, double, and full.

## Tank-type architecture comparison

| Type | Primary | Secondary | Roof | Typical service |
|------|---------|-----------|------|-----------------|
| Single-containment | Inner tank (steel) | Diked impoundment surrounding the tank | Inner-tank dome (steel) | Older and smaller plants; some peak-shaving |
| Double-containment | Inner tank + outer wall (concrete or steel) | Outer wall (limited LNG-holding capability, not vapor-tight) | Inner-tank dome (steel) | Mid-size terminals where land allows reduced vapor-fence area |
| Full-containment | Inner tank (9 % Ni) + outer wall (post-tensioned concrete) | Outer wall + concrete dome (vapor-tight) | Concrete dome | Modern export and import terminals — dominant configuration today |
| Membrane | Cryogenic Invar or stainless membrane | Concrete outer wall | Concrete dome | LNG-carrier-derived containment adopted at modern terminals |

## Materials

- **9 % nickel steel** for the primary inner tank — typical specifications
  ASTM A553 (quenched-and-tempered) and ASTM A841 (TMCP). Selected for
  Charpy and CTOD toughness at LNG service temperature (≈ 110 K / −163 °C).
- **Aluminum alloys** (e.g., 5083 and 5454) for inner tanks and internals
  in some service categories.
- **Austenitic stainless steel** (304L) for selected components — piping,
  internals, some inner-tank service for non-LNG liquefied gases.
- **Invar** (36 % Ni iron) for cryogenic membranes in NO 96-style
  membrane systems; near-zero coefficient of thermal expansion is the
  design driver.
- **Post-tensioned concrete** for the outer wall and dome of full-
  containment and membrane tanks; provides the secondary-containment and
  vapor-envelope load path.
- **Insulation systems**: expanded perlite (annular bulk fill, often
  vacuum-evacuated), glass-wool blanket, corkboard panels, and
  mineral-fiber rock-wool — combined per the tank-system designer's
  thermal-budget and boil-off-rate target.

## Construction and commissioning

- **Hydrotest at ambient temperature** of the assembled tank, against the
  acceptance criteria of API 620 (or EN 14620 equivalent) — confirms the
  static-pressure and weld-integrity envelope before cryogenic service.
- **Cool-down per a controlled cool-down curve** — gradual cooling from
  ambient to LNG temperature, time- and gradient-limited to avoid thermal
  shock and weld-zone embrittlement; rates are typically of the order of
  a few kelvin per hour.
- **Vacuum-insulation-pressure check** for tanks with perlite-evacuated
  annular insulation; confirms the annulus has been evacuated to design
  vacuum and that vacuum is maintained over the commissioning hold.
- **Boil-off-rate (BOR) measurement** during the cool-down and initial
  hold; verifies the as-built thermal-loss performance against the
  design-basis BOR (typically 0.05–0.15 % of full inventory per day for
  modern full-containment LNG tanks).
- **Leak-tightness verification** of the inner-tank weldments (helium or
  ammonia leak testing per the project specification) and of the outer
  vapor envelope.
- **9 % Ni weldment Charpy and CTOD acceptance** — coupon and production
  weld testing per API 625 / API 620 / project-spec acceptance bands;
  rejects are remediated before cool-down.

## Why this page exists

Resolver target for any LNG calculation or specification module that
derives a constant or methodology from API 625 — most commonly inner-tank
material-grade selection, annular-insulation design, BOR design targets,
and seismic-loading combinations. The frontmatter `code_id` / `publisher`
/ `revision` triplet is what the calc-time citation contract matches
against. Downstream consumers must pin to the specific edition cited
(currently 3rd, latest-in-catalog) rather than relying on this page
drifting to a future revision. The page is also the standards-side anchor
for the `lng-storage-tanks` concept page, which names API 625 in its
*Standards / References* section, and for any project-spec template that
incorporates API 625 by reference.

## Cross-references

**Sibling lng-projects standards**

- [`nfpa-59a`](nfpa-59a.md) — US LNG-facility design code; **incorporates
  API 625 by reference** for tank-system design within the broader
  facility-safety framework.
- *CSA Z276* — Canadian LNG production-storage-handling parallel; also
  references API 625 (or EN 14620) for tank-system design (file when
  landed).
- [`igc-code`](igc-code.md) — IMO International Gas Carrier Code; ship-side
  counterpart for cargo-containment systems. Membrane systems (GTT NO 96,
  Mark III, Mark V) and Type B Moss tanks recognised under the IGC Code
  are the technological lineage for onshore membrane tanks scoped under
  API 625; some material specifications (9 % Ni, Invar) cross-reference.
- [`ferc-18-cfr-153`](ferc-18-cfr-153.md) — FERC siting authorization for
  US LNG export and import terminals; project applications must demonstrate
  tank-system design conformance to a recognised standard, typically
  API 625.
- [`phmsa-49-cfr-193`](phmsa-49-cfr-193.md) — federal pipeline-safety
  regulation for onshore LNG facilities; incorporates NFPA 59A by
  reference, which in turn invokes API 625.

**Companion design codes**

- **API Std 620** — *Design and Construction of Large, Welded, Low-Pressure
  Storage Tanks*. Partial scope-overlap with API 625; the outer welded
  steel tank in some configurations is designed to API 620 within the
  API 625 system framework.
- **API Std 650** — *Welded Steel Tanks for Oil Storage*. Adjacent
  non-cryogenic service; relevant for nearby atmospheric tankage in an
  LNG-facility plot plan.
- **ACI 376** — *Code Requirements for Design and Construction of Concrete
  Structures for the Containment of Refrigerated Liquefied Gases*. The
  concrete-design code that API 625 invokes for the post-tensioned
  concrete outer wall and dome of full-containment and membrane tanks.
- **BS EN 14620** (parts 1–5) — *Design and Manufacture of Site-Built,
  Vertical, Cylindrical, Flat-Bottomed Steel Tanks for the Storage of
  Refrigerated, Liquefied Gases at Service Temperatures Between 0 °C and
  −165 °C* — the European parallel cryogenic-tank standard set.
- **ASTM A553 / A841** — 9 % nickel-steel plate specifications, the
  primary material grades for LNG inner tanks under API 625.

**lng-projects concepts**

- [lng-storage-tanks](../concepts/lng-storage-tanks.md) — tank-type
  taxonomy aligned with API 625's containment categories.
- [lng-boil-off-gas-management](../concepts/lng-boil-off-gas-management.md)
  — BOG handling, downstream of API 625 thermal-design choices and
  commissioned BOR.
- [lng-process-safety](../concepts/lng-process-safety.md) — facility-level
  safety scenarios; tank-impact and insulation-failure modes are
  API 625 design loadings.
- [lng-project-lifecycle](../concepts/lng-project-lifecycle.md) — phase
  at which API 625 selection (or EN 14620 equivalent) is locked in.
- [lng-project-shapes](../concepts/lng-project-shapes.md) — onshore-
  greenfield, brownfield, and FSRU/FLNG shapes whose tank-system scope
  is governed by API 625 (or EN 14620 in EU jurisdictions).
- [lng-regulatory-framework](../concepts/lng-regulatory-framework.md)
  — bodies-and-codes synthesis; API 625 is the API-published tank-
  system arm referenced by NFPA 59A and CSA Z276.

## Sources

- Source page: [`igu-2025-lng-report`](../sources/igu-2025-lng-report.md)
  — IGU 2025 World LNG Report — global tank-fleet and project-level data
  consistent with API 625 / EN 14620 design practice.
- API publisher catalog: <https://www.api.org/products-and-services/standards>
