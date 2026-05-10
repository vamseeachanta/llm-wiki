---
title: "ASTM G129 — Standard Practice for Slow Strain Rate Testing to Evaluate the Susceptibility of Metallic Materials to Environmentally Assisted Cracking (bounded resolver)"
slug: astm-g129
tags: ["astm", "g-series", "ssrt", "slow-strain-rate", "scc", "eac", "hydrogen-embrittlement", "test-method", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g129
publisher: ASTM
revision: "G129-21 — publisher-current"
publisher_current_edition: "G129-21"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0129-21.html
public_url: https://www.astm.org/g0129-21.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G129 — Slow Strain Rate Testing to Evaluate the Susceptibility of Metallic Materials to Environmentally Assisted Cracking (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, strain-rate tables, ductility-loss formulas, or fractography reference reproductions are included.
> **code_id:** `astm-g129` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals, Subcommittee G01.06 — Stress-Corrosion Cracking) &nbsp;•&nbsp; **revision:** G129-21.

## Scope

ASTM G129 is a **dynamic-strain-rate test practice** that uses **slow-strain-rate tensile testing (SSRT)** in an aggressive environment to **evaluate the susceptibility of metallic materials to environmentally assisted cracking (EAC)**. EAC is the umbrella term covering stress-corrosion cracking (SCC), sulfide stress cracking (SSC), hydrogen embrittlement (HE), hydrogen-induced stress cracking (HISC), and stepwise / hydrogen-induced cracking (HIC) — all of which share dependence on a sustained tensile stress in a hostile environment.

The G129 protocol pulls a uniaxial tensile specimen at a constant cross-head displacement rate corresponding to a strain rate of typically **10⁻⁵ to 10⁻⁷ s⁻¹** (a small fraction of conventional tensile-test strain rates of ≈ 10⁻³ s⁻¹). The slow strain rate keeps the specimen under tensile loading long enough for environmental hydrogen ingress, anodic dissolution at slip steps, and crack-initiation kinetics to play out — mechanisms that are bypassed at conventional strain rates. The test produces stress-strain curves in the **inert environment (reference)** and in the **aggressive environment (test)**; the comparison reveals whether and how much the environment degrades ductility, ultimate tensile strength, time-to-failure, reduction-of-area at fracture, and post-failure-surface morphology.

G129 is **kinetically informative** — unlike screening practices ([[astm-g36]], [[astm-g30]] U-bend) that yield binary or ranking outcomes — making it the **service-life-relevant SCC/EAC test method** of the G-Series. Quantitative metrics include:

- **Time-to-failure ratio** (test environment / inert environment).
- **Ductility-loss ratio** (reduction of area, elongation; test / inert).
- **Fracture morphology** — fractographic SEM of the fracture surface for transgranular vs. intergranular crack-propagation morphology and brittle-vs-ductile mode classification.

## Revision history

- **1995 — Original G129 publication** as a slow-strain-rate testing practice within ASTM Committee G01. The protocol was developed during the 1980s-90s as a fast EAC-screening alternative to traditional months-long static SCC tests.
- **2006 / 2013 / 2021 revisions** — Periodic updates with strain-rate guidance refinement and cross-references to environment-specific test methods.
- **G129-21** — publisher-current edition.
- The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` may contain a G129 PDF; the parent source page ([og-standards-astm-g-series](../sources/og-standards-astm-g-series.md)) records ASTM G-Series presence.

## Key sections

The following are the test-method anchors that appear in the practice (consult the on-disk PDF for clause-exact text):

- **Apparatus** — slow-strain-rate tensile machine (motorized lead screw or servohydraulic) capable of crosshead rates corresponding to 10⁻⁵ to 10⁻⁷ s⁻¹; environmental cell sealing the gauge-length region; reference electrode and counter electrode for cathodically-charged variants; potentiostat for applied-potential testing.
- **Specimen geometry** — round or flat tensile specimens with conventional gauge-length to gauge-diameter ratio; surface finish to a specified grit; pre-test material conditioning recorded.
- **Test environment** — aggressive environment for the test specimen; inert reference environment (typically air or inert gas) for the reference specimen; same strain rate, gauge geometry, and temperature for both.
- **Strain-rate selection** — practice provides guidance on choosing strain rate for the EAC mechanism under study (10⁻⁶ s⁻¹ commonly used for room-temperature aqueous SCC; lower strain rates for hydrogen-charged tests).
- **Cathodic-charging variants** — applied-potential and pre-charged specimens for hydrogen-embrittlement screening per [[hydrogen-embrittlement]] mechanism testing.
- **Reporting** — stress-strain curves (test and reference), ductility-loss ratios, time-to-failure, fractographic SEM, environment composition and temperature, applied potential.

## Practitioner application

- **Sour-service-CRA SCC qualification** — SSRT under H2S-bearing solutions referenced via ISO 7539-7 (cited from [[iso-15156-3]] / [[ampp-mr-0175-pt3]]) for CRAs that fall outside the pre-qualified MR0175-3 envelopes.
- **HISC qualification of duplex / super-duplex CRAs under cathodic protection** — SSRT under cathodic polarization with hydrogen pre-charging; central to [[dnv-rp-f112]] HISC test programs for subsea-and-cathodically-protected equipment.
- **Hydrogen-embrittlement screening of high-strength steels** — SSRT under cathodic-charging or H2 gas-phase environments for fastener-grade and structural high-strength steels; [[hydrogen-embrittlement]] mechanism characterization.
- **Polythionic-acid SCC of sensitized austenitic stainless steels** — SSRT in dilute polythionic acid for sensitized-vs-solution-annealed comparison.
- **Refining-process CRA selection** — SSRT data feeds [[damage-mechanism-screening]] for sour-water-stripper, hydroprocessing-reactor-internals, and amine-unit material selection.
- **Service-life-extrapolation evidence** — SSRT data is the dominant input for fitness-assessment-route evidence under [[iso-15156-3]] for non-pre-listed materials.

## Industry adoption

G129 is the **dominant fast-screening EAC test method** in the corrosion-engineering community; it is the kinetic-counterpart to the static U-bend and bent-beam screening practices. Industry uptake is universal among CRA suppliers (ATI, Sandvik, VDM, Carpenter, Special Metals), oil-and-gas operators (Shell, BP, Chevron, ExxonMobil, Equinor), and offshore-engineering firms qualifying duplex and super-duplex CRAs for HISC under DNV-RP-F112. The protocol is also widely adopted in the hydrogen-economy and aerospace-fastener communities for HE qualification.

International parallel: **ISO 7539-7** (Slow Strain Rate Test) carries similar normative content; ISO 15156-3 / NACE MR0175-3 cite ISO 7539-7 in the fitness-assessment route for CRA SCC qualification. G129 and ISO 7539-7 are functionally interchangeable for most calc-citation purposes; specific projects may pin one or the other by jurisdiction.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g129` under `.claude/rules/calc-citation-contract.md`. W201 audit (iter-43) surfaced `astm-g129` as an unmatched slug from multiple cross-references in [[astm-g36]] (kinetic-counterpart bullet), [[stress-corrosion-cracking]] concept page (SSRT row in test-method table), [[hydrogen-embrittlement]] (HE-screening reference), and [[dnv-rp-f112]] (HISC qualification). The page anchors that link target without reproducing any clause text, strain-rate tables, ductility-loss formulas, or fractography references.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0129-21.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [[astm-g36]] — *Boiling Magnesium Chloride SCC Test* — sister Cl-SCC screening practice; G36 yields static-deformation ranking, G129 yields kinetic-and-ductility metrics.
- [[astm-g30]] — *U-Bend Stress-Corrosion Test Specimens* — static-deformation specimen practice; G129 is the dynamic-strain-rate complement.
- [[astm-g39]] — *Bent-Beam Stress-Corrosion Test Specimens* — static-deformation 4PBB practice; G129 is the dynamic-strain-rate complement.
- [[astm-g38]] — *C-Ring Stress-Corrosion Test Specimens* — static-deformation tube/ring practice; G129 is the dynamic-strain-rate complement.
- [[astm-g31]] — *Laboratory Immersion Corrosion Testing of Metals* — non-SCC immersion-testing companion practice.
- [[astm-g1]] — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens* — pre-and-post-exposure specimen-handling baseline.
- [[ampp-tm-0177]] — *Laboratory Testing of Metals for Resistance to SSC and SCC in H2S Environments* — sour-service test method; G129 SSRT data feeds the [[iso-15156-3]] / [[ampp-mr-0175-pt3]] fitness-assessment route.
- [[iso-15156-3]] / [[ampp-mr-0175-pt3]] — sour-service CRA qualification; SSRT data feeds the fitness-assessment route via ISO 7539-7 cross-link.
- [[ampp-mr-0175-pt2]] — sour-service carbon/low-alloy steel qualification; SSRT data feeds non-pre-listed material qualification.
- [[dnv-rp-f112]] — duplex/super-duplex stainless under cathodic protection; HISC qualification by SSRT-under-CP.
- [[stress-corrosion-cracking]] (concept) — primary consumer concept page; SSRT row in the test-method table.
- [[sour-service-materials]] (concept) — secondary consumer; SSRT is foundational to fitness-assessment-route evidence.
- [[hydrogen-embrittlement]] (concept) — HE/HISC mechanism family; SSRT is the dominant HE-screening test.
- [[cathodic-protection]] (concept) — HISC overlap; SSRT-under-CP characterizes susceptibility envelope.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
