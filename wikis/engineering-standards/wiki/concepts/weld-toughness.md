---
title: "Weld Toughness and Heat-Affected-Zone Properties"
slug: weld-toughness
tags:
  - welding
  - haz
  - fracture-toughness
  - charpy
  - ctod
  - weldment-qualification
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/astm-a370.md
  - standards/astm-e1820.md
---

# Weld Toughness and Heat-Affected-Zone Properties

> Concept page. Definitional and link-rich; load-bearing acceptance numbers, clause text, and method detail live on the standards pages this concept routes into. No clause text or formulas are reproduced here.

## Why weld toughness matters

A weld is a metallurgical discontinuity in an otherwise homogeneous component. Three coupled factors mean the weld zone routinely controls the fracture-toughness budget of a structure even when the parent material has been chosen with margin:

- **Weld metal microstructure differs from parent.** It is a small as-cast ingot — solidified from melt, with its own dendrite morphology, residual elements from the consumable, and (for multi-pass welds) layered reheat structure. Its toughness can be either higher or lower than parent, depending on the consumable choice and heat input.
- **The HAZ has experienced multiple thermal histories.** Each pass of a multi-pass weld reheats earlier-deposited material and the adjacent parent. Local microstructural zones develop, each with a distinct toughness signature, and the boundaries between them can themselves be brittleness magnets (see *Local brittle zones* below).
- **Residual stresses near the weld are tensile.** As-welded residual stress at the weld fusion line approaches the parent's yield strength in tension. Tensile residual stress reduces the apparent toughness available to resist applied load and is a mandatory input to engineering critical assessment.

Together these factors mean that a weldment toughness specification is *not* satisfied by parent-metal toughness data — the weld and HAZ must be sampled directly. This is the core justification for the weldment-toughness sampling regimes in [[api-std-1104]], [[asme-bpvc-ix]], [[aws-d1-1]], and the offshore rules that build on them.

## HAZ sub-zones

The HAZ is conventionally divided by peak temperature reached during the welding thermal cycle. Each sub-zone has a characteristic microstructure and a characteristic toughness implication:

| Sub-zone | Peak T | Microstructure | Toughness implication |
|---|---|---|---|
| Coarse-Grained HAZ (CGHAZ) | > ~1100 °C | Coarse austenite grains; on cooling → bainite or martensite depending on hardenability and cooling rate | Lowest toughness; usually the controlling region for weldment fracture |
| Fine-Grained HAZ (FGHAZ) | ~900–1100 °C | Fully austenitised, refined grain on cooling | Comparable to or better than parent |
| Inter-Critical HAZ (ICHAZ) | ~750–900 °C | Partial austenitisation; mixed transformed-and-untransformed structure | Variable; can host MA islands |
| Sub-Critical HAZ (SCHAZ) | < ~725 °C | Tempering and recovery of parent microstructure | Slight toughness *increase* in some hardened parents |
| Inter-Critically Reheated CGHAZ (ICCGHAZ) | reheated CGHAZ from a later pass into the inter-critical range | Coarse prior austenite + martensite-austenite (MA) constituents on grain boundaries | Worst-case for offshore / arctic service — primary local-brittle-zone concern |

The CGHAZ and ICCGHAZ are the two sub-zones that dominate weldment fracture-toughness specifications. Sampling regimes (below) explicitly target them.

## Test specimens

Weldment toughness testing follows the same parameter families as parent-metal toughness ([[fracture-toughness-measurement]]), with weldment-specific sampling rules layered on top:

- **Charpy V-notch (CVN).** Method per [[astm-a370]] (which calls ASTM E23 for the impact test itself). Notch locations published by the welding code, typically: weld centreline (weld-CL), fusion line (FL), FL+1 mm, FL+3 mm, FL+5 mm. Each location samples a different microstructural target — weld-CL hits weld metal; FL straddles weld / CGHAZ; FL+1 / FL+3 / FL+5 progress out into the FGHAZ / ICHAZ / unaffected parent.
- **CTOD or J-integral.** Method per [[astm-e1820]] (with BS 7448 / ISO 12135 as recognised parallels). Notch placed deliberately on the weld metal or the targeted HAZ sub-zone (FL or CGHAZ). Specimen geometry typically SE(B) for weldments because the through-thickness orientation aligns naturally with bend loading.
- **Specimen orientation.** Two conventions in common use: **NP** (notch parallel to the weld direction — samples a long line of weld metal or HAZ at a fixed depth) and **NB** / through-thickness (notch perpendicular to the surface — samples weld and HAZ across the full wall thickness). Offshore specs typically require both because the controlling defect orientation is project-dependent.
- **Sub-size considerations.** Pipeline wall thicknesses below the standard 10 mm Charpy specimen require sub-size CVN coupons (typically 7.5 mm or 5 mm). [[astm-a370]] publishes the energy-correlation rules for sub-size acceptance.

## Local brittle zones (LBZ)

A "local brittle zone" is an island of low-toughness microstructure — typically ICCGHAZ with martensite-austenite (MA) constituents on prior austenite grain boundaries — embedded in an otherwise acceptable HAZ. Multi-pass weld procedures, especially those used on heavy-wall offshore line-pipe and structural plate, are predisposed to LBZ formation because each pass reheats the prior CGHAZ into the inter-critical range, generating fresh MA at the grain boundaries.

Because LBZs are spatially small and randomly distributed along the fusion line, mean-toughness sampling will under-detect them. Offshore and arctic specs respond with **random-spot CTOD testing**, where a population of CTOD specimens is removed from the FL+1 mm position and reported as a distribution. The acceptance criterion is on the *minimum* (or low-quantile) result, not the mean. ABS, DNV (DNV-OS-F101 weldment annex), and the ISO 15614 weld-procedure-qualification series each publish their own LBZ-targeted sampling protocol.

## Acceptance criteria

Acceptance limits are heavily code-dependent. The following table lists the *kind* of acceptance — the actual numerical limits live on the cited standards pages:

| Standard | Method called | Acceptance flavour |
|---|---|---|
| [[api-std-1104]] | Charpy at weld-CL and at HAZ; bend; tensile | Energy floor at lowest service temperature, weld and HAZ separately; Annex A opens an ECA route |
| [[asme-bpvc-ix]] | Tensile (cross-weld) + bend (face / root / side); supplementary CVN when called by construction code | Bend acceptance + parent-strength tensile; toughness via supplementary-essential variables when in scope |
| [[aws-d1-1]] | Bend + Charpy when toughness is a contract requirement | Energy floor by service category; pre-qualified WPS option for many common joints |
| DNV-OS-F101 | CTOD at FL and FL+1 mm; multiple HAZ sample positions; weldment qualification annex | CTOD floor at the lowest design temperature; LBZ-aware random-spot sampling |
| [[api-spec-5l]] PSL2 | Drop-Weight Tear Test (DWTT) + Charpy at weld-CL | Acceptance varies by line-pipe class and toughness category |

The general pattern: **prescriptive workmanship-based codes (API 1104 main body, ASME BPVC IX, AWS D1.1) accept on Charpy energy and bend behaviour**; **fracture-mechanics-based offshore codes (DNV-OS-F101, BS 7910 via API 1104 Annex A) accept on CTOD or J**. The two routes are not interchangeable — a CTOD-qualified procedure does not retroactively meet a Charpy-only acceptance and vice versa.

## Sour-service weld toughness

Wet-H<sub>2</sub>S service per [[iso-15156]] (NACE MR0175) layers additional constraints on top of the welding-code toughness regime:

- **HAZ hardness control.** Cap typically **250 HV<sub>10</sub>** (API 1104 Annex A / ISO 15156-2), tightened to **275 HV<sub>10</sub>** for some carbon-steel families. Achieved by heat-input control, preheat, and PWHT.
- **Post-weld heat treatment (PWHT).** Stress-relief at code-specified temperature and hold time, sized to wall thickness. PWHT softens the CGHAZ, tempers martensitic transformation products, and reduces residual stress; net effect on toughness is generally favourable, though over-long PWHT cycles can re-embrittle some Cr-Mo grades (temper embrittlement window).
- **Ferrite-content control.** For duplex and super-duplex weldments, ferrite/austenite phase balance in the weld and HAZ is specified (typically 30–70 % ferrite). Excess ferrite from rapid cooling reduces toughness; excess austenite from slow cooling reduces SCC resistance.
- **Filler-metal residual-element controls.** Low-residual-element grades (low S, P, low diffusible hydrogen) are specified. For [[api-spec-5l]] sour line-pipe, *low-Ni* HAZ chemistry is sometimes a counterintuitive requirement — Ni promotes austenite stability and can worsen SSC susceptibility at the same hardness, despite improving low-temperature CVN.

Sour-service-specific qualification adds NACE TM0177 SSC testing on the qualification coupon at the target H<sub>2</sub>S partial pressure, alongside the standard mechanical and toughness tests. The materials envelope is captured on [[sour-service-materials]].

## Standards

Bidirectional links — each standards page below cross-references this concept page in turn:

- [[api-std-1104]] — pipeline-weld qualification, mechanical-test menu including weldment Charpy, ECA route via Annex A.
- [[asme-bpvc-ix]] — generalised welding qualification; supplementary-essential variables govern when toughness is in scope.
- [[aws-d1-1]] — structural welding code (steel); pre-qualified WPS option and Charpy acceptance by service category.
- [[astm-a370]] — Charpy V-notch test method, bend test method; called by reference from the welding codes.
- [[astm-e1820]] — J-integral, CTOD, and resistance-curve test method for weldment fracture-mechanics inputs.
- [[iso-15156]] — sour-service materials envelope; HAZ hardness cap and PWHT requirements for welds in scope.

## Related concepts

- [[welding-procedures-and-acceptance]] — the WPS / PQR / WPQ qualification pyramid; this concept page is the toughness-specific deep-dive on the mechanical-test side of that workflow.
- [[fracture-toughness-measurement]] — parent-metal K / J / CTOD / `T₀` measurement; this page is the weldment-specific counterpart.
- [[brittle-fracture]] — failure-mode framing for low-toughness weldment failures (lower-shelf and transition-region cleavage).
- [[sour-service-materials]] — H<sub>2</sub>S service envelope per ISO 15156; constrains HAZ hardness, PWHT, and consumable residual-element chemistry.
- [[fatigue-design-and-assessment]] — weld-detail S-N classification (BS 7608, DNV-RP-C203); downstream consumer of weld geometry and residual-stress profile set by the welding procedure.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog reference for API 1104 and the API spec-line-pipe family.
- [og-standards-astm-a-series](../sources/og-standards-astm-a-series.md) — catalog reference for ASTM A370 and the A-series specimen and test-method standards.
- [og-standards-astm-e-series](../sources/og-standards-astm-e-series.md) — catalog reference for ASTM E23, E1820, E1921, and the E-series fracture-mechanics method standards.

## Notes

- Concept page only — no clause text, acceptance numbers, or method-specific equations are reproduced here. For normative use, cite the publisher edition of the relevant standard directly.
- Specific HAZ hardness limits (250 HV<sub>10</sub> / 275 HV<sub>10</sub>) and CVN / CTOD acceptance floors are standards-derived constants. Per the [calc citation contract](../../../../../.claude/rules/calc-citation-contract.md), any calc module that consumes these values must emit a `Citation` instance pinning `code_id=api-std-1104`, `code_id=iso-15156`, or the relevant DNV / ABS code with the applicable revision.
- LBZ random-spot sampling protocols are operator and project-specific; this wiki does not host project-specific weldment-qualification matrices.
