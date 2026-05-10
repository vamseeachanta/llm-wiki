---
title: "Sour Service Materials & H2S Cracking"
slug: sour-service-materials
tags: ["sour-service", "h2s", "ssc", "hic", "sohic", "cra", "material-selection"]
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - standards/iso-15156.md
---

# Sour Service Materials & H2S Cracking

## What is sour service?

Sour service describes oil and gas production environments in which the partial pressure of hydrogen sulfide (pH2S) in the wet hydrocarbon-bearing fluid exceeds publisher-defined thresholds, triggering material-selection and qualification requirements to prevent environmentally-assisted cracking failures. The governing materials code, [iso-15156](../standards/iso-15156.md) / NACE / AMPP MR0175, classifies an environment as sour once total system pressure and pH2S place the equipment above the entry threshold for the materials class under consideration; below that threshold the environment is conventionally termed "sweet" and ordinary carbon-steel selection rules apply. Threshold values, in-situ pH determination, chloride concentration, free elemental sulfur, and temperature are all read from the publisher source — no normative numbers are reproduced in this wiki.

## Cracking mechanisms

Sour-service qualification protects against a family of hydrogen-driven cracking failure modes in metallic equipment exposed to wet H2S. The dominant mechanisms catalogued by [iso-15156](../standards/iso-15156.md) / [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) / [ampp-mr-0175-pt3](../standards/ampp-mr-0175-pt3.md):

- **SSC (sulfide stress cracking)** — brittle cracking of high-strength steels under sustained tensile stress in wet H2S; atomic hydrogen liberated by the H2S corrosion reaction is absorbed into the steel and embrittles the lattice. Hardness-controlled in carbon and low-alloy steels (Pt 2); composition-and-cold-work-controlled in CRAs (Pt 3).
- **HIC (hydrogen-induced cracking)** — internal stepwise blister-and-crack networks in plate steels, driven by hydrogen accumulation at MnS inclusion sites and segregation bands. Stress-independent (occurs in unstressed plate). Qualified by NACE TM-0284.
- **SOHIC (stress-oriented hydrogen-induced cracking)** — stacked HIC blisters linked through-thickness by SSC ligaments under applied or residual tensile stress; combines HIC nucleation with SSC propagation. Heat-affected zones of welded carbon-steel pressure vessels are the canonical concern.
- **SCC (sulfide stress corrosion cracking variants)** — chloride-and-H2S co-driven transgranular or intergranular cracking of austenitic, duplex, and precipitation-hardened stainless steels and Ni-base alloys; characterised through slow strain-rate (ISO 7539-7) and four-point-bend tests at elevated temperature.
- **Galvanic acceleration with chlorides** — coupling of dissimilar materials (e.g., 13Cr tubing to carbon-steel casing, or CRA cladding to carbon-steel substrate) in chloride-bearing brines accelerates the active member's H2S-driven attack and can shift its qualification envelope.

## Severity zoning (ISO 15156-2)

Part 2 of [iso-15156](../standards/iso-15156.md) / [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) codifies a four-region sour-service severity classification for carbon and low-alloy steels. The classification is plotted as a pH2S–pH diagram (log partial pressure of H2S on the x-axis vs. in-situ pH on the y-axis); each region carries distinct hardness, heat-treatment, and welding-procedure constraints:

- **Region 0 — sweet.** Below the sour-service entry threshold. Conventional carbon-steel selection; no MR0175 hardness caps invoked.
- **Region 1 — mild sour.** Lowest sour severity; broadest set of carbon and low-alloy steels qualifies subject to base hardness limits.
- **Region 2 — intermediate sour.** Tighter hardness, chemistry, and heat-treatment caps; some grades fall out vs. Region 1.
- **Region 3 — severe sour.** Most restrictive zone; only specific microstructure-and-hardness-controlled steels qualify, and SOHIC-resistance evidence may be required in addition to SSC.

**Modifiers** that shift an environment toward higher severity within or across regions: chloride concentration (high Cl- raises pitting susceptibility and depresses in-situ pH); presence of free elemental sulfur S0 (a hydrogen-charging accelerator that can disqualify otherwise-eligible materials); and temperature (which interacts non-monotonically with SSC vs. HIC kinetics — see Pt 2 for the threshold envelope). For CRAs in Part 3 the diagram is replaced by per-alloy-group temperature/chloride/pH2S envelopes.

## Material classes & qualification

| Material class | Standard | Typical materials |
|---|---|---|
| Carbon & low-alloy steel | [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) (= ISO 15156-2 / NACE MR0175-2) | API 5L X65 / X70 line pipe, ASTM A516 plate, A350 LF2 forgings; hardness limits in HAZ commonly cited near 250 HV (verify against publisher source) |
| Corrosion-resistant alloys (CRAs) | [ampp-mr-0175-pt3](../standards/ampp-mr-0175-pt3.md) (= ISO 15156-3 / NACE MR0175-3) | 13Cr martensitic stainless, 22Cr / 25Cr duplex and super-duplex, austenitic stainless (316/UNS S31603), Ni-base 825 / 625 / 718 / C-276 |
| Cast iron | [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) (= ISO 15156-2) | Severely restricted; permissible only in narrow non-pressure-retaining roles per Pt 2 |

Qualification routes per [ampp-mr-0175-pt1](../standards/ampp-mr-0175-pt1.md): (a) selection from the standard's pre-qualified material tables within the cited environmental envelope; (b) laboratory qualification by NACE TM-0177 (SSC) and NACE TM-0284 (HIC) at conditions bounding the in-service exposure; or (c) prior-field-experience evidence accepted under the Part 1 fitness-assessment route. Welding-procedure qualification (PWHT, hardness mapping in HAZ, and consumable selection) is integral to the qualification record and is governed jointly with [asme-bpvc-ix](../standards/asme-bpvc-ix.md) and operator weld-procedure specifications.

## Test methods

- **NACE TM-0177 — SSC laboratory test methods** ([ampp-tm-0177](../standards/ampp-tm-0177.md)). Four standardized geometries: Method A uniaxial tension, Method B bent-beam, Method C C-ring, Method D double-cantilever-beam (DCB, fracture-mechanics K_ISSC). Specimens are exposed in deaerated H2S-saturated test solutions under sustained load until time-to-failure or no-failure-at-720-h is recorded. Method-D K_ISSC is the fitness-for-service-grade SSC threshold.
- **NACE TM-0284 — HIC test method.** Plate coupons immersed in H2S-saturated test solution (Solution A standard / Solution B harsher) for 96 hours; metallographic measurement of crack length ratio (CLR), crack thickness ratio (CTR), and crack sensitivity ratio (CSR) against acceptance criteria.
- **ASTM G48 — pitting and crevice corrosion of stainless steels and CRAs** ([astm-g48](../standards/astm-g48.md)). Method A ferric-chloride pitting; Method B ferric-chloride crevice; Method E critical pitting temperature (CPT); Method F critical crevice temperature (CCT). Used as a pre-screen for Part-3 CRA candidates and to set chloride-temperature operating envelopes for duplex and super-duplex grades.
- **Environmental conditioning.** Test solutions are specified in the TM standards (NACE Solution A = 5% NaCl + 0.5% acetic acid, H2S-saturated; Solution B = buffered acidified brine; Solution C = harsher chloride brine for CRAs). Conditioning controls dissolved O2, pH2S, temperature, and pH; deviations from the prescribed conditioning invalidate the qualification.

## Standards

Bidirectional links to the standards-page resolvers (each carries `code_id`, `publisher`, `revision` frontmatter per the wiki schema):

- [iso-15156](../standards/iso-15156.md) — primary materials-selection code, three-part joint publication (ISO 15156-1/-2/-3 = NACE MR0175 = AMPP MR0175)
- [ampp-mr-0175-pt1](../standards/ampp-mr-0175-pt1.md) — Part 1, general principles for selection of cracking-resistant materials
- [ampp-mr-0175-pt2](../standards/ampp-mr-0175-pt2.md) — Part 2, carbon and low-alloy steels and cast iron
- [ampp-mr-0175-pt3](../standards/ampp-mr-0175-pt3.md) — Part 3, corrosion-resistant alloys and other alloys
- [ampp-tm-0177](../standards/ampp-tm-0177.md) — NACE TM-0177 SSC laboratory test method (Methods A/B/C/D)
- [api-spec-6a](../standards/api-spec-6a.md) — API Spec 6A wellhead and tree equipment (sour-service material qualification cites MR0175)
- [astm-g48](../standards/astm-g48.md) — pitting and crevice corrosion test methods for CRAs (CPT/CCT pre-screen)

## Related concepts

- [cathodic-protection](cathodic-protection.md) — interaction with sour-service equipment; CP-induced hydrogen charging compounds H2S-driven hydrogen embrittlement on duplex/super-duplex (HISC), addressed by DNV-RP-F112 alongside MR0175 SSC qualification
- [pitting-and-crevice-corrosion](pitting-and-crevice-corrosion.md) — chloride-driven pitting can locally depress pH and trigger SSC initiation at pit roots; CPT/CCT (ASTM G48) sets the chloride-temperature operating window for CRAs in sour service
- [[weld-procedure-qualification]] — post-weld heat treatment (PWHT), HAZ hardness mapping, and consumable selection for sour-service carbon-steel welds; jointly governed by [asme-bpvc-ix](../standards/asme-bpvc-ix.md) and Pt 2 hardness caps
- [fitness-for-service](fitness-for-service.md) — in-service H2S-exposure assessment of equipment with HIC/SOHIC indications, per API 579 / ASME FFS-1 procedures combined with MR0175 Part 1 fitness route

## Source materials

- [O&G Standards catalog — ISO](../sources/og-standards-iso.md) — catalog summary for the ISO slice of `/mnt/ace/O&G-Standards/`, including the `15xxx/` subfolder that holds the on-disk Pt-1 (2001), Pt-2 (2003), and Pt-3 (2003) PDFs of ISO 15156 1st Edition.
- Vendor PDFs are read-only at the `/mnt/ace/O&G-Standards/` mount and **never enter this repo** per the spinout 2026-05-05 governance and the firewall in this repo's root `CLAUDE.md`.
