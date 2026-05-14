---
title: "Casing Program Design"
tags: [casing, well-design, collapse-design, burst-design, tension-design, triaxial, biaxial, lubinski]
sources:
  - api-spec-5ct
  - api-rp-5c5
  - api-rp-5c1
added: 2026-05-13
last_updated: 2026-05-13
---

# Casing Program Design

## Scope

Engineering design of the casing program for a well — selecting the number of casing strings (conductor → surface → intermediate → production → liner), the setting depth of each, the grade, weight, and connection of each string, and verifying that each string meets the four design-load criteria (collapse, burst, tension, triaxial) with adequate design factors. This is the load-bearing well-design concept that ties casing-spec inputs to safety-of-well outputs.

## Casing-string sequence

- **Conductor** — typically 30" or 36", driven or jetted; isolates surface unconsolidated formations.
- **Surface** — typically 13⅜" or 20"; isolates shallow freshwater aquifers, anchors BOP stack.
- **Intermediate** — one or more strings (e.g., 9⅝", 11¾"); isolates problem formations (lost-circulation zones, sloughing shales, salt sections).
- **Production** — typically 7" or 5½"; isolates the producing zone, hosts the production tubing.
- **Liner** — partial-length casing run from the previous shoe to TD; alternative to a full production string.

## Four design loads

1. **Collapse** — external pressure tries to crush the casing inward. Worst case typically during lost-circulation event where mud column drops below the casing-shoe pressure.
2. **Burst** — internal pressure tries to split the casing outward. Worst case during well-control kick scenarios with full reservoir gas to surface (gas-to-surface or BHP-1-EPP design).
3. **Tension** — weight of the casing string in air + buoyant weight + setting overpull + cementing differential pressure forces.
4. **Triaxial (von Mises)** — combined-load envelope. Casing in a triaxial state can fail at loads below individual collapse / burst / tension limits.

## Biaxial reduction (Lubinski ellipse / API ellipse)

Tension reduces collapse capacity and increases burst capacity; compression does the inverse. The API ellipse (in API Bul 5C3 historically, now in 5C5 / textbook restatements) plots the biaxial reduction. Casing checked at high tension near surface may fail collapse at depths where it would otherwise pass.

## Design-factor convention

Typical operator design factors (not API-mandated thresholds; operator-specified):

- Collapse: 1.0 to 1.125
- Burst: 1.1 to 1.25
- Tension: 1.4 to 1.8 (highest because tension failures are catastrophic)
- Triaxial: 1.25 to 1.4

## Selection workflow

1. **Setting depths first** — driven by formation pressures, lost-circulation zones, salt sections, kick tolerance.
2. **Worst-case loads second** — for each string, evaluate the worst credible collapse, burst, tension scenario.
3. **Grade-and-weight selection** — pick the lightest, cheapest combination meeting design factors at every depth point. Often "tapered" strings with heavier sections at the top (high tension) and lighter sections near the shoe (low tension, moderate burst).
4. **Connection selection** — API for routine, premium for high-pressure or gas-tight requirements.
5. **PSL specification** — PSL-2 or PSL-3 for sour service, HPHT, or critical wells.

## Public references

- **Bourgoyne, Chenevert, Millheim, Young** — *Applied Drilling Engineering*, SPE Textbook Series Vol. 2, 1986 (ISBN 1-55563-001-4). Chapter 7 casing design.
- **Mitchell & Miska** — *Fundamentals of Drilling Engineering*, SPE 2011 (ISBN 978-1-55563-207-6). Tubular design chapter.
- **Lyons (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Casing-design section.
- **API Spec 5CT** 10th Edition (identical adoption of ISO 11960) — see [api-spec-5ct.md](../standards/api-spec-5ct.md).

## Cross-references

- [Casing Grades and PSL](casing-grades-and-psl.md) — grade families and PSL framework
- [Casing Shoe Track](casing-shoe-track.md) — shoe / float-collar geometry and cement-bond design boundary
- [API Spec 5CT](../standards/api-spec-5ct.md), [API RP 5C5](../standards/api-rp-5c5.md), [API RP 5C1](../standards/api-rp-5c1.md)
- Downstream consumer: [vamseeachanta/workspace-hub#1958](https://github.com/vamseeachanta/workspace-hub/issues/1958) — slim-hole well-engineering calc module (casing-program comparison + economics) — this concept page is the design-rationale anchor that module's outputs should cite
- Founding source: [Papkov (2026)](../sources/papkov-2026-drilling-tender-ai-agent.md) — AI-tender-evaluation downstream consumer
