---
title: "Fitness-for-Service (FFS)"
slug: fitness-for-service
tags:
  - ffs
  - integrity-management
  - damage-mechanisms
  - fad
  - fracture-mechanics
  - in-service-inspection
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-std-579.md
  - standards/bs-7910-flaw-assessment.md
---

# Fitness-for-Service (FFS)

> First concept page in this wiki — establishes the concept-page convention by example. Concepts here are short, definitional, and link-rich; load-bearing technical detail lives on the standards pages this concept routes into.

## What is FFS?

**Fitness-for-Service (FFS)** is a quantitative engineering analysis applied to in-service equipment (pressure vessels, piping, tankage, pipelines, structural components) that contains detected damage, flaws, or out-of-tolerance geometry, in order to determine whether the equipment remains fit for continued operation under its design and operating loads. FFS produces a defensible run / repair / replace / re-rate / re-inspect decision, typically expressed as a remaining-strength factor (RSF), a remaining-life estimate, or an acceptance verdict against an assessment criterion.

FFS differs in posture from new-build design. New-build design starts from a clean geometry and applies code-prescribed safety factors against postulated loads. FFS starts from the **actual measured damage state** — wall-thickness profiles, crack dimensions, dent depths, blister maps, distortion measurements — and the **actual applied loads**, then evaluates the as-found component using fracture mechanics, limit-state analysis, or screening rules calibrated for that damage mechanism. Because the geometry is no longer the as-designed geometry, FFS accepts narrower margins than new-build codes, in exchange for richer input data and tighter assessment rigour.

## When FFS applies

- **Post-inspection findings.** When in-service inspection (visual, UT thickness, MFL, ILI, EMAT, RT, PAUT, ACFM, dye-pen, MPI) detects corrosion, pitting, blisters, dents, cracks, weld defects, or distortion exceeding the inspection-code acceptance threshold, FFS is the route to disposition the finding without immediate repair.
- **Code-gated invocation.** The in-service inspection codes — **API 510** (pressure vessels), **API 570** (process piping), **API 653** (atmospheric storage tanks) — explicitly delegate to [[api-std-579]] / [[bs-7910-flaw-assessment]] when an out-of-code condition is found. FFS is not a free-standing decision; it is invoked under the authority of an inspection code.
- **Life-extension assessment.** When operators seek to extend service life of ageing assets (refineries, offshore platforms, pipelines) past original design life, FFS quantifies remaining life from the current damage state plus a projected damage-progression model (corrosion rate, fatigue-cycle accumulation, creep-strain accumulation).
- **Run-or-repair decisions.** During planned shutdowns, FFS supports go/no-go calls on whether a flaw warrants immediate repair, can be deferred to the next turnaround under a monitoring regime, or can be left in service indefinitely.
- **Re-rating.** When operating envelope changes (pressure, temperature, fluid composition), FFS evaluates whether existing damaged components are acceptable under the revised loads.

## Damage mechanisms covered

The FFS standards organise their methods by damage-mechanism family. The table below maps damage mechanisms onto the part / annex structure of the two dominant codes, [[api-std-579]] and [[bs-7910-flaw-assessment]].

| Damage mechanism | API 579-1 / ASME FFS-1 part | BS 7910 (2013) annex / clause |
|---|---|---|
| Brittle fracture (low-temp, low-toughness) | Part 3 | FAD framework, Annex A; toughness inputs from BS 7448 |
| General metal loss (uniform thinning) | Part 4 | Not in primary scope (volumetric flaws treated by analogy) |
| Local metal loss (LTAs, grooves) | Part 5 | Not in primary scope |
| Pitting corrosion | Part 6 | Not in primary scope |
| Hydrogen blisters, HIC, SOHIC, laminations | Part 7 | Not in primary scope |
| Weld misalignment, shell distortion, out-of-roundness | Part 8 | Stress-magnification factors feed FAD primary stress |
| Crack-like flaws (planar) | Part 9 | Annex A (FAD), Annex K (residual stress), Annex M (fatigue), Annex T (LBB) |
| Creep damage and creep-fatigue | Part 10 | Annex J (creep crack growth) |
| Fire damage (post-event metallurgical) | Part 11 | Not in primary scope |
| Dents, gouges, dent-gouge combinations | Part 12 | Not in primary scope (pipeline FFS via DNV-RP-F101 / API 1104 ECA) |

> Cells marked "Not in primary scope" indicate that BS 7910 deliberately concentrates on crack-like flaws and fatigue/creep growth; the broader FFS suite (corrosion, pitting, blisters, fire, dents) is API 579-1 / ASME FFS-1 territory. Practitioners typically use both codes in tandem for a mixed-damage assessment.

## Methodological backbone

FFS standards share a tiered-assessment philosophy, sized to the rigour of input data available and the severity of the consequence of error.

- **Level 1 — Conservative screening.** Tabulated acceptance criteria, charts, look-up curves. Suitable for inspector-grade evaluation with limited input data. Pass at Level 1 means accept; fail at Level 1 means escalate to Level 2.
- **Level 2 — Detailed engineering analysis.** Closed-form or simplified numerical methods (reference-stress, beam-on-elastic-foundation, plate-with-flaw stress intensity factor catalogues). Most field assessments stop here. Requires engineering judgement and validated input data.
- **Level 3 — Advanced analysis.** Detailed FEA, elastic-plastic fracture mechanics (J-integral, R-curve, ductile-tearing), constraint correction, probabilistic / Monte Carlo treatment. Reserved for high-consequence components, marginal Level 2 results, or novel geometries outside the catalogues.

The shared analytical core for crack-like flaws is the **Failure Assessment Diagram (FAD)** — a two-criterion plot with K<sub>r</sub> (toughness ratio, ordinate) versus L<sub>r</sub> (load ratio, abscissa). Points inside the FAD curve are acceptable; points outside indicate unstable fracture (high K<sub>r</sub>) or plastic collapse (high L<sub>r</sub>) or interaction. Both [[api-std-579]] Part 9 and [[bs-7910-flaw-assessment]] Annex A use the FAD, with code-specific calibration of the curve and option-numbering of the toughness inputs.

**Residual stress** treatment is a load-bearing input. Welded components carry as-welded residual stresses up to the parent-material yield; post-weld heat treatment (PWHT) reduces but does not eliminate them. Both codes provide tabulated residual-stress profiles (membrane plus bending) for common weld geometries; these are summed with primary stress in the FAD ordinate. Mixing residual-stress profiles between codes is **not permitted** — each code's profiles are internally calibrated against its own FAD.

**Partial safety factors** (PSFs) are applied to load, toughness, flaw size, and material-strength inputs to account for measurement uncertainty. BS 7910 Annex N provides probabilistic / FORM-SORM frameworks; API 579-1 provides PSF tables in Part 9 and aligns with API RP 581 risk-based inspection inputs.

## Standards

- [[api-std-579]] — **API 579-1 / ASME FFS-1**, the joint API + ASME consensus standard. Full FFS suite covering brittle fracture (Pt 3), general / local thinning (Pt 4–5), pitting (Pt 6), blisters (Pt 7), distortion (Pt 8), crack-like flaws (Pt 9), creep (Pt 10), fire (Pt 11), dents/gouges (Pt 12). US-led, refining/petrochem industry default.
- [[bs-7910-flaw-assessment]] — **BS 7910:2013+A1:2015**, BSI's parallel UK guide. Concentrates on crack-like flaws, fatigue crack growth, leak-before-break, creep crack growth. Offshore O&G and EU/UK fabrication default. Methodologically aligned with API 579-1 but with BS-specific FAD calibration and residual-stress profiles.
- [[asme-bpvc-viii-1]] — **ASME BPVC Section VIII Division 1**, design-by-rule pressure-vessel construction code. Reference for new-build design margins; FFS critical-flaw-size assessments benchmark against the original design's allowable-stress envelope.
- [[asme-bpvc-viii-2]] — **ASME BPVC Section VIII Division 2**, design-by-analysis alternative-rules construction code. The stress-classification and linearisation conventions used in FFS Annexes (membrane / bending / peak decomposition; primary / secondary / peak categorisation) are inherited from VIII-2.

Bidirectional: each of those standards pages should cross-link back to this concept page once the convention propagates.

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [[fracture-toughness-measurement]] — K<sub>Ic</sub>, J<sub>Ic</sub>, CTOD, T<sub>0</sub> (Master Curve); the test methods (ASTM E399 / E1820 / E1921, BS 7448) that produce the toughness inputs feeding FFS Level 2/3 crack assessments.
- [[fatigue-design]] — S-N (BS 7608, DNV-RP-C203), Paris-law crack-growth integration, mean-stress and environmental modifiers; FFS fatigue assessments integrate forward in time from a known initial flaw.
- [[weld-acceptance]] — workmanship acceptance criteria (AWS D1.1, API 1104, ISO 5817) versus fitness-for-purpose (ECA via BS 7910 Annex A or API 1104 Annex A); FFS is the escalation path when a flaw fails workmanship but may pass fitness-for-purpose.
- [[ductile-tearing]] — J-R curve behaviour, tearing instability, constraint effects; basis for FFS Level 3 advanced assessments and the ductile-fracture branch of the FAD.

## Source materials

- [[og-standards-api]](../sources/og-standards-api.md) — catalog reference for the API 579 family, including the joint API/ASME FFS-1 numbering and edition history.

## Notes

- This is a concept page, not a standards page. No clause text, formulas, FAD curves, or tabulated data are reproduced here. For normative use, cite the publisher edition of the relevant standard directly.
- The FFS workflow is gated upstream by the in-service inspection codes (API 510 / 570 / 653); a standalone FFS calculation without a documented inspection finding is not a sanctioned engineering deliverable.
- Pipeline FFS for corrosion-only damage typically routes through [[dnv-rp-f101]] (Corroded Pipelines) rather than the general API 579-1 Part 5; pipeline ECA for crack-like flaws routes through [[api-std-1104]] Annex A or BS 7910 Annex A.
