---
title: "Wind Loads on Offshore and Onshore Industrial Structures"
slug: wind-loads
tags:
  - environmental-loads
  - wind
  - metocean
  - hurricane
  - typhoon
  - offshore
  - lng
  - facility-design
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - sources/og-standards-asce.md
cross_links:
  - standards/api-rp-2met.md
  - standards/dnv-rp-c205.md
  - standards/iso-19901-1.md
extraction_policy: metadata-and-doctrinal-synthesis
---

# Wind Loads on Offshore and Onshore Industrial Structures

## Why wind-loads matter

Wind is one of the three governing environmental load families (wind,
wave, current) on offshore steel and the dominant lateral load on most
onshore industrial structures above grade. For an offshore jacket or
floating production unit the wind-on-topsides component sets a large
share of the global-overturning moment that drives mooring or pile
sizing. For an LNG storage tank the wind-on-shell component drives the
anchorage design at the tank base and the buckling check of the
windward primary container. For an onshore gas-processing facility,
wind sets pipe-rack anchor forces, vessel anchor-bolt sizing, flare-stack
guy-wire tensions, and cooling-tower hold-down design.

Because wind acts continuously and turbulently, two design questions
must be answered jointly:

1. **Static (mean-pressure) sizing** — what reference wind speed and
   what height/exposure-corrected pressure does the structure resist
   at the design return period?
2. **Dynamic response** — does the structure have natural periods or
   along-wind / across-wind response that requires a gust-response
   factor, vortex-shedding check, or full aeroelastic analysis?

The two questions are answered by different chapters of the same code
family but cannot be separated in a defensible design.

## Doctrinal evolution

Wind-load codification has tracked the evolution of meteorological
measurement and structural-reliability theory:

- **Beaufort scale (1805 onward)** — qualitative wind classification
  by sea-state appearance; useful for marine operations, never used
  as a design-load basis.
- **First quantitative codes (1930s–1960s)** — early ASCE / British /
  Russian codes used a fastest-mile or 10-min-mean reference wind speed
  with empirical pressure coefficients tabulated for common building
  geometries.
- **ASCE 7 modern era (1995 onward)** — three-second gust at 10 m
  height in Exposure C as the reference, ultimate-strength-design-paired
  load factors, importance-category mapping to MRI (mean recurrence
  interval), and explicit hurricane-zone basic wind-speed contours.
- **ISO 19901-1 + DNV-RP-C205 + API RP 2MET (2000s onward)** — the
  offshore branch of the codification; 1-hour-mean reference at 10 m
  above mean sea level, separate spectra for along-wind, vertical, and
  across-wind turbulence, regional 100-year metocean envelopes for
  GoM hurricane / NW-Australia tropical-cyclone / North-Sea winter-storm
  regimes, and explicit treatment of platform topsides aerodynamics.
- **Eurocode EN 1991-1-4 (2005 onward)** — harmonised European method
  with 10-min-mean reference, terrain-roughness categories I–IV,
  procedure-1 and procedure-2 dynamic methods, and orography
  multipliers for hill / cliff sites.

The two branches (onshore ASCE / Eurocode vs. offshore API/DNV/ISO)
have not fully converged. The reference averaging time, height, and
exposure category differ between branches, so a wind-speed value
quoted from one branch cannot be plugged directly into a formula from
the other branch without a conversion.

## Wind-load determination — the framework

Across the major codes the design wind pressure on a surface element
is built up from a small number of factors:

```
p = (1/2) · ρ_air · V_ref^2 · K_z · K_zt · K_d · I · G · C_p
```

| Factor | Meaning | Typical code source |
|---|---|---|
| `ρ_air` | Air density (≈ 1.225 kg/m³ standard) | ASCE 7 §26 / DNV-RP-C205 §2 |
| `V_ref` | Basic wind speed at reference height & averaging time | ASCE 7 wind-zone maps / RP-2MET regional envelope |
| `K_z` | Velocity-pressure exposure coefficient (height & exposure) | ASCE 7 Table 26.10-1 / Eurocode terrain class |
| `K_zt` | Topographic factor (hill, ridge, escarpment) | ASCE 7 §26.8 / EN 1991-1-4 §4.3.3 |
| `K_d` | Wind-directionality factor | ASCE 7 §26.6 / Eurocode `c_dir` |
| `I` | Importance factor (life-safety classification) | ASCE 7 Table 1.5-2 / RP-2MET Risk Class |
| `G` | Gust-response (or peak-factor / dynamic-response) factor | ASCE 7 §26.11 / Eurocode `c_sc_d` |
| `C_p` | External / internal pressure coefficient (geometry) | ASCE 7 Ch. 27–30 / Eurocode §7 |

Each branch tabulates these coefficients for its set of canonical
geometries (gable roof, low-rise, open frame, chimney, lattice tower,
storage tank, jacket truss, FPSO topsides). The arithmetic is the same;
the inputs are not.

### Reference wind speed and averaging time

This is the most-mistranscribed input across branches:

| Branch | Averaging | Reference height | Notation |
|---|---|---|---|
| ASCE 7 (modern) | 3-second gust | 10 m / 33 ft | `V` |
| Eurocode EN 1991-1-4 | 10-minute mean | 10 m | `v_b` |
| API RP 2MET / ISO 19901-1 / DNV-RP-C205 (offshore) | 1-hour mean | 10 m above MSL | `U_w` or `V̄_{1h}` |
| Older ASCE / fastest-mile codes | Fastest mile (≈ 1-min) | 10 m | `V_fm` |

Conversion between averaging times uses the [Durst gust factor](https://en.wikipedia.org/wiki/Wind_gust)
or, for offshore application, the API/ISO turbulence-intensity profile.
A 3-second-gust value is roughly 1.45–1.55× the 1-hour-mean value at
10 m in open terrain — a factor large enough that mixing branches
without conversion silently inflates or deflates the design pressure
by 50% or more.

### Exposure / terrain category

ASCE 7 uses three exposure categories (B urban/suburban,
C open terrain, D unobstructed water). Eurocode uses four (I sea/lakes,
II open country, III suburban, IV city). Offshore wind work uses
either ASCE 7 Exposure D or the API/DNV "open sea" profile, which is
slightly more aggressive than Exposure D because there is no fetch
limitation and no transition from rougher to smoother terrain.

### Importance / risk classification

The importance factor scales the design wind speed (or directly scales
the velocity-pressure) to set the target reliability:

| Branch | Class system | Target MRI |
|---|---|---|
| ASCE 7 | Risk Cat I–IV | 300 / 700 / 1700 / 3000 yr |
| API RP 2MET | L-1 / L-2 / L-3 | 100 yr / 25 yr / 5 yr (factory MOPU exposure) |
| ISO 19901-1 | Exposure Level L1 / L2 / L3 | Same family as RP-2MET |

Offshore manned production platforms are typically L-1 (100-yr design
condition); offshore unmanned satellite structures may be L-2 or L-3.
The classification drives the regional metocean envelope, not just a
multiplier.

## Codes — branch by branch

### Onshore — ASCE 7 and Eurocode

- [**ASCE 7**](../standards/asce-7.md)
  *Minimum Design Loads and Associated Criteria for Buildings and Other
  Structures.* The dominant US wind-load code; chapters 26–31 are the
  wind provisions. Splits the design between Main Wind Force Resisting
  System (MWFRS, global stability) and Components and Cladding (C&C,
  local pressures). The basic-wind-speed contours embed the
  hurricane-coast 700-yr ultimate map.
- **EN 1991-1-4 — Eurocode 1 Part 1-4** (placeholder — not yet
  wiki-resolved). Wind actions for the EU; harmonised with national
  annexes that supply country-specific basic wind speeds.

### Offshore metocean trio

- [**API RP 2MET**](../standards/api-rp-2met.md) — *Derivation of
  Metocean Design and Operating Conditions.* The US-side offshore
  metocean code; tabulates regional 100-year wind speed, current,
  wave-height envelopes for the Gulf of Mexico, US Atlantic, US
  Pacific, and gives the framework for derived combinations. Joint
  development with ISO 19901-1; substantively aligned.
- [**DNV-RP-C205**](../standards/dnv-rp-c205.md) — *Environmental
  Conditions and Environmental Loads.* The offshore wind / wave /
  current method and reference data, used worldwide by DNV-class
  offshore designs. Includes turbulence-intensity profiles, mean-wind
  and gust spectra (NPD / Frøya / Kaimal), and combined-environment
  analysis.
- [**ISO 19901-1**](../standards/iso-19901-1.md) — *Metocean Design
  and Operating Considerations.* The international harmonisation;
  ISO 19900 family parent for metocean across fixed, floating, and
  subsea structures.

The three offshore codes do not exactly agree on every coefficient,
but the combinations they produce are within a few percent of each
other for the canonical Gulf-of-Mexico / North-Sea / NW-Australia
regions. A design that follows any one of the three is normally
acceptable to operators and class societies in those regions.

## Practitioner application

### Offshore platforms and FPSO topsides

For a fixed jacket the wind load contributes the smallest of the three
environmental drivers (wave is dominant, current second, wind third),
but it is not negligible because it acts on the largest moment-arm
(topsides above the splash zone). For a deep-draft floating unit the
wind force on topsides drives the steady-offset component of the
station-keeping system and combines non-linearly with low-frequency
wave drift to set mean mooring tension.

The drag-shape coefficient `C_s` for a platform topsides cluster is
geometry-specific and is normally derived by:

- itemised method — sum of `C_s · A_proj` for each topsides element
  per RP-2MET / RP-C205 tabulated drag coefficients, or
- wind-tunnel testing for non-standard geometries (FPSO with above-deck
  process modules, floating LNG with cryogenic storage above deck,
  semi with concentrated topsides clusters).

Hurricane-rated US Gulf-of-Mexico installations design to a 100-year
hurricane envelope per RP-2MET; the wind coordinate is paired with a
companion wave / current envelope so that the combined load is
self-consistent.

### LNG storage tanks

Above-ground LNG tanks (full-containment 9% Ni inner / pre-stressed
concrete outer) are governed by ASCE 7 (US sites) or Eurocode
(EU sites) for wind. The critical checks are:

- anchorage of the inner tank against wind-uplift on the dome roof,
- buckling of the outer concrete shell windward face under the
  combined wind + thermal load,
- piping and platform attachments routed up the tank exterior, where
  C&C pressures exceed MWFRS pressures by a wide margin.

US Gulf-coast LNG export terminals (Sabine Pass, Cameron, Corpus
Christi, Plaquemines, Rio Grande) sit in the ASCE 7 hurricane zone
with basic wind speeds in the 130–180 mph (3-s gust) range, and
the foundation / anchorage design is dominated by the wind case for
the empty tank.

### Onshore gas-processing and refining facilities

Pipe racks, vertical vessels, fired heaters, and flare stacks are
governed by ASCE 7 (US) or the local national code. Tall slender
elements (flare stacks, fractionation columns above ~50 m) require
both:

- a static / quasi-static MWFRS check using the gust-response factor,
  and
- a vortex-shedding check at the lock-in wind speed, since the across-wind
  response can govern over the along-wind response for
  high-aspect-ratio cylinders.

Stacks are normally fitted with helical strakes or a damping ring
when the lock-in check is violated; this is design practice rather
than a code mandate, but it is nearly universal.

### Cooling towers, fin-fans, modular packages

Cooling-tower fan stacks and fin-fan banks have published manufacturer
wind-load drawings that already include the gust factor and the
shape coefficient for the assembly. The site-specific work is to
confirm that the manufacturer's basic wind speed and exposure are at
or above the site's, and to design the structural-steel support to
the same reference.

## Design wind speed — regional and return-period considerations

The design wind speed is the **product** of two choices:

1. The geographic basic-wind-speed value at the reference averaging
   time and height (from a national / regional contour map or a
   site-specific metocean study).
2. The mean recurrence interval (MRI) appropriate to the consequence
   class of the asset.

US onshore practice (ASCE 7) builds the MRI into the contour map via
the Risk Category — a Risk Cat II ordinary occupancy reads from the
700-year map, a Risk Cat IV essential facility reads from the 3000-year
map. There is no separate importance-factor multiplication on the
wind speed in modern ASCE 7.

US offshore practice (RP-2MET) **separates** the MRI from the contour:
the regional metocean envelope is published at the 100-year MRI, and
the exposure-level (L-1 / L-2 / L-3) selects which combination of
return-period values is used for the design case. The numbers do not
mix with onshore values without adjustment.

Internationally, ISO 19901-1 follows the offshore-API pattern; Eurocode
follows the onshore-ASCE pattern with national-annex basic wind speeds
calibrated to a 50-year MRI (the multiplier to other return periods is
in EN 1991-1-4 §4.2).

## Hurricane / typhoon design — regional regimes

Three regions dominate the offshore-hurricane / -typhoon literature,
each with its own metocean envelope and its own catastrophic-event
reference cyclone:

| Region | Reference cyclones | Code | 100-yr 1-h-mean wind (open sea, indicative) |
|---|---|---|---|
| Gulf of Mexico | Camille 1969, Andrew 1992, Ivan 2004, Katrina/Rita 2005, Ike 2008 | API RP 2MET | ≈ 41–46 m/s |
| NW Australia | Olivia 1996 (Barrow Is. record), Vance 1999, George 2007 | DNV-RP-C205 + national | ≈ 45–55 m/s (cyclonic-coast worst case) |
| North Sea | December 1990, "New Year" 1992, Andrea 2007 | DNV-RP-C205 + NORSOK | ≈ 38–42 m/s |
| US Atlantic / Caribbean | Hugo 1989, Wilma 2005, Maria 2017 | API RP 2MET / ISO 19901-1 | ≈ 38–44 m/s |

The numerical values above are illustrative practitioner ranges drawn
from publicly available metocean summaries; for a real design the
project-specific metocean criteria document is the controlling input.

GoM hurricane experience after Ivan/Katrina/Rita (multiple platform
losses) drove the 2007 revision of API RP 2MET and the introduction of
the explicit L-1/L-2/L-3 exposure-level system. The post-2007 design
basin is markedly more demanding than the pre-2005 envelope.

## Cross-references

- [API RP 2MET](../standards/api-rp-2met.md) — offshore metocean
  envelope and exposure-level framework (US / international).
- [DNV-RP-C205](../standards/dnv-rp-c205.md) — environmental conditions
  and loads (DNV class worldwide).
- [ISO 19901-1](../standards/iso-19901-1.md) — international metocean
  harmonisation.
- [[fatigue-design-and-assessment]] — wind-induced vortex-shedding
  fatigue is one of the inputs to mechanical-fatigue assessment of
  slender stacks and risers.
- [[mechanical-fatigue]] — VIV / vortex-induced fatigue is a sibling
  topic for slender structures under wind or current.

## Source materials

- [O&G Standards catalog — ASCE](../sources/og-standards-asce.md)
  — publisher-slice source page that flagged this concept gap during
  iter-41 W194 substrate review.

## Standards not yet wiki-resolved (flagged for future ingest)

- **ASCE 7** — *Minimum Design Loads for Buildings and Other Structures.*
  US onshore wind-load anchor; will be cited as `standards/asce-7.md`
  once the standards page is created.
- **EN 1991-1-4** — Eurocode 1 Part 1-4 wind actions; international
  branch peer to ASCE 7.
- **NBR 6123** (Brazil), **AS/NZS 1170.2** (Australia/New Zealand),
  **GB 50009** (China) — major non-US/EU national wind codes; relevant
  for project-specific application outside the Anglo / EU branches.
