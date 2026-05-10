---
title: "API Recommended Practice 578 — Material Verification Program for New and Existing Alloy Piping Systems"
slug: api-rp-578
code_id: api-rp-578
publisher: API
revision: "3rd ed (2018); current published edition. Earlier editions: 1st (1999), 2nd (2010)."
jurisdiction: "Industry recommended practice for refining, petrochemical, and offshore alloy material verification (PMI); consumed through owner-user inspection and quality programmes anchored on API 510 / 570 / 653 and on construction codes ASME B31.3 / B31.1."
instrument_type: recommended-practice
supersedes: ~
extraction_policy: metadata-only
raw_copy_allowed: false
sources:
  - ../sources/og-standards-api.md
public_url: https://www.api.org/products-and-services/standards
publisher_catalog_url: https://www.api.org/products-and-services/standards/important-standards-announcements/recommended-practice-578
tags:
  - api
  - api-rp
  - pmi
  - positive-material-identification
  - alloy-verification
  - quality-control
  - inspection-practice
  - mix-up-prevention
added: 2026-05-10
last_updated: 2026-05-10
domain: engineering-standards
---

# API Recommended Practice 578 — Material Verification Program for New and Existing Alloy Piping Systems

> **code_id:** `api-rp-578` · **publisher:** API · **revision:** 3rd ed (2018); current published edition.

## Scope

API RP 578 is the **Positive Material Identification (PMI) practice** that defines how owner-users verify the alloy composition of metallic piping components — pipe, fittings, flanges, valves, bolting, and weldments — at the point of fabrication, construction, repair, and (selectively) during in-service inspection. The practice exists because alloy mix-ups between carbon steel and low-alloy / stainless / nickel-alloy components have caused multiple high-consequence releases in refining and petrochemical service: substituting a 1¼Cr-½Mo elbow with a carbon-steel elbow in high-temperature hydrogen service can fail by HTHA within months, and a 304L vs 316L mix-up in a chloride-containing service can fail by chloride SCC. RP 578 specifies **when** PMI is required (alloy criticality screening), **what** instrumentation is acceptable (XRF, OES; with method-specific limitations), **how** sampling is structured (extent-of-coverage rules, exhaustive vs statistical), and **who** is qualified to perform the verification.

## Revision history

| Edition | Year | Notes |
|---------|------|-------|
| 1st ed | 1999 | Original issue; piping focus |
| 2nd ed | 2010 | Expanded XRF and OES technique coverage; clarified alloy-criticality screening |
| 3rd ed | 2018 | Current published edition; expanded bolting and weld-filler-metal verification, alignment with [api-rp-577](api-rp-577.md) welding-inspection practice |

Catalog presence: not currently on disk in `/mnt/ace/O&G-Standards/API/`; obtain via publisher catalog.

## Key sections

The headings below summarise the practice's structural backbone — clause text, alloy-criticality screening tables, and instrument-method tabulations are **not reproduced** per metadata-only governance.

- **Material verification program elements.** Written program scope, alloy-criticality screening, sampling rules, recordkeeping, examiner qualification.
- **PMI instrumentation.** X-Ray Fluorescence (XRF) — handheld and benchtop; Optical Emission Spectrometry (OES) — handheld arc; method-specific limitations (XRF cannot detect light elements like C, Si below ~Mg without inert-gas purge; OES requires sparking and surface preparation).
- **Sampling extent.** 100% verification for high-criticality alloys (e.g., chrome-moly in high-temperature hydrogen service per [api-rp-941](api-rp-941.md)); statistical sampling for lower-criticality service.
- **Weld filler metal verification.** Verification that deposited weld metal matches the specified filler-metal classification — distinct from base-metal PMI.
- **Bolting verification.** Verification of stud bolts and nuts, especially in high-temperature service where alloy substitution has caused multiple failures.
- **Recordkeeping.** Marking, traceability, and documentation requirements that integrate with mill test reports (MTRs) and quality-management systems.
- **Alloy-criticality screening.** Decision logic for when to invoke PMI: combination of damage mechanism (HTHA, sulfidation, chloride SCC, naphthenic acid corrosion) and consequence-of-failure.

## Practitioner application

API RP 578 is the practice cited by:
- **Construction QA/QC inspectors** at the fabrication shop and field-construction stage to verify that delivered alloy components match specification before installation.
- **In-service inspectors** working under [api-510](api-510.md), [api-570](api-570.md), or [api-653](api-653.md) when investigating suspected alloy mix-ups (e.g., unexpected wall loss in what should be a corrosion-resistant alloy circuit).
- **Owner-user material engineers** authoring the alloy-criticality screening procedure that drives PMI extent-of-coverage decisions.
- **Inspection contractors** qualifying their PMI technicians and instruments per RP 578 examiner-qualification rules.

PMI findings inform mechanical-integrity programmes under OSHA 29 CFR 1910.119 PSM and feed RBI updating per [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) when alloy mix-up is identified as a credible damage-introduction mechanism.

## Industry adoption

Universally adopted in North American refining and petrochemical industries as the PMI execution standard. Widely cited internationally via owner-user programmes. Industry incident reviews (notably the 2009 Tesoro Anacortes naphtha-hydrotreater rupture investigated by CSB) drove broad adoption of 100% PMI on chrome-moly hydroprocess piping circuits.

## Why this page exists

W215 (iter-46) flagged API RP 578 as a missing API inspection-domain slug heavily cross-referenced from concepts/{fitness-for-service, risk-based-inspection, corrosion-rate-measurement} but lacking a first-class standards page. This resolver closes the substrate gap and provides the canonical-slug entry point for citation pinning.

## Where to find the full text

Publisher catalog: <https://www.api.org/products-and-services/standards>. RP 578 is sold individually and in API Inspection Practices packages.

## Cross-references

- [api-rp-577](api-rp-577.md) — welding inspection and metallurgy; weld-filler-metal verification companion practice.
- [api-510](api-510.md) — pressure-vessel inspection code; consumes PMI findings during in-service inspection.
- [api-570](api-570.md) / [api-std-570](api-std-570.md) — piping inspection code; primary in-service consumer of PMI findings.
- [api-653](api-653.md) / [api-std-653](api-std-653.md) — tank inspection code; PMI applies to alloy-clad and alloy-internals verification.
- [api-rp-572](api-rp-572.md) — pressure-vessel inspection practice; cites PMI as inspection-data source.
- [api-rp-580](api-rp-580.md) / [api-rp-581](api-rp-581.md) — RBI methodology; alloy mix-up is a credible damage-introduction mechanism in POF updating.
- [api-rp-941](api-rp-941.md) — Nelson curves for HTHA service; high-temperature hydrogen service is a primary high-criticality PMI target.
- [api-rp-571](api-rp-571.md) — damage mechanisms; the credible-mechanism catalogue that drives alloy-criticality screening.
- [fitness-for-service](../concepts/fitness-for-service.md) — concept anchor for FFS workflow consuming verified material data.
- [risk-based-inspection](../concepts/risk-based-inspection.md) — concept anchor for RBI consuming PMI findings.
- [corrosion-rate-measurement](../concepts/corrosion-rate-measurement.md) — concept anchor; alloy substitution can confound corrosion-rate calculations.
- [og-standards-api](../sources/og-standards-api.md) — parent source page.
- Calc citation contract: `.claude/rules/calc-citation-contract.md` — emit a `Citation(...)` whenever a calc module hard-codes an RP 578 sampling-extent rule or alloy-criticality threshold.

**Cross-wiki (maritime-law)** *(where PMI/material-traceability gates chemical-tanker pollution-prevention compliance)*

- [marpol-73-78](../../../maritime-law/wiki/standards/marpol-73-78.md) — **bidirectional bridge**: API RP 578 Material Verification Program (PMI / alloy verification via XRF and OES) for chemical-tanker piping and cargo-containment systems gates the **material-traceability** required by **MARPOL Annex II** (Noxious Liquid Substances in Bulk) — the operational discharge regime tied to the **IBC Code** (International Code for the Construction and Equipment of Ships Carrying Dangerous Chemicals in Bulk) under SOLAS Ch. VII Part B. IBC Code material-of-construction requirements (Chapter 6 — materials of construction; Chapter 7 — cargo containment) prescribe specific alloys (e.g., 316L stainless for category-X/Y noxious liquids, duplex stainless for chloride-containing services, nickel alloys for sour-service residues), and **MARPOL Annex II prewash-cycle and discharge-criteria compliance presumes the cargo-handling system actually contains the specified material**. **PMI ensures material-of-construction matches documentation** — closing the alloy-mix-up failure mode that would silently invalidate the Annex II compliance regime. Annex II-relevant failure modes traceable to material-misidentification include **sour-service hydrogen-induced cracking (HIC/SOHIC)** in cargo-tank piping, **chloride stress-corrosion cracking (SCC)** in austenitic stainless lines exposed to seawater-residue + chloride-containing cargo, and **naphthenic-acid corrosion** in slop-tank and cargo-heating coils — each of which can fail-open the cargo containment and trigger an Annex II reportable discharge. RP 578's alloy-criticality screening, 100%-PMI rules for high-criticality alloys, and weld-filler-metal verification close the upstream-construction gap that the MARPOL Annex II IOPP/NLS-certificate survey regime presumes is closed. The pairing is the construction-stage analogue to the API RP 571 ↔ MARPOL bridge (post-incident damage-mechanism diagnosis): **RP 578 supplies pre-incident material-correctness assurance** whose absence the RP 571 mechanisms expose post-incident. Use the pairing for chemical-tanker construction-quality digests that link PMI non-conformance to MARPOL Annex II reportable-discharge exposure.
