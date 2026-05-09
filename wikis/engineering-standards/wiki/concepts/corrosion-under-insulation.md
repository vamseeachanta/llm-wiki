---
title: "Corrosion Under Insulation (CUI)"
slug: corrosion-under-insulation
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - cui
  - insulated-piping
  - austenitic-scc
  - refinery
  - offshore
  - intermittent-wet-dry
  - scaffolding-cost
sources:
  - ../standards/api-rp-571.md
  - ../sources/og-standards-api.md
---

# Corrosion Under Insulation (CUI)

> Concept anchor for the external-corrosion damage family that occurs beneath thermal insulation, fireproofing, and weather-protection cladding. Bidirectional with [api-rp-571](../standards/api-rp-571.md) (mechanism catalogue, §4 loss-of-thickness), [api-rp-581](../standards/api-rp-581.md) (RBI damage factor), [api-510](../standards/api-510.md), [api-570](../standards/api-570.md), and [api-rp-574](../standards/api-rp-574.md). Routes upstream from [[damage-mechanism-screening]] and downstream into [[risk-based-inspection]] and [[corrosion-rate-measurement]].

## What is CUI?

**Corrosion Under Insulation (CUI)** is external corrosion of metallic surfaces beneath thermal insulation, fireproofing, or weather-protection cladding. It is driven by intermittent moisture ingress (rain, condensate, deluge / firewater, equipment washing, marine spray) combined with **chloride or other corrosive contaminants** dissolved in the insulation matrix, and the inability of the steel surface to fully dry between wettings. Operating temperature governs severity: for **carbon steel**, the worst window is roughly **−12 °C to ~175 °C**, with peak rates in the boiling-water band; for **austenitic stainless steel**, the chloride-stress-corrosion-cracking (CISCC) risk extends to ~205 °C and beyond, because evaporation at the metal surface concentrates chlorides faster than they are flushed away.

CUI is the dominant external-damage mechanism on insulated process piping and pressure vessels in refineries, petrochemical plants, LNG / cryogenic terminals, FPSOs, and offshore production platforms.

## Why CUI is operationally vicious

| Property | Why it matters |
|---|---|
| Hidden | The insulation jacket conceals damage until a thickness-loss patch becomes a leak or an austenitic crack vents to atmosphere. Visual inspection of the jacket is a poor proxy for the steel beneath. |
| Cyclic wet–dry | The wet phase corrodes; the dry phase concentrates chlorides and sulphates at the steel surface; the next rainfall re-wets a now-more-aggressive electrolyte. The cycle repeats every weather event. |
| High inspection cost | Direct UT access requires insulation removal **and scaffolding** for elevated piping. Scaffolding-plus-stripping is often the largest single line item in an inspection campaign budget. |
| Long latency | First-detected damage is commonly **>10 years** into service. Coatings degrade slowly, jacketing seals fail at known weak points (penetrations, hangers, low-points), and the failure mode is ratchet-like. |
| Variable rate | Typical rates fall in the **0.05–0.5 mm/yr** range but can spike to **>1 mm/yr** at chloride hot spots (drips below cooling-tower plumes, deluge nozzles, marine-spray bands). Single-CML estimates can mislead by an order of magnitude. |

## Two CUI mechanism families

CUI is not a single mechanism — it is a service envelope that hosts at least two distinct degradation modes that demand different mitigation and inspection strategies.

- **CS-CUI (carbon-steel CUI)** — external general and pitting corrosion of carbon steel and low-alloy steels, accelerated by salt deposition, dirt loading, and the insulation acting as a wick that holds water against the metal surface long after the surrounding atmosphere has dried. Damage morphology is patchy thinning, often with localized deep pits at insulation seams and termination points.
- **CISCC-CUI (chloride-induced stress-corrosion cracking under insulation)** — chloride-SCC of austenitic stainless steels, almost always the 304 / 304L / 316 / 316L family, occurring under chloride-rich wet insulation. The morphology is **transgranular branched cracking** that often propagates **through wall** with little prior warning, making CISCC a leak-before-break-violating mechanism in practice. Because austenitic SS resists general corrosion, operators have historically under-inspected stainless lines under insulation — a false-confidence trap that several high-profile refinery and offshore failures have made expensive lessons.

## Two service-temperature windows

| Material | Worst T window | Mechanism note |
|---|---|---|
| Carbon steel | **−12 to ~150 °C** (worst around **65–100 °C**, the boiling-water band) | Wet film persists; oxygen diffusion + chloride concentration are both active. Below −12 °C the surface stays frozen and corrosion stalls; above ~175 °C the surface dries faster than it re-wets. |
| Austenitic SS | **60 to ~205 °C** (and somewhat higher for high-chloride insulation) | CISCC requires a surface temperature high enough to drive evaporative concentration of chlorides but not so high that the surface stays bone-dry between wettings. The upper bound is service- and chloride-load-dependent. |

Cold-service equipment (LNG, cryogenic, cold-end refrigeration) sits below the carbon-steel window during normal operation, but **transient warm-up cycles** (defrost, shutdown, regeneration) sweep the steel through the worst window — making cold service a nontrivial CUI risk despite the steady-state temperature.

## Inspection methods

- **Profile (or tangential) radiography** — RT through insulation; resolves wall-thickness profile without stripping. Throughput-limited and access-limited.
- **Pulsed eddy-current (PEC)** — through-insulation average-thickness screening; good for large-area triage, poor for localized pitting.
- **Guided-wave UT (GWUT)** — long-range coverage from a single coupling point; useful for buried, sleeved, and elevated insulated piping where scaffolding cost dominates.
- **Insulation removal + UT spot** — gold-standard for direct thickness measurement and CISCC dye-penetrant inspection; applied at PEC / GWUT-flagged hot spots and at high-consequence circuits per RBI plan.
- **Infrared thermography** — limited utility; detects wet-insulation patches and missing insulation but does not directly image steel-side damage.
- **Real-time radiography (RTR)** — same physics as profile RT, faster image cycle for high-throughput campaigns.
- **Magnetic-flux-leakage (MFL)** — applicable to insulated tank shells and floor-to-shell weld bands.

Selection follows the [api-rp-574](../standards/api-rp-574.md) inspection-practices framework and is gated by the [api-rp-581](../standards/api-rp-581.md) damage-factor / inspection-effectiveness tables.

## Mitigation hierarchy

1. **Insulation system selection** — specify low-chloride, low-leachable-ion content insulation (verified via leachate testing per the standards-cited limits); choose hydrophobic chemistries that do not retain water; specify removable jacketing at known wet-zone bands so future inspections do not require destructive stripping.
2. **Sealing, caulking, and drainage** — proper jacket overlap orientation (shed water downward), sealant at every penetration (instrument tap, hanger, support, tee, valve), drainage holes at the lowest point of every jacketed run so that any ingress water exits rather than ponding.
3. **CUI-specific coatings** — **TSA (thermal-sprayed aluminum)** is the workhorse for high-temperature CUI service on carbon steel and provides cathodic protection of the steel beneath holidays; **immersion-grade epoxies** and **inorganic copolymer / silicone hybrids** cover the moderate-temperature band; coating selection is governed by the operating-T-vs-coating-class matrix in the relevant CUI-specific RP.
4. **Targeted insulation removal** — when a service does not need insulation for personnel protection, energy conservation, or process control, **removing it** is the cheapest CUI mitigation. Tropical-climate cold-service equipment in particular often gets less benefit from insulation than the CUI risk it creates.
5. **CUI-specific RBI** — use the CUI damage factor in [api-rp-581](../standards/api-rp-581.md) and (where applicable) the CUI-specific RP guidance to drive inspection-interval and inspection-effectiveness decisions, rather than a generic external-corrosion treatment.

## Standards

- **[api-rp-571](../standards/api-rp-571.md)** — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry*. CUI sits in §4 (loss-of-thickness mechanisms); CISCC-CUI is cross-referenced from §5 environmentally-assisted cracking. Primary mechanism-catalogue source for this page.
- **[api-rp-581](../standards/api-rp-581.md)** — RBI quantitative methodology; provides the CUI damage factor, inspection-effectiveness categories, and POF combination rules.
- **[api-510](../standards/api-510.md)** — Pressure Vessel Inspection Code; consumer of CUI screening output for vessel inspection planning.
- **[api-570](../standards/api-570.md)** — Piping Inspection Code; consumer of CUI screening output for piping inspection planning.
- **[api-rp-574](../standards/api-rp-574.md)** — Inspection Practices for Piping System Components; selects the inspection technique applied to a CUI-credible circuit.
- **API RP 583** — *Corrosion Under Insulation and Fireproofing* (the API-specialized standard for CUI). **Future-promotion candidate** — page not yet in this wiki; track for ingest with the next API-RP batch.
- **NACE / AMPP SP0198** — *Control of Corrosion Under Thermal Insulation and Fireproofing Materials*. **Future-promotion candidate** — page not yet in this wiki; complementary AMPP guidance.

## Related concepts

- [[damage-mechanism-screening]] — CUI is one of the loss-of-thickness mechanisms enumerated upstream.
- [[corrosion-rate-measurement]] — CUI rate ranges and CML strategy interpretation.
- [[pitting-and-crevice-corrosion]] — overlaps with CISCC-CUI on the chloride-pitting / chloride-cracking continuum on austenitic stainless steel.
- [[risk-based-inspection]] — consumer of the CUI damage factor and the CUI inspection-effectiveness table.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — API standards summary that anchors the API RP 571 / 574 / 580 / 581 / 510 / 570 references on this page.
