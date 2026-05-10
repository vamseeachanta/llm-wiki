---
title: "ASTM G30 — Standard Practice for Making and Using U-Bend Stress-Corrosion Test Specimens (bounded resolver)"
slug: astm-g30
tags: ["astm", "g-series", "scc", "u-bend", "stress-corrosion", "test-method", "specimen-geometry", "metadata-only"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: astm-g30
publisher: ASTM
revision: "G30-97 (R2016) — publisher-current"
publisher_current_edition: "G30-97 (R2016)"
jurisdiction: "ASTM jurisdiction (US-origin, global adoption)"
instrument_type: test-method
supersedes: None
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-astm-g-series.md
  - https://www.astm.org/g0030-97r16.html
public_url: https://www.astm.org/g0030-97r16.html
publisher_catalog_url: https://www.astm.org/
---

# ASTM G30 — Standard Practice for Making and Using U-Bend Stress-Corrosion Test Specimens (bounded resolver)

> Bounded metadata-only standards page. Per llm-wiki spinout governance (2026-05-05), vendor PDFs are not copied into this repo; this page records only publisher facts and a domain-knowledge scope description. No clause text, fixture geometry tables, stress formulas, or photographic reference reproductions are included.
> **code_id:** `astm-g30` &nbsp;•&nbsp; **publisher:** ASTM International (Committee G01 — Corrosion of Metals, Subcommittee G01.06 — Stress-Corrosion Cracking) &nbsp;•&nbsp; **revision:** G30-97 reapproved most recently as G30-97(2016).

## Scope

ASTM G30 is a **specimen-preparation practice** that defines fixturing, stressing, and conditioning conventions for **U-bend stress-corrosion-cracking (SCC) test specimens**. The U-bend geometry — a flat strip plastically bent through ≈ 180° around a central radius into an inverted-U shape — is one of the **dominant stressed-specimen geometries** used in SCC testing. The plastic deformation imposes high residual tensile strain on the outer-fiber surface of the bend, which is then exposed to the test environment.

G30 is **explicitly a specimen-preparation practice, not a test method**: it provides the specimen recipe but does not specify the test environment, exposure duration, inspection schedule, or pass/fail criteria. The specifying body (a project specification, materials standard, or environment-specific test method such as [[astm-g36]] for boiling MgCl2 Cl-SCC, [[astm-g44]] for alternate-immersion 3.5% NaCl, or [[ampp-tm-0177]] for sour-service SSC) supplies those parameters. G30 is the most-cited specimen-preparation reference in the SCC test literature for sheet and plate product forms.

The U-bend is a high-strain, **constant-deformation** specimen: the imposed strain (and resulting residual surface stress) is set by the bend radius, the strip thickness, and the elastic-plastic post-springback relaxation. The practice provides the elastic-plastic-bending derivations needed to estimate outer-fiber residual stress at and above the proof of the candidate material. Two common variants are the **single-stage U-bend** (full 180° plastic bend, springback released against a stop) and the **two-stage U-bend** (initial bend with subsequent additional flexure to add elastic strain over the plastic baseline). Both are anchored in G30.

## Revision history

- **1979 — Original G30 publication** as the U-bend specimen-preparation practice within ASTM Committee G01.
- **1997 — Revision** to G30-97; the modern technical baseline. Reapproved without substantive technical change in subsequent cycles.
- **G30-97 (R2016)** — most recent reapproval cycle as of this page; the practice description is mature and the fixturing-and-bending conventions have not materially changed.
- The local O&G-Standards catalog at `/mnt/ace/O&G-Standards/ASTM/G-Series/` may contain a G30 PDF; the parent source page ([og-standards-astm-g-series](../sources/og-standards-astm-g-series.md)) records ASTM G-Series presence.

## Key sections

The following are the specimen-preparation anchors that appear in the practice (consult the on-disk PDF for clause-exact text):

- **Apparatus and fixturing** — bending jigs, stop blocks, restraint bolts, electrically-isolating insulation washers (to prevent galvanic interactions during exposure).
- **Specimen geometry** — strip dimensions (length, width, thickness), bend radius, restraint mechanism (bolted-and-restrained or self-stressing two-stage geometry).
- **Material conditioning** — heat-treatment condition recording, surface finish (typically wet-ground to a specified grit immediately before exposure), descaling, and welding history.
- **Bending procedure** — slow plastic bending around the central radius, springback release, and (for two-stage variants) subsequent elastic flexure addition.
- **Stress estimation** — analytical formulas relating bend radius, strip thickness, and post-bend residual outer-fiber stress for the chosen variant.
- **Identification, handling, and storage** — pre-exposure documentation requirements.
- **Reporting** — specimen-preparation provenance to be recorded alongside test results.

## Practitioner application

- **Cl-SCC ranking of austenitic stainless steels** — U-bends in boiling MgCl2 ([[astm-g36]]) is the workhorse Cl-SCC screen; G30 is the specimen-preparation reference invoked by the test method.
- **Sour-service-CRA SSC qualification** — Method-B-class bent-beam variants and U-bend variants under [[ampp-tm-0177]] for [[ampp-mr-0175-pt3]] / [[iso-15156-3]] CRA acceptance.
- **Welding-procedure SCC qualification** — sensitized-vs-solution-annealed weldment comparison; G30 specimens spanning weldment, HAZ, and parent-metal regions.
- **Surface-finish and cold-work studies** — U-bend's high-strain regime amplifies the residual-stress contribution of cold work; G30 specimens are used to probe fabrication-route effects on SCC initiation.
- **Aluminum-alloy SCC ranking** — ASTM G47 and G64 cite U-bend geometries derived from G30 for 2XXX and 7XXX heat-treatable aluminum alloys.

## Industry adoption

G30 is the **default U-bend specimen-preparation reference** for SCC testing across the corrosion-engineering community: refining, oil-and-gas, marine, power, and chemical-process. The practice is referenced from virtually every SCC environment-specific test method that uses a U-bend geometry: boiling MgCl2 (G36), alternate-immersion NaCl (G44), aluminum SCC (G47), polythionic-acid SCC (G35), and the SSC variants under TM-0177. Its mature 1979/1997 baseline means industrial test labs treat G30 as foundational, not as an active revision target.

## Why this page exists

This page is the citation resolver target for `code_id = astm-g30` under `.claude/rules/calc-citation-contract.md`. W201 audit (iter-43) surfaced `astm-g30` as an unmatched slug from multiple cross-references in [[astm-g36]] and [[stress-corrosion-cracking]] concept page (table of SCC test specimen geometries). The page anchors that link target without reproducing any clause text, fixture-geometry tables, or stress formulas.

## Where to find the full text

ASTM catalog (registration required for purchase): `https://www.astm.org/g0030-97r16.html`. The publisher-derivative full text is **not** stored in this repo per the vendor-derivative deny-list governance. Calc-citation callers resolve only against this page's frontmatter (`code_id`, `publisher`, `revision`); they do not require body text.

## Cross-references

- [[astm-g36]] — *Boiling Magnesium Chloride SCC Test* — primary consumer test method that invokes G30 U-bend geometry for Cl-SCC ranking of austenitic stainless steels.
- [[astm-g38]] — *C-Ring Stress-Corrosion Test Specimens* — sister specimen-preparation practice for tube/ring product forms (G30 covers sheet/plate; G38 covers tube/ring).
- [[astm-g39]] — *Bent-Beam Stress-Corrosion Test Specimens* — sister specimen-preparation practice for 4-point bent-beam geometry; complementary to U-bend.
- [[astm-g129]] — *Slow Strain Rate Testing* — kinetic-counterpart test method; G30 specimens are static-deformation, G129 specimens are dynamic-strain-rate.
- [[astm-g48]] — *Pitting and Crevice Corrosion in FeCl3 Solution* — different damage mode (pitting/crevice, not SCC); CRA pre-screening that complements SCC testing.
- [[astm-g31]] — *Laboratory Immersion Corrosion Testing of Metals* — non-SCC immersion-testing companion practice.
- [[astm-g1]] — *Preparing, Cleaning, and Evaluating Corrosion Test Specimens* — pre-and-post-exposure specimen-handling baseline; cited from G30.
- [[ampp-tm-0177]] — *Laboratory Testing of Metals for Resistance to SSC and SCC in H2S Environments* — sour-service SCC test method that references U-bend / bent-beam geometries for [[ampp-mr-0175-pt3]] / [[iso-15156-3]] CRA acceptance.
- [[stress-corrosion-cracking]] (concept) — primary consumer concept page; U-bend geometry anchors the SCC test-method ladder.
- [[sour-service-materials]] (concept) — secondary consumer; U-bend specimens are used in some sour-service-CRA qualification routes.
- [[pitting-and-crevice-corrosion]] (concept) — adjacent damage mode; G30 does not address pitting/crevice but is companion to G48.
- [Calc citation contract](../../../../../.claude/rules/calc-citation-contract.md)
