---
title: "ASTM G1 — Preparing, Cleaning, and Evaluating Corrosion Test Specimens"
slug: astm-g1
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g1
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - mass-loss
  - specimen-prep
  - cleaning
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G1 — Standard Practice for Preparing, Cleaning, and Evaluating Corrosion Test Specimens

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g1` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals) &nbsp;•&nbsp; **revision:** latest publisher edition (current ASTM G1 carries the year-suffix and reapproval cycle posted at the publisher catalog; the local on-disk corpus runs G1-90(R99) and G1-03 — see Edition history below).

## Scope

ASTM G1 is the foundational ASTM-G corrosion practice covering the three workflow stages that bracket every metallic-coupon corrosion test:

1. **Specimen preparation** — sectioning, machining, identification, surface finishing, dimensioning, pre-test photographing, and pre-test weighing of metallic test coupons.
2. **Post-exposure cleaning** — chemical, electrolytic, and mechanical procedures for removing corrosion products from the exposed coupon without removing significant base metal, with a multi-cycle weight-loss extrapolation procedure that backs out cleaning-induced mass loss to recover the true exposure-induced mass loss.
3. **Evaluation** — converting the corrected mass loss to an engineering corrosion rate (mils per year, mm/y, μm/y, g/m²·d, mdd) using specimen density, exposed area, and exposure time; plus reporting requirements that make the result reproducible and defensible.

G1 is a **practice**, not a test method — it does not specify environment, temperature, duration, or acceptance criterion. It is the **method substrate** invoked by every weight-loss / lab-immersion / field-coupon corrosion test in the offshore and onshore oil-and-gas stack: laboratory immersion testing under [astm-g31](astm-g31.md), pitting and crevice screening under [astm-g48](astm-g48.md) (mass-loss reporting clause), atmospheric exposure under [[astm-g50]]/[[astm-g85]], sour-service mass-loss work coupled with NACE/AMPP MR0175 and TM0177, and field coupon programs run under NACE/AMPP SP0775. Every one of those callers cites G1 for **specimen prep, post-test cleaning, and corrosion-rate calculation** even when their own scope is the exposure protocol itself. This makes G1 the highest-traffic upstream node in the ASTM-G corrosion-method graph.

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **three G1 PDFs spanning two distinct editions** (the G1-90(R99) designation appears as two separately-hashed files — likely a re-scanned or differently-collated copy of the same edition). The parent source page records "G1 ×3" and lists G1 as a multi-edition code (3 revisions) warranting a per-revision history table:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G1-90 (Reapproved 1999) | `G_1_-_90_R99_RZETOTBSOTLFMQ_.pdf`, `G_1_-_90_R99_RZETUKVE.pdf` | 2 files | 1990 revision, reapproved 1999 (two catalog copies, distinct content hashes) |
| G1-03 | `G_1_-_03_RZE_.pdf` | 1 file | 2003 revision |
| G1 (current) | not on disk | — | The publisher-current ASTM G1 edition is later than 2003 (post-2003 reapproval cycles have been issued); calc-callers needing the current edition must obtain it from the ASTM catalog |

The on-disk three-file count matches the parent source-page tally for G1 exactly. Calc modules that hard-code G1-derived recipes or coefficients should record both the **edition** they sourced and the **clause/annex** in their `Citation(...)` payload, since the specific cleaning recipes evolve between revisions (annex tables receive incremental edits across reapprovals).

## Key sections

The following are the procedural anchors that recur across the G1 revisions on disk (consult the on-disk PDFs for clause-exact text — this page records only the design-of-test substrate):

**Specimen preparation**
- Sectioning and machining of coupons from the parent stock; control of cutting heat to avoid microstructural disturbance.
- Surface finish menu — common selections are wet-ground or wet-polished SiC paper at **240, 320, 400, or 600 grit**, with the as-machined / as-received finish also explicitly permitted when the test simulates an in-service surface. The choice of finish affects the result and must be reported.
- Identification (stamping, edge-notching, or scribing) placed where it will not affect the exposed area or trap solution.
- Dimensioning (length, width, thickness, hole diameter) to compute exposed surface area; pre-test photographing for baseline morphology.
- **Pre-test weighing** to a balance precision specified relative to the expected mass loss (ASTM G1 typically requires the balance precision to be at least 1 % of the anticipated mass loss).

**Post-exposure cleaning**
- Three cleaning modalities: **chemical** (immersion in a reagent that dissolves corrosion products but minimally attacks base metal; usually with an organic inhibitor), **electrolytic** (cathodic polarization in a specified electrolyte to reduce / detach corrosion product), **mechanical** (brushing, scraping, ultrasonic — typically used to dislodge loose product before chemical cleaning).
- **Multi-cycle weight-loss extrapolation** — the load-bearing G1 evaluation step. The cleaned coupon is repeatedly subjected to short cleaning cycles, weighed between cycles, and the cumulative mass-loss-vs.-cycle-count curve is **extrapolated back to t = 0 cycles** (the y-intercept). The intercept is taken as the true exposure-induced mass loss; the per-cycle slope is the parasitic base-metal removal rate of the cleaning method itself, which is subtracted out. This procedure is what makes G1-derived corrosion rates defensible against cleaning-bias attack from reviewers.

**Corrosion-rate calculation**
- The G1 corrosion-rate equation is canonical: **CR = (K · W) / (A · t · ρ)** where W is the corrected mass loss, A is the exposed area, t is the exposure time, ρ is the specimen density, and K is the unit-conversion constant chosen for the desired output units. Output choices include **mils per year (mpy), millimetres per year (mm/y), micrometres per year (μm/y)**, and gravimetric rates **g/m²·d** (= mdd, milligrams per decimeter squared per day) for applications where the rate is reported by mass flux rather than penetration depth. The K-constant table in G1 carries the unit conversions for each combination.

**Reporting**
- Required reporting: alloy designation and heat / lot, surface finish, specimen dimensions and exposed area, exposure environment, duration, temperature, pre- and post-test masses, cleaning method (annex reference), number of cleaning cycles, extrapolated corrected mass loss, calculated corrosion rate with units, and any photographs or pit-depth measurements. Companion-page guidance for pit examination flows in via [astm-g46](astm-g46.md).

## Cleaning method tables

G1 carries a set of **annex tables** that prescribe specific chemical and electrolytic cleaning recipes per metal class. The following table is a metal-class roadmap of the recipe categories — **consult the relevant G1 annex for the exact concentrations, temperatures, and exposure times** (those clause-specific details are not reproduced here per the metadata-only extraction policy):

| Metal class | Typical cleaning solution (G1 annex category) |
|-------------|----------------------------------------------|
| Carbon and low-alloy steel | Inhibited hydrochloric acid (HCl); **Clarke solution** (HCl + stannous chloride + antimony trioxide) for tenacious oxide |
| Stainless steel | Nitric acid (HNO3); HNO3 + hydrofluoric acid (HF) at G1 §C.3.5; oxidizing-acid passivation-style chemistry |
| Aluminum and aluminum alloys | HNO3-based (concentrated nitric); chromic acid + phosphoric acid blends in older revisions |
| Copper and copper alloys | Sulfuric acid (H2SO4) with **thiourea inhibitor**; sometimes HCl-based for heavily oxidized surfaces |
| Lead and lead alloys | **Ammonium acetate** (CH3COONH4); avoid acidic chemistries that aggressively attack lead |
| Magnesium and magnesium alloys | Chromate solution (chromic acid based); ethylene-glycol / silver-nitrate variants in some revisions |
| Nickel and Ni-Cr / Ni-Cr-Mo alloys | HCl with organic inhibitor (e.g., hexamethylenetetramine); HNO3 for some grades |
| Titanium and titanium alloys | HNO3 / HF blends at controlled ratios to avoid hydride pickup |
| Zinc and zinc alloys | Glycine / ammonium chloride; chromate-free acidic cleans |

The G1 annex also gives **electrolytic cleaning recipes** for several of the above classes (cathodic cleaning in dilute sulfuric acid with an organic inhibitor is a common workhorse for steel) plus **mechanical cleaning** guidance (ultrasonic, soft brush, scraping). The multi-cycle weight-loss extrapolation procedure described under "Key sections" applies to **all three modalities** and is what isolates the exposure-induced mass loss from the cleaning-induced parasitic loss.

## Cross-references

- [astm-g31](astm-g31.md) — *Standard Guide for Laboratory Immersion Corrosion Testing of Metals.* The primary protocol consumer of G1 — G31 specifies the immersion exposure (vessel, solution, agitation, aeration, duration, temperature) and explicitly delegates specimen prep, cleaning, and corrosion-rate calculation to G1.
- [astm-g46](astm-g46.md) — *Standard Guide for Examination and Evaluation of Pitting Corrosion.* G1 reporting requirements pull pit-depth and pit-density terminology and rating charts from G46 whenever pitting accompanies the mass-loss result.
- [astm-g3](astm-g3.md) — *Standard Practice for Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Sign-convention and reporting complement to G1 — G1 covers the gravimetric path to corrosion rate, G3 covers the electrochemical-measurement reporting conventions.
- [astm-g102](astm-g102.md) — *Standard Practice for Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* Complement to G1 for the electrochemical pathway: where G1 converts mass loss to corrosion rate via Faraday-equivalent gravimetry, G102 converts measured polarization-derived current density (from [astm-g5](astm-g5.md)/[astm-g59](astm-g59.md)) to the same rate units. A complete corrosion-rate cross-check report typically reports both the G1-derived gravimetric rate and the G102-derived electrochemical rate and compares the two.
- [astm-g48](astm-g48.md) — *Pitting and Crevice Corrosion Tests in FeCl3.* G48 mass-loss reporting (Methods A, B, and the CPT/CCT methods) flows through the G1 cleaning + extrapolation + corrosion-rate machinery.
- [ampp-sp0775](ampp-sp0775.md) / NACE SP0775 — *Preparation, Installation, Analysis, and Interpretation of Corrosion Coupons in Oilfield Operations.* The field-coupon counterpart to G1's lab-coupon practice; SP0775 prescribes the operational deployment (coupon racks, retrieval, holders) and points at G1 for the lab-side cleaning and evaluation. SP0775 represents the **online / in-service-monitoring paradigm** alternative to lab-coupon testing — both paradigms ultimately converge on a G1-style mass-loss-to-rate calculation.
- [api-rp-571](api-rp-571.md) — *Damage Mechanisms Affecting Fixed Equipment in the Refining Industry.* Provides the damage-mechanism and metal-class context (which alloys see which corrosion mechanisms in which service environments) that informs the choice of G1 cleaning annex when post-test cleaning a field-retrieved coupon or component.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that forward-references G1 as the **mass-loss method primary** and G102 as the electrochemical-measurement counterpart.
- Concept anchor: [sour-service-materials](../concepts/sour-service-materials.md) — anchors G1 + G31 mass-loss methods inside the NACE MR0175 / ISO 15156 / AMPP TM0177 sour-service qualification stack.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G1-derived cleaning recipe, K-constant, or extrapolation coefficient, recording both the edition (e.g., G1-03) and the clause/annex (e.g., Annex A1 §A1.1 for steel chemical cleaning).

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the three-file G1 presence ("G1 ×3"), the multi-edition status (G1 listed in the edition-history index with 3 revisions), the catalog file paths, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0001-03r17e01.html (or the latest reapproval listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, not copied into this repo per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_1_-_90_R99_RZETOTBSOTLFMQ_.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_1_-_90_R99_RZETUKVE.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_1_-_03_RZE_.pdf`
