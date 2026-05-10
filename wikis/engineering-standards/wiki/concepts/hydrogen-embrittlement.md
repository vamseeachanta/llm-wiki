---
title: "Hydrogen Embrittlement and HISC"
slug: hydrogen-embrittlement
tags:
  - hydrogen-embrittlement
  - hisc
  - hsc
  - hic
  - sohic
  - cra
  - sour-service
  - cathodic-protection
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/dnv-rp-f112.md
  - standards/iso-15156.md
---

# Hydrogen Embrittlement and HISC

> Concept anchor for the hydrogen-driven cracking failure family that spans
> cathodic-protection over-protection of CRAs (HISC), wet-H2S exposure of
> carbon and low-alloy steels (HIC, SOHIC, SSC), and high-strength-steel
> service in marine + CP environments. Bidirectional with
> [[cathodic-protection]], [[sour-service-materials]], and the
> [[pitting-and-crevice-corrosion]] qualification chain.

## What is hydrogen embrittlement?

**Hydrogen embrittlement (HE)** is the reduction of mechanical properties —
tensile elongation, fracture toughness, fatigue life, and resistance to
sustained-load cracking — that occurs when atomic hydrogen dissolves into
a metallic lattice and interacts with trapping sites (carbides,
dislocations, prior-austenite grain boundaries, second-phase interfaces,
inclusions). The bulk chemistry of the alloy is unchanged; what changes
is the alloy's tolerance for stress, strain, and time.

Three closely related failure modes are catalogued by the offshore and
oil-and-gas materials standards:

- **HE (general hydrogen embrittlement)** — broad term for hydrogen-driven
  loss of ductility and toughness; manifests as low-load brittle fracture
  on susceptible materials under sustained tension.
- **HISC (hydrogen-induced stress cracking)** — hydrogen-assisted cracking
  of corrosion-resistant alloys (CRAs), classically the ferrite phase of
  22Cr/25Cr duplex stainless steel under cathodic protection. Governed
  offshore by [[dnv-rp-f112]].
- **HIC (hydrogen-induced cracking)** — internal stepwise blister-and-crack
  networks in carbon-steel plate driven by hydrogen accumulation at MnS
  inclusions and segregation bands; stress-independent (occurs in
  unstressed plate). Qualified by [[ampp-tm-0284]].

The mechanisms differ in detail (decohesion at trapping interfaces,
hydrogen-enhanced localized plasticity, internal-pressure blistering at
inclusion sites) but share an upstream requirement: a sufficient flux of
atomic hydrogen into the lattice to reach a critical concentration at the
trapping site.

## Hydrogen sources

| Source | Mechanism |
|---|---|
| Cathodic protection (over-protected) | Cathodic reduction of water at the steel surface, `2 H2O + 2 e- -> H2 + 2 OH-`, producing adsorbed atomic H; a fraction is absorbed into the lattice rather than recombined to H2 |
| H2S sour service | H2S corrosion liberates atomic H at the steel surface; sulfide-ion (S^2-) acts as a hydrogen-recombination poison, raising the surface H activity and the absorbed fraction |
| Welding (moist consumables, low-hydrogen practice) | Arc dissociates moisture and hydrocarbon contamination on consumables, base metal, or shielding gas; atomic H is entrained into the molten pool and trapped at solidification |
| Acid pickling / electroplating | Surface H generation during cathodic cleaning or plating (zinc, cadmium, chromium); diffusible H is locked under the plated film |
| High-pressure H2 service | Lattice solubility scales with `sqrt(p_H2)` (Sieverts' law); high partial pressures sustain a high lattice equilibrium concentration |

The first two sources are the dominant offshore concerns: CP-driven HE
on CRAs and high-strength steels, and wet-H2S-driven cracking on carbon
and low-alloy steels. Welding and plating sources are controlled by
fabrication-procedure qualification and post-process baking.

## HISC of duplex stainless steel

The canonical CRA failure mode is **HISC of duplex and super-duplex
stainless steels (DSS / SDSS, 22Cr / 25Cr) under cathodic protection**.
DSS gets its corrosion resistance from a roughly 50/50 ferrite-austenite
microstructure; the ferrite phase is the hydrogen-susceptible partner.
Under CP, atomic hydrogen evolved at the steel surface diffuses
preferentially into the ferrite, where the combination of elevated
lattice H, sustained tensile stress (design stress + tensile residual
stress from welding or cold work), and stress-raiser geometry triggers
cleavage of the ferrite phase. The austenite phase locally arrests the
crack, producing the characteristic step-and-arrest fracture surface
seen in HISC failures.

The offshore governance for DSS subsea hardware exposed to CP is
[[dnv-rp-f112]]. The standard's headline design moves are: PREN >= 40
(super-duplex preferred) with controlled ferrite content and absence of
sigma-phase; CP protection-potential bounded less negative than
approximately -1050 mV vs. Ag/AgCl/seawater; reduced design-stress
allowables in CP-exposed zones; tight residual-stress and weld-profile
control; and stricter surface-NDT acceptance than non-CP service. The
2000s offshore HISC failures of subsea trees, manifolds, hubs, and
connectors drove the publication of RP-F112 and remain the precedent
case for any DSS hardware on a CP-protected circuit.

## HIC of carbon-steel plate

In wet H2S, carbon-steel plate fails by a stress-independent mechanism:
atomic H absorbed at the surface diffuses to MnS inclusions and
segregation bands at mid-thickness, recombines to molecular H2 at the
inclusion-matrix interface, and generates internal pressures sufficient
to nucleate **stepwise blisters and through-thickness crack networks**.
Because the driving force is internal H2 pressure rather than applied
stress, HIC occurs in unstressed plate — a common surprise during
fabrication of pressure-vessel shells from non-HIC-qualified plate.

Qualification of plate, pipe, and forgings for HIC resistance is
governed by [[iso-15156]] / [[ampp-mr-0175-pt2]] (materials selection
under H2S) using the [[ampp-tm-0284]] laboratory test method: plate
coupons are immersed in H2S-saturated test solution (Solution A standard
or Solution B harsher) for 96 hours, sectioned, and examined
metallographically against acceptance limits expressed as crack length
ratio (CLR), crack thickness ratio (CTR), and crack sensitivity ratio
(CSR). HIC-resistant grades are produced by inclusion-shape control
(Ca-treatment to spheroidize MnS), low-S chemistry, and segregation
control during continuous casting.

## SSC and SOHIC

**SSC (sulfide stress cracking)** is the cracking-side companion to HIC
in the same wet-H2S environment but on stressed components. Atomic H
absorbed at the surface embrittles the steel under sustained tensile
stress; failure is brittle, time-dependent, and concentrated at high-
hardness regions (heat-affected zones, cold-worked zones, high-strength
fasteners). Qualification is by [[ampp-tm-0177]] in four standardized
geometries: Method A uniaxial tension, Method B bent beam, Method C
C-ring, Method D double-cantilever beam (DCB, fracture-mechanics
`K_ISSC`). Hardness control in carbon and low-alloy steels is the
primary mitigation lever and is codified in [[ampp-mr-0175-pt2]].

**SOHIC (stress-oriented hydrogen-induced cracking)** is the worst-of-
both-worlds mode: stacked HIC blisters at mid-thickness link
through-thickness via SSC ligaments under applied or residual tensile
stress. Heat-affected zones of welded carbon-steel pressure vessels in
sour service are the canonical SOHIC concern. Qualification combines
TM-0284 (HIC nucleation) and TM-0177 (SSC propagation) evidence;
acceptance is governed by [[ampp-mr-0175-pt2]] in the severe-sour
(Region 3) classification.

## High-strength-steel HE in marine + CP service

Steels with specified minimum yield strength (SMYS) above roughly
950 MPa — the regime of riser-tensioner rods, mooring shackles and
connectors, subsea bolting, drill-string components, and high-strength
fasteners — are intrinsically susceptible to hydrogen embrittlement
when exposed to seawater under cathodic protection. The mechanism does
not require H2S; CP-evolved hydrogen alone is sufficient at this
strength level. [[api-spec-6a]] and [[api-spec-17d]] restrict the use
of high-strength steels in subsea wellhead and tree service for this
reason and impose hardness, heat-treatment, and surface-finish controls
on permitted grades.

The practical design move is to specify lower-strength alloys for
CP-exposed components wherever the load case allows, and where high
strength is unavoidable, to pair the alloy with a coating barrier,
dielectric isolation from the CP circuit, and tight control of
tensile residual stress.

## Mitigation

Mitigation operates on the four levers that govern the
hydrogen-stress-microstructure interaction:

- **Material selection** — low-strength, low-hardness, controlled-
  microstructure alloys (PREN >=40 for DSS subsea; hardness caps per
  [[ampp-mr-0175-pt2]] for sour carbon-steel; SMYS limits per
  [[api-spec-6a]] for subsea bolting). The most reliable mitigation is
  to keep the susceptibility envelope outside the service envelope.
- **Hydrogen baking after plating** — diffusible hydrogen introduced by
  electroplating (zinc, cadmium, chromium) is removed by a controlled
  thermal bake within a defined window after plating and before service
  loading; baking schedules are specified by the plating standard.
- **Low-hydrogen welding consumables and practice** — moisture-controlled
  consumables, controlled storage and re-baking of electrodes, preheat
  and interpass temperature control, post-weld heat treatment to
  redistribute trapped H and to reduce HAZ hardness; jointly governed by
  [[asme-bpvc-ix]] and the relevant materials-and-construction codes.
- **Design-stress limits** — reduced allowables in CP-exposed CRA zones
  per [[dnv-rp-f112]]; hardness-and-stress envelopes per
  [[ampp-mr-0175-pt2]] and [[ampp-mr-0175-pt3]].
- **CP protection-potential limits** — bound the most-negative potential
  the susceptible material will see; coordinate CP design under
  [[dnv-rp-b401]] with HISC governance under [[dnv-rp-f112]].
- **Coating barriers and dielectric isolation** — paint, FBE, and
  three-layer-PE/PP coatings reduce direct CP current to susceptible
  surfaces; dielectric isolation (insulating washers, isolation joints)
  removes high-strength bolting from the CP circuit entirely.

The mitigation chain is most effective when applied jointly — single-
lever mitigation (e.g., hardness control without stress control) has a
documented track record of HISC and SSC service failures.

## Standards

Bidirectional links to the standards-page resolvers (each carries
`code_id`, `publisher`, `revision` frontmatter per the wiki schema):

- [[dnv-rp-f112]] — *Design of Duplex SS Subsea Equipment Exposed to
  Cathodic Protection.* Governing offshore reference for HISC of
  duplex/super-duplex subsea hardware under CP. Material, CP-potential,
  design-stress, residual-stress, surface-finish, and inspection
  controls.
- [[iso-15156]] — *Materials for Use in H2S-Containing Environments in
  Oil and Gas Production.* Three-part joint publication
  (ISO 15156-1/-2/-3 = NACE MR0175 = AMPP MR0175); the master
  sour-service materials code.
- [[ampp-mr-0175-pt2]] — *Carbon and Low-Alloy Steels and the Use of
  Cast Iron.* Hardness, heat-treatment, and welding controls for
  carbon-steel SSC, HIC, and SOHIC qualification; severity-zone
  classification (Regions 0–3) on the pH2S-vs-pH diagram.
- [[ampp-mr-0175-pt3]] — *Cracking-Resistant CRAs and Other Alloys.*
  Per-alloy temperature/chloride/pH2S envelopes for 13Cr martensitic,
  duplex, super-duplex, austenitic, and Ni-base alloys in sour service.
- [[ampp-tm-0284]] — *HIC Test Method.* 96-hour H2S-saturated immersion;
  CLR/CTR/CSR metallographic acceptance.
- [[ampp-tm-0177]] — *SSC Laboratory Test Methods.* Methods A
  (uniaxial), B (bent beam), C (C-ring), D (DCB / `K_ISSC`).

## Related concepts

- [cathodic-protection](./cathodic-protection.md) — over-protection is
  the primary HE driver on CRAs and high-strength steels; the
  CP-design / HE-mitigation interface is governed jointly by
  [dnv-rp-b401](../standards/dnv-rp-b401.md) (CP design) and
  [dnv-rp-f112](../standards/dnv-rp-f112.md) (HISC mitigation).
- [sour-service-materials](./sour-service-materials.md) — H2S-driven
  hydrogen charging on carbon and low-alloy steels (SSC, HIC, SOHIC) and
  on CRAs (HISC variants); qualification chain via TM-0284, TM-0177, and
  ASTM G48.
- [pitting-and-crevice-corrosion](./pitting-and-crevice-corrosion.md) —
  chloride-driven pit nucleation can locally depress pH at pit roots and
  trigger SSC initiation; CPT/CCT envelopes set the chloride-temperature
  operating window upstream of the HE susceptibility analysis.
- [brittle-fracture](./brittle-fracture.md) — low-temperature service
  compounds HE susceptibility (lower toughness baseline + lower H
  diffusivity to desorb out); HE-driven cracks propagate via the same
  cleavage / quasi-cleavage transgranular mode catalogued there.
- [stress-corrosion-cracking](./stress-corrosion-cracking.md) — SSC and
  HISC are the H2S-charged and CP-charged sub-families of the broader
  environmentally-assisted-cracking taxonomy; the SCC concept-page
  catalogues the wider mechanism portfolio (chloride-SCC, caustic, PASCC).
- [htha-nelson-curves](./htha-nelson-curves.md) — high-temperature
  hydrogen-attack sibling above ~200 degC; mechanistically distinct
  (carbide consumption and methane voids vs. trapping-and-embrittlement)
  but shares the hydrogen-damage parent taxonomy.

## Source materials

- [Source summary — DNV offshore standards](../sources/og-standards-dnv.md)
  — catalog summary covering DNV-RP-F112 (HISC governance) and
  DNV-RP-B401 (CP design) on the consolidated standards mount.
- [Source summary — ISO standards](../sources/og-standards-iso.md) —
  catalog summary covering ISO 15156 (materials for H2S service),
  including the three-part 1st-edition PDFs on the consolidated mount.

Vendor PDFs are read-only at the consolidated standards mount and never
enter this repo per the spinout 2026-05-05 governance and the
vendor-derivative firewall in the repo-root `CLAUDE.md`.
