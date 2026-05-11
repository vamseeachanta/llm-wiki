# Codex Adversarial Review — llm-wiki issues 43-48 plan batch (round 1)

Initial review returned MAJOR and drove the first patch set.

Verdict: MAJOR

Findings:
- **High: validation command is not executable in all six plans.** `grep -RInE '<repo secret/client/private denylist pattern>' docs/governance docs/plans` is a placeholder, not an exact command. This fails review question 3. Each plan should name the concrete denylist file/patterns or provide a repo-local script/command that can actually run.
- **High: issue references are unsafe for a public/forked repo context.** All plans rely on bare issue numbers such as `GitHub issue #43`, `Parent blocker: #19`, and `future #25 execution command`. Since the review explicitly warns that fork issue numbering can conflict, these should include stable artifact names/titles or repo-qualified references, not bare numbers alone.
- **High: Issues #47 and #48 are ambiguous around approval-bound private artifacts.** The source/input family references plan branches and SHAs, and required fields include `approved plan artifact path or replacement approval`, `registry/subset artifact path`, `transfer ledger artifact path`, etc. The plans do not explicitly say these artifacts must not be copied from private/approval-bound branches unless independently cleared and public-safe. This is a risk against “no copied approval-bound private artifacts.”
- **Medium: public-safety boundaries are strong but generic.** The common forbidden actions cover `/mnt/ace`, vendor standards text, client/private material, and raw extraction. However, #47/#48 need extra language for “do not copy private planning artifacts, ledgers, registries, summaries, or aliases verbatim; recreate only approved public-safe metadata.”
- **Medium: owned paths are mostly clear, but validation scope is broader than touched artifacts.** The plans say scan `docs/governance docs/plans`, which may produce unrelated historical matches. Better acceptance would define “touched artifact paths” exactly, plus an optional broader repo safety scan.
- **Low: approval gate is clear.** Each plan states `status: plan-review`, blocks implementation until explicit user approval and `status:plan-approved`, and frames the deliverable as governance/planning only.

Required fixes before posting/commit:
- Replace the placeholder grep with concrete executable validation commands.
- Replace or augment bare issue numbers with stable titles/artifact identifiers and repo-qualified references.
- Add explicit #47/#48 prohibition on copying approval-bound private artifacts or branch contents into the public repo without separate clearance.
- Clarify exact touched paths for validation.

Residual risks acceptable for plan-review:
- The plans still depend on future human approval and issue comments, but that is acceptable because they do not authorize implementation.
- The source-family labels expose limited project/topic metadata, but the current level appears acceptable for governance planning if the project already considers those labels public-safe.
