---
title: "Sucker-Rod Pumping Overview"
tags: [rod-pump, artificial-lift, sucker-rod, beam-pump, polished-rod, downhole-pump]
sources:
  - api-spec-11ax
  - api-rp-11l
  - api-spec-11b
added: 2026-05-13
last_updated: 2026-05-13
---

# Sucker-Rod Pumping Overview

## Scope

The sucker-rod-pumping artificial-lift system as a whole — surface pumping unit, polished rod, sucker-rod string, downhole pump — and the operating principles that connect them. Scope-edge note: rod pump is post-drilling artificial lift, but is included in drilling-engineering per the API "drilling and well servicing" umbrella; it sits at the well-completion / production-engineering boundary.

## Why sucker-rod pumping dominates

Approximately 80% of producing US wells use sucker-rod pumping. Reasons:

- **Low capital and operating cost** for low-rate stripper wells
- **Mature operations** — every field operator has crews trained on rod-pump maintenance
- **Tolerant of varying inflow** — well kicks back from declining flow rates without operator intervention
- **Simple failure modes** — broken rods, worn pumps, leaking tubing are all repairable in a routine workover

## System anatomy (surface to bottomhole)

1. **Prime mover** — diesel engine or electric motor on the pumping unit.
2. **Pumping unit** — beam pump (conventional), Mark II (counterbalance-shifted), RotaFlex (long-stroke), hydraulic long-stroke. Translates rotary engine motion into vertical reciprocating polished-rod motion.
3. **Polished rod** — precision-machined surface rod inside the wellhead stuffing box, providing dynamic seal at surface.
4. **Pony rods** — short adjustment lengths for fine-tuning string length.
5. **Sucker-rod string** — typically 25 ft or 30 ft joints, threaded couplings, frequently tapered (multiple rod-diameter sections from larger near surface to smaller near pump).
6. **Downhole pump** — barrel-and-plunger reciprocating positive-displacement pump with standing valve (intake) and traveling valve (discharge to tubing). See [API 11AX Pump Designation](api-11ax-pump-designation.md).
7. **Producing tubing** — production-tubing string conducts fluid up to surface.

## Operating cycle

- **Upstroke** — plunger lifts, traveling valve closes (column above plunger lifts), standing valve opens (formation fluid enters barrel below plunger).
- **Downstroke** — plunger descends, standing valve closes (formation fluid trapped in barrel), traveling valve opens (fluid passes around plunger into tubing column).
- Net: each cycle delivers one barrel-volume of fluid to the tubing column.

## Public references

- **API Spec 11AX** — [api-spec-11ax.md](../standards/api-spec-11ax.md). Pump component specs.
- **API RP 11L** — [api-rp-11l.md](../standards/api-rp-11l.md). Design calculations.
- **API Spec 11B** — [api-spec-11b.md](../standards/api-spec-11b.md). Sucker-rod elements.
- **Takacs, Gabor** — *Sucker-Rod Pumping Manual*, PennWell 2003 (ISBN 978-0-87814-892-5). Practitioner-canonical reference.
- **Lyons (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, artificial-lift section.

## Cross-references

- [API 11AX Pump Designation](api-11ax-pump-designation.md), [API 11L Design Charts](api-11l-design-charts.md), [Pump Cards and Dynamometer](pump-cards-and-dynamometer.md), [Sucker Rods and Tapered Strings](sucker-rods-and-tapered-strings.md)
- [Artificial-Lift Method Selection](artificial-lift-method-selection.md)
