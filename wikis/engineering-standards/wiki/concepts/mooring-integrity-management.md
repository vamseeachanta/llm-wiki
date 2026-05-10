---
title: "Mooring Integrity Management"
slug: mooring-integrity-management
tags:
  - mooring
  - station-keeping
  - integrity-management
  - fpso
  - flng
  - fsru
  - modu
  - rbi
  - offshore
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - sources/og-standards-onepetro.md
cross_links:
  - standards/api-rp-2sk.md
  - standards/dnv-os-e301.md
  - concepts/cathodic-protection.md
  - concepts/fatigue-design-and-assessment.md
extraction_policy: metadata-and-doctrinal-synthesis
---

# Mooring Integrity Management

## Why mooring-integrity matters

Permanent-moored floating production assets — FPSOs, FLNGs, FSRUs,
spar platforms, semi-submersible production units, deep-draft tension-leg
platforms, and CALM / SALM oil-export buoys — depend continuously on
their mooring system to remain on station. Loss of station-keeping is a
near-binary failure mode: the asset either stays within its
watch-circle and operates, or it drifts off station and the
consequences cascade through the riser system, the export topology,
and (on FPSOs / FLNGs) the cargo-tank inventory.

The realised consequence list from industry experience covers the
full range:

- **Riser-system damage** — disconnect emergency-disconnect packages
  (EDPs) trigger only inside a narrow watch-circle envelope; loss of
  station beyond that envelope tears risers off in service. Banff FPSO
  (UK North Sea, December 2011) lost station after multiple mooring
  lines parted in winter storm `Berit`; seven flexible risers and
  three umbilicals were torn off.
- **Single-line failure with continued operation** — Volve FPSO
  (Norwegian sector, 2016) experienced an undetected single-line
  failure that was only diagnosed in the periodic monitoring review;
  the asset continued operating in degraded condition until repair.
- **Hull / bow-loading conflict** — turret-moored FPSO bow-loading
  manifolds clash with shuttle-tanker offtake operations once the
  watch-circle is enlarged by failed lines.
- **Mooring-induced fatigue on risers and umbilicals** — line-tension
  redistribution after a single failure changes the dynamic excitation
  of the surviving lines and can accelerate fatigue on
  porch-attached risers.
- **Hydrocarbon release** — a worst-case escalation if the asset
  drifts off station with risers still connected.

Industry experience accumulated through the 1990s and 2000s
demonstrated that a "design-and-forget" approach was insufficient:
mooring lines age, anchor positions drift, components fatigue, and
the only credible mitigation is a formal in-service integrity-management
program tracking inspection intervals, failure-mode screening, and
risk-based reassessment.

## Doctrinal evolution

Mooring integrity practice evolved through four codification stages:

- **POSM (Position-keeping Operating-Status Monitoring) — 1980s/1990s
  early MODU practice.** First-generation tension-monitoring on
  individual mooring lines on mobile drilling units; no structured
  inspection or reliability-based component management.
- **API RP 2I (1990s)** — *In-service Inspection of Mooring Hardware
  for Floating Drilling Units.* First API integrity-management practice
  for MODU mooring; covered MODU chain, wire-rope, connectors, fairleads;
  the foundation document.
- **API RP 2SK (current)** — *Design and Analysis of Stationkeeping
  Systems for Floating Structures.* The design-side anchor;
  3rd Edition with the 2008 addendum is the current US-side reference
  for permanent-moored production systems.
- **API RP 2MIM (2018+)** — *Mooring Integrity Management.* The first
  US-side integrity-management practice specifically for permanent
  production moorings; codified the RBI tier system, condition-based
  maintenance approach, and the mooring failure-mode catalog after
  multiple OTC papers from operators of GoM and West-Africa assets
  surfaced common failure patterns.
- **DNV-RP-F203 / DNV-OS-E301 family** — DNV class-side integrity
  practice; RP-F203 for dynamic-positioning vessels, OS-E301 for
  permanent moorings, RP-F205 for global performance analysis.

The two branches (API and DNV) are not identical but cover the same
practitioner space; an operator typically picks one branch and follows
it consistently across the asset class.

## Mooring failure modes

Permanent mooring failures cluster into a small set of recurring
mechanisms; the integrity-management program is structured around
detecting and pre-empting each:

### Chain-link wear

Mechanical wear of chain-link surfaces at points of relative motion
(at the fairlead, at the chain-stopper, at the touchdown point on the
seabed). Wear rate depends on:

- relative sliding velocity (proportional to vessel motion),
- contact-surface hardness of mating components,
- abrasive content of the seabed (where the chain rests in mud or sand),
- coating loss and bare-steel exposure.

Chain-wear inspection is the single largest line item in a mooring
integrity-management program by ROV-survey time.

### Polyester-rope creep and abrasion

Polyester rope is the dominant deepwater taut-leg material because it
combines a lower submerged weight than chain or wire with a sub-modulus
that limits station-keeping load amplification. Failure modes specific
to polyester include:

- **Creep elongation** — slow length increase under sustained tension
  that gradually shifts the watch-circle and pretension distribution;
  bounded by the rope-construction creep coefficient.
- **Abrasion at terminations** — particularly at the rope-to-chain
  connector where small-particle ingress can score the load-bearing
  yarns.
- **Internal-yarn damage** from bend-over-sheave operations during
  installation; not always evident from visual inspection.

### Wire-rope corrosion and fatigue

Wire-rope components (typically the splash-zone or the upper-water
column section in a mixed-line configuration) suffer:

- atmospheric and seawater-immersion corrosion,
- tension–tension and tension–bending fatigue at terminations and at
  the fairlead bend,
- internal-corrosion of zinc-coated wires once the protection is lost.

### Fairlead and stopper failures

The fairlead (chain-jack chock or hawse pipe) and the chain-stopper
are the highest-cycle-loaded components in the system; they carry
wave-frequency tension cycles concentrated at a single location, and
their failure mechanisms are hardware-specific:

- **Fairlead bushing wear** — geometric distortion of the chain
  contact path.
- **Chain-stopper pawl fatigue** — historically the most-cited
  permanent-mooring failure surface in OTC papers from the 2010s.
- **Hydraulic-actuator failure** on retractable stoppers — often a
  monitoring rather than a structural issue.

### Anchor drag and pile pull-out

The anchor (drag-embedment, suction caisson, driven pile, or torpedo
anchor) is the foundation of the mooring system. Failures here are
rare but consequential:

- **Drag-embedment anchor walk** — slow translation under cyclic
  tension, observed historically in soft-clay basins.
- **Suction-caisson tilt or extraction** — geotechnical failure under
  combined tension / moment loading.
- **Driven-pile pull-out** — rare; usually indicates installation
  shortfall rather than service degradation.

### Broken-line scenarios

A single broken line redistributes tension to its neighbours; the
adjacent lines see an instantaneous tension increase and a permanent
mean-tension shift. The integrity-management program must demonstrate
that:

- the asset survives the single-line-failure case by analysis (per
  RP-2SK / OS-E301), and
- the surviving lines are not driven into an accelerated-fatigue or
  extreme-load regime by the redistribution.

Multi-line failure scenarios (Banff FPSO 2011 was effectively a
multi-line failure in a winter storm) require additional analysis and
operational mitigations.

## Inspection methods

The integrity-management toolbox covers visual / dimensional / NDE /
monitoring methods at different intervals:

| Method | Target | Typical interval |
|---|---|---|
| Topside visual / dimensional | Above-water chain, stoppers, fairleads | Monthly–quarterly |
| ROV general visual | Splash-zone + upper water-column lines | 6-monthly–annual |
| ROV detailed close-visual | Touchdown / wear-zone chain links | Annual–biennial |
| Chain-link diameter measurement | Wear-allowance check vs. design | Per RBI tier; typically biennial |
| In-line tension monitoring | Continuous load history | Continuous (per-line load cells) |
| MMS / mooring-monitoring system | Position + heading + line tension | Continuous |
| Rope tension / length measurement | Polyester creep tracking | Annual |
| NDE (MPI, UT, EMI) | Crack-detection at high-stress locations | Per RBI tier |
| Anchor-position survey | Anchor walk / drag detection | 5-yearly typical |
| Detailed special periodic survey | Class renewal | 5-yearly survey + dry-dock |

ROV survey time dominates the cost; an integrity-management program is
optimised by routing inspection effort to the components flagged by
the RBI tier system rather than uniformly across the line set.

### Fatigue monitoring

Real-time tension-monitoring data feeds directly into a fatigue-life
re-assessment using the as-installed structural connectivity and the
measured tension history. Per [fatigue-design-and-assessment](../concepts/fatigue-design-and-assessment.md),
the S-N curve and stress-concentration factor (SCF) at each component
are pre-determined; the integrity-management program maintains a
running cumulative-damage estimate and re-orders inspection priorities
when damage accrual deviates from the design-basis prediction.

## API RP 2MIM recommendations

The 2MIM framework introduced three companion management approaches,
applied jointly:

1. **Condition-based maintenance** — replace or repair when monitored
   condition (wear, corrosion, dimensional change) crosses a
   pre-defined threshold. Requires the inspection regime above.
2. **Interval-based maintenance** — replace components on a fixed
   calendar or operating-hours schedule regardless of condition.
   Used for components where reliable in-service inspection is not
   practical (e.g., embedded chain segments, anchor connectors).
3. **Reliability-based maintenance (RBI)** — risk-rank each component
   on probability-of-failure × consequence-of-failure, route inspection
   intervals and methods to the high-risk components, and adjust the
   ranking as inspection data accrues.

The RBI tier system (commonly expressed as Tier 1 / 2 / 3 with
increasing inspection rigor) maps directly to the per-component PoF
ranking. Tier-1 components (low PoF, low consequence) get the lightest
inspection regime; Tier-3 components (high PoF or high consequence
or both) get the most rigorous regime, often combined with redundant
monitoring.

The methodology is the mooring-specific analogue of the wider
[risk-based-inspection](../concepts/risk-based-inspection.md)
practice on fixed-equipment integrity (API RP 580 / 581).

## Industry experience — published incidents

The OTC paper series captured operator experience and drove the
codification of mooring integrity practice:

- **OTC-25134** (2014) — operator-side experience report on permanent
  mooring failures and the integrity-management response, drawn from
  multiple GoM and West-Africa assets.
- **OTC-25273** (2014) — mooring-integrity management framework
  presentation by major-operator integrity engineering teams; one of
  the inputs to the API RP 2MIM scope.
- **OTC-26035** (2015) — mooring failure case histories with detailed
  failure-surface analysis; cited as evidence for the chain-stopper
  pawl-fatigue and chain-fairlead wear concerns.
- **Banff FPSO incident (December 2011)** — UK North Sea; multiple
  mooring lines parted in winter storm conditions; the asset broke
  free with risers still attached; widely cited as the canonical
  catastrophic-failure reference for the class.
- **Volve FPSO single-line failure (2016)** — Norwegian sector;
  single-line failure detected only on periodic monitoring review;
  reference for the case that monitoring-only without inspection is
  insufficient.
- **Gryphon-A FPSO (2011)** — UK North Sea; off-station event after
  multiple mooring failures; precursor to the wider integrity-management
  policy response.

These incidents collectively shifted the industry from reactive
"replace-when-broken" practice to the formal RP-2MIM /
DNV-OS-E301-aligned integrity programs now standard on permanent-moored
production assets.

## Practitioner application

The integrity-management surface has four main practitioner roles:

- **Operators** — own the integrity-management plan, fund the
  inspection campaign, hold the operational decision authority on
  station-keeping availability.
- **Mooring contractors** — design and install the original system,
  often retain a long-term service contract that covers component
  replacement and inspection support.
- **Classification societies** (ABS, BV, DNV, LR, RINA, ClassNK) —
  set the survey requirements, issue the period-of-validity
  certificates, and audit the integrity-management program against
  the relevant class rules.
- **Regulators** (UK HSE, NOPSEMA, BSEE, NPD/PSA, ANP, NPC) — set the
  facility-permit and country-specific regulatory requirements,
  conduct major-accident-hazard verification.

A mature integrity-management program ties all four roles to a single
shared dataset (the mooring monitoring system feed plus the inspection
history database) and re-runs the risk ranking at each major
review point.

### CP integration

Mooring-component external corrosion is controlled by the same
[cathodic-protection](../concepts/cathodic-protection.md) framework
used for the wider offshore structure. The chain and connector hardware
is in the immersion zone and is protected by sacrificial-anode or
ICCP installation; the integrity-management program tracks CP
potential as one of its monitored variables, and links the
corrosion-monitoring evidence to the chain-link diameter measurement
trend.

The hydrogen-embrittlement caveat for high-strength chain-shackle
material is a real concern under aggressive CP — see the CP page for
the over-protection threshold and the susceptible-alloy list.

## Cross-references

- [API RP 2SK](../standards/api-rp-2sk.md) — design-side anchor for
  permanent station-keeping.
- [DNV-OS-E301](../standards/dnv-os-e301.md) — DNV class-side
  position-mooring offshore standard; pilot for the calc-citation
  resolver.
- [cathodic-protection](cathodic-protection.md) — CP design for mooring components in the
  immersion zone.
- [fatigue-design-and-assessment](fatigue-design-and-assessment.md) — S-N + cumulative-damage method
  used in tension-history fatigue assessment.
- [risk-based-inspection](risk-based-inspection.md) — wider RBI methodology of which the
  mooring tier system is a specialisation.

## Source materials

- [O&G Papers catalog — OnePetro](../sources/og-standards-onepetro.md)
  — publisher-slice source page that flagged this concept gap during
  iter-41 W194 substrate review; OTC-25134/25273/26035 were the
  primary triggers.

## Standards not yet wiki-resolved (flagged for future ingest)

- **API RP 2I** — *In-service Inspection of Mooring Hardware for
  Floating Drilling Units* (MODU integrity-management foundation).
- **API RP 2MIM** — *Mooring Integrity Management* (the dominant
  US-side production-mooring integrity practice; will be cited as
  `standards/api-rp-2mim.md` once the standards page is created).
- **API Spec 2F** — *Mooring Chain* (manufacturing specification
  underpinning the chain-component side of the integrity discussion).
- **DNV-RP-F203** — *Dynamic Positioning Vessel Design Philosophy
  Guidelines* (DP integrity peer to permanent-mooring 2MIM).
- **DNV-RP-F205** — *Global Performance Analysis of Deepwater Floating
  Structures* (sets the analysis framework on which integrity
  re-assessment runs).
