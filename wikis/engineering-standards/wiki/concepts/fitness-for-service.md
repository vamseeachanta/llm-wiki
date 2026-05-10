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
last_updated: 2026-05-10
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
- **Code-gated invocation.** The in-service inspection codes — **API 510** (pressure vessels), **API 570** (process piping), **API 653** (atmospheric storage tanks) — explicitly delegate to [api-std-579](../standards/api-std-579.md) / [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) when an out-of-code condition is found. FFS is not a free-standing decision; it is invoked under the authority of an inspection code.
- **Life-extension assessment.** When operators seek to extend service life of ageing assets (refineries, offshore platforms, pipelines) past original design life, FFS quantifies remaining life from the current damage state plus a projected damage-progression model (corrosion rate, fatigue-cycle accumulation, creep-strain accumulation).
- **Run-or-repair decisions.** During planned shutdowns, FFS supports go/no-go calls on whether a flaw warrants immediate repair, can be deferred to the next turnaround under a monitoring regime, or can be left in service indefinitely.
- **Re-rating.** When operating envelope changes (pressure, temperature, fluid composition), FFS evaluates whether existing damaged components are acceptable under the revised loads.

## Damage mechanisms covered

The FFS standards organise their methods by damage-mechanism family. The table below maps damage mechanisms onto the part / annex structure of the two dominant codes, [api-std-579](../standards/api-std-579.md) and [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md).

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

### Three-tier assessment — multi-criteria comparison

The level distinction is not arbitrary; each tier is engineered for a particular trade-off between input cost, conservatism, and acceptance authority. The table below summarises how the three tiers differ across the six dimensions practitioners actually weigh when scoping an assessment.

| Dimension | Level 1 (screening) | Level 2 (engineering) | Level 3 (advanced) |
|---|---|---|---|
| **Input requirements** | Nominal geometry, single thickness reading or flaw dimension, design pressure/temperature | Full damage profile (grid UT, crack length + depth + aspect ratio), measured operating loads, validated material properties (yield, UTS, toughness) | All Level-2 inputs plus J–R curve, constraint parameter (T-stress or Q), residual-stress field from process-specific weld simulation, optional in-situ measurements |
| **Method** | Tabulated charts, look-up curves, single-equation acceptance criteria | Closed-form FAD with code-tabulated K<sub>I</sub> solutions, reference-stress collapse loads, screening Paris-law fatigue integration | Elastic-plastic FEA, ductile-tearing analysis, probabilistic / Monte Carlo, full-field residual-stress mapping |
| **Conservatism** | High — bounds the worst credible damage state | Moderate — calibrated for typical refinery / petrochem geometries | Low — best-estimate result with explicit uncertainty quantification |
| **Output** | Pass / fail verdict; no remaining-life estimate | Remaining-strength factor (RSF), allowable maximum operating pressure, remaining-life estimate, re-inspection interval | Probability of failure, distribution on remaining life, sensitivity ranking on inputs, deformation field |
| **Computational cost** | Minutes (spreadsheet) | Hours to days (engineering software, e.g. Signal FFS, Quest Integrity LifeQuest, in-house Python/MATLAB) | Days to weeks (commercial FEA: Abaqus, ANSYS, ADINA; specialist consultancy required) |
| **Regulatory / inspection-code acceptance** | Routine acceptance by API 510 / 570 / 653 jurisdictional inspectors with minimal supplementary review | Requires registered/chartered engineer sign-off; often peer-reviewed by operator's central reliability group | Commonly subject to third-party verification (DNV, Lloyd's, ABS) for offshore / high-consequence assets; may be compulsory for life-extension regulatory submissions |

A **disciplined escalation gate** runs through the three tiers: pass at Level 1 closes the assessment; fail at Level 1 invokes Level 2; marginal-pass at Level 2 (e.g. RSF within 5 % of acceptance) or atypical geometry invokes Level 3. Operators who jump straight to Level 3 without a documented Level-2 fail expose themselves to "expensive answer to the wrong question" — Level 3 has more degrees of freedom and is more sensitive to input quality.

The shared analytical core for crack-like flaws is the **Failure Assessment Diagram (FAD)** — a two-criterion plot with K<sub>r</sub> (toughness ratio, ordinate) versus L<sub>r</sub> (load ratio, abscissa). Points inside the FAD curve are acceptable; points outside indicate unstable fracture (high K<sub>r</sub>) or plastic collapse (high L<sub>r</sub>) or interaction. Both [api-std-579](../standards/api-std-579.md) Part 9 and [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) Annex A use the FAD, with code-specific calibration of the curve and option-numbering of the toughness inputs. The FAD's ordinate K<sub>r</sub> is grounded in [fracture-toughness-measurement](./fracture-toughness-measurement.md) (K<sub>Ic</sub>, J<sub>Ic</sub>, CTOD), often delivered through [master-curve-and-transition-temperature](./master-curve-and-transition-temperature.md) for ferritic steels in the transition regime; the abscissa L<sub>r</sub> is the ratio of applied primary load to plastic-collapse load.

**Residual stress** treatment is a load-bearing input. Welded components carry as-welded residual stresses up to the parent-material yield; post-weld heat treatment (PWHT) reduces but does not eliminate them. Both codes provide tabulated residual-stress profiles (membrane plus bending) for common weld geometries; these are summed with primary stress in the FAD ordinate. Mixing residual-stress profiles between codes is **not permitted** — each code's profiles are internally calibrated against its own FAD.

**Partial safety factors** (PSFs) are applied to load, toughness, flaw size, and material-strength inputs to account for measurement uncertainty. BS 7910 Annex N provides probabilistic / FORM-SORM frameworks; API 579-1 provides PSF tables in Part 9 and aligns with API RP 581 risk-based inspection inputs. The probabilistic route ties FFS to [risk-based-inspection](./risk-based-inspection.md) — outputs become probability-of-failure inputs for the next RBI cycle.

## API 579-1 / ASME FFS-1 — Part-by-Part synthesis

The fourteen Parts of API 579-1 / ASME FFS-1 (Third Edition, 2016, with subsequent addenda) are the de facto industry default for refining and petrochemical FFS. The synthesis below is non-normative — for any clause-level work, cite the publisher edition directly.

| Part | Scope | Practical-application notes |
|---|---|---|
| **Part 1** — General | Scope, organisation, applicability, assessment procedure overview, RSF definition, remaining-life concepts, glossary | Read first on every project — defines RSF acceptance threshold (typically 0.90 for continued service) and the Level 1/2/3 escalation contract |
| **Part 2** — FFS Engineering Procedures | Generic five-step assessment (applicability → data → screening → assessment → remediation/reinspection) | The procedural skeleton imported by every other Part; auditors cite Part 2 step numbers when reviewing FFS reports |
| **Part 3** — Brittle Fracture | Low-temperature service, MAT (Minimum Allowable Temperature) curves, Charpy / toughness inputs | Critical for cold restart, depressurisation events, autorefrigeration; pairs with [brittle-fracture](./brittle-fracture.md) and [master-curve-and-transition-temperature](./master-curve-and-transition-temperature.md) |
| **Part 4** — General Metal Loss | Uniform thinning, RSF based on average measured thickness over critical thickness profile | Most-used Part in refineries; Level 1 is the inspector's go-to for routine UT-grid disposition; integrates directly with API 510 / 570 / 653 inspection findings |
| **Part 5** — Local Metal Loss | Localised thin areas (LTAs), grooves, geometric thinning | Folias-type bulging factor; pipeline corroded-pipe equivalent is [dnv-rp-f101](../standards/dnv-rp-f101.md), which is methodologically aligned but separately maintained |
| **Part 6** — Pitting | Discrete and grouped pits, pit-couple interaction, widespread pitting | Visual-pattern-density approach at Level 1; finite-element pit-cluster modelling at Level 3 |
| **Part 7** — Hydrogen Blisters, HIC, SOHIC, Laminations | Wet-H<sub>2</sub>S service damage; ties to NACE MR0175 / ISO 15156 | Common in sour-service refining; cross-references [hydrogen-embrittlement](./hydrogen-embrittlement.md) and [stress-corrosion-cracking](./stress-corrosion-cracking.md) for SOHIC initiation |
| **Part 8** — Weld Misalignment & Shell Distortion | Out-of-roundness, peaking, flat spots, bulges; stress-magnification factors | Output feeds Part 9 (cracks at distorted welds) or HTHA assessment per Part 4/8 hybrid; common on legacy heat-exchanger shells |
| **Part 9** — Crack-like Flaws | Planar flaws, FAD assessment, fatigue and SCC growth, leak-before-break | The headline FFS Part; methodologically aligned with [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) Annex A. Inputs from [fatigue-crack-growth](./fatigue-crack-growth.md) Paris-law and [stress-corrosion-cracking](./stress-corrosion-cracking.md) for environmental cracking |
| **Part 10** — Creep | Time-dependent damage, creep-fatigue interaction, creep crack growth | High-temperature service (refining hot units, ammonia plants, ethylene cracking); Omega method for creep-strain accumulation; pairs with API RP 941 for HTHA proximity assessments |
| **Part 11** — Fire Damage | Post-fire metallurgical assessment, hardness/thickness mapping | Typically post-incident; Heat-Affected Zone classification (Heat I–IV) defines salvage-versus-replace decisions |
| **Part 12** — Dents, Gouges, Combinations | Mechanical damage assessment | More commonly applied to vessels; pipeline-dent assessments route through [dnv-rp-f101](../standards/dnv-rp-f101.md) and [api-std-1104](../standards/api-std-1104.md) Annex A |
| **Part 13** — Laminations | Pre-existing rolling-mill laminations, mid-wall planar discontinuities | Distinguish stable (no growth) from active (HIC-coupled); inputs to Part 7 when laminations interact with H<sub>2</sub>-induced damage |
| **Part 14** — Fatigue | Cyclic-loading damage, S-N (stress-life) and ε-N (strain-life), Paris-law crack growth | Aligned conceptually with [fatigue-design-and-assessment](./fatigue-design-and-assessment.md); pressure-cycle counting per API 579 Annex 14B |

## Worked-example mini-case-studies

The following case sketches illustrate the FFS workflow on representative industry geometries. Numbers are illustrative; every real assessment requires the publisher edition's clause text and verified inputs.

### Case A — Corroded pressure-vessel shell (Part 4)

A 1980-vintage 2.5 m-diameter, 25 mm-wall carbon-steel reactor in a sour-water-stripper service shows external general thinning to a grid-average 19 mm with isolated local minima of 16 mm over a 200 mm × 200 mm patch. Original design pressure 18 barg; design [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md). Inspection invoked by API 510 finds the average below 80 % nominal — escalates to FFS.

- **Level 1 (Part 4 general metal loss):** average thickness above the Part 4 screening curve for the operating pressure → general-loss screen passes.
- **Level 2 (Part 4 + Part 5):** the 200 mm × 200 mm local minimum is treated as an LTA; Folias-corrected RSF computed against the design [hoop-stress](./hoop-stress.md) condition. RSF = 0.93 — above the 0.90 acceptance threshold, but inside the 0.05 escalation margin.
- **Verdict:** continue service at design MAOP, re-inspect in two years, install corrosion monitoring per [corrosion-rate-measurement](./corrosion-rate-measurement.md). RBI risk rank steps up one band.

### Case B — HTHA-affected hydrogen-service reactor (Part 4 + Part 8)

A 30-year-old hydrocracker reactor operating at 380 °C / 120 barg H<sub>2</sub> partial pressure (originally specified to API RP 941 Nelson-curve envelope) is suspected of incipient high-temperature hydrogen attack (HTHA) after wet-fluorescent-magnetic-particle UT detects subsurface fissuring. The carbon steel grade is borderline on the post-2016 [htha-nelson-curves](./htha-nelson-curves.md) revision.

- **Level 1:** screening per API RP 941 Nelson curve places the operating point within HTHA-susceptibility envelope → fails screen.
- **Level 2 (Part 4 + Part 8):** subsurface UT mapping characterises fissure depth and extent; effective wall thickness is reduced by the fissured layer; out-of-roundness measured separately for shell distortion stress concentration.
- **Level 3:** elastic-plastic FEA with degraded-layer constitutive model; tearing-instability assessment per Part 9 ductile-tearing branch.
- **Verdict:** de-rate temperature by 20 °C, install permanent acoustic-emission monitoring, plan reactor replacement at next major turnaround. RBI POF input upgraded from "inspection-controlled" to "monitoring-controlled".

### Case C — Pipe creep fissure (Part 10)

A Cr–Mo high-temperature header in a refinery reformer, 35 years in service at 580 °C, shows surface-breaking creep fissures detected by replication metallography during a turnaround.

- **Level 1:** Larson–Miller life-fraction estimate from operating history — life-fraction exceeds 0.7, screen fails.
- **Level 2 (Part 10):** Omega-method strain-rate analysis with measured fissure depth; remaining-life estimated as 4 years at current conditions.
- **Level 3:** creep-crack-growth integration per Annex F (CC-similar to BS 7910 Annex J); confirms fissure growth dominates over uniform creep accumulation.
- **Verdict:** replace section at next turnaround (18 months); install thermocouples on the suspect spool to confirm metal temperature; reduce header dwell-temperature 10 °C as interim mitigation. Cross-references [creep-rupture](./creep-rupture.md) and [larson-miller-parameter](./larson-miller-parameter.md).

### Case D — Welded-joint flaw assessment (Part 9)

During UT shear-wave inspection of a recently fabricated stainless-steel pipework butt weld in a cryogenic LNG service, a planar 8 mm × 2 mm crack-like indication is detected at the root. Workmanship code [api-std-1104](../standards/api-std-1104.md) workmanship criteria fail — escalates to ECA / FFS.

- **Level 1 (Part 9):** screening table for crack-like flaws in the relevant geometry → marginal, depends on toughness assumption.
- **Level 2 (Part 9 / [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) Annex A):** FAD analysis with measured CTOD inputs (parent and HAZ), pre-service residual-stress profile from Annex K. Operating point at L<sub>r</sub> = 0.6, K<sub>r</sub> = 0.55 — inside the FAD with safe margin.
- **Verdict:** accept the flaw, monitor at next planned shutdown via PAUT; document in plant integrity register. Cross-reference: [engineering-critical-assessment](./engineering-critical-assessment.md) (the pre-service analogue), [welding-procedures-and-acceptance](./welding-procedures-and-acceptance.md) (workmanship escalation route).

## FFS + RBI integration loop

[risk-based-inspection](./risk-based-inspection.md) and FFS form a closed control loop on equipment integrity. RBI ranks equipment by combined probability of failure (POF) × consequence of failure (COF) per API RP 580 / 581 methodology; high-POF items get inspected first or more thoroughly. The inspection finding (or absence thereof) feeds back into the next RBI cycle.

The integration sequence on a real refining unit:

1. **RBI screening** — annually or per turnaround cycle; produces a ranked inspection plan with prescribed coverage per damage mechanism.
2. **Inspection** — UT, RT, MFL, ILI, PAUT executed to the RBI-prescribed scope; findings logged against [api-510](../standards/api-510.md) / API 570 / API 653 acceptance criteria.
3. **Acceptance gate** — workmanship-equivalent codes accept or reject the as-found state.
4. **FFS invocation** — for rejected findings, FFS Part-2 procedure applied; Level 1 first, escalating only on fail.
5. **Verdict back to RBI** — FFS RSF, remaining-life, and re-inspection interval directly update the RBI POF and inspection-plan input deck for the next cycle.
6. **Re-rating or repair** — if FFS verdict is "repair", planning routes to ASME PCC-2 (see next section); if "re-rate", the operating envelope is updated and a Management-of-Change cycle records the basis.

The loop's validity depends on **input quality at every stage** — a sloppy UT grid feeding a rigorous Part 4 FFS produces a precise wrong answer. The probabilistic FFS methods in API 579-1 Part 9 Annex N and BS 7910 Annex N quantify input-uncertainty propagation, but cannot manufacture data quality that wasn't captured.

## FFS + repair planning (ASME PCC-2)

Where FFS produces a "repair" verdict, the canonical planning standard is **ASME PCC-2 — Repair of Pressure Equipment and Piping**. PCC-2 catalogues weld-repair and non-weld-repair methods (composite repairs, mechanical clamps, bolted enclosures, hot tapping, weld overlay, controlled deposition welding). Each PCC-2 article is engineered to a specified damage scenario; the FFS verdict's damage-mechanism characterisation (Part 4 thinning vs Part 9 cracking vs Part 10 creep) routes directly to the matching PCC-2 article.

Part 13 of API 579-1 (Laminations) and Part 7 (HIC/SOHIC/blistering) feed PCC-2 Article 2.6 (Filler-fillet patches) and Article 3.5 (Composite repair systems) respectively. Crack-like Part 9 verdicts route to PCC-2 Article 2.10 (Weld build-up) or Article 3.10 (Mechanical clamp). Post-repair, the repair itself becomes a new FFS-traceable feature on the equipment, entering the next RBI-FFS cycle with its own degradation model.

## Industry adoption

| Industry | Primary FFS authority | Notes |
|---|---|---|
| **Refining (downstream petroleum)** | API 579-1 / ASME FFS-1, governed under [api-510](../standards/api-510.md) (vessels), API 570 (piping), API 653 (tanks) | Largest installed-base of FFS practice globally; refinery turnaround RBI/FFS workflow is the canonical implementation pattern |
| **Petrochemicals** | API 579-1 / ASME FFS-1 | Olefin plants, ammonia, methanol; Part 10 creep + Part 7 HIC commonly invoked together |
| **Offshore O&G (topsides + structures)** | [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md), [dnv-rp-c210](../standards/dnv-rp-c210.md) (probabilistic structural integrity), [dnv-rp-c203](../standards/dnv-rp-c203.md) (fatigue) | UK/EU sector; FPSO hull plate / topsides piping; class-society verification (DNV, Lloyd's, ABS) is compulsory |
| **Pipelines (onshore + offshore)** | [dnv-rp-f101](../standards/dnv-rp-f101.md) (corrosion), [api-std-1104](../standards/api-std-1104.md) Annex A (girth-weld ECA), BS 7910 Annex G | ILI-driven dig prioritisation feeds FFS; mechanical-damage assessments per ASME B31.8S Appendix R |
| **Power generation (fossil)** | API 579-1 + R6 (UK CEGB legacy) for boiler / steam piping; ASME B&PV Section XI for nuclear | Creep and creep-fatigue (Part 10) dominant; high-temperature header replacements driven by creep-life estimates |
| **Nuclear** | ASME BPVC Section XI (in-service inspection), proprietary utility procedures | API 579-1 not directly invoked; methodology shared (FAD, J-integral) but governed under nuclear regulator |

A consistent thread across industries: FFS authority is always invoked downstream of an inspection-code finding, never as a standalone go/no-go.

## Standards

- [api-std-579](../standards/api-std-579.md) — **API 579-1 / ASME FFS-1**, the joint API + ASME consensus standard. Full FFS suite covering brittle fracture (Pt 3), general / local thinning (Pt 4–5), pitting (Pt 6), blisters (Pt 7), distortion (Pt 8), crack-like flaws (Pt 9), creep (Pt 10), fire (Pt 11), dents/gouges (Pt 12). US-led, refining/petrochem industry default.
- [bs-7910-flaw-assessment](../standards/bs-7910-flaw-assessment.md) — **BS 7910:2013+A1:2015**, BSI's parallel UK guide. Concentrates on crack-like flaws, fatigue crack growth, leak-before-break, creep crack growth. Offshore O&G and EU/UK fabrication default. Methodologically aligned with API 579-1 but with BS-specific FAD calibration and residual-stress profiles.
- [asme-bpvc-viii-1](../standards/asme-bpvc-viii-1.md) — **ASME BPVC Section VIII Division 1**, design-by-rule pressure-vessel construction code. Reference for new-build design margins; FFS critical-flaw-size assessments benchmark against the original design's allowable-stress envelope.
- [asme-bpvc-viii-2](../standards/asme-bpvc-viii-2.md) — **ASME BPVC Section VIII Division 2**, design-by-analysis alternative-rules construction code. The stress-classification and linearisation conventions used in FFS Annexes (membrane / bending / peak decomposition; primary / secondary / peak categorisation) are inherited from VIII-2.

Bidirectional: each of those standards pages should cross-link back to this concept page once the convention propagates.

## Related concepts

- [fracture-toughness-measurement](./fracture-toughness-measurement.md) —
  K<sub>Ic</sub>, J<sub>Ic</sub>, CTOD, T<sub>0</sub> (Master Curve); the
  test methods (ASTM E399 / E1820 / E1921, BS 7448) that produce the
  toughness inputs feeding FFS Level 2/3 crack assessments.
- [fatigue-design-and-assessment](./fatigue-design-and-assessment.md) —
  S-N (BS 7608, DNV-RP-C203), Paris-law crack-growth integration,
  mean-stress and environmental modifiers; FFS fatigue assessments
  integrate forward in time from a known initial flaw.
- [welding-procedures-and-acceptance](./welding-procedures-and-acceptance.md) —
  workmanship acceptance criteria (AWS D1.1, API 1104, ISO 5817) versus
  fitness-for-purpose (ECA via BS 7910 Annex A or API 1104 Annex A); FFS
  is the escalation path when a flaw fails workmanship but may pass
  fitness-for-purpose.
- [ductile-tearing](./ductile-tearing.md) — J-R curve behaviour, tearing
  instability, constraint effects; basis for FFS Level 3 advanced
  assessments and the ductile-fracture branch of the FAD.
- [risk-based-inspection](./risk-based-inspection.md) — upstream
  programme that schedules the inspection finding which invokes FFS;
  the FFS verdict feeds back into the next RBI cycle's POF.
- [engineering-critical-assessment](./engineering-critical-assessment.md) —
  ECA is the pre-service / fabrication-acceptance analogue of FFS using
  the same BS 7910 / API 579 FAD machinery; FFS is its in-service twin.
- [brittle-fracture](./brittle-fracture.md) — failure mode addressed by
  [api-std-579](../standards/api-std-579.md) Part 3 (low-temperature
  service) and the FAD-K<sub>r</sub> ordinate.

## Source materials

- [og-standards-api](../sources/og-standards-api.md) — catalog reference for the API 579 family, including the joint API/ASME FFS-1 numbering and edition history.

## Notes

- This is a concept page, not a standards page. No clause text, formulas, FAD curves, or tabulated data are reproduced here. For normative use, cite the publisher edition of the relevant standard directly.
- The FFS workflow is gated upstream by the in-service inspection codes (API 510 / 570 / 653); a standalone FFS calculation without a documented inspection finding is not a sanctioned engineering deliverable.
- Pipeline FFS for corrosion-only damage typically routes through [dnv-rp-f101](../standards/dnv-rp-f101.md) (Corroded Pipelines) rather than the general API 579-1 Part 5; pipeline ECA for crack-like flaws routes through [api-std-1104](../standards/api-std-1104.md) Annex A or BS 7910 Annex A.
