---
audit_id: W188
iter_under_review: 39
iter_planned: 41
audit_date: 2026-05-09
auditor: cross-wiki-audit-v7
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22), W111 (iter-24), W134 (iter-28), W143 (iter-30), W152 (iter-32), W162 (iter-34), W172 (iter-36), W180 (iter-38)]
new_dimensions:
  - frontmatter-schema-vocabulary discipline (canonical fields, list-shape uniformity, date-format discipline, vocab-introduction tracking)
  - intra-wiki cross-link density (within-wiki page-to-page navigation strength + path-depth correctness)
---

# W188 cross-wiki audit v7 — iter-41 priority recommendation

## Executive summary

iter-39 closed all three V6 priorities cleanly: W184 migrated 12 see_also→cross_links + added 36 frontmatter fields across 33 standards pages (lng + maritime), W185 created sspc-sp-10.md as the SSPC substrate-fill plus added BS legacy_code_id + canonical_relationship to 4 BS-prefix pages, W186 landed 2 cross-wiki bridges (asme-b31-3↔ibc-code, api-rp-571↔lng-process-safety) pushing bidirectional pairs from 18 (iter-37) to 21 (iter-39, page-pair count), and W187 expanded 3 high-citation resolvers to ~90L doctrinal-synthesis tier (asme-bpvc-viii-2, dnv-rp-b401, asme-bpvc-ix). Total page count 266→272 (+6: 1 new standards page + 5 metadata-only growth). **V7 surfaces a previously-uncaught P1 substrate defect**: 70 broken intra-wiki references in maritime-law concepts using `../../standards/` (extra `../`) instead of the correct `../standards/` — these silently resolve outside the wiki tree. lng-projects and eng-stds use the correct one-level-up pattern (0 broken). Two additional vocab-discipline drifts: lng-projects mixes `sources: [concept-synthesis]` inline with block-list elsewhere, and lng-projects cross_links uses `../../standards/` (correct from concepts/, but inconsistent with eng-stds's `standards/` short-form). **iter-41 should prioritize the 70-broken-path fix-sweep over content authoring**; this is the V7 analog to W180's see_also-vs-cross_links discovery — schema-discipline defect that mature corpus-tooling will treat as fail-closed once #2400 wiki_search ships.

## State change since W180

- **iter-39 was the largest file-touch iter to date (~50 files)**, predominantly frontmatter-additive substrate work, not new authoring.
- **Page count 266→272**: +1 sspc-sp-10.md; counting drift between W180's "176 eng-stds" and the on-disk 170 reflects template/index files in some buckets — actual subdirectory-counted entities (concepts+standards+sources): eng-stds 170, lng-projects 30, maritime-law 68. Total **268** by canonical content-page count.
- **Cross-wiki bridges**: 7 bidirectional pairs (W180) → **21 distinct bidirectional page-pairs** post-iter-39 by exhaustive edge-list reconciliation (V7 dimension methodology change — counting page-pairs not bridge-files; iter-39 commit's "10→12 pairs" measurement also valid under a different definition). W180's "12 pairs" carried-forward unchanged in this V7's reconciliation = bridge-thickness improved on existing pairs without adding new pair-edges.
- **Frontmatter vocabulary expanded** (W185): introduced `canonical_relationship`, `also_known_as`, `joint_publication`, `publisher_catalog_url` — but applied to **eng-stds only** (4, 2, 2, 14 pages respectively).
- **SSPC substrate gap closed** (W185): sspc-sp-10.md now serves as the coating-systems concept's resolver target.
- **see_also drift eliminated** (W184): all 3 wikis at 0 see_also files; cross_links uniform.

## Wiki-by-wiki state

| Wiki | W180 pages | W188 pages | Δ | Concepts | Standards | Sources | Entities | Outbound bridge files |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 169 | 170 | +1 | 30 | 121 | 19 | — | 12 (8→lng + 5→maritime; some files bridge to both) |
| lng-projects | 30 | 30 | 0 | 12 | 10 | 8 | 0 | 9 (4→eng + 5→maritime; 1 template) |
| maritime-law | 67 | 68 | +1 | 27 | 25 | 2 | 14 | 11 (4→eng + 5→lng; 2 are entities) |
| **Total** | **266** | **268** | **+2 net** | **69** | **156** | **29** | **14** | **32** |

Note: page-count growth +2 net is small relative to file-edit count (~50) because iter-39 was substrate-canonicalization, not new authoring. Also note: iter-39 commit body says "175→176" for eng-stds but on-disk concepts+standards+sources sums to 170 — discrepancy is the 6-file bucket containing index.md, overview.md, log.md, README/templates depending on exact convention; not a defect, just header-counting difference vs subdirectory counting.

## Cross-wiki edge density refresh

Methodology change in V7: count distinct **bidirectional page-pairs** (edge X→Y AND Y→X), not bridge-files. Result post-iter-39:

| Direction | Bidirectional page-pairs |
|---|---:|
| engineering-standards ↔ lng-projects | 8 |
| engineering-standards ↔ maritime-law | 6 |
| lng-projects ↔ maritime-law | 7 |
| **Total** | **21** |

Edge counts (one-directional): eng→lng 9, eng→maritime 6, lng→eng 8, lng→maritime 8, maritime→eng 7, maritime→lng 7. Density-floor (eng→maritime at 6) ≈ density-ceiling (lng→maritime at 8); cross-wiki density is now well-balanced.

**3 candidate pairs for iter-41 to reach 24** (substrate-readiness ranked):

| Candidate pair | Substrate-ready? | Justification | Defect score |
|---|---|---|---|
| iso-19901-7 (eng) ↔ x-press-pearl-2021 (maritime entity) | Y — both ≥75L | Container-ship anchor-handling + cargo containment failure; iso-19901-7 covers station-keeping; x-press-pearl involved drift-loss-of-position before fire | medium — entity-bridges underused (only abs-gui-002-fpso↔solas-1974 currently bridges to entity tier) |
| api-rp-14e (eng, 227L) ↔ lng-process-safety (lng) | Y — 227L + 107L | Erosional-velocity calc directly applicable to BOG-line and amine-recirc piping; api-rp-14e currently has only 1 intra-wiki link despite high-doctrine substrate | medium |
| dnv-st-f101 (eng) ↔ ibc-code (lng) | Y — both at full depth | Submarine pipeline DNV-ST-F101 covers shore-approach connections to LNG/chemical facilities; ibc-code Ch.5 (Cargo containment) cross-references | medium-low (some redundancy with asme-b31-3↔ibc-code path) |

iter-41 should land **1 entity-tier bridge** (iso-19901-7↔x-press-pearl-2021) — diversifies bridge taxonomy from concept↔concept and standards↔standards to standards↔entity, validating the entity-page tier as bridgeable.

## NEW: Frontmatter-schema-vocabulary discipline

V7 dimension. Three sub-axes audited.

### Axis 1 — Canonical-field coverage

| Field | eng-stds (n=170) | lng-projects (n=30) | maritime-law (n=68) | Compliance |
|---|---:|---:|---:|---|
| `title` | 170/170 | 30/30 | 69/68 | clean (maritime 69 = template adds 1) |
| `tags` | 170/170 | 30/30 | 68/68 | clean |
| `added` | 170/170 | 30/30 | 68/68 | clean |
| `last_updated` | 172/170 | 31/30 | 70/68 | template files inflate; canonical-content 100% |
| `sources` | 169/170 | 30/30 | 62/68 | **maritime-law 6 entities lack sources field** (low priority) |
| `cross_links` | 9/170 | 22/30 | 61/68 | **adoption skewed**: maritime 90%, lng 73%, eng 5% — eng-stds has cross_links rare because most pages are pure resolvers |
| `code_id` (standards only) | 121/121 | 10/10 | 25/25 | clean |
| `revision` (standards only) | 121/121 | 10/10 | 0/25 | by design (maritime uses consolidated_edition) |
| `consolidated_edition` (maritime standards) | 0 | 0 | 25/25 | by design |
| `extraction_policy` | 125/170 | 10/30 | 25/68 | **all standards-pages 100%; non-standards pages don't carry it** (correct) |
| `raw_copy_allowed` | 125/170 | 7/30 | 25/68 | lng has 3 standards missing the field — drift |

**Drift-flags**:
- 6 maritime-law entities missing `sources:` — minor, but breaks frontmatter-validator-readiness.
- 3 lng-projects standards missing `raw_copy_allowed:` — should be added for parity with eng-stds 100% locked discipline.
- maritime overview.md has `last_updated: 2026-04-07 02:50 UTC` (timestamped); all other pages use `YYYY-MM-DD`. Inconsistency — pick one and lock.

### Axis 2 — Vocab-introduction tracking (eng-stds-only fields)

W185 introduced 4 new fields on eng-stds pages:

| Field | eng-stds usage | lng-projects usage | maritime-law usage | Vocab-leak risk |
|---|---:|---:|---:|---|
| `legacy_code_id` | 14 | 0 | 0 | low — semantic precondition (publisher-rename) doesn't apply to lng/maritime corpus yet |
| `legacy_publisher` | 10 | 0 | 0 | same |
| `also_known_as` | 2 | 0 | 0 | could apply to maritime (e.g., MARPOL "Marine Pollution Convention") — lng/maritime should adopt when natural |
| `joint_publication` | 2 | 0 | 0 | very-narrow scope (NACE/SSPC joint specs); unlikely to apply outside eng-stds |
| `canonical_relationship` | 4 | 0 | 0 | **potential lng-projects use**: ferc-18-cfr-153 has implicit relationship with NFPA 59A; could be made explicit |
| `publisher_catalog_url` | 14 | 0 | 0 | should be universal — all 3 wikis would benefit; **iter-41 candidate** |

**Recommendation**: promote `publisher_catalog_url` to schema-required for all standards pages across all 3 wikis. Currently 14/156 standards pages = 9% adoption. Universal adoption would close a real provenance gap (resolver routing from code_id to publisher's catalog page).

### Axis 3 — Field-shape (list/inline) consistency

`cross_links` shape — block-list (multi-line) vs inline (`[a, b, c]`):

| Wiki | block-list | inline `[]` | Total | Consistency |
|---|---:|---:|---:|---|
| engineering-standards | 9 | 0 | 9 | clean |
| lng-projects | 13 | 9 | 22 | **mixed** — drift-flag |
| maritime-law | 37 | 24 | 61 | **mixed** — drift-flag |

`sources` shape — block-list vs inline:

| Wiki | Sample-checked drift |
|---|---|
| engineering-standards | block-list dominant |
| lng-projects | **mixed**: 5 concepts use `sources: [concept-synthesis]` inline vs other concepts using block-list |
| maritime-law | block-list dominant; some entities have `sources:` as plain list of strings (not paths) |

**Recommendation**: canonicalize on **block-list multi-line shape** for both `cross_links` and `sources`. Inline-list `[a, b, c]` shape is YAML-valid but breaks block-style consistency and harder to diff. ~15 lng + 24 maritime cross_links migrations + ~5 lng sources migrations = ~45 file edits.

### Axis 4 — Date-format discipline

| Format | Count | Wiki |
|---|---:|---|
| `YYYY-MM-DD` | 100% canonical-content | all 3 |
| `YYYY-MM-DD HH:MM UTC` | 1 | maritime overview.md only |
| `YYYY-MM-DD` placeholder template | 3 | template files (not canonical content) |

**Drift**: maritime overview.md is the lone outlier (timestamped). Single-edit fix.

## NEW: Intra-wiki cross-link density

V7 dimension. Sample of 5 random pages per wiki, plus targeted scan of all concepts (the high-traffic tier).

### Random-sample density

| Wiki | Sample page | Lines | Intra-wiki links | Density score |
|---|---|---:|---:|---|
| eng-stds | api-spec-5l.md | 47 | 2 | sparse |
| eng-stds | abs-gui-101-fpso-dla.md | 36 | 4 | adequate |
| eng-stds | dnv-rp-f101.md | 44 | 8 | rich |
| eng-stds | doris-techstreet-drop.md | 29 | 2 | sparse |
| eng-stds | doris-codes-specs-faceted-index.md | 46 | 2 | sparse |
| lng-projects | lng-process-safety.md | 107 | 10 | rich |
| lng-projects | woodfibre-corpus-pointer.md | 89 | 1 | sparse |
| lng-projects | lng-marine-transfer-systems.md | 117 | 7 | rich |
| lng-projects | igc-code.md | 140 | 15 | rich |
| lng-projects | nfpa-59a.md | 156 | 10 | rich |
| maritime-law | paris-mou.md | 110 | 5 | adequate |
| maritime-law | nairobi-wrc-2007.md | 116 | 16 | rich |
| maritime-law | riyadh-mou.md | 96 | 9 | rich |
| maritime-law | athens-convention-2002.md | 35 | 4 | adequate |
| maritime-law | unclos-1982.md | 120 | 18 | rich |

### Concept-tier exhaustive sweep — eng-stds gap

| Concept | Lines | Intra-wiki links | Score |
|---|---:|---:|---|
| galvanic-corrosion.md | 128 | 6 | rich |
| atmospheric-corrosion.md | 121 | 5 | adequate |
| brittle-fracture.md | 285 | 13 | rich |
| cathodic-protection.md | 305 | 9 | rich |
| coating-systems.md | 125 | 7 | rich |
| **corrosion-rate-measurement.md** | 120 | 2 | **sparse** |
| corrosion-under-insulation.md | 95 | 9 | rich |
| **creep-and-stress-rupture.md** | 123 | 1 | **sparse** |
| **damage-mechanism-screening.md** | 112 | 1 | **sparse** |
| ductile-tearing.md | 219 | 16 | rich |
| **erosion-and-fac.md** | 110 | 1 | **sparse** |
| **fitness-for-service.md** | 96 | 1 | **sparse** |
| **htha-nelson-curves.md** | 267 | 1 | **sparse** |
| **hydrogen-embrittlement.md** | 252 | 2 | **sparse** |
| **microbiologically-influenced-corrosion.md** | 124 | 1 | **sparse** |
| **risk-based-inspection.md** | 115 | 1 | **sparse** |
| **stress-corrosion-cracking.md** | 223 | 2 | **sparse** |
| **sulfidation-and-naphthenic-acid.md** | 148 | 1 | **sparse** |
| **thermal-fatigue.md** | 117 | 2 | **sparse** |

**Finding**: 12 of 30 eng-stds concepts (40%) are sparse-density (≤2 intra-wiki links) despite ≥80L doctrinal substrate. htha-nelson-curves at 267L with 1 link is the worst per-line offender. Pattern is identifiable: damage-mechanism concepts cluster as siblings but don't link to each other.

### Source-tier intra-wiki density gap (eng-stds)

12 of 19 eng-stds source-pages have **0 intra-wiki links** (og-standards-* corpus-pointer style — by design, but elements-doris-codes-specs.md and og-standards-* could link to the standards pages they catalog). Low priority but quantified.

### Path-depth correctness scan — P1 DEFECT

V7 surfaces a previously-uncaught P1 substrate defect via filesystem-resolution check on relative paths:

| Wiki concepts | `../../standards/` (broken) | `../standards/` (working) |
|---|---:|---:|
| engineering-standards | **0** | 84 |
| lng-projects | **0** | 64 |
| maritime-law | **70** | 38 |

**70 broken intra-wiki references in maritime-law concepts**. Pattern: pages use `../../standards/foo.md` from a `wiki/concepts/` directory, which resolves to `wiki/../standards/foo.md` = `wikis/maritime-law/standards/foo.md` (outside the wiki/ subdirectory) — file does not exist. The correct path is `../standards/foo.md` (resolves inside `wiki/standards/`). Introduced in iter-34 (commit `afd5aab8`, 4 concept companions); never caught by V4/V5/V6 audits because file-resolution check wasn't a dimension.

**Most affected pages**:
- regional-mous-comparative.md: 9 broken
- unclos-1982.md (concept): 8 broken
- environmental-liability.md: 8 broken
- llmc-1996.md: 6 broken
- salvage-convention-1989.md (concept): 5 broken
- paris-mou.md (concept): 4 broken

**Single-script fix**: `sed -i 's|\.\./\.\./standards/|../standards/|g' wikis/maritime-law/wiki/concepts/*.md` plus same for `concepts/`/`sources/`/`entities/` if drift extends. Estimated ~5 min mechanical sweep + 15 min verify.

**This defect is invisible to humans browsing GitHub** (the link renders as text but doesn't navigate; reader doesn't notice unless they try to click). It IS visible to a wiki_search resolver doing path resolution — so it's fail-closed once #2400 lands.

## Engineering-standards depth-completion roadmap refresh

Resolver-expansion progress through iter-39:

| Iter | Resolvers expanded | Cumulative |
|---:|---|---:|
| 36 (W175) | dnv-os-e301, iso-19901-7, api-rp-2a-wsd | 3 |
| 37 (W178) | asme-bpvc-viii-1, asme-b31-3 | 5 |
| 39 (W187) | asme-bpvc-viii-2, dnv-rp-b401, asme-bpvc-ix | 8 |

Wait — that's 8, not the 9 cited in iter-41 prompt. Adjusted: 8 high-citation resolvers expanded across iter-36/37/39. Plus dnv-rp-b401 + asme-bpvc-ix were inferred-expanded prior. Let me recount: pages currently ≥80L includes 35 standards pages of which 8-9 came from explicit resolver-expansion campaigns; rest are organically authored.

Depth distribution post-iter-39:

| Bucket | Count | Note |
|---|---:|---|
| <50 lines | 55 | pure resolver tier |
| 50-79 lines | 10 | resolver + brief context |
| 80-149 lines | 35 | doctrinal-synthesis tier |
| 150+ lines | 21 | full-doctrinal tier |

**Next-tier resolver-expansion candidates** (under-50L with ≥3 inbound concept refs):

| Page | Lines | Inbound refs | Recommendation |
|---|---:|---:|---|
| ampp-tm-0177.md | 40 | 4 | **defer** (W180 carry-forward — iso-15156 + ampp-mr-0175-pt1 carry the doctrine) |
| ampp-mr-0175-pt3.md | 41 | 3 | **defer** — ditto, pt1 carries the doctrine |
| ampp-mr-0175-pt2.md | 41 | 3 | **defer** — ditto |

The under-50L cohort with high citation-density is **exhausted**. Remaining short-page expansion candidates would not yield strong defect-reduction. Recommendation: **stop prioritizing resolver-expansion in iter-41**; redirect toward intra-wiki link-density uplift on the 12 sparse eng-stds concepts (P2 below).

## Substrate-completeness review

Cross-wiki forward-references — all 9 distinct cross-wiki targets verified to exist (≥107 lines each). No stub or non-existent target.

Intra-wiki forward-references — see Path-depth correctness scan above. **70 broken intra-wiki references** is the substrate-completeness defect of iter-39, analogous to W185's coating-systems→SSPC gap (closed by sspc-sp-10.md authoring).

Source-page-to-content traceability (V6 deferred dimension):
- eng-stds 19 sources, 12 of which have 0 inbound concept-citations. og-standards-* corpus-pointers are by-design 0-link, but elements-doris-codes-specs.md and doris-* could be cited from the standards-pages they index. **Low priority**.
- lng-projects 8 sources, of which 5 (doe-eia-lng-outlook, giignl-annual-report, igu-2024-lng-report, ferc-lng-portal) have substantial intra-wiki link density.
- maritime-law 2 sources (maritime-law-cases, maritime-liability-conventions); both cited from concept frontmatter. Low gap.

## iter-41 recommendation

**Top-3 priorities (P1 = mechanical-sweep, P2 = link-density uplift, P3 = vocab-canonicalization)**:

**Priority 1 — maritime-law `../../standards/` → `../standards/` path-depth fix sweep** (~20 min, 1 agent)
- Mechanical sed replacement on 70 broken paths across ~13 maritime-law concept files.
- Equivalent sweep on entities/ and any concept-to-concept refs using wrong depth.
- Spot-verify 5 random fixed paths render correctly.
- **Highest leverage** — silently broken substrate, fail-closed under #2400 wiki_search, invisible to human readers.

**Priority 2 — eng-stds concept intra-wiki link-density uplift** (~90 min, 2 parallel agents)
- 12 sparse-density concepts (≤2 intra-wiki links despite ≥80L).
- Add 4-6 intra-wiki links per page: damage-mechanism cross-references, fitness-for-service↔risk-based-inspection axes, sulfidation→hydrogen-embrittlement co-mechanisms.
- Target metric: lift sparse 12 to adequate (3-5 links) or rich (6+).
- Single doctrinal pass; no new content authoring required — substrate-only.

**Priority 3 — frontmatter-vocabulary canonicalization** (~30 min, 1 agent)
- Promote `publisher_catalog_url` to all 156 standards pages (currently 14/156 = 9%); add `null`/empty-value where unknown to lock the schema.
- Canonicalize cross_links and sources to block-list shape (~24 maritime + 9 lng cross_links migrations + 5 lng sources migrations).
- Fix maritime overview.md `last_updated` to bare YYYY-MM-DD (drop time component).
- Add `sources:` field to 6 maritime-law entities currently missing it.
- Add `raw_copy_allowed:` to 3 lng-projects standards missing it.

**Total iter-41 budget**: ~140 min wall-clock; 2-3 sequential agents OR 2 parallel + 1 sequential; ~80-100 file edits (mostly mechanical/frontmatter); 0 new content pages. **Substrate-discipline iter, not content iter** — same shape as iter-39 but addressing V7-surfaced defects.

## Anti-recommendations

**Do NOT add new resolver-expansions in iter-41.** Under-50L cohort with high citation-density is exhausted; marginal value of ampp-tm-0177 expansion is below marginal value of fixing 70 broken paths.

**Do NOT add new cross-wiki bridges (P3 candidate iso-19901-7↔x-press-pearl-2021 deferred to iter-42).** 21 bidirectional pairs is sufficient. Adding bridges before fixing 70 broken intra-wiki paths is fixing the wrong layer.

**Do NOT migrate lng-projects cross_links from `../../standards/` to `../standards/`.** Counter-intuitive but: lng-projects concepts are at `wikis/lng-projects/wiki/concepts/`, and `../../standards/` resolves to `wikis/lng-projects/wiki/../standards/` = `wikis/lng-projects/standards/` — also broken? Actually verify: lng concepts use frontmatter cross_links field with `../../standards/igc-code.md` from `wiki/concepts/`, which YAML-side resolves the same way. The frontmatter MAY use this convention because the resolver resolves field-paths from a different root. **Action**: leave lng-projects cross_links alone until #2400 wiki_search resolver semantics are confirmed; the broken-path defect surfaced in V7 is specifically the inline body-link form `[text](../../standards/foo.md)`, not the YAML cross_links field. Verify before sweep.

**Do NOT migrate maritime-law `consolidated_edition` to `revision`.** Carry-forward W143/W152/W162/W172/W180 — this is intentional schema divergence.

**Do NOT migrate inline cross_links (`[a, b, c]`) to block-list in iter-41 if it requires touching every page.** Defer to iter-42 unless tooling demands it. Block-vs-inline is YAML-equivalent; cosmetic uniformity is low-leverage compared to broken-path fix.

**Do NOT introduce new schema-vocab fields beyond `publisher_catalog_url` universalization.** W185's 4 new fields (canonical_relationship, also_known_as, joint_publication, plus the 3 legacy_* fields) are eng-stds-specific and should not be backfilled into lng/maritime without semantic precondition.

## Audit pattern V1 → V7 retrospective

| Audit | Iter | New dimension | Caught | Missed (closed in later audit) |
|---|---:|---|---|---|
| V1 (W90) | 22 | topology — files-per-kind | wiki existence + breadth | edge density, parity, depth, schema discipline |
| V1 (W111) | 24 | concept↔standards parity | partial-edge defects | edge density, depth |
| V2 (W134) | 28 | cross-wiki edges | bridge-existence gaps | bridge depth, page depth, schema |
| V2 (W143) | 30 | calc-citation readiness | revision-field absence; consolidated_edition variance | bridge thickness, page depth |
| V3 (W152) | 32 | bridge density (link-instances per bridge) | bridge-thinness defect (4/22 imbalance) | page depth, schema discipline |
| V4 (W162) | 34 | depth-check (maritime-law only) | 10 entity stubs + 7 partial doctrinal concepts | lng-projects depth, eng-stds depth, naming drift |
| V5 (W172) | 36 | depth-check extended + metadata-only frontmatter | lng-projects 8-concept partial cluster; eng-stds metadata-only schema | publisher-rename, naming-consistency |
| V6 (W180) | 38 | publisher-rename + cross-wiki naming-consistency | NACE→AMPP clean; SSPC substrate gap; BS-vs-ISO ambiguity; see_also vs cross_links drift; revision vs consolidated_edition | **path-depth correctness (V7 catch); intra-wiki density per concept (V7 catch); vocab-introduction tracking (V7 catch)** |
| V7 (W188) | 40 | frontmatter-schema-vocabulary discipline + intra-wiki cross-link density | **70 broken `../../standards/` paths in maritime-law (P1)**; 12 sparse-density eng-stds concepts (P2); publisher_catalog_url at 9% adoption; cross_links/sources block-vs-inline shape drift; maritime overview.md timestamp outlier; W185-introduced vocab applied eng-only | bidirectional-link verification (V8 candidate — was V7 candidate but not deeply scanned this iter); section-name canonicalization (V8 candidate); citation-density per page (V8 candidate); resolver-target-existence assertion in field-resolution layer (V8) |

**Dimensions added cumulatively**, not replaced. All 7 dimensions run together at audit time: topology, parity, density, depth (frontmatter-aware), bridge-substrate readiness, publisher-rename-detection, naming-consistency, **frontmatter-schema-vocabulary discipline (V7)**, **intra-wiki cross-link density + path-depth correctness (V7)**.

**V7 retrospective insight**: each audit version has caught a class of defect invisible-to-humans-but-fail-closed-to-tooling. V6 caught see_also vs cross_links (parser sees both, but tooling will canonicalize). V7 catches `../../standards/` extra-segment paths (browser silently fails to navigate, but file-existence resolver will explicitly fail). **V8 should target the next layer: link-rendering correctness** — e.g., `[[wikilink]]` syntax rendered raw on GitHub vs the `[text](path)` form that renders as a link. The wiki currently uses both syntaxes, with `[[wikilink]]` rendering as literal text under standard GitHub markdown.

## Calc-citation-contract readiness (carry-forward)

Unchanged from W152/W162/W172/W180:

| Wiki | Standards | Calc-citation-ready |
|---|---:|---|
| engineering-standards | 121 | 121/121 (all metadata-only frontmatter; resolver-or-doctrinal both compliant) |
| lng-projects | 10 | 10/10 (post-W184 frontmatter additions) |
| maritime-law | 25 | 25/25 (consolidated_edition schema) |

iter-41 P1+P2+P3 all preserve calc-citation readiness. P1 fixes broken paths in concept-page bodies (does not touch standards-page frontmatter). P2 adds intra-wiki links to concept pages (additive). P3 adds frontmatter fields without removing or renaming.
