---
title: "Stress-Corrosion Cracking (SCC) — Variants and Industry Coverage"
slug: stress-corrosion-cracking
tags:
  - scc
  - environmental-cracking
  - chloride-scc
  - caustic-scc
  - amine-scc
  - polythionic
  - carbonate
  - nitrate
  - ammonia
  - ssc
  - refinery
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/iso-15156.md
---

# Stress-Corrosion Cracking (SCC) — Variants and Industry Coverage

> Concept anchor for the **environmental-cracking family** that spans
> refinery, upstream, midstream, and offshore service. Bidirectional with
> [[hydrogen-embrittlement]] (the hydrogen-driven branch),
> [[sour-service-materials]] (the SSC + HIC subset), and
> [[damage-mechanism-screening]] (the API RP 571 catalogue route).

## What is SCC?

**Stress-corrosion cracking (SCC)** is sub-critical, environmentally-assisted
**brittle cracking** of an otherwise-ductile alloy under sustained tensile
stress in a specific corrodent environment. The defining feature is that
cracks propagate at applied stress-intensity factors `K_app` well below the
plane-strain fracture toughness `K_Ic` of the un-charged alloy — meaning a
component nominally below its mechanical-design fracture envelope still
fails by slow crack growth once the environment is wrong.

Three conditions must hold simultaneously for SCC to occur:

1. **Susceptible material** — a specific alloy / heat-treatment combination
   that the environment can attack in the SCC mode (e.g., sensitized
   austenitic stainless in chlorides; high-strength steel in wet H2S).
2. **Tensile stress** — applied (operating pressure / external load) or
   residual (welding, cold work, fit-up). Compressive stress arrests SCC,
   which is why shot-peening and weld-overlay residual-stress
   redistribution are recurring mitigations.
3. **Specific corrodent environment** — chlorides, caustic, amines, wet
   H2S, polythionic acid, carbonates, ammonia, nitrates, or aqueous
   electrolyte plus a hydrogen-charge source — each cracks a distinct
   alloy family. Wrong corrodent → no SCC even if material and stress
   align.

Crack propagation proceeds via **dissolution-and-repassivation cycles**
at the strained crack tip (anodic-dissolution-driven variants) or via
**hydrogen ingress and lattice embrittlement** at the crack-tip plastic
zone (hydrogen-driven variants — see [[hydrogen-embrittlement]]). Both
families produce branched, transgranular or intergranular crack
morphologies that distinguish SCC from mechanical fatigue or single-cycle
overload.

## SCC variants in oil and gas / refining

The umbrella catalogue below lists the SCC variants that recur across
upstream, midstream, refining, and offshore service. Reference standards
are the umbrella catalogue ([[api-rp-571]]), the sour-service materials
code ([[iso-15156]] / AMPP MR0175), the SSC test method
([[ampp-tm-0177]]), and the duplex-SS HISC governance ([[dnv-rp-f112]]).

| Variant | Susceptible material | Environment | Reference standard |
|---------|----------------------|-------------|--------------------|
| **Cl-SCC of austenitic SS** | 304L / 316L; sensitized HAZs especially | Chlorides + tensile stress + ~60–205 °C | [[api-rp-571]] §4.5; ASME PCC-3; chloride-content + temperature envelope per project MDS |
| **Caustic SCC** ("caustic embrittlement") | Carbon and low-alloy steel | NaOH / KOH > ~2 wt%, ~50–90 °C window (per API 571 caustic chart) | [[api-rp-571]] §4.5 family; NACE SP0403 (operator practice — flagged for ingest) |
| **Amine SCC** | Carbon steel, especially welded | Lean / rich amine (MEA, DEA, MDEA), ~50–100 °C, residual-stress-driven | [[api-rp-571]] §4.5 family; PWHT mitigation per [[asme-bpvc-viii-1]] / [[asme-bpvc-viii-2]] |
| **Sulfide stress cracking (SSC)** | Carbon + low-alloy steels (hardness-controlled); CRAs (composition-and-cold-work-controlled) | Wet H2S + tensile stress (sour service) | [[iso-15156]] / [[ampp-mr-0175-pt2]] / [[ampp-mr-0175-pt3]]; test method [[ampp-tm-0177]] |
| **HIC / SOHIC** | Carbon-steel plate (HIC stress-independent; SOHIC stress-dependent) | Wet H2S | [[iso-15156]] / [[ampp-mr-0175-pt2]]; test method [[ampp-tm-0284]] |
| **Polythionic acid SCC (PTASCC)** | Sensitized austenitic SS (304/321/347 in FCC, HDS, HCK service) | H2S + air + condensate at shutdown — forms `H2S_xO_6` polythionic species | [[api-rp-571]] §4.5; NACE SP0170 mitigation practice (flagged for ingest) |
| **Carbonate SCC** | Carbon steel | CO3²⁻ / HCO3⁻ alkaline waters + tensile stress (FCC overhead, alkaline-sour environments) | [[api-rp-571]] §4.5 |
| **Ammonia SCC** | Brass / aluminum brass (heat-exchanger tubing) | NH3 + tensile + moisture + trace O2 | [[api-rp-571]] §4.5 |
| **Nitrate SCC** | Carbon steel | NO3⁻ + tensile stress + elevated temperature (boiler / heater service) | [[api-rp-571]] §4.5 |
| **Hydrogen SCC of high-strength steel** | UTS / SMYS above ~950 MPa (riser-tensioner rods, mooring shackles, subsea bolting) | Aqueous + cathodic charge from CP or wet H2S | [[api-rp-571]] §4.5; [[dnv-rp-f112]] (CRA HISC, the related CP-driven mode); see [[hydrogen-embrittlement]] |

API RP 571 §4.5 family is the umbrella catalogue cross-referenced
throughout — verify per-variant section numbers against the publisher
source as RP 571 revisions reorganize the §4.5 sub-clauses.

## Common-thread mechanisms

Three propagation mechanisms underlie the variants above. The same
environment can drive different mechanisms on different alloys, and the
same alloy can crack by different mechanisms depending on the corrodent.

- **Anodic-dissolution-driven SCC.** Crack-tip strain ruptures the
  passive film; bare metal anodically dissolves; the surrounding still-
  passive surface acts as a large cathode; partial repassivation occurs
  before the next strain-rupture event, and the cycle repeats. Selective
  dissolution along strained grain boundaries (intergranular) or along
  active slip planes (transgranular) drives crack advance. Examples:
  Cl-SCC of austenitic SS, polythionic SCC (intergranular at sensitized
  Cr-depleted boundaries), some caustic-SCC mechanisms.
- **Hydrogen-embrittlement-driven SCC.** Atomic hydrogen liberated by
  the cathodic reaction (or by sulfide-poisoned recombination at H2S
  surfaces) ingresses into the lattice, accumulates at trapping sites in
  the crack-tip plastic zone, and embrittles the local ductility /
  toughness. Examples: SSC of carbon steel and CRAs, HISC of duplex SS
  under cathodic protection, HE of high-strength steel in marine + CP
  service. See [[hydrogen-embrittlement]] for the full hydrogen-source
  taxonomy and the HISC / HIC / SOHIC subdivision.
- **Surface-film-rupture-driven SCC.** A protective surface film
  (magnetite in caustic service, FeCO3 in carbonate service, an amine-
  passivation layer in amine service) repeatedly ruptures and reforms at
  the crack tip under tensile strain; the bared metal corrodes between
  reforming events. Mechanistically a sub-class of anodic-dissolution
  SCC but useful to call out separately because the design lever
  (control film integrity via temperature and chemistry) is distinct
  from grain-boundary-sensitization control. Examples: caustic SCC,
  amine SCC, carbonate SCC.

The mechanism family determines the mitigation lever — anodic-dissolution
variants respond to potential control, deaeration, and inhibitor
addition; hydrogen-driven variants respond to hardness control, CP-
potential ceiling, and post-weld baking; film-rupture variants respond to
temperature and concentration limits and to PWHT to redistribute residual
stress.

## Test methods

| Method | Standard | Notes |
|--------|----------|-------|
| Boiling MgCl2 (Cl-SCC screen) | ASTM G36 | 154 °C boiling-MgCl2 immersion; rapid Cl-SCC ranking on austenitic SS |
| C-ring (any SCC environment) | ASTM G38 | Stressed C-ring specimen; fixture-defined elastic stress; environment per project |
| Bent-beam (any SCC environment) | ASTM G39 | Two/three/four-point bent beam; constant strain; environment per project |
| Alternate immersion | ASTM G44 | 3.5 % NaCl alternate-immersion 10 min in / 50 min out; high-strength alloy SCC ranking |
| Tension specimens (general) | ASTM G47 | Aluminum-alloy SCC test in alternate-immersion 3.5 % NaCl |
| U-bend (any SCC environment) | ASTM G64 | Severe plastic-strain U-bend specimen; pass/fail screening |
| Slow-strain-rate (SSRT) | ASTM G129 | Constant low strain-rate (~10⁻⁶ s⁻¹) tensile test in environment; ductility-loss ratio quantifies SCC susceptibility |
| Sulfide stress cracking | [[ampp-tm-0177]] | Methods A (uniaxial), B (bent beam), C (C-ring), D (DCB / `K_ISSC`) in deaerated H2S-saturated NACE solutions |
| HIC plate test | [[ampp-tm-0284]] | 96-h H2S-saturated immersion; CLR / CTR / CSR metallographic acceptance |
| DSS HISC under CP | [[dnv-rp-f112]] | Project-test envelope: CP potential, residual-stress, design-stress, surface-finish controls |
| Caustic SCC test | NACE TM-0103 | Caustic-cracking susceptibility test (flagged for ingest) |

ASTM G36 / G38 / G39 / G44 / G47 / G64 / G129 do not yet have dedicated
standards pages in this wiki — flagged for ingest as the ASTM G-series
catalogue expands beyond the existing [[astm-g48]] anchor.

## Standards

Bidirectional links to the standards-page resolvers (each carries
`code_id`, `publisher`, `revision` frontmatter per the wiki schema):

- [[api-rp-571]] — *Damage Mechanisms Affecting Fixed Equipment in the
  Refining Industry.* Umbrella catalogue for the SCC variant family
  (Cl-SCC, caustic, amine, polythionic, carbonate, ammonia, nitrate,
  hydrogen SCC of high-strength steel). Each variant carries
  susceptibility envelope, morphology description, inspection guidance,
  and mitigation cross-references.
- [[iso-15156]] — *Materials for Use in H2S-Containing Environments in
  Oil and Gas Production.* Three-part joint publication
  (ISO 15156-1/-2/-3 = NACE MR0175 = AMPP MR0175); covers the SSC, HIC,
  and SOHIC sub-family of SCC for sour service.
- [[ampp-mr-0175-pt2]] — *Carbon and Low-Alloy Steels and the Use of
  Cast Iron.* Hardness, heat-treatment, and welding controls for
  carbon-steel SSC, HIC, and SOHIC qualification.
- [[ampp-mr-0175-pt3]] — *Cracking-Resistant CRAs and Other Alloys.*
  Per-alloy temperature/chloride/pH2S envelopes for SSC variants on
  13Cr martensitic, duplex, super-duplex, austenitic, and Ni-base
  alloys.
- [[ampp-tm-0177]] — *NACE TM-0177 SSC Laboratory Test Methods.*
  Methods A (uniaxial), B (bent beam), C (C-ring), D (DCB / `K_ISSC`)
  for SSC qualification.
- [[ampp-tm-0284]] — *NACE TM-0284 HIC Test Method.* 96-h H2S-saturated
  plate-coupon immersion; CLR / CTR / CSR acceptance.
- [[api-rp-581]] — *Risk-Based Inspection Methodology.* Damage-factor
  modules for multiple SCC families (Cl-SCC, caustic, amine, sulfide,
  polythionic, carbonate, HF, HIC/SOHIC) consume the API RP 571
  susceptibility-envelope catalogue.
- [[dnv-rp-f112]] — *Design of Duplex SS Subsea Equipment Exposed to
  Cathodic Protection.* Governs the HISC sub-family of hydrogen-driven
  SCC on duplex / super-duplex CRAs in CP-protected subsea service.

## Related concepts

- [[hydrogen-embrittlement]] — the hydrogen-driven branch of the SCC
  family (SSC, HIC, SOHIC, HISC, HE of high-strength steel); shares the
  upstream hydrogen-source taxonomy and the trapping-site / lattice-
  embrittlement mechanism.
- [[sour-service-materials]] — SSC + HIC + SOHIC subset of SCC; the
  H2S-specific qualification chain via TM-0177, TM-0284, and the
  Region 0–3 severity zoning of [[ampp-mr-0175-pt2]].
- [[damage-mechanism-screening]] — RBI / inspection-program entry
  point that consumes the API RP 571 SCC catalogue and routes each
  unit's SCC-susceptibility evidence into [[risk-based-inspection]] /
  [[api-rp-581]].
- [[pitting-and-crevice-corrosion]] — pits frequently nucleate the
  SCC initiation site (chloride pit → Cl-SCC of austenitic SS;
  sulfide pit → SSC at pit root); CPT/CCT envelopes set the chloride-
  temperature operating window upstream of the SCC susceptibility
  analysis.
- [[corrosion-rate-measurement]] — uniform-corrosion-rate techniques
  (LPR, ER probes, mass-loss coupons) measure a fundamentally
  different damage form. SCC is **depth-driven not rate-driven**: a
  zero-uniform-rate environment can still harbour an SCC failure if
  the susceptibility triangle (material + stress + corrodent) closes.
  Inspection programs must instrument for SCC separately
  (e.g., wet-fluorescent MT, eddy-current array, phased-array UT) and
  not infer absence-of-SCC from low corrosion-rate readings.

## Source materials

- [O&G Standards catalog — API](../sources/og-standards-api.md) —
  catalog summary for the API slice of the consolidated standards
  mount, including API RP 571 (damage-mechanism umbrella) and
  API RP 581 (RBI methodology).
- [O&G Standards catalog — ISO](../sources/og-standards-iso.md) —
  catalog summary for the ISO slice, including ISO 15156 1st-edition
  three-part PDFs (Pt-1 / Pt-2 / Pt-3).

Vendor PDFs are read-only at the consolidated standards mount and never
enter this repo per the spinout 2026-05-05 governance and the
vendor-derivative firewall in the repo-root `CLAUDE.md`.
