---
title: "API RP 583 — Corrosion Under Insulation and Fireproofing"
slug: api-rp-583
code_id: api-rp-583
publisher: API
revision: "not-on-disk (catalog has no API 583 entry as of 2025-12-25 catalog generation); 1st ed (2014) and 2nd ed (2024) are the publisher editions, 2nd ed is current"
tags:
  - api
  - cui
  - insulated-piping
  - fireproofing
  - refinery
  - offshore
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 583 — Corrosion Under Insulation and Fireproofing

> **code_id:** `api-rp-583` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** not-on-disk in `_catalog.json` (no API 583 entry under the 27,343-document catalog snapshot); publisher editions are 1st ed (2014) and 2nd ed (2024, current).

## Scope

API RP 583 is the **specialized recommended practice** that addresses
**corrosion under insulation (CUI)** and **corrosion under fireproofing
(CUF)** as a distinct programme problem — the detection, mitigation, and
inspection-programme design needed to manage external degradation of
insulated piping, pressure vessels, and structural fireproofed members.

It is the **CUI/CUF-specific companion** to the in-service inspection
codes [api-510](api-510.md) (pressure vessels), [[api-std-570]] (piping), and
[[api-std-653]] (atmospheric storage tanks). Where those codes define
**what to inspect and on what interval** (item classification, table-
based intervals, half-remaining-life rule, RBI alternative), RP 583 fills
the **CUI-specific methods and risk factors** gap that the parent
inspection codes deliberately do not enumerate clause-by-clause.

It is also the API-side counterpart to **NACE / AMPP SP0198** (*Control
of Corrosion Under Thermal Insulation and Fireproofing Materials*),
which covers the same scope from the materials-control / coatings-
selection direction. Practitioners typically read both: SP0198 for
insulation-system and coating-system specification, RP 583 for
inspection-programme design and risk-factor screening.

RP 583 is **not** a code — it cannot be invoked as a stand-alone
compliance authority. It is invoked **through** API 510 / 570 / 653 (or
the owner-user's written CUI programme) and is the technical-content
anchor that the [corrosion-under-insulation](../concepts/corrosion-under-insulation.md) concept page forward-
references.

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 1st ed | 2014 | **not-on-disk** | Inaugural edition; codified the CUI/CUF-screening risk-factor list (operating temperature, climate, insulation type, jacketing condition, age, contaminants), aligned with the API 581 (2nd ed, 2008) CUI damage factor and the [api-rp-571](api-rp-571.md) §4 CUI mechanism entry. |
| 2nd ed | 2024 | **not-on-disk** | Current published edition. Material updates: expanded through-insulation NDE coverage (PEC, GWUT, RTR, profile RT) reflecting field-deployed maturity since 2014; expanded CISCC-CUI guidance on austenitic stainless steel (the chloride-stress-corrosion cracking mode); re-aligned with API 581 3rd ed (2016) CUI damage factor; expanded fireproofing-specific sub-programme content. |

> **Edition selection.** Both editions are absent from
> `/mnt/ace/O&G-Standards/_catalog.json` (verified against the
> 2025-12-25 generation; 0 hits on `organization=API` AND
> `doc_number=583` and 0 filename hits). The frontmatter `revision`
> field records `not-on-disk` per the spinout's metadata-only policy.
> The 2nd edition (2024) is the publisher's current edition and is the
> appropriate citation for new CUI/CUF programme work — particularly
> for RBI integration, where the 2nd edition aligns with the API 581
> 3rd-edition damage-factor methodology. Forward-adopt the publisher
> edition when a catalog copy is added.

## Key sections

The headings below summarise the practice's structural backbone — clause
text, screening-criteria threshold tables, NDE acceptance tables, and
coating-class-vs-temperature tabulations are **not reproduced** per
metadata-only governance.

- **CUI risk factors.** RP 583 enumerates the per-circuit / per-item
  risk factors that drive the CUI screening score and prioritise
  inspection effort:
  - **Operating temperature** — the dominant variable. For carbon
    steel, the wet-film band (roughly **−12 °C to ~175 °C**, peaking in
    the boiling-water band) governs CS-CUI severity. For austenitic
    stainless steel, the CISCC-CUI band extends higher (~60 °C to
    ~205 °C and beyond) because evaporative chloride concentration
    drives cracking even when general corrosion would have arrested.
    Cold-service equipment is non-trivially at risk through warm-up
    transients (defrost, shutdown, regeneration) that sweep the steel
    through the worst window.
  - **Climate / external environment** — rainfall, humidity, marine
    chloride load (proximity to coast / spray), proximity to cooling-
    tower drift and deluge / firewater spray patterns. Tropical and
    coastal sites carry materially higher CUI risk than arid inland.
  - **Insulation type** — leachable-chloride content, water-retention
    behaviour, hydrophobicity, ageing behaviour (binder breakdown,
    facing degradation). Calcium silicate, mineral wool, perlite,
    foam-glass, aerogel, and polyisocyanurate each have a different
    CUI-promoting profile.
  - **Jacketing / weather-barrier condition** — overlap orientation
    (shed water downward), seam sealant integrity at every penetration
    (instrument tap, hanger, support, tee, valve), drainage-hole
    presence at low points, mechanical damage from scaffolding /
    traffic / wind. The jacket is the primary moisture barrier; its
    condition gates risk severity on otherwise-vulnerable services.
  - **Age in service** — first-detected damage is commonly **>10
    years** into service. Age-since-coating-application and age-since-
    insulation-installation are both inputs to the screening score.
  - **Contaminants** — chloride and sulphate loadings on the
    insulation, dirt accumulation, drips from upstream cooling-tower
    plumes or aerial chemical injection lines, and process-side leaks
    that contaminate the insulation matrix with hydrocarbon or amine.

- **CUI screening criteria and extent-of-condition ranking.** Items
  are screened against the risk-factor matrix to yield a CUI
  susceptibility ranking. The screening output drives where insulation
  removal and direct UT are worth the scaffolding-plus-stripping cost
  versus where through-insulation methods (PEC, GWUT, profile RT) are
  appropriate. Extent-of-condition logic is the standard inspection-
  campaign procedure: a single CUI finding triggers a defined widening
  of the inspection sample around the affected circuit until the
  damage envelope is bounded.

- **Inspection methods.** The practice covers the full method
  inventory used on insulated and fireproofed equipment:
  - **Visual inspection (jacket external)** — first-pass screen for
    jacket damage, seam separation, support-band displacement,
    staining patterns indicative of through-jacket leakage.
  - **Insulation removal + UT spot** — gold-standard for direct
    thickness measurement at PEC / GWUT-flagged hot spots and on
    high-consequence circuits per the RBI plan; supports CISCC dye-
    penetrant inspection on austenitic stainless lines.
  - **Profile (or tangential) radiography (RT)** — through-insulation
    wall-thickness profiling without stripping; throughput-limited
    and access-limited.
  - **Pulsed eddy current (PEC)** — through-insulation average-
    thickness screening over large areas; good for triage, poor at
    localised pitting resolution.
  - **Guided-wave UT (GWUT)** — long-range coverage from a single
    coupling point; useful for buried, sleeved, and elevated
    insulated piping where scaffolding cost dominates.
  - **Infrared (IR) thermography** — detects wet-insulation patches
    and missing-insulation regions; does not directly image steel-
    side damage, but flags zones for follow-up.
  - **Real-time radiography (RTR)** — same physics as profile RT,
    faster image cycle for high-throughput campaigns.
  - **Spot UT (post-strip)** — direct thickness reading on the steel
    surface after localised insulation removal at flagged locations.

- **Repair and re-insulation good practice.** Surface preparation
  back to the coating-class specification (typically near-white or
  white-metal blast for high-temperature service), coating reapplication
  per the operating-T-vs-coating-class matrix (TSA — thermal-sprayed
  aluminium — is the workhorse for high-T CUI service on carbon steel
  and provides cathodic protection through holidays; immersion-grade
  epoxies and inorganic copolymer / silicone hybrids cover the
  moderate-T band), insulation reinstatement with corrected jacket
  overlap, sealant at every penetration, and drainage holes at low
  points. The practice also addresses removable jacketing at known
  wet-zone bands so subsequent inspections do not require destructive
  stripping.

- **Fireproofing-specific sub-programme.** Corrosion-under-fireproofing
  (CUF) is a related but distinct service problem: cementitious or
  lightweight concrete fireproofing on structural steel (column
  flanges, vessel skirts, cable-tray supports, pipe-rack columns) traps
  moisture against the steel substrate and accumulates chloride and
  sulphate over decades. The mitigation hierarchy parallels CUI
  (specification of the fireproofing matrix, primer / intumescent
  coating beneath, mechanical sealing at top and bottom terminations,
  drainage at base plates) but the inspection methods skew toward
  direct removal at suspect locations because through-fireproofing
  NDE is materially harder than through-insulation NDE. The 2nd
  edition expanded this sub-programme content.

- **RBI integration via the API 581 CUI damage factor.** RP 583's
  risk-factor screening output is the input that the [api-rp-581](api-rp-581.md)
  CUI damage-factor module consumes — the screening score, inspection-
  effectiveness category (A–E from [api-rp-574](api-rp-574.md)), and inspection-
  history coverage combine to drive probability-of-failure and the
  RBI inspection interval. The CUI damage factor is one of the
  longest-running modules in API 581 and has a particularly strong
  RP 583 dependency for its credibility-of-screening input.

## Cross-references

- **[api-rp-571](api-rp-571.md)** — *Damage Mechanisms Affecting Fixed Equipment in
  the Refining Industry*. CUI sits in §4 (loss-of-thickness mechanisms)
  with CISCC-CUI cross-referenced from §5 (environmentally-assisted
  cracking). RP 583 is the **programme-level practice** that operationalises
  the §4 mechanism description into a screening-and-inspection workflow.
- **[api-rp-581](api-rp-581.md)** — *Risk-Based Inspection Methodology* (quantitative).
  Consumes RP 583's screening-score and risk-factor inputs through the
  CUI damage factor; combines with [api-rp-574](api-rp-574.md) inspection-effectiveness
  factors A–E to produce the RBI POF and interval.
- **[api-510](api-510.md)** — *Pressure Vessel Inspection Code*. Parent in-service
  inspection code; defines vessel inspection intervals and item
  classification. RP 583 supplies the CUI-specific methods and risk
  factors that API 510's external-inspection clauses reference.
- **[[api-std-570]]** — *Piping Inspection Code*. Parent in-service
  inspection code for process piping. Same relationship as API 510:
  RP 583 supplies the CUI-specific methods that API 570 invokes.
- **[api-rp-574](api-rp-574.md)** — *Inspection Practices for Piping System Components*.
  Sibling inspection-RP that supplies the broader piping-component NDE
  framework (CML selection, UT spot vs. scan, off-stream vs. on-stream).
  RP 583 is the **CUI-specialisation** of that framework — the
  inspection-effectiveness factors A–E from RP 574 apply to RP 583's
  through-insulation methods and gate the API 581 RBI POF.
- **[api-rp-577](api-rp-577.md)** — *Welding Inspection and Metallurgy*. Complementary
  NDE-method reference; the surface-NDE techniques (MT, PT, PAUT) used
  on RP 583's insulation-removal-plus-direct-inspection windows are
  documented in RP 577 from the welding-inspection perspective and
  apply equally to repair-weld inspection during CUI repairs.
- **[corrosion-under-insulation](../concepts/corrosion-under-insulation.md)** — concept-page consumer; bidirectional
  link target. The concept page forward-references RP 583 in its
  *Standards* section; this page is the standards-side anchor.
- **[risk-based-inspection](../concepts/risk-based-inspection.md)** — concept-page consumer; RP 583's
  screening output is one of the named damage-factor inputs to the
  RBI workflow.
- **NACE / AMPP SP0198** — *Control of Corrosion Under Thermal Insulation
  and Fireproofing Materials*. Parallel-scope AMPP standard covering the
  same problem from the materials-control / coatings-selection direction.
  Practitioners read both. **Future-promotion candidate** — not yet a
  page in this wiki; track for ingest with the next AMPP-SP batch.
- **API 12T** — *Recommended Practice for Tank Coatings* (water-injection
  and similar tank service). Adjacent in scope on the coating-selection
  side; CUI / CUF coatings on insulated tanks intersect with the tank-
  coating practice. **Future-promotion candidate**.
- **API RP 690** — *Insulation specification* (insulation-system
  specification family). Adjacent on the insulation-selection side; RP
  690 governs the leachable-chloride content, water-retention behaviour,
  and ageing properties of the insulation that RP 583 then asks the
  inspection programme to live with. **Future-promotion candidate** —
  surface against the insulation-selection-side canon when the AMPP
  SP0198 page lands.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground CUI/CUF programme outputs (CUI screening scores,
extent-of-condition envelopes, through-insulation NDE method selection,
CUI damage-factor inputs to RBI) against this practice. It also closes
the bidirectional link from the [corrosion-under-insulation](../concepts/corrosion-under-insulation.md) concept
page, which has previously listed RP 583 as a *future-promotion
candidate*. **Metadata-only** per spinout 2026-05-05 governance: no
clause text, screening-threshold tables, NDE acceptance tables, or
coating-class-vs-temperature tabulations are reproduced here.

## Where to find the full text

- **Not-on-disk** in `/mnt/ace/O&G-Standards/_catalog.json` (catalog
  generation 2025-12-25, 27,343 documents): zero hits on
  `organization=API` AND `doc_number=583`, zero filename hits. Forward-
  adopt the publisher edition when a catalog copy is added.
- API publisher catalog: <https://www.api.org/products-and-services/standards>
- Practitioner usage: invoked through API 510 / 570 / 653 inspection
  programmes and through API 581 RBI; not cited as a standalone
  compliance authority.

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  the API source page lists the inspection-RP cluster (510, 570, 572,
  574, 576, 578, 580, 581, 582) but does **not** currently enumerate
  RP 583. This page is the standards-side entry that should drive a
  follow-on update to extend the cluster listing on the source page.
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` —
  no entry; `revision: not-on-disk` per spinout governance.
