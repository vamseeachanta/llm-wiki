---
title: "Sandstone Acidizing"
tags: [matrix-acid, sandstone-acidizing, mud-acid, hf, hcl, schechter-gidley-williams, preflush, postflush, reaction-kinetics, completion]
added: 2026-05-16
last_updated: 2026-05-16
---

# Sandstone Acidizing

## Scope

Sandstone acidizing is the matrix-acid treatment family designed to dissolve **damage minerals** (drilling-fluid filtercake, swelled and migrated clays, cementing-fluid debris, perforation crushed-zone fines) in sandstone formations using hydrofluoric-acid-bearing chemistries. The dominant chemistry is **mud acid** — a mixture of HCl and HF — and the dominant treatment architecture is the **three-stage Schechter-Gidley-Williams sequence** of HCl preflush, HCl/HF main treatment, and HCl-or-ammonium-chloride postflush.

The fundamental constraint that defines sandstone acidizing is the **HF-carbonate incompatibility**: HF reacts with calcite (CaCO₃) and dolomite (CaMg(CO₃)₂) to produce **calcium fluoride (CaF₂)**, an extraordinarily insoluble precipitate that blocks pore throats and damages the very flow paths the treatment is meant to clean. Sandstone-acid treatment design is therefore primarily an exercise in **managing acid composition along the flow path** so that HF arrives at the silicate matrix only after every carbonate species in its path has been dissolved by the upstream HCl.

Where carbonate acidizing creates new flow paths (wormholes), sandstone acidizing enlarges existing ones. The design objective is not "how far does my acid penetrate?" — it is "how completely does my acid dissolve the damage minerals in the near-wellbore band where productivity loss is concentrated?" Typical effective stimulation distances are inches to a few feet — well inside the radius where damage is actually located.

This page covers the design framework, the chemistry stoichiometry, the reaction kinetics, the practical preflush/main/postflush sizing logic, and the operator-relevant common failure modes. The chemistry-family overview lives at [Matrix Acid Stimulation](matrix-acid-stimulation.md); the carbonate sister-page is [Carbonate Acidizing](carbonate-acidizing.md); the diversion problem (critical for any sandstone job over 30 ft of interval) is [Matrix Acid Diversion](matrix-acid-diversion.md).

## The Schechter-Gidley-Williams 3-stage framework

The 3-stage framework is the operator-canonical treatment architecture for sandstone matrix acidizing. It was codified by Williams, Gidley, and Schechter in *Acidizing Fundamentals* (SPE Monograph 6, 1979) — synthesising operator practice from the preceding decade — and has remained the default treatment shape for sandstone matrix-acid jobs ever since.

### Stage 1 — Preflush (HCl)

**Purpose**: Dissolve every carbonate mineral in the flow path that the upcoming HF would otherwise react with. Calcite cement, dolomite cement, calcite scale, residual carbonate from drilling fluid, all dissolved to soluble chloride salts and gaseous CO₂ before HF arrives.

**Composition**: Typically 5-15% HCl. Concentration depends on carbonate-mineral fraction (higher carbonate fraction → higher HCl concentration to dissolve it within reasonable contact time) and on temperature (higher temperature → faster spending → can use lower concentration).

**Volume**: 50-200 gal/ft of treated interval as a starting heuristic; volume scales with carbonate-mineral fraction. For a typical 5-10% carbonate-cement sandstone, 50-100 gal/ft of 7.5-15% HCl is a defensible starting point. The volume must be large enough that the HCl front actually reaches the design penetration distance, not just the wellbore-adjacent zone.

**What the preflush is NOT**: it is not a wellbore-cleanup step (that happens earlier with treated brine or fresh-water displacement). It is a formation-conditioning step whose entire purpose is to remove carbonate species from the future-mud-acid flow path.

### Stage 2 — Main treatment (HCl/HF mud acid)

**Purpose**: Dissolve damage minerals (silicates: quartz, feldspars, clays) in the near-wellbore band. The mud acid is the only stage in which HF is present, and it is the only stage that actually performs the silicate-dissolution stimulation work. Everything else exists to make this stage safe and effective.

**Composition**: The "regular" mud acid is **12-3** — 12% HCl + 3% HF. Reduced-HF variants for chlorite/zeolite-rich or HPHT formations include **9-1** (9% + 1%), **6-1.5** (6% + 1.5%), and **3-1.5** (3% + 1.5%) per Williams-Gidley-Schechter discussion. The HCl in mud acid serves two purposes: (a) it carries the HF (HF without HCl rapidly re-precipitates secondary fluorosilicates), and (b) it dissolves any residual carbonate that the preflush missed in irregular flow paths.

**Volume**: 50-150 gal/ft of treated interval. Smaller per-foot volumes than the preflush because the silicate-dissolution stoichiometry is unfavourable (HF consumes far more pore-volume per mole of silicate dissolved than HCl does per mole of carbonate). Larger per-foot volumes are unproductive because HF spends quickly on the available silicate surface area and the live-acid penetration distance is short.

**The dominant failure mode in this stage**: HF arrives at calcite/dolomite (because the preflush was undersized or because the formation contains an irregular carbonate streak) and produces CaF₂. The CaF₂ precipitate plugs the flow paths and the stimulation job leaves the formation in worse shape than it started. The mitigation is the postflush.

### Stage 3 — Postflush (HCl or ammonium chloride brine)

**Purpose**: Displace the spent-acid mud-acid front away from the wellbore before secondary fluorosilicate precipitation reactions complete, and re-condition the near-wellbore for production fluids.

**Composition**: Either dilute HCl (typically 3-5%) or ammonium chloride (NH₄Cl) brine. The choice depends on temperature and on the dominant clay species in the formation. NH₄Cl is preferred where clay-swelling or clay-mobilisation is a concern, because NH₄⁺ stabilises clays better than spent-acid ions during the rate-transient flowback.

**Volume**: At minimum, displacement volume to push the mud-acid front away from the wellbore (50-100 gal/ft as a heuristic; can be reduced when nitrogen lift is co-injected for fast flowback). Adequate postflush is essential — undersized postflush leaves spent acid in the near-wellbore where the secondary precipitation reactions damage the formation.

**Why this is non-negotiable**: The reaction products of HF with silicates are fluorosilicates that remain in solution **only while the pH is low**. As the spent acid spends further (or as the spent acid is diluted by formation water in the flowback), the pH rises and fluorosilicates begin to re-precipitate. If the spent acid is still in the near-wellbore when this happens, the precipitates plug the flow paths. The postflush displaces spent acid into a larger pore volume where the precipitates do less damage and are more readily produced back.

## HF reaction kinetics — what the design framework is built on

The Schechter-Gidley-Williams 3-stage framework exists because HF reaction kinetics with silicates and carbonates differ in two important ways:

### HF-carbonate reaction — fast and CaF₂-producing

HF reacts with calcite to produce calcium fluoride:

```
CaCO₃ + 2 HF → CaF₂ + H₂O + CO₂
```

The reaction is fast (carbonate dissolution by acid is generally transport-limited rather than reaction-rate-limited, and HF is no exception). The product CaF₂ has solubility-product around 4 × 10⁻¹¹ at 25 °C — for context, this is approximately six orders of magnitude less soluble than CaCO₃ in water. CaF₂ precipitates immediately upon formation and remains where it precipitates.

This is why HF cannot be allowed to contact carbonate in the formation matrix — the CaF₂ precipitate is a job-killer.

### HF-silicate reaction — slow, multi-stage, secondary-precipitate-producing

HF reacts with silicates (quartz, feldspar, clays) via complex multi-stage stoichiometry. The first-stage reaction with quartz is:

```
SiO₂ + 6 HF → H₂SiF₆ + 2 H₂O
```

The reaction is slow compared to HCl-carbonate reactions, primarily because silicate dissolution is reaction-rate-limited at the mineral surface (HF must adsorb, react, and the products must desorb). Reaction rate accelerates strongly with temperature.

The H₂SiF₆ product (hexafluorosilicic acid) is soluble in low-pH solution. As the acid spends and pH rises, fluorosilicates begin to react with cations in solution to produce **secondary precipitates** — most notably sodium hexafluorosilicate (Na₂SiF₆) when sodium is available, calcium hexafluorosilicate (CaSiF₆) when calcium is available, and potassium hexafluorosilicate (K₂SiF₆) when potassium is available. These secondary precipitates are highly insoluble and can plug pore throats far from where the original silicate reaction took place.

The postflush exists precisely to push spent acid into a larger pore volume before these secondary reactions complete.

### Feldspars and clays — practical complications

Feldspars react more rapidly than quartz with HF, and aluminum-bearing dissolution products (aluminum fluoride complexes) can re-precipitate as aluminum-fluoride scales if the postflush is inadequate. Clay reactions are even more complex — chlorite and zeolite groups in particular release iron and aluminum that re-precipitate in damaging forms.

The practical consequence for treatment design: **reduce HF concentration in clay-rich and chlorite/zeolite-rich formations**. The 6-1.5 and 3-1.5 mud-acid ratios exist for this reason. A lower HF concentration produces less aggressive silicate dissolution but also produces less aggressive secondary precipitation, and the net stimulation result is better than what 12-3 mud acid would deliver in the same formation.

### Tertiary reactions — fines mobilisation and gel formation

Even with optimal preflush and postflush, HF-silicate reactions destabilise the clay-bound near-wellbore framework. Fines that were held in place by clay-cement can be mobilised when the cement dissolves; these fines then migrate during flowback and can plug pore throats away from the treated zone. Clay-stabiliser additives (typically organic cationic polymers) in the mud acid attempt to manage this — partially effective.

## Treatment sizing — operator-facing heuristics

The 3-stage framework imposes three volume decisions on the operator. The empirical defaults are:

| Stage | Volume (gal/ft) | Composition |
|---|---|---|
| Preflush | 50-200 | 5-15% HCl (concentration scales with carbonate-mineral fraction) |
| Main treatment | 50-150 | 12-3 mud acid (standard); 9-1, 6-1.5, 3-1.5 for sensitive formations |
| Postflush | 50-100 | 3-5% HCl or NH₄Cl brine; volume floor = wellbore displacement |

For most field jobs, the preflush is the largest stage (most of the carbonate dissolution work is done in this stage), the main treatment is the most expensive stage (HF chemistry is expensive and HF additive packages are larger), and the postflush is the smallest stage (volume is set by displacement requirements, not by reaction kinetics).

Total per-foot volumes therefore typically fall in the 150-450 gal/ft range. A 50-ft interval might consume 7,500-22,500 gallons total acid plus comparable preflush plus comparable displacement — a single-day job, transportable in road-tanker volumes.

## Diversion is mandatory for any non-trivial interval

For intervals over approximately 30 ft (operator practice varies — some use a 50-ft threshold), unmodified acid placement is unacceptable because high-permeability streaks will consume the acid preferentially, leaving low-permeability damaged zones un-stimulated. Diversion is the operational discipline of forcing acid into the un-stimulated zones; in sandstone matrix acid the dominant diversion choices are:

- **Foam diversion** — nitrogen foam pre-injected or co-injected with the acid, providing apparent viscosity in the high-permeability streaks that diverts subsequent acid to lower-permeability zones
- **Ball sealers** — small spheres dropped or pumped that seat on perforations, diverting acid to un-sealed perforations
- **Mechanical isolation** — straddle packers, ball-activated sleeves, or coiled-tubing-conveyed isolation tools that physically isolate sub-intervals for stage-by-stage treatment

See [Matrix Acid Diversion](matrix-acid-diversion.md) for the full diversion-family catalogue and selection logic.

## Common failure modes

Operator-experience-driven failure-mode catalogue:

### 1. CaF₂ precipitation from inadequate preflush

The dominant in-class failure mode. Symptom: the job produces no productivity uplift, sometimes worse-than-pre-job production. Diagnosis: post-job well-test shows skin elevated above pre-job baseline. Cause: HF contacted carbonate in the formation matrix and produced CaF₂ that plugged the near-wellbore. Mitigation: increase preflush volume on the repeat job; if the formation has irregular carbonate streaks, consider alternating preflush-and-main-treatment stages to chase the carbonate front.

### 2. Secondary fluorosilicate precipitation from inadequate postflush

Second-most-common failure mode. Symptom: similar to CaF₂ — no uplift or worse-than-pre-job production. Diagnosis: post-job flowback samples contain visible fluorosilicate precipitates; produced-water analysis shows elevated silicate species at low pH. Mitigation: increase postflush volume; in repeat treatments, consider co-injecting nitrogen for accelerated post-job flowback.

### 3. Wrong mud-acid concentration for formation mineralogy

Symptom: the job dissolved the matrix but mobilised fines and chlorite-class precipitates that plugged the formation downstream. Diagnosis: post-job flowback samples contain visible fines and clay-class material; productivity uplift is short-lived. Mitigation: reduce HF concentration on repeat jobs (9-1 or 6-1.5 instead of 12-3); consider clay-stabiliser additive packages.

### 4. Inadequate diversion — high-perm streaks over-stimulated, damage-zone untreated

Symptom: total productivity uplift is modest despite well-designed chemistry; offset-well comparison shows the high-permeability zones over-producing relative to expectation. Diagnosis: post-job production logging (PLT) shows the bulk of inflow from a narrow high-permeability streak. Mitigation: implement diversion on repeat treatments; for difficult cases, switch to mechanical isolation and stage-by-stage treatment.

### 5. Iron-precipitation damage

Symptom: post-job production has elevated iron-content, iron-hydroxide flocs are visible in produced fluids, and productivity uplift fades within weeks. Diagnosis: tubular rust dissolved by live HCl during pumping was carried into the formation; as the acid spent and pH rose, iron(III) precipitated as iron hydroxide in the pore throats. Mitigation: aggressive wellbore cleanup before the job; iron-control additive (citric acid, erythorbic acid, EDTA) at concentrations matched to the expected tubular-iron loading.

### 6. Asphaltene destabilisation in asphaltene-class crudes

Symptom: post-job production is loaded with asphaltene precipitates; surface separators choke; downhole pump (if ESP) trips on intake-pressure spikes. Diagnosis: live acid destabilised asphaltene molecules in the crude; precipitated asphaltenes coated the near-wellbore and plugged flow paths. Mitigation: anti-sludge additive in the acid; in severe cases, switch from HCl to acetic acid (weaker, less destabilising); consider mutual-solvent (EGMBE) co-injection.

## Cross-domain interactions

- **Perforating** — overbalanced perforating produces a crushed-zone debris ring around each tunnel that contributes to post-completion skin; matrix-acid (with appropriate HF management) is the standard cleanup. Underbalanced perforating reduces crushed-zone severity but does not eliminate the need for matrix-acid cleanup in formations with measured drilling-fluid invasion damage. See [Perforating](perforating.md) and [Perforation Strategy](perforation-strategy.md).
- **Sand control** — sandstone-acid treatments on gravel-packed and frac-packed completions require special care: HF-class chemistries can degrade some screen alloys, and the increased rate-pressure transients during acid injection can disturb the gravel pack. The completion engineer and stimulation engineer must align on what mud-acid concentration and rate envelope are allowable. See [Sand Control](sand-control.md), [Gravel Packing](gravel-packing.md).
- **Carbonate acidizing distinction** — see [Carbonate Acidizing](carbonate-acidizing.md) for the sister chemistry. The lithology dispatch is at [Matrix Acid Stimulation](matrix-acid-stimulation.md).
- **Drilling-fluid invasion** — the invasion-depth measurement that drives perforation EHL selection also drives matrix-acid candidate-screening: if measured invasion is shallow (< 6 inches) and perforations are deep (> 12 inches EHL), the perforations already bypass the damage and matrix acid may not be needed. If invasion is deep or perforations are shallow, matrix acid is the standard recovery intervention.

## Cross-references

- [Matrix Acid Stimulation](matrix-acid-stimulation.md) — chemistry-family overview and lithology dispatch
- [Carbonate Acidizing](carbonate-acidizing.md) — carbonate sister-page (wormhole framework)
- [Matrix Acid Diversion](matrix-acid-diversion.md) — diversion families (foam, ball sealer, fiber, VES, mechanical)
- [Perforating](perforating.md), [Perforation Strategy](perforation-strategy.md) — placement and crushed-zone-cleanup coupling
- [Sand Control](sand-control.md), [Gravel Packing](gravel-packing.md) — completion-architecture constraints

## Public references

- **Williams, B. B., Gidley, J. L. & Schechter, R. S.** — *Acidizing Fundamentals* (SPE Monograph 6), Society of Petroleum Engineers, 1979. The foundational sandstone-acidizing reference; the 3-stage preflush/main/postflush framework originates here.
- **Schechter, R. S.** — *Oil Well Stimulation*, Prentice Hall 1992, ISBN 0-13-949786-2. Comprehensive matrix-acid textbook; widely used as a graduate-level reference and operator-training source.
- **Economides, M. J. & Nolte, K. G. (eds.)** — *Reservoir Stimulation*, 3rd Edition (SPE Monograph 17), Wiley 2000, ISBN 978-0-471-49192-7. Matrix-acid chapters synthesise sandstone and carbonate frameworks.
- **McLeod, H. O.** — "Matrix Acidizing," JPT 36(13), December 1984. Practitioner-classic field-design framework.
- **Crowe, C. W., McGowan, G. R. & Baranet, S. E.** — "Investigation of Retarded Acids Provides Better Understanding of Their Effectiveness," SPE Production Engineering 5(2), May 1990. Practitioner discussion of retarded-acid systems applicable to sandstone HPHT treatments.
- **Hill, A. D., Lindsay, D. M., Silberberg, I. H. & Schechter, R. S.** — "Theoretical and Experimental Studies of Sandstone Acidizing," SPE Journal 21(1), 1981. Reaction-kinetics framework for sandstone acidizing design.
- **Lyons, W. C. (ed.)** — *Standard Handbook of Petroleum and Natural Gas Engineering*, Elsevier (ISBN 978-0-7506-7785-1). Acidizing chapter.
- **SPE OnePetro sandstone-acidizing literature** — extensive corpus on mud-acid concentration selection, reaction-kinetics measurement, secondary-precipitation management.
