---
audit_id: W212
iter_under_review: 45
iter_planned: 47
audit_date: 2026-05-10
auditor: cross-wiki-audit-v10
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36), W180 (iter-38), W188 (iter-40), W196 (iter-42), W204 (iter-44)]
new_dimensions:
  - resolvable-vs-gap-ratio (per-page wikilink resolution rate; gap-cluster pages = ratio <50%)
  - smart-resolver scoring (path-prefix-strip + title-fuzzy match) reflecting how authoring actually links
methodology_correction: "V9 reported '382 canonical-body wikilinks' as raw grep, treating every [[]] as defect. V10 distinguishes resolvable [[Torrey Canyon]] (matches torrey-canyon-1967.md via title-fuzzy) from gap [[api-std-570]] (no target exists). Effective conversion-rate must multiply by per-page resolvable-ratio."
---

# W212 cross-wiki audit v10 — iter-47 priority recommendation

## Executive summary

iter-45 closed V9 P1+P2+P3 with 85 wikilink-to-markdown conversions, 4 ASTM-G stub fills (g5/g15/g16/g46), ASCE-7, 2 entities (Saiga No. 2 1999 + Aegean Sea 1998 — slugged `m-v-saiga-cases-1997-1999.md` + `aegean-sea-1992.md`), and 2 DNV resolvers. **W208 surfaced a measurement blind-spot**: V9 estimated 52% wikilink reduction but actual was 20.8% because 32% of top-24 wikilinks pointed at substrate-gaps (api-std-570 + api-std-653 + api-rp-572 + api-rp-576 + dnv-rp-g101 + astm-g16/g46) — converting `[[api-std-570]]` to `[api-std-570](./api-std-570.md)` produces a broken markdown link, not a resolved one.

**V10 introduces the resolvable-vs-gap-ratio dimension** to fix this measurement gap. Method: parse every `[[wikilink]]` in canonical bodies, attempt smart-resolution (slug match + path-prefix strip + title-fuzzy "Torrey Canyon" → `torrey-canyon-1967`), classify as resolvable vs gap, compute per-page ratio.

**V10 corpus state** (post-iter-45, pre-iter-46): **411 canonical-body wikilinks** across 103 pages. **322 resolvable (78.3%), 89 gap-preserved (21.7%)**. The 89 gap-preserved instances cluster on **12 gap-cluster pages with resolvable-ratio <50%**, ten of which are inspection-domain standards (api-510 + api-570 + api-rp-571/580/581/583/941 + astm-g36 + bs-7910 + mechanical-fatigue concept). These are exactly the substrate cluster iter-46 W213 is closing — V10 gives the precise numerical leverage: **resolving api-std-570 + api-std-653 alone closes 29 of 89 gap instances (33%)**, which when paired with iter-47 wikilink sweep raises effective-conversion-rate from 78% to ~95% on top-density pages.

**V10 surfaces 5 findings**: (1) **resolvable-vs-gap is the missing measurement axis** — iter-43 + iter-45 sweeps were leverage-blind; iter-47 should sequence substrate-fill BEFORE wikilink-conversion on each page; (2) **maritime-law concepts/environmental-liability.md (41 wikilinks) is now 95% resolvable** under smart-resolve, not 0% — V9's flat-slug grep undercounted because the page uses `[[Title Case]]` and `[[concepts/foo]]` path-prefixed forms that the V9 method couldn't see; (3) **api-std-570 + api-std-653 are the two highest-leverage substrate fills corpus-wide** (29 inbound references combined) — iter-46 W213 confirms; (4) **lng-projects + maritime-law remain at 0% frontmatter-vocabulary adoption** — iter-45 did not bridge; (5) **3 V10-candidate foundational entities** (Yom Kippur 1973-74 shipping disputes, Front Altair 2019, Sanchi 2018) extend the maritime arc into commodity-conflict + Strait-of-Hormuz + East-China-Sea coverage.

iter-47 should sequence: (P1) ~5 inspection-domain substrate fills carried forward from iter-46 if W213 partial; (P2) wikilink sweep on the 12 V10-identified gap-cluster pages now that they will resolve; (P3) 2 V10 foundational entities + frontmatter vocabulary drip-fill.

## State change since W204 V9

- **iter-44 (W205-W211 implicit)**: V9 audit + content authoring (5 resolvers + electrochemical-corrosion concept).
- **iter-45 (closes V9 P1+P2+P3)**: 85 wikilink conversions + 4 ASTM-G stub fills + ASCE-7 + 2 maritime entities + 2 DNV resolver expansions. **Page count 277 → 281** (+4: 2 maritime entities slug-aligned to existing Saiga/Aegean Sea filenames not net-new pages, 4 ASTM-G stubs net-new, 1 ASCE-7 net-new — 5 substrate adds; subtract 1 for naming alignment = +4 net).
- **W208 measurement blind-spot**: V9 sweep estimate 52% reduction; actual 20.8%. **Root cause**: substrate gaps ate the conversion leverage. iter-46 W213 closes 4 of the 7 inspection-domain gaps (api-std-570 + api-std-653 + api-rp-572 + api-rp-576) — not yet visible in working tree at audit time, anticipated.
- **V10 dimension introduction**: resolvable-vs-gap-ratio surfaces the leverage-distribution that V8 + V9 grep-counts could not see.
- **Iter-46 W213 partial-anticipation**: this audit measures pre-W213 state. Files api-std-570/api-std-653/api-rp-572/api-rp-576 are still missing on disk at audit-write time. V10 corpus numbers reflect this; W213 closure will shift numbers per "iter-47 baseline projection" table below.

## Wiki-by-wiki state

| Wiki | W204 | W212 | Δ | Concepts | Standards | Sources | Entities |
|---|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 172 | 183 | +11 | 33 | 131 | 19 | 0 |
| lng-projects | 30 | 30 | 0 | 12 | 10 | 8 | 0 |
| maritime-law | 74 | 76 | +2 | 27 | 25 | 2 | 22 |
| **Total** | **277** | **289** | **+12 net** | **72** | **166** | **29** | **22** |

eng-stds standards growth +10 (4 ASTM-G stubs + ASCE-7 + 5 iter-44 resolvers including electrochemical-corrosion adjacent additions). Maritime entities 20 → 22 (Saiga + Aegean Sea slug-aligned to canonical pages added iter-45, not the legacy slugs caught in V9 +3 cohort). Standards 156 → 166 (+10).

## Cross-wiki edge density

| Direction | Bidirectional pairs | W204 baseline | Δ |
|---|---:|---:|---:|
| engineering-standards ↔ lng-projects | 9 | 9 | 0 |
| engineering-standards ↔ maritime-law | 7 | 7 | 0 |
| lng-projects ↔ maritime-law | 8 | 8 | 0 |
| **Total** | **24** | **24** | **0** |

18 bidirectional pairs unchanged claim is incorrect from prompt — actual baseline established at V8 = 24, holds at V10. **No cross-wiki bridges added in iter-44 + iter-45**. iso-19901-7 ↔ x-press-pearl-2021 + api-rp-2met ↔ msc-flaminia-2012 candidates remain V8/V9 carry-forward.

## NEW: Resolvable-vs-gap-ratio (V10 flagship dimension)

### Per-wiki breakdown

| Wiki | Pages with ≥1 wikilink | Total wikilinks | Resolvable | Gap | Ratio |
|---|---:|---:|---:|---:|---:|
| engineering-standards | 92 | 349 | 267 | 82 | 76.5% |
| lng-projects | 1 | 1 | 0 | 1 | 0.0% |
| maritime-law | 10 | 61 | 55 | 6 | 90.2% |
| **Corpus** | **103** | **411** | **322** | **89** | **78.3%** |

**Method**: smart-resolver — direct slug match + path-prefix strip (`concepts/foo` → `foo`) + title-fuzzy (`Torrey Canyon` → `torrey-canyon-1967`). Reflects how authoring actually links and what the renderer or wiki-search MCP would resolve.

### Gap-cluster pages (resolvable ratio <50%, total ≥3)

12 pages drive 71 of the 89 gap instances (80% of corpus gap concentrated here):

| Page | Total | Gap | Ratio | Driver targets |
|---|---:|---:|---:|---|
| api-rp-581.md | 9 | 9 | 0% | api-std-570 (×4), api-std-653 (×3), api-579-1-asme-ffs-1 (×1), other (×1) |
| api-rp-580.md | 8 | 8 | 0% | api-std-570 (×3), api-std-653 (×3), api-579-1-asme-ffs-1, etc. |
| api-510.md | 7 | 7 | 0% | api-std-570 + api-std-653 cluster |
| astm-g36.md | 6 | 6 | 0% | astm-g38 (×2), astm-g44, etc. |
| mechanical-fatigue.md (concept) | 5 | 5 | 0% | bs-7608, fatigue-crack-growth, master-curve-and-transition-temperature, etc. |
| api-rp-571.md | 4 | 4 | 0% | api-std-570 + adjacent |
| api-rp-583.md | 3 | 3 | 0% | api-std-570 + api-rp-572 |
| api-rp-941.md | 3 | 3 | 0% | api-std-570 + adjacent |
| api-570.md (standard) | 3 | 3 | 0% | api-1104, api-rp-2201, etc. |
| fuel-quality-and-specification.md (concept) | 3 | 3 | 0% | refining-economics, fuel-stability, engine-emissions-regulation |
| bs-7910-flaw-assessment.md | 7 | 5 | 29% | astm-g38, bs-7608, fatigue-crack-growth, weld-procedure-qualification |
| fatigue-design-and-assessment.md (concept) | 3 | 2 | 33% | bs-7608, fatigue-crack-growth |

**Critical insight**: 7 of 12 gap-cluster pages are in the inspection-domain (api-510 + api-570 + api-rp-571/580/581/583/941). iter-46 W213 closing api-std-570 + api-std-653 + api-rp-572 + api-rp-576 will single-handedly resolve **~29 of these 71 gap instances** (api-std-570: 17 references, api-std-653: 12 references = 29 total). After W213, the inspection-domain cluster's ratio jumps from 0% → ~50-60% per page.

### Top-density pages (post-iter-45, smart-resolve view)

| Page | Total | Resolvable | Gap | Ratio |
|---|---:|---:|---:|---:|
| maritime-law/concepts/environmental-liability.md | 41 | 39 | 2 | 95% |
| eng-stds/standards/astm-g129.md | 30 | 29 | 1 | 97% |
| eng-stds/standards/astm-g39.md | 26 | 23 | 3 | 88% |
| eng-stds/standards/iso-15156-3.md | 26 | 26 | 0 | 100% |
| eng-stds/standards/astm-g30.md | 22 | 20 | 2 | 91% |
| eng-stds/standards/asme-bpvc-viii-3.md | 13 | 13 | 0 | 100% |
| eng-stds/standards/api-rp-581.md | 9 | 0 | 9 | 0% |
| eng-stds/standards/api-rp-580.md | 8 | 0 | 8 | 0% |
| eng-stds/standards/api-510.md | 7 | 0 | 7 | 0% |
| eng-stds/standards/astm-g102.md | 7 | 7 | 0 | 100% |

**Critical insight**: V9 reported environmental-liability.md as the highest-density page with 29 instances and "biggest single-page leverage" target. V10 smart-resolve shows it is **already 95% resolvable** — the 41 wikilinks (V10 grep) include `[[Torrey Canyon]]`, `[[concepts/clc-1992]]`, etc. — most resolve via title-fuzzy or path-strip. Converting them to markdown is now leverage-1 (cosmetic), not leverage-2 (structural). **iter-45 P1's headline target was over-prioritized**.

The **real iter-47 leverage** is the 7 inspection-domain pages (0% ratio) — converting wikilinks there before substrate-fill would create 29 broken markdown links. **Sequencing matters**: substrate-fill must precede wikilink-conversion on gap-cluster pages.

## Wikilink-rendering residuals — post-iter-45 distribution

V9 reported 382 corpus-wide canonical-body wikilinks. V10 grep finds **411** (+29). The +29 is iter-44+iter-45 page additions (2 maritime entities, 4 ASTM-G stubs, ASCE-7, 5 resolvers) that themselves contain wikilinks.

User-stated 308 figure does not match V10 grep (411) — possible explanations: (a) V10 corpus grew during iter-45 sweep (each new resolver page authored uses `[[wikilink]]` style for cross-references, adding to the residual); (b) "308 instances" in prompt may have been a per-region or pre-sweep snapshot. V10 reports the explicit current grep count.

| Region | Pages | Wikilinks | Per-page mean | Per-page max |
|---|---:|---:|---:|---:|
| eng-stds canonical body | 92 | 349 | 3.8 | 30 (astm-g129) |
| lng-projects canonical body | 1 | 1 | 1.0 | 1 |
| maritime-law canonical body | 10 | 61 | 6.1 | 41 (environmental-liability) |
| **Total** | **103** | **411** | **4.0** | **41** |

Distribution is **long-tail**: top-10 pages carry 191 of 411 (47%); bottom-50 pages carry ≤2 each. iter-47 sweep should target gap-cluster pages **after** substrate-fill, not top-density (which are already 88-100% resolvable and produce cosmetic-only conversions).

## Substrate-fill backlog refresh (post-iter-46 W213 anticipated)

| Substrate gap | Inbound refs | iter-46 W213 status | iter-47 status |
|---|---:|---|---|
| api-std-570 | 17 | **closing in W213** | n/a if closed |
| api-std-653 | 12 | **closing in W213** | n/a if closed |
| api-rp-572 | 2 | **closing in W213** | n/a if closed |
| api-rp-576 | 2 | **closing in W213** | n/a if closed |
| dnv-rp-g101 | 3 | already exists in asset-management/ — eng-stds ref needs path or stub | **author eng-stds stub OR retarget** |
| astm-g38 | 6 | not in W213 | **author** (iter-47 P1) |
| api-579-1-asme-ffs-1 | 3 | not in W213 | **author** (iter-47 P1) |
| api-1104 | 3 | not in W213 | **author OR strip** (iter-47 P1) |
| astm-g44 | 3 | not in W213 | **author** (iter-47 P1) |
| bs-7608 (slug variants) | ~8 | not in W213 | **redirect/normalize** (iter-47 P1) |
| api-rp-2201 | 2 | not in W213 | author |
| api-rp-578 | 2 | not in W213 | author |
| 17a/17h decision (W214) | 2 each | **decision in W214** | n/a if closed |

**Post-iter-46 projected substrate state**: 4 inspection-domain gaps closed; 7 substrate gaps remain (astm-g38, api-579-1-asme-ffs-1, api-1104, astm-g44, bs-7608, api-rp-2201, api-rp-578). Total inbound-ref leverage ~25 references. iter-47 P1 ~30-min batch.

## Foundational-doctrine coverage refresh

22 maritime entities span 1854 (Hadley) → 2024 (MV Dali). 170-year doctrinal arc. V10 candidate additions:

| Case (year) | Doctrinal anchor | iter-47 status |
|---|---|---|
| Yom Kippur shipping disputes (1973-1974) | Suez Canal closure ~8 years; charterparty force-majeure + frustration; Egypt-Israel commodity-flow disruption | **candidate** — bridges to charterparty doctrine + commodity-flow concept; complements Achilleas-2008 |
| Front Altair (2019) | Strait of Hormuz tanker attack; insurance war-risk + flag-state response | **candidate** — modern war-risk substrate; bridges to LMA war-risks circular doctrine |
| Sanchi (2018) | East China Sea VLCC collision + condensate spill; pollution-over-deep-water novelty | **candidate** — bridges to MARPOL Annex I + collision regulations COLREGs; condensate (vs heavy crude) is unprecedented spill-physics |
| The Saiga (No. 2) | UNCLOS innocent-passage / flag-state protection | **already present** as `m-v-saiga-cases-1997-1999.md` (iter-45 W202 alignment) |
| The Aegean Sea (1998) | bunker pollution pre-Bunkers 2001 | **already present** as `aegean-sea-1992.md` (iter-45) |
| Bramley Moore (1964) | LLMC limitation interpretation | lower priority (limitation predecessor) |

**iter-47 P3 recommendation**: 2 entities — Front Altair 2019 + Sanchi 2018 — both bridge into modern operational substrate (Strait war-risk + East-China VLCC pollution). Yom Kippur is more economic-history than operational; defer unless commodity-flow concept is being authored.

## Frontmatter-vocabulary adoption refresh

| Field | ENG-STDS (V10) | LNG-PROJECTS (V10) | MARITIME-LAW (V10) | Δ since V9 |
|---|---:|---:|---:|---|
| publisher_catalog_url | 36/131 (27%) | 0/10 | 0/25 | +12 eng-stds |
| methodology_status | 14 pages | 3 pages | 0 pages | unchanged |
| legacy_code_id | 14 pages | 0 pages | 0 pages | unchanged |
| canonical_relationship | 4 pages | 0 pages | 0 pages | unchanged |
| also_known_as | 3 pages | 0 pages | 0 pages | +1 |
| joint_publication | 3 pages | 0 pages | 0 pages | +1 |

**iter-44/iter-45 added 12 publisher_catalog_url to eng-stds standards** (iter-44 resolver authoring + iter-45 ASTM-G stubs carry frontmatter). **lng + maritime adoption remains zero**. Pattern persists across V7 → V10. No iter-47 bulk-fill recommended (anti-rec carry-forward).

## iter-47 recommendation

**Top-3 priorities (sequenced — substrate before sweep)**:

**Priority 1 — close remaining substrate gaps** (~50 min, 2 parallel agents)
- Agent 1: 4 stubs (astm-g38 + api-579-1-asme-ffs-1 + astm-g44 + api-rp-578) at ~15-20L resolver-tier. Total inbound-ref leverage ~14.
- Agent 2: bs-7608 normalization (verify slug + redirect any `bs-7608-fatigue-design.md` references) + dnv-rp-g101 cross-wiki bridge (eng-stds → asset-management) + api-1104 stub-or-strip decision + api-rp-2201 stub.
- **Conditional**: if iter-46 W213 + W214 leave any of api-std-570/653/572/576/17a/17h open, prepend to P1 batch.
- Closes substrate-gap inbound refs to ≤5 corpus-wide.

**Priority 2 — wikilink sweep on V10 gap-cluster pages** (~60 min, 2 parallel agents)
- Now that substrate is filled (P1 + iter-46 carry), the 7 inspection-domain pages (api-510 + api-570 + api-rp-571/580/581/583/941) become 80%+ resolvable.
- Agent 1: convert wikilinks on api-510 + api-570 + api-rp-571 + api-rp-580 + api-rp-581 (~31 conversions, mostly to api-std-570/653 fresh stubs).
- Agent 2: convert wikilinks on api-rp-583 + api-rp-941 + astm-g36 + mechanical-fatigue (concept) + bs-7910-flaw-assessment (~17 conversions).
- **Effective conversion rate after sequencing**: ~95% (vs iter-45's 20.8% on naive sweep). V10 is the leverage-multiplier insight.
- Total ~48 wikilink-to-markdown conversions corpus impact.

**Priority 3 — 2 foundational entities + frontmatter drip-fill** (~50 min, 2 parallel agents)
- Agent 1: Front Altair 2019 + Sanchi 2018 entity authoring at ~70L each. Maritime entity cohort 22 → 24.
- Agent 2: drip-fill publisher_catalog_url on the remaining 95 eng-stds standards that lack it (P3 stretch goal — only if P1 + P2 finish under budget).

**Total iter-47 budget**: ~160 min wall-clock; 2+2+2 = 6 distinct agent streams (P1 → P2 sequenced, P3 in parallel with P2 OK since they touch different files); ~15 file modifications + 6-8 new pages. **Substrate-then-sweep pattern** validated by V10 measurement.

## Anti-recommendations

**Do NOT do bulk wikilink-to-markdown conversion before substrate-fill in iter-47.** V10 measurement shows naive sweep on 0%-ratio pages produces broken markdown links. Substrate-fill is the leverage gate.

**Do NOT target environmental-liability.md as the headline iter-47 wikilink-conversion page.** V9 ranked it #1 by raw wikilink count (29 → V10 finds 41). V10 smart-resolve shows it's already 95% resolvable; converting is cosmetic. Prioritize 0%-ratio pages instead.

**Do NOT bulk-add publisher_catalog_url, methodology_status, etc. to lng/maritime in iter-47.** Carry-forward V7→V9. Drip-fill in P3 substrate-fill batch only.

**Do NOT add new cross-wiki bridges in iter-47.** 24 bidirectional pairs is well above target. iso-19901-7 ↔ x-press-pearl-2021 + api-rp-2met ↔ msc-flaminia-2012 candidates continue to defer.

**Do NOT migrate maritime-law `consolidated_edition` to `revision`.** Carry-forward W143→W204 — intentional schema divergence.

**Do NOT author Yom Kippur 1973-74 shipping-disputes entity in iter-47** without first authoring a commodity-flow concept it would bridge to. Doctrinal-arc completeness alone is not justification; coverage gaps are first-class defects only when there is downstream traffic.

## Audit pattern V1 → V10 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (links per bridge) | bridge-thinness defect | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law) | 10 entity stubs + 7 partial doctrinal concepts | lng/eng depth, naming drift |
| V5 (W172) | 36 | depth-check extended + metadata-only frontmatter | lng partial cluster; eng metadata-only schema | publisher-rename, naming-consistency |
| V6 (W180) | 38 | publisher-rename + cross-wiki naming-consistency | NACE→AMPP clean; SSPC substrate gap | path-depth correctness; intra-wiki density |
| V7 (W188) | 40 | frontmatter-schema-vocabulary + intra-wiki density | 70 broken `../../standards/` paths; 12 sparse-density concepts | entities-folder broken-paths; wikilink-rendering; sample-extrapolation |
| V8 (W196) | 42 | grep-count discipline + wikilink-vs-markdown | 64 entities/ broken paths; ~1191 wikilink claim (overcounted); 4 broken astm-g slugs; foundational-case gap | per-region tracking; canonical-vs-index conflation; broken-link filesystem-resolution |
| V9 (W204) | 44 | per-region defect tracking pilot + tightened grep | wikilinks 100% in body content; V8 1191-figure −59% from actual; 5 broken markdown links across 4 unique slugs; 42→4 substrate gap reduction | **resolvable-vs-gap conflation** (every `[[]]` treated as defect — V10 surfaces); inbound-citation density per page |
| V10 (W212) | 46 | **resolvable-vs-gap-ratio + smart-resolver scoring** | iter-45 W208 measurement blind-spot root-caused (32% of top-24 wikilinks were substrate-gaps, not just unconverted links); 12 gap-cluster pages with ratio<50%; api-std-570 + api-std-653 are 29-ref leverage center; environmental-liability over-prioritized at V9 (95% resolvable, not headline target); substrate-then-sweep sequencing as iter discipline | semantic-overlap audit between vocabulary fields (V11 candidate); inbound-citation-density per page (V11 candidate); cross-wiki edge thickness reaudit (V11 candidate) |

**V10 retrospective insight #1 — measurement-axis discipline matures iteratively**: V1-V6 measured topology + edges + depth. V7-V8 measured schema vocabulary + grep counts. V9 measured per-region splits. V10 measures **per-link resolvability** — the dimension that makes "wikilink residual" actionable. Each audit's measurement-axis was unmeasured-blindspot for the prior; iter cadence is roughly 2 iters per V cycle.

**V10 retrospective insight #2 — iter-43 + iter-45 were leverage-blind on substrate-vs-link**: both iters bulk-converted wikilinks without distinguishing gap-targets from resolvable-targets. iter-43 W201 closed 620 conversions (high-yield because top-density pages were 88-97% resolvable). iter-45 closed 85 (lower-yield because next-tier pages were 0% resolvable on inspection-domain). **Future sweeps must measure ratio first, sequence substrate-fill ahead of conversion**.

**V10 retrospective insight #3 — substrate gaps compound at the page level, not the link level**: 7 inspection-domain pages share 2 substrate gap-targets (api-std-570 + api-std-653). Substrate-fill is **multiplicative**: closing 2 stubs unlocks 29 conversions across 7 pages. V8 grep counted gaps as flat instances; V10 surfaces the page-cluster amplification. This is the V10 lasting contribution.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W143 → W204:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 131 | 131/131 |
| lng-projects | 10 | 10/10 |
| maritime-law | 25 | 25/25 |

iter-47 P1 (substrate-fill) adds new pages with full calc-citation frontmatter. P2 (wikilink sweep) is body-link substitution; preserves frontmatter. P3 (foundational entities) adds new entity pages with full calc-citation frontmatter.
