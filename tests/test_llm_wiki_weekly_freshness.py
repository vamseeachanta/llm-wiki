"""Tests for the weekly llm-wiki freshness control loop."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "llm_wiki_weekly_freshness.py"


def _load_weekly():
    spec = importlib.util.spec_from_file_location("llm_wiki_weekly_freshness", SCRIPT_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_analyze_repo_detects_stale_frontmatter_and_broken_links(tmp_path: Path) -> None:
    weekly = _load_weekly()
    repo = tmp_path
    _write(
        repo / "wikis" / "engineering" / "wiki" / "concepts" / "old-page.md",
        "---\ntitle: Old Page\nlast_updated: 2026-03-01\n---\n# Old Page\n[Missing](../entities/missing.md)\n",
    )
    _write(
        repo / "wikis" / "engineering" / "wiki" / "entities" / "fresh.md",
        "---\ntitle: Fresh\nlast_updated: 2026-05-14\n---\n# Fresh\n[Old](../concepts/old-page.md)\n",
    )
    _write(repo / "wikis" / "engineering" / "wiki" / "sources" / "no-frontmatter.md", "# No Frontmatter\n")

    report = weekly.analyze_repo(repo, date(2026, 5, 15), stale_days=30, max_items=10)

    assert report.totals.total_pages == 3
    assert report.totals.missing_frontmatter == 1
    assert report.domains["engineering"].total_pages == 3
    assert report.domains["engineering"].missing_frontmatter == 1
    assert [item.path for item in report.stale_pages] == ["wikis/engineering/wiki/concepts/old-page.md"]
    assert report.stale_pages[0].age_days == 75
    assert report.broken_links[0].source == "wikis/engineering/wiki/concepts/old-page.md"
    assert report.broken_links[0].target == "../entities/missing.md"


def test_issue_recommendations_are_deduplicated_to_existing_lanes(tmp_path: Path) -> None:
    weekly = _load_weekly()
    repo = tmp_path
    _write(repo / "wikis" / "lng-projects" / "wiki" / "concepts" / "gap.md", "# Gap\n")
    _write(
        repo / "wikis" / "engineering" / "wiki" / "concepts" / "stale.md",
        "---\ntitle: Stale\nlast_updated: 2026-01-01\n---\n# Stale\n",
    )
    _write(
        repo / "data" / "concept_watchlist.json",
        '{"items":[{"concept":"llms.txt","route_key":"llms-entrypoints"},{"concept":"GraphRAG","route_key":"oss-watchlist"}]}',
    )

    report = weekly.analyze_repo(repo, date(2026, 5, 15), stale_days=30, max_items=10)
    recommendations = weekly.build_recommendations(report)

    assert any(r.issue == 13 and r.action == "comment-on-roadmap" for r in recommendations)
    assert any(r.issue == 13 and r.issue_route == "llms-entrypoints" for r in recommendations)
    assert any(r.issue == 13 and r.issue_route == "oss-watchlist" for r in recommendations)
    titles = [r.title for r in recommendations]
    assert len(titles) == len(set(titles))
    assert not any(r.action == "open-new-issue" for r in recommendations)


def test_weekly_route_state_rejects_closed_active_update_issue() -> None:
    weekly = _load_weekly()
    routes = {
        "oss-watchlist": {"issue": 79, "title": "Weekly OSS engineering-tool watchlist", "action": "update-existing-issue"},
        "portfolio-roadmap": {"issue": 13, "title": "Roadmap anchor", "action": "comment-on-roadmap"},
    }

    failures = weekly.validate_issue_routes(routes, {79: "CLOSED", 13: "OPEN"})

    assert failures == ["oss-watchlist targets closed issue #79 with active action update-existing-issue"]


def test_weekly_route_state_allows_open_active_update_issue() -> None:
    weekly = _load_weekly()
    routes = {"active-plan": {"issue": 88, "title": "Active plan", "action": "update-existing-issue"}}

    assert weekly.validate_issue_routes(routes, {88: "OPEN"}) == []


def test_weekly_default_routes_do_not_target_closed_children_when_map_missing(tmp_path: Path) -> None:
    weekly = _load_weekly()

    routes = weekly.load_issue_routes(tmp_path)

    assert routes["llms-entrypoints"]["issue"] == 13
    assert routes["llms-entrypoints"]["action"] == "comment-on-roadmap"
    assert routes["oss-watchlist"]["issue"] == 13
    assert routes["oss-watchlist"]["action"] == "comment-on-roadmap"


def test_weekly_generated_report_has_no_closed_active_update_targets(tmp_path: Path) -> None:
    weekly = _load_weekly()
    repo = tmp_path
    _write(repo / "wikis" / "engineering" / "wiki" / "concepts" / "fresh.md", "---\ntitle: Fresh\nlast_updated: 2026-05-15\n---\n# Fresh\n")
    _write(repo / "data" / "concept_watchlist.json", '{"items":[{"concept":"llms.txt","route_key":"llms-entrypoints"},{"concept":"GraphRAG","route_key":"oss-watchlist"}]}')

    report = weekly.analyze_repo(repo, date(2026, 5, 15), stale_days=30, max_items=10)
    rendered = weekly.render_report(report)

    assert "update-existing-issue | [#76]" not in rendered
    assert "update-existing-issue | [#79]" not in rendered


def test_validate_issue_route_state_cli_reports_closed_targets(tmp_path: Path) -> None:
    route_map = tmp_path / "route-map.json"
    state_map = tmp_path / "states.json"
    route_map.write_text(json.dumps({"routes": {"bad-route": {"issue": 79, "action": "update-existing-issue", "title": "Closed target"}}}), encoding="utf-8")
    state_map.write_text(json.dumps({"79": "CLOSED"}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_issue_route_state.py"), str(route_map), "--state-json", str(state_map)],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "bad-route targets closed issue #79" in result.stderr


def test_validate_issue_route_state_cli_rejects_malformed_routes(tmp_path: Path) -> None:
    route_map = tmp_path / "route-map.json"
    route_map.write_text(json.dumps({"routes": {"bad-route": "not-an-object"}}), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_issue_route_state.py"), str(route_map)],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "bad-route route must be an object" in result.stderr


def test_analyze_repo_uses_previous_json_artifact_as_baseline(tmp_path: Path) -> None:
    weekly = _load_weekly()
    repo = tmp_path
    _write(
        repo / "wikis" / "engineering" / "wiki" / "concepts" / "fresh.md",
        "---\ntitle: Fresh\nlast_updated: 2026-05-15\n---\n# Fresh\n",
    )
    _write(
        repo / "artifacts" / "freshness" / "2026-05-08-weekly-freshness-summary.json",
        '{"schema_version":"weekly-freshness/v1","run_date":"2026-05-08","repo_totals":{"total_pages":3,"missing_frontmatter":1,"missing_last_updated":1,"stale_pages":2,"broken_links":1},"domain_freshness":[{"domain":"engineering","total_pages":3,"missing_frontmatter":1,"missing_last_updated":1,"stale_pages":2,"broken_links":1}]}',
    )

    report = weekly.analyze_repo(repo, date(2026, 5, 15), stale_days=30, max_items=10)

    assert report.baseline_run_date == "2026-05-08"
    assert report.totals.total_pages_delta == -2
    assert report.domains["engineering"].stale_pages_delta == -2



def test_render_report_contains_required_public_safe_sections(tmp_path: Path) -> None:
    weekly = _load_weekly()
    repo = tmp_path
    _write(
        repo / "wikis" / "engineering" / "wiki" / "concepts" / "fresh.md",
        "---\ntitle: Fresh\nlast_updated: 2026-05-15\n---\n# Fresh\n",
    )

    report = weekly.analyze_repo(repo, date(2026, 5, 15), stale_days=30, max_items=10)
    rendered = weekly.render_report(report, recommendations=weekly.build_recommendations(report))

    assert "# llm-wiki weekly freshness report — 2026-05-15" in rendered
    assert "## Repo freshness summary" in rendered
    assert "## Concept watchlist" in rendered
    assert "## Issue recommendations" in rendered
    assert "Issue route" in rendered
    assert "## Blocked / approval-gated lanes" in rendered
    assert "https://github.com/vamseeachanta/llm-wiki/issues/13" in rendered
    assert "/mnt/ace" not in rendered
    assert "public-safe" in rendered
