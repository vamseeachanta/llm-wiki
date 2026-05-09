---
title: "Pitting and Crevice Corrosion"
slug: pitting-and-crevice-corrosion
domain: engineering-standards
added: 2026-05-09
last_updated: 2026-05-09
tags:
  - corrosion
  - pitting
  - crevice
  - cra
  - stainless-steel
  - cpt
  - cct
sources:
  - ../standards/astm-g48.md
---

# Pitting and Crevice Corrosion

> Concept anchor for the ASTM G46/G48/G78 cluster and the sour-service CRA qualification chain. Bidirectional with [astm-g48](../standards/astm-g48.md) (primary), [iso-15156](../standards/iso-15156.md), and [ampp-tm-0177](../standards/ampp-tm-0177.md).

## What are pitting and crevice corrosion?

**Pitting** and **crevice** corrosion are localized breakdown modes of the protective passive film on stainless steels, nickel-base alloys, copper-nickel alloys, titanium, and related corrosion-resistant alloys (CRAs). Unlike general (uniform) corrosion, the attack concentrates at small surface sites, producing deep, narrow cavities that consume little total mass but can perforate a wall thickness or initiate a fatigue crack.

The driving conditions are the same for both modes:

- **Chloride (Cl⁻) ions** in the wetted environment (seawater, brines, produced water, deicing-salt aerosol, FeCl3 test solution).
- **Low local pH**, either ambient (acidified service) or autocatalytically generated inside the defect once it nucleates.
- **Restricted-flow geometry** — for crevice corrosion this is the gasket lap, flange face, threaded joint, or tube/tubesheet annulus that traps stagnant electrolyte; for pitting it is the micro-defect (inclusion site, scratch, weld arc strike) that seeds the initial passive-film breach.

The two modes share initiation chemistry but differ in geometry: pitting initiates on an **open, freely-flushed surface**; crevice corrosion initiates inside an **occluded geometry** that prevents oxygen replenishment and chloride wash-out. Crevice attack typically initiates at a **lower temperature** than pitting on the same alloy.

## Why CRAs are vulnerable

The corrosion resistance of stainless steels and Ni-base alloys derives from a thin (1–3 nm) passive film dominated by **Cr2O3** with Mo and N enrichment in the underlying alloy contributing to film stability. The film is metastable: at sufficiently aggressive Cl⁻ activity and low pH it breaks down locally, exposing bare metal that anodically dissolves while the surrounding still-passive surface acts as a large cathode.

Once a pit or crevice nucleates the chemistry **autocatalyzes**:

1. Anodic metal dissolution inside the cavity produces Mⁿ⁺ cations (Fe²⁺, Cr³⁺, Ni²⁺, Mo⁴⁺/⁶⁺).
2. Cl⁻ migrates inward to maintain charge neutrality, raising local chloride concentration well above bulk.
3. Hydrolysis of the dissolved cations (Mⁿ⁺ + n H2O → M(OH)n + n H⁺) drops local pH to 1–3.
4. The acidified, chloride-rich micro-environment is more aggressive than bulk and **prevents repassivation**, so the pit or crevice continues to deepen.

This autocatalytic loop is why localized corrosion can perforate a CRA wall while the bulk surface remains visually pristine, and why apparently-modest temperature increases can dramatically accelerate damage.

## CPT/CCT — critical temperatures

Two screening metrics rank an alloy's localized-corrosion resistance:

- **Critical Pitting Temperature (CPT)** — the lowest temperature at which stable pitting is observed under a defined chloride exposure.
- **Critical Crevice Temperature (CCT)** — the lowest temperature at which stable crevice attack is observed under the same chloride exposure with a controlled crevice former. CCT < CPT for the same alloy.

A useful compositional proxy is the **Pitting Resistance Equivalent Number (PREN)**:

```
PREN = %Cr + 3.3 · %Mo + 16 · %N
```

Higher PREN correlates with higher CPT/CCT but does not substitute for testing — heat treatment, microstructure (sigma/chi phase in duplex grades), surface finish, and weld metallurgy all shift the actual test result away from the PREN-implied ranking.

## Standard test methods

| Method | Standard | Notes |
|--------|----------|-------|
| FeCl3 immersion (pitting) | [ASTM G48 Method A](../standards/astm-g48.md) | 6.0 % FeCl3 · 6H2O, 72 h, mass loss + pit depth |
| FeCl3 crevice | [ASTM G48 Method B](../standards/astm-g48.md) | Crevice former (PTFE block or 12-tooth multiple-crevice washer) + same chemistry |
| CPT step-up | [ASTM G48 Method C](../standards/astm-g48.md) | 5 °C steps, 24 h per step, weight-change criterion |
| CCT step-up | [ASTM G48 Method D](../standards/astm-g48.md) | Same with crevice former |
| Refined CPT/CCT | [ASTM G48 Methods E/F](../standards/astm-g48.md) | Tightened specimen prep + step-control envelope |
| Crevice (general guidance) | ASTM G46 / ASTM G78 | G46 — pit examination + rating; G78 — crevice testing in flowing chloride / seawater (closer to in-service) |
| Electrochemical CPT | ASTM G150 | Potentiodynamic / potentiostatic CPT determination (faster, smaller specimens than G48 C/E) |

ASTM G46, G78, and G150 do not yet have dedicated standards pages in this wiki — they are flagged for ingest as the source-corpus expands.

## Material-class qualification

Typical CPT/CCT envelopes from FeCl3-based testing (indicative ranking; actual project numbers come from the specifying body's MDS):

| Alloy class | Example UNS | Indicative CPT (FeCl3, °C) | Indicative CCT (FeCl3, °C) |
|-------------|-------------|----------------------------|----------------------------|
| 304L austenitic | S30403 | < 25 | < 10 |
| 316L austenitic | S31603 | 25 – 30 | 10 – 20 |
| 22Cr duplex | S32205 | 35 – 45 | 20 – 35 |
| 25Cr super-duplex | S32750 / S32760 | 50 – 60 | 35 – 50 |
| 6Mo super-austenitic | S31254 / N08367 | 65 – 75 | 45 – 55 |
| Alloy 825 | N08825 | 70 – 80 | 50 – 60 |
| Alloy 625 | N06625 | > 85 | > 70 |
| Alloy C-276 | N10276 | > 100 | > 90 |

These envelopes are bands, not point values — within a class, heat-treatment, surface-finish, and weld-metallurgy effects routinely shift the measured CPT/CCT by ±5–10 °C. Project specifications (e.g., NORSOK MDS D44/D45/D55/D57 for super-duplex) lock the acceptance temperature for a given component.

## Sour-service interaction

For H2S-containing service the controlling document is [ISO 15156 / NACE MR0175](../standards/iso-15156.md) Part 3 (CRA materials selection). Project specifications implementing MR0175-3 routinely cite **G48 Method B** mass-loss/pit-depth limits and **CCT-by-Method-F** thresholds as the qualification evidence for 22Cr and 25Cr duplex grades and for nickel-base alloys (UNS N06625 / N08825 / N06022 / N06059 / N06200) destined for sour service.

The interaction matters: combined Cl⁻ + H2S environments are **more aggressive** than aerated chloride alone for CRAs. Empirically, the CPT for a given alloy in a sour-Cl⁻ brine is typically **10 – 20 °C lower** than its FeCl3-derived value, and the failure mode often shifts from pitting to a coupled pit-initiation / sulfide-stress-cracking propagation. SSC is the cracking-side companion to localized corrosion and is qualified separately under [AMPP TM0177](../standards/ampp-tm-0177.md) (parallel cracking-test method, not a pitting test) — but the two qualification chains feed the same MR0175 acceptance package.

## Standards

- **Primary:** [ASTM G48](../standards/astm-g48.md) — six-method FeCl3 test family for pitting and crevice ranking, CPT, and CCT determination on stainless and Ni-base CRAs.
- **Sour-service material qualification:** [ISO 15156 / NACE MR0175 Part 3](../standards/iso-15156.md) — cites G48 acceptance evidence in CRA selection for H2S service.
- **Parallel cracking method (SSC, not pitting):** [AMPP TM0177](../standards/ampp-tm-0177.md) — tensile / bent-beam / DCB tests for sulfide stress cracking; companion to G48 in the MR0175 qualification dossier.
- **Flagged for future ingest:** ASTM G46 (pit examination + rating practice), ASTM G78 (flowing-chloride crevice guide), ASTM G150 (electrochemical CPT). These appear as bare references in this page and in [astm-g48](../standards/astm-g48.md); promote to standards pages on next ingest pass.

## Related concepts

- [[sour-service-materials]] — CRA selection envelope for H2S service; consumes G48 + MR0175 evidence.
- [[cathodic-protection]] — galvanic interactions can shift the localized-corrosion susceptibility window (notably for duplex SS under CP, governed by DNV-RP-F112).
- [[corrosion-rate-measurement]] — uniform-corrosion rate measurement; complementary but distinct from localized-attack ranking.

## Source materials

- [og-standards-astm-g-series](../sources/og-standards-astm-g-series.md) — parent source page for the ASTM G-series slice of the local catalog; records the four-edition G48 presence and the metadata-only extraction policy that scopes the standards page this concept points to.
