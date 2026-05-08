# Codex /goal Prompt — llm-wiki Completion

Paste the following into Codex CLI using `/goal` from inside the repo clone at:

```bash
cd <llm-wiki-repo>
codex
```

Then submit:

```text
/goal Complete the llm-wiki public repo to the best practical state from the approved GitHub issue queue, while preserving raw/private/vendor-source boundaries and following issue lifecycle discipline.

You are operating in the public repository:

- Local repo: <llm-wiki-repo>
- GitHub repo: vamseeachanta/llm-wiki
- Branch: main
- Current known pushed HEAD: 19178ef6cbc55095d1ae1466b67e5b17b60f61a4
- Latest landed commit: Add llm-wiki strengthening scorecard and portal

Critical context:
A Hermes session already completed and pushed a safe metadata-only strengthening pass:
- Added docs/reports/llm-wiki-strengthening-scorecard.md
- Added docs/reports/llm-wiki-strengthening-scorecard.json
- Added scripts/llm_wiki_strengthening_scorecard.py
- Added wikis/marine-engineering/wiki/portal.md
- Updated wikis/marine-engineering/wiki/index.md with a portal link
- Validation passed:
  - uv run scripts/llm_wiki_strengthening_scorecard.py --date 2026-05-06 --write
  - uv run python -m py_compile scripts/llm_wiki_strengthening_scorecard.py
  - uv run scripts/llm_wiki_strengthening_scorecard.py --help
  - uv run python -m json.tool docs/reports/llm-wiki-strengthening-scorecard.json
  - generated Markdown local-link checks passed
  - targeted raw/private-path/obvious-secret scan over changed files passed
- Closeout comments were posted to:
  - #37: https://github.com/vamseeachanta/llm-wiki/issues/37#issuecomment-4384887219
  - #22: https://github.com/vamseeachanta/llm-wiki/issues/22#issuecomment-4384887280

The user has approved the following issues for execution, and live GitHub verification showed each has status:plan-approved:
- #14 https://github.com/vamseeachanta/llm-wiki/issues/14
- #15 https://github.com/vamseeachanta/llm-wiki/issues/15
- #16 https://github.com/vamseeachanta/llm-wiki/issues/16
- #17 https://github.com/vamseeachanta/llm-wiki/issues/17
- #18 https://github.com/vamseeachanta/llm-wiki/issues/18
- #19 https://github.com/vamseeachanta/llm-wiki/issues/19

Other relevant approved/working issues:
- #22 feat(knowledge): generate faceted portal pages for large LLM-wiki domains
- #25 feat(knowledge): execute Batch Pack 1 to promote API/standards-portal metadata into thin wiki domains
- #26 feat(knowledge): execute Batch Pack 4 for non-ACMA standards summary promotion
- #37 scorecard/portal work is already landed and should be treated as completed unless live GitHub says otherwise.

Hard boundaries:
1. This is a public repository. Do NOT copy raw PDFs, private archives, private mount paths, vendor PDFs, vendor-derived text, credentials, tokens, API keys, or connection strings into git.
2. Public artifacts may summarize only committed public Markdown/wiki metadata already in this repo, or safely authored public synthesis.
3. Private/raw archives remain outside git. If an issue depends on raw/private source access or unresolved data/source decisions, mark it blocked with evidence instead of guessing.
4. llm-wiki is the public content/artifact repo. workspace-hub remains the control-plane/pipeline repo. Do not add private pipeline orchestration here unless the issue explicitly calls for public repo-local tooling.
5. Respect licensing: wikis/**/*.md are CC-BY-4.0; code/tooling is MIT.
6. Do not claim a full scanner/security-suite pass unless you actually run one. Targeted scans are acceptable but label them as targeted.
7. Use uv for Python commands. Do not use bare python3.
8. Do not close issues before push, branch/worktree disposition, cleanup, and clean-state proof are complete.

Primary goal:
Maximize the practical completeness and usability of the llm-wiki repo from the approved issue queue, safely and transactionally. Prefer high-leverage, metadata-only or public-synthesis improvements that make the repo more navigable, governed, and complete without raw-data leakage.

Recommended execution order:
1. First verify live state:
   - git status -sb
   - git fetch origin main
   - git rev-parse HEAD origin/main
   - gh issue view 14 15 16 17 18 19 22 25 26 37 --repo vamseeachanta/llm-wiki --json number,title,state,labels,url
   - Inspect README.md and the latest scorecard report.
2. Continue #22 if still open/approved: use scripts/llm_wiki_strengthening_scorecard.py to generate safe faceted portal pages for additional large or graph-weak domains. Keep generator metadata-only. Do not rewrite raw content.
3. Execute #17 and/or #18 if their issue bodies show bounded public-wiki backfill/overview-refresh scope that can be satisfied from already committed repo content. For marine-engineering, prefer:
   - refresh stale overview counts using current committed wiki files,
   - add safe navigation links,
   - promote existing public synthesized pages,
   - avoid copying vendor text or private/raw content.
4. Execute #16 if bounded: classification-society entity pages for DNV/ABS/LR/BV should be public synthesis only, based on existing committed wiki metadata/pages and safe general descriptions. Avoid standards text reproduction.
5. Execute #15 before broad routing changes: resolve standards-routing/meta classification decisions in public metadata/docs only. If it requires policy decisions beyond the issue, post a blocker or create a follow-up issue.
6. Treat #14 and #19 with extra caution. They involve curated corpus/raw-source-family planning. If execution requires private/raw data access or copying from non-public sources, do NOT implement content directly. Instead produce a public-safe plan/dossier or blocker comment with exact boundaries and next required approval/data decision.
7. Execute #25/#26 only if their scope is clear, public-safe, and not dependent on private source copying.

Required issue workflow:
For each issue you execute:
1. Confirm the issue is open and labeled status:plan-approved.
2. Read the issue body and comments.
3. Decide whether it is:
   - already satisfied,
   - executable now,
   - blocked by raw/private/source decision,
   - or should be split into a future issue.
4. Post a GitHub execution-start comment before changes, including:
   - issue scope,
   - execution mode: central,
   - intended files/paths,
   - validation plan,
   - raw/private/vendor boundary statement.
5. Use TDD where code/script behavior changes. For docs-only/generated-artifact changes, use deterministic inspection and link checks as the proof path.
6. Keep each commit tightly scoped to one issue or a tightly related approved pair.
7. Before commit:
   - run targeted validators,
   - run relevant generator/help/compile/json checks if scripts or generated JSON changed,
   - run Markdown local-link checks for generated or edited markdown,
   - run targeted grep for private mount paths and obvious secret patterns over changed files,
   - run git diff --check,
   - inspect git diff --stat and changed paths.
8. Commit with issue-linked message.
9. Push immediately to origin/main unless repo state requires a branch/PR.
10. Verify:
   - git status -sb is clean,
   - local HEAD equals origin/main,
   - pushed commit hash is recorded.
11. Post a final closeout comment before closing, with:
   - Result,
   - Change summary,
   - Acceptance criteria -> proof mapping,
   - Validation commands/results,
   - Adversarial/self-review result,
   - Residual risk,
   - Git evidence,
   - Future issues or none.
12. Close only if landed/already-satisfied/invalid with evidence. Otherwise leave open with blocker note.

Suggested validators:
- git status -sb
- uv run scripts/llm_wiki_strengthening_scorecard.py --date 2026-05-06 --write
- uv run python -m py_compile scripts/llm_wiki_strengthening_scorecard.py
- uv run scripts/llm_wiki_strengthening_scorecard.py --help
- uv run python -m json.tool docs/reports/llm-wiki-strengthening-scorecard.json
- custom local Markdown link checker for generated/edited markdown
- git diff --check
- targeted scan over changed files for:
  - <workspace-root>
  - <private-vendor-mount>
  - <private-source-mount>
  - token/API key/password/secret patterns
  - credential-looking strings
Only report these scans as targeted, not comprehensive.

Path contract:
Owned paths for safe public repo strengthening:
- docs/reports/
- scripts/llm_wiki_strengthening_scorecard.py
- wikis/*/wiki/portal.md
- wikis/*/wiki/index.md only for safe navigation links
- wikis/*/wiki/overview.md only for safe count/navigation/summary refreshes based on committed repo content
- wikis/*/wiki/entities/ only when issue-approved and public-safe
- wikis/*/wiki/concepts/ only when issue-approved and public-safe
- wikis/*/wiki/standards/ only when issue-approved and public-safe and not reproducing standards text

Read-only paths:
- README.md
- LICENSE
- wikis/cross-links.md
- existing wikis/** pages used as public metadata/context
- tests/fixtures/** unless a test change is explicitly needed
- seeds/** unless an issue explicitly owns them

Forbidden paths/content:
- any raw PDFs or private archives
- non-public source mounts
- external/private source trees
- credentials/tokens/secrets
- vendor standards text reproduction
- workspace-hub pipeline/control-plane files unless you are only reading them outside this repo for context
- unrelated repo root clutter
- broad rewrites not tied to an approved issue

Expected final output:
When done, provide a concise operator report:
- issues completed/closed,
- issues left open and why,
- commits pushed,
- validation evidence,
- any future issues created,
- raw/private/vendor boundary confirmation,
- final git clean-state proof.
```

For a non-interactive Codex launch, run:

```bash
cd <llm-wiki-repo>
codex exec --sandbox workspace-write "$(cat docs/session-handoffs/2026-05-06-codex-goal-llm-wiki-completion-prompt.md)" < /dev/null 2>&1 | tee /tmp/codex-llm-wiki-goal.log
```
