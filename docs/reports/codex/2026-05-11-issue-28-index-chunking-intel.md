---
title: "Issue #28 Index Chunking Implementation Surface"
created: 2026-05-11
issue: 28
scope: public-safe resource intelligence only
---

# Issue #28 Index Chunking Implementation Surface

## 1. Existing Assets

- `wikis/marine-engineering/wiki/index.md` — actual canonical marine index path. Confirmed at 21,654 lines, with frontmatter `page_count: 19210` and `source_count: 19167`.
- `wikis/marine-engineering/wiki/sources/` — actual source-page directory. Current filesystem count: 19,171 `*.md` files.
- `wikis/marine-engineering/wiki/portal.md` — generated faceted entry point; complements, but does not replace, `index.md`.
- `wikis/marine-engineering/wiki/code-results-links.md` — existing public-safe marine implementation/result link page referenced from the canonical index tail.
- `wikis/marine-engineering/CLAUDE.md` — domain schema says `wiki/index.md` is the content catalog and lists expected sections: `Entities`, `Concepts`, `Sources`, etc.
- `README.md` — repo layout and consumption contract use `wikis/<domain>/...`; states source pipeline remains upstream and this repo stores public artifacts.
- `docs/plans/2026-05-11-issue-28-marine-index-chunking.md` — existing plan-review artifact for this issue; already calls out the stale `knowledge/wikis/...` prefix.
- `scripts/llm_wiki_strengthening_scorecard.py` — existing deterministic metadata/portal generator. Important surfaces: `WIKI_ROOT = Path("wikis")`, `PORTAL_SECTIONS`, `count_indexed_paths()`, `content_pages()`, `make_portal()`, and `ensure_index_portal_link()`.
- Existing validators/tests: `scripts/validate_completion_artifacts.py`, `scripts/validate_governance_artifacts.py`, `tests/test_completion_artifacts.py`, `tests/test_governance_artifacts.py`, `tests/test_scan_source_families_safe.py`.

## 2. Implementation Surface

- Add `scripts/chunk_wiki_index.py` or equivalent reusable generator to parse a domain `wiki/index.md`, split oversized table sections, and write deterministic chunk pages.
- Add tests, likely `tests/test_chunk_wiki_index.py`, using temporary fixture indexes rather than the 21K-line production file.
- Change `wikis/marine-engineering/wiki/index.md` only through the generator: keep it as the canonical entry point, keep curated sections visible, and replace/augment the oversized `Sources` table with a bounded chunk-jump table.
- Add generated chunk pages under a stable repo-local directory such as `wikis/marine-engineering/wiki/index-chunks/` unless implementation chooses a more explicit generated-navigation path.
- Add `docs/generated-index-chunking-policy.md` or similar policy doc to define thresholds, naming, regeneration command, generated-file warnings, and link-stability rules.
- Potentially adjust `scripts/llm_wiki_strengthening_scorecard.py` so generated chunk pages do not inflate curated/source counts or create false missing-index/orphan signals.
- Potentially extend completion/governance validators if the new policy/chunk files become acceptance artifacts.

## 3. TDD Plan

- Test canonical entry point preservation: `wikis/<domain>/wiki/index.md` remains present and links to chunks without moving current source pages.
- Test bounded chunk creation: fixture `Sources` rows split into deterministic files with max-row limits and no row loss.
- Test stable navigation: each chunk has canonical backlink plus previous/next links; top index has a jump table covering all chunks.
- Test link stability: existing `sources/*.md` relative links remain unchanged from source rows to chunks/top index.
- Test deterministic rerun: running the generator twice produces identical bytes and deletes or refreshes stale generated chunks predictably.
- Test bad inputs: missing index, missing section, malformed table, unknown domain, and unsafe output path fail clearly.
- If scorecard changes, test generated chunk pages are excluded from content-page counts or classified so they do not distort domain metrics.

## 4. Risks / Unknowns

- Path mismatch: issue body says `knowledge/wikis/marine-engineering/wiki/index.md`; actual repo path is `wikis/marine-engineering/wiki/index.md`.
- Count mismatch: index frontmatter says `source_count: 19167`; filesystem currently has 19,171 source markdown files. The implementation should decide whether generated chunking preserves frontmatter counts or recomputes them.
- Current `## Sources` section starts near line 69, while additional source rows continue after `## Topics Covered`; parser logic must not assume all source rows are in one clean contiguous table unless tests prove it.
- Link stability risk is high because existing consumers may link directly to `index.md` or expect source links relative to it.
- Generated-output volume could add dozens of new chunk files; choose a clear naming convention and avoid churn from sorting changes.
- `scripts/llm_wiki_strengthening_scorecard.py::content_pages()` excludes only `index.md`, `log.md`, `overview.md`, and `portal.md`; generated chunk files would currently be counted unless explicitly handled.
- Existing repo memory path from the bootstrap instruction was not present in this local checkout, so this report relies on repo-local public files and direct inspection.

## 5. Public-Safety Notes

- Scope should remain repo-local generated navigation over already committed markdown metadata.
- Do not read, copy, summarize, or promote raw private archives, vendor standards clauses/tables/figures, client data, secrets, or private path manifests.
- Chunk pages should preserve public-safe titles, summaries, dates, and relative links already present in committed wiki index rows; do not enrich from raw source files.
- Keep generated-file headers explicit so future maintainers regenerate rather than hand-editing large derived navigation files.

## 6. Acceptance-Criteria Verification Commands

Run from repo root after implementation:

```bash
uv run python scripts/chunk_wiki_index.py --domain marine-engineering --section Sources --max-rows 500
uv run python scripts/llm_wiki_strengthening_scorecard.py --date 2026-05-11
uv run python scripts/validate_governance_artifacts.py
uv run python scripts/validate_completion_artifacts.py
PYTHONDONTWRITEBYTECODE=1 uv run pytest -q -p no:cacheprovider
wc -l wikis/marine-engineering/wiki/index.md
find wikis/marine-engineering/wiki -path '*index*' -name '*.md' | sort | head -50
```

Useful pre/post checks:

```bash
find wikis/marine-engineering/wiki/sources -maxdepth 1 -type f -name '*.md' | wc -l
rg -n '^## |page_count|source_count|portal.md|index-chunks|Sources' wikis/marine-engineering/wiki/index.md
git diff --stat -- wikis/marine-engineering/wiki docs scripts tests
```
