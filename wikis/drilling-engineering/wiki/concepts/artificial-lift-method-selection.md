---
title: "Artificial-Lift Method Selection"
tags: [artificial-lift, rod-pump, esp, gas-lift, pcp, plunger-lift, method-selection]
sources:
  - api-spec-11ax
  - api-rp-11l
added: 2026-05-13
last_updated: 2026-05-13
---

# Artificial-Lift Method Selection

## Scope

Comparison and selection across the five common artificial-lift methods — sucker-rod pumping (rod pump), electric submersible pump (ESP), gas lift, progressing-cavity pump (PCP), and plunger lift. Scope-edge note: this concept page extends slightly past pure drilling-engineering into completions / production-engineering territory; it lives here to anchor the rod-pump sub-issue context, and will re-route to a future production-engineering domain when one is founded.

## The five methods

### Rod pump (sucker-rod pumping)

- **Mechanism** — surface beam pump reciprocates downhole positive-displacement pump via sucker-rod string
- **Best for** — low-to-moderate rate (< 1,000 bbl/d), shallow-to-medium depth (< 12,000 ft), conventional crude
- **Strengths** — lowest cost, mature operations, tolerates declining inflow, simple repairs
- **Weaknesses** — depth-limited by rod-string mechanical limits, poor for high gas-liquid ratio, slow response to inflow changes
- **Coverage** — ~80% of US producing wells

### Electric submersible pump (ESP)

- **Mechanism** — downhole electric centrifugal multi-stage pump driven by surface-supplied power cable
- **Best for** — high rate (500-30,000 bbl/d), moderate depth, low-to-moderate viscosity
- **Strengths** — very high rate capacity; compact downhole footprint; remote monitoring
- **Weaknesses** — power-cable failure is common workover trigger; intolerant of free gas; expensive

### Gas lift

- **Mechanism** — high-pressure gas injected down annulus, enters production tubing through gas-lift valves, reduces fluid column density; reservoir pressure lifts the lighter column
- **Best for** — wells with associated gas-handling capacity, deep wells, high gas-liquid ratio
- **Strengths** — no moving downhole parts; works with high free-gas; works in deviated wells
- **Weaknesses** — requires high-pressure gas source / compression; less efficient at low rate

### Progressing-cavity pump (PCP)

- **Mechanism** — downhole helical-stator-and-rotor positive-displacement pump driven by surface motor through rotating rod string
- **Best for** — high-viscosity oil, heavy oil, sand production
- **Strengths** — handles solids and viscous fluid better than rod pump or ESP
- **Weaknesses** — elastomer-stator chemical compatibility limits; depth-limited

### Plunger lift

- **Mechanism** — gas-driven free-piston cycles between bottomhole and surface, sweeping liquid up the tubing
- **Best for** — gas wells with liquid loading at low rate
- **Strengths** — no surface pump; minimal equipment; energy comes from reservoir gas
- **Weaknesses** — requires gas-drive; rate-limited

## Selection comparison

| Criterion | Rod pump | ESP | Gas lift | PCP | Plunger lift |
|---|---|---|---|---|---|
| Typical rate | < 1,000 | 500-30,000 | 100-30,000 | < 4,000 | < 200 (liquid) |
| Depth limit | < 12,000 ft | < 15,000 ft | unlimited | < 8,000 ft | < 12,000 ft |
| Free-gas tolerance | low | very low | excellent | moderate | excellent |
| Solids tolerance | moderate | poor | excellent | excellent | moderate |
| Capital cost | low | high | moderate | low-moderate | very low |
| Operating cost | low | moderate | high (gas) | low | very low |

## Selection drivers

Rule-of-thumb:
- Liquid-loaded gas well → plunger lift
- Low-rate routine oil → rod pump (default)
- High-viscosity / heavy oil → PCP or rod pump with care
- High-rate / deep / available power → ESP
- High-rate / available gas / deep / deviated → gas lift

The selection process is iterative: an initial method picks based on rate-and-depth screening, then refines based on fluid properties, gas-liquid ratio, sand cut, and economic constraints.

## Public references

- **Takacs 2003** *Sucker-Rod Pumping Manual* — comparison framework
- **Brown 1980** *Technology of Artificial Lift Methods* — multi-volume canonical reference
- **Lyons handbook** — artificial-lift comparison section

## Cross-references

- [Sucker-Rod Pumping Overview](sucker-rod-pumping-overview.md), [API 11AX Pump Designation](api-11ax-pump-designation.md), [API 11L Design Charts](api-11l-design-charts.md), [Pump Cards and Dynamometer](pump-cards-and-dynamometer.md), [Sucker Rods and Tapered Strings](sucker-rods-and-tapered-strings.md)

## Scope-edge note — production-engineering domain founded 2026-05-13

This page describes methods beyond rod pump (ESP, gas lift, PCP, plunger lift) that are strictly production-engineering / completions-engineering content. They live here to anchor the rod-pump method-selection context from drilling-engineering's framing.

**The `production-engineering/` wiki domain was founded 2026-05-13 in commit [`7dc802d1`](https://github.com/vamseeachanta/llm-wiki/commit/7dc802d1).** Its founding concept anchor [Artificial Lift Overview](../../../production-engineering/wiki/concepts/artificial-lift-overview.md) is the production-engineering-side counterpart to this page; together they form the bidirectional cross-link this scope-edge note had been anticipating.

**Scope split now operational:**

- **Drilling-engineering (this page + the rod-pump cluster)** — completion-design-time framing of method selection, rod-pump deep coverage per the API "drilling and well servicing" umbrella
- **Production-engineering** — production-design-time framing of method selection, deep coverage of the other 4 method families (ESP, gas lift, PCP, plunger lift) plus jet pump and hydraulic lift, lifecycle-aware re-selection (early-life vs late-life), field-mix optimization across multiple wells

Rod-pump deep coverage **stays in drilling-engineering** — see [Sucker-Rod Pumping Overview](sucker-rod-pumping-overview.md) and the rest of the cluster.
