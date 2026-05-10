---
title: "API RP 14E — Offshore Production Platform Piping Systems"
slug: api-rp-14e
code_id: api-rp-14e
publisher: API
revision: "5th ed (1991) — catalog latest; 7th ed (2013, with subsequent reaffirmation) is the current published edition"
tags:
  - api
  - offshore-piping
  - production-platform
  - erosional-velocity
  - ve-formula
  - slug-flow
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_14E_1991_Design_and_Installation_of_Offshore_Production_Platform_Piping_Systems.pdf
  - /mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_14E_(1991).pdf
  - /mnt/ace/O&G-Standards/API/Standards/API_14E_Design_and_Installation_of_Offshore_Production_Platform_Piping.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 14E — Offshore Production Platform Piping Systems

> **code_id:** `api-rp-14e` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** 5th ed (1991) — catalog latest; 7th ed (2013) is the current published edition

## Scope

API RP 14E is the recommended practice for the **design and installation
of offshore production platform piping systems** carrying natural gas,
crude oil, produced water, and mixed-phase production fluids — the
topsides piping that ties wellheads, manifolds, separators, treaters,
metering, and export risers together on fixed and floating offshore
production facilities. It addresses pressure-class and material
selection, valve and fitting selection, sizing for flow and erosion,
support and flexibility, fabrication, hydrostatic and leak testing, and
the integration of piping with the platform's safety, fire-protection,
and process-shutdown systems.

The practice is most-cited industry-wide for a single equation — the
**erosional-velocity screening formula** `V_e = C / sqrt(ρ)` — that
provides a starting bound on flowing-fluid velocity in two-phase oil/gas
service to limit erosion-corrosion damage. The formula is the canonical
"first screen" for two-phase production-piping sizing and is referenced
from operator design bases, EPC topsides specifications, and concept-page
[erosion-and-fac](../concepts/erosion-and-fac.md) in this wiki.

RP 14E is a **companion** rather than a substitute for general process-
piping codes. Materials and fabrication build on [asme-b31-3](asme-b31-3.md) (process
piping) and [api-spec-5l](api-spec-5l.md) (line-pipe). Pressure-relief sizing follows
**API 520 / 521** (relief-device sizing and disposal). Wellhead and tree
interfaces follow [api-spec-6a](api-spec-6a.md). Subsea ROV-tool interfaces follow
**API RP 17H**. Platform-level safety integration ties to **API RP 14C**
(safety systems) and **API RP 14J** (hazards analysis). The page does
**not** reproduce clause text, the V_e formula's derivation, C-constant
tables, or any sizing prescriptions — those live in the publisher
document and are referenced via the catalog copy enumerated below per
the spinout 2026-05-05 metadata-only governance.

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 5th ed | 1991 | **catalog copy** (`API_RP_14E_1991_Design_and_Installation_of_Offshore_Production_Platform_Piping_Systems.pdf`, `API_RP_14E_(1991).pdf`, plus an undated `API 14E Design and Installation of Offshore Production Platform Piping.pdf`) | The edition that codified the modern V_e = C/√ρ form with C = 100 (continuous) / 125 (intermittent) and that subsequent operator design bases continue to reference. |
| 6th ed | 2007 | not in catalog | Editorial alignment; no substantive change to the V_e screening framework. |
| 7th ed | 2013 (with subsequent reaffirmation) | not in catalog | Current published edition; clarifies that the V_e formula is a **screening tool** rather than an absolute limit, points users toward sand-erosion-specific quantitative methods for sand-laden production, and aligns terminology with the rest of the API-14 series. |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (5th ed, 1991) per the spinout's metadata-only
> policy; the 7th edition (2013) is the publisher's current edition and
> is the appropriate citation for new design work, particularly for
> sand-producing wells where the 7th-edition framing of V_e as a
> screening tool (with deeper sand-erosion analysis required when the
> screen flags) materially changes the design loop relative to the 5th-
> edition presentation. Forward-adopt the publisher edition when a more
> recent catalog copy lands.

## Key sections

The 5th-edition organisation (mirrored in the 6th and 7th editions with
editorial renumbering) groups topsides-piping content into the following
families. Section numbering shifts edition-over-edition; the family-level
grouping is invariant.

| Family | Coverage |
|--------|----------|
| **System-design philosophy** | Service segregation (oil, gas, produced water, utilities, fuel-gas, instrument-gas, fire-water, drains) and pressure-class selection per the platform's hazard zones and the ANSI / ASME B16.5 flange-rating ladder. Sets the per-service pressure-temperature design envelope that the rest of the practice builds on. |
| **Material selection** | Carbon-steel default for sweet hydrocarbon service; CRA upgrades (13Cr, duplex, super-duplex, 6Mo, Alloy 625, Alloy 825) for sour service per [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md) / [iso-15156](iso-15156.md) and for erosion-corrosion service per [erosion-and-fac](../concepts/erosion-and-fac.md); cross-references to [api-spec-5l](api-spec-5l.md) for line pipe and to [asme-bpvc-ii-d](asme-bpvc-ii-d.md) for allowable-stress data. The materials matrix is a screening tool — detailed materials selection still requires the operator's metallurgy / corrosion specialist input, particularly for sour + sand combined service. |
| **Valve and fitting selection** | Trim selection by service; gate / globe / ball / check valve selection criteria; flange ratings tied to [asme-b16-5](asme-b16-5.md) and [asme-b16-34](asme-b16-34.md); reference to [api-spec-6d](api-spec-6d.md) for pipeline valves and to API 600/602/603 series for general industrial valves. Discusses valve selection for emergency shutdown, blowdown, and isolation duty. |
| **Erosional velocity** | The V_e = C / sqrt(ρ) screening formula with C = 100 for continuous service and C = 125 for intermittent service (5th-edition values; 7th-edition retains them as starting screens). Caveats around clean-fluid assumption, sand-laden service, fluid-composition effects, and entrained-solids effects (see *V_e formula caveats* below). |
| **Pressure relief** | Relief-device sizing follows **API 520 Pt I/II** (sizing) and **API 521** (disposal-system design); RP 14E is the platform-piping reference that points process and piping designers at the API 520/521 framework rather than reproducing it. |
| **Supports and flexibility** | Pipe-support spacing, flexibility-analysis triggers, expansion-loop sizing, anchor and guide-block design, and the platform-deflection / hull-deflection envelopes that piping must accommodate on floating production units. Ties to [asme-b31-3](asme-b31-3.md) flexibility-analysis methodology. |
| **Hydrotest and leak test** | Hydrostatic-test pressure, hold time, test-medium selection, and pre-commissioning leak testing. Cross-referenced from API Spec 5L (line-pipe hydrotest at the mill) and from operator pre-commissioning specifications. |
| **NDE acceptance** | Non-destructive examination of welds (RT, UT, MT, PT) with acceptance criteria for production-piping service classes; references back to [asme-bpvc-ix](asme-bpvc-ix.md) for welder qualification and to [asme-b31-3](asme-b31-3.md) for code-level acceptance. |
| **Fire-resistance and safety integration** | Fire-rating of valves and piping in fire zones; emergency-isolation valve placement; integration with the platform-level safety-shutdown logic governed by **API RP 14C** (safety-systems design) and the hazards-analysis framework of **API RP 14J**. |

## V_e formula caveats

The `V_e = C / sqrt(ρ)` screen is the most-cited content in the
practice and is also the most-misapplied. Caveats that matter for
defensible offshore-piping design:

- The formula is **empirical** — calibrated against historical
  experience with clean two-phase liquid + gas production flow on
  carbon-steel topsides piping. It has no first-principles derivation;
  the C constants were fitted, not computed.
- **C = 100 (continuous service) and C = 125 (intermittent service)**
  are the 5th-edition values that operators continue to cite. For
  most clean-service applications the values are conservative — actual
  in-service erosion-corrosion rates at V_e are typically well below
  the assumed wall-loss budget — but the conservatism **does not
  carry over to sand-laden production**, where the cubic
  particle-velocity dependence of mechanical erosion (see
  [erosion-and-fac](../concepts/erosion-and-fac.md)) overwhelms the formula's clean-fluid framing.
- **Sand-laden production fluids require a quantitative
  sand-erosion model.** Modern alternatives:
  - **Salama (1998)** — explicit sand-erosion rate model that
    captures particle size, particle loading, and impact geometry.
  - **Shirazi / E/CRC (Erosion / Corrosion Research Center, University
    of Tulsa) McLaury-Shirazi family** — particle-tracking models with
    geometry-specific (elbow, tee, reducer) erosion-rate predictions
    and material-property dependence (hardness, ductility).
  - **DNV RP O501** (subsea managed-pressure-drilling and
    sand-management practice) provides a complementary sand-erosion
    assessment framework used widely in North Sea operations.
- **Industry treatment.** The 7th-edition (2013) text and current
  operator design bases treat V_e as a **screening tool**: the
  formula's role is to flag locations where a deeper sand-erosion +
  multiphase-CFD analysis is required, not to set the as-built
  velocity limit on its own. A V_e screening flag is **not** an
  automatic design failure — it is the trigger for the next-level
  analysis using the Salama / Shirazi / DNV-O501 lineage.
- **Fluid-composition and entrained-solids effects** the V_e formula
  does **not** capture: high-CO2 sweet corrosion (modelled separately
  per the de Waard–Milliams framework), H2S sour-corrosion (governed
  by [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md) / [iso-15156](iso-15156.md) materials selection), free
  water at low spots, slug-flow regime (the mechanical-impact loading
  on bends in slug flow is not a V_e phenomenon), and CRA-versus-CS
  metallurgy (the C constant was calibrated on carbon-steel data —
  CRA piping has substantially higher actual erosion-velocity
  thresholds and the formula is over-conservative for CRA).

## Cross-references

- **API RP 571 — Damage mechanisms.** Erosion and erosion-corrosion
  catalogue entries provide the failure-mode context that V_e screening
  is intended to bound. See [api-rp-571](api-rp-571.md).
- **API Spec 5L — Line pipe.** Material and dimensional specification
  for the carbon-steel pipe that RP 14E topsides piping is fabricated
  from. See [api-spec-5l](api-spec-5l.md).
- **ASME B31.3 — Process piping.** The general process-piping code that
  RP 14E supplements for offshore-production service. RP 14E does not
  replace B31.3 — designs cite both: B31.3 for the code-level rules
  and RP 14E for the offshore-production-specific guidance. See
  [asme-b31-3](asme-b31-3.md).
- **Erosion / FAC concept page.** The concept-page consumer for the
  V_e formula and for the modern Salama / Shirazi / EPRI-CHECWORKS
  lineage. See [erosion-and-fac](../concepts/erosion-and-fac.md).
- **Sour-service materials.** When the produced fluid is sour (H2S
  partial pressure above the [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md) / [iso-15156](iso-15156.md)
  threshold), RP 14E material-selection points the designer at the
  sour-service materials track. See [sour-service-materials](../concepts/sour-service-materials.md) and
  [ampp-mr-0175-pt1](ampp-mr-0175-pt1.md).
- **API Spec 6A — Wellhead and Christmas tree equipment.** The
  upstream interface for topsides piping at the tree connection. See
  [api-spec-6a](api-spec-6a.md).
- **API RP 17H — Subsea ROV interfaces.** When the topsides piping
  ties into subsea jumpers and tie-in spools, ROV-tool interfaces are
  governed by API RP 17H (future-promotion candidate; not yet a
  per-code page in this wiki).
- **API 520 (Pt I/II) and API 521 — Pressure relief.** Relief-device
  sizing and disposal-system design that RP 14E points the platform
  designer at for pressure-relief and blowdown components of the
  piping system. Future-promotion candidates.
- **API Std 660 — Shell-and-tube heat exchangers.** Inlet-end
  erosion-corrosion at heat-exchanger tube inlets is the typical
  failure mode that V_e screening on the upstream piping is intended
  to bound; heat-exchanger design itself is governed by API 660 (and
  TEMA). Future-promotion candidate.
- **API RP 14C — Analysis, design, installation, and testing of
  basic surface safety systems.** Companion practice that integrates
  RP 14E piping with the platform-level safety-shutdown logic.
  Catalog copy present (2001, 2007, 7th ed) — future-promotion
  candidate.
- **API RP 14J — Design and hazards analysis for offshore production
  facilities.** Companion practice that places RP 14E piping into the
  facility-level hazards-analysis (HAZOP, HAZID) framework. Catalog
  copy present — future-promotion candidate.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground V_e-derived two-phase-piping screening outputs,
topsides-piping material-selection outputs, and pressure-relief
referrals against this practice. It also serves as the standards-page
target for [erosion-and-fac](../concepts/erosion-and-fac.md), which forward-references the V_e
formula. **Metadata-only** per spinout 2026-05-05 governance: no clause
text, formula derivation, C-constant tables, sizing prescriptions, or
material-selection matrices are reproduced here.

## Where to find the full text

- Catalog copies (read-only, vendor-derivative; do NOT copy into git
  per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_14E_1991_Design_and_Installation_of_Offshore_Production_Platform_Piping_Systems.pdf`
    — 5th edition (catalog latest; primary copy)
  - `/mnt/ace/O&G-Standards/API/Recommended-Practice/API_RP_14E_(1991).pdf`
    — 5th edition duplicate filename
  - `/mnt/ace/O&G-Standards/API/Standards/API_14E_Design_and_Installation_of_Offshore_Production_Platform_Piping.pdf`
    — undated copy filed under `Standards/`; hash-distinct from the two
    Recommended-Practice copies
- API publisher catalog: <https://www.api.org/products-and-services/standards>

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  catalog rows matching `API RP 14E` (5th ed 1991, three distinct
  copies).
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json`
  (entries with `organization: API`, `doc_number: 14E`, three rows
  spanning the Recommended-Practice and Standards subtrees with
  distinct content hashes).
