---
title: "API RP 19B — Evaluation of Well Perforators"
code_id: api-rp-19b
publisher: API
revision: "to be verified at next ingest pass (most-recent edition tracked on api.org)"
jurisdiction: international
tags: [recommended-practice, api, perforating, shaped-charge, completions, ballistic-evaluation]
sources:
  - api-rp-19b
added: 2026-05-15
last_updated: 2026-05-15
---

# API RP 19B — Evaluation of Well Perforators

## Scope

API RP 19B is the practitioner-canonical recommended practice for the **evaluation** of well perforators — that is, the test methodology used to characterize shaped-charge performance for downhole perforating systems. It defines the standardized ballistic-test sections (variously identified as Sections I through V across editions) that produce the penetration and entrance-hole values quoted on charge data-sheets.

The standard does **not** prescribe perforation strategy or shot density for a given completion. Its scope is bounded to the test methodology that gives an apples-to-apples comparison between charges from different manufacturers, in different gun systems, under defined conditions. Operators then apply judgement (or proprietary modelling) to translate the RP-19B numbers into field expectations.

## Why operators read it

- **Vendor-comparison framework** — without a common test methodology, vendor-quoted penetration depths cannot be compared. RP 19B is the only widely-adopted standardised methodology.
- **Acceptance-test reference** — completion engineers specifying gun systems often write acceptance tests against RP 19B section thresholds.
- **Skin-prediction inputs** — perforation-skin models (Karakas–Tariq, McLeod, Locke) require entrance-hole diameter, penetration length, and shot phasing as inputs. The first two come from RP 19B testing.
- **Litigation and regulator audit trail** — when post-completion performance disputes arise (productivity below expectation, integrity event linked to perforation geometry), the RP-19B test records are the documentary fallback.

## Test-section structure (high level)

The standard defines a small number of distinct test configurations, each instrumented to capture a defined performance metric. The exact section labels and concrete numerical thresholds have evolved across editions and are not transcribed here (paywalled standard); the structural intent is stable:

- **Surface flat-target test** — charge fired into a stack of concrete or steel-cement composite at surface. Gives a vendor-comparable penetration length and entrance-hole diameter under standardized stand-off conditions. Largely a quality-control + vendor-comparison datum.
- **Stressed Berea-sandstone test** — charge fired through a casing-cement-formation sandwich with the formation core under confining pressure, simulating downhole conditions more faithfully. Penetration is shorter than the surface flat-target test (typically 50-70% on the same charge) because rock under stress resists better. This is the most operationally meaningful test section.
- **Casing-and-cement test** — measures entrance-hole diameter and the consistency of penetration through casing wall + cement sheath. Quality-control oriented.
- **Long-clearance variants** — capture charge performance with greater stand-off between gun and casing (relevant for big-bore casing with smaller-diameter guns).

Operators reading vendor data-sheets should always check which section produced each quoted number; the surface-test number is much larger than the stressed-rock number for the same charge, and conflating them inflates performance expectations.

## Concept-page references

- [Perforating](../concepts/perforating.md) — the production-engineering router page
- [Perforating — Shaped Charges](../concepts/perforating-shaped-charges.md) — charge mechanics
- [Perforation Strategy](../concepts/perforation-strategy.md) — shot density / phasing / EHD / EHL design
- [Perforating Gun Systems](../concepts/perforating-gun-systems.md) — TCP / wireline / CT-conveyed

## Cross-references

- **Adjacent standards** — API Spec 16A (BOP equipment, applicable to HPHT perforating operations), NACE MR0175 / ISO 15156 (sour-service material requirements applicable to perforating-tool metallurgy)
- **Drilling-engineering** — [Casing Program Design](../../../drilling-engineering/wiki/concepts/casing-program-design.md) (perforation policy interacts with the burst-rating margin of the production casing)
- **Vendor-archetype framing** — gun-system manufacturers (Halliburton, Schlumberger, Baker Hughes, Owen Oil Tools, GEODynamics, DynaEnergetics) publish charge data-sheets citing RP-19B section numbers; concept-level only, no proprietary content reproduced here.

## Public references

- **API** — official publication page for API RP 19B (current edition retrievable from api.org)
- **Bell, W. T. & Behrmann, L. A.** — *Perforating Applications in the Petroleum Industry* (SPE Reprint Series). The practitioner-canonical companion volume; explains the methodology context that RP 19B formalises.
- **SPE OnePetro perforating literature** — papers on RP-19B-section-method-vs-field-performance correlation, especially the late-1990s and 2000s sequence that drove the stressed-Berea variants into the methodology.
- **Behrmann, L. A.** — multiple SPE papers on shaped-charge performance evaluation methodology (1980s-1990s era).

## Notes

- RP 19B revisions have been issued multiple times since the 1990s. Operators specifying perforating-equipment acceptance tests should always pin to a specific edition in their AFE / scope-of-work documents.
- The standard's evolution has been driven by recognition that surface flat-target numbers overstate downhole performance. The stressed-Berea section was added precisely to give a more field-representative datum.
- API RP 19B is paywalled. This wiki paraphrases the structural intent and references the standard for operators who already have a licensed copy. No verbatim text reproduced.
