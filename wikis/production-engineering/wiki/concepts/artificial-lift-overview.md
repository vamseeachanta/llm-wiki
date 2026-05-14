---
title: "Artificial Lift Overview"
tags: [artificial-lift, esp, gas-lift, pcp, plunger-lift, jet-pump, hydraulic-lift, rod-pump]
added: 2026-05-13
last_updated: 2026-05-13
---

# Artificial Lift Overview

## Scope

Production-engineering-side overview of the artificial-lift method families. **This page is the founding concept anchor for the production-engineering wiki domain** — together with drilling-engineering's [artificial-lift-method-selection.md](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md) it forms the bidirectional cross-link the scope-edge note on that page anticipated.

Most producing wells eventually need artificial lift — reservoir pressure declines over field life until natural flow stops; from that point onward, an external energy source is required to lift fluids to surface. Method selection at completion-design time is one of the most economically-leveraged decisions in a well's life-cycle.

## Six artificial-lift families

### 1. Sucker-Rod Pumping (Rod Pump / Beam Pump)

**See: [drilling-engineering/sucker-rod-pumping-overview.md](../../../drilling-engineering/wiki/concepts/sucker-rod-pumping-overview.md)** — rod-pump deep coverage is housed in drilling-engineering per the API "drilling and well servicing" umbrella. Production-engineering scope is the method-selection context only.

- ~80% of producing US wells
- Low rate (< 1,000 bbl/d), shallow-to-medium depth (< 12,000 ft)
- Mature operations, low cost, tolerates declining inflow

### 2. Electric Submersible Pumps (ESP)

- **Mechanism** — downhole multi-stage centrifugal pump driven by an electric motor; power delivered via armored cable from surface variable-frequency drive (VFD)
- **Rate** — high (500-30,000 bbl/d typical; specialty units to 60,000+)
- **Depth** — moderate (< 15,000 ft); deeper for HPHT-rated ESPs
- **Strengths** — very high rate capacity, compact downhole footprint, remote monitoring via VFD instrumentation
- **Weaknesses** — power-cable failure is the dominant workover trigger, intolerant of significant free gas at intake, intolerant of solids, mid-cost to high-cost
- **Standards** — API RP 11S family (RP 11S design, RP 11S1 install, RP 11S2 operations, RP 11S4 sizing, RP 11S7 connector)
- **Vendors** — Schlumberger REDA, Baker Hughes Centrilift, Borets, Wood Group ESP (acquired by Baker Hughes 2017)
- **Detailed page** — `concepts/electric-submersible-pumps.md` (planned Phase 1)

### 3. Gas Lift

- **Mechanism** — high-pressure gas injected down the casing-tubing annulus, enters production tubing through gas-lift valves at controlled depths, reduces fluid column density; reservoir pressure then lifts the lighter column
- **Rate** — 100-30,000 bbl/d
- **Depth** — effectively unlimited (depth-limited by available injection-gas pressure, not by mechanical limits)
- **Strengths** — no moving downhole parts (long mean-time-to-failure), handles high gas-liquid ratio, works in deviated wells, gentle on wellbore
- **Weaknesses** — requires available high-pressure gas source and surface compression, lower efficiency at low rate, valve workovers when gas-lift valves fail
- **Variants** — continuous gas lift (steady injection), intermittent gas lift (cyclic injection for low-rate wells)
- **Standards** — API RP 11V6 (gas-lift design), API RP 11V2 (gas-lift valve performance)
- **Detailed page** — `concepts/gas-lift-overview.md` (planned Phase 1)

### 4. Progressing-Cavity Pumps (PCP)

- **Mechanism** — downhole helical rotor turning inside an elastomeric stator; positive-displacement pump driven by surface motor through a rotating rod string
- **Rate** — < 4,000 bbl/d
- **Depth** — < 8,000 ft typical
- **Strengths** — handles high-viscosity oil and solids better than ESP or rod pump; common in heavy oil
- **Weaknesses** — elastomer chemical compatibility limits service environment; depth-limited; rotating rod string adds wear
- **Variants** — surface-driven PCP (most common), electric-submersible PCP (no surface rod string)
- **Detailed page** — `concepts/progressing-cavity-pumps.md` (planned Phase 1)

### 5. Plunger Lift

- **Mechanism** — gas-driven free piston cycles between bottomhole and surface, sweeping liquid up the tubing on each cycle
- **Rate** — < 200 bbl/d liquid (this is a low-rate method)
- **Depth** — < 12,000 ft typical
- **Strengths** — no surface pump, minimal equipment, energy comes from reservoir gas (no external power)
- **Weaknesses** — requires gas drive, rate-limited, cycle-time management needed
- **Use case** — liquid-loaded gas wells where the gas can't lift accumulated water without help
- **Detailed page** — `concepts/plunger-lift.md` (planned Phase 1)

### 6. Jet Pump and Hydraulic Lift

- **Mechanism** — power fluid pumped down a parallel string drives a jet (Venturi-style) or piston pump at depth; returned with produced fluid up the production tubing
- **Rate** — moderate (200-15,000 bbl/d)
- **Depth** — effective at deep wells (> 15,000 ft)
- **Strengths** — no moving downhole parts (jet pump variant), good for deep / deviated wells
- **Weaknesses** — surface power-fluid system adds complexity, lower overall efficiency than ESP at design point
- **Detailed page** — `concepts/jet-pump-hydraulic-lift.md` (planned Phase 1)

## Method-selection rubric (production-engineering framing)

The drilling-engineering page presents the method-selection comparison from completion-design-time. The production-engineering framing differs in two ways:

1. **Lifecycle-aware** — methods that work early-life (rod pump for slow-decliner wells) versus late-life (gas lift for high-water-cut wells) and the *transition cost* between methods
2. **Field-level optimization** — when a field has many wells, the right answer is often a *mix* of methods; this perspective is invisible from a single-well drilling-engineering view

| Criterion | Rod | ESP | Gas Lift | PCP | Plunger | Jet/Hydraulic |
|---|---|---|---|---|---|---|
| Typical rate (bbl/d) | < 1,000 | 500-30,000 | 100-30,000 | < 4,000 | < 200 | 200-15,000 |
| Depth limit | < 12,000 | < 15,000 | unlimited | < 8,000 | < 12,000 | > 15,000 |
| Free-gas tolerance | low | very low | excellent | moderate | excellent | moderate |
| Solids tolerance | moderate | poor | excellent | excellent | moderate | moderate |
| CAPEX | low | high | moderate | low-moderate | very low | moderate |
| OPEX | low | moderate | high (gas) | low | very low | moderate |
| Workover frequency | medium | high (cable) | low | medium | low | medium |
| Field-mix coverage | very common | common | very common | niche | gas-well-specific | niche |

## Public references

- **Takacs, Gabor** — *Electrical Submersible Pumps Manual*, Gulf Professional Publishing, 2e 2017 (ISBN 978-0-12-814570-8)
- **Takacs, Gabor** — *Gas Lift Manual*, PennWell 2005 (ISBN 0-87814-805-1)
- **Takacs, Gabor** — *Sucker-Rod Pumping Manual*, PennWell 2003 (ISBN 978-0-87814-892-5) — cited from drilling-engineering rod-pump pages
- **Brown, Kermit E.** — *The Technology of Artificial Lift Methods*, multi-volume, PennWell — Vol 1 (1977, plunger lift + gas lift), Vol 2a (1980, sucker rod), Vol 2b (1980, ESP / hydraulic / PCP), Vol 4 (1984, field application case studies). Older but still cited.
- **Lyons (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1) — artificial-lift section
- **API RP 11S family** — ESP design, application, installation guidance (publisher pages: api.org)
- **API RP 11V6** — gas-lift design

## Cross-references

- **Drilling-engineering counterpart**: [Artificial-Lift Method Selection](../../../drilling-engineering/wiki/concepts/artificial-lift-method-selection.md) — completion-design-time framing
- **Drilling-engineering rod-pump cluster** (rod-pump stays there): [Sucker-Rod Pumping Overview](../../../drilling-engineering/wiki/concepts/sucker-rod-pumping-overview.md), [API 11AX Pump Designation](../../../drilling-engineering/wiki/concepts/api-11ax-pump-designation.md), [API 11L Design Charts](../../../drilling-engineering/wiki/concepts/api-11l-design-charts.md), [Pump Cards and Dynamometer](../../../drilling-engineering/wiki/concepts/pump-cards-and-dynamometer.md), [Sucker Rods and Tapered Strings](../../../drilling-engineering/wiki/concepts/sucker-rods-and-tapered-strings.md)
- **Future production-engineering detailed pages** (planned Phase 1): `electric-submersible-pumps.md`, `gas-lift-overview.md`, `gas-lift-valve-design.md`, `progressing-cavity-pumps.md`, `plunger-lift.md`, `jet-pump-hydraulic-lift.md`
