---
audit_id: W134
iter_under_review: 27
iter_planned: 29
audit_date: 2026-05-09
auditor: cross-wiki-audit
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22 → eng-standards saturation), W111 (iter-24 → maritime-law pickup)]
---

# W134 cross-wiki audit — iter-29 priority recommendation

## Executive summary

After iter-27 closed the maritime-law concept↔standards parity for the IMO/ILO liability stack (CLC / Bunkers / ISPS / STCW / Athens / HNS), the highest-leverage iter-29 work is **not a new wiki pivot** — it is the **bidirectional cross-wiki bridge layer**, which is currently near-zero (only 1 of 3 wiki pairs has any outbound edge, and zero have return-edges). Engineering-standards remains saturated at 167 pages with sub-5%-iteration-lift, lng-projects has a hard backlog of 3 standards (api-std-625, csa-z276, en-1473) cited from zero concept pages, and maritime-law has 9 concept-only / 9 standards-only stems plus a slug mismatch (bunker- vs bunkers-) that breaks tooling. Iter-29 should ship cross-wiki bridge edges first, close the lng-projects internal back-link backlog second, and reconcile maritime-law parity gaps third — defer any naval-architecture / pipeline / refining pivot until W134 successor audit confirms bridge-layer convergence.

## Wiki-by-wiki state

| Wiki | Total pages | Concepts | Standards | Sources | Entities | Last iter | Cadence signal |
|---|---:|---:|---:|---:|---:|---:|---|
| engineering-standards | 167 | 30 | 118 | 19 | 0 | iter-22 (paused per W90) | 16 log entries; saturated |
| lng-projects | 21 | 8 | 8 (+1 template) | 5 | 0 | iter-23-24 | 4 log entries; mid-bootstrap |
| maritime-law | 46 | 17 | 17 (+1 template) | 2 | 10 | iter-25-26-27 | 6 log entries; hottest wiki |

**Key observations:**

- **engineering-standards** is the heaviest wiki by far (167 pages, 7.96× lng-projects). Sub-5%-iteration-lift was the W90 pause trigger and remains correct: 17 of 30 concepts have **zero** standards back-links, but the standards corpus is 118-deep so each new standards-page touches ≤5% of current scope.
- **lng-projects** has perfect 1:1 concept:standards count (8:8) but 3 standards (api-std-625, csa-z276, en-1473) are orphaned with **0** concept back-links — a known iter-24 backlog item ("8 existing concepts pages need return-links to the 5 new standards pages") that did not actually land. The W107 cross-link sweep advertised 24 return-links but the file-grep confirms only 5 of 8 standards are reachable from concepts.
- **maritime-law** is the most active wiki by recent iteration count (3 iters in one day on 2026-05-09). Iter-27 closed concept↔standards parity *for the convention pages that already had concept pages*, but **9 concept stems still have no standards companion** and **9 standards stems have no concept companion**. The total-pages count is inflated by the entities/ subdirectory (10 historical-case pages migrated from YAML seed) which is a one-shot import, not a recurring cadence.
- **Sources gap on maritime-law:** only 2 source pages support 17 standards + 17 concepts + 10 entities. Compare lng-projects 5 sources / 21 pages (24%) and engineering-standards 19 sources / 167 pages (11%). Maritime-law sources/source-page ratio is 4.3% — likely a structural artifact (treaty-text is the source) but worth noting if external citations are added.

## Concept↔standards parity gaps

### engineering-standards

(Stems do not 1:1 match because concepts are damage-mechanisms and standards are publisher codes. Gap = concepts cited from **zero** standards pages, ranked by topical centrality to the existing API RP 571 / 581 spine.)

| Concept (no standards back-link) | Topical anchor | Recommended standards pair |
|---|---|---|
| atmospheric-corrosion | new in iter-22; ISO 9223 not yet authored | iso-9223 (atm-corrosivity classification) |
| risk-based-inspection | RBI is the methodology spine; API 580/581 standards exist | back-link from api-rp-580.md / api-rp-581.md |
| fitness-for-service | FFS is the integrity-assessment spine; API 579 + BS 7910 standards exist | back-link from api-std-579.md / bs-7910 |
| damage-mechanism-screening | screens to RP 571 mechanism families | back-link from api-rp-571.md |
| coating-systems | new in iter-22; NACE SP0108 / ISO 12944 not yet | iso-12944 (atmospheric-coating system) |

### lng-projects

(Hard 8:8 stem count but 3 standards are unreachable from any concept. iter-29 should treat this as a **return-link backlog**, not new-page work.)

| Standard (zero concept back-link) | Concept(s) that should link in | Already-authored anchor |
|---|---|---|
| api-std-625 (refrigerated tanks) | lng-storage-tanks, lng-process-safety | both exist |
| csa-z276 (Canada LNG) | lng-regulatory-framework, lng-storage-tanks | both exist |
| en-1473 (EU LNG plant) | lng-regulatory-framework, lng-process-safety, lng-project-shapes | all exist |
| (gap-fill) IGF Code | lng-marine-transfer-systems, lng-regulatory-framework | needs new standards/igf-code.md |
| (gap-fill) ISO 16903 (LNG props) | lng-process-safety, lng-boil-off-gas-management | needs new standards/iso-16903.md |

### maritime-law

(9 concept-only + 9 standards-only stems. Slug-mismatch on bunker(s) is a P0 fix.)

| Gap type | Stem | Recommended action |
|---|---|---|
| **slug mismatch** | concepts/bunker-convention-2001 vs standards/bunkers-convention-2001 | rename concept → bunkers-convention-2001 (standards-side is grammatically correct) |
| concept-only (no standards) | charterparties | concept covers commercial law not treaty text — DEFER (out of scope for standards/) |
| concept-only (no standards) | environmental-liability | concept synthesizes 4 conventions — DEFER (synthesis page, not 1:1 treaty) |
| concept-only (no standards) | flag-state-jurisdiction | doctrine concept anchored in UNCLOS Art. 91-94 — back-link to standards/unclos-1982.md, no new file |
| concept-only (no standards) | general-average | concept covers York-Antwerp Rules — back-link to standards/york-antwerp-rules.md, no new file |
| concept-only (no standards) | ism-code | iter-26 already shipped this in standards/ but slug check needed |
| concept-only (no standards) | limitation-of-liability | doctrine concept anchored in LLMC 1996 — back-link to standards/llmc-1996.md, no new file |
| concept-only (no standards) | port-state-control | doctrine concept anchored in Paris MoU — back-link to standards/paris-mou.md, no new file |
| concept-only (no standards) | salvage | doctrine concept anchored in Salvage Convention 1989 — back-link to standards/salvage-convention-1989.md, no new file |
| standards-only (no concept) | hague-visby-rules | needs concepts/hague-visby-rules.md (carriage-of-goods regime) |
| standards-only (no concept) | isps-code | iter-27 added standard but concept still missing |
| standards-only (no concept) | paris-mou | needs concepts/paris-mou.md (PSC enforcement regime) |
| standards-only (no concept) | rotterdam-rules | needs concepts/rotterdam-rules.md (multimodal carriage; not yet in force) |
| standards-only (no concept) | salvage-convention-1989 | back-link from concepts/salvage.md sufficient (no new concept file) |
| standards-only (no concept) | stcw-convention | iter-27 added standard but concept still missing (training-and-watchkeeping doctrine) |
| standards-only (no concept) | unclos-1982 | iter-25 added standard; needs concepts/unclos-1982.md (constitutional treaty) |
| standards-only (no concept) | york-antwerp-rules | back-link from concepts/general-average.md sufficient |

**Top 5 highest-priority maritime-law gap-fills for iter-29:**
1. Fix bunker(s) slug mismatch (P0 tooling break)
2. Add 8 doctrine→treaty back-links (concepts/{flag-state-jurisdiction, general-average, limitation-of-liability, port-state-control, salvage} → existing standards pages) — pure edit, no new pages
3. Author concepts/unclos-1982.md (constitutional-treaty concept page)
4. Author concepts/{isps-code, stcw-convention}.md (already-shipped standards still missing concept-pair)
5. Author concepts/hague-visby-rules.md (carriage-of-goods regime)

## Cross-wiki bridge gaps

Currently zero engineering-standards outbound edges; one maritime-law outbound (solas → igc-code) with **no return-edge**. iter-29 should ship the following bidirectional bridge edges (each is two file-edits, no new content):

| # | Edge A | Edge B (return-link) | Topical justification |
|---|---|---|---|
| 1 | maritime-law/standards/solas-1974.md → lng-projects/standards/igc-code.md | lng-projects/standards/igc-code.md → maritime-law/standards/solas-1974.md | already half-built; SOLAS Ch. VII Part C is the IGC parent. **This is the lowest-friction bridge edit in the whole repo.** |
| 2 | maritime-law/standards/hns-convention-2010.md → lng-projects/standards/igc-code.md | lng-projects/standards/igc-code.md → maritime-law/standards/hns-convention-2010.md | HNS Article 1 explicitly cross-references IGC carriage list; LNG/LPG cargo is HNS-defined |
| 3 | maritime-law/standards/marpol-73-78.md → lng-projects/concepts/lng-process-safety.md | lng-projects/concepts/lng-process-safety.md → maritime-law/standards/marpol-73-78.md | MARPOL Annex VI air-emissions binds LNG fuel/BOG combustion |
| 4 | maritime-law/standards/solas-1974.md → engineering-standards/standards/asme-bpvc-viii-1.md | engineering-standards/standards/asme-bpvc-viii-1.md → maritime-law/standards/solas-1974.md | SOLAS Ch. II-1 boiler/pressure-vessel construction defers to ASME VIII for non-classed vessels |
| 5 | lng-projects/standards/igc-code.md → engineering-standards/concepts/cathodic-protection.md | engineering-standards/concepts/cathodic-protection.md → lng-projects/standards/igc-code.md | IGC Ch. 4 cargo-tank materials reference DNV-RP-B401 CP for cryogenic-service hulls |
| 6 | lng-projects/concepts/lng-process-safety.md → engineering-standards/concepts/brittle-fracture.md | engineering-standards/concepts/brittle-fracture.md → lng-projects/concepts/lng-process-safety.md | LNG cryogenic-service brittle-ductile transition is the canonical brittle-fracture LNG case (Cleveland 1944) |
| 7 | maritime-law/concepts/environmental-liability.md → engineering-standards/concepts/atmospheric-corrosion.md | engineering-standards/concepts/atmospheric-corrosion.md → maritime-law/concepts/environmental-liability.md | weakest of the 10; defer to iter-30 |
| 8 | maritime-law/standards/opa-90.md → lng-projects/standards/phmsa-49-cfr-193.md | lng-projects/standards/phmsa-49-cfr-193.md → maritime-law/standards/opa-90.md | OPA-90 land-side vs PHMSA Part 193 LNG-facility safety; both are US 49 CFR family |
| 9 | maritime-law/standards/mlc-2006.md → engineering-standards/concepts/welding-procedures-and-acceptance.md | engineering-standards/concepts/welding-procedures-and-acceptance.md → maritime-law/standards/mlc-2006.md | MLC crew-welfare doesn't materially bind welding QA; **DROP this edge — anti-bridge** |
| 10 | maritime-law/entities/mv-prestige-2002.md → engineering-standards/concepts/sulfidation-and-naphthenic-acid.md | engineering-standards/concepts/sulfidation-and-naphthenic-acid.md → maritime-law/entities/mv-prestige-2002.md | Prestige-2002 hull-failure root cause includes corrosion-under-insulation + sulfidation in heavy-fuel-oil cargo holds |

**Top-5 ranked bridges for iter-29 (drop edges 7 and 9, keep 1-6 + 8 + 10 = 8 bridges):**

1. SOLAS ↔ IGC (#1) — lowest friction, half-built
2. HNS ↔ IGC (#2) — HNS Art. 1 explicit cross-ref already in source text
3. SOLAS ↔ ASME BPVC (#4) — first eng-standards outbound edge ever
4. IGC ↔ DNV-RP-B401 / cathodic-protection (#5) — anchors lng-projects standards back-link backlog
5. MARPOL ↔ lng-process-safety (#3) — high-traffic concept, easy win

## iter-29 recommendation

### Top-3 ranked priorities

**Priority 1 — Cross-wiki bridge layer (8 bidirectional edges, ~16 file-edits)**
Rationale: this is the single lowest-friction, highest-leverage work in the repo. Bridge edges turn three siloed wikis into a connected substrate, which is the explicit value-prop of llm-wiki vs. domain-specific corpora. Six of the eight edges have content support already in the source text (e.g., SOLAS Ch. VII references IGC by name, HNS Art. 1 references IGC by name) — the work is grep-and-paste, not authoring. **Estimated agent-count: 1 (single edit-only agent, no parallelization needed; ~30 minutes wall-clock).**

**Priority 2 — lng-projects internal back-link backlog (3 standards × 5-8 concept edits each = ~20 edits)**
Rationale: api-std-625, csa-z276, en-1473 are zero-citation orphans. The W107 cross-link sweep advertised this work as done in iter-24 but file-grep proves it didn't land. This is a tooling/observability gap and should be closed before iter-29 ships any new content. **Estimated agent-count: 1 (same agent as priority 1; sequential).**

**Priority 3 — maritime-law parity reconciliation (5 page edits + 3 new concept pages)**
Rationale: P0 slug-mismatch fix (bunker→bunkers), 8 doctrine→treaty back-link edits, plus 3 new concept pages (unclos-1982, isps-code, stcw-convention) close the 9-stem gap on the standards-only side and the most defensible 3 of 9 concept-only stems. Defer hague-visby-rules, paris-mou, rotterdam-rules to iter-30; defer salvage and york-antwerp-rules entirely (back-links suffice). **Estimated agent-count: 2 (1 agent on slug+back-links, 1 agent on 3 new concept pages, parallelizable).**

### Total iter-29 budget

- ~36 file-edits + 3 new concept pages
- 2 agents in parallel for priority 3, 1 agent serial for priorities 1+2
- Wall-clock estimate: 60-90 minutes
- No new pivot decision; defer until W160-successor audit

## Anti-recommendations

**Do NOT pivot to a new wiki domain in iter-29.** Three reasons:

1. **Bridge-layer is at zero.** Adding a fourth wiki (naval-architecture / pipeline-engineering / petroleum-refining) before the first three are bidirectionally connected creates a 4-node graph with 1 edge — even worse degree distribution. Connect the existing three first.
2. **engineering-standards saturation is real but not the bottleneck.** 17 of 30 concepts have zero standards back-links — that is *internal* saturation, not topical exhaustion. The Priority 2 backlink work would lift internal connectivity by ~50% with zero new authoring; only after that does eng-standards genuinely look saturated.
3. **lng-projects + maritime-law are still mid-bootstrap.** lng-projects has 4 log entries total, maritime-law has 6. Compare engineering-standards at 16 log entries before W90 pivot. Neither wiki has earned a pause yet.

**Do NOT author concepts/charterparties.md as a standards companion.** Charterparties are commercial contract law (NYPE, Asbatime, Shelltime forms), not treaty / statute / regulation. The existing concept page is correct; forcing a standards/ companion would corrupt the standards/-tier semantics.

**Do NOT author concepts/{environmental-liability,salvage,general-average}.md as standards-only mirrors.** These three are *synthesis* concept pages that already aggregate multiple treaties. Their job is to back-link out, not to mirror a single standards-page. Adding salvage→salvage-convention-1989 as a back-link edit is correct; creating a parallel standards/ stub for "general-average" or "environmental-liability" would split the synthesis.

**Do NOT count the maritime-law entities/ subdirectory toward iteration cadence.** The 10 historical-case pages were a one-shot YAML seed migration on 2026-04-07; they inflate the page count but do not represent recurring research velocity. Future audits should report concepts+standards+sources as the cadence-relevant subset.

**Do NOT extend cross-link sweep to engineering-standards yet.** The 17-of-30 zero-back-link concepts in eng-standards are a real gap, but they do not require bridge-layer work — they require *internal* eng-standards back-links from existing standards pages. Treating eng-standards as a saturated-and-paused wiki per W90 is still correct; resuming eng-standards work should wait for W160-successor audit confirming maritime-law / lng-projects parity convergence.

**Do NOT promote any iter-29 work without first running the slug-consistency check.** The bunker(s)-convention-2001 mismatch was undetected by W111 and W134 manual audits — it surfaced only through `comm -23 concepts standards`. A pre-iter-29 sanity sweep should diff every concept stem against every standards stem in maritime-law and lng-projects to catch any other latent slug drift before it ossifies.
