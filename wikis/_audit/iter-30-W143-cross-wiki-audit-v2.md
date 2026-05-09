---
audit_id: W143
iter_under_review: 29
iter_planned: 31
audit_date: 2026-05-09
auditor: cross-wiki-audit-v2
scope: [engineering-standards, lng-projects, maritime-law]
prior_audits: [W90 (iter-22 → eng-standards saturation), W111 (iter-24 → maritime-law pickup), W134 (iter-28 → bridges/back-links/parity)]
---

# W143 cross-wiki audit v2 — iter-31 priority recommendation

## Executive summary

W134's three priorities all landed in iter-29 commit `243c4d3b` (7 cross-wiki bridges + 14 lng back-link return-edges + bunker(s) slug rename + UNCLOS-1982 concept page), and iter-30 is mid-flight on lng concept gap-fill (W144/W145) plus maritime standards (W146/W147) — so the bridge-layer-first thesis converged. The next bottleneck has shifted: **cross-wiki edges are still ≤4 per ordered-pair on the two LNG-touching axes and exactly 0 on both engineering-standards axes**, so iter-31 should focus on (a) seeding the first eng-standards outbound edges via the high-citation-density entities, (b) closing the 4 remaining maritime-law concept-only stems that have a treaty-grade companion, and (c) drafting the missing IMO/UN/ILO concept-pages whose standards already shipped iter-26/27. Defer any new-wiki pivot until eng-standards has at least 5 outbound bridges and maritime-law concept↔standards parity drops below 4 mismatches.

## State change since W134

- **engineering-standards**: 167 → 170 pages (+3 concepts authored 2026-05-08/09 outside the W134 audit window). Still 0 outbound cross-wiki edges. Calc-citation frontmatter coverage now 118/118 (was reported but not measured in W134) — `code_id` + `publisher` + `revision` all present.
- **lng-projects**: 21 → 26 pages (+1 standard `ibc-code` iter-28, +nothing-else; cross-link returns landed). Outbound edges 1 → 7 (W139+W140 bridges + IBC). 9 standards (sans template) all have full `code_id`/`publisher`/`revision`.
- **maritime-law**: 46 → 54 pages (+1 standard `tokyo-mou`, +2 concepts `stcw-convention`/`isps-code` iter-28; +1 concept `unclos-1982` iter-29; bunker→bunkers slug fix). 18 standards now exist; concept↔standards mismatch shrank from 9+9 → 4+4. 18/18 standards have `code_id` + `publisher` but use treaty-flavored `consolidated_edition`/`effective_date` in lieu of `revision`.
- **Cross-wiki bridges**: from 1 (lng-regulatory-framework→solas, asymmetric) to 7 bidirectional pairs landing as 11 link-instances total across 4 lng files + 4 maritime files.

## Wiki-by-wiki state

| Wiki | W134 pages | W143 pages | Δ | Concepts | Standards | Sources | Entities | Outbound cross-wiki refs (files) |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering-standards | 167 | 170 | +3 | 30 | 118 | 19 | — | 0 |
| lng-projects | 21 | 26 | +5 | 8 | 10 (+template) | 5 | — | 4 |
| maritime-law | 46 | 54 | +8 | 20 | 19 (+template) | 2 | 10 | 4 |
| **Total** | **234** | **250** | **+16** | **58** | **148** | **26** | **10** | **8** |

**Observations:**

- Maritime-law is still the hottest wiki — 4 of the last 5 commits touched it. Concept↔standards mismatch dropped from 18 stems (9+9) to 8 (4+4): standards-side missing `charterparties`, `environmental-liability`, `flag-state-jurisdiction`, `general-average`, `limitation-of-liability`, `port-state-control`, `salvage`; concept-side missing `hague-visby-rules`, `paris-mou`, `rotterdam-rules`, `salvage-convention-1989`, `tokyo-mou`, `york-antwerp-rules`. The synthesis-page DEFER list from W134 (`charterparties`, `environmental-liability`, `general-average`, `limitation-of-liability`, `salvage`, `port-state-control`, `flag-state-jurisdiction`) accounts for 7 of those 8, so the genuinely-actionable concept-only-side residue is 0; the genuinely-actionable standards-only-side residue (concepts to author) is 4: `hague-visby-rules`, `paris-mou`, `rotterdam-rules`, `salvage-convention-1989` (since iter-30 W144/W145 are scoped to lng).
- engineering-standards is still saturated by absolute size but **0 outbound bridges** is now the biggest defect, not internal back-link gaps. The W134 17-of-30 zero-back-link concept count was internal; bridge-edge work is structurally distinct.
- lng-projects template still references `asme-b31-8` cross-wiki bridge (eng-standards/standards/) but that link is in `_template.md` placeholder text — it represents zero real edges to eng-standards, just a model for future authoring.
- Sources gap on maritime-law worsened on a per-page basis: 2 sources / 54 pages = 3.7% (was 4.3%). Treaty-text-as-source is structural.

## Cross-wiki edge density

Bridge counts measured by file-instances grepping `../../../<other-wiki>/wiki/` markdown links, excluding `_template.md`.

| Source wiki | Target wiki | File-pairs (links) | Bidirectional pairs | Notes |
|---|---|---:|---:|---|
| engineering-standards | lng-projects | 0 | 0 | none |
| engineering-standards | maritime-law | 0 | 0 | none |
| lng-projects | engineering-standards | 0 | 0 | template-placeholder only |
| lng-projects | maritime-law | 6 link-instances across 3 files | 3 | igc↔solas, igc↔marpol, igc↔hns; ibc↔hns, ibc↔marpol, ibc↔solas; lng-regulatory-framework→solas |
| maritime-law | engineering-standards | 0 | 0 | none |
| maritime-law | lng-projects | 7 link-instances across 3 files | 3 | mirror of above (solas, marpol, hns standards-pages outbound to igc/ibc/lng-regulatory-framework) |
| **Totals** | | **13** | **6 (+1 asym)** | only 1 of 3 wiki pairs is connected |

The lng↔maritime axis has 6 bidirectional pairs; the eng-standards↔lng and eng-standards↔maritime axes have **zero**. Engineering-standards is structurally a sink with 170 pages and 0 outbound — exactly the configuration W134 warned would occur if iter-29 didn't break ground on eng-standards bridges. iter-29 took the W134 anti-recommendation literally (drop edge #4 SOLAS↔ASME BPVC and #9 MLC↔welding) and shipped 0 eng-standards bridges; iter-31 should reverse that.

## iter-31 recommendation

**Priority 1 — First engineering-standards outbound bridges (3 high-confidence pairs, ~6 file-edits)**

The audit-flagged "drop these edges" from W134 (#4 SOLAS↔ASME BPVC, #5 IGC↔DNV-RP-B401/cathodic-protection, #6 LNG-process-safety↔brittle-fracture) were dropped on the wrong grounds — W134 conservatism rather than topical weakness. Three high-confidence eng-standards bridges, in priority order:

1. `engineering-standards/concepts/brittle-fracture.md` ↔ `lng-projects/concepts/lng-process-safety.md` — Cleveland 1944 LNG cryogenic brittle-fracture is the canonical case study; 9% Ni and Invar steel selection is brittle-fracture-driven; both pages stand to gain.
2. `engineering-standards/concepts/cathodic-protection.md` ↔ `lng-projects/standards/igc-code.md` — IGC Ch. 4 cargo-tank materials reference DNV-RP-B401 CP for cryogenic-service hulls; eng-standards/dnv-rp-b401.md is already authored.
3. `engineering-standards/standards/asme-bpvc-viii-1.md` ↔ `maritime-law/standards/solas-1974.md` — SOLAS Ch. II-1 boiler/pressure-vessel construction defers to ASME VIII for non-classed vessels; bridges the highest-density eng-standards page (api-rp-571 spine) to the highest-density maritime-law page.

These three plus their return edges = 6 file-edits and unlock the 3-wiki connected-graph topology (currently lng↔maritime is the only connected pair). **Estimated agent count: 1 (single edit-only agent, ~30 min wall-clock).**

**Priority 2 — Maritime-law concept-page authoring for standards-only stems (4 new concept pages)**

Standards-only stems with no concept companion: `hague-visby-rules`, `paris-mou`, `rotterdam-rules`, `salvage-convention-1989`. Of these, `salvage-convention-1989` was W134-flagged "no new concept needed; back-link from concepts/salvage.md sufficient" — confirmed: defer `salvage-convention-1989` and `york-antwerp-rules` (both subsumed by synthesis-pages). That leaves **3 actionable concept pages**: `hague-visby-rules` (carriage-of-goods regime, distinct from Rotterdam), `paris-mou` (PSC enforcement regime, distinct from `port-state-control` synthesis), `rotterdam-rules` (multimodal carriage; not yet in force; topically distinct from Hague-Visby). Each is ~150-line authoring + frontmatter + concept↔standards return-link sweep. **Estimated agent count: 1 (single concept-authoring agent, ~45 min wall-clock).**

**Priority 3 — engineering-standards saturation revisit: standards/-tier promotion of high-citation-density entities is NOT yet warranted**

After this audit's measurement, the top-15 most-cited eng-standards stems are: `api-rp-571` (49), `api-std-579` (45), `bs-7910-flaw-assessment` (29), `iso-15156` (25), `astm-e1820` (23), `api-510` (21), `api-570` (20), `api-std-1104` (17), `api-rp-581` (16), `api-653` (15), `ampp-mr-0175-pt2` (15), `astm-g48` (14), `dnv-rp-f112` (11), `dnv-rp-b401` (11), `ampp-tm-0177` (11). **All 15 already have first-class standards/ pages with full `code_id`/`publisher`/`revision` frontmatter** — there is no promotion gap. Calc-citation-contract readiness for eng-standards is at ceiling. Iter-31 should NOT spend cycles bootstrapping a new tier or sub-classifying the existing standards/. **Estimated agent count: 0.**

### Total iter-31 budget

- ~6 cross-wiki bridge edits + 3 new maritime-law concept pages + concept↔standards return-link sweep
- 1 sequential agent for priority 1, 1 sequential agent for priority 2 (parallelizable since file sets disjoint)
- Wall-clock estimate: 60-90 minutes
- No new-wiki pivot

## Anti-recommendations

**Do NOT pivot to a new wiki domain in iter-31.** Engineering-standards still has 0 outbound bridges. Adding a 4th wiki before fixing this leaves the substrate in a degraded 4-node graph with one pair connected, one pair half-connected, two pairs disconnected. Same W134 rationale, stronger this iteration because the eng-standards isolation is now the dominant defect.

**Do NOT author standards-companion pages for the 7 maritime-law synthesis concepts** (`charterparties`, `environmental-liability`, `flag-state-jurisdiction`, `general-average`, `limitation-of-liability`, `port-state-control`, `salvage`). W134 ruled these out; iter-29 confirmed via 8 doctrine→treaty back-link edits. Reopening this would split synthesis into duplicates.

**Do NOT promote any eng-standards entity to a new sub-tier.** All 15 highest-cited eng-standards already exist as first-class standards pages with full calc-citation frontmatter. There is no "high-citation-density entity not yet first-class" gap. The W90 saturation diagnosis remains correct: the wiki is topically complete for petroleum-/offshore-asset integrity, and incremental authoring should follow user demand, not iteration cadence.

**Do NOT add `revision:` field retroactively to maritime-law standards pages**. The wiki's CLAUDE.md schema explicitly substitutes `consolidated_edition` + `effective_date` for `revision` because treaties don't have edition revisions in the standards-publisher sense. Forcing `revision:` would corrupt the schema; calc-citation-contract should be amended to recognize either pattern instead.

**Do NOT revisit the bunker(s) slug pattern in iter-31.** iter-29 W141 closed it; ten incoming-link sites were updated; no further drift detected by spot-grep. Re-opening would risk a new mismatch.

**Do NOT count iter-30 W144/W145/W146/W147 as iter-31 prerequisites.** Those 4 work items are scoped to within-wiki concept/standards growth and do not change the cross-wiki graph topology that this audit measures. iter-31 priorities 1+2 are independent and can launch in parallel with iter-30 in-flight work.

## Calc-citation-contract readiness

| Wiki | Standards (sans template) | code_id present | publisher present | revision/edition present | Notes |
|---|---:|---:|---:|---:|---|
| engineering-standards | 118 | 118/118 | 118/118 | 118/118 | At ceiling. `calc-citation-contract.md` resolver can directly read any of the 118. |
| lng-projects | 9 | 9/9 | 9/9 | 9/9 | At ceiling for the 9-page corpus. |
| maritime-law | 18 | 18/18 | 18/18 | 0/18 (uses `consolidated_edition` + `effective_date` instead) | Schema mismatch with calc-citation-contract resolver. Either contract amends to accept treaty-flavored fields, or maritime-law standards are explicitly scoped out of calc-side citation (likely correct for treaty pages — they aren't calc inputs). Document the scope in the contract; don't backfill `revision:` here. |

The corollary: the calc-citation-contract is **production-ready for the 127 engineering-standards + lng-projects standards pages today**. Maritime-law treaties are not calc-citation targets in practice (no calc module consumes a SOLAS clause as a numeric constant); the schema delta should be documented as intentional, not as a defect.
