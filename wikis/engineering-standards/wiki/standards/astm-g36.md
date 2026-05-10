---
title: "ASTM G36 — Boiling Magnesium Chloride SCC Test"
slug: astm-g36
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
code_id: astm-g36
publisher: ASTM
revision: G36-94 (R2000) — latest edition present in local catalog
tags:
  - astm
  - g-series
  - scc
  - chloride-scc
  - austenitic-stainless
  - screening-test
sources:
  - ../sources/og-standards-astm-g-series.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# ASTM G36 — Standard Practice for Evaluating Stress-Corrosion-Cracking Resistance of Metals and Alloys in a Boiling Magnesium Chloride Solution

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description.
> **code_id:** `astm-g36` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals, Subcommittee G01.06 — Stress-Corrosion Cracking) &nbsp;•&nbsp; **revision:** publisher-current edition is the post-2000 reapproval cycle of G36-94 (the local on-disk corpus carries G36-94 R(2000) — see Edition history below).

## Scope

ASTM G36 is a **screening practice** for ranking the susceptibility of metallic materials — primarily austenitic stainless steels and related corrosion-resistant alloys (CRAs) — to **chloride stress-corrosion cracking (Cl-SCC)**. The test exposes a stressed specimen to **boiling 42% (by mass) magnesium chloride solution at the natural boiling point of ≈ 155 °C (≈ 311 °F)** at atmospheric pressure, under reflux. The boiling MgCl2 environment is among the most aggressive Cl-SCC accelerants available in a laboratory at 1 atm — initiation and propagation of transgranular Cl-SCC in 18Cr-8Ni austenitic grades is observed within hours, an acceleration of roughly **10²–10³×** vs. typical chloride-rich service environments (cooling water, refinery overheads, marine atmospheres).

Because the acceleration is so severe, **G36 is explicitly a pass/fail / ranking screen, not a service-life predictor**. The output is binary (cracking observed / not observed at a fixed exposure time) and a comparative time-to-cracking against reference materials, **not** a kinetic constant that can be extrapolated to service. For service-life-relevant kinetics under prescribed strain rate, ASTM G129 (slow-strain-rate, SSRT) is the companion practice; for milder Cl-SCC ranking closer to atmospheric service, ASTM G44 (alternate immersion in 3.5% NaCl) is the milder-environment counterpart.

The practice is **not** a sour-service qualification: H2S-bearing environments require [ampp-tm-0177](ampp-tm-0177.md) (NACE TM0177) for SSC and the acceptance framework of [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) (ISO 15156-3 / NACE MR0175-3) for CRAs. G36 likewise does not qualify duplex stainless steels for hydrogen-induced stress cracking under cathodic protection — that envelope is governed by [dnv-rp-f112](dnv-rp-f112.md) protocols.

## Edition history

The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` contains a **single G36 edition**:

| Edition | Filename (catalog) | Catalog presence | Notes |
|---------|-------------------|------------------|-------|
| G36-94 (R2000) | `G_36_-_94_R00_RZM2.pdf` | 1 file | 1994 revision, reapproved 2000 (the `R00` token in the filename denotes the reapproval year) |
| G36 (current) | not on disk | — | The publisher catalog publishes the current G36 reapproval at `astm.org`; the post-R(2000) reapproval cycle continues without substantive technical revision based on the parent source-page year-token survey ([og-standards-astm-g-series](../sources/og-standards-astm-g-series.md)) |

The parent ASTM G-Series source page recorded G36 with **1 edition** in the local catalog, matching the single row above. G36 has had relatively few technical revisions since 1994 — the practice description is mature and the reagent-grade reference solution (42% MgCl2) has not changed.

## Key sections

The following are the procedural anchors that appear in the practice (consult the on-disk PDF for clause-exact text — this page records only the design-of-test substrate):

| Section | Specification |
|---------|---------------|
| **Apparatus** | Glass reflux flask (typically a Erlenmeyer or round-bottom flask with a vertical Allihn-type or Liebig water-cooled condenser), boiling chips, electric heating mantle. The condenser returns water vapor to the flask, holding solution composition near-constant at the equilibrium boiling point. Solution depth and flask geometry are specified to keep the specimen fully immersed throughout the exposure. |
| **Test solution** | **42 ± 1 % w/w MgCl2 · 6H2O** in reagent water, prepared from ACS-grade magnesium chloride hexahydrate. Boiling point at this composition is **≈ 155 °C** at 1 atm and is verified at the start of each test by thermometer reading on the refluxing solution. Boiling-point depression / elevation in service-water analogs (e.g., 5–10% NaCl at 100 °C) is the principal reason G36 acceleration is so much higher than service. |
| **Specimen geometry** | The practice itself does not mandate one geometry; it cross-references the established stressed-specimen base methods so the user picks per the alloy product form: **U-bend per [astm-g30](astm-g30.md)** (sheet/plate), **C-ring per [astm-g38](astm-g38.md)** (tube/ring product), **bent-beam (4-point) per [astm-g39](astm-g39.md)** (sheet/plate), or pre-cracked specimens for fracture-mechanics-style testing. Surface finish is typically wet-ground to 600-grit SiC immediately before exposure; descaling and welding history is recorded because both materially shift Cl-SCC initiation. |
| **Stress level** | Set by the chosen base-method specimen (e.g., a U-bend bent to ~180° with the deformation lying above proof; a C-ring stressed to a target outer-fiber stress at or above 0.9 σ_y). G36 itself does not prescribe a target stress — the base-method (G30/G38/G39) does. |
| **Exposure duration** | **Variable, application-driven**: 24 h is a common short screen for highly susceptible 18Cr-8Ni grades (Type 304/316), 100–200 h is typical for mid-tier alloys (e.g., Type 317L, 904L), and 500–1000 h+ for high-Mo and Ni-base CRAs (Alloy 825, Alloy 625, Alloy C-276). The practice explicitly anticipates re-inspecting at staged intervals to record **time-to-first-cracking** against a reference. |
| **Inspection** | **Visual** at staged intervals (using low-power stereomicroscopy) for surface crack indications, followed by **metallographic cross-sectioning** of representative specimens to confirm cracks are SCC (transgranular, branched morphology in austenitic grades) and to record crack count and **maximum crack depth**. Mass loss is recorded but is not a primary acceptance metric — Cl-SCC produces little mass change. |
| **Acceptance / reporting** | Binary at a fixed exposure time (cracking observed / not observed) and/or **time-to-first-cracking** vs. reference materials run in the same flask. The practice does not define numeric pass thresholds — those are set by the **specifying body** (project specification, materials standard, or end-user specification). |

The boiling-MgCl2 environment is intentionally severe: nearly all standard 18Cr-8Ni austenitic stainless steels (Type 304, 304L, 316, 316L) **fail** within 1–24 h of exposure. The test's discriminating power lies in the **mid-range** alloys (high-Mo super-austenitics, lean duplexes, mid-tier nickel-bases) where time-to-cracking spreads over orders of magnitude.

## When G36 applies

- **Alloy screening for Cl-SCC resistance during materials selection** for chloride-rich service:
  - Cooling-water heat-exchanger tube bundles (open-loop seawater, brackish water, treated cooling water with chloride concentration >50 ppm).
  - Marine seawater piping and topsides chloride-exposed components on offshore platforms (FPSO, MODU, fixed jackets).
  - Refinery overhead condensers and stripper-overhead piping where chloride salts deposit and concentrate during shutdowns.
  - Pulp-and-paper digester components and chemical-industry process vessels handling chloride-contaminated streams.
- **Comparative ranking** of candidate alloys against a reference (commonly Type 304 / Type 316 as the lower bound and Alloy 600 / Alloy 825 / Alloy 625 as the upper bound).
- **Welding-procedure / heat-treatment qualification** evidence — a sensitized austenitic weldment vs. a solution-annealed parent comparison reveals heat-affected-zone susceptibility.
- **Surface-finish / cold-work studies** — boiling MgCl2 amplifies the residual-stress contribution of cold work and surface roughness, making it a sensitive probe for fabrication-route qualification.

## When G36 does NOT apply

- **Service-life prediction.** G36 is a screening / ranking practice. The 10²–10³× acceleration of boiling 42% MgCl2 vs. service environments is non-linear in stress, temperature, and chloride activity, so time-to-cracking in G36 cannot be back-calculated to a service crack-initiation time. Use **slow-strain-rate testing per [astm-g129](astm-g129.md)** for service-life-relevant kinetics.
- **Sour-service CRA qualification.** Materials destined for H2S-bearing service must be qualified per [ampp-tm-0177](ampp-tm-0177.md) (Method A tensile, B beam, C C-ring, D DCB) and accepted under [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) / ISO 15156-3. G36 cracking results do not translate into MR0175 acceptability and are not accepted as substitute evidence.
- **Hydrogen-induced cracking (HIC) and stepwise cracking in carbon and low-alloy steels.** Use [ampp-tm-0284](ampp-tm-0284.md) (NACE TM0284) for HIC; G36 does not exercise the H-charging and stepwise-cracking failure mode.
- **Hydrogen-induced stress cracking (HISC) of duplex stainless steels under cathodic protection.** The HISC envelope is governed by [dnv-rp-f112](dnv-rp-f112.md) design protocols and slow-strain-rate qualification under cathodic polarization, not by boiling MgCl2.
- **Atmospheric / outdoor Cl-SCC ranking under near-service conditions.** For the milder environment closer to coastal-atmospheric exposure, use **alternate-immersion in 3.5% NaCl per ASTM G44**.
- **Pitting and crevice corrosion ranking.** G36 produces some pitting in the most susceptible grades but is not designed to discriminate pitting/crevice resistance — use [astm-g48](astm-g48.md) in ferric chloride for that envelope.

## Cross-references

- [astm-g30](astm-g30.md) — *Standard Practice for Making and Using U-Bend Stress-Corrosion Test Specimens.* Common specimen geometry referenced from G36 for sheet/plate product forms.
- [astm-g38](astm-g38.md) — *Standard Practice for Making and Using C-Ring Stress-Corrosion Test Specimens.* Common specimen geometry referenced from G36 for tube/ring product forms.
- [astm-g39](astm-g39.md) — *Standard Practice for Preparation and Use of Bent-Beam Stress-Corrosion Test Specimens.* Common specimen geometry referenced from G36 for sheet/plate; 4-point loading variants also widely used.
- [astm-g44](astm-g44.md) — *Standard Practice for Exposure of Metals and Alloys by Alternate Immersion in Neutral 3.5% Sodium Chloride Solution.* The **milder** Cl-SCC environment closer to marine-atmospheric service; complementary to G36.
- [astm-g47](astm-g47.md) — *Standard Test Method for Determining Susceptibility to Stress-Corrosion Cracking of 2XXX and 7XXX Aluminum Alloy Products.* Aluminum-alloy SCC counterpart; G36's MgCl2 chemistry is generally not used for aluminum alloys (which are tested in chromate-chloride environments per G47 / G64).
- [astm-g64](astm-g64.md) — *Standard Classification of Resistance to Stress-Corrosion Cracking of Heat-Treatable Aluminum Alloys.* Companion classification standard to G47 for Al-alloy SCC ranking.
- [astm-g123](astm-g123.md) — *Standard Test Method for Evaluating Stress-Corrosion Cracking of Stainless Alloys with Different Nickel Content in Boiling Acidified Sodium Chloride Solution.* The **boiling-NaCl alternative chemistry** for ranking SCC in higher-nickel austenitic and Ni-base alloys (G36's MgCl2 is so severe it saturates discrimination among high-Ni alloys; G123 was developed to spread the response in that regime).
- [astm-g129](astm-g129.md) — *Standard Practice for Slow Strain Rate Testing to Evaluate the Susceptibility of Metallic Materials to Environmentally Assisted Cracking.* The **service-life-relevant** kinetic counterpart; used when G36 ranking must be supplemented by strain-rate-resolved data.
- [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) (alias [iso-15156-3](iso-15156-3.md) / NACE MR0175-3) — sour-service CRA qualification framework. **Complementary, non-overlapping** with G36: sour-service requires H2S-bearing test environments (TM0177), not boiling MgCl2.
- [ampp-tm-0177](ampp-tm-0177.md) — *Laboratory Testing of Metals for Resistance to Sulfide Stress Cracking and Stress Corrosion Cracking in H2S Environments.* The sour-service SCC test method; G36 does not substitute.
- [dnv-rp-f112](dnv-rp-f112.md) — *Design of Duplex Stainless Steel Subsea Equipment Exposed to Cathodic Protection.* HISC-under-CP design envelope; G36 does not address this failure mode.
- Concept anchor: [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) — landing page for the SCC test-method cluster (G36, G38, G39, G44, G47, G64, G123, G129); G36 is the **primary Cl-SCC screening test** referenced from this concept page.
- Concept anchor: [sour-service-materials](../concepts/sour-service-materials.md) — explicit non-applicability boundary for G36; sour-service CRA selection cites MR0175-3, not G36.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes a G36-derived ranking, reference time-to-cracking, or pass/fail acceptance temperature.

## Sources

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-Series slice of the local catalog; records the single-edition G36 presence, the catalog file path, and the metadata-only extraction policy that scopes this standards page.
- Publisher catalog (current edition for purchase, registration required): `https://www.astm.org/g0036-94r18.html` (or the latest reapproval listing on `astm.org`).
- On-disk raw PDF (vendor-derivative, **not copied into this repo** per llm-wiki spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/ASTM/G-Series/G_36_-_94_R00_RZM2.pdf`
