---
title: "ASME B31.12 — Hydrogen Piping and Pipelines"
slug: asme-b31-12
tags: ["asme", "b31", "hydrogen-piping", "h2-pipelines", "hydrogen-economy", "fuel-cell", "embrittlement"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
code_id: asme-b31-12
publisher: ASME
revision: "not-on-disk"
revision_source: "not present in /mnt/ace/O&G-Standards/ASME/ catalog as of 2026-05-09"
publisher_current_edition: "B31.12-2023 (1st edition 2008; ~3-yr revision cycle: 2008, 2011, 2014, 2019, 2023)"
methodology_status: catalog-absent-publisher-only
verified_on: 2026-05-09
public_url: https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines
sources:
  - wikis/engineering-standards/wiki/sources/og-standards-asme.md
extraction_policy: metadata-only
raw_copy_allowed: false
cross_links:
  - ../concepts/hydrogen-embrittlement.md
  - ../concepts/leak-before-break.md
  - asme-b31-1.md
  - asme-b31-3.md
  - asme-b31-4.md
  - asme-b31-8.md
---

# ASME B31.12 — Hydrogen Piping and Pipelines

> Resolver target for digitalmodel `Citation` instances per `.claude/rules/calc-citation-contract.md`. Contains no clause text, no formulas, and no tables from the source — publisher facts and methodology pointers only. **No on-disk copy in the workspace catalog as of 2026-05-09**; this page documents publisher-side facts and downstream-consumer needs ahead of catalog acquisition.

## Scope

ASME B31.12 governs design, materials, fabrication, examination, testing, and operation of **piping systems and pipelines** for transmission of **gaseous and liquid hydrogen**. The code's scope spans plant-internal industrial piping (refinery hydrogen-treating units, fuel-cell systems, hydrogen-refueling stations) and cross-country transmission pipelines, with a unified materials-and-stress framework that propagates the hydrogen-specific degradation risk into design margins.

B31.12 is distinguished from its B31 siblings by the **hydrogen-specific materials qualification** (Article G — *Performance Qualification*) and a **higher safety factor** to envelope life-cycle hydrogen-embrittlement risk. Where [B31.4](asme-b31-4.md) (liquid pipelines) and [B31.8](asme-b31-8.md) (gas transmission) treat the transported fluid as inert from a material-degradation standpoint, B31.12 treats hydrogen as a metallurgical actor on the steel itself. Companion code on the vessel side: **ASME BPVC Section VIII Division 3 Article KD-10** (high-pressure hydrogen-vessel design).

## Edition history

B31.12 revises on an approximate three-year cycle. Editions in the publisher stream:

| Edition | Status |
|---------|--------|
| B31.12-2008 | First edition |
| B31.12-2011 | Superseded |
| B31.12-2014 | Superseded |
| B31.12-2019 | Superseded |
| B31.12-2023 | Most recent at publisher (verify against the public catalog URL above before citing) |

No revision is present on disk in the workspace ASME catalog (`/mnt/ace/O&G-Standards/ASME/`) as of the page's `verified_on` date; calc callers requesting B31.12-resolved citations must treat the resolver as **catalog-absent** until acquisition lands. The cross-cutting methodology (material-performance-factor de-rating, Article G qualification, Article H processing controls) is structurally stable across editions; specific tabulated factors and the materials roster have moved across the 2014→2019→2023 stream as the hydrogen-economy infrastructure pipeline matured.

## Key Articles

- **Article IP** — *Industrial piping*: piping inside fuel-cell systems, hydrogen-refueling stations, and refinery hydrogen-treating units. Plant-internal envelope.
- **Article PL** — *Hydrogen pipelines*: transmission across right-of-way, sister to B31.8 in form but with B31.12 stress-and-materials rules.
- **Article GR** — *General requirements*: cross-cutting administrative and procedural baseline shared by Articles IP and PL.
- **Article G** — *Performance qualification*: material-property tests in hydrogen environment to verify hydrogen-compatibility (S-N fatigue, tensile, and fracture-toughness in H₂; slow-strain-rate per ASTM G129). The discriminating feature versus the rest of the B31 family.
- **Article H** — *Hardness limits and processing controls* for high-strength steels, calibrated to mitigate hydrogen-embrittlement risk in the as-fabricated and as-welded condition.

## Why hydrogen needs a special code

Hydrogen exhibits **three distinct degradation mechanisms** in piping materials, each addressed by B31.12 design rules:

1. **HE — Hydrogen Embrittlement**: low-temperature, low-strain-rate cracking driven by atomic-hydrogen ingress and trapping at defects, grain boundaries, and high-stress sites. See the concept page on [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) for the metallurgical mechanism, susceptibility-by-microstructure, and operating-window picture.
2. **HEAC — Hydrogen-Enhanced Aqueous Corrosion**: in moist hydrogen at low pH, accelerated steel corrosion that compounds with embrittlement to shorten service life faster than either mechanism alone.
3. **HHA — High-Pressure Hydrogen Attack**: room-temperature, very-high-pressure analogue of high-temperature hydrogen attack (HTHA). Distinct from the refining-side HTHA covered by API RP 941 / API RP 571 — same physics class (hydrogen reacting with carbide phases) but driven by pressure rather than temperature, and relevant to high-pressure storage and 700-bar dispensing.

Material selection (carbon-steel grade + heat treatment + impurity limits per Article H) and design-stress de-rating (the Material Performance Factor `M_f`, Article GR / Article PL) are calibrated against these mechanisms.

## Material Performance Factor (`M_f`)

`M_f` is a design-stress de-rating multiplier applied to the basic allowable stress, indexed against nominal pipe-grade tensile strength and design pressure. The counter-intuitive physics: **higher pipe-grade strength produces a stiffer `M_f` penalty** (stronger steel embrittles worse in hydrogen, because higher-strength microstructures are more susceptible to HE-driven cracking). This forces designers toward lower-strength, more hydrogen-tolerant grades for high-pressure service rather than reaching for higher-grade steel to cut wall thickness — the opposite of the natural-gas-pipeline (B31.8) optimization.

The `M_f` table and the underlying qualification protocol (Article G) are the load-bearing differentiators of this code from the rest of the B31 family.

## Hydrogen economy relevance

As global decarbonization drives green-H₂ (electrolysis from renewable power) and blue-H₂ (steam-methane reforming with CCS) production and transmission, B31.12 governs the new infrastructure layer:

- **Gas-transmission pipelines** for high-purity H₂ and for natural-gas + H₂ blends (the blending question itself drives ongoing B31.12 / B31.8 boundary discussions, since blend ratios affect material qualification choices).
- **Refueling stations** dispensing at 350-bar (heavy-duty) and 700-bar (light-duty) classes, including the high-pressure storage cascades that sit upstream of the dispenser.
- **Industrial fuel-cell systems** — piping within stationary and mobile fuel-cell installations.
- **Refining hydroprocessing** — hydrotreating and hydrocracking unit piping, which is the legacy industrial domain of high-pressure hydrogen service that predates the hydrogen-economy framing.

## Cross-references

Sibling B31 piping codes (different fluid or service envelope):

- [ASME B31.1](asme-b31-1.md) — Power Piping
- [ASME B31.3](asme-b31-3.md) — Process Piping
- [ASME B31.4](asme-b31-4.md) — Pipeline Transportation Systems for Liquids
- [ASME B31.8](asme-b31-8.md) — Gas Transmission and Distribution Piping

Companion vessel-side hydrogen code:

- ASME BPVC Section VIII Division 3 — Article KD-10: design rules for high-pressure hydrogen vessels (the storage-side counterpart to B31.12 PL/IP).

Hydrogen-environment material-test methods cited by Article G qualification:

- **ASTM G142** — tensile testing of metals in H₂-containing environments.
- **ASTM G129** — slow-strain-rate testing for environmentally assisted cracking.
- **ASTM G146** — evaluation of stress-corrosion-cracking and hydrogen-embrittlement of high-strength steels (fracture-toughness in H₂ context).

Adjacent hydrogen-damage references (different mechanism class):

- **API RP 941** — Nelson curves for high-temperature hydrogen attack (refining-side, temperature-driven; complementary to B31.12 HHA/HE focus).
- **API RP 571** — damage mechanisms in refinery service (HTHA, HE, sulfide-stress-cracking context).

Concept-page consumers in this wiki:

- [hydrogen-embrittlement](../concepts/hydrogen-embrittlement.md) (`../concepts/hydrogen-embrittlement.md`) — primary consumer; B31.12 Article G qualification protocol and `M_f` de-rating are the design-side response to the HE mechanism described there.
- [leak-before-break](../concepts/leak-before-break.md) (`../concepts/leak-before-break.md`) — LBB demonstration is increasingly applied to high-pressure-H₂ storage and pipeline service, where B31.12 fracture-toughness qualification supplies the material-property inputs to the LBB analysis.

## Sources

- Catalog source page: [og-standards-asme](../sources/og-standards-asme.md) — ASME slice metadata. B31.12 is not enumerated in the on-disk ASME catalog as of 2026-05-09 (verified absent under `/mnt/ace/O&G-Standards/ASME/`).
- Publisher catalog: https://www.asme.org/codes-standards/find-codes-standards/b31-12-hydrogen-piping-pipelines (verify current edition before citing).
- Calc citation contract: `.claude/rules/calc-citation-contract.md` (workspace-hub) — defines how `digitalmodel` Citation instances resolve to this page; resolver will return `catalog-absent` for B31.12 until a revision lands on disk.
