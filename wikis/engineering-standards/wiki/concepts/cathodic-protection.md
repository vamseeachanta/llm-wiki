---
title: "Cathodic Protection"
slug: cathodic-protection
tags:
  - corrosion
  - cp
  - sacrificial-anode
  - iccp
  - offshore
  - subsea-pipelines
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/dnv-rp-b401.md
  - standards/dnv-rp-f103.md
  - standards/abs-gn-239-cathodic-protection-offshore.md
---

# Cathodic Protection

## What is CP?

Cathodic protection (CP) is an electrochemical corrosion-control
technique that imposes an external electrical potential onto a
metallic structure so that the entire wetted surface is driven to a
sufficiently negative (cathodic) potential to suppress the anodic
half-reaction (metal dissolution, `M → M^{n+} + n e^-`). With the
anodic site moved off the protected steel and onto a deliberately
chosen anode, generalized and pitting corrosion of the structure are
arrested for as long as protective current is maintained.

Two delivery modes are in industrial use:

1. **Galvanic (sacrificial) anode CP** — a less-noble metal coupled
   electrically to the structure spontaneously corrodes and supplies
   the protective current. No external power source is required.
2. **Impressed-current CP (ICCP)** — a DC power supply forces current
   from inert (or near-inert) anodes through the electrolyte to the
   structure. Current and potential can be regulated to demand.

The selection between the two is driven by structure size, current
demand, electrolyte resistivity, accessibility for monitoring, and the
availability of reliable power.

## Why offshore systems use it

Offshore and subsea steel sees one of the most aggressive natural
corrosion environments on Earth: high chloride seawater, dissolved
oxygen in the splash and upper water columns, microbiologically
active biofilms, anaerobic sulphate-reducing bacteria in seabed muds,
and mechanical disturbance of any barrier coating during installation
and operation. Bare steel exposed to seawater corrodes at a rate
broadly in the 0.1–0.5 mm/year range, with localized rates well above
that around coating defects, weld toes, and crevices. A 25–40-year
asset life is not achievable from coating alone.

Offshore practice therefore pairs CP with an external coating system,
where the coating absorbs the bulk of the demand and the CP system
sizes for the *coating-defect area* — quantified by a coating
breakdown factor that grows over the design life. This synergy gives
predictable, defensible mass-loss budgets and lets the designer trade
anode mass against coating quality.

## Galvanic (sacrificial) anode CP

In galvanic CP a less-noble alloy is bolted, welded, or banded to the
structure as a discrete or distributed anode. The alloy choice fixes
two design quantities:

- **Driving voltage** — the closed-circuit potential difference
  between the anode and the protected steel in the operating
  electrolyte; sets how much current a given anode-to-steel resistance
  path can deliver.
- **Current capacity** — the amp-hours of charge the alloy releases
  per kilogram before consumption, in `Ah/kg`; sets how much anode
  mass is required for a given design life and average current
  demand.

Common offshore galvanic-anode alloys:

| Family | Typical use | Notes |
|---|---|---|
| **Al-Zn-In** | Seawater immersion, jackets, subsea components, pipelines | Workhorse offshore alloy; highest practical capacity |
| **Al-Zn-Mg** | Brackish / variable-salinity service | Lower capacity than Al-Zn-In |
| **Zn** | Seawater, occasional in seabed mud | Lower capacity per kg than Al-Zn-In; used where Al passivates |
| **Mg** | Soils and fresh / low-conductivity water | High driving voltage; rarely used offshore due to over-protection / hydrogen risk |

Sizing of a galvanic-anode CP system is dominated by:

- average current demand over the life (sets anode mass via Faradaic
  capacity),
- initial and final current demand (sets the number and resistance of
  individual anodes),
- coating breakdown factor as a function of time and coating
  category,
- anode-to-electrolyte resistance, which depends on anode shape and
  electrolyte resistivity (seawater vs. seabed).

Design lookup tables for design current density, utilization factor,
coating breakdown factor, and anode capacity per alloy are tabulated
in [DNV-RP-B401](../standards/dnv-rp-b401.md) (the dominant offshore
reference) and, for submarine pipelines specifically, in
[DNV-RP-F103](../standards/dnv-rp-f103.md). Spreadsheet-style sizing
that walks per-zone current demand, mass balance, and per-anode
resistance against these tabulated inputs remains the standard
working method.

## Impressed-current CP

Impressed-current CP (ICCP) replaces the sacrificial alloy with a DC
power supply driving inert or near-inert anodes. Because the power
supply sets the current independently of the anode-electrolyte
chemistry, ICCP delivers high currents from a small number of
long-life anodes and is suited to:

- large structures where the equivalent galvanic anode mass would be
  prohibitive,
- buried onshore pipelines where soil resistivity makes galvanic
  drive voltage insufficient,
- shore-based plant, ship hulls, and floating-asset hulls where
  monitoring and adjustment are practical.

Typical ICCP component palette:

- **Inert anodes:** mixed-metal-oxide (MMO) coated titanium,
  platinized titanium, lead-silver alloy, graphite, magnetite, or
  high-silicon cast iron. MMO and platinized Ti dominate new offshore
  and modern marine designs.
- **Reference electrodes:** Ag/AgCl/seawater for marine immersion,
  Cu/CuSO4 for buried onshore service, Zn for permanent coupons.
- **Transformer-rectifier (T/R) units:** regulated DC supplies, often
  with potential-controlled feedback against the reference
  electrodes.

ICCP can be over- or under-driven; potential surveys against the
reference electrode network are part of the lifecycle and are
required by the offshore CP standards.

## Polarization criteria

Adequate protection is defined by the structure-to-electrolyte
potential measured against a reference electrode. The criteria below
are the practitioner-level summary; the controlling values for any
given calculation are taken from the relevant standard:

| Environment | Reference electrode | Steel protection criterion |
|---|---|---|
| Aerated seawater | Ag/AgCl/seawater | more negative than `−800 mV` |
| Anaerobic seabed mud (SRB-active) | Ag/AgCl/seawater | more negative than `−900 mV` |
| Sour service / SRB-driven | Ag/AgCl/seawater | more negative than `−900 mV` (with HE caveat) |

Over-protection — a potential more negative than roughly `−1100 mV`
vs. Ag/AgCl/seawater — is undesirable and, for high-strength steels
and several crack-susceptible alloy families, actively damaging
because of hydrogen uptake (see next section).

NACE / AMPP and ISO equivalents express these as a `−850 mV` Cu/CuSO4
criterion for buried onshore steel; the offshore-DNV `−800 mV`
Ag/AgCl/seawater criterion is the same physical potential expressed
against a different reference.

## Hydrogen embrittlement caveat

The CP reaction at the steel surface produces atomic hydrogen as a
by-product. At protective potentials the rate is small and the
hydrogen recombines and desorbs harmlessly. As the potential is
driven more negative — through over-protection, ICCP miscalibration,
or proximity to a high-output anode — the surface concentration of
atomic hydrogen rises, and a fraction is absorbed into the metal
lattice rather than recombined.

For susceptible materials this absorbed hydrogen interacts with
trapping sites at carbides, dislocations, and prior-austenite grain
boundaries to drive **hydrogen embrittlement (HE)**: a
stress-and-time-dependent loss of ductility and fracture resistance
that can cause sudden, low-load fracture in service.

Susceptibility is concentrated in:

- **High-strength low-alloy steels** with SMYS roughly above 950 MPa
  (e.g., bolting, riser-tensioner rods, mooring shackles).
- **Martensitic and precipitation-hardened CRAs** (13Cr, 17-4PH and
  similar).
- **Duplex and super-duplex stainless steels** when at the upper end
  of their strength range and operated under CP.
- Cold-worked, surface-rolled, or quenched-and-tempered fasteners.

DNV-RP-F112 (HISC — hydrogen-induced stress cracking — of subsea
duplex SS components under CP) is the governing offshore reference
for this regime; DNV-RP-B401 cross-refers to it whenever CP design
encloses duplex / super-duplex pressure-containing components. The
practical design move is to limit the most-negative potential the
component will see and to keep CRAs out of the immediate vicinity of
high-output sacrificial anodes.

## Cathodic disbondment of coatings

CP and barrier coatings interact at coating defects. The hydroxide
generated by the cathodic reaction at a defect can, in time, attack
the coating-to-steel adhesion radially outward from the defect — a
failure mode known as **cathodic disbondment**. Pipeline and offshore
coating systems are screened for this in laboratory tests:

- **ASTM G8** — cathodic-disbondment of pipeline coatings (older
  reference, still cited).
- **ASTM G80** — specific cathodic-disbondment test geometry.
- **ASTM G42** — elevated-temperature cathodic-disbondment of
  pipeline coatings, important for thermally-insulated subsea lines.
- **CSA Z245.20 / Z245.21** — Canadian FBE and 3-layer-PE pipeline
  coating qualification with cathodic-disbondment acceptance.

A coating that disbonds under CP fails in the worst possible way:
the disbonded film traps electrolyte against the steel, shields the
underlying surface from the cathodic current, and creates an
under-film corrosion cell that CP cannot reach. Coating selection
therefore has to be made jointly with the CP design, not before it.

## Coatings + CP synergy

Modern offshore practice treats coating and CP as one system, with
the CP system sized for the *coating-defect area*, not the bare
steel. The design knob is the **coating breakdown factor**, a
time-dependent fraction of the protected surface that the CP system
must treat as electrically exposed.

Common pipeline external coating systems used in this synergy:

- **Fusion-bonded epoxy (FBE)** — single-layer or dual-layer FBE,
  typical for in-plant and small-bore lines.
- **Three-layer polyethylene (3LPE)** — FBE primer + adhesive +
  PE topcoat; standard for warm-line carbon-steel pipelines.
- **Three-layer polypropylene (3LPP)** — same architecture with PP
  topcoat for higher-temperature service.
- **Field-joint coatings (FJC)** — separately specified, with
  coating-breakdown constants that are *not* the same as the linepipe
  coating; tracked independently in the CP calc.

Linepipe and field-joint coating breakdown constants enter directly
into the CP sizing formulas — see the `f_cm` (mean) and `f_cf`
(final) breakdown-factor tables in
[DNV-RP-F103](../standards/dnv-rp-f103.md) Annex 1.

## Standards

Primary references for offshore and subsea CP design:

- [DNV-RP-B401](../standards/dnv-rp-b401.md) — *Cathodic Protection
  Design.* The dominant offshore CP-design reference; covers
  galvanic and impressed-current CP for submerged offshore structures
  and subsea components, design current densities by zone and
  exposure, coating breakdown factors, and anode mass / current
  output sizing.
- [DNV-RP-F103](../standards/dnv-rp-f103.md) — *Cathodic Protection
  of Submarine Pipelines by Galvanic Anodes.* Submarine-pipeline
  companion to RP-B401; current density requirements as a function of
  burial state and internal fluid temperature, coating breakdown
  factors over design life, longitudinal pipe-metal resistance,
  bracelet-anode spacing, and pipeline attenuation analysis.
- [ABS GN-239](../standards/abs-gn-239-cathodic-protection-offshore.md)
  — *Guidance Notes on Cathodic Protection of Offshore Structures.*
  ABS-class equivalent to RP-B401 for fixed and floating offshore
  steel structures and subsea systems.

Adjacent international standards (not yet wiki-resolved; flagged for
future ingest):

- **BS EN 13509** — *Cathodic protection measurement techniques.*
- **BS EN 14505** — *Cathodic protection of complex structures.*
- **ISO 15589-1** — *Cathodic protection of pipeline systems —
  on-land pipelines.*
- **ISO 15589-2** — *Cathodic protection of pipeline systems —
  offshore pipelines.*
- **DNV-RP-F112** — *Design of duplex stainless steel subsea
  equipment exposed to cathodic protection* (HISC governance for
  CRAs under CP).

## Related concepts

- [sour-service-materials](sour-service-materials.md) — material selection under H2S where the
  CP-induced HE caveat is most acute.
- [[submarine-pipeline-design]] — pipeline external corrosion control
  is one input to the wider design.
- [hydrogen-embrittlement](hydrogen-embrittlement.md) — the failure mode the over-protection
  caveat exists to prevent.

## Cross-wiki bridges

- [IMO IGC Code](../../../lng-projects/wiki/standards/igc-code.md)
  (lng-projects) — **bidirectional bridge**: CP design is binding for
  steel hull and ballast-tank protection on IGC-certified gas carriers
  (LNG, LPG, ethylene, ammonia). IGC Code Ch.2 and Ch.3 (ship
  arrangements, ballast/void-space corrosion control) interact with
  the offshore CP design rules summarised here; over-protection
  caveats apply with extra force to the **9% Ni cargo-tank
  attachments and the duplex-stainless cargo-handling components**
  that IGC Ch.6 mandates, because hydrogen embrittlement and HISC are
  the dominant CP failure modes on those alloy families. ICCP hull
  systems on LNG carriers are sized against the same DNV-RP-B401 /
  ABS GN-239 framework cited above.

## Source materials

- [Source summary — DNV offshore CP standards](../sources/og-standards-dnv.md)
- [Source summary — ABS offshore CP standards](../sources/og-standards-abs.md)
