---
title: "API RP 577 — Welding Inspection and Metallurgy"
slug: api-rp-577
code_id: api-rp-577
publisher: API
revision: "1st ed (2004) — catalog latest; 2nd ed (2013) and 3rd ed (2020) are subsequent published editions"
tags:
  - api
  - welding-inspection
  - ndt
  - weld-metallurgy
  - post-weld-heat-treatment
  - refining
added: 2026-05-09
last_updated: 2026-05-09
domain: engineering-standards
sources:
  - /mnt/ace/O&G-Standards/API/Specifications/API_577_Welding_Inspection_and_Metallurgy.pdf
  - ../sources/og-standards-api.md
extraction_policy: metadata-only
raw_copy_allowed: false
---

# API RP 577 — Welding Inspection and Metallurgy

> **code_id:** `api-rp-577` &nbsp;·&nbsp; **publisher:** API &nbsp;·&nbsp; **revision:** 1st ed (2004) — catalog latest; 2nd ed (2013) and 3rd ed (2020) are subsequent published editions.

## Scope

API RP 577 is the **welding-inspection and weld-metallurgy practice
guide** for construction and maintenance welding in the petroleum and
petrochemical industry. It provides the welding-process descriptions,
in-process and post-weld inspection guidance, post-weld heat-treatment
(PWHT) verification protocols, and weldment-metallurgy primer that the
in-service inspection codes [api-510](api-510.md) (pressure vessels),
[api-570](api-570.md) (process piping), and [api-653](api-653.md) (atmospheric storage
tanks) invoke when an inspection programme touches a weld — repair
welding, fitness-for-service repair, alteration, re-rating, or
new-construction acceptance carried over into the in-service file.

Where [api-std-1104](api-std-1104.md) is the **construction code** for pipeline
girth welding (procedure / welder qualification with prescriptive
acceptance), and ASME BPVC Section IX is the **construction code**
for pressure-equipment welding qualification, RP 577 is the
**inspection-grade companion** — the document an inspector consults
to understand *what to look for* on a weld in the field, *which NDE
method* discriminates the expected flaw morphology, and *which
metallurgical risk* the inspection must guard against. RP 577 is not
itself a code — it cannot be invoked as a compliance authority on its
own; it is invoked **through** API 510 / 570 / 653 or the owner-user's
written inspection programme.

The recommended practice covers, in particular: arc-welding process
descriptions (SMAW, GTAW, GMAW, FCAW, SAW, ESW, PAW) with their
typical applications and welding-defect signatures; pre-weld
inspection (joint preparation, fit-up, preheat, materials
verification); in-process inspection (interpass temperature, run
sequence, heat input control); post-weld inspection across the full
NDE menu (visual, RT, UT, AUT/PAUT, MT, PT, ECT, AET, TOFD); PWHT
specification, soak-band determination, and verification by
thermocouple records; hardness traversing protocols including the
sour-service overlay; and a weldment-metallurgy primer covering the
heat-affected zone (HAZ) sub-zones, weld-metal solidification,
parent-metal dilution, and residual-stress development.

## Edition history

| Edition | Year | Catalog status | Notes |
|---------|------|----------------|-------|
| 1st ed | 2004 | **catalog copy** (`API_577_Welding_Inspection_and_Metallurgy.pdf`, PDF metadata `CreationDate 2004-10-07`) | Inaugural edition; established the welding-process-description + NDE-method + metallurgy-primer structure that subsequent editions retained. |
| 2nd ed | 2013 | not in catalog | Expanded NDE coverage (PAUT, TOFD), updated PWHT guidance, refreshed sour-service hardness cross-references against the then-current NACE MR0175 / ISO 15156 wording. |
| 3rd ed | 2020 | not in catalog | Current published edition; further alignment with the [api-rp-571](api-rp-571.md) 3rd-edition damage-mechanism descriptions (post-Tesoro-Anacortes HTHA reassessment) and with the API 581 3rd-edition RBI methodology for welding-inspection effectiveness inputs. |

> **Edition selection.** The frontmatter `revision` field reflects the
> catalog-latest copy (1st ed, 2004) per the spinout's metadata-only
> policy. The 3rd edition (2020) is API's current published edition and
> is the appropriate citation for new construction or repair-welding
> inspection programmes — particularly where modern NDE methods (PAUT,
> TOFD, AUT) or post-2015 sour-service hardness practice are in scope.
> Forward-adopt the publisher edition when a more recent catalog copy
> lands.

## Key sections

The headings below summarise the practice's structural backbone — clause
text, NDE acceptance tables, hardness limits, and PWHT
time-and-temperature tabulations are **not reproduced** per
metadata-only governance.

- **Welding-process descriptions.** RP 577 enumerates the arc-welding
  processes used in petroleum / petrochemical construction and
  maintenance, with applicability and risk:
  - **SMAW (Shielded Metal Arc Welding)** — manual stick electrode;
    field-friendly; hydrogen-cracking risk on low-hydrogen-required
    materials if electrode storage is mishandled.
  - **GTAW (Gas Tungsten Arc Welding)** — manual / mechanised; low
    deposition rate but high cleanliness; preferred for root passes,
    austenitic stainless, and nickel-alloy work.
  - **GMAW (Gas Metal Arc Welding)** — semi-automatic / mechanised;
    higher productivity than SMAW; short-circuit transfer carries
    incomplete-fusion risk on thicker sections.
  - **FCAW (Flux-Cored Arc Welding)** — self-shielded and
    gas-shielded variants; field-friendly; slag inclusions and
    porosity are the dominant defect signatures.
  - **SAW (Submerged Arc Welding)** — high deposition; shop / mill
    longitudinal seams; flux moisture control governs hydrogen risk.
  - **ESW (Electroslag Welding)** — single-pass on thick section;
    coarse HAZ grain growth carries notch-toughness risk; PWHT or
    grain-refining post-pass typically required.
  - **PAW (Plasma Arc Welding)** — narrow, deep keyhole; specialised
    applications (thin-wall stainless tubing, root passes on critical
    joints).

- **Pre-weld inspection.** Verification of materials (mill certs and
  PMI for alloy materials per [api-rp-578](api-rp-578.md) practice), joint geometry
  and fit-up (groove angle, root face, root opening, alignment,
  hi-low), cleanliness, preheat measurement and uniformity across
  the soak band, and consumable handling (electrode storage, flux
  rebake, shielding-gas dewpoint) before arc-on.

- **In-process inspection.** Interpass-temperature measurement (the
  variable most prone to drift on multi-pass welds and the dominant
  control on HAZ peak-temperature exposure); run-sequence verification
  against the WPS (back-step, block, cascade); and heat-input
  monitoring (volts × amps ÷ travel speed) — heat input governs both
  HAZ grain coarsening and weld-metal cooling rate, the two
  metallurgical levers most readily corrupted in the field.

- **Post-weld inspection.** The full NDE menu with method-vs-flaw-
  morphology guidance — see the *NDE method coverage* table below.
  RP 577 is the practice document that maps each welding-process
  defect signature (porosity, slag, lack of fusion, undercut, crater
  cracks, hydrogen-induced cold cracking, solidification cracking,
  reheat cracking) to the NDE method that reliably finds it.

- **Post-weld heat treatment (PWHT).** Soak-band determination
  (heated-band, gradient-control-band, insulation-band geometry),
  thermocouple placement, soak time-and-temperature requirements
  drawn from the construction code (ASME B31.3, ASME BPVC VIII,
  API 650, etc.), heating- and cooling-rate limits to avoid
  distortion and through-thickness gradients, and verification by
  the thermocouple chart record. PWHT effectiveness is **verified**
  by hardness traverse (HV<sub>10</sub> across parent / HAZ / weld
  metal) and, where toughness is in scope, by Charpy V-notch testing
  on the qualified production-test coupon.

- **Hardness traversing protocols.** RP 577 specifies the geometry
  of a hardness traverse (line of indents stepping across parent /
  HAZ / weld / HAZ / parent at controlled spacing), instrument and
  load (typically Vickers HV<sub>10</sub>), and reporting format.
  Hardness is the practical proxy for HAZ microstructure on a
  finished weld — a hardness peak in the coarse-grained HAZ flags
  unreversed martensite (insufficient PWHT) and is the
  controlling acceptance variable for sour service.

- **Weldment-metallurgy primer.** RP 577 walks the **HAZ sub-zones**
  (coarse-grained HAZ at peak temperature, fine-grained HAZ,
  intercritical HAZ, sub-critical HAZ, and the local-brittle-zone
  behaviour at sub-critically reheated coarse-grained regions in
  multi-pass welds), **weld-metal solidification** (epitaxial growth
  off the fusion-line grains, columnar dendrite morphology, segregation
  patterns), **dilution** of weld metal by parent metal at the fusion
  line (governs weld-metal alloy composition for dissimilar-metal
  welds), and **residual stress** development from the welding
  thermal cycle (membrane and through-thickness components,
  as-welded vs. PWHT magnitudes).

## NDE method coverage

RP 577 maps welding-process defect morphology to NDE method. The table
below summarises the practice-grade method-selection guidance used
when planning a weld-inspection campaign; sensitivity bands are
indicative and should be confirmed against the procedure-qualified
NDE technique sheet for the actual inspection.

| Method | When to use | Sensitivity / depth |
|--------|-------------|---------------------|
| Visual (VT) | Surface defects, weld profile, undercut, overlap, crater cracks; mandatory on every weld | Surface only |
| Liquid penetrant (PT) | Surface-breaking defects on non-magnetic materials (austenitic stainless, nickel alloys, aluminium) | Surface only; ~10 μm flaw width |
| Magnetic particle (MT) | Surface and slightly sub-surface defects on ferromagnetic materials; standard for fillet and dressed-weld examination | Surface + near-subsurface (≤6 mm in ferritics) |
| Radiography (RT) | Volumetric examination, gamma- or X-ray; image-based; historical baseline for girth-weld and longitudinal-seam NDE | Through-thickness; weld-volume; favours rounded indications |
| Ultrasonic (UT) | Volumetric examination by contact or immersion pulse-echo; planar flaw detection where RT under-discriminates | Through-thickness; planar flaws (cracks, lack of fusion) |
| Phased-array UT (PAUT) | Volumetric, AUT-grade examination with electronic beam steering and focusing | Higher resolution than conventional UT; electronic scanning replaces mechanical raster |
| Time-of-flight diffraction (TOFD) | Volumetric; sizing-grade flaw-height measurement for ECA inputs | Through-thickness; sizing-accurate on planar flaws |
| Eddy-current (ECT) | Surface and near-subsurface inspection on conductive materials; conductivity / permeability contrast | Surface; conductivity-contrast-limited depth |
| Acoustic emission (AET) | In-service, real-time global screening for actively growing flaws under controlled pressurisation | Active growth detection only; flags locations for follow-up UT/RT |

Modern campaigns commonly run **AUT (PAUT + TOFD combined)** in place
of conventional RT for girth-weld production inspection — RP 577 (2nd
ed onward) carries the practice-level guidance for the AUT
substitution and is the inspection-side counterpart to the
construction-code allowance for AUT under [api-std-1104](api-std-1104.md) Annex /
Appendix B and ASME B31.3.

## Sour-service welding overlay

RP 577 provides the welding-inspection overlay for sour-service
materials — the additional verifications that ride on top of the
base-code inspection programme when the weld will see wet-H<sub>2</sub>S
service per [iso-15156](iso-15156.md) / NACE MR0175:

- **PWHT verification.** PWHT is mandatory for most carbon-steel
  sour-service welds to relax residual stress and to temper HAZ
  martensite below the sour-service hardness ceiling. RP 577 prescribes
  the **dual verification**: (1) thermocouple chart records confirming
  soak time-and-temperature within the heated band, and (2) hardness
  traverse on a production-test coupon confirming HAZ hardness below
  the sour-service limit (typically 250 HV<sub>10</sub> per ISO 15156-2
  for carbon and low-alloy steels).
- **Charpy V-notch toughness.** Where the construction code calls
  toughness testing, RP 577 specifies the production-test coupon
  geometry, notch placement (weld metal, fusion line, HAZ), and
  test-temperature derivation from the lowest-anticipated-service
  temperature.
- **Residual-element control.** RP 577 cross-references the residual-
  element limits that govern HAZ susceptibility — in particular **low-
  Ni** residual-element control on sour-service line-pipe HAZ, where
  Ni residuals raise HAZ hardenability and complicate hardness
  acceptance — see [api-spec-5l](api-spec-5l.md) PSL 2 sour-service annex and
  [iso-15156](iso-15156.md) Part 2.
- **AMPP / NACE MR0175 hardness limits in HAZ.** The HAZ hardness
  ceiling is set by [iso-15156](iso-15156.md) / [ampp-mr-0175-pt2](ampp-mr-0175-pt2.md) (carbon and
  low-alloy steels) and is the load-bearing acceptance variable for
  sour-service weld inspection.

## Cross-references

- **[api-510](api-510.md)** — *Pressure Vessel Inspection Code*. Consumer
  inspection code; invokes RP 577 as the welding-inspection practice
  guide for repair, alteration, and re-rating welds on in-service
  pressure vessels.
- **[api-570](api-570.md)** — *Piping Inspection Code*. Consumer inspection
  code; invokes RP 577 for repair welds on in-service piping (with
  [api-rp-574](api-rp-574.md) as the broader piping-component inspection-method
  guide and [api-std-1104](api-std-1104.md) / ASME B31.3 governing the actual
  weld-construction acceptance).
- **[api-653](api-653.md)** — *Tank Inspection, Repair, Alteration, and
  Reconstruction*. Consumer inspection code; invokes RP 577 for
  shell-course and bottom repair welds on atmospheric storage
  tanks.
- **[api-std-1104](api-std-1104.md)** — *Welding of Pipelines and Related Facilities*.
  Companion construction code for pipeline girth welding; RP 577 is
  the inspection-side practice guide that complements API 1104's
  procedure-and-welder-qualification framework.
- **[api-rp-571](api-rp-571.md)** — *Damage Mechanisms Affecting Fixed Equipment
  in the Refining Industry*. Damage-mechanism context for the
  weldment-metallurgy primer (HAZ damage modes, dissimilar-metal-
  weld cracking, reheat cracking, hydrogen-induced cracking).
- **[api-rp-580](api-rp-580.md)** / **[api-rp-581](api-rp-581.md)** — *Risk-Based Inspection*
  (qualitative) / *Risk-Based Inspection Methodology* (quantitative).
  Consume RP 577 inspection-effectiveness inputs (NDE method
  selection, coverage fraction) to grade weld-inspection
  effectiveness in the RBI probability-of-failure calculation.
- **ASME BPVC IX** — *Welding and Brazing Qualifications*. Construction
  code for pressure-equipment welding qualification (WPS, PQR,
  WPQ); RP 577 is the inspection-side practice guide that complements
  Section IX's qualification framework.
- **AWS D1.1** — *Structural Welding Code — Steel*. Construction code
  for structural carbon and low-alloy steel welding (bridges,
  buildings, fixed offshore jackets); pre-qualified-WPS and
  workmanship-acceptance frame is independent of RP 577 but the
  NDE-method-vs-flaw-morphology guidance carries across.
- **ISO 9712** — *Non-destructive testing — Qualification and
  certification of NDT personnel*. The international NDE
  personnel-certification scheme RP 577 cross-references for
  inspector qualifications (alongside SNT-TC-1A and ASNT CP-189
  in North American practice).
- **[iso-15156](iso-15156.md)** — *Petroleum and natural gas industries — Materials
  for use in H2S-containing environments in oil and gas production*
  (NACE MR0175). Sour-service materials standard; governs the HAZ
  hardness ceiling and PWHT requirement that RP 577 verifies.
- **[welding-procedures-and-acceptance](../concepts/welding-procedures-and-acceptance.md)** — concept-page consumer.
  RP 577 supplies the inspection-side counterpart to the construction-
  code procedure-and-acceptance framework summarised on the concept
  page.
- **[weld-toughness](../concepts/weld-toughness.md)** — concept-page consumer. RP 577's Charpy and
  hardness-traverse protocols are the inspection-side anchors for the
  weld-toughness verification flow described on the concept page.

## Why this page exists

Resolver target for digitalmodel `Citation` instances per
`.claude/rules/calc-citation-contract.md`. The page records publisher
facts (`code_id`, `publisher`, `revision`) so fail-closed citation
resolution can ground welding-inspection-derived outputs (NDE
method-effectiveness inputs to RBI, PWHT verification flags, HAZ
hardness acceptance, sour-service welding compliance assertions)
against this practice. **Metadata-only** per spinout 2026-05-05
governance: no clause text, NDE acceptance tables, PWHT time-and-
temperature tabulations, hardness limits, or weld-metallurgy figures
are reproduced here.

## Where to find the full text

- Catalog copy (read-only, vendor-derivative; do NOT copy into git per
  spinout 2026-05-05 governance):
  - `/mnt/ace/O&G-Standards/API/Specifications/API_577_Welding_Inspection_and_Metallurgy.pdf`
    — 1st edition (2004), catalog latest. (PDF stored under the
    `Specifications/` subdirectory by the catalog ingest, but the
    document is normatively a Recommended Practice.)
- API publisher catalog: <https://www.api.org/products-and-services/standards>
- Practitioner usage: invoked through API 510 / 570 / 653 inspection
  programmes; not cited as a standalone compliance authority.

## Sources

- Source page: [og-standards-api](../sources/og-standards-api.md) —
  catalog row for `API 577 Welding Inspection and Metallurgy` in the
  RP-grade inspection cluster (`510, 570, 572, 574, 576, 577, 578,
  580, 581, 582`).
- Catalog provenance: `/mnt/ace/O&G-Standards/_catalog.json` —
  entry `organization: API`, `doc_number: 577`, `relative_path:
  API/Specifications/API_577_Welding_Inspection_and_Metallurgy.pdf`;
  PDF metadata `CreationDate 2004-10-07` confirms the 1st edition
  (2004) as the catalog copy.
