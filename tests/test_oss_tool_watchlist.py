"""Tests for the OSS engineering-tool watchlist scanner."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "llm_wiki_oss_tool_watchlist.py"


def _load_watchlist():
    spec = importlib.util.spec_from_file_location("llm_wiki_oss_tool_watchlist", SCRIPT_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _sample_watchlist() -> dict:
    return {
        "schema_version": "oss-tool-watchlist/v1",
        "tools": [
            {
                "name": "MoorDyn",
                "slug": "moordyn",
                "owner": "FloatingArrayDesign",
                "repo": "MoorDyn",
                "upstream_url": "https://github.com/FloatingArrayDesign/MoorDyn",
                "docs_url": "https://moordyn.readthedocs.io/",
                "source_type": "github",
                "source_url": "https://api.github.com/repos/FloatingArrayDesign/MoorDyn/releases/latest",
                "signal_strategy": "github_release",
                "domain": "marine-offshore",
                "tier1_repo_links": ["https://github.com/vamseeachanta/digitalmodel"],
                "wiki_target": "wikis/engineering/wiki/entities/moordyn-tool.md",
                "affected_paths": ["wikis/engineering/wiki/entities/moordyn-tool.md"],
                "update_relevance_rule": "Update wiki page when public release version changes.",
                "last_checked": "2026-05-08",
                "last_seen_version": "v1.0.0",
                "last_seen_release_date": "2026-05-01",
                "last_seen_signal_summary": "Baseline release.",
                "status": "candidate",
                "confidence": "high",
                "why_it_matters": "Mooring dynamics coverage supports offshore code development.",
                "noise_policy": "release-only",
            },
            {
                "name": "OpenFOAM",
                "slug": "openfoam",
                "owner": "OpenFOAM",
                "repo": "OpenFOAM-dev",
                "upstream_url": "https://github.com/OpenFOAM/OpenFOAM-dev",
                "docs_url": "https://www.openfoam.com/documentation/",
                "source_type": "github",
                "source_url": "https://api.github.com/repos/OpenFOAM/OpenFOAM-dev/releases/latest",
                "signal_strategy": "github_release",
                "domain": "cfd",
                "tier1_repo_links": ["https://github.com/vamseeachanta/digitalmodel"],
                "wiki_target": "wikis/engineering/wiki/entities/openfoam-cfd.md",
                "affected_paths": ["wikis/engineering/wiki/entities/openfoam-cfd.md"],
                "update_relevance_rule": "Review when release or docs version changes.",
                "last_checked": "2026-05-08",
                "last_seen_version": "v2312",
                "last_seen_release_date": "2023-12-01",
                "last_seen_signal_summary": "Existing wiki page baseline.",
                "status": "active",
                "confidence": "medium",
                "why_it_matters": "CFD solver coverage supports simulation workflows.",
                "noise_policy": "manual-review-for-dev-branch",
            },
        ],
    }


def test_manifest_schema_requires_priority_public_fields(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    manifest = tmp_path / "data" / "oss_tool_watchlist.json"
    _write_json(manifest, _sample_watchlist())

    loaded = watchlist.load_watchlist(manifest)
    failures = watchlist.validate_watchlist(loaded, repo_root=tmp_path)

    assert failures == []
    assert len(loaded["tools"]) == 2
    assert {tool["slug"] for tool in loaded["tools"]} == {"moordyn", "openfoam"}


def test_signal_normalization_detects_new_release_docs_change_unavailable_and_missing_page(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    tool = _sample_watchlist()["tools"][0]
    previous = {"observed_value": "v1.0.0", "observed_release_date": "2026-05-01", "observed_docs_marker": "docs-1"}

    release = watchlist.normalize_signal(tool, {"observed_value": "v1.1.0", "observed_release_date": "2026-05-12"}, previous, repo_root=tmp_path, observed_at="2026-05-15")
    assert release.signal_type == "new_release"
    assert release.recommendation_action == "create_initial_seed_page"

    docs = watchlist.normalize_signal(tool, {"observed_value": "v1.0.0", "observed_docs_marker": "docs-2"}, previous, repo_root=tmp_path, observed_at="2026-05-15")
    assert docs.signal_type == "docs_changed"

    unavailable = watchlist.normalize_signal(tool, {"error": "rate limited"}, previous, repo_root=tmp_path, observed_at="2026-05-15")
    assert unavailable.signal_type == "signal_unavailable"

    missing_page = watchlist.normalize_signal(tool, {"observed_value": "v1.0.0"}, previous, repo_root=tmp_path, observed_at="2026-05-15")
    assert missing_page.signal_type == "candidate_page_missing"


def test_scan_fixture_mode_renders_issue_deduplicated_report(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    repo = tmp_path
    manifest = repo / "data" / "oss_tool_watchlist.json"
    issue_map = repo / "data" / "oss_tool_issue_map.json"
    fixture_dir = repo / "tests" / "fixtures" / "oss_tool_watchlist"
    _write_json(manifest, _sample_watchlist())
    _write_json(issue_map, {"schema_version": "oss-tool-issue-map/v1", "routes": {"moordyn": {"issue": 79, "action": "reuse-existing-issue", "title": "MoorDyn watchlist lane"}, "default": {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"}}})
    _write_json(fixture_dir / "moordyn.json", {"observed_value": "v1.1.0", "observed_release_date": "2026-05-12", "signal_summary": "Release metadata changed."})
    _write_json(fixture_dir / "openfoam.json", {"observed_value": "v2312", "signal_summary": "No new release metadata."})
    (repo / "wikis" / "engineering" / "wiki" / "entities").mkdir(parents=True)
    (repo / "wikis" / "engineering" / "wiki" / "entities" / "openfoam-cfd.md").write_text("# OpenFOAM\n", encoding="utf-8")

    report = watchlist.scan_watchlist(repo, manifest, issue_map, fixture_dir, run_date="2026-05-15")
    rendered = watchlist.render_report(report)

    assert report.totals["tools_checked"] == 2
    assert report.totals["new_release"] == 1
    assert any(row.slug == "moordyn" and row.route_issue == 13 and row.route_action == "comment-on-roadmap" for row in report.rows)
    assert not any(row.recommendation_action == "open-new-issue" for row in report.rows)
    assert "## Tools checked and signal sources" in rendered
    assert "## Duplicate/open-issue routing" in rendered
    assert "https://github.com/vamseeachanta/llm-wiki/issues/13" in rendered
    assert "/mnt/ace" not in rendered


def test_signal_type_routes_apply_before_recommendation_action_fallback(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    repo = tmp_path
    manifest = repo / "data" / "oss_tool_watchlist.json"
    issue_map = repo / "data" / "oss_tool_issue_map.json"
    fixture_dir = repo / "tests" / "fixtures" / "oss_tool_watchlist"
    _write_json(manifest, _sample_watchlist())
    _write_json(
        issue_map,
        {
            "schema_version": "oss-tool-issue-map/v1",
            "routes": {
                "docs_changed": {"issue": 88, "action": "comment-on-docs-review", "title": "Docs review lane"},
                "update_existing_wiki_page": {"issue": 77, "action": "comment-on-update-lane", "title": "Update lane"},
                "default": {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"},
            },
        },
    )
    _write_json(fixture_dir / "openfoam.json", {"observed_value": "v2312", "observed_docs_marker": "docs-v2", "signal_summary": "Docs marker changed."})
    _write_json(fixture_dir / "moordyn.json", {"observed_value": "v1.0.0", "signal_summary": "No release change."})
    previous = repo / "artifacts" / "watchlist" / "latest-state.json"
    _write_json(
        previous,
        {
            "schema_version": "oss-tool-watchlist-state/v1",
            "run_date": "2026-05-08",
            "rows": [
                {"slug": "openfoam", "observed_value": "v2312", "observed_release_date": "2023-12-01", "observed_docs_marker": "docs-v1"},
                {"slug": "moordyn", "observed_value": "v1.0.0", "observed_release_date": "2026-05-01", "observed_docs_marker": "docs-v1"},
            ],
        },
    )
    (repo / "wikis" / "engineering" / "wiki" / "entities").mkdir(parents=True)
    (repo / "wikis" / "engineering" / "wiki" / "entities" / "openfoam-cfd.md").write_text("# OpenFOAM\n", encoding="utf-8")
    (repo / "wikis" / "engineering" / "wiki" / "entities" / "moordyn-tool.md").write_text("# MoorDyn\n", encoding="utf-8")

    report = watchlist.scan_watchlist(repo, manifest, issue_map, fixture_dir, run_date="2026-05-15", previous_state_path=previous)

    docs_row = next(row for row in report.rows if row.slug == "openfoam")
    assert docs_row.signal_type == "docs_changed"
    assert docs_row.recommendation_action == "update_existing_wiki_page"
    assert docs_row.route_issue == 88
    assert docs_row.route_action == "comment-on-docs-review"


def test_oss_route_state_rejects_closed_reuse_existing_issue() -> None:
    watchlist = _load_watchlist()
    routes = {"moordyn": {"issue": 79, "action": "reuse-existing-issue", "title": "MoorDyn watchlist lane"}}

    failures = watchlist.validate_issue_routes(routes, {79: "CLOSED"})

    assert failures == ["moordyn targets closed issue #79 with active action reuse-existing-issue"]


def test_oss_slug_specific_closed_route_is_normalized_before_render(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    repo = tmp_path
    manifest = repo / "data" / "oss_tool_watchlist.json"
    issue_map = repo / "data" / "oss_tool_issue_map.json"
    fixture_dir = repo / "tests" / "fixtures" / "oss_tool_watchlist"
    _write_json(manifest, _sample_watchlist())
    _write_json(issue_map, {"schema_version": "oss-tool-issue-map/v1", "routes": {"moordyn": {"issue": 79, "action": "reuse-existing-issue", "title": "MoorDyn watchlist lane"}, "default": {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"}}})
    _write_json(fixture_dir / "moordyn.json", {"observed_value": "v1.1.0", "observed_release_date": "2026-05-12", "signal_summary": "Release metadata changed."})

    report = watchlist.scan_watchlist(repo, manifest, issue_map, fixture_dir, run_date="2026-05-15")
    rendered = watchlist.render_report(report)

    moordyn = next(row for row in report.rows if row.slug == "moordyn")
    assert moordyn.route_issue == 13
    assert moordyn.route_action == "comment-on-roadmap"
    assert "reuse-existing-issue | [#79]" not in rendered


def test_write_outputs_separates_static_config_state_and_report(tmp_path: Path) -> None:
    watchlist = _load_watchlist()
    repo = tmp_path
    manifest = repo / "data" / "oss_tool_watchlist.json"
    issue_map = repo / "data" / "oss_tool_issue_map.json"
    _write_json(manifest, _sample_watchlist())
    _write_json(issue_map, {"schema_version": "oss-tool-issue-map/v1", "routes": {"default": {"issue": 13, "action": "comment-on-roadmap", "title": "Roadmap anchor"}}})

    report = watchlist.scan_watchlist(repo, manifest, issue_map, fixtures_dir=None, run_date="2026-05-15")
    md_path, state_path = watchlist.write_outputs(repo, report)

    assert md_path == repo / "docs" / "reports" / "2026-05-15-oss-engineering-tool-watchlist.md"
    assert state_path == repo / "artifacts" / "watchlist" / "2026-05-15-oss-tool-watchlist-state.json"
    assert md_path.exists()
    assert state_path.exists()
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["schema_version"] == "oss-tool-watchlist-state/v1"
    assert state["run_date"] == "2026-05-15"
