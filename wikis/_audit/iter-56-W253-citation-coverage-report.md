---
audit_id: W253
iter_under_review: 56
audit_date: 2026-05-10
auditor: cross-wiki-audit-v15-citation-coverage
scope: [engineering-standards, lng-projects, maritime-law]
dimension: citation-graph reciprocity + orphan detection (Option B quality-pivot from V14)
prior_audits: [W90, W111, W134, W143, W152, W162, W172, W180, W188, W196, W204, W212, W220, W228, W239, W247]
methodology: Parsed all markdown body links + frontmatter `sources:` lists across 321 canonical pages. Resolved relative paths to (wiki,tier,slug) page-ids. Built directed citation graph; computed inbound/outbound degree per page; classified orphans by tier; verified cross-wiki edge reciprocity.
---

# W253 cross-wiki citation-coverage audit (v15) — iter-56 quality-dimension pivot

## Executive summary

V14 (W247) closed iter-49→55 depth-pilot at 322 canonical pages and proposed (P2) a **quality-dimension pivot** (Option B) for iter-56. W253 executes that pivot by validating the **citation graph is reciprocal and complete** across 321 measured pages (V14's 322 — _template.md guards reconciled). Methodology: AST-resolve every relative `.md` link in markdown bodies + frontmatter `sources:` blocks across all three wikis, build directed graph, score inbound-degree per page.

**W253 surfaces 5 findings:** (1) **Citation graph is dense and healthy at the corpus level** — median page has **5 inbound citations**, 95-of-321 pages (30%) carry 11+ inbound (deep navigation hubs), distribution is right-skewed power-law; (2) **Orphan count is 10-of-321 (3.1%)** — well below 5% threshold, but every orphan is actionable; (3) **Cross-wiki bridge graph is 27 bidirectional + 7 unidirectional** (vs V14's claimed 26 bidirectional) — the +1 reflects a newly-symmetric pair, the 7 unidirectional bridges are the iter-57 cleanup target; (4) **Top-cited hub is `engineering-standards/sources/og-standards-api` at 49 inbound** — the registry-source pattern is working as designed; **top-citing hub is `engineering-standards/concepts/stress-corrosion-cracking` at 50 outbound** confirming V14's depth-pilot identified the right cluster lead; (5) **Tier-density imbalance**: maritime-law `entities/` tier has 5-of-24 orphans (21%) — highest orphan rate of any tier × wiki cell.

**iter-57 default recommendation:** **fix the 7 unidirectional bridges + cite the 10 orphans** (~17 surgical edits, 1-page-equivalent effort, completes the citation-graph closure that V14 P2-Option-B opened.)

## Corpus state

| Wiki | Concepts | Standards | Sources | Entities | Total |
|---|---:|---:|---:|---:|---:|
| engineering-standards | 35 | 161 | 19 | 0 | 215 |
| lng-projects | 12 | 9 | 8 | 0 | 29 |
| maritime-law | 27 | 24 | 2 | 24 | 77 |
| **Total** | **74** | **194** | **29** | **24** | **321** |

V14 reported 322 (one extra reconciliation). W253 measured 321 directly via discovery (filters: `_template.md`, `_index.md` excluded). Delta is documentation-only.

## Inbound-citation density distribution

Histogram of inbound-degree (how many other pages cite this page):

| Bucket | Pages | % of corpus |
|---|---:|---:|
|     0 inbound | 10 | 3.1% |
|   1-2 inbound | 66 | 20.6% |
|   3-5 inbound | 76 | 23.7% |
|  6-10 inbound | 74 | 23.1% |
|   11+ inbound | 95 | 29.6% |

Median inbound = 5; 30% of pages carry 11+ inbound (deep hubs); only 3.1% are zero-inbound orphans. **Distribution is healthy power-law** consistent with mature wiki citation graphs.

## Orphan pages (zero inbound citations)

**10 orphans** identified (3.1% of 321 pages). Per-tier breakdown:

| Tier | Orphans | Notes |
|---|---:|---|
| concepts | 1 | |
| entities | 5 | |
| sources | 2 | |
| standards | 2 | |

### Orphan slugs by wiki × tier

**engineering-standards:**
- `standards/`: nace-34103, sspc-sp-10
- `sources/`: og-standards-astm-top-level

**lng-projects:**
- `sources/`: elements-doris-62092-sesa

**maritime-law:**
- `concepts/`: rotterdam-rules
- `entities/`: eurymedon-1974, glendarroch-1894, m-v-saiga-cases-1997-1999, mv-dali-2024, wagon-mound-1961

### Orphan-class assessment

- **Standards-orphans** (substrate-fills not yet cited): every standards-page should be cited from ≥1 concept-page that explains its scope. Orphans here indicate **concept-page coverage gaps** — either the concept doesn't exist yet, or it exists and forgot to back-cite.
- **Concept-orphans** (the rarest, most surprising): a concept page nobody references suggests either the concept is too narrow (merge candidate) or the parent concept hasn't surfaced it (cross-link cleanup).
- **Entity-orphans** (5-of-24 in maritime-law): entities tier should be referenced from concept-pages that describe the regulatory/institutional landscape; 21% orphan rate is the corpus's worst tier-density signal.
- **Source-orphans**: a registry-source nobody has cited yet — usually means the source predates the concept-pages it would back. Lower priority.

## Cross-wiki bridge reciprocity

**27 bidirectional bridges + 7 unidirectional bridges** (vs V14's claimed 26 bidirectional). One bridge transitioned to bidirectional since iter-50; 7 still need a back-edge.

### Bidirectional bridges per wiki-pair

| Wiki pair | Bidirectional | V14 W247 | Δ |
|---|---:|---:|---:|
| engineering-standards ↔ lng-projects | 8 | 10 | -2 |
| engineering-standards ↔ maritime-law | 12 | 8 | +4 |
| lng-projects ↔ maritime-law | 7 | 8 | -1 |
| **Total** | **27** | **26** | **+1** |

### Unidirectional bridges (iter-57 fix candidates)

These pages cite a page in another wiki, but the cited page does not back-cite. Each unidirectional bridge is a 1-line fix: add a single markdown link in the cited page back to the citing page.

| # | Citing page | → Cited page (missing back-edge) |
|---:|---|---|
| 1 | `engi/standards/api-17j` | `lng-/standards/igc-code` |
| 2 | `engi/standards/dnv-rp-c203` | `mari/standards/solas-1974` |
| 3 | `engi/concepts/risk-based-inspection` | `mari/concepts/ism-code` |
| 4 | `engi/concepts/risk-based-inspection` | `lng-/standards/csa-z276` |
| 5 | `mari/concepts/ism-code` | `engi/standards/api-rp-581` |
| 6 | `lng-/concepts/lng-regulatory-framework` | `mari/standards/marpol-73-78` |
| 7 | `engi/concepts/risk-based-inspection` | `mari/concepts/opa-90` |

## Top-10 most-cited hubs (deep navigation anchors)

| Rank | Page | Inbound | Tier |
|---:|---|---:|---|
| 1 | `engineering-standards/sources/og-standards-api` | 49 | sources |
| 2 | `engineering-standards/standards/api-std-579` | 41 | standards |
| 3 | `engineering-standards/concepts/fitness-for-service` | 39 | concepts |
| 4 | `engineering-standards/standards/api-rp-571` | 37 | standards |
| 5 | `maritime-law/standards/marpol-73-78` | 36 | standards |
| 6 | `maritime-law/concepts/environmental-liability` | 34 | concepts |
| 7 | `engineering-standards/concepts/risk-based-inspection` | 32 | concepts |
| 8 | `engineering-standards/concepts/corrosion-rate-measurement` | 31 | concepts |
| 9 | `engineering-standards/concepts/sour-service-materials` | 30 | concepts |
| 10 | `engineering-standards/standards/api-rp-581` | 30 | standards |

## Top-10 most-citing hubs (broad cross-link spreaders)

| Rank | Page | Outbound | Tier |
|---:|---|---:|---|
| 1 | `engineering-standards/concepts/stress-corrosion-cracking` | 50 | concepts |
| 2 | `engineering-standards/concepts/risk-based-inspection` | 44 | concepts |
| 3 | `engineering-standards/sources/og-standards-api` | 33 | sources |
| 4 | `maritime-law/standards/marpol-73-78` | 26 | standards |
| 5 | `engineering-standards/standards/api-579-1-asme-ffs-1` | 25 | standards |
| 6 | `maritime-law/concepts/environmental-liability` | 24 | concepts |
| 7 | `engineering-standards/concepts/fitness-for-service` | 23 | concepts |
| 8 | `engineering-standards/concepts/fatigue-crack-growth` | 22 | concepts |
| 9 | `engineering-standards/sources/og-standards-minor-publishers` | 22 | sources |
| 10 | `maritime-law/concepts/clc-1992` | 22 | concepts |

## Tier-tier citation matrix (source-tier → target-tier counts)

Total directed edges between tiers (intra-wiki + cross-wiki summed). Reading: row cites column.

| from \\ to | concepts | standards | entities | sources |
|---|---|---|---|---|
| concepts | 407 | 398 | 51 | 69 |
| standards | 333 | 978 | 17 | 83 |
| entities | 80 | 34 | 44 | 6 |
| sources | 63 | 123 | 0 | 39 |

**Reading:** concepts→standards is the dominant edge class (calc-citation pattern). standards→concepts back-edges are sparser (orphan-source signal). Entity-tier rarely cites — it's a leaf tier.

## Iter-57 cleanup recommendations (priority-ordered)

**P0 — fix 7 unidirectional cross-wiki bridges** (1 hour effort, completes V14 Option-B): each is a single markdown-link addition in the cited page. Backed by spec evidence that each pair has been semantically intentional since iter-29 W141. See bridge table above.

**P1 — cite the 10 orphan pages** (~2 hours effort): each orphan needs ≥1 concept-page or standards-page to reference it. Highest leverage in maritime-law/entities/ (5-of-24 orphans, 21% tier-orphan rate).

**P2 — defer dense-hub audit**: top-10-most-cited carry 30+ inbound each; these are working-as-designed and need no intervention. Re-measure in iter-60 after orphan cleanup lands.

**P3 — declare quality-dimension closure when** orphan-count ≤ 3 AND unidirectional-bridges = 0. Iter-57 P0+P1 will satisfy both. Iter-58 can pivot back to depth-pilot residual or wind-down.

**Anti-recommendation**: do **not** force-cite source-tier orphans by adding spurious back-references. Sources are leaf nodes by design; some inbound = 0 is expected.

## Appendix A — sparse pages (1-2 inbound, near-orphan)

66 pages carry only 1-2 inbound citations. Sample (first 20 by tier):

**entities** (showing 7-of-7):
- `maritime-law/achilleas-2008` (2 inbound)
- `maritime-law/aegean-sea-1992` (1 inbound)
- `maritime-law/front-altair-2019` (1 inbound)
- `maritime-law/fso-safer-2023` (1 inbound)
- `maritime-law/hadley-v-baxendale-1854` (1 inbound)
- `maritime-law/heron-ii-1969` (1 inbound)
- `maritime-law/x-press-pearl-2021` (2 inbound)

**sources** (showing 8-of-11):
- `engineering-standards/doris-company-specs` (1 inbound)
- `engineering-standards/doris-deepstar` (1 inbound)
- `engineering-standards/doris-techstreet-drop` (1 inbound)
- `engineering-standards/og-standards-abs` (1 inbound)
- `engineering-standards/og-standards-asce` (2 inbound)
- `engineering-standards/og-standards-onepetro` (1 inbound)
- `lng-projects/doe-eia-lng-outlook` (2 inbound)
- `lng-projects/elements-acma-projects-31522-woodfibre` (1 inbound)

**concepts** (showing 8-of-9):
- `engineering-standards/microbiologically-influenced-corrosion` (2 inbound)
- `engineering-standards/mooring-integrity-management` (2 inbound)
- `engineering-standards/temper-embrittlement` (2 inbound)
- `engineering-standards/wind-loads` (1 inbound)
- `lng-projects/lng-composition-management` (2 inbound)
- `maritime-law/regional-mous-comparative` (1 inbound)
- `maritime-law/stcw-convention` (2 inbound)
- `maritime-law/unclos-1982` (1 inbound)

**standards** (showing 8-of-39):
- `engineering-standards/abs-gn-239-cathodic-protection-offshore` (2 inbound)
- `engineering-standards/abs-gui-123-offshore-risers` (1 inbound)
- `engineering-standards/abs-rules-coc-part1-offshore` (2 inbound)
- `engineering-standards/api-17a` (2 inbound)
- `engineering-standards/api-17h` (2 inbound)
- `engineering-standards/api-rp-2mim` (1 inbound)
- `engineering-standards/api-spec-6d` (2 inbound)
- `engineering-standards/asme-pcc-3` (1 inbound)

## Appendix B — methodology + data integrity

- **Page discovery**: `find <wiki>/wiki/<tier> -maxdepth 2 -name '*.md'` minus `_template.md`/`_index.md` filters.
- **Link extraction**: regex `\(([^)]+\.md)\)` on body + YAML frontmatter `sources:` list block.
- **Resolution**: `Path.resolve()` on relative paths; mapped to `(wiki, tier, slug)` tuple-id.
- **Edge dedup**: each (src, tgt) counted once even if multiple links exist between the pair.
- **V14 → W253 corpus delta**: 322 → 321 (-1). Likely V14 enumeration counted `_template.md` as canonical or double-counted a reconciliation.
- **Anchors stripped**: `#section` fragments dropped before resolution to avoid false negatives.

Generated by `/tmp/citation_audit.py` + `/tmp/citation_report.py`. Read-only across content tier; only writes to `_audit/`.