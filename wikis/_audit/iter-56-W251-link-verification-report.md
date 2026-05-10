# iter-56 W251 — Cross-wiki link verification report

**Date:** 2026-05-10
**Scope:** All `[text](path.md)` links in `engineering-standards/`, `lng-projects/`, `maritime-law/` wikis (excludes `_audit/`)
**Tooling:** `/tmp/iter56-link-verify/verify.py` — read-only on content; this report is the only filesystem write.

## Summary

- Total markdown files scanned: **332** (engineering-standards: 215, lng-projects: 30, maritime-law: 80 — note: engineering-standards has more than the briefed 218 because raw/ tooling files were excluded)
- Total internal `.md` links discovered: **4413**
- Resolving inside in-scope wiki tree: **4157** (94.2%)
- Resolving to sibling-wiki content (`engineering/`, `asset-management/`, `marine-engineering/`, `naval-architecture/`, `acma-projects/`): **44** — links exist on disk but point outside the spinout's audit scope. Worth a separate decision-point for iter-57+ (rewrite to in-scope canonical, or accept cross-wiki bridge).
- Resolving to non-wiki repo files (`.claude/rules/calc-citation-contract.md` etc.): **142**
- Broken (Type A — target does not exist anywhere): **67**
- Broken (Type B — target exists at a different in-scope path): **3**
- Broken (Type C — canonical-paired-slug match): **0**
- **Total broken: 70 (1.59% of links)**

## Top-20 broken-target slugs (most-referenced missing slugs)

| Rank | Target slug | Refs | Type-A | Type-B | Type-C |
|------|-------------|------|--------|--------|--------|
| 1 | `calc-citation-contract` | 16 | 16 | 0 | 0 |
| 2 | `iso-9223` | 3 | 3 | 0 | 0 |
| 3 | `stcw-1978` | 3 | 3 | 0 | 0 |
| 4 | `itf-international-transport-workers-federation` | 3 | 3 | 0 | 0 |
| 5 | `astm-d1141` | 2 | 2 | 0 | 0 |
| 6 | `<slug>` | 2 | 2 | 0 | 0 |
| 7 | `master-authority` | 2 | 2 | 0 | 0 |
| 8 | `costa-concordia-2012` | 2 | 2 | 0 | 0 |
| 9 | `exxon-valdez-1989` | 2 | 2 | 0 | 0 |
| 10 | `prestige-2002` | 2 | 2 | 0 | 0 |
| 11 | `hebei-spirit-2007` | 2 | 2 | 0 | 0 |
| 12 | `paris-mou` | 2 | 0 | 2 | 0 |
| 13 | `colregs-1972` | 2 | 2 | 0 | 0 |
| 14 | `astm-g5` | 1 | 0 | 1 | 0 |
| 15 | `hoop-stress` | 1 | 1 | 0 | 0 |
| 16 | `creep-rupture` | 1 | 1 | 0 | 0 |
| 17 | `larson-miller-parameter` | 1 | 1 | 0 | 0 |
| 18 | `sulfidation-naphthenic-acid` | 1 | 1 | 0 | 0 |
| 19 | `api-rp-582` | 1 | 1 | 0 | 0 |
| 20 | `norsok-m-601` | 1 | 1 | 0 | 0 |

## Top-20 most-affected source pages

| Rank | Source page | Broken-link count |
|------|-------------|-------------------|
| 1 | `maritime-law/wiki/standards/solas-1974.md` | 16 |
| 2 | `maritime-law/wiki/standards/marpol-73-78.md` | 10 |
| 3 | `maritime-law/wiki/standards/mlc-2006.md` | 6 |
| 4 | `maritime-law/wiki/concepts/ism-code.md` | 4 |
| 5 | `engineering-standards/wiki/concepts/fitness-for-service.md` | 3 |
| 6 | `engineering-standards/wiki/standards/astm-a923.md` | 2 |
| 7 | `engineering-standards/wiki/standards/dnv-os-f201.md` | 2 |
| 8 | `engineering-standards/wiki/standards/astm-g50.md` | 2 |
| 9 | `engineering-standards/wiki/standards/astm-g78.md` | 2 |
| 10 | `lng-projects/wiki/standards/_template.md` | 2 |
| 11 | `maritime-law/wiki/standards/_template.md` | 2 |
| 12 | `engineering-standards/wiki/log.md` | 1 |
| 13 | `engineering-standards/wiki/standards/api-rp-571.md` | 1 |
| 14 | `engineering-standards/wiki/standards/dnv-rp-c210.md` | 1 |
| 15 | `engineering-standards/wiki/standards/asme-b31j.md` | 1 |
| 16 | `engineering-standards/wiki/standards/astm-g85.md` | 1 |
| 17 | `lng-projects/wiki/concepts/lng-project-shapes.md` | 1 |
| 18 | `lng-projects/wiki/standards/csa-z276.md` | 1 |
| 19 | `lng-projects/wiki/standards/en-1473.md` | 1 |
| 20 | `lng-projects/wiki/standards/ibc-code.md` | 1 |

## Type A — Missing-target detail (top 30 by reference count)

| Target slug | Refs | Sample source |
|-------------|------|---------------|
| `calc-citation-contract` | 16 | `lng-projects/wiki/standards/csa-z276.md` |
| `iso-9223` | 3 | `engineering-standards/wiki/standards/astm-g50.md` |
| `stcw-1978` | 3 | `maritime-law/wiki/concepts/ism-code.md` |
| `itf-international-transport-workers-federation` | 3 | `maritime-law/wiki/standards/mlc-2006.md` |
| `astm-d1141` | 2 | `engineering-standards/wiki/standards/astm-g78.md` |
| `<slug>` | 2 | `lng-projects/wiki/standards/_template.md` |
| `master-authority` | 2 | `maritime-law/wiki/concepts/ism-code.md` |
| `costa-concordia-2012` | 2 | `maritime-law/wiki/concepts/regional-mous-comparative.md` |
| `exxon-valdez-1989` | 2 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `prestige-2002` | 2 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `hebei-spirit-2007` | 2 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `colregs-1972` | 2 | `maritime-law/wiki/standards/solas-1974.md` |
| `hoop-stress` | 1 | `engineering-standards/wiki/concepts/fitness-for-service.md` |
| `creep-rupture` | 1 | `engineering-standards/wiki/concepts/fitness-for-service.md` |
| `larson-miller-parameter` | 1 | `engineering-standards/wiki/concepts/fitness-for-service.md` |
| `sulfidation-naphthenic-acid` | 1 | `engineering-standards/wiki/standards/api-rp-571.md` |
| `api-rp-582` | 1 | `engineering-standards/wiki/standards/astm-a923.md` |
| `norsok-m-601` | 1 | `engineering-standards/wiki/standards/astm-a923.md` |
| `dnv-os-f101` | 1 | `engineering-standards/wiki/standards/dnv-os-f201.md` |
| `api-rp-2rd` | 1 | `engineering-standards/wiki/standards/dnv-os-f201.md` |
| `dnv-os-c401` | 1 | `engineering-standards/wiki/standards/dnv-rp-c210.md` |
| `pipe-stress-analysis` | 1 | `engineering-standards/wiki/standards/asme-b31j.md` |
| `mooring-systems` | 1 | `lng-projects/wiki/concepts/lng-project-shapes.md` |
| `path` | 1 | `maritime-law/wiki/log.md` |
| `coastal-state-jurisdiction` | 1 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `iopc-funds` | 1 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `tacit-amendment-procedure` | 1 | `maritime-law/wiki/standards/marpol-73-78.md` |
| `classification-societies` | 1 | `maritime-law/wiki/standards/solas-1974.md` |
| `recognized-organizations-code` | 1 | `maritime-law/wiki/standards/solas-1974.md` |
| `load-lines-1966` | 1 | `maritime-law/wiki/standards/solas-1974.md` |

## Type B — Path-resolution errors (target exists at different in-scope path)

| Source | Bad link | Target exists at |
|--------|----------|------------------|
| `engineering-standards/wiki/log.md` | `../standards/astm-g5.md` | `engineering-standards/wiki/standards/astm-g5.md` |
| `maritime-law/wiki/standards/mlc-2006.md` | `../entities/paris-mou.md` | `maritime-law/wiki/concepts/paris-mou.md; maritime-law/wiki/standards/paris-mou.md` |
| `maritime-law/wiki/standards/mlc-2006.md` | `../entities/paris-mou.md` | `maritime-law/wiki/concepts/paris-mou.md; maritime-law/wiki/standards/paris-mou.md` |

## Type C — Canonical-paired-slug pairs (sibling-slug suggestions)

*None found this iteration. iter-46 W203 fix (`astm-g48` → `pitting-and-crevice-corrosion`) was the last canonical-pairing residue.*

## Notable patterns

### Pattern 1: `calc-citation-contract` (16 broken refs in lng-projects)
- All 16 broken refs use `../../../../.claude/rules/calc-citation-contract.md` (4 levels up).
- From `wikis/lng-projects/wiki/standards/`, that resolves to `llm-wiki/.claude/rules/...` — one level too shallow.
- Engineering-standards equivalents use `../../../../../.claude/...` (5 levels) which correctly lands in `workspace-hub/.claude/`.
- **Fix:** sed-style rewrite of `../../../../.claude/` → `../../../../../.claude/` in all lng-projects pages. Pure mechanical; no substrate-fill needed.
- This was a spinout-induced regression — these links worked pre-spinout when llm-wiki/ lived inside workspace-hub/.

### Pattern 2: maritime-law incident entities (10 refs)
- `costa-concordia-2012`, `exxon-valdez-1989`, `prestige-2002`, `hebei-spirit-2007` referenced from `marpol-73-78.md`, `solas-1974.md`, `regional-mous-comparative.md`.
- These belong in `maritime-law/wiki/entities/` per existing entity-page convention.
- **Fix:** substrate-fill — author 4 incident-history entity pages.

### Pattern 3: maritime-law standards substrate gaps (10 refs)
- `stcw-1978`, `colregs-1972`, `itf-international-transport-workers-federation` (×3 each), `iopc-funds`, `tacit-amendment-procedure`, `coastal-state-jurisdiction`, `recognized-organizations-code`, `load-lines-1966`.
- Cluster around SOLAS/MARPOL/MLC parent standards.
- **Fix:** substrate-fill — 8-10 standards stub pages in maritime-law.

### Pattern 4: engineering-standards concept gaps (3 refs)
- `hoop-stress`, `creep-rupture`, `larson-miller-parameter` from `fitness-for-service.md`.
- **Fix:** substrate-fill — 3 concept pages.

### Pattern 5: `_template.md` placeholder slugs (2 refs, false positive)
- `lng-projects/wiki/standards/_template.md` and `maritime-law/wiki/standards/_template.md` contain literal `<slug>` placeholders.
- **Fix:** exclude `_template.md` from link-verification scope in iter-57.

## Recommendation for iter-57 fix-batching

- **Total defect count: 70** — manageable as a single iteration if scoped tightly.
- **iter-57 (mechanical, low-risk, ~30 min):**
  - (a) sed-rewrite the 16 lng-projects `calc-citation-contract` links (`../../../../.claude/` → `../../../../../.claude/`).
  - (b) Fix 3 Type-B path errors (1 in `engineering-standards/wiki/log.md`, 2 in `mlc-2006.md`).
  - (c) Add `_template.md` exclude to scanner.
  - Resolves ~19/70 = 27% of defects with no substrate-authoring.
- **iter-58 (substrate-fill wave A — maritime-law, ~2 hrs):**
  - 4 incident entity pages (Pattern 2).
  - 8-10 maritime standards stubs (Pattern 3).
  - 3 concept pages (`master-authority`, `port-state-control` consolidations).
  - Resolves ~30 defects.
- **iter-59 (substrate-fill wave B — engineering-standards, ~1 hr):**
  - 3 concept pages (Pattern 4).
  - 5-8 standards stubs (`iso-9223`, `astm-d1141`, `api-rp-582`, `norsok-m-601`, `norsok-z-008`, `dnv-os-c401`, `dnv-os-f101`, `api-rp-2rd`).
  - Resolves remaining ~20 defects.
- **iter-60+ (long-tail, optional):** singletons not in above patterns (~5-7 defects) — consider link-removal vs stub-creation per case.

## Sibling-wiki cross-link decision-point (iter-57 P1)

- **44 links** point to content in `engineering/`, `asset-management/`, etc. — outside the spinout's 3 in-scope wikis.
- These are not "broken" — files exist. But strategically, are these links acceptable cross-wiki bridges, or should they be rewritten to in-scope canonical paths?
- Top patterns: `engineering/wiki/standards/dnv-rp-c203.md`, `asset-management/wiki/standards/api-rp-581.md`, `asset-management/wiki/standards/dnv-rp-g101.md` — all have engineering-standards canonical equivalents.
- **Recommend:** iter-57 P1 user-decision: confirm rewrite-to-canonical posture, then mechanical sed pass.

## Notes on classification

- `Total broken` excludes 4,343 links that resolve correctly (in-scope, sibling-wiki, or out-of-wiki-disk). That's a **98.4% link-integrity rate** across the 3 in-scope wikis — strong baseline given 7+ iterations of cross-link enrichment.
- Type B count is small (3) because most legacy-prefix links (`engineering/...`, `asset-management/...`) actually resolve to existing files in sibling wikis — they're classified as sibling-wiki-OK, not Type B.
- Type C is empty — canonical-pairing residue from iter-46 has not regressed.

---
*Generated by `/tmp/iter56-link-verify/verify.py` 2026-05-10*
