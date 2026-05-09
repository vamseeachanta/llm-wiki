---
title: "Engineering Critical Assessment (ECA)"
slug: engineering-critical-assessment
tags:
  - eca
  - fracture-mechanics
  - weld-acceptance
  - fitness-for-service
  - alternative-acceptance
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/bs-7910-flaw-assessment.md
  - standards/api-std-579.md
  - standards/api-std-1104.md
---

# Engineering Critical Assessment (ECA)

> Concept page. Definitional and link-rich; load-bearing technical detail (clause text, FAD curves, residual-stress profiles, partial safety factors, Paris-law constants) lives on the standards pages this concept routes into. No clause text, formulas, or figures are reproduced here.

## What is ECA?

**Engineering Critical Assessment (ECA)** is a fracture-mechanics + fatigue-mechanics analysis used to derive **alternative weld-acceptance criteria** when standard workmanship limits would unnecessarily reject flaws not actually consequential to structural integrity. ECA accepts a flaw if it can be demonstrated to remain stable under all design loads plus cyclic loading over the design life, with margin against unstable fracture and plastic collapse on the [Failure Assessment Diagram (FAD)](../standards/bs-7910-flaw-assessment.md) and against fatigue-driven crack growth from the as-found size to a critical size.

ECA is not a license to ship bad welds. It is the disciplined route — calibrated by upstream WPS-qualification toughness data, controlled flaw sizing (typically AUT/PAUT), and explicit residual-stress accounting — by which a fabricator or operator can accept a flaw that fails workmanship while still demonstrating that the structure meets its design life with margin. The relationship to [[welding-procedures-and-acceptance]] is structural: workmanship is the default; ECA is the sanctioned escalation when workmanship would force costly or metallurgically risky repair.

## When ECA replaces workmanship

| Scenario | Drives ECA |
|---|---|
| Pipeline girth welds (large-diameter, large flaw rate) | [[api-std-1104]] Annex A — saves repair costs at production rates |
| Offshore welded jacket nodes (very large flaws, complex geometry) | [[dnv-st-f101]] + DNV-RP-F108 (offshore pipeline ECA) |
| In-service flaws (FFS) | [[api-std-579]] + [[bs-7910-flaw-assessment]] |
| Aerospace and nuclear damage tolerance | Dedicated ECA programmes (outside this wiki's scope) |

The common driver is that workmanship rejection imposes a cost (repair, re-NDE, schedule, hydrogen-cracking exposure on reheat, distortion) that exceeds the engineering risk of the as-found flaw, and the operator has the toughness data and stress envelope to demonstrate the latter quantitatively.

## Inputs

ECA stands or falls on the quality of its inputs. The five input families:

- **Accurate flaw characterisation.** Length, height, depth-from-surface, ligament, orientation. Modern pipeline ECA depends on **Automated Ultrasonic Testing (AUT)** rather than radiography because AUT provides direct height sizing that radiography cannot. Sizing tolerances are themselves an explicit input — the assessment is performed on the upper-bound sized flaw, not the nominal.
- **Material toughness.** Either Charpy-V-notch screening with a published correlation to CTOD/J (conservative, screening-grade), or **direct CTOD or J-integral** test results per [ASTM E1820](../standards/astm-e1820.md), BS 7448, or ISO 12135 on weld metal and HAZ at the lowest service temperature. ECA-grade toughness data must be available from the WPS qualification — an ECA cannot rescue a procedure that did not test for CTOD in the first place. See [[fracture-toughness-measurement]].
- **Residual stresses.** As-welded residual stresses approach parent yield; PWHT reduces but does not eliminate them. The FAD ordinate sums primary plus residual stress, and code-published residual-stress profiles (membrane plus bending) are the normative input. Mixing residual-stress profiles between codes is **not permitted**.
- **Applied stresses.** Static (axial, bending, internal pressure), dynamic (waves, vortex shedding, transients), and cyclic (operating cycles, installation cycles, shutdown / startup). For pipeline strain-based design, the input is plastic strain rather than stress.
- **Environmental factors.** Sour service ([[iso-15156]]), seawater + cathodic protection, temperature regime (Arctic, cryogenic). These modify both toughness (via hydrogen embrittlement / HE) and crack-growth rate.

## Outputs

ECA produces an **acceptance criterion** for a population of flaws found in production welds. Typically expressed as

`flaw_height ≤ allowable_height(flaw_length, applied_stress, toughness, residual_stress, fatigue_design_life)`

and tabulated as a **flaw-acceptance matrix** spanning height × length × position-on-weld (cap, root, fill, sidewall). Production NDE then sizes each flaw and looks it up in the matrix; flaws inside the matrix are accepted, flaws outside are repaired or rejected. The matrix is the operator's contractual artefact and travels with the WPS / PQR / weld-map records.

Secondary outputs include the underlying assessment file (FAD plot, FCG integration, sensitivity study), the partial-safety-factor justification, and the residual-stress profile used.

## Two-tier methodology

Most ECA standards offer multiple levels, sized to the rigour of input data and the conservatism the operator can absorb:

| Level | Method | Conservatism |
|---|---|---|
| Level 1 | Simplified screening (BS 7910 Level 1 / API 579 Level 1) | Highest |
| Level 2 | Standard FAD (BS 7910 2A/2B / API 579 Level 2) | Moderate |
| Level 3 | Advanced (J-integral analysis, ductile-tearing, R-curve, constraint correction) | Lowest |

Level 1 is screening-grade — pass means accept, fail means escalate. Level 2 is where most field assessments sit; it uses tabulated FAD curves with code-specific calibration of the toughness option (`Option 1`/`2`/`3` in BS 7910, equivalent in API 579 Part 9). Level 3 is reserved for high-consequence or marginal-Level-2 cases and unlocks ductile tearing on the J-R curve, plus T-stress / Q-parameter constraint correction. Assessment-rigour cost rises sharply between levels — Level 3 is days-to-weeks of senior fracture-mechanics engineering.

## ECA + fatigue

For components subject to cyclic loading (pipelines under operating-pressure cycles, risers under wave loading, offshore jackets under sea-state, drilling risers under VIV), the ECA workflow integrates a fatigue-crack-growth (FCG) law:

1. **Initial flaw** — as-found size from AUT, upper-bound on sizing tolerance.
2. **Crack-growth law** — Paris equation `da/dN = C·(ΔK)^m` with `C`, `m` from [ASTM E647](../standards/astm-e647.md) testing or published bands; threshold `ΔK_th` and environmental modifiers as appropriate.
3. **Final flaw** — integrated forward over the design cycle count.
4. **Stability check** — final flaw plotted on the FAD; must remain inside the curve with margin.
5. **Remaining cycles** — derived from the integration; safety factor on life applied per the governing standard.

For pipelines installed by **reeling** (large-diameter rigid pipe spooled onto an installation vessel) or operating in **high-strain environments** (Arctic frost-heave, route-buckling), **strain-based ECA** replaces stress-based ECA. The driving variable is plastic strain rather than primary stress; the FAD is reformulated; CTOD-R curves and tearing-resistance curves become primary inputs. See [[fatigue-design-and-assessment]] for the broader fatigue-paradigm framing.

## Sour-service ECA

Wet H₂S service introduces hydrogen embrittlement (HE), which both **lowers toughness** (HE-affected CTOD can be a fraction of in-air CTOD) and **enhances crack-growth rate** (often 10–100× the in-air Paris-law `C`). FFS literature ([[api-std-579]] Part 9 and BS 7910 Annex K) provides envelopes for HE-affected toughness; environmental crack-growth-rate enhancement is captured by H₂S-service-specific Paris constants from [ASTM E647](../standards/astm-e647.md) testing in the actual fluid + partial pressure of interest. Hardness control in the HAZ (cap typically 250 HV per [[iso-15156]] and [[api-std-1104]] Annex A) is the upstream procedural mitigation; ECA is the downstream verification that the qualified HAZ remains tolerable for the actual flaw population. See [[sour-service-materials]].

## Standards

Bidirectional links — each of the standards pages below references this concept page in turn:

- [[bs-7910-flaw-assessment]] — primary UK / international ECA standard. Full FAD methodology, Annex A (FAD), Annex K (residual stress), Annex M (fatigue), Annex T (LBB). The detailed methodology referenced normatively from [[api-std-1104]] Annex A.
- [[api-std-579]] — FFS / ECA US sibling (API 579-1 / ASME FFS-1). Crack-like flaws covered in Part 9; the in-service framing is described under [[fitness-for-service]].
- [[api-std-1104]] — pipeline girth-weld ECA via Annex A. The North-American hook for new-construction and tie-in welds; cites BS 7910 for the underlying methodology.
- [[astm-e1820]] — CTOD / J-integral test method; produces the toughness inputs feeding ECA Level 2 / 3.
- [[astm-e647]] — fatigue-crack-growth-rate test method; produces the Paris-law constants feeding the ECA fatigue integration.
- [[dnv-st-f101]] — offshore-pipeline ECA. DNV-ST-F101 (with DNV-RP-F108) provides the offshore pipeline construction-and-operation framing; strain-based ECA for reeled installation and high-strain routes.

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [[fitness-for-service]] — the in-service framing; this concept page is the new-build / construction-time counterpart, and the two share the FAD methodology.
- [[welding-procedures-and-acceptance]] — workmanship is the default, ECA the sanctioned escalation; the upstream WPS qualification must include CTOD / J for ECA to be available.
- [[fracture-toughness-measurement]] — `K_Ic`, `J_Ic`, CTOD, `T₀`; the test methods that produce the toughness inputs feeding ECA.
- [[fatigue-design-and-assessment]] — S-N (BS 7608, DNV-RP-C203) and Paris-law FCG; the broader fatigue-paradigm framing into which ECA's fatigue-integration step fits.
- [[brittle-fracture]] — low-temperature, low-toughness failure mode that the FAD's K_r axis and the Master Curve `T₀` shift are designed to screen against.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog reference for the API 579 family and API 1104 (Annex A ECA).
- [og-standards-bsi](../sources/og-standards-bsi.md) — catalog reference for BS 7910 and the BS 7448 toughness-test family.
- [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md) — catalog reference for ASTM E1820 (CTOD / J), E647 (FCG), E399 (`K_Ic`), and E1921 (Master Curve `T₀`).

## Notes

- This is a concept page, not a standards page. No clause text, FAD curves, residual-stress profiles, partial-safety-factor tables, or Paris-law constants are reproduced here. For normative use, cite the publisher edition of the relevant standard directly.
- ECA outputs (acceptance matrices, FAD plots, FCG integration files) are operator deliverables. This wiki does not host project-specific ECA artefacts; those live with the operator's engineering-management system.
- Per the [calc citation contract](../../../../../.claude/rules/calc-citation-contract.md), any calc module that consumes an ECA-derived constant (FAD curve coefficients, residual-stress-profile coefficients, Paris-law `C` / `m`, partial safety factors) must emit a `Citation` instance pinning `code_id=bs-7910-flaw-assessment`, `api-std-579`, `api-std-1104`, `astm-e1820`, or `astm-e647` with the specific revision.
