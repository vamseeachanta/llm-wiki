---
title: "ASTM G31 — Laboratory Immersion Corrosion Testing of Metals"
slug: astm-g31
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g31
publisher: ASTM
revision: latest
tags:
  - astm
  - g-series
  - corrosion
  - mass-loss
  - immersion-test
  - lab-corrosion
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G31 — Standard Guide for Laboratory Immersion Corrosion Testing of Metals

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g31` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals, Subcommittee G01.05) &nbsp;•&nbsp; **revision:** latest publisher edition (the local on-disk corpus carries the G31-72 base practice with R99 and R04 reapprovals — see Edition history below; the publisher-current edition is later than R04 and was reissued as a Standard Guide).

## Scope

ASTM G31 prescribes the recommended **apparatus, specimen-handling protocol, exposure procedure, and result-evaluation framework** for laboratory immersion corrosion tests of metallic specimens in liquid environments — aqueous solutions, organic liquids, low-temperature melts, and mixed-phase systems. The test is the simplest and most widely used corrosion screen in the industry: prepare a coupon, weigh it, expose it to a controlled liquid for a controlled time at a controlled temperature, retrieve it, clean it, reweigh it, and convert the mass loss to a uniform-corrosion penetration rate.

G31 is a **companion standard to [astm-g1](astm-g1.md)**, not a replacement for it. The two standards split the workflow:

- **G1** owns specimen *preparation* before exposure and specimen *cleaning + mass-loss-to-rate conversion* after exposure (the chemistry and metallurgy of getting clean, well-characterized coupons in and out).
- **G31** owns the *exposure phase itself* — vessel design, solution makeup, support hardware, agitation, aeration, temperature control, exposure duration, and replicate count.

Together they define **the laboratory-coupon mass-loss method** that engineers use to screen material–environment compatibility before committing to full-scale field deployment, pilot loops, or autoclave programs. G31 results are used to:

1. **Rank candidate alloys** for service in a given process stream (e.g., refinery overhead condensate, amine-treating circuit, geothermal brine, sour-water stripper).
2. **Generate baseline uniform-corrosion rates** for material-selection diagrams and isocorrosion charts (e.g., the classic Hastelloy / Inconel / 316L / 825 isocorrosion plots in HCl, H2SO4, HF, and chloride brines).
3. **Provide a low-cost first screen** before committing to electrochemical (G3 / G5 / G59), stress-corrosion (G36 / G39 / G44), or full-pressure / full-temperature autoclave testing.
4. **Feed sour-service qualification packages** under NACE MR0175 / ISO 15156 — G31 mass-loss in H2S-bearing liquids is routinely run alongside AMPP (NACE) TM0177 SSC tests on the same heat of material.

The standard is explicitly a **guide**, not a pass/fail acceptance method: it specifies how to run the test rigorously and report the result, but it does not set acceptance limits. Acceptance criteria are the responsibility of the specifying body (project specification, materials standard, or end-user materials data sheet — e.g., NORSOK MDS, an oil-company materials spec, or an EPC contract).

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` holds **two G31 PDFs** corresponding to two reapproval issuances of the 1972 base practice:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G31-72 (R99) | `G_31_-_72_R99_RZMXLTCYUJK5.pdf` | 1 file | 1999 reapproval of the 1972 practice |
| G31-72 (R04) | `G_31_-_72_R04_RZMX.pdf` | 1 file | 2004 reapproval of the 1972 practice |
| G31 (current) | not on disk | — | The publisher-current edition was reissued as a **Standard Guide** (post-R04 cycle); calc-callers needing the current edition must obtain it from the ASTM catalog |

The publisher-catalog year-token sweep done for the [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) source page recorded G31 with **2 editions** in the catalog; that count matches the two file rows above. The G31 base practice has been remarkably stable — the 1972 procedural substrate has carried forward through multiple reapprovals with editorial-only changes — but the post-R04 reissuance promoted G31 from a *practice* to a *guide* (a status change ASTM uses to flag broadly applicable methodology rather than a tightly prescribed procedure).

## Key sections

The procedural anchors that define a G31-compliant immersion test (consult the on-disk PDFs for clause-exact text — this page records only the design-of-test substrate):

| Parameter | Value / specification |
|-----------|----------------------|
| Specimen mounting | **Inert non-conducting supports** — PTFE, glass, ceramic, or fluoropolymer-coated wire. Avoid any galvanic contact between specimen and support hardware (a common silent error that contaminates rate data with galvanic-couple corrosion). |
| Solution volume-to-area ratio | **≥ 40 mL/cm²** as the typical minimum (some texts cite the historical "20–40 mL/cm² minimum, 250 mL/cm² preferred" range) — chosen to keep solution chemistry near-constant during exposure as corrosion products accumulate and reactants deplete. |
| Solution refresh | **Closed (static) systems**: refresh on a schedule when solution depletion or product accumulation would shift the chemistry beyond the test envelope. **Open (flow-through / refluxing) systems**: continuous or scheduled make-up to hold composition. The standard explicitly addresses both. |
| Temperature control | Specified to within a tight tolerance (typically ± 1 °C) over the full exposure window; the test vessel must be able to hold the target temperature continuously, which often drives use of a refluxing flask, a glass autoclave, or a thermostatted bath. |
| Aeration vs. deaeration | Tester selects per the service simulated — **aerated** (open to atmosphere or actively sparged with air/O2) for cooling-water and topside-condensate simulations, **deaerated** (N2- or argon-sparged) for sour-service and pipeline-fluid simulations. The aeration regime must be reported with the result; oxygen has first-order influence on uniform-corrosion rate for most alloys. |
| Agitation regime | One of: **stagnant** (no agitation), **stirred** (magnetic stirrer or paddle at a specified rpm), or **gas-purged** (sparge ring delivering a controlled gas-phase composition simultaneously with mass transfer). The flow regime must be reported; agitation routinely changes uniform rates by 2–10× by altering the diffusion-boundary layer. |
| Exposure duration | Long enough that mass loss is large compared with weighing precision and short enough that solution chemistry and surface state remain representative. Typical screening exposures: **24–72 hours** for aggressive media, **168 hours (1 week)** to **720 hours (30 days)** for moderate media. The standard discourages extrapolating from short single-exposure runs and recommends **interval testing** (parallel coupons pulled at multiple time points) when rate-vs-time behavior is unknown. |
| Replicate count | **Minimum of 3 specimens per condition** (alloy × environment × temperature). Replicates are required to detect outlier behavior from local pitting, edge effects, or solution-handling errors. |
| Specimen identification | Each specimen carries a non-altering identifier (stamped, scribed clear of the exposed face, or fluoropolymer-tag-suspended) so that mass-loss data can be traced back to coupon-level metallurgical pedigree. |
| Edge effects | The standard recognizes that cut edges have different surface state from rolled / ground faces; surface-area accounting must include all exposed faces, and edge masking is permissible when justified. |

## Output

A G31-compliant test produces:

1. **Mass loss → uniform corrosion rate** per [astm-g1](astm-g1.md) §9 / §10 — converted to penetration rate (mils/yr or mm/yr) using the alloy density and exposed surface area. G1's mass-loss-to-rate equation is the canonical conversion; G31 supplies the mass-loss data, G1 supplies the arithmetic and the cleaning-procedure tables that the mass-loss number depends on.
2. **Visual + microscopic examination** per [[astm-g46]] — pitting depth distribution, pit count, crevice-attack rating, edge-attack vs. face-attack discrimination. A G31 test that reports only the average uniform rate without the G46 pit/crevice rating is incomplete: localized attack invalidates the uniform-rate interpretation.
3. **Supplementary electrochemical measurements on parallel specimens** — it is common practice to run [astm-g3](astm-g3.md) / G5 / G59 polarization or LPR measurements on a parallel coupon set in the same vessel to cross-check the mass-loss-derived rate against a Tafel- or polarization-resistance-derived rate. Disagreement between the two streams (sometimes by an order of magnitude) is a known signal of localized attack, scale formation, or non-Faradaic mass loss (mechanical erosion, dissolution of an alloying element).
4. **Reported metadata** — alloy heat ID, surface preparation, solution composition (as-mixed plus pre- and post-exposure analyses where applicable), temperature, aeration regime, agitation regime, exposure duration, replicate spread, and any cleaning-procedure mass-loss correction (per G1's reference cleaning-blank protocol).

The reported rate is treated as **a screening number with order-of-magnitude reliability for material ranking**, not as a design corrosion rate for thickness-allowance calculations. Design rates use field-loop data, pilot-plant data, or in-service inspection trends, and the laboratory G31 number provides the cross-check.

## Cross-references

- [astm-g1](astm-g1.md) — *Standard Practice for Preparing, Cleaning, and Evaluating Corrosion Test Specimens.* **Required companion**: G1 owns specimen prep, cleaning blanks, and mass-loss → rate conversion. A G31 result is uninterpretable without the G1 framework around it.
- [[astm-g46]] — *Standard Guide for Examination and Evaluation of Pitting Corrosion.* Required for the post-exposure visual and pit-rating workflow; without it, localized attack is silently rolled into the uniform rate.
- [astm-g3](astm-g3.md) — *Standard Practice for Conventions Applicable to Electrochemical Measurements in Corrosion Testing.* Sign and reporting conventions for the parallel-electrochemistry coupon set commonly run alongside G31.
- **ASTM G5** — *Standard Reference Test Method for Making Potentiodynamic Anodic Polarization Measurements.* The canonical Tafel-scan reference test, often co-run with G31 to cross-check the mass-loss-derived rate.
- **ASTM G59** — *Standard Test Method for Conducting Potentiodynamic Polarization Resistance Measurements.* LPR-cell rate measurement; routinely paired with G31 mass-loss for time-resolved rate-vs-exposure data.
- **ASTM G102** — *Standard Practice for Calculation of Corrosion Rates and Related Information from Electrochemical Measurements.* Converts G5 / G59 current density into a corrosion rate that is directly comparable to the G31 / G1 mass-loss rate.
- [astm-g48](astm-g48.md) — *Standard Test Methods for Pitting and Crevice Corrosion Resistance of Stainless Steels and Related Alloys by Use of Ferric Chloride Solution.* G48 is a **specialized variant of immersion testing** for CRA pitting/crevice screening with a fixed FeCl3 chemistry; G31 is the broader umbrella for any liquid environment.
- **ASTM G16** — *Standard Guide for Applying Statistics to Analysis of Corrosion Data.* The statistical framework that turns three-replicate G31 results into reportable confidence intervals.
- **NACE TM-0169 / ASTM G31 parallel scope** — NACE TM-0169 *Laboratory Corrosion Testing of Metals* covers parallel ground for the NACE / AMPP audience; many oil-company specs cite the two together or interchangeably for laboratory mass-loss qualification.
- **AMPP (NACE) TM0177** — Sulfide-stress-cracking laboratory test; G31 mass-loss is routinely run on companion specimens from the same heat as TM0177 SSC bars to bound the uniform-corrosion contribution to the SSC failure window.
- [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) / [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) — Sour-service materials selection. G31 mass-loss data populates the qualification dossier for carbon-steel and CRA selections under MR0175 / ISO 15156.
- Concept anchor: [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — landing page that names G31 as the **primary mass-loss-in-liquids method** alongside G1 (prep) and G102 (electrochemical conversion).
- Concept anchor: [sour-service-materials](../concepts/sour-service-materials.md) — names G1 / G31 as the mass-loss substrate referenced from NACE MR0175 / ISO 15156 / AMPP TM0177 sour-service qualifications.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md) — emit a `Citation(...)` whenever a calc module hard-codes a G31-derived screening rate, exposure protocol, or material-selection threshold.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the two-edition presence, the catalog file paths, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): https://www.astm.org/g0031.html (or the latest reapproval / guide-status listing on `astm.org`).
- On-disk raw PDFs (vendor-derivative, do not copy into git per spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_31_-_72_R99_RZMXLTCYUJK5.pdf`
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_31_-_72_R04_RZMX.pdf`
