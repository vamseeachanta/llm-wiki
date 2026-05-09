---
title: "Welding Procedures, Qualification, and Acceptance"
slug: welding-procedures-and-acceptance
tags:
  - welding
  - wps
  - pqr
  - weld-acceptance
  - ndt
  - eca
  - pipeline-welding
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/api-std-1104.md
  - standards/asme-bpvc-ix.md
  - standards/aws-d1-1.md
---

# Welding Procedures, Qualification, and Acceptance

> Concept page. Definitional and link-rich; load-bearing technical detail (clauses, tables, equations) lives on the standards pages this concept routes into. No clause text, formulas, or figures are reproduced here.

## What this concept covers

A weld delivered to a pressure-containing or load-bearing service is the joint product of three artefacts: a written **procedure** (WPS) that the welder will follow, **evidence** that the procedure produces sound metal (PQR + welder/operator performance qualification), and **acceptance** of the finished production weld against either prescriptive workmanship limits or a fitness-for-purpose engineering critical assessment. This page maps that pipeline across the three governing-standard families and routes into each one.

## The qualification pyramid

The shared structure across welding codes is a three-tier qualification pyramid:

- **Welding Procedure Specification (WPS).** A written document describing the joint geometry, base material, filler metal, electrical and process parameters, preheat / interpass / post-weld heat treatment (PWHT), position, and shielding. The WPS is what the welder actually follows on the shop or field floor. It defines the *envelope of allowed parameters* — minimum / maximum heat input, allowed stickout, allowed travel-speed window, and so on.
- **Procedure Qualification Record (PQR).** The destructive-test evidence that *one specific weld coupon*, made within the WPS envelope, produced metal that meets the standard's mechanical-property acceptance. The PQR captures the actual variables used (not the allowed ranges), the test specimens removed, and their results — tensile, bend, nick-break, hardness, Charpy, macro-etch as required. A WPS without a supporting PQR is a draft, not a qualified procedure.
- **Welder / Welding-Operator Performance Qualification (WPQ / WOPQ).** Evidence that *a specific welder* (or mechanised-welding-equipment operator) can apply the WPS and produce sound metal. Tested by destructive coupons (bend, nick-break) or by NDE of a production weld. WPQs expire on a periodic schedule and on lapse of practice; the operator must requalify.

Variables in a WPS are categorised by the governing standard:

| Variable class | Effect of change | Action required |
|---|---|---|
| **Essential** | Materially changes weld mechanical properties | New PQR (procedure requalification) |
| **Supplementary essential** | Affects notch toughness when toughness is in scope | New PQR if toughness testing is required |
| **Nonessential** | Documentation / convenience parameters | WPS revision, no requalification |

Each governing standard publishes its own **enumerated list** of which variable falls into which class — the lists differ between [[asme-bpvc-ix]], [[api-std-1104]], and [[aws-d1-1]], so a WPS qualified to one code is *not* automatically valid under another. Cross-code dual-qualification is common at facility-pipeline interfaces (compressor stations, pump stations) and is an explicit operator deliverable.

## Three governing-standard families

Welding qualification in the western codes splits cleanly into three application families, each with its own code home:

| Application | Standard | Notes |
|---|---|---|
| Pressure vessels & process piping | [[asme-bpvc-ix]] (with B31.x construction codes) | Most exhaustive variable lists; PQR + WPQ explicit; toughness via supplementary-essential variables when required by construction code. |
| Pipelines (cross-country transmission, gathering, distribution) | [[api-std-1104]] | Mechanical-test driven (tensile, nick-break, bend); less prescriptive on supplementary-essential variables; ECA route via Annex A. |
| Structural (bridges, buildings, fixed offshore jackets) | [[aws-d1-1]] (carbon/low-alloy steel), AWS D1.2 (aluminium), AWS D1.5 (bridges) | **Pre-qualified WPS option** for many common joints — qualification by reference instead of by coupon test. |

Filler-metal classification is itself a substantial subsystem and is summarised in [[aws-filler-metal-overview]]; the AWS A5.x specifications are referenced normatively from all three families above.

## Mechanical qualification tests

Qualification coupons are destructively tested. The test menu and specimen geometry are typically called out in the welding code with the *test method* delegated to ASTM:

- **Cross-weld tensile (transverse).** The coupon must break in the parent material, or in the weld at or above the parent material's specified minimum tensile strength. Specimen prep per [[astm-a370]].
- **Bend tests (face / root / side).** Guided-bend specimens are bent around a mandrel; acceptance is on the maximum allowable open-defect length on the convex face after bending. API 1104 sets a 1/8 in (3.2 mm) crack limit; ASME BPVC IX sets its own equivalent. Side-bend is used in lieu of face/root for thicker material.
- **Nick-break.** A notched specimen broken open to expose the weld cross-section; acceptance on aggregate area of porosity, slag, and incomplete fusion visible on the fracture surface.
- **Macro-etch.** A polished and etched cross-section examined for incomplete penetration, incomplete fusion, slag, and crack indications. Required for fillet welds and for some groove-weld configurations.
- **Hardness survey.** Vickers HV<sub>10</sub> traverse across parent / HAZ / weld metal; acceptance limits depend on service. Sour service (see below) caps HAZ hardness at 250 HV (API 1104 Annex A / ISO 15156).
- **Charpy V-notch (CVN) impact.** Notch-toughness screening at the lowest service temperature; subsize specimens (5 mm, 7.5 mm) are common for pipe wall thicknesses below the standard 10 mm. Method per [[astm-a370]] / ASTM E23.
- **CTOD / J-integral.** Fracture-mechanics toughness inputs for engineering-critical-assessment work; required when ECA acceptance is invoked. Method per ASTM E1820, BS 7448, or ISO 12135. See [[fracture-toughness-measurement]].

Most welding codes call ASTM A370 / E8 / E23 by reference for *how* to make and test the specimens, while reserving the *acceptance limit* to the welding code itself.

## NDE acceptance criteria

Production welds are examined non-destructively after completion. The NDE menu and acceptance limits depend on application and code:

- **Visual examination (VT).** Universal — every weld; no equipment required beyond gauges and adequate lighting. Catches surface profile, undercut, overlap, and gross defects.
- **Radiography (RT).** Film or digital radiography; the historical baseline for girth-weld pipeline NDE and for pressure-vessel longitudinal seams. Acceptance on discontinuity class — porosity (rounded indication), slag (linear indication), incomplete penetration, incomplete fusion, cracks, undercut, burn-through — keyed to length, aggregate length per weld length, and depth.
- **Ultrasonic testing (UT).** Manual pulse-echo for spot examination; **Automated UT (AUT)** for mechanised pipeline girth welds at production rates. AUT replaces RT on most modern pipeline projects because it is faster, has sub-surface depth resolution that RT lacks, and supports direct ECA flaw-sizing. Acceptance windows differ from RT; codes publish them separately.
- **Magnetic particle (MT).** Surface and slightly-sub-surface flaws on ferromagnetic materials; standard for fillet-weld and structural-weld examination on carbon and low-alloy steel.
- **Liquid penetrant (PT).** Surface flaws on any material; the only convenient NDE for austenitic stainless and aluminium when MT is unavailable.

Acceptance is published in two flavours:

- **Workmanship-based acceptance.** Empirically calibrated limits on flaw length and aggregate length, derived from a long history of fabricator experience and conservative against assumed loading. Default in AWS D1.1, API 1104 Section 9, ASME BPVC IX. Pass / fail is fast, traceable, and inspector-grade.
- **Fitness-for-service acceptance.** Custom limits derived from a fracture-mechanics analysis of the actual flaw, the actual applied stress (including residual), and the actual material toughness. See ECA below.

## Engineering Critical Assessment (ECA)

When a flaw fails workmanship-based acceptance but is not actually structurally consequential, repair is wasteful and itself introduces metallurgical risk (HAZ reheats, hydrogen-cracking exposure, distortion). **Engineering Critical Assessment (ECA)** is the sanctioned escalation path: derive custom acceptance criteria from a documented fracture-mechanics assessment and accept the as-found flaw without repair.

The standard ECA workflow:

1. **Flaw characterisation.** AUT or PAUT sizing of length, height, depth-from-surface, ligament, and orientation. Sizing tolerances are an explicit input to the assessment.
2. **Fracture-toughness data.** CTOD or J-integral test results at the lowest service temperature, on weld metal and HAZ, from the qualified WPS. See [[fracture-toughness-measurement]].
3. **Stress analysis.** Primary stress (axial, bending, internal pressure), secondary stress (thermal, displacement-controlled), residual stress (as-welded or post-PWHT) — summed per the chosen code's residual-stress profile.
4. **FAD assessment.** Plot the flaw on the Failure Assessment Diagram in K<sub>r</sub> – L<sub>r</sub> space; flaws inside the curve are acceptable, outside are not. Methodology shared with [[fitness-for-service]].
5. **Run / repair decision.** Document acceptance with operator and certifying-authority sign-off; or repair and re-NDE.

Code routes:

- **Pipeline girth welds — [[api-std-1104]] Annex A.** The North American hook for ECA on new-construction and tie-in welds.
- **General fabrication — [[bs-7910-flaw-assessment]].** The detailed methodology referenced from API 1104 Annex A and used directly in EU / UK / offshore fabrication.
- **In-service flaws — [[api-std-579]] (API 579-1 / ASME FFS-1).** For flaws found *after* commissioning. See [[fitness-for-service]] for the in-service framing.

ECA is conditional on the upstream WPS having been qualified to produce welds with toughness compatible with the assessment — an ECA cannot rescue a procedure that did not test for CTOD in the first place.

## Sour-service welding

Welds destined for wet H<sub>2</sub>S service (oil and gas with sulphide partial pressure above the [[iso-15156]] threshold) carry additional constraints aimed at preventing sulphide stress cracking (SSC) and hydrogen-induced cracking (HIC):

- **Hardness control in the HAZ.** Cap typically **250 HV<sub>10</sub>** (API 1104 Annex A / ISO 15156-2) and as low as **275 HV<sub>10</sub>** for some carbon-steel families; higher hardness correlates with SSC susceptibility. Achieved by heat-input control, preheat, and PWHT.
- **Post-weld heat treatment (PWHT).** Stress-relief at code-specified temperature and hold time, sized to wall thickness. PWHT reduces residual stress and tempers martensitic HAZ. Construction-code rules for PWHT live in ASME BPVC VIII / B31.3 / B31.4 / B31.8; the sour-service overlay tightens them.
- **Filler-metal selection.** Low-residual-element grades (low S, P, low diffusible hydrogen E-Hx low classifications); for severe sour service, Cr-Mo grades or duplex / nickel-alloy fillers. See [[aws-filler-metal-overview]] and AWS A5.5 / A5.10 specifications.
- **Qualification-coupon testing.** Sour-service qualification adds NACE TM0177 SSC testing on the qualification coupon for the target H<sub>2</sub>S partial pressure, alongside the standard mechanical tests.

The governing materials standard is **[[iso-15156]]** (NACE MR0175 / ISO 15156); welding-procedure-specific overlays appear in API 1104 Annex A, ASME B31.4 / B31.8, and operator specifications.

## Standards

Bidirectional links — each of the standards pages below references this concept page in turn:

- [[api-std-1104]] — pipeline welding, mechanical-test-driven qualification, ECA via Annex A.
- [[asme-bpvc-ix]] — generalised welding / brazing / fusing qualification, exhaustive essential / supplementary-essential / nonessential variable lists.
- [[aws-d1-1]] — structural welding code (steel); pre-qualified WPS option.
- [[aws-filler-metal-overview]] — AWS A5.x consumable classification and selection.
- [[bs-7910-flaw-assessment]] — ECA methodology (FAD, residual-stress profiles, partial safety factors).
- [[astm-a370]] — mechanical-test methods called by reference from all three welding-code families.
- [[iso-15156]] — sour-service materials envelope; constrains welding-procedure hardness and PWHT.
- [[api-std-579]] — in-service ECA counterpart; applied when flaws are detected post-commissioning.

## Related concepts

Wikilinks below point to concept pages that may not yet exist — leave as wikilinks for future creation per the spinout's link-and-fill convention.

- [[fitness-for-service]] — the in-service ECA framing; this concept page is the new-build / construction-time counterpart, and the two share the FAD methodology.
- [[fracture-toughness-measurement]] — K<sub>Ic</sub>, J<sub>Ic</sub>, CTOD, T<sub>0</sub>; the test methods that produce the toughness inputs feeding ECA.
- [[sour-service-materials]] — H<sub>2</sub>S service envelope per ISO 15156; constrains PWHT and HAZ hardness for welds in scope.
- [[fatigue-design-and-assessment]] — weld-detail S-N classification (BS 7608, DNV-RP-C203), fatigue crack-growth integration; downstream of weld-procedure-set residual stress and toughness.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog reference for API 1104, API 579, API RP 2201, and the API spec-line-pipe family.
- [og-standards-bsi](../sources/og-standards-bsi.md) — catalog reference for BS 7910 and the BS 7448 toughness-test family.
- [og-standards-astm-a-series](../sources/og-standards-astm-a-series.md) — catalog reference for ASTM A370 and the A-series specimen and test-method standards.

## Notes

- This is a concept page, not a standards page. No clause text, mechanical-acceptance numbers (other than the API 1104 1/8 in / 3.2 mm and the ISO 15156 250 HV figures already public on the standards pages), formulas, or FAD curves are reproduced here. For normative use, cite the publisher edition of the relevant standard directly.
- The 1/8 in (3.2 mm) bend-test crack limit and the 250 HV HAZ hardness cap are standards-derived constants. Per the [calc citation contract](../../../../../.claude/rules/calc-citation-contract.md), any calc module that consumes these values must emit a `Citation` instance pinning `code_id=api-std-1104` or `code_id=iso-15156` with the specific revision.
- WPS / PQR records are operator deliverables. This wiki does not host project-specific WPS / PQR templates; those live with the fabricator's quality system.
