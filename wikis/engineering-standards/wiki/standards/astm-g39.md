---
title: "ASTM G39 — Standard Practice for Preparation and Use of Bent-Beam Stress-Corrosion Test Specimens (bounded resolver)"
slug: astm-g39
tags: ["astm", "g-series", "scc", "bent-beam", "four-point", "stress-corrosion", "test-method", "specimen-geometry", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g39
publisher: ASTM
revision: "G39-99 (R2021) — publisher-current"
publisher_current_edition: "G39-99 (R2021)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0039-99r21.html
public_url: https://www.astm.org/g0039-99r21.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G39 — Standard Practice for Preparation and Use of Bent-Beam Stress-Corrosion Test Specimens (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, fixture geometry tables, stress formulas, or photographic reference reproductions are included.
> **code_id:** `astm-g39` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals, Subcommittee G01.06 — Stress-Corrosion Cracking) &nbsp;•&nbsp; **revision:** G39-99 reapproved most recently as G39-99(2021).

## Scope

ASTM G39 is a **specimen-preparation practice** that defines fixturing, stressing, and conditioning conventions for **bent-beam stress-corrosion-cracking (SCC) test specimens**, with primary emphasis on the **four-point bent-beam (4PBB) geometry**. The 4PBB specimen is a flat strip or rectangular bar held in a fixture under inner-load-point and outer-support-point loading; the geometry produces a region of **uniform bending moment** between the inner load points where the outer-fiber tensile stress is approximately constant and analytically tractable. The fixture-imposed deflection sets the outer-fiber stress, and the deflected specimen is then exposed to the test environment.

G39 is **explicitly a specimen-preparation practice, not a test method**: it provides the specimen recipe but does not specify the test environment, exposure duration, inspection schedule, or pass/fail criteria. The specifying test method ([astm-g36](astm-g36.md) for boiling MgCl2 Cl-SCC, [[astm-g44]] for 3.5% NaCl alternate immersion, [ampp-tm-0177](ampp-tm-0177.md) for sour-service SSC, ISO 7539-2 internationally) supplies those parameters. G39 is the dominant sheet/plate **bent-beam specimen-preparation reference** alongside [astm-g30](astm-g30.md) (U-bend) and [[astm-g38]] (C-ring) in the ASTM G-Series specimen-geometry triad.

The 4PBB geometry is a **constant-deformation** specimen (the deflection is fixture-imposed and held), but unlike the U-bend's plastic-bend regime, the 4PBB outer-fiber stress is typically held in the elastic regime, often at a target outer-fiber stress at or above 0.9 σ_y but below the proof. This makes the 4PBB the **preferred geometry for SCC threshold-stress determination** — sequentially stressed specimens at varying load levels can bound the threshold stress σ_SCC for a given environment. G39 also covers two-point and three-point bent-beam variants for special applications.

## Revision history

- **1973 — Original G39 publication** as the bent-beam specimen-preparation practice within ASTM Committee G01.
- **1999 — Revision** to G39-99; the modern technical baseline. Reapproved without substantive technical change in subsequent cycles.
- **G39-99 (R2011) and G39-99 (R2021)** — sequential reapproval cycles; the practice description is mature.
- The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` may contain a G39 PDF; the parent source page ([og-standards-astm-g-series](../sources/og-standards-astm-g-series.md)) records ASTM G-Series presence.

## Key sections

The following are the specimen-preparation anchors that appear in the practice (consult the on-disk PDF for clause-exact text):

- **Apparatus and fixturing** — four-point bend fixtures with adjustable inner-load and outer-support spans, locking screws to hold the deflected position, and electrically-isolating insulation between fixture and specimen.
- **Specimen geometry** — strip dimensions (length, width, thickness), inner span, outer span, target outer-fiber stress.
- **Material conditioning** — heat-treatment condition recording, surface finish (typically wet-ground to a specified grit immediately before exposure), descaling, welding history.
- **Stressing procedure** — slow elastic deflection to the target deflection, locking against the fixture, and verification of imposed strain via strain gauge or analytical formula.
- **Stress estimation** — beam-theory formulas relating fixture geometry, deflection, and outer-fiber stress for the linear-elastic range; corrections for the elastic-plastic transition near σ_y.
- **Identification, handling, and storage** — pre-exposure documentation requirements.
- **Reporting** — specimen-preparation provenance and target stress level recorded alongside test results.

## Practitioner application

- **SCC threshold-stress determination** — sequential 4PBB tests at varying outer-fiber stress to bracket σ_SCC for a given material-environment pair.
- **Cl-SCC ranking of austenitic stainless steels** — 4PBB specimens in boiling MgCl2 ([astm-g36](astm-g36.md)) for elastic-regime ranking, complementary to plastic-regime U-bends.
- **Sour-service-CRA SSC qualification** — Method-B-class bent-beam variants under [ampp-tm-0177](ampp-tm-0177.md) for [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) / [iso-15156-3](iso-15156-3.md) CRA acceptance.
- **Welding-procedure SCC qualification** — sensitized-vs-solution-annealed weldment comparison; 4PBB specimens spanning weldment, HAZ, and parent-metal regions for [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md).
- **Heat-affected-zone (HAZ) SCC** — 4PBB specimens with a transverse weld in the uniform-moment region probe HAZ susceptibility to SCC.
- **Aluminum-alloy SCC** — ASTM G47 and G64 reference G39 bent-beam geometries for 2XXX and 7XXX heat-treatable aluminum alloy SCC ranking.

## Industry adoption

G39 is the **default bent-beam specimen-preparation reference** for SCC testing across the corrosion-engineering community: refining, oil-and-gas, marine, power, and chemical-process. The 4PBB geometry is preferred over the U-bend and C-ring when an analytically tractable, elastic-regime, threshold-stress-bracketing test program is required. The practice is referenced from virtually every SCC environment-specific test method that uses a bent-beam geometry, and is the geometry of choice in test programs that must cover both elastic and plastic stress regimes (with U-bend covering the plastic-bend baseline). Its mature 1973/1999 baseline means industrial test labs treat G39 as foundational.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g39` under `.claude/rules/calc-citation-contract.md`. W201 audit (iter-43) surfaced `astm-g39` as an unmatched slug from multiple cross-references in [astm-g36](astm-g36.md) and the [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) concept page (table of SCC test specimen geometries; row "Bent-beam (any SCC environment) | ASTM G39"). The page anchors that link target without reproducing any clause text, fixture-geometry tables, or stress formulas.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0039-99r21.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [astm-g36](astm-g36.md) — *Boiling Magnesium Chloride SCC Test* — primary consumer test method that invokes G39 bent-beam geometry for elastic-regime Cl-SCC ranking of austenitic stainless steels.
- [astm-g30](astm-g30.md) — *U-Bend Stress-Corrosion Test Specimens* — sister specimen-preparation practice for the plastic-bend U-bend geometry; complementary to G39's elastic-regime bent-beam.
- [[astm-g38]] — *C-Ring Stress-Corrosion Test Specimens* — sister specimen-preparation practice for tube/ring product forms.
- [astm-g129](astm-g129.md) — *Slow Strain Rate Testing* — kinetic-counterpart test method; G39 specimens are static-deformation, G129 specimens are dynamic-strain-rate.
- [astm-g31](astm-g31.md) — *Laboratory Immersion Corrosion Testing of Metals* — non-SCC immersion-testing companion practice.
- [astm-g1](astm-g1.md) — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens* — pre-and-post-exposure specimen-handling baseline; cited from G39.
- [ampp-tm-0177](ampp-tm-0177.md) — *Laboratory Testing of Metals for Resistance to SSC and SCC in H2S Environments* — sour-service SCC test method that references bent-beam geometries for [ampp-mr-0175-pt3](ampp-mr-0175-pt3.md) / [iso-15156-3](iso-15156-3.md) CRA acceptance and [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) carbon/low-alloy steel acceptance.
- [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) — Part 2 carbon/low-alloy steel sour-service qualification; consumer of bent-beam SSC test data.
- [stress-corrosion-cracking](../concepts/stress-corrosion-cracking.md) (concept) — primary consumer concept page; bent-beam geometry anchors the SCC test-method ladder.
- [sour-service-materials](../concepts/sour-service-materials.md) (concept) — secondary consumer; bent-beam specimens are routine in sour-service qualification.
- [welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md) (concept) — HAZ SCC characterization uses 4PBB specimens spanning weldment regions.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
