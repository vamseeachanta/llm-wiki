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
last_updated: 2026-05-10
domain: engineering-standards
sources:
  - standards/api-rp-571.md
  - standards/iso-15156.md
---

# Stress-Corrosion Cracking (SCC) — Variants and Industry Coverage

> Concept anchor for the **environmental-cracking family** that spans
> refinery, upstream, midstream, and offshore service. Bidirectional with
> [hydrogen-embrittlement](hydrogen-embrittlement.md) (the hydrogen-driven branch),
> [sour-service-materials](sour-service-materials.md) (the SSC + HIC subset), and
> [damage-mechanism-screening](damage-mechanism-screening.md) (the API RP 571 catalogue route).

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
zone (hydrogen-driven variants — see [hydrogen-embrittlement](hydrogen-embrittlement.md)). Both
families produce branched, transgranular or intergranular crack
morphologies that distinguish SCC from mechanical fatigue or single-cycle
overload.

The kinetic signature is also distinct. Once the susceptibility triangle
closes, SCC growth rates typically lie in the band
`da/dt ≈ 10⁻¹¹ to 10⁻⁷ m/s` — slow enough that a single inspection
campaign may miss the crack, fast enough that a missed inspection
interval can take the flaw past the [api-std-579](../standards/api-std-579.md) Part 9 critical
size before the next outage. Threshold stress-intensity factors `K_ISCC`
(anodic-dissolution variants) and `K_ISSC` (sulfide-driven variants)
define the lower bound below which crack-like flaws will not propagate
in a given environment; both are environment-and-alloy-specific
quantities and must be measured per the test catalogue below rather than
back-calculated from `K_Ic`. The relationship between SCC kinetics, the
[fatigue-crack-growth](fatigue-crack-growth.md) `da/dN` curve, and the [engineering-critical-assessment](engineering-critical-assessment.md)
remaining-life envelope is the principal coupling SCC introduces into
the fixed-equipment integrity chain.

## SCC variants in oil and gas / refining

The umbrella catalogue below lists the SCC variants that recur across
upstream, midstream, refining, and offshore service. Reference standards
are the umbrella catalogue ([api-rp-571](../standards/api-rp-571.md)), the sour-service materials
code ([iso-15156](../standards/iso-15156.md) / AMPP MR0175), the SSC test method
([ampp-tm-0177](../standards/ampp-tm-0177.md)), and the duplex-SS HISC governance ([dnv-rp-f112](../standards/dnv-rp-f112.md)).

| Variant | Susceptible material | Environment | Reference standard |
|---------|----------------------|-------------|--------------------|
| **Cl-SCC of austenitic SS** | 304L / 316L; sensitized HAZs especially | Chlorides + tensile stress + ~60–205 °C | [api-rp-571](../standards/api-rp-571.md) §4.5; ASME PCC-3; chloride-content + temperature envelope per project MDS |
| **Caustic SCC** ("caustic embrittlement") | Carbon and low-alloy steel | NaOH / KOH > ~2 wt%, ~50–90 °C window (per API 571 caustic chart) | [api-rp-571](../standards/api-rp-571.md) §4.5 family; NACE SP0403 (operator practice — flagged for ingest) |
| **Amine SCC** | Carbon steel, especially welded | Lean / rich amine (MEA, DEA, MDEA), ~50–100 °C, residual-stress-driven | [api-rp-571](../standards/api-rp-571.md) §4.5 family; PWHT mitigation per [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) / [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) |
| **Sulfide stress cracking (SSC)** | Carbon + low-alloy steels (hardness-controlled); CRAs (composition-and-cold-work-controlled) | Wet H2S + tensile stress (sour service) | [iso-15156](../standards/iso-15156.md) / [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) / [ampp-mr-0175-pt3](../standards/ampp-mr-0175-pt3.md); test method [ampp-tm-0177](../standards/ampp-tm-0177.md) |
| **HIC / SOHIC** | Carbon-steel plate (HIC stress-independent; SOHIC stress-dependent) | Wet H2S | [iso-15156](../standards/iso-15156.md) / [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md); test method [ampp-tm-0284](../standards/ampp-tm-0284.md) |
| **Polythionic acid SCC (PTASCC)** | Sensitized austenitic SS (304/321/347 in FCC, HDS, HCK service) | H2S + air + condensate at shutdown — forms `H2S_xO_6` polythionic species | [api-rp-571](../standards/api-rp-571.md) §4.5; NACE SP0170 mitigation practice (flagged for ingest) |
| **Carbonate SCC** | Carbon steel | CO3²⁻ / HCO3⁻ alkaline waters + tensile stress (FCC overhead, alkaline-sour environments) | [api-rp-571](../standards/api-rp-571.md) §4.5 |
| **Ammonia SCC** | Brass / aluminum brass (heat-exchanger tubing) | NH3 + tensile + moisture + trace O2 | [api-rp-571](../standards/api-rp-571.md) §4.5 |
| **Nitrate SCC** | Carbon steel | NO3⁻ + tensile stress + elevated temperature (boiler / heater service) | [api-rp-571](../standards/api-rp-571.md) §4.5 |
| **Hydrogen SCC of high-strength steel** | UTS / SMYS above ~950 MPa (riser-tensioner rods, mooring shackles, subsea bolting) | Aqueous + cathodic charge from CP or wet H2S | [api-rp-571](../standards/api-rp-571.md) §4.5; [dnv-rp-f112](../standards/dnv-rp-f112.md) (CRA HISC, the related CP-driven mode); see [hydrogen-embrittlement](hydrogen-embrittlement.md) |

API RP 571 §4.5 family is the umbrella catalogue cross-referenced
throughout — verify per-variant section numbers against the publisher
source as RP 571 revisions reorganize the §4.5 sub-clauses.

### Material-environment combinations beyond the refining catalogue

The variants tabulated above concentrate on oil-and-gas / refining
service, but the material-environment pairings extend across marine,
power, and process industries. The five canonical pairings every
materials engineer should recognize:

| Material family | Aggressive environment | Variant name | Mechanism class | Typical service |
|-----------------|------------------------|--------------|-----------------|------------------|
| Austenitic stainless (304/316/321/347) | Cl⁻ + tensile + ~60–205 °C | Cl-SCC | Anodic dissolution / film rupture | Refinery overheads, seawater coolers, marine handrails, insulation-condensate trace |
| Carbon and low-alloy steel (welded, residual stress) | NaOH / KOH > 2 wt% in 50–90 °C window | Caustic SCC ("caustic embrittlement") | Film rupture | Boilers, caustic injection, evaporators, alkylation neutralization |
| Aluminum 2xxx / 7xxx (high-strength, peak-aged) | Chloride aqueous + alternate-immersion / marine atmosphere | Al-SCC (alternate-immersion regime) | Anodic dissolution at grain boundaries (intergranular) + hydrogen-assist branch | Aerospace structural, marine fasteners, offshore lightweight platforms |
| Titanium (commercially pure, near-α, α-β) | Methanol / red-fuming nitric acid / hot dry chloride at > ~290 °C | Ti-SCC | Anodic dissolution + hydride-cracking branch | Aerospace storage tanks, methanol-handling, hot-chloride heat exchangers |
| Cu / brass (α + β phase, residual stress from cold-form) | NH3 / NH4⁺ + moisture + trace O2 | Season-cracking / ammonia SCC | Tarnish-rupture (Cu film) | Heat-exchanger tubing, marine fittings, refrigeration / fertilizer plants |

Two extra reminders sit alongside the table. First, **temperature is not
just a kinetics knob, it gates the variant.** Cl-SCC of 304L is
historically reported to have an effective lower bound near 60 °C
because slower repassivation rates below that threshold let the surface
re-passivate before the next strain event. Second, **chloride
concentration interacts with pit chemistry, not bulk fluid chemistry.**
A bulk fluid at 100 ppm Cl⁻ can generate pit-bottom electrolyte at
several percent Cl⁻ once the pit-surface area ratio shrinks — see
[pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) for the pit-chemistry-evolution
mechanism that nucleates Cl-SCC on austenitic stainless.

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
  service. See [hydrogen-embrittlement](hydrogen-embrittlement.md) for the full hydrogen-source
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

### Multi-criteria mechanism comparison

The three mechanism classes can be distinguished on six criteria that
matter operationally — fractography, kinetics, mitigation lever,
inspection method, design code touchpoint, and reversibility. The same
variant can shift mechanism class as conditions move (e.g., caustic SCC
crosses from film-rupture into hydrogen-assisted territory near
~85 °C / high concentration), so the criteria below describe the
**dominant** mode for each class.

| Criterion | Anodic-dissolution SCC | Hydrogen-driven SCC | Film-rupture SCC |
|-----------|-----------------------|---------------------|------------------|
| Crack path (typical) | Transgranular branched (Cl-SCC) or intergranular at sensitized boundaries (PTASCC) | Transgranular cleavage-like in CS / quasi-cleavage in CRAs; intergranular in high-strength steel | Intergranular along grain boundaries decorated with film-discontinuity sites |
| Growth rate band | `10⁻¹⁰ to 10⁻⁸ m/s` once active | `10⁻⁹ to 10⁻⁶ m/s`; sensitive to CP overpotential | `10⁻¹¹ to 10⁻⁹ m/s`; sensitive to film-reform kinetics |
| Threshold parameter | `K_ISCC` (per [astm-g129](../standards/astm-g129.md) SSRT extrapolation or DCB testing) | `K_ISSC` per [ampp-tm-0177](../standards/ampp-tm-0177.md) Method D (DCB) | Concentration-temperature envelope (no `K_ISCC` published for many film-rupture variants) |
| Primary mitigation | Inhibitor / deaeration; chloride excursion limits; sensitization control via L-grade | Hardness ceiling (≤ 22 HRC for CS sour service); CP potential window; H-bake after plating | PWHT to lower residual stress; concentration / temperature window control |
| Inspection method | Wet-fluorescent MT, dye-pen, eddy-current array on austenitic SS surfaces | Phased-array UT (TFM / FMC) for embedded HIC/SOHIC; AUT for sour-service welds | Visual + WFMT after PWHT verification; intrusive inspection of caustic-injection nozzles |
| Reversibility | Crack growth halts when corrodent removed (no post-cracking propagation) | Hydrogen can be partially baked out from un-cracked regions; cracks themselves are not reversible | Crack growth halts when temperature / concentration moves out of envelope |
| Code touchpoint | [api-rp-571](../standards/api-rp-571.md) §4.5 family + [api-rp-581](../standards/api-rp-581.md) damage factors | [iso-15156](../standards/iso-15156.md) (sour) + [dnv-rp-f112](../standards/dnv-rp-f112.md) (HISC) | [api-rp-571](../standards/api-rp-571.md) §4.5 caustic / amine / carbonate; PWHT requirements per [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) UCS-56 |

The criteria interlock with [damage-mechanism-screening](damage-mechanism-screening.md) and
[api-rp-583](../standards/api-rp-583.md) inspection-program design: anodic-dissolution variants
are caught by surface-techniques while hydrogen-driven variants
mandate volumetric techniques because the cracks grow embedded.

### Worked-example named incidents

Three named incidents illustrate the material-environment-mechanism
mapping in the field. Each example threads the SCC triangle (material,
stress, environment) through the failure narrative; details are kept at
the publicly-documented level and not reproduced from copyrighted
incident reports.

**Worked example 1 — refinery FCC fractionator overhead (Cl-SCC of
304L).** A type-304L stainless overhead piping spool in a fluid
catalytic cracker fractionator developed transgranular branched cracks
within ~18 months of a reboiler upset that forced overhead temperatures
into the 130–170 °C window with chloride salt deposition from an
upstream caustic-injection imbalance. The SCC triangle: 304L (post-weld
sensitized HAZ — material), residual welding stress + operating pressure
(stress), wet chloride deposit at the elevated temperature (corrodent).
Mechanism: anodic-dissolution + film-rupture at the strained crack tip
on a sensitized HAZ. Mitigation lever applied: switch overhead corrosion
control to a film-forming amine and tighten chloride monitoring
([api-rp-571](../standards/api-rp-571.md) §4.5 chloride-SCC subsection); subsequent inspection
campaign added eddy-current array on the affected spool — see
[risk-based-inspection](risk-based-inspection.md) for how the consequence-of-failure tier
is recalculated post-incident.

**Worked example 2 — offshore platform mooring shackle (HE of
high-strength steel under CP).** A high-strength quenched-and-tempered
mooring shackle on a deepwater FPSO experienced sub-critical cracking
within several thousand operating hours of installation. The SCC
triangle: AISI 4340-class high-strength steel above ~950 MPa SMYS
(material), tensile pre-load + cyclic operational load (stress),
seawater + cathodic-protection overpotential at the surface (corrodent —
hydrogen-charge source). Mechanism: hydrogen embrittlement from CP
hydrogen evolution at the sacrificial-anode-protected surface,
exacerbated by hardness above the [iso-15156](../standards/iso-15156.md) /
[ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) ceiling for sour-service applications even though
the service was nominally sweet. Mitigation lever applied: lower the
material strength / hardness ceiling, cap the CP potential at ICCP
control rather than bulk-anode, and apply [dnv-rp-f112](../standards/dnv-rp-f112.md)-style
hydrogen-charging qualification to the bolting class — see
[hydrogen-embrittlement](hydrogen-embrittlement.md) for the full hydrogen-source taxonomy that
governs this regime.

**Worked example 3 — refinery process vessel (caustic embrittlement).**
A carbon-steel evaporator vessel handling 25–40 wt% NaOH at 85 °C
developed intergranular cracks at the toe of an unrelieved fillet weld
within ~24 months of commissioning. The SCC triangle: ASTM A516 Gr 70
plate at as-welded residual stress (material, with stress combined),
above-yield welding residual stress at the weld toe (stress), strong-
caustic process fluid at the high-risk corner of the API 571 caustic-
SCC chart (corrodent). Mechanism: film-rupture of the magnetite-passive
layer with selective grain-boundary attack. Mitigation lever applied:
post-weld heat treatment per [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) UCS-56 stress-relief
schedule plus operational reset of the caustic concentration cap; the
post-incident inspection plan upgraded WFMT coverage of caustic-side
welds to 100% per outage cycle. The case is the canonical illustration
of why caustic-service vessels mandate PWHT regardless of thickness —
the residual stress magnitude, not the membrane stress, drives the
failure.

The three incidents share a structure that recurs across SCC
investigations: (1) the susceptibility triangle was already closed at
commissioning but not recognized; (2) inspection coverage targeted
uniform-corrosion-rate metrics rather than crack-detection methods; and
(3) the operational excursion or design feature that closed the
triangle was external to the original materials-selection envelope.
This is why [api-rp-571](../standards/api-rp-571.md)-driven [damage-mechanism-screening](damage-mechanism-screening.md) is
the entry gate for SCC management — the screening exercise forces
recognition of the triangle before metallurgy is locked in.

## Test methods

| Method | Standard | Notes |
|--------|----------|-------|
| SCC test specimen / fixture overview | [astm-g30](../standards/astm-g30.md) | Standard practice for U-bend; covers fabrication, stressing, and exposure of stressed bent-strip specimens |
| Boiling MgCl2 (Cl-SCC screen) | [astm-g36](../standards/astm-g36.md) | 154 °C boiling-MgCl2 immersion; rapid Cl-SCC ranking on austenitic SS |
| C-ring (any SCC environment) | [astm-g38](../standards/astm-g38.md) | Stressed C-ring specimen; fixture-defined elastic stress; environment per project |
| Bent-beam (any SCC environment) | [astm-g39](../standards/astm-g39.md) | Two/three/four-point bent beam; constant strain; environment per project |
| Alternate immersion | [astm-g44](../standards/astm-g44.md) | 3.5 % NaCl alternate-immersion 10 min in / 50 min out; high-strength alloy SCC ranking |
| Tension specimens (general) | [astm-g47](../standards/astm-g47.md) | Aluminum-alloy SCC test in alternate-immersion 3.5 % NaCl |
| U-bend (any SCC environment) | [astm-g64](../standards/astm-g64.md) | Severe plastic-strain U-bend specimen; pass/fail screening of resistance classes |
| SCC of Al alloy weldments | [astm-g78](../standards/astm-g78.md) | Crevice corrosion / SCC test of weldments in flowing seawater; aluminum and other alloys |
| Boldly-exposed corrosion under cyclic-wet conditions | [astm-g123](../standards/astm-g123.md) | Boiling acid-chloride test for Cl-SCC ranking with environmental cycling |
| Slow-strain-rate (SSRT) | [astm-g129](../standards/astm-g129.md) | Constant low strain-rate (~10⁻⁶ s⁻¹) tensile test in environment; ductility-loss ratio quantifies SCC susceptibility |
| Sulfide stress cracking | [ampp-tm-0177](../standards/ampp-tm-0177.md) | Methods A (uniaxial), B (bent beam), C (C-ring), D (DCB / `K_ISSC`) in deaerated H2S-saturated NACE solutions |
| HIC plate test | [ampp-tm-0284](../standards/ampp-tm-0284.md) | 96-h H2S-saturated immersion; CLR / CTR / CSR metallographic acceptance |
| DSS HISC under CP | [dnv-rp-f112](../standards/dnv-rp-f112.md) | Project-test envelope: CP potential, residual-stress, design-stress, surface-finish controls |
| Caustic SCC test | NACE TM-0103 | Caustic-cracking susceptibility test (flagged for ingest) |

The ASTM G-series stub resolvers ([astm-g30](../standards/astm-g30.md),
[astm-g36](../standards/astm-g36.md), [astm-g38](../standards/astm-g38.md),
[astm-g39](../standards/astm-g39.md), [astm-g44](../standards/astm-g44.md),
[astm-g47](../standards/astm-g47.md), [astm-g64](../standards/astm-g64.md),
[astm-g78](../standards/astm-g78.md), [astm-g123](../standards/astm-g123.md),
[astm-g129](../standards/astm-g129.md)) carry only the L0 frontmatter
(`code_id`, `publisher`, `revision`) plus a one-line scope summary at
this revision; they will deepen as the ASTM G-series catalogue expands
beyond the existing [astm-g48](../standards/astm-g48.md) pitting/crevice
anchor and the [astm-g15](../standards/astm-g15.md) /
[astm-g16](../standards/astm-g16.md) terminology and statistical-
treatment pair. Test-method selection is mechanism-driven: SSRT
([astm-g129](../standards/astm-g129.md)) is the universal screening
test because it accelerates SCC by forcing strain-rate-induced film
rupture, while constant-load DCB ([ampp-tm-0177](../standards/ampp-tm-0177.md) Method D)
is preferred when a `K_ISSC` value is required for engineering-critical-
assessment input — see [engineering-critical-assessment](engineering-critical-assessment.md) for how
test-derived thresholds feed the [api-std-579](../standards/api-std-579.md) Part 9 crack-like-flaw
remaining-life calculation.

## Standards

Bidirectional links to the standards-page resolvers (each carries
`code_id`, `publisher`, `revision` frontmatter per the wiki schema):

- [api-rp-571](../standards/api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the
  Refining Industry.* Umbrella catalogue for the SCC variant family
  (Cl-SCC, caustic, amine, polythionic, carbonate, ammonia, nitrate,
  hydrogen SCC of high-strength steel). Each variant carries
  susceptibility envelope, morphology description, inspection guidance,
  and mitigation cross-references.
- [iso-15156](../standards/iso-15156.md) — *Materials for Use in H2S-Containing Environments in
  Oil and Gas Production.* Three-part joint publication
  (ISO 15156-1/-2/-3 = NACE MR0175 = AMPP MR0175); covers the SSC, HIC,
  and SOHIC sub-family of SCC for sour service.
- [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) — *Carbon and Low-Alloy Steels and the Use of
  Cast Iron.* Hardness, heat-treatment, and welding controls for
  carbon-steel SSC, HIC, and SOHIC qualification.
- [ampp-mr-0175-pt3](../standards/ampp-mr-0175-pt3.md) — *Cracking-Resistant CRAs and Other Alloys.*
  Per-alloy temperature/chloride/pH2S envelopes for SSC variants on
  13Cr martensitic, duplex, super-duplex, austenitic, and Ni-base
  alloys.
- [ampp-tm-0177](../standards/ampp-tm-0177.md) — *NACE TM-0177 SSC Laboratory Test Methods.*
  Methods A (uniaxial), B (bent beam), C (C-ring), D (DCB / `K_ISSC`)
  for SSC qualification.
- [ampp-tm-0284](../standards/ampp-tm-0284.md) — *NACE TM-0284 HIC Test Method.* 96-h H2S-saturated
  plate-coupon immersion; CLR / CTR / CSR acceptance.
- [api-rp-581](../standards/api-rp-581.md) — *Risk-Based Inspection Methodology.* Damage-factor
  modules for multiple SCC families (Cl-SCC, caustic, amine, sulfide,
  polythionic, carbonate, HF, HIC/SOHIC) consume the API RP 571
  susceptibility-envelope catalogue.
- [dnv-rp-f112](../standards/dnv-rp-f112.md) — *Design of Duplex SS Subsea Equipment Exposed to
  Cathodic Protection.* Governs the HISC sub-family of hydrogen-driven
  SCC on duplex / super-duplex CRAs in CP-protected subsea service.
- [api-rp-580](../standards/api-rp-580.md) — *Risk-Based Inspection.* The qualitative-RBI
  procedure document that pairs with [api-rp-581](../standards/api-rp-581.md)'s quantitative
  damage factors; SCC susceptibility flows from
  [damage-mechanism-screening](damage-mechanism-screening.md) into the RP 580 prioritization grid.
- [api-rp-583](../standards/api-rp-583.md) — *Corrosion Under Insulation and Fireproofing.*
  Adjacent-mode reference: insulation-driven CUI generates the chloride
  trace that feeds Cl-SCC of austenitic SS at lagged-piping
  temperatures.
- [api-std-579](../standards/api-std-579.md) — *Fitness-for-Service.* Part 9 crack-like-flaw
  assessment is the standard remaining-life calculation for SCC-affected
  equipment; consumes `K_ISCC` / `K_ISSC` thresholds from the test
  programme above and feeds operating-pressure / inspection-interval
  decisions through [fitness-for-service](fitness-for-service.md).
- [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) /
  [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) — pressure-vessel construction codes.
  UCS-56 (Div 1) and Part 6 (Div 2) PWHT requirements are the primary
  residual-stress mitigation for film-rupture SCC variants (caustic,
  amine, carbonate). Material-specification cross-references to
  [asme-bpvc-ii-d](../standards/asme-bpvc-ii-d.md) for allowable-stress and to
  [asme-bpvc-ix](../standards/asme-bpvc-ix.md) for welding-procedure qualification.

### RBI integration: SCC consequence of failure

Risk-based inspection treats SCC as a primary damage mechanism with a
distinct workflow because the kinetics are slow but the failure mode is
catastrophic. The RBI calculation for an SCC-exposed circuit
sequentially:

1. **Probability-of-failure (PoF) input.** [api-rp-581](../standards/api-rp-581.md) Part 2
   damage-factor modules for Cl-SCC, caustic, amine, sulfide,
   polythionic, carbonate, HIC/SOHIC, and HF-SCC each consume a
   susceptibility tier from [api-rp-571](../standards/api-rp-571.md) §4.5
   plus inspection-effectiveness modifiers. Each module uses an
   independent susceptibility envelope keyed on temperature, fluid
   chemistry, alloy, residual-stress condition, and history of
   inspection findings.
2. **Consequence-of-failure (CoF) input.** SCC failures usually fall in
   the leak-or-rupture-with-released-volume tier rather than the
   gradual-loss-of-containment tier that uniform-corrosion modules
   produce; the higher consequence multiplier shifts SCC-affected
   equipment toward shorter inspection intervals at the same PoF.
3. **Inspection-effectiveness ladder.** Highly-effective inspection
   ([api-rp-581](../standards/api-rp-581.md) Annex 2 Table A) for SCC
   demands volumetric methods (phased-array UT, AUT) on susceptible
   welds plus surface methods (WFMT, eddy-current array) on susceptible
   parent metal. Visual inspection alone is graded "ineffective" against
   embedded SCC and earns no PoF reduction.
4. **Reassessment trigger.** A confirmed SCC indication shortcuts the
   prescribed RBI cycle and forces an [api-std-579](../standards/api-std-579.md) Part 9 fitness-
   for-service reassessment; the RBI interval cannot relax until the
   FFS remaining-life calculation is on file.

The CoF asymmetry is the reason an SCC-susceptible CS hydroprocessor
overhead with a low PoF still earns short inspection intervals — the
expected loss given failure dominates the risk integral. See
[risk-based-inspection](risk-based-inspection.md) for the full PoF × CoF mechanics and
[fitness-for-service](fitness-for-service.md) for the post-detection assessment chain.

### Industry-application context

Although the SCC catalogue applies wherever the susceptibility triangle
closes, the dominant industry-by-industry exposure differs:

- **Refining and petrochemical.** Cl-SCC of austenitic SS overheads;
  caustic SCC of CS evaporators and caustic-injection points; amine SCC
  of CS amine-treater bottoms; PTASCC of FCC / HDS / hydrocracker
  reactor effluent piping during shutdown; carbonate SCC of FCC
  fractionator overheads; HF-SCC of CS in alkylation. The
  [api-rp-571](../standards/api-rp-571.md) §4.5 family is the umbrella catalogue
  for refining service.
- **Upstream production and midstream transport.** SSC and HIC/SOHIC of
  CS pipelines and equipment in sour service; HE of high-strength
  bolting, riser tensioner rods, and well-completion components.
  [iso-15156](../standards/iso-15156.md) governs material qualification end-to-end. See
  [sour-service-materials](sour-service-materials.md) for the sour-service-specific subset.
- **Offshore platform and subsea.** HISC of duplex / super-duplex CRAs
  under cathodic protection; HE of high-strength mooring shackles and
  subsea bolting; Cl-SCC of austenitic SS instrumentation tubing in
  marine-atmosphere exposure. [dnv-rp-f112](../standards/dnv-rp-f112.md) governs the HISC
  qualification chain. Mooring system failure analysis sits in
  [mooring-integrity-management](mooring-integrity-management.md).
- **LNG and cryogenic service.** Generally outside the SCC envelope at
  cryogenic operating temperatures, but warm-side process piping and
  amine-treater systems on the gas-treatment train carry the standard
  refining SCC exposures. The cool-down / warm-up transient brings
  surfaces through the chloride-deposition and amine-condensation
  windows.
- **Power generation and nuclear.** IGSCC of sensitized austenitic SS
  in BWR primary piping (chloride / oxygenated-water variant); caustic
  SCC of CS feedwater and steam-generator components; PWSCC of nickel-
  base Alloy 600 / 690 in PWR primary water (a hydrogen-assist /
  intergranular variant). The nuclear-specific qualification chain is
  outside this wiki's refining/oil-and-gas scope.
- **Marine and aerospace.** Cl-SCC of austenitic SS in seawater; Al-SCC
  of high-strength 7xxx / 2xxx fasteners and structural members in
  marine and salt-fog atmospheres; HE of high-strength steel landing-
  gear and fastener stock in cadmium / zinc-plated assemblies (tied to
  the post-plating hydrogen-bake requirement).

## Related concepts

- [hydrogen-embrittlement](./hydrogen-embrittlement.md) — the
  hydrogen-driven branch of the SCC family (SSC, HIC, SOHIC, HISC, HE of
  high-strength steel); shares the upstream hydrogen-source taxonomy and
  the trapping-site / lattice-embrittlement mechanism.
- [sour-service-materials](./sour-service-materials.md) — SSC + HIC +
  SOHIC subset of SCC; the H2S-specific qualification chain via
  TM-0177, TM-0284, and the Region 0–3 severity zoning of
  [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md).
- [damage-mechanism-screening](./damage-mechanism-screening.md) — RBI /
  inspection-program entry point that consumes the API RP 571 SCC
  catalogue and routes each unit's SCC-susceptibility evidence into
  [risk-based-inspection](./risk-based-inspection.md) /
  [api-rp-581](../standards/api-rp-581.md).
- [pitting-and-crevice-corrosion](./pitting-and-crevice-corrosion.md) —
  pits frequently nucleate the SCC initiation site (chloride pit →
  Cl-SCC of austenitic SS; sulfide pit → SSC at pit root); CPT/CCT
  envelopes set the chloride-temperature operating window upstream of
  the SCC susceptibility analysis.
- [corrosion-rate-measurement](./corrosion-rate-measurement.md) —
  uniform-corrosion-rate techniques (LPR, ER probes, mass-loss coupons)
  measure a fundamentally different damage form. SCC is **depth-driven
  not rate-driven**: a zero-uniform-rate environment can still harbour
  an SCC failure if the susceptibility triangle (material + stress +
  corrodent) closes. Inspection programs must instrument for SCC
  separately (e.g., wet-fluorescent MT, eddy-current array, phased-array
  UT) and not infer absence-of-SCC from low corrosion-rate readings.
- [brittle-fracture](./brittle-fracture.md) — SCC produces a brittle
  fracture-surface morphology (transgranular cleavage or intergranular
  separation) once a crack has propagated through the susceptible
  microstructure; SCC is a primary nucleation route for the brittle
  failure mode catalogued there.
- [fitness-for-service](./fitness-for-service.md) — SCC-affected
  equipment is assessed via [api-std-579](../standards/api-std-579.md)
  Part 9 (crack-like-flaw assessment) on the in-service residual-life
  side of the inspection chain.
- [fatigue-crack-growth](./fatigue-crack-growth.md) — SCC and
  corrosion-fatigue interact on cyclic-loaded equipment: SCC kinetics
  add a quasi-static crack-extension term to the Paris-law
  `da/dN` integral, and the [api-std-579](../standards/api-std-579.md) Part 9 remaining-life
  envelope must combine both contributions.
- [engineering-critical-assessment](./engineering-critical-assessment.md) —
  ECA frameworks for SCC-exposed welds use `K_ISCC` / `K_ISSC`
  thresholds as the lower-bound `K_max` and combine them with
  fatigue-crack-growth and FFS Part 9 critical-flaw size to set
  inspection intervals.
- [master-curve-and-transition-temperature](./master-curve-and-transition-temperature.md) —
  the SCC fracture surface produced by hydrogen-driven variants on
  ferritic steels is morphologically continuous with the
  brittle-cleavage facet population governed by the master-curve
  framework; relevant when calibrating fracture-toughness inputs to FFS
  Part 9.
- [welding-procedures-and-acceptance](./welding-procedures-and-acceptance.md) —
  weld-procedure qualification per [asme-bpvc-ix](../standards/asme-bpvc-ix.md) and SCC-resistance
  controls (sensitization avoidance for austenitic SS, hardness limits
  for sour-service CS) interact at WPS / PQR specification time;
  caustic / amine PWHT requirements per
  [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) UCS-56 are
  baked into the WPS for film-rupture-SCC service.
- [weld-toughness](./weld-toughness.md) — SCC propagation through HAZ
  microstructures interacts with the local toughness profile; coarse-
  grain HAZ (CGHAZ) is both lower-toughness and higher-residual-stress,
  the dominant nucleation site for caustic and amine SCC.
- [cathodic-protection](./cathodic-protection.md) — CP overpotential
  is a hydrogen-charge source for HE / HISC; the CP design envelope
  must respect the [dnv-rp-f112](../standards/dnv-rp-f112.md)
  hydrogen-charge ceiling for duplex / super-duplex CRAs and the
  hydrogen-bake requirement for high-strength bolting.
- [galvanic-corrosion](./galvanic-corrosion.md) — galvanic-couple
  geometry can locally elevate cathodic-current density and depress
  pH near the noble member, supplying both the chloride-pit nucleation
  site and the hydrogen-charge density that feed Cl-SCC and HE.
- [microbiologically-influenced-corrosion](./microbiologically-influenced-corrosion.md) —
  MIC-driven sulfate-reducing bacteria generate localized H2S and
  acid-pit chemistry that nucleate SSC on otherwise sweet-service
  carbon steel.
- [erosion-and-fac](./erosion-and-fac.md) — flow-accelerated corrosion
  and erosion remove the protective film whose presence governs the
  film-rupture SCC variants; FAC plus stress at a flow-disturbance
  geometry is a recurring root cause for caustic and amine SCC at
  injection nozzles.
- [coating-systems](./coating-systems.md) — coating breakdown plus
  cathodic-protection overpotential under disbonded coatings is the
  classic field nucleation site for HE / HISC; coating selection feeds
  back into the SCC mitigation strategy.
- [corrosion-under-insulation](./corrosion-under-insulation.md) —
  CUI is the upstream mode that typically supplies the chloride trace
  for Cl-SCC of insulated austenitic SS at lagged-piping
  temperatures; coverage gap on insulation joints is a recurring SCC
  root cause and is governed by [api-rp-583](../standards/api-rp-583.md).

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
