---
title: "Issue #28 plan — Marine engineering canonical index chunking"
issue: 28
status: plan-approved
created: 2026-05-11
last_updated: 2026-05-11
public_safety: repo-local generated navigation only; no raw archive ingestion
---

# Issue #28 Plan — Marine Engineering Canonical Index Chunking

## Gate status

- GitHub issue: [vamseeachanta/llm-wiki#28](https://github.com/vamseeachanta/llm-wiki/issues/28)
- Current local plan state: `status:plan-approved`
- Implementation status: **approved for future implementation; not implemented in this exit-closeout pass**
- Scope class: repo-local markdown/script/test work; no raw private-archive ingestion or private content promotion.

## Resource intelligence

Fresh local inspection on 2026-05-11 found:

- Actual repo path: `wikis/marine-engineering/wiki/index.md`.
- Issue body path prefix `knowledge/wikis/...` is stale for this spinout repo; implementation must use `wikis/...`.
- Current canonical index size: 21,654 lines.
- Current marine source-page count by filesystem: 19,171 files under `wikis/marine-engineering/wiki/sources/`.
- Existing generator/scoring surface: `scripts/llm_wiki_strengthening_scorecard.py` reads `WIKI_ROOT = Path("wikis")` and already knows portal sections.
- Codex scouting found a likely parser risk: the current `## Sources` section begins near the top of the file, but source rows may not be cleanly isolated in one simple contiguous table. Implementation tests must prove row extraction against the real generated shape before rewriting `index.md`.
- Codex scouting also found that generated chunk files would currently be counted by `scripts/llm_wiki_strengthening_scorecard.py::content_pages()` unless explicitly excluded or classified.
- Existing validation/test surface:
  - `tests/test_completion_artifacts.py`
  - `tests/test_governance_artifacts.py`
  - `tests/test_scan_source_families_safe.py`
  - `scripts/validate_completion_artifacts.py`
  - `scripts/validate_governance_artifacts.py`

## Public-safety boundary

Allowed:

- Generate bounded index/chunk pages from already committed wiki metadata.
- Preserve existing stable page links.
- Add aggregate navigation/counts and generated-output policy docs.
- Reference tier-1 public repository URLs and public-safe result/report artifacts.

Forbidden:

- Reading or committing new raw private-archive source files.
- Copying vendor standards text/tables/figures, client material, raw CAD/model data, admin/personal data, secrets, or path-rich private manifests.
- Replacing the canonical index with hand-curated excerpts that hide committed pages.

## Implementation plan after approval

1. **Write failing tests first.**
   - Add unit tests for a new chunking helper module/script.
   - Use temporary fixture wiki indexes to avoid loading the full 21K-line production file in unit tests.
   - Assert chunk size, range naming, next/previous links, canonical backlink, and deterministic rerun behavior.

2. **Add a deterministic chunking script.**
   - Proposed path: `scripts/chunk_wiki_index.py`.
   - Inputs: domain name, source index path, output directory, section name, max rows per chunk.
   - Default target: domain `marine-engineering`, section `Sources`, output under `wikis/marine-engineering/wiki/index-chunks/` or another explicit generated-navigation directory chosen during implementation.
   - Output: bounded markdown chunks with frontmatter, row-range metadata, canonical index backlink, next/previous links, and stable relative links.

3. **Keep `index.md` canonical.**
   - Preserve the top-level canonical `index.md` path.
   - Replace or augment the oversized source table with a compact generated chunk table only if tests prove all source links remain reachable.
   - Keep curated sections (`Entities`, `Concepts`, `Comparisons`, `Standards`) visible in the top-level index.

4. **Document reusable policy.**
   - Add a short policy doc, proposed path: `docs/generated-index-chunking-policy.md`.
   - Define chunk thresholds, naming convention, generated-file warning, regeneration command, and link-stability rules.

5. **Regenerate scorecard/control-plane reports only if affected.**
   - If scorecard indexing logic must learn chunk pages, update `scripts/llm_wiki_strengthening_scorecard.py` and tests before regenerating reports.

## TDD checklist

Minimum tests before implementation:

- `test_chunk_wiki_index_preserves_canonical_entrypoint`
- `test_chunk_wiki_index_creates_bounded_source_chunks`
- `test_chunk_wiki_index_adds_prev_next_and_canonical_backlinks`
- `test_chunk_wiki_index_is_deterministic_on_second_run`
- `test_chunk_wiki_index_rejects_unknown_or_missing_section`
- If scorecard logic changes: `test_scorecard_counts_pages_without_treating_generated_chunks_as curated content`

## Acceptance verification commands

Run from repo root after approval/implementation:

```bash
uv run python scripts/chunk_wiki_index.py --domain marine-engineering --section Sources --max-rows 500
uv run python scripts/llm_wiki_strengthening_scorecard.py --date 2026-05-11
uv run python scripts/validate_governance_artifacts.py
uv run python scripts/validate_completion_artifacts.py
PYTHONDONTWRITEBYTECODE=1 uv run pytest -q -p no:cacheprovider
```

Additional manual checks:

```bash
wc -l wikis/marine-engineering/wiki/index.md
find wikis/marine-engineering/wiki -path '*index*' -name '*.md' | sort | head -50
```

## Done criteria

- Top-level `wikis/marine-engineering/wiki/index.md` remains the canonical entry point.
- Exhaustive marine source navigation no longer requires reading one 21K-line file.
- Generated chunk pages have stable range links, next/previous links, and backlinks to the top-level index.
- Chunking can be regenerated deterministically.
- Tests and validators pass.
- GitHub issue #28 receives a completion comment with touched paths, commands, and public-safety statement before closure.
