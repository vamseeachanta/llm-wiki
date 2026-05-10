---
audit_id: W196
iter_under_review: 41
iter_planned: 43
audit_date: 2026-05-09
auditor: cross-wiki-audit-v8
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36), W180 (iter-38), W188 (iter-40)]
new_dimensions:
  - grep-count discipline (explicit Grep totals replacing sample-based extrapolation)
  - wikilink-vs-markdown rendering discipline ([[]] non-navigable on GitHub vs []() markdown-renderable)
methodology_correction: "W188 V7 underestimated 2 dimensions by 50-65% (broken-paths 70 vs actual 115; zero-link sources 12 vs actual 18) — V8 substitutes explicit grep for sampled extrapolation"
---

# W196 cross-wiki audit v8 — iter-43 priority recommendation

## Executive summary

iter-41 closed all three V7 priorities in a single 4-way fanout iter (W192/W193/W194/W195, ~56 file modifications). W192 mechanical sweep on 15 maritime-law concepts fixed **115 broken `../../standards/`→`../standards/` paths** (V7 estimated 70; defect was 65% larger). W193 navigable-link uplift on 6 eng-stds concepts replaced ~54 non-navigable `[[wikilink]]` instances with markdown-style `[text](path.md)`. W194 cross-references to 15 eng-stds source pages added ~143 intra-wiki links (closing the actual 18-of-19 zero-link gap, not the V7-estimated 12). W195 frontmatter canonicalization on 20 files added 6 maritime sources fields + 3 lng raw_copy_allowed + 12 eng-stds publisher_catalog_url + 1 ISO-date fix. **V8 surfaces a previously-uncaught P1 substrate defect**: 64 broken intra-wiki references in maritime-law **entities/** YAML cross_links (`../../standards/` and `../../concepts/` from entities/ resolve outside the wiki tree — same defect class as iter-41 W192 fixed in concepts/, missed because V7 sweep targeted concept/body-link form, not entity/YAML-cross_links form). Plus a separately-quantified `[[wikilink]]` rendering defect at corpus scale: **eng-stds carries 1191 non-navigable `[[]]` instances** (concepts 388, standards 634, plus ~169 in index files), maritime-law 125, lng-projects 31. iter-43 should prioritize the entity-folder broken-path mechanical sweep + bulk wikilink-to-markdown conversion on top-density pages over content authoring.

## State change since W188

- **iter-41 was simultaneously substrate-discipline and content authoring** (~56 file modifications) — closed V7 P1+P2+P3 in one iter via 4-way fanout (W192/W193/W194/W195).
- **Page count 268→272**: +3 maritime entities (W189 — Glendarroch 1894 + Eurymedon 1974 + Achilleas 2008 from iter-40) + 1 eng-stds astm-a553 (W183 from iter-38; counted in W188 baseline drift). On-disk canonical content (concepts+standards+sources+entities): eng-stds 170, lng-projects 30, maritime-law 71. Total **271** by canonical content-page count.
- **Cross-wiki bridges 21→24 bidirectional pairs** (target met) per iter-40 W190 (3 bridges: ASME BPVC IX↔IGC + ABS GUI-002↔SOLAS + API RP 17B↔MARPOL Annex I) plus 0 net add in iter-41. Reconciled count below.
- **V7 P1 defect (70 broken paths)** closed in iter-41 W192 — but defect-class persists in entities/ folder, undiscovered until V8 grep.
- **Zero-link source pages**: eng-stds was 18-of-19 (V7 said 12); now 19-of-19 carry intra-wiki links. lng-projects has 2 remaining zero-link sources (elements-acma-projects-31522-woodfibre, elements-doris-62092-sesa) — both auto-generated catalog stubs, by-design near-empty.
- **Frontmatter discipline**: publisher_catalog_url 14→24 on eng-stds (post-W195); 0 on lng/maritime. Block-vs-inline cross_links shape unchanged (drift not addressed in iter-41).

## Wiki-by-wiki state

| Wiki | W188 pages | W196 pages | Δ | Concepts | Standards | Sources | Entities |
|---|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 170 | 170 | 0 | 30 | 121 | 19 | 0 |
| lng-projects | 30 | 30 | 0 | 12 | 10 | 8 | 0 |
| maritime-law | 68 | 71 | +3 | 27 | 25 | 2 | 17 |
| **Total** | **268** | **271** | **+3 net** | **69** | **156** | **29** | **17** |

iter-40 added 3 maritime-law entities (Glendarroch + Eurymedon + Achilleas — pre-modern foundational case-law). iter-41 was 100% modification-only (zero new pages — substrate-discipline iter).

## Cross-wiki edge density refresh

Bidirectional page-pair count post-iter-41 (V8 reconciliation):

| Direction | Bidirectional page-pairs | W188 baseline | Δ |
|---|---:|---:|---:|
| engineering-standards ↔ lng-projects | 9 | 8 | +1 |
| engineering-standards ↔ maritime-law | 7 | 6 | +1 |
| lng-projects ↔ maritime-law | 8 | 7 | +1 |
| **Total** | **24** | **21** | **+3** |

Detailed pairs:
- **eng↔lng (9)**: cathodic-protection↔igc-code, brittle-fracture↔lng-process-safety, api-17j↔igc-code, api-rp-571↔lng-process-safety, asme-b31-3↔ibc-code, asme-b31-3↔igc-code, asme-bpvc-ix↔igc-code, astm-a553↔igc-code, iso-15156↔lng-process-safety
- **eng↔maritime (7)**: abs-gui-002-fpso↔solas-1974, api-17j↔marpol-73-78, api-rp-17b↔marpol-73-78, api-rp-571↔marpol-73-78, api-rp-580↔ism-code, asme-bpvc-viii-1↔solas-1974, iso-19901-7↔solas-1974
- **lng↔maritime (8)**: lng-regulatory-framework↔marpol-73-78, lng-regulatory-framework↔solas-1974, ibc-code↔hns-convention-2010, ibc-code↔marpol-73-78, ibc-code↔solas-1974, igc-code↔hns-convention-2010, igc-code↔marpol-73-78, igc-code↔solas-1974

**One-way-only edge** (not counted): api-rp-581→ism-code (one direction only — reverse from ism-code only links to api-rp-580). Could be made bidirectional with single-line edit on api-rp-581 (~25th bidirectional pair, very cheap).

**Bridge target met**: 24 bidirectional pairs is well above any prior target. Cross-wiki density is no longer the bottleneck. **iter-43 should NOT add new cross-wiki bridges** unless an entity-tier bridge surfaces (iso-19901-7↔x-press-pearl-2021 candidate from W188 iter-41 deferred — still defer to iter-44+).

## NEW: Grep-count discipline — explicit defect totals

V8 dimension. V7 underestimated 2 defect counts (70 vs 115; 12 vs 18) by sampling 1-2 pages and extrapolating. V8 runs explicit Grep across all 3 wikis.

### Defect class A: broken intra-wiki paths (`../../<dir>/`)

Grep pattern: `\.\./\.\./(standards|concepts|entities|sources)/` across `<wiki>/wiki/`.

| Wiki | `../../standards/` | `../../concepts/` | `../../entities/` | `../../sources/` | Total |
|---|---:|---:|---:|---:|---:|
| engineering-standards | 0 | 0 | 0 | 0 | **0** |
| lng-projects | 51 | 0 | 0 | 0 | **51 (all YAML cross_links — see anti-rec)** |
| maritime-law | 21 | 45 | 0 | 0 | **66** |

**Critical finding**: 64 of the 66 maritime-law broken paths are in **entities/** YAML cross_links (14 of 17 entity files have broken `../../standards/` and `../../concepts/` paths — entities/ is at same depth as concepts/, so `../concepts/` is correct, `../../concepts/` resolves to `wikis/maritime-law/concepts/` which is outside the wiki/ subtree). Affected entities: 19 path-instances to standards + 45 to concepts. Pattern matches the iter-40 entities introduction (W189 added Glendarroch/Eurymedon/Achilleas with the wrong path-depth, but most pre-W189 entities also drifted — total 14 of 17 affected).

**lng-projects 51 instances**: all are in concepts/ YAML cross_links field. Per V7 anti-rec note, these may be valid under YAML resolver semantics (YAML cross_links resolved from a different root than body-link Markdown). Cannot be confirmed without testing #2400 wiki_search resolver. **Recommendation**: leave lng-projects YAML alone until resolver semantics ship; treat as semantic-divergent, not defect.

**Maritime entities are unambiguously a defect**: 14 entity files use `../../<dir>/` in YAML cross_links, but the YAML field uses the same path-resolution semantics as the body-link in maritime-law concepts (which iter-41 W192 fixed by going from `../../` to `../`). Entities sit at the same depth as concepts (`wiki/entities/` parallel to `wiki/concepts/`), so the same fix applies: `sed -i 's|\.\./\.\./standards/|../standards/|g; s|\.\./\.\./concepts/|../concepts/|g' wikis/maritime-law/wiki/entities/*.md`.

### Defect class B: zero-link source pages

Grep pattern: count Markdown-style `\]\([^)]+\.md` references per source page.

| Wiki | Total sources | Zero-link sources | Single-link sources | Multi-link sources |
|---|---:|---:|---:|---:|
| engineering-standards | 19 | 0 | 0 | 19 (all post-W194) |
| lng-projects | 8 | 2 (auto-gen catalogs) | 1 (woodfibre-corpus-pointer) | 5 |
| maritime-law | 2 | 0 | 0 | 2 |

**Eng-stds source-page citation gap fully closed by W194**. lng-projects 2 remaining zero-link sources (elements-acma-projects-31522-woodfibre, elements-doris-62092-sesa) are auto-generated `llm-wiki batch-ingest` catalog stubs with only filesystem path-pointers; they correctly carry zero in-wiki links (referenced from index.md only). **Not a defect, by design**.

### Defect class C: missing canonical frontmatter fields

Explicit field-by-field count across all 3 wikis (substantively unchanged from W188 except where iter-41 W195 closed gaps):

| Field | Pre-W195 (W188) | Post-W195 (W196) | Compliance |
|---|---|---|---|
| `sources` field on maritime-law entities | 6 missing | 0 missing | **closed** by W195 |
| `raw_copy_allowed` on lng-projects standards | 3 missing | 0 missing | **closed** by W195 |
| `publisher_catalog_url` on eng-stds standards | 14/121 = 12% | 24/121 = 20% | partial — 97 still missing |
| `publisher_catalog_url` on lng standards | 0/10 | 0/10 | unstarted |
| `publisher_catalog_url` on maritime standards | 0/25 | 0/25 | unstarted |
| Maritime overview.md `last_updated` time-component | drift | clean (ISO-date) | **closed** by W195 |

**publisher_catalog_url at 24/156 = 15% across all 3 wikis** — universal adoption (W188 V7 recommendation) is one-third complete. Rolling-fill candidate for iter-43 P3.

## NEW: Wikilink-vs-markdown rendering — `[[]]` density per wiki/section

V8 dimension. The `[[slug]]` syntax is non-navigable on GitHub (renders as raw text including the brackets). Markdown-style `[text](path.md)` is the only navigable form. Iter-41 W193 set the conversion pattern on 6 eng-stds concepts (~54 conversions). V8 quantifies remaining defect across all 3 wikis.

### Wikilink corpus scale

Grep pattern: `\[\[[a-zA-Z]` (excludes false-positive `[[1]]` numeric citations).

| Wiki | Concepts | Standards | Sources | Entities | Index | Total |
|---|---:|---:|---:|---:|---:|---:|
| engineering-standards | 388 | 634 | 0 | — | 168 | **1190** (1191 in v3 grep due to template) |
| lng-projects | ~5 | ~14 | 0 | — | 30 | **31** (excluding _template ~12 = ~19 canonical) |
| maritime-law | 33 | ~92 | 0 | 0 | 72 | **125** |

**eng-stds dominates at ~1191 wikilink instances**. Concepts contribute 388 (post-W193 reduction; was higher), standards contribute 634 (untouched), index 168 (browse-page; potentially worth converting). Pages with ≥20 wikilinks (top-density tier):

| Page | Wikilinks | Lines | Wikilink-density-per-line |
|---|---:|---:|---:|
| eng-stds standards/api-rp-571.md | 24 | ~75 | 0.32 |
| eng-stds standards/api-rp-581.md | 22 | ~60 | 0.37 |
| eng-stds standards/api-rp-577.md | 22 | ~55 | 0.40 |
| eng-stds standards/api-510.md | 22 | ~50 | 0.44 |
| eng-stds standards/ampp-sp0775.md | 21 | ~60 | 0.35 |
| eng-stds standards/astm-g36.md | 20 | ~55 | 0.36 |
| eng-stds standards/api-rp-580.md | 20 | ~55 | 0.36 |
| eng-stds standards/api-rp-14e.md | 20 | ~227 | 0.09 |
| eng-stds concepts/stress-corrosion-cracking.md | 30 | 234 | 0.13 |
| eng-stds concepts/welding-procedures-and-acceptance.md | 28 | 151 | 0.19 |
| eng-stds concepts/weld-toughness.md | 23 | 116 | 0.20 |
| eng-stds concepts/hydrogen-embrittlement.md | 23 | 263 | 0.09 |
| eng-stds concepts/sour-service-materials.md | 20 | 78 | 0.26 |
| maritime-law concepts/environmental-liability.md | 29 | ~75 | 0.39 |

### Wikilink density by wiki section

| Wiki/section | Pages affected (≥1 [[]]) | Total `[[]]` |
|---|---:|---:|
| eng-stds concepts/ | 18 of 30 | 388 |
| eng-stds standards/ | ~50 of 121 | 634 |
| eng-stds index.md | 1 | 168 |
| maritime-law concepts/ | 4 of 27 | 33 |
| maritime-law standards/ | ~15 of 25 | ~92 |
| maritime-law index.md | 1 | 72 |
| lng-projects mostly index/templates | 3-4 | 31 |

**Pattern recognition**: high-wikilink eng-stds standards-pages cluster on API damage-mechanism corpus (api-rp-571, api-rp-581, api-rp-577, api-510, api-rp-580) — these were authored before the W193 markdown-style convention was established. Wikilink-to-markdown conversion on top-30 pages would close ~600 of the 1191 instances (50% of corpus defect) at ~20 minutes per page. iter-41 W193 did 6 pages in one batch — 30 pages = 5 batches.

**Critical insight**: maritime-law concepts/environmental-liability.md has 29 wikilinks (highest single-page concentration in maritime). This page was authored iter-35 (W167 — partial-depth → 133L/8S expansion); it predates the markdown-style convention. Single-page conversion target.

## Engineering-standards depth-completion roadmap refresh

Resolver-expansion progress through iter-41:

| Iter | Resolvers expanded | Cumulative |
|---:|---|---:|
| 36 (W175) | dnv-os-e301, iso-19901-7, api-rp-2a-wsd | 3 |
| 37 (W178) | asme-bpvc-viii-1, asme-b31-3 | 5 |
| 39 (W187) | asme-bpvc-viii-2, dnv-rp-b401, asme-bpvc-ix | 8 |
| 40 (W191) | asme-b16-5, api-spec-5l, asme-b31-4 | 11 |
| Earlier substrate-fills | sspc-sp-10 (W185), api-17j (W179), astm-a553 (W183) | 11 + 3 |

Total: 11 high-citation resolvers expanded + 3 substrate-fills = 14 distinct campaign expansions across iter-36→iter-41.

Depth distribution post-iter-41:

| Bucket | W188 (post-iter-39) | W196 (post-iter-41) | Δ |
|---|---:|---:|---:|
| <50 lines | 55 | 52 | -3 (W191 expansions) |
| 50-79 lines | 10 | 10 | 0 |
| 80-149 lines | 35 | 38 | +3 |
| 150+ lines | 21 | 21 | 0 |

**Next-tier resolver-expansion candidates** (under-50L with high inbound):

| Page | Lines | Concept-inb | Total-inb | Recommendation |
|---|---:|---:|---:|---|
| ampp-tm-0177 | 40 | 4 | 16 | **defer** — iso-15156 + ampp-mr-0175-pt1 carry doctrine |
| ampp-mr-0175-pt3 | 41 | 3 | 18 | **defer** — pt1 carries |
| ampp-mr-0175-pt2 | 41 | 3 | 17 | **defer** — pt1 carries |
| dnv-os-f201 | 42 | 2 | 7 | **candidate** — riser system standard, no sibling |
| dnv-rp-c203 | 47 | 2 | 13 | **candidate** — fatigue assessment, ties to dnv-rp-c205 |
| dnv-rp-c205 | 47 | 1 | 8 | **candidate** — environmental loads, station-keeping |
| dnv-st-f101 | 44 | 1 | 7 | **candidate** — submarine pipeline |
| dnv-rp-f101 | 44 | 1 | 7 | **candidate** — corroded pipeline assessment |
| iso-19901-1 | 39 | 1 | 6 | **candidate** — metocean envelope |
| api-rp-2met | 48 | 1 | 5 | **candidate** — metocean for offshore design |

**Roadmap shift**: AMPP cohort exhausted (V7 finding holds). DNV-RP/ST cohort emerges as next-tier — 5 candidates (dnv-os-f201, dnv-rp-c203, dnv-rp-c205, dnv-st-f101, dnv-rp-f101) form a coherent offshore-engineering substrate cluster (riser + fatigue + environmental + pipeline + corrosion-assessment). iter-43 could land 2-3 DNV expansions in one resolver-campaign batch.

## Substrate-completeness review

Substrate gaps surfaced by iter-41 W194 (carry-forward to iter-43+):

| Gap | Description | Recommendation |
|---|---|---|
| `concepts/wind-loads.md` | Referenced in og-standards-* but page does not exist | **author** — common substrate for offshore (api-rp-2met + iso-19901-1 + dnv-rp-c205 all reference) |
| `concepts/mooring-integrity-management.md` | Referenced from sources but page absent | **author** — ties to dnv-os-e301 (mooring) + iso-19901-7 (station-keeping) |
| `astm-g15` slug | Referenced from og-standards-astm-g-series but page absent (4 broken slugs total: g5/g15/g16/g46) | **stub-fill** — ASTM corrosion-test methods cluster |
| `astm-g16` slug | Referenced but absent | **stub-fill** |
| `astm-g46` slug | Referenced but absent | **stub-fill** |
| `astm-g5` slug | Referenced but absent | **stub-fill** |
| 3 confidential doris source pointers | Intentionally unlinked per vendor governance | **leave** — by-design |

**4 broken astm-g slugs (V7 said 3)** — V8 grep correction. Stub-fills are minimal-effort (~10-20L resolver-tier each) but close real navigation paths.

## Foundational-doctrine coverage

iter-40 W189 added 3 foundational case-law entities (Glendarroch 1894 + Eurymedon 1974 + Achilleas 2008). Coverage gap analysis for additional foundational pre-modern cases:

| Case (year) | Doctrinal anchor | Gap analysis |
|---|---|---|
| Hadley v Baxendale (1854) | foreseeability rule for damages | **absent** — Achilleas 2008 narrows it; the originating case is doctrinally cited but no entity page |
| The Heron II (1969) | reasonable contemplation in carriage damages | **absent** — bridges Hadley→Achilleas |
| The Saiga (No. 2) (1999) | innocent passage + flag-state protection (UNCLOS) | **absent** — defining UNCLOS port-state-control case |
| The Wagon Mound (No. 1) (1961) | foreseeability in tort/admiralty | **absent** — Privy Council |
| Bramley Moore (1964) | LLMC limitation interpretation | **absent** — limitation-act predecessor |
| The Aegean Sea (1998) | bunker pollution pre-Bunkers Convention 2001 | **absent** — bridges to Bunkers 2001 |

**Recommendation**: maritime-law entities cohort can grow 17→20 via 3 foundational pre-modern cases (Hadley + Heron II + Wagon Mound) in one iter-43 batch. Each at ~70L resolver-tier matches Glendarroch/Eurymedon/Achilleas pattern. Defer Saiga/Aegean Sea/Bramley Moore to iter-44+.

## iter-43 recommendation

**Top-3 priorities (P1 = mechanical-sweep, P2 = wikilink-conversion, P3 = substrate-fill + foundational-cases)**:

**Priority 1 — maritime-law entities/ broken-path mechanical sweep** (~15 min, 1 agent)
- Sed replacement on 64 broken `../../standards/` and `../../concepts/` paths across 14 entity files.
- Verify YAML cross_links resolve correctly post-fix.
- **Highest leverage** — same defect class as iter-41 W192 closed in concepts/, missed because V7 sweep targeted concept body-link form not entity YAML form. Single-pattern, mechanical, fail-closed under #2400.

**Priority 2 — wikilink-to-markdown conversion campaign** (~120 min, 3 parallel agents)
- Top-30 high-density pages (concepts + standards) — closes ~600 of 1191 corpus wikilinks (50% defect reduction).
- Batch A (10 pages, agent 1): top-10 eng-stds standards (api-rp-571, api-rp-581, api-rp-577, api-510, ampp-sp0775, astm-g36, api-rp-580, api-rp-14e, api-rp-941, api-570).
- Batch B (10 pages, agent 2): top-10 eng-stds concepts (stress-corrosion-cracking, welding-procedures-and-acceptance, weld-toughness, hydrogen-embrittlement, sour-service-materials, engineering-critical-assessment, corrosion-rate-measurement, htha-nelson-curves, mic, ductile-tearing).
- Batch C (10 pages, agent 3): mixed cleanup — maritime environmental-liability + 8 maritime standards with [[]] + lng-projects standards templates.
- Each conversion page: ~20 min (similar to W193 throughput — 6 pages in one batch).
- Defer index-page wikilink conversion (eng-stds 168 + maritime 72 + lng 30 = 270 instances) to iter-44.

**Priority 3 — substrate-fill + foundational case-law** (~60 min, 2 parallel agents)
- Agent 1: 4 ASTM G stub-fills (astm-g5/g15/g16/g46) + 2 concept authoring (wind-loads.md + mooring-integrity-management.md). ~40 min.
- Agent 2: 3 foundational maritime entities (Hadley v Baxendale 1854 + Heron II 1969 + Wagon Mound 1961). ~20 min at 70L resolver-tier per W189 pattern.
- Closes substrate gaps surfaced by W194 + extends entity-coverage cohort 17→20.

**Total iter-43 budget**: ~195 min wall-clock; 3 parallel + 1 sequential agents (4 distinct streams); ~50 file modifications + 6-7 new pages. **Substrate-discipline + content-authoring iter** — restores breadth-balance after iter-41's substrate-only nature.

## Anti-recommendations

**Do NOT add new cross-wiki bridges in iter-43.** 24 bidirectional pairs is well above any prior target; cross-wiki density is no longer the bottleneck. Defer iso-19901-7↔x-press-pearl-2021 to iter-44+ unless a substrate-driven need surfaces.

**Do NOT migrate lng-projects YAML cross_links from `../../standards/` to `../standards/`.** V7 anti-rec carry-forward — these may be valid under YAML resolver semantics. Verify against #2400 wiki_search before sweeping; pre-emptive sweep may CREATE breakage.

**Do NOT do bulk wikilink-to-markdown conversion on the index pages in iter-43.** eng-stds index 168 + maritime 72 + lng 30 = 270 instances; index pages are browse-only and the wikilink rendering issue is less load-bearing there. Defer to iter-44 dedicated index-cleanup batch.

**Do NOT bulk-fill `publisher_catalog_url` to all 132 missing standards in iter-43.** Drip-fill pattern is preferred — add when authoring/expanding a page, not in bulk-sweep mode (avoids `null` placeholder pollution). Roll the field forward in iter-43 P3 substrate-fills only.

**Do NOT migrate maritime-law `consolidated_edition` to `revision`.** Carry-forward W143/W152/W162/W172/W180/W188 — intentional schema divergence.

**Do NOT migrate inline cross_links (`[a, b, c]`) to block-list in iter-43.** YAML-equivalent; cosmetic. Defer.

**Do NOT add new V7 schema vocabulary (legacy_code_id, also_known_as, joint_publication, canonical_relationship) to lng/maritime in iter-43.** These fields are eng-stds-specific until natural semantic preconditions appear.

## Audit pattern V1 → V8 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence; consolidated_edition variance | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (link-instances per bridge) | bridge-thinness defect (4/22 imbalance) | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law only) | 10 entity stubs + 7 partial doctrinal concepts | lng/eng depth, naming drift |
| V5 (W172) | 36 | depth-check extended + metadata-only frontmatter | lng-projects 8-concept partial cluster; eng-stds metadata-only schema | publisher-rename, naming-consistency |
| V6 (W180) | 38 | publisher-rename + cross-wiki naming-consistency | NACE→AMPP clean; SSPC substrate gap; BS-vs-ISO ambiguity; see_also vs cross_links drift | path-depth correctness; intra-wiki density |
| V7 (W188) | 40 | frontmatter-schema-vocabulary + intra-wiki cross-link density | 70 broken `../../standards/` (concepts only); 12 sparse-density concepts; publisher_catalog_url 9% | **entities-folder broken-paths (V8 catch); wikilink-rendering corpus scale (V8 catch); under-counting via sample-extrapolation (V8 catch)** |
| V8 (W196) | 42 | grep-count discipline + wikilink-vs-markdown rendering | **64 broken paths in maritime entities/ folder (P1)**; 1191 eng-stds wikilink instances (P2); 4 broken astm-g slugs (V7 said 3); foundational-case gap (Hadley/Heron II/Wagon Mound) | bidirectional-link verification (V9 candidate); section-name canonicalization (V9 candidate); citation-density-per-page (V9 candidate); resolver-target-existence assertion (V9 candidate when #2400 wiki_search ships) |

**V8 retrospective insight #1 — methodology correction**: V7 underestimated 2 defect counts by 50-65% via sample-and-extrapolate approach. V8 substituted explicit Grep across all 3 wikis for these dimensions, surfacing the entities-folder broken-path defect class (64 instances) that sample-of-concepts methodology would have missed indefinitely. Future audits should grep-count any defect class where the underlying pattern is regex-detectable, even if sample-based estimation was sufficient earlier.

**V8 retrospective insight #2 — visual-vs-functional defect classes**: V8's wikilink dimension is the third "invisible-to-humans-but-fail-closed-to-tooling" defect (after V6's see_also drift and V7's path-depth). On GitHub, `[[wikilink]]` renders as the literal text `[[wikilink]]` — readers see brackets and assume "internal link" but cannot click. Markdown-style `[text](path)` is the only navigable form. The pattern: each audit version catches a new class of silent defect that visual rendering hides.

**V8 retrospective insight #3 — substrate-discipline iters compound**: iter-39 + iter-41 were both 4-way fanout substrate-discipline iters (frontmatter + paths + links + naming). Compound effect: corpus is now structurally clean enough that V8 finds defects only at the boundary (entity-folder paths overlooked because V7 sweep targeted concepts only) and at scale (1191 wikilinks corpus-wide because no single page exceeds 30 instances and no prior audit grep-counted). **iter-43 should remain in this substrate-discipline mode** rather than pivoting to content authoring; defect-classes still surfacing per audit version.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W152/W162/W172/W180/W188:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 121 | 121/121 |
| lng-projects | 10 | 10/10 |
| maritime-law | 25 | 25/25 |

iter-43 P1 (entity-folder path sweep) does not touch standards-page frontmatter. P2 (wikilink-to-markdown) is body-link conversion; preserves frontmatter. P3 substrate-fills add new pages with full calc-citation frontmatter.
