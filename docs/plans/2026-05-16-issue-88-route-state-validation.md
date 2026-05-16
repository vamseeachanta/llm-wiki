# Plan for #88: Prevent weekly route maps from targeting closed issues

> **Status:** plan-review
> **Complexity:** T1
> **Date:** 2026-05-16
> **Issue:** https://github.com/vamseeachanta/llm-wiki/issues/88
> **Review artifacts:** scripts/review/results/2026-05-16-plan-88-hermes.md

---

## Resource Intelligence Summary

### Existing repo code
- `scripts/llm_wiki_weekly_freshness.py` will remain the weekly freshness generator. Its `load_issue_routes()` and `build_recommendations()` path currently reads `data/issue_routing_map.json` and emits issue links into Markdown/JSON report artifacts.
- `scripts/llm_wiki_oss_tool_watchlist.py` will remain the OSS tool watchlist generator. Its `_apply_route()` path currently reads `data/oss_tool_issue_map.json` and emits route actions/issues into report rows.
- `tests/test_llm_wiki_weekly_freshness.py` and `tests/test_oss_tool_watchlist.py` will receive TDD regression coverage before route-map implementation changes.

### Standards
Not applicable — route-state validation is a repo workflow / harness issue, not engineering calculation or standards content.

### LLM Wiki pages consulted
No domain wiki page content will be changed. This issue will affect cadence control-plane metadata and report routing only.

### Documents consulted
- Issue [#88](https://github.com/vamseeachanta/llm-wiki/issues/88) defines the route-state bug and acceptance criteria.
- Issue [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) remains the live roadmap anchor and fallback routing target for weekly triage.
- Issues [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) and [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) are closed implementation issues; future weekly updates should not be routed to them by default.
- `docs/reports/2026-05-15-llm-wiki-weekly-freshness-report.md` shows current weekly recommendation output with routes to #76 and #79.
- `docs/reports/2026-05-16-oss-engineering-tool-watchlist.md` shows current OSS watchlist route output with at least one signal routed to #79.

### Gaps identified
- No current test will fail when a route map targets a closed GitHub issue for active update actions.
- No current command will validate live GitHub issue state for weekly/OSS route targets before closeout.
- `scripts/llm_wiki_weekly_freshness.py` also carries built-in fallback routes to closed child issues [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) and [#79](https://github.com/vamseeachanta/llm-wiki/issues/79); a JSON-only fix would leave a reachable closed-target path.
- Route maps and generator defaults need a safe fallback rule for completed child implementation issues: use [#13](https://github.com/vamseeachanta/llm-wiki/issues/13) unless a new open child issue explicitly owns the lane.

### Evidence

**Issue statuses** (verified 2026-05-16T12:38:01Z via `gh issue view`):
- `#13` — OPEN — `epic(knowledge): llm-wiki strengthening roadmap and execution waves`
- `#76` — CLOSED — `docs(agent): add llms.txt entrypoints and curated domain manifests`
- `#79` — CLOSED — `feat(research): maintain weekly OSS engineering-tool watchlist and update candidates`
- `#88` — OPEN — `fix(cadence): prevent weekly route maps from targeting closed issues`

**File existence** (verified 2026-05-16T12:38:01Z):
- EXISTS: `data/issue_routing_map.json`
- EXISTS: `data/oss_tool_issue_map.json`
- EXISTS: `scripts/llm_wiki_weekly_freshness.py`
- EXISTS: `scripts/llm_wiki_oss_tool_watchlist.py`
- EXISTS: `tests/test_llm_wiki_weekly_freshness.py`
- EXISTS: `tests/test_oss_tool_watchlist.py`
- EXISTS: `docs/reports/2026-05-15-llm-wiki-weekly-freshness-report.md`
- EXISTS: `docs/reports/2026-05-16-oss-engineering-tool-watchlist.md`

**Line excerpts** (`read_file` evidence):

`data/issue_routing_map.json`:
```json
"llms-entrypoints": {"issue": 76, "title": "llms.txt entrypoints", "action": "update-existing-issue"}
"oss-watchlist": {"issue": 79, "title": "Weekly OSS engineering-tool watchlist", "action": "update-existing-issue"}
```

`scripts/llm_wiki_weekly_freshness.py` lines 346-386:
```python
def load_issue_routes(repo_root: Path | None = None) -> dict[str, dict[str, str | int]]:
    ...
    "llms-entrypoints": {"issue": 76, "title": "llms.txt entrypoints", "action": "update-existing-issue"},
    "oss-watchlist": {"issue": 79, "title": "Weekly OSS engineering-tool watchlist", "action": "update-existing-issue"},
    return {str(key): value for key, value in routes.items()}
...
for item in report.concept_watchlist:
    route_key = str(item.get("route_key", "")).strip()
    ...
    recs.append(_recommendation(routes[route_key], rationale, f"concept-{route_key}", ...))
```

`scripts/llm_wiki_oss_tool_watchlist.py` lines 263-267:
```python
def _apply_route(row: WatchlistRow, issue_map: dict[str, Any]) -> WatchlistRow:
    routes = issue_map.get("routes", {}) if isinstance(issue_map.get("routes", {}), dict) else {}
    route = routes.get(row.slug) or routes.get(row.signal_type) or routes.get(row.recommendation_action) or routes.get("default") or {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"}
    ...
```

**Reproduction proofs**:

```text
$ gh issue view 76 --json state --jq .state
CLOSED
$ gh issue view 79 --json state --jq .state
CLOSED
$ jq '.routes["llms-entrypoints"], .routes["oss-watchlist"]' data/issue_routing_map.json
{"issue":76,...}
{"issue":79,...}
$ jq '.routes.moordyn' data/oss_tool_issue_map.json
{"issue":79,...}
```

- Reproduced at: 2026-05-16T12:38:01Z
- Failure mode observed matches issue claim: YES — committed route maps reference closed issues for active routing actions.

---

## Artifact Map

| Artifact | Path |
|---|---|
| This plan | `docs/plans/2026-05-16-issue-88-route-state-validation.md` |
| Weekly freshness tests | `tests/test_llm_wiki_weekly_freshness.py` |
| OSS watchlist tests | `tests/test_oss_tool_watchlist.py` |
| Weekly freshness generator | `scripts/llm_wiki_weekly_freshness.py` |
| OSS watchlist generator | `scripts/llm_wiki_oss_tool_watchlist.py` |
| Weekly route map | `data/issue_routing_map.json` |
| OSS route map | `data/oss_tool_issue_map.json` |
| Route-state validator or documented command | `scripts/validate_issue_route_state.py` or an existing validator extension |
| Plan review | `scripts/review/results/2026-05-16-plan-88-hermes.md` |

---

## Deliverable

A TDD-backed route-state validation layer will prevent weekly freshness and OSS watchlist outputs from routing active updates to closed GitHub issues unless the action is explicitly archival/non-updating.

---

## Pseudocode

```text
ACTIVE_UPDATE_ACTIONS = {"update-existing-issue", "reuse-existing-issue"}
FALLBACK_ROUTE = {issue: 13, action: "comment-on-roadmap", title: "Roadmap anchor"}

function validate_route_map(route_map, issue_state_lookup):
    for each route in route_map.routes:
        if route.action in ACTIVE_UPDATE_ACTIONS:
            state = issue_state_lookup(route.issue)
            if state != "OPEN":
                record failure or fallback recommendation

function apply_safe_route(route, issue_state_lookup, allow_offline=False):
    if offline/default generation and no live state is requested:
        use code-level safe defaults plus committed route map data that tests prove does not target known closed child issues
    if live state validation is requested and route is active-update to closed issue:
        return roadmap fallback route or fail validation before closeout

function load_weekly_default_routes():
    return only #13 roadmap fallback routes unless a child issue is known open and intentionally configured

function apply_oss_route(row, issue_map):
    select slug/signal/action/default route
    if route is a known completed child issue in committed policy:
        normalize to #13 roadmap fallback before rendering

function validate_issue_route_state_cli(files):
    load each route-map JSON
    use gh issue view for unique issue IDs
    fail with clear route keys and closed issue IDs when active-update routes target closed issues
```

---

## Files to Change

| Action | Path | Reason |
|---|---|---|
| Modify | `tests/test_llm_wiki_weekly_freshness.py` | Add RED regression for active weekly routes targeting closed issues / closed-state fixtures. |
| Modify | `tests/test_oss_tool_watchlist.py` | Add RED regression for active OSS route actions targeting closed issues / fallback behavior. |
| Modify | `data/issue_routing_map.json` | Route completed child-lane weekly recommendations to #13 unless a new open child issue owns them. |
| Modify | `data/oss_tool_issue_map.json` | Route completed implementation issue signals to #13 or an open follow-up issue instead of closed #79. |
| Modify | `scripts/llm_wiki_weekly_freshness.py` | Mandatory: remove closed #76/#79 built-in defaults and add code-level route-state safe defaults/normalization needed by tests. |
| Modify | `scripts/llm_wiki_oss_tool_watchlist.py` | Mandatory: add code-level route-state safe normalization so slug/action routes cannot keep targeting closed implementation issues. |
| Create/Modify | `scripts/validate_issue_route_state.py` or existing validators | Provide closeout command that checks live GitHub state for route targets. |
| Update | `docs/plans/README.md` | Index this plan with `plan-review` status. |

---

## TDD Test List

| Test name | What it verifies | Expected input | Expected output |
|---|---|---|---|
| `test_weekly_route_state_rejects_closed_active_update_issue` | Weekly active update routes may not target closed issues. | Temp route map route `issue: 79`, `action: update-existing-issue`, fixture state `CLOSED`. | Validation failure names route key and issue. |
| `test_weekly_route_state_allows_open_active_update_issue` | Open child issue routes remain valid. | Temp route map route `issue: 88`, `action: update-existing-issue`, fixture state `OPEN`. | Validation passes. |
| `test_weekly_closed_child_routes_fall_back_to_roadmap` | Completed weekly lanes fall back to #13 when no open child owns the lane. | Committed route map after fix. | Recommendations for completed lanes use #13 / `comment-on-roadmap`. |
| `test_weekly_default_routes_do_not_target_closed_children_when_map_missing` | Built-in weekly fallback routes cannot reintroduce #76/#79 if JSON is absent. | Temp repo without `data/issue_routing_map.json`. | `load_issue_routes()` returns #13 fallback routes only for completed lanes. |
| `test_weekly_generated_report_has_no_closed_active_update_targets` | Normal offline generation output is safe even without a separate live validator. | Committed maps and concept watchlist. | Rendered report contains no `update-existing-issue` row to #76/#79. |
| `test_oss_route_state_rejects_closed_reuse_existing_issue` | OSS `reuse-existing-issue` may not target closed issues. | Temp map route `moordyn -> #79`, fixture state `CLOSED`. | Validation failure names `moordyn` and `#79`. |
| `test_oss_closed_child_routes_fall_back_to_roadmap` | OSS watchlist route output does not route actionable updates to closed #79. | Fixture producing MoorDyn update signal. | Row route uses #13 or an explicitly open issue. |
| `test_oss_slug_specific_closed_route_is_normalized_before_render` | Slug-specific routes cannot bypass fallback policy. | Route map with `moordyn -> #79`, action `reuse-existing-issue`. | Rendered row routes to #13 / `comment-on-roadmap`. |
| `test_oss_generated_report_has_no_closed_active_update_targets` | Normal offline OSS generation output is safe even without a separate live validator. | Committed OSS watchlist and issue map. | Rendered report contains no `reuse-existing-issue` row to closed #79. |
| `test_validate_issue_route_state_cli_reports_closed_targets` | The closeout validator catches route-state drift through a CLI. | Temp route map with closed fixture state. | Non-zero exit / failure message. |

---

## Acceptance Criteria

- [ ] RED tests are written first and fail for closed active-update route targets, weekly missing-map fallback, slug-specific OSS fallback, and normal offline rendered output.
- [ ] Implementation updates route maps and route helper/default code so active update actions do not target closed issues by default.
- [ ] Weekly built-in defaults no longer reference closed [#76](https://github.com/vamseeachanta/llm-wiki/issues/76) or [#79](https://github.com/vamseeachanta/llm-wiki/issues/79).
- [ ] OSS slug/action route normalization prevents a closed issue route from reaching rendered report rows.
- [ ] A closeout validation command exists and is documented in affected report validation evidence or README notes.
- [ ] Targeted tests pass: `uv run pytest tests/test_llm_wiki_weekly_freshness.py tests/test_oss_tool_watchlist.py -q`.
- [ ] Full suite passes: `uv run pytest -q`.
- [ ] Public-safety scan passes over changed files; no raw/private/vendor/client content or secrets are introduced.
- [ ] Issue [#88](https://github.com/vamseeachanta/llm-wiki/issues/88) receives implementation evidence before closure.

---

## Adversarial Review Summary

| Provider | Verdict | Key findings |
|---|---|---|
| Hermes | APPROVE after revision | Initial MAJOR found detection-only validation, missed weekly hardcoded closed defaults, and data-only ambiguity; revised plan now requires code-level safe routing/defaults and expanded TDD coverage. |

**Overall result:** PASS after revisions

Revisions made based on review:
- Required code-level safe routing in both generators, not data-only changes.
- Added explicit weekly default-route fix for hardcoded #76/#79 fallbacks.
- Added TDD cases for missing-map fallback, slug-specific OSS fallback, and normal offline rendered output safety.
- Tightened acceptance criteria to require code + data changes.

---

## Risks and Open Questions

- **Risk:** Live `gh` validation could make normal offline report generation flaky. The implementation should keep generation offline-first and make live route-state validation an explicit closeout/validator command.
- **Risk:** Falling back every closed child issue to #13 may reduce specificity. This is acceptable until a new open child issue owns the follow-up lane.
- **Open for approval:** Whether implementation should create a reusable `scripts/validate_issue_route_state.py` command or extend existing report validators. Recommended: create the reusable script because two route maps need the same policy.

---

## Complexity: T1

**T1** — bounded harness/data correction across existing weekly cadence scripts and tests; no domain content expansion and no network data ingestion in report generation.
