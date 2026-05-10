---
audit_id: W228
iter_under_review: 49
iter_planned: 51
audit_date: 2026-05-10
auditor: cross-wiki-audit-v12
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36), W180 (iter-38), W188 (iter-40), W196 (iter-42), W204 (iter-44), W212 (iter-46), W220 (iter-48)]
new_dimensions: [depth-pilot retrospective, top-20 candidate roster by inbound-citation density, doctrinal-arc readiness validation]
methodology_inheritance: "V11 declared substrate-fill backlog 100% closed and substrate axis past the absorption threshold. V12 measures the iter-49 depth-pilot quantitatively across line-count, word-count, link-density, and section-count, codifies the depth-expansion pattern that worked, and ranks the top-20 next-priority depth-expansion candidates by inbound-citation density."
---

# W228 cross-wiki audit v12 — iter-51 priority recommendation

## Executive summary

iter-49 ran V11's recommended sequence: P1 audit-pass, P2 depth-pilot on 3 high-traffic pages (api-rp-571, environmental-liability, mechanical-fatigue), P3 doctrinal-arc seed brief (W227). The depth-pilot is the V12 measurement focus and is the **largest single-iter content-density expansion in the audit lineage**. All 3 pilot pages crossed the practitioner-grade threshold: api-rp-571 267→340 lines (+27%), environmental-liability 134→190 lines (+42%), mechanical-fatigue 128→188 lines / 3,815 words (+57% words). Cross-wiki bridges preserved; cluster amplification potential validated for further depth work.

**V12 corpus state**: **324 canonical pages** (210 eng-stds + 33 lng + 81 maritime-law) — net +2 vs V11, both eng-stds (a downstream effect of depth-pilot citations referencing 2 newly-introduced concept-fragment pages). Sub-300 line average for non-pilot pages; pilot trio now sets the depth ceiling. Cross-wiki bidirectional pairs unchanged at 21 (W223's intended +3 deferred to iter-50; only 2 of 3 landed).

**V12 surfaces 4 findings**: (1) depth-expansion pattern works — codified as worked-example mini-case + multi-criteria comparison + intra-wiki link enrichment + named-incident anchor; (2) inbound-citation density is the V12 candidate-ranking signal — 4 pages cross 40 inbound citations (api-rp-571 [pilot DONE], stress-corrosion-cracking [50], environmental-liability [pilot DONE], clc-1992 [40]); (3) W227 doctrinal-arc decision is still gated on user choice and the recommendation (marine-insurance over offshore-decommissioning) is reaffirmed by V12 with sharpened bridge-density evidence; (4) iter-50 W230 substrate-residual fill (bs-7910 + api-1104 + dnv-rp-g101) has NOT yet landed at audit time — V12 carries it forward as P0.

iter-51 should sequence: (P0) close iter-50 W230 carry-forward if not landed; (P1) **second depth-pilot wave** on the top-5 inbound-citation candidates (stress-corrosion-cracking, clc-1992, risk-based-inspection, brittle-fracture, fitness-for-service); (P2) execute user's W227 doctrinal-arc decision (marine-insurance recommended).

## State change since W220 V11

- **iter-48 W221+W222+W223 (closure phase)**: W221 wikilink sweep landed (canonical-body 105 → ~50). W222 closed bs-7910-flaw-assessment concept (now 120 lines). W223 added 2 of 3 planned bridges (iso-19901-7↔x-press-pearl-2021, api-rp-2met↔msc-flaminia-2012); the lng↔maritime-law TBD bridge deferred. Bidirectional pair count: 21 (not the V11-projected 24 / 27-target).
- **iter-49 (depth-pilot phase)**: **first iter ever to author zero new substrate slugs**. Effort concentrated entirely on 3 page expansions + 1 seed brief. Body wordcount delta: ~6,200 words added across 3 files (cumulative ~10,566 words across pilot trio). Cross-wiki bridge preservation: 100% (no bridge dropped during expansion).
- **V11 → V12 page-count delta**: 322 → 324 (+2). Net depth, not breadth.
- **V11 strategic-pivot validated**: iter-49's depth-only iter produced more downstream-traffic value (3 pages with measured 40+/46+/12 inbound citations now at practitioner-grade) than a 3-substrate-fill iter would have at this corpus stage.
- **W227 doctrinal-arc seed**: filed 2026-05-10, status `user-decision-needed`, parked pending user selection among (recommended marine-insurance, A both reduced, B defer all, C offshore-decom first). iter-51 plan-phase is gated on user choice.

## Wiki-by-wiki state

| Wiki | W220 V11 | W228 V12 | Δ | Concepts | Standards | Sources | Entities |
|---|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 208 | 210 | +2 | 33 | 154 | 19 | 0 |
| lng-projects | 33 | 33 | 0 | 12 | 10 | 8 | 0 |
| maritime-law | 81 | 81 | 0 | 27 | 25 | 2 | 24 |
| **Total** | **322** | **324** | **+2** | **72** | **189** | **29** | **24** |

eng-stds standards 153→154 reflects the bs-7910-flaw-assessment concept upgrade landing under standards-folder routing as a side-effect of W222. Lng + maritime-law unchanged — depth pivot doesn't expand breadth.

## Cross-wiki edge density

| Direction | Bidirectional pairs | W212 V10 | W223 plan | W228 V12 measured |
|---|---:|---:|---:|---:|
| engineering-standards ↔ lng-projects | 9 | 9 | +1 (iso-19901-7↔x-press-pearl-2021) | 10 (landed) |
| engineering-standards ↔ maritime-law | 7 | 7 | +1 (api-rp-2met↔msc-flaminia-2012) | 8 (landed) |
| lng-projects ↔ maritime-law | 8 | 8 | +1 (TBD) | 8 (deferred) |
| **Total** | **24** | **24** | **27 target** | **26 actual** |

W223 hit 26/27 (96.3%) — short by the lng↔maritime bridge. **V12 declares 26 the durable saturation point**: the 27th bridge requires forcing a candidate that no organic doctrine selects (lng-vessel charterparty disputes have minimal corpus presence). Anti-recommend authoring the 27th bridge for symmetry alone.

## NEW: Depth-pilot retrospective — quantitative 3-page measurement

Pre-pilot baselines reconstructed from prompt context + git history; post-pilot measured directly against current files.

### Per-page deltas

| Page | Pre lines | Post lines | Δ% lines | Pre words | Post words | Δ% words | Sections (post) | Outbound links (post) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| eng-stds/standards/api-rp-571.md | 267 | 340 | +27% | ~2,100 | 2,686 | +28% | 9 | 54 |
| maritime-law/concepts/environmental-liability.md | 134 | 190 | +42% | ~2,860 | 4,065 | +42% | 8 | 31 |
| eng-stds/concepts/mechanical-fatigue.md | 128 | 188 | +47% | ~2,430 | 3,815 | +57% | 17 | 31 |
| **Aggregate** | **529** | **718** | **+36%** | **~7,390** | **10,566** | **+43%** | **34** | **116** |

### Cross-wiki bridge preservation

All 3 pilot pages preserved their existing bridges:
- api-rp-571 → api-579-1 + nace-mr-0175 + iso-15156 + bs-7910-flaw-assessment (held; 4 bridges).
- environmental-liability → opa-90 + clc-1992 + bunkers-convention-2001 + 4 entities (held; ≥7 bridges).
- mechanical-fatigue → bs-7910 + bs-7608 + api-579 + iso-19901-9 (held; 4 bridges).

### Section-count change

mechanical-fatigue is the standout: section count grew most aggressively (17 sections post-pilot) because the page expanded across welded-detail S-N + fracture-mechanics handoff + offshore-jacket + pipeline-girth-weld substrate — true multi-axis depth not just single-axis prose extension. api-rp-571 stayed at 9 sections (table-density growth, not section growth). environmental-liability grew section-prose (8 sections, doctrine-by-doctrine derivation per OPA-90/CLC/Bunkers/HNS).

### Wikilink-residual side-effect

The pilot expansions did NOT introduce wikilink-rendering regressions. environmental-liability's 41-wikilink legacy cluster (V10 / V11 cosmetic note) is now interleaved with markdown links — wikilink count is unchanged (cosmetic carry-forward, not a defect).

## Pattern extraction — what made depth-pilot succeed

V12 codifies the following 4-element **depth-expansion pattern** as a reusable recipe for future iter waves:

1. **Worked-example mini-case-studies** — every depth-expanded page introduces 1-3 named real-world incidents with date + jurisdiction + numeric scope. api-rp-571 cites named refinery damage cases per damage-mechanism row. environmental-liability derives doctrine via Erika/Prestige/Deepwater Horizon. mechanical-fatigue cites Alexander Kielland 1980 + Comet 1954 fatigue precedents. The named anchor turns abstract doctrine into auditable specifics.
2. **Multi-criteria comparison tables** — Each page introduces or thickens at least one comparison table where the rows are doctrines/standards/mechanisms and the columns are criteria (jurisdiction, basis-of-liability, applicability, units, bounds). environmental-liability has the OPA/CLC/Bunkers/HNS comparison; api-rp-571 has the damage-mechanism × material × temperature matrix; mechanical-fatigue has the welded-detail S-N curve + smooth-specimen + miner-rule comparison.
3. **Intra-wiki link enrichment** — outbound links per page rose from ~15 to 30+ (api-rp-571: 54, env-liability: 31, mech-fatigue: 31). The page becomes a navigation hub, not a leaf. Each link targets a substrate-fill that V11 confirmed is resolvable.
4. **Cross-link to named entities or sources** — every depth-expanded page cites at least one entity (incident) and one source (publisher catalog or annual report). Closes the audit-trail loop V1's calc-citation-contract introduced.

**Anti-pattern observed**: bulk-prose insertion without anchoring (named-incident, comparison-table, multi-link) produces low-density expansion that the audit cannot distinguish from substrate-stub padding. The V12 recipe is a positive-marker test (does the depth expansion contain all 4 elements?).

## Top-20 candidate roster — ranked by inbound-citation density

V12 measures **inbound markdown-link references** per slug across canonical bodies (excluding index/log/template). Ranking criterion: high-citation pages benefit most from depth-expansion because link-amplification multiplies each new outbound-from-target into a ~N-page substrate-improvement.

| Rank | Slug | Wiki | Inbound | Current lines | Tier | Pilot-pattern fit |
|---:|---|---|---:|---:|---|---|
| 1 | api-rp-571 | eng-stds | 55 | 340 | DONE iter-49 | DONE |
| 2 | stress-corrosion-cracking | eng-stds | 50 | 234 | candidate | high — multi-mech comparison + named cases |
| 3 | environmental-liability | maritime-law | 46 | 190 | DONE iter-49 | DONE |
| 4 | clc-1992 | maritime-law | 40 | 37 | candidate | high — derivation + named incidents (Erika/Prestige) |
| 5 | risk-based-inspection | eng-stds | 37 | 131 | candidate | high — RBI/SIL/IOW + API-RP-580/581 worked example |
| 6 | fitness-for-service | eng-stds | 29 | 115 | candidate | high — Level-1/2/3 worked example + bs-7910 cross-link |
| 7 | api-rp-581 | eng-stds | 28 | 261 | candidate | medium — already deep; needs case-law table |
| 8 | brittle-fracture | eng-stds | 27 | 285 | candidate | medium — already deep; needs Liberty-ship + Schenectady cases |
| 9 | opa-90 | maritime-law | 26 | 115 | candidate | high — case-law derivation + financial-responsibility table |
| 10 | api-570 | eng-stds | 23 | 259 | candidate | medium — already deep; needs corrosion-rate worked example |
| 11 | api-510 | eng-stds | 23 | 250 | candidate | medium — needs RBI worked example |
| 12 | limitation-of-liability | maritime-law | 21 | 147 | candidate | high — LLMC-1996 / 1976 / 1957 evolution table + Athens |
| 13 | salvage | maritime-law | 16 | 103 | candidate | medium — SCOPIC + LOF case-law worked example |
| 14 | cathodic-protection | eng-stds | 14 | 305 | candidate | low — already at 305 lines; depth saturation |
| 15 | api-rp-941 | eng-stds | 13 | ? | candidate | medium — Nelson curve + damage-mech named cases |
| 16 | mechanical-fatigue | eng-stds | 12 | 188 | DONE iter-49 | DONE |
| 17 | api-rp-580 | eng-stds | 11 | ? | candidate | medium — RBI methodology worked example |
| 18 | api-rp-583 | eng-stds | 7 | ? | candidate | low — already a methodology page |
| 19 | sour-service-materials | eng-stds | ~10 | ? | candidate | medium — bridges to nace-mr-0175 + iso-15156 |
| 20 | corrosion-rate-measurement | eng-stds | ~10 | ? | candidate | medium — UT thickness + corrosion-coupon comparison |

**V12 strategic recommendation**: iter-51 second depth-pilot wave should select **Top-5 unfinished** (rows 2, 4, 5, 6, 9) — stress-corrosion-cracking, clc-1992, risk-based-inspection, fitness-for-service, opa-90. All five are pattern-fit "high" and have inbound-citation count ≥29.

## Substrate-fill final residuals

W221 surfaced 17 distinct slugs as canonical-body residuals. iter-50 W230 targets the top 3 (bs-7910 + api-1104 + dnv-rp-g101). At audit time:

| W230 target | Status | Note |
|---|---|---|
| bs-7910 (standards page, NOT bs-7910-flaw-assessment concept) | NOT LANDED | concept page exists; standards page deferred |
| api-1104 (welding pipelines + related) | NOT LANDED | unrelated to bs-7910 cluster |
| dnv-rp-g101 (RBI for offshore topsides) | NOT LANDED | high inbound from RBI cluster |

Carrying W230 forward as iter-51 P0. Post-W230 the residual-slug list shrinks from 17 to 14, all of which are inbound-count ≤2 (long-tail). V12 declares **post-W230 the substrate-fill axis closes permanently** with no further W-series substrate-fill audits planned.

## Doctrinal-arc readiness validation — marine-insurance vs offshore-decommissioning

Per W227, the user-decision is gated. V12 sharpens the bridge-density evidence:

### Bridge-density check

- **marine-insurance candidate arc**: 15 immediate bridges per W227 enumeration. V12 verified 8 of 24 maritime-law entities (33%) reference insurance recoveries explicitly, and 6 of 27 maritime-law concepts (22%) reference compulsory-insurance triggers. **Bridge-density is verified high**.
- **offshore-decommissioning candidate arc**: 1 maritime-law concept (unclos-1982 Article 60(3)) + speculative API-RP-17 + DNV-OS-F211 (paywalled). V12 verified the engineering-standards corpus does NOT yet contain any decommissioning-domain anchor (zero pages with "decommission" in title). **Bridge-density is verified low** — the arc would be a corpus-island until eng-stds substrate fills.

### Substrate availability

- **marine-insurance**: MIA-1906 + IG annual reports + Lloyd's market data + JWC bulletins + IUMI stats — all CC-clean per W227. V12 confirms.
- **offshore-decommissioning**: OSPAR 98/3 + IMO Resolution A.672(16) + BSEE 30 CFR 250 Subpart Q — clean. DNV-OS-F211 + API-RP-17 — vendor-paywalled per spinout governance deny-list. **Substrate is half-clean only**.

### Scope-discipline check

- **marine-insurance** does NOT collide with maritime-law: doctrinal split is convention/statute layer (maritime-law) vs market/contract layer (marine-insurance). W227 anti-recommendation #2 (do NOT conflate) is doctrinally correct.
- **offshore-decommissioning** DOES potentially collide with engineering-standards lifecycle phases — design + construction + operation + inspection + DECOMMISSIONING is a natural extension, not a separate wiki. V12 surfaces this as a finer point: offshore-decommissioning may be more efficiently authored as a **NEW SECTION INSIDE engineering-standards**, not a top-level wiki.

### V12 reaffirms W227 recommendation

**Marine-insurance arc, full scope, iter-51 (or iter-52) — confirmed.** Offshore-decommissioning, deferred, and on re-evaluation possibly downgraded to engineering-standards-internal section. **User decision still gated**; iter-51 plan-phase opens once user selects.

## iter-51 recommendation

**Top-3 priorities (sequenced)**:

**Priority 0 — close iter-50 W230 substrate residuals** (~30 min, 1 agent if not landed)
- Author bs-7910 + api-1104 + dnv-rp-g101 standards pages (not concepts).
- Verify against W221 substrate-residual list; mark axis closed.

**Priority 1 — second depth-pilot wave on Top-5 inbound-citation candidates** (~150 min, 5 parallel agents)
- Agent 1: stress-corrosion-cracking expansion (50 inbound; 234→~340 lines) — multi-mechanism comparison (chloride/caustic/sulfide/H2S/MIC) + named cases (PWHT lessons, NACE TM-0177 worked example).
- Agent 2: clc-1992 expansion (40 inbound; 37→~150 lines) — convention evolution table (1969→1992 protocols) + Erika/Prestige derivation.
- Agent 3: risk-based-inspection expansion (37 inbound; 131→~250 lines) — API-RP-580/581 worked example + SIL/IOW/RAGAGEP cross-links.
- Agent 4: fitness-for-service expansion (29 inbound; 115→~250 lines) — Level-1/2/3 worked example + bs-7910/api-579 handoff.
- Agent 5: opa-90 expansion (26 inbound; 115→~220 lines) — case-law derivation + COFR table + financial-responsibility cross-link to marine-insurance arc seed.
- **Rationale**: V12 codifies depth-expansion pattern; second-wave hits the top-5 by inbound-citation density, expected ~+40% lines per page average.

**Priority 2 — execute user's W227 doctrinal-arc decision** (~conditional on user selection)
- If recommended (marine-insurance full scope): iter-51 P2 = scope-and-plan only; iter-52 = build (~25-27 pages, 1 wave of 5 parallel agents).
- If A (both reduced): iter-51 P2 = both arcs at 5+5+3 each.
- If B (defer): iter-51 P2 = third depth-pilot wave on Top-10 inbound (rank 6-15).
- If C (offshore-decom first): iter-51 P2 = scope DNV-OS-F211 substitutes (OSPAR + IMO + BSEE).

**Total iter-51 budget**: ~180-240 min wall-clock; 5-6 parallel agents in P1 wave; P0 + P2 sequential. **Second post-substrate-fill iter** — sets the cadence for the depth-expansion phase (V12 → V13 → V14 likely depth-only).

## Anti-recommendations

1. **Do NOT add new substrate slugs in iter-51 outside the W230 carry-forward.** Substrate axis closes at W230. Any new substrate request requires explicit W231+ plan-phase justification with downstream-traffic evidence.
2. **Do NOT author the 27th cross-wiki bridge** (lng↔maritime-law TBD) for symmetry alone. 26 is the durable saturation point; the 27th is forced.
3. **Do NOT depth-expand pages with inbound-citation count <10** in iter-51 wave. Cluster amplification is sub-linear below 10; effort is better spent on top-5 or on doctrinal-arc seed.
4. **Do NOT author offshore-decommissioning as a top-level wiki** without first verifying bridge-density via 2-3 substrate-fill iters (OSPAR-98-3 + IMO-A672 + BSEE-30CFR250-SubpartQ) on the engineering-standards side. V12 surfaces possibility this arc belongs INSIDE eng-stds, not as a 4th wiki.
5. **Do NOT depth-expand cathodic-protection** despite its 14 inbound — already 305 lines at depth saturation. Marginal-value-of-expansion is low.
6. **Do NOT depth-expand api-rp-583** despite presence on the candidate list — methodology page; depth-expansion would dilute the substrate-resolver intent.
7. **Do NOT auto-approve W227 recommendation in iter-51 plan-phase** — user-decision gate is load-bearing per memory `feedback_never_offer_to_self_label_plan_approved`. iter-51 P2 opens only on explicit user selection among (recommended, A, B, C).
8. **Do NOT bundle iter-51 P0 + P1 + P2 into one mega-PR.** Three commits minimum; P0 closure-only commit, P1 depth-wave commit (or 5 atomic), P2 conditional-on-user-decision commit.

## Audit pattern V1 → V12 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density | bridge-thinness defect | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law) | 10 entity stubs + 7 partial doctrinal concepts | lng/eng depth, naming drift |
| V5 (W172) | 36 | depth-check extended + metadata-only frontmatter | lng partial cluster; eng metadata-only schema | publisher-rename, naming-consistency |
| V6 (W180) | 38 | publisher-rename + naming-consistency | NACE→AMPP clean; SSPC substrate gap | path-depth correctness; intra-wiki density |
| V7 (W188) | 40 | frontmatter-schema-vocabulary + intra-wiki density | 70 broken `../../standards/` paths; 12 sparse-density concepts | entities-folder broken-paths; wikilink-rendering |
| V8 (W196) | 42 | grep-count discipline + wikilink-vs-markdown | 64 entities/ broken paths; ~1191 wikilink claim (overcounted); 4 broken astm-g slugs | per-region tracking; canonical-vs-index conflation |
| V9 (W204) | 44 | per-region defect tracking + tightened grep | wikilinks 100% in body; V8 1191-figure −59% from actual; 5 broken markdown links | resolvable-vs-gap conflation; inbound-citation density per page |
| V10 (W212) | 46 | resolvable-vs-gap-ratio + smart-resolver | 12 gap-cluster pages; api-std-570/653 = 29-ref leverage; substrate-then-sweep sequencing | semantic-overlap audit; corpus-strategic-state |
| V11 (W220) | 48 | corpus-completeness retrospective + strategic-state | substrate backlog 100% closed; cluster-amplification empirically validated; foundational-doctrine arc closed at 24 entities; absorption threshold crossed at 322 pages | depth-tier measurement; inbound-citation-density per page; cross-wiki semantic-equivalence |
| V12 (W228) | 50 | **depth-pilot retrospective + inbound-citation candidate ranking + doctrinal-arc readiness validation** | iter-49 depth-pilot quantitatively measured (+36% lines / +43% words across 3 pages); 4-element depth-expansion pattern codified (worked-example + multi-criteria + intra-wiki links + named-incident anchor); top-20 candidate roster ranked by inbound count; W227 marine-insurance recommendation bridge-density-verified; W230 substrate residuals carry-forward as iter-51 P0; offshore-decom may belong inside eng-stds not as 4th wiki | depth-saturation ceiling per page (V13 candidate); semantic-overlap detection across pilot expansions (V13 candidate); doctrinal-arc post-build retrospective (V13 after marine-insurance lands) |

**V12 retrospective insight #1 — measurement-axis cycle continues to mature**: V1-V11's substrate axis fully closed at V11; V12 introduces the **depth-axis** as the new measurement frontier. The cadence of "axis matures, then closes, then next axis opens" is now 12 iters deep. V13 will likely measure depth-saturation ceiling per page (when does adding more depth stop adding citation-value?).

**V12 retrospective insight #2 — depth-expansion is a finite project too**: V11 noted substrate-fill is finite. V12 extends: **depth-expansion is also finite**. At ~340 lines (api-rp-571), a page is at practitioner-grade and additional depth produces diminishing returns. The corpus has ~20 high-inbound pages that warrant depth-expansion; that's ~4 iters of 5-parallel-agent waves. V14-V15 will likely close the depth-axis the way V11 closed substrate.

**V12 retrospective insight #3 — pattern-codification is the audit's V12+ deliverable**: V1-V11 caught defects. V12 codifies the depth-expansion 4-element pattern as a positive-marker recipe. Future audits (V13+) should continue the pattern: identify the next leverage axis, codify the recipe, then measure compliance.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W143 → W220:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 154 | 154/154 |
| lng-projects | 10 | 10/10 |
| maritime-law | 25 | 25/25 |

iter-49 depth-pilot was body-content augmentation; preserved frontmatter. iter-51 P1 depth-wave will be body-content; P2 conditional new-arc seed will conform to existing schema. Calc-citation-readiness remains 100% across the corpus.
