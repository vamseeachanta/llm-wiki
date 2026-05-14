---
title: "Casing Shoe Track"
tags: [casing, shoe, float-collar, float-shoe, centralizer, cementing, formation-integrity-test]
sources:
  - api-rp-5c1
added: 2026-05-13
last_updated: 2026-05-13
---

# Casing Shoe Track

## Scope

The lower-end assembly of a casing string — guide shoe (or float shoe), float collar, centralizers in the cemented interval — and the operational concepts (formation integrity test, leakoff test) that derive from successful shoe-and-cement placement. The shoe track is where casing design hands off to cementing design.

## Components

- **Guide shoe / float shoe** — bullnose-profiled lower end that helps the casing string steer past ledges as it runs to bottom. A *float* shoe adds an internal check valve that prevents fluid backflow from the annulus into the casing during running and cementing.
- **Float collar** — second check-valve assembly typically one or two joints above the shoe. Catches the cement-job wiper plug; provides backup if the shoe valve fails.
- **Landing collar** — for liners; the polished receptacle that lands and seats the liner-top packer.
- **Centralizers** — bow-spring or rigid; spaced along the cemented interval to keep casing concentric in the open hole so the cement column has uniform thickness.

## Cementing-design coupling

The shoe-track length (typically 60-120 ft from shoe up to float collar) is the volume of cement that stays below the float collar after the cement job — it is **shoe-track cement**, treated as a sacrificial volume. After cementing:

1. Wait-on-cement (WOC) per the cement-design spec.
2. Drill out the cement above the float collar.
3. Drill through the float collar and shoe-track cement.
4. **Formation integrity test (FIT)** or **leakoff test (LOT)** at the new shoe to verify cement integrity and establish the formation-strength upper bound for kick-tolerance calculations on the next hole section.

## Pressure-test framework

- **FIT** — pressure-test to a predetermined value (the next-section design pressure) and stop. Confirms the shoe will not leak at that pressure but doesn't establish the failure pressure.
- **LOT** — increase pressure until a non-linear inflection appears on the pressure-volume curve (the leakoff point). Establishes the actual formation strength as an equivalent mud weight.
- **XLOT (extended LOT)** — push past leakoff to find the formation breakdown pressure. Used when fracture-gradient is critical to the next-section drilling plan.

## Public references

- **Bourgoyne et al.** Chapter 7 (casing) and Chapter 13 (cementing) — shoe-track design integration
- **Mitchell & Miska** — tubular design + cementing chapters
- **API Spec 10A** + **API RP 10B** — cementing standards (Phase 2 ingest target; see [llm-wiki#49](https://github.com/vamseeachanta/llm-wiki/issues/49) Phase 2 deferred list)

## Cross-references

- [Casing Program Design](casing-program-design.md) — design-load integration
- [Casing Grades and PSL](casing-grades-and-psl.md)
- [API RP 5C1](../standards/api-rp-5c1.md)
