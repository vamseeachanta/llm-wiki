---
domain: reservoir-engineering
created: 2026-05-16
last_updated: 2026-05-16
---

# Overview: Reservoir Engineering (Formation-Evaluation Foundation)

> **Scope-narrow notice.** This wiki was founded 2026-05-16 with a deliberately narrow initial scope: **formation evaluation** as a foundation for the [Kaggle ROGII 2026 competition](https://github.com/vamseeachanta/kaggle-rogii-2026/issues/5) modeling work. It is NOT a full reservoir-engineering domain founding. Core reservoir-engineering topics — relative permeability, capillary pressure, recovery factor, material balance, decline-curve analysis, well-test interpretation, PVT analysis — are **explicitly deferred** to future plans. See [Scope (out)](#scope-out) below for the deferred list.

This wiki captures **reservoir-engineering / formation-evaluation foundation** content — the rock-property and log-interpretation surface that horizontal-well placement, geosteering, and stratigraphic correlation all consume. It is the 11th llm-wiki domain.

## Strategic role

Founded 2026-05-16 as the 11th llm-wiki domain, under user-approved plan [#40](https://github.com/vamseeachanta/llm-wiki/issues/40) (approval marker `.planning/plan-approved/40.md`, dated 2026-05-16). The plan body resolved a scope-decision: instead of founding a full reservoir-engineering domain in one plan (which would duplicate effort with the parallel `#2667 Domain Knowledge Sweep`), the plan narrows to a formation-evaluation foundation driven by the Kaggle ROGII competition's modeling needs (porosity, permeability, gamma-ray log interpretation, dip-azimuth, formation tops, geosteering workflow, log correlation).

This founding completes a partial value-chain bridge:
- `drilling-engineering/concepts/formation-evaluation-basics.md` already covers the well-construction-time framing ("what does the LWD tool tell me about the formation while I'm still drilling?").
- This wiki adds the reservoir-side complement ("what does the openhole / LWD log tell me about the rock as a reservoir-property substrate?").
- The bidirectional cross-link between the two is the value-chain hand-off the founding plan anticipated.

### Coordination with `#2667` Domain Knowledge Sweep

The [Domain Knowledge Sweep parent issue](https://github.com/vamseeachanta/workspace-hub/issues/2667) launched Domain 1 (Hydrodynamics, `#2668`) on 2026-05-12. Reservoir engineering is a likely future domain in that sweep. **The two scopes are designed to partition cleanly**:

- **This wiki (formation-evaluation foundation)** — porosity, permeability, gamma-ray log interpretation, dip-azimuth, formation tops, geosteering workflow, log correlation. Driven by Kaggle ROGII modeling needs.
- **`#2667` (when it reaches reservoir-eng)** — recovery factor, EOR design, simulation, material balance, decline-curve analysis, well-test interpretation, PVT. The reservoir-engineering substrate.

If `#2667` does reach reservoir-engineering, future plans against this wiki MUST verify boundary alignment before scope-expansion, to avoid two parallel initiatives duplicating effort.

## Scope (in)

- **Foundational rock properties** — porosity (definitions, types, measurement), permeability (Darcy framework, units, measurement)
- **Open-hole log interpretation (foundational)** — gamma-ray log (lithology indicator + shale-volume estimator); density / neutron / sonic / NMR for porosity; resistivity for saturation (named at concept level here; deep coverage staged for follow-up plans)
- **Dip and azimuth** — structural-geology surface needed for horizontal-well placement
- **Formation tops** — stratigraphic correlation surface
- **Geosteering workflow** — methodology overlay; horizontal-well placement using LWD response as the steering input
- **Log correlation** — methodology overlay; well-to-well stratigraphic alignment

## Scope (out)

Explicitly deferred from this founding plan — may be covered by future plans or by `#2667 Domain Knowledge Sweep` when it reaches reservoir engineering:

- **Relative permeability** (k_rw, k_ro, k_rg curves; Corey models; Brooks-Corey; LET; SCAL methodology). The absolute-vs-effective-vs-relative scope-distinction is *named* in `concepts/permeability.md` with a placeholder cross-link, but no relative-perm content is drafted.
- **Capillary pressure** (P_c curves, J-function, leverett scaling, mercury-injection / centrifuge / porous-plate measurement)
- **Recovery factor** (RF estimation by reservoir type and drive mechanism)
- **Material balance** (Tarek Ahmed, Havlena-Odeh, F-vs-E plotting)
- **Decline-curve analysis** — Arps three-form decline (exponential / hyperbolic / harmonic) coverage already exists in `production-engineering/concepts/production-history-decline-analysis.md` as it applies to refrac candidate-selection; full DCA-as-reservoir-engineering-tool is deferred here.
- **Well-test interpretation** (PBU, DST, IPR analysis from transient pressure data; Horner plot; type-curve matching; Bourdet derivative)
- **PVT analysis** (CCE / DL / CVD lab tests; black-oil PVT functions; EOS modeling)
- **Reservoir simulation** (finite-difference / streamline / unstructured-grid; EOR design via simulation)
- **Reservoir geophysics at the seismic-acquisition level** — would belong in a future `seismic-interpretation/` domain (not yet founded)

## Cross-wiki anchor map

- **`drilling-engineering/`** — `concepts/formation-evaluation-basics.md` (the well-construction-time view of formation evaluation; bidirectional cross-link), `concepts/directional-drilling.md` (horizontal-well placement context), `concepts/mwd-lwd-overview.md` (the sensor systems that produce the logs this wiki interprets), `concepts/well-plan.md` (formation-tops feed the well-plan trajectory).
- **`production-engineering/`** — `concepts/perforation-strategy.md` (perforation interval selection consumes formation-tops + porosity + permeability outputs).
- **`engineering-standards/`** — API RP 40 (core analysis recommended practices), SPWLA formation-evaluation references (paywalled), CWLS LAS file format (open), SEG-Y format spec (open).
- **`kaggle-rogii-2026/`** — the founding-driver companion repo; `geosteering-workflow.md` + `dip-azimuth.md` are the educational substrate for that competition's modeling work.

## Seed roadmap (founding + near-term)

Phases below describe **formation-evaluation foundation scope only**. Full reservoir-engineering substrate phases are intentionally absent from this roadmap; they belong to future plans (see [Scope (out)](#scope-out)).

### Phase 1 (Wave 1, this founding session) — structural scaffold + foundational rock properties

1. CLAUDE.md (schema)
2. wiki/overview.md (this page)
3. wiki/index.md
4. wiki/log.md
5. concepts/porosity.md (foundational rock property)
6. concepts/permeability.md (foundational rock property)

### Phase 2 (Wave 2) — corpus manifest

7. `docs/research/reservoir-engineering-corpus.md` — license-triaged ingest-candidate manifest per plan acceptance criterion ≥30 high-quality OR ≥50 mixed-quality sources

### Phase 3 (Wave 3) — remaining founding concept pages

8. concepts/gamma-ray-log-interpretation.md
9. concepts/dip-azimuth.md
10. concepts/formation-tops.md

### Phase 4 (Wave 4) — methodology pages

11. methodology/geosteering-workflow.md (the Kaggle-driver methodology page)
12. methodology/log-correlation.md

### Phase 5 (Wave 5) — standards-page anchors

13. standards/api-rp-40.md (core analysis — paywalled, paraphrase only)
14. standards/cwls-las-2.0.md (LAS file format — open standard; the de-facto wireline-log file interchange format)
15. standards/seg-y-rev2.md (SEG-Y format — open standard for seismic; named here as adjacency anchor)
16. standards/spwla-formation-evaluation.md (SPWLA references — paywalled, structural intent only)

Beyond Wave 5 is **future-plan scope**, not this founding plan's commitment.

## Founding-content anchor

The founding concept pages are [Porosity](concepts/porosity.md) and [Permeability](concepts/permeability.md) — the two foundational rock properties that every downstream formation-evaluation page consumes. Together they establish:

- The rock-storage-vs-rock-transport scope distinction (porosity = storage, permeability = transport).
- The measurement-method taxonomy (core analysis vs log analysis vs well-test derived; cross-link to `drilling-engineering/concepts/formation-evaluation-basics.md` for the LWD-time framing).
- The standards anchor (API RP 40 for core analysis) and the textbook reference set (Tiab & Donaldson, Cosentino, Ahmed — public textbook citations by name + ISBN, **not** ingested copies).

License-triage discipline (per plan #40 license-fail-closed posture): textbook references on the founding concept pages are NAME + ISBN references only — no ingested content. Vendor publications (Schlumberger *Log Interpretation Charts*) are cited by name with access-discipline note. Paywalled standards (API RP 40, SPWLA references) are paraphrased structurally only; no verbatim chunks > 30 words.
