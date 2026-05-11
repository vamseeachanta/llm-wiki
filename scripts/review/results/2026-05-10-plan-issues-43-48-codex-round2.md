# Codex Adversarial Re-Review — llm-wiki issues 43-48 plan batch (round 2)

Round 2 reviewed the first validation-command patch and found remaining MAJOR issues; later rounds corrected them.

Verdict: MAJOR

**Findings**

1. **MAJOR: Validation commands are still not concrete/executable as written.**  
   All six plans keep:
   ```bash
   TOUCHED='docs/governance/<target-artifact>.md docs/plans/<this-plan>.md'
   ```
   This still depends on manual substitution. That does not fully satisfy the prior required fix to replace placeholder grep with concrete executable validation commands or clarify exact touched paths.

   Required fix: make each plan’s validation command use the exact two touched paths, for example for #43:
   ```bash
   TOUCHED='docs/governance/sesa-extraction-clearance-checklist.md docs/plans/2026-05-10-issue-43-sesa-extraction-clearance-checklist.md'
   grep -RInE '...' $TOUCHED
   ```

2. **MAJOR: Public-safety scan has an impossible expected result.**  
   The grep pattern includes `/mnt/ace|/mnt/ace-data`, but every plan being scanned contains those strings in the forbidden actions and/or parent blocker title. Therefore `Expected result: no matches` is false for the plan files themselves.

   Required fix: either remove `/mnt/ace|/mnt/ace-data` from the touched-file “no matches” scan and validate private-path leakage separately with an allowlist, or change the expected result to allow only the known governance boundary references. A better pattern is two checks:
   - secret/PII scan: expected no matches
   - private path scan: expected only approved boundary/prohibition lines, no raw artifact paths or manifests

3. **MINOR: #47/#48 provenance is improved but not fully repo-qualified.**  
   The branch/SHA references are stable enough for planning, but “Batch Pack 1 plan branch `plan/issue-2364-batch-pack-1` at SHA `7cc1c0b1a`” and equivalent #48 wording do not explicitly say which repository owns those refs. The parent issues are repo-qualified, but the branch provenance should be too.

   Required fix: write those as repo-qualified refs, e.g. `vamseeachanta/llm-wiki@7cc1c0b1a`, branch `plan/issue-2364-batch-pack-1`.

**Answers**

1. Prior findings are only partially resolved. Titles, repo-qualified issue references, and #47/#48 private-artifact prohibitions are mostly addressed, but the validation-command findings are not resolved enough.

2. The plans remain implementation-blocked until explicit user approval / `status:plan-approved`. They are broadly public-safe in intent, and #47/#48 now include the needed prohibition against copying approval-bound private artifacts or branch contents.

3. Yes. The non-concrete validation commands and impossible “expected no matches” scan are MAJOR blockers to committing/posting these as final plan-review artifacts.
