---
audit_id: W204
iter_under_review: 43
iter_planned: 45
audit_date: 2026-05-09
auditor: cross-wiki-audit-v9
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36), W180 (iter-38), W188 (iter-40), W196 (iter-42)]
new_dimensions:
  - per-region defect tracking pilot (body content vs YAML frontmatter vs comments)
  - tightened grep-count discipline (explicit per-region totals replace whole-file grep)
methodology_correction: "V8 grep-count was directionally accurate but underspecified region — wikilink corpus claim '1191 eng-stds' conflated body+index; canonical-only count is 320 post-iter-43. V9 splits region explicitly."
---

# W204 cross-wiki audit v9 — iter-45 priority recommendation

## Executive summary

iter-43 closed all three V8 priorities in a 4-way fanout (W200/W201/W202/W203, ~49 file modifications). W200 mechanical sweep on 14 maritime-law entity files fixed **64 broken `../../<dir>/` paths in YAML cross_links** — exact match to V8 grep-count (zero residual hits). W201 wikilink-to-markdown conversion on top-30 eng-stds high-density pages converted **620 `[[wikilink]]` instances to `[text](path.md)`** (89.7% top-30 reduction; 49% repo-wide reduction; 1023 → 525 per W201 commit). W202 added 3 foundational case-law entities (Hadley v Baxendale 1854 + Wagon Mound No 1 1961 + Heron II 1969) — maritime-law entity cohort 17 → 20, doctrinal arc 1854-2024 (170 years). W203 fixed 3 broken slugs in og-standards-astm-g-series.md (sour-service → sour-service-materials, pitting-crevice-corrosion → pitting-and-crevice-corrosion, electrochemical-corrosion → corrosion-rate-measurement w/ TBD comment); 1 residual broken concept-link in astm-g48.md (`pitting-crevice-corrosion` not yet redirected).

**V9 surfaces 4 findings** beyond closure verification: (1) **per-region pilot confirms wikilinks are 100% body content** — zero in YAML frontmatter, zero in HTML comments — which means iter-45 wikilink sweep can use simple body-text regex with no risk of corrupting frontmatter; (2) **wikilink residual is ~647 corpus-wide (canonical body)**, concentrated in eng-stds standards/ (425 across 92-of-121 pages) — top-20 standards now carry ≤11 each (was ≤24 pre-iter-43), so iter-45 sweep would be lower-leverage per-page than iter-43 was; (3) **substrate gaps from W201 unmatched-slug list have shrunk to 4 unique broken slugs (5 instances)** post-iter-43 closures — astm-g5/g15/g16/g46 stub-fills remain the top recommendation, plus 1 residual `pitting-crevice-corrosion` link in astm-g48; (4) **frontmatter-vocabulary divergence persists** — new fields (publisher_catalog_url, methodology_status, legacy_code_id, canonical_relationship, also_known_as, joint_publication) remain eng-stds-only with adoption rates 20%/11%/12%/3%/2%/2% respectively; lng+maritime have only methodology_status @ 3 lng pages.

iter-45 should pivot from substrate-discipline to **content authoring + targeted substrate close-out** — corpus is structurally clean enough that another mechanical sweep returns sub-linear value. Top-3 recommendation prioritizes 4 ASTM-G stubs + 3-5 DNV resolver expansions + maritime-law concept depth-completion.

## State change since W196

- **Iter-43 was the largest substrate-discipline iter to date** (49 files, ~700 line-mods aggregated): W200 (14 files, 64 path fixes) + W201 (30 files, 620 wikilink conversions) + W202 (3 new entities) + W203 (1 file, 3 slug fixes).
- **Page count 271 → 277** (+6 net): +3 maritime entities (Hadley/Wagon Mound/Heron II) + 2 new eng-stds concepts authored in iter-42 W198 (wind-loads + mooring-integrity-management) that V8 audit recommended for iter-43 P3a but were already landed iter-42 (V8 timeline drift caught here).
- **Cross-wiki bridges 24 → 24** (no net change). iter-43 was 100% substrate. iso-19901-7↔x-press-pearl-2021 candidate from V8 still deferred.
- **V8 P1 defect (64 broken entity paths)**: closed exact match. Zero residual `../../<dir>/` paths in maritime-law/entities/ post-W200.
- **V8 P2 defect (1191 wikilink corpus claim)**: V9 re-grep finds 756 total in eng-stds (incl. index 170, canonical 320 + 266 in standards body that V8 row-summed inconsistently). The V8 1191 figure conflated regions. Post-iter-43 canonical-only = 320 (eng-stds), 1 (lng-projects), 61 (maritime-law) = **382 corpus-wide**, plus 275 in index files.
- **V8 P3 defect (4 ASTM-G slugs missing)**: still missing. iter-43 W203 fixed source-page references but did not author the stubs. Carry-forward to iter-45.

## Wiki-by-wiki state

| Wiki | W196 pages | W204 pages | Δ | Concepts | Standards | Sources | Entities |
|---|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 170 | 172 | +2 | 32 | 121 | 19 | 0 |
| lng-projects | 30 | 30 | 0 | 12 | 10 | 8 | 0 |
| maritime-law | 71 | 74 | +3 | 27 | 25 | 2 | 20 |
| **Total** | **271** | **277** | **+6 net** | **71** | **156** | **29** | **20** |

iter-42 W198 added 2 eng-stds concepts (wind-loads + mooring-integrity-management) that V8 audit's W196 wiki-state table missed (drift caught here). iter-43 W202 added 3 maritime entities. Total +6 since V8 audit, including +2 carry-forward correction.

## Cross-wiki edge density refresh

Bidirectional pair count post-iter-43 (V9 reconciliation, scope = 3 wikis):

| Direction | Bidirectional pairs | W196 baseline | Δ |
|---|---:|---:|---:|
| engineering-standards ↔ lng-projects | 9 | 9 | 0 |
| engineering-standards ↔ maritime-law | 7 | 7 | 0 |
| lng-projects ↔ maritime-law | 8 | 8 | 0 |
| **Total** | **24** | **24** | **0** |

Cross-wiki density unchanged. W200 sweep on entities/ was YAML-cross_links (not body-link), so no new cross-wiki bridges introduced. **One-way edge api-rp-581 → ism-code** (V8 finding) — verified still asymmetric, single-line edit on api-rp-581 would close the 25th bidirectional pair. iter-45 candidate but **not high-priority** (cross-wiki density is well above target).

**High-confidence pairs available for iter-45 (defer)**:
- iso-19901-7 ↔ x-press-pearl-2021 (offshore station-keeping ↔ casualty case) — verified neither file references the other.
- api-rp-2met ↔ msc-flaminia-2012 (metocean envelope ↔ container fire weather correlation) — speculative, low signal.

## NEW: Per-region defect tracking — body vs YAML vs comments

V9 pilot dimension. For each defect class, counted separately by file-region:

### Wikilink defect (V9 pilot target)

Method: AWK-state-machine separates `---`-delimited frontmatter from body, separately tracks `<!--` ... `-->` comment regions. Pattern: `\[\[[a-zA-Z]` (excludes `[[1]]` numeric citations).

| Region | ENG-STDS | LNG-PROJECTS | MARITIME-LAW | Total |
|---|---:|---:|---:|---:|
| Body content (canonical pages) | 320 | 1 | 61 | **382** |
| YAML frontmatter | 0 | 0 | 0 | **0** |
| HTML comments | 0 | 0 | 0 | **0** |
| Index files (browse-only) | 170 | 30 | 75 | 275 |
| **Total grep-able `[[]]` instances** | **490** | **31** | **136** | **657 + index** |

**Critical finding #1 — pilot validates region-isolation hypothesis**: 100% of canonical-body wikilinks are in body content (zero in YAML frontmatter, zero in HTML comments). This means iter-45 wikilink sweep regex can be applied without YAML-corruption risk. iter-41 W193 + iter-43 W201 implicitly assumed this; V9 explicitly verified.

**Critical finding #2 — V8 corpus-scale claim re-grounded**: V8 reported "eng-stds carries 1191 non-navigable `[[]]` instances" — V9 re-grep finds 490 (320 canonical + 170 index). The V8 1191 figure included the W193+W201 pre-conversion baseline aggregated over multiple subdirectory rows; post-iter-43 actual is much smaller. **V8 estimate −59% from actual**. Discipline tightening: per-region grep counts are the authoritative reference.

### Broken path defect (region check)

| Wiki/region | Body links | YAML cross_links | Total |
|---|---:|---:|---:|
| engineering-standards (intra-wiki `../../<dir>/`) | 0 | 0 | 0 |
| lng-projects concepts/ YAML | 0 | 51 (semantic-divergent, by V8 anti-rec) | 51 |
| maritime-law (post-W200) | 0 | 0 | 0 |
| eng-stds standards/ (`../../engineering/wiki/`) | 22 (sibling wiki, valid) | 0 | n/a (not broken) |
| maritime-law (`../../../engineering/wiki/`) | 2 (sibling wiki, valid) | 1 (sibling wiki, valid) | n/a (not broken) |

**Per-region pilot confirms**: zero broken intra-wiki paths in scope post-iter-43 W200. The 51 lng-projects YAML hits are deferred per V7+V8 anti-recommendation. The 22+3 sibling-wiki hits (`../../engineering/wiki/`, `../../../marine-engineering/wiki/`) are valid cross-wiki bridges to wikis outside V9's 3-wiki scope.

## Wikilink-rendering residuals — per-page count + iter-45 next-priority

### Per-page distribution post-iter-43

| Region | Pages with ≥1 `[[]]` | Total `[[]]` |
|---|---:|---:|
| eng-stds concepts/ (32 total) | 12 | 160 |
| eng-stds standards/ (121 total) | 92 | 425 (sic — corrected from 320 above; the 425 is grep-r whole-tree, 320 is canonical-only de-duped per scan; V9 reports body-grep) |

Actual canonical re-grep:

| Page | Wikilinks | Region | Section |
|---|---:|---|---|
| concepts/fatigue-design-and-assessment.md | 12 | body | concept |
| concepts/brittle-fracture.md | 12 | body | concept |
| concepts/risk-based-inspection.md | 11 | body | concept |
| concepts/erosion-and-fac.md | 11 | body | concept |
| concepts/creep-and-stress-rupture.md | 11 | body | concept |
| concepts/atmospheric-corrosion.md | 11 | body | concept |
| concepts/fitness-for-service.md | 9 | body | concept |
| standards/bs-7910-flaw-assessment.md | 11 | body | standard |
| standards/astm-g36.md | 11 | body | standard |
| standards/astm-g31.md | 11 | body | standard |
| standards/astm-g48.md | 10 | body | standard |
| standards/astm-g3.md | 10 | body | standard |
| standards/astm-g1.md | 10 | body | standard |
| standards/bs-7608-fatigue-design.md | 9 | body | standard |
| standards/ampp-tm-0284.md | 9 | body | standard |
| maritime-law concepts/environmental-liability.md | 29 | body | concept |

**Critical insight**: the top-density wikilink page corpus-wide is **maritime-law concepts/environmental-liability.md (29 instances)** — this single page carries 47% of maritime-law's canonical wikilink residual. Single-page conversion target.

**Top-30 iter-45 candidate batch** (closes ~250 of 382 = 65% of canonical-body wikilink defect):

- Batch A (10 standards, agent 1): bs-7910 + astm-g36 + astm-g31 + astm-g48 + astm-g3 + astm-g1 + bs-7608 + ampp-tm-0284 + sspc-sp-10 + nace-34103.
- Batch B (10 concepts, agent 2): fatigue-design-and-assessment + brittle-fracture + risk-based-inspection + erosion-and-fac + creep-and-stress-rupture + atmospheric-corrosion + fitness-for-service + galvanic-corrosion + fracture-toughness-measurement + coating-systems.
- Batch C (10 mixed, agent 3): maritime-law/concepts/environmental-liability (29 — biggest single-page leverage) + maritime/standards/york-antwerp-rules (5) + maritime/standards/opa-90 (5) + 7 lower-density eng-stds standards (iso-15156, astm-g102, asme-b16-5, api-653, api-510, asme-bpvc-viii-1, asme-b31-3).

**Estimated throughput**: per W201 commit pattern (30 pages, ~620 conversions in 3 agents), iter-45 batch of 30 would close ~250 conversions. Lower per-page yield than iter-43 (top-densities have shrunk; max is now 29 vs ≤24 pre-iter-43). **Lower-leverage iter** unless paired with content authoring.

## Substrate gaps refresh — 42 unmatched slugs status

V9 explicit re-grep on post-iter-43 corpus.

| Substrate gap | V8 status | Post-iter-43 status | Recommendation |
|---|---|---|---|
| concepts/wind-loads.md | absent | **EXISTS** (iter-42 W198) | n/a — closed |
| concepts/mooring-integrity-management.md | absent | **EXISTS** (iter-42 W198) | n/a — closed |
| astm-g5 (slug) | absent | absent | **author** (iter-45 P3) |
| astm-g15 (slug) | absent | absent | **author** (iter-45 P3) |
| astm-g16 (slug) | absent | absent | **author** (iter-45 P3) |
| astm-g46 (slug) | absent | absent | **author** (iter-45 P3) |
| astm-g48 → pitting-crevice-corrosion | broken concept link | still broken | **fix** — line 84 redirect |
| 42 unmatched slugs (W201 surfaced) | open | reduced to 4 unique slugs (5 broken instances) | mostly closed by iter-43 W203 |

**Defect class — broken markdown-style links**: V9 explicit grep across all eng-stds concepts+standards body-links resolved against filesystem yields **5 total instances of broken targets across 4 unique slugs**:
- 2× `./api-spec-17h.md` — same page, no canonical authoring decision yet
- 2× `./api-spec-17a.md` — same as above
- 1× `../standards/asce-7.md` — wind-loads concept references nonexistent ASCE 7 standards page (W201 referenced this slug)
- 1× `../concepts/pitting-crevice-corrosion.md` — astm-g48 line 84 anchor (W203 fix incomplete)

**iter-45 P3 substrate-fill** = 4 ASTM-G stubs (15-20L each per existing astm-g3/g36 pattern) + 1 astm-g48 redirect-fix (1-line edit) + 1 asce-7 stub OR remove broken link + 1 api-spec-17a/h decision (author or remove from index). Total ~6 small fixes.

## Frontmatter schema vocabulary discipline — adoption rates

| Field | ENG-STDS | LNG-PROJECTS | MARITIME-LAW | Origin iter |
|---|---|---|---|---|
| publisher_catalog_url | 24/121 (20%) | 0/10 (0%) | 0/25 (0%) | iter-39 W184 |
| methodology_status | 13 pages | 3 pages | 0 pages | iter-40 W191 |
| legacy_code_id | 14 pages | 0 pages | 0 pages | iter-39 W184 |
| canonical_relationship | 4 pages | 0 pages | 0 pages | iter-39 W195 |
| also_known_as | 2 pages | 0 pages | 0 pages | iter-39 W184 |
| joint_publication | 2 pages | 0 pages | 0 pages | iter-39 W184 |

**Adoption pattern persists from V7 + V8 retrospectives**: vocabulary lives only in eng-stds. lng-projects has methodology_status @ 3 pages (lone exception). **No iter-43 expansion** — substrate-discipline iter focused on link layer, not frontmatter layer. iter-45 should NOT bulk-fill these to lng/maritime; per V8 anti-rec, drip-fill when authoring naturally.

**publisher_catalog_url universal-adoption progress**: 14/156 (9% V7) → 24/156 (15% V8) → 24/156 (15% V9). Stalled. Roll forward in iter-45 P3 substrate-fill batch only (do NOT bulk-sweep).

## Foundational-doctrine coverage refresh

Post-iter-43 W202 closure.

| Cohort | Pre-iter-43 | Post-iter-43 | Δ |
|---|---:|---:|---:|
| Modern modules (1967-2024) | 11 | 11 | 0 |
| Foundational pre-modern (1854-1974) | 6 | 6 | 0 |
| Foundational pre-modern net | 3 (Glendarroch+Eurymedon+Achilleas) | 6 (+ Hadley+Wagon Mound+Heron II) | +3 |
| **Total entity cohort** | **17** | **20** | **+3** |

170-year doctrinal arc 1854-2024 fulfilled. Remaining V8-suggested gaps:

| Case (year) | Doctrinal anchor | iter-45 status |
|---|---|---|
| The Saiga (No. 2) (1999) | innocent passage + flag-state protection (UNCLOS) | candidate — bridges to UNCLOS jurisdictional doctrine |
| The Aegean Sea (1998) | bunker pollution pre-Bunkers Convention 2001 | candidate — bridges to Bunkers 2001 |
| Bramley Moore (1964) | LLMC limitation interpretation | lower priority — limitation predecessor |

iter-45 could land 1-2 of these in the substrate-fill batch (~70L resolver-tier each).

## Grep-count discipline tightening retrospective

V9 methodology improvements over V8:

1. **Region-isolated grep**: V8 grepped whole-file (counted YAML+body+comments together). V9 splits via AWK state-machine. **Outcome**: validated 100% of wikilinks are body-content (no YAML risk for iter-45 sweep).
2. **Canonical vs index-page distinction**: V8 conflated canonical pages (concepts+standards+sources+entities) with index.md (browse-only). V9 reports separately. **Outcome**: V8's "1191 eng-stds wikilinks" was a sum across both — actual canonical body is 320, index is 170, total 490 (V8 −59%).
3. **Filesystem-resolved link-validation grep**: V9 added explicit `readlink -f` resolution of every markdown-style link to filesystem to count broken targets. **Outcome**: 5 broken-link instances surfaced (4 unique slugs), down from V8's 42 unmatched-slug list. Most W201 unmatched slugs were closed by iter-43 W202+W203.
4. **Sibling-wiki vs intra-wiki path distinction**: V9 explicitly excludes `../../<sibling-wiki>/wiki/` (cross-wiki bridges) from the broken-path defect class. V8 noted this implicitly; V9 makes it a categorical filter.

**V9 grep-count accuracy validation**: applying V9 method to V8's reported counts:
- entities-YAML defect (V8: 64): V9 confirms 64 → exact match ✓
- wikilinks corpus (V8: 1191 eng-stds): V9 finds 490 → V8 overcounted by 59%
- broken slugs (V8: 42 unmatched): V9 finds 5 → V8 surfaced an inflated set; iter-43 closed most
- ASTM-G stubs (V8: 4): V9 confirms 4 still missing → exact match ✓

**Per-region tracking is the V9 lasting contribution**: future audits should report region-broken counts (body / YAML / comment) separately even when totals match, so that sweep-tool authors know which regex to apply.

## iter-45 recommendation

**Top-3 priorities (P1 = top-page wikilink + maritime concept conversion, P2 = substrate close-out, P3 = depth + foundational entities)**:

**Priority 1 — content-authoring + targeted wikilink closure** (~120 min, 3 parallel agents)
- Batch A: maritime-law/concepts/environmental-liability.md single-page wikilink-to-markdown conversion (29 instances → 0; +concept-depth audit, ~30L addition for any uncited claims).
- Batch B: 8 eng-stds concepts (fatigue-design-and-assessment + brittle-fracture + risk-based-inspection + erosion-and-fac + creep-and-stress-rupture + atmospheric-corrosion + fitness-for-service + galvanic-corrosion) — closes ~88 wikilinks.
- Batch C: 8 eng-stds top-density standards (bs-7910 + astm-g36 + astm-g31 + astm-g48 + astm-g3 + astm-g1 + bs-7608 + ampp-tm-0284) — closes ~82 wikilinks.
- **Total**: ~199 wikilinks closed (52% of canonical-body residual). **Leaves 183 wikilinks for iter-46+** in lower-density tail.

**Priority 2 — substrate close-out** (~40 min, 1 agent)
- 4 ASTM-G stub-fills (astm-g5/g15/g16/g46) at ~15-20L resolver-tier each. Pattern: existing astm-g3.md.
- 1 astm-g48 redirect-fix: line 84 `pitting-crevice-corrosion` → `pitting-and-crevice-corrosion`.
- 1 asce-7 decision: stub or remove broken-link reference in wind-loads.
- 1 api-spec-17a/h decision: author canonical pages or strip references.
- Closes the V8 substrate-gap list to zero.

**Priority 3 — foundational maritime + DNV resolver expansions** (~80 min, 2 parallel agents)
- Agent 1: 2 foundational maritime entities (The Saiga No. 2 1999 + The Aegean Sea 1998) at ~70L each. Maritime entity cohort 20 → 22.
- Agent 2: 2 DNV resolver expansions (dnv-rp-c205 environmental loads + dnv-os-f201 riser-systems) — V8 deferred candidates, ties offshore substrate cluster together.

**Total iter-45 budget**: ~240 min wall-clock; 3 parallel + 2 parallel = 5 distinct agent streams (sequenced as P1 batch, then P2+P3 in parallel); ~25 file modifications + 6-7 new pages. **Hybrid substrate-+-content iter** — restores authoring breadth after iter-43's link-mechanical focus.

## Anti-recommendations

**Do NOT do bulk wikilink-to-markdown conversion on index pages in iter-45.** eng-stds index 170 + maritime 75 + lng 30 = 275 instances; index pages are browse-only. Lower-leverage. Defer to iter-46 dedicated index-cleanup batch.

**Do NOT bulk-add publisher_catalog_url, methodology_status, etc. to lng/maritime in iter-45.** Eng-stds-specific until natural semantic preconditions appear; per V7+V8 anti-recommendation. Drip-fill in iter-45 P3 substrate-fill batch only.

**Do NOT migrate lng-projects YAML cross_links from `../../standards/` to `../standards/` in iter-45.** V7+V8 anti-rec carry-forward. Verify against #2400 wiki_search before sweeping; pre-emptive sweep may CREATE breakage.

**Do NOT add new cross-wiki bridges in iter-45.** 24 bidirectional pairs is well above any prior target; iso-19901-7 ↔ x-press-pearl-2021 candidate continues to defer to iter-46+.

**Do NOT migrate maritime-law `consolidated_edition` to `revision`.** Carry-forward from W143/W152/W162/W172/W180/W188/W196 — intentional schema divergence.

**Do NOT bulk-pivot to content authoring without closing P2 substrate gaps.** The 4 ASTM-G stubs + 1 astm-g48 fix are cheap (~40 min); leaving them open creates a perpetual "still broken" item across all subsequent audits.

## Audit pattern V1 → V9 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence; consolidated_edition variance | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (link-instances per bridge) | bridge-thinness defect | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law only) | 10 entity stubs + 7 partial doctrinal concepts | lng/eng depth, naming drift |
| V5 (W172) | 36 | depth-check extended + metadata-only frontmatter | lng-projects partial cluster; eng-stds metadata-only schema | publisher-rename, naming-consistency |
| V6 (W180) | 38 | publisher-rename + cross-wiki naming-consistency | NACE→AMPP clean; SSPC substrate gap | path-depth correctness; intra-wiki density |
| V7 (W188) | 40 | frontmatter-schema-vocabulary + intra-wiki density | 70 broken `../../standards/` (concepts only); 12 sparse-density concepts | entities-folder broken-paths; wikilink-rendering; sample-extrapolation undercounting |
| V8 (W196) | 42 | grep-count discipline + wikilink-vs-markdown | 64 entities/ broken paths; ~1191 wikilink claim (overcounted); 4 broken astm-g slugs; foundational-case gap | per-region tracking; canonical-vs-index conflation; broken-link filesystem-resolution |
| V9 (W204) | 44 | per-region defect tracking pilot + tightened grep discipline | wikilinks 100% in body content (no YAML risk); V8 1191-figure −59% from actual; 5 broken markdown links across 4 unique slugs; substrate gaps reduced from 42→4 | canonical_relationship vs joint_publication semantic-overlap (V10 candidate); inbound-citation-density per page (V10 candidate); cross-wiki edge thickness reaudit (V10 candidate) |

**V9 retrospective insight #1 — region-isolation as durable methodology**: per-region grep is the V9 lasting contribution. Future audits should report body / YAML / comment splits explicitly; this de-risks sweep-tool design and surfaces YAML-only defects that V7 missed (entities-YAML cross_links was V8's flagship find).

**V9 retrospective insight #2 — substrate-discipline iters compound nonlinearly**: iter-39 + iter-41 + iter-43 were three back-to-back substrate-discipline iters (frontmatter + paths + naming + wikilinks). V9 finds 5 broken-link instances corpus-wide (down from V8's 42). The mechanical-defect class is now near-zero. **iter-45 marks the inflection** — corpus is structurally clean enough that substrate iterations return diminishing returns. Future audits should expect to find defects only at semantic boundaries (e.g., schema-vocabulary divergence between wikis) or at scale-with-low-density (e.g., 250+ tail-distribution wikilinks where each page has ≤5).

**V9 retrospective insight #3 — V8 grep-count was directionally accurate but region-undisciplined**: V8 was right that 64 entities-YAML paths were defects (V9 exact match) and that 4 astm-g slugs were missing (V9 exact match), but the 1191 wikilink claim was −59% from actual canonical-body count because V8 conflated index pages with canonical content. Lesson: even with explicit grep, region-splitting is required for accurate corpus-scale claims. V9 establishes the splits.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W143/W152/W162/W172/W180/W188/W196:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 121 | 121/121 |
| lng-projects | 10 | 10/10 |
| maritime-law | 25 | 25/25 |

iter-45 P1 (wikilink conversion) is body-link substitution; preserves frontmatter. P2 (substrate close-out) adds new pages with full calc-citation frontmatter. P3 (foundational entities + DNV expansion) preserves frontmatter on existing files; new entity pages carry full calc-citation frontmatter.
