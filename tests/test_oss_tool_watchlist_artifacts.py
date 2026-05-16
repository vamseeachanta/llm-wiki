"""Regression tests for OSS engineering-tool watchlist artifacts."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_oss_tool_watchlist.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_oss_tool_watchlist", VALIDATOR_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALID_REPORT = """# OSS engineering-tool watchlist — 2026-05-15

## Run metadata
- Date: 2026-05-15
- Schema version: `oss-tool-watchlist-report/v1`
- Roadmap anchor: https://github.com/vamseeachanta/llm-wiki/issues/13
- Public-safety note: public-safe metadata-only report; no raw/private/vendor/client content.

## Tools checked and signal sources
| Tool | Signal strategy | Source URL | Docs URL | Tier-1 links | Wiki target |
|---|---|---|---|---|---|
| MoorDyn | github_release | https://api.github.com/repos/FloatingArrayDesign/MoorDyn/releases/latest | https://moordyn.readthedocs.io/ | https://github.com/vamseeachanta/digitalmodel | `wikis/engineering/wiki/entities/moordyn-tool.md` |

## Detected changes
| Tool | Signal type | Observed | Previous | Confidence | Why it matters |
|---|---|---|---|---|---|
| MoorDyn | new_release | v1.1.0 | v1.0.0 | high | Mooring dynamics coverage supports offshore code development. |

## Candidate wiki updates
| Tool | Candidate action | Affected paths | Rationale |
|---|---|---|---|
| MoorDyn | create_initial_seed_page | `wikis/engineering/wiki/entities/moordyn-tool.md` | Public release changed and wiki target is missing. |

## Duplicate/open-issue routing
| Tool | Route action | Issue | Route reason |
|---|---|---|---|
| MoorDyn | reuse-existing-issue | [#79](https://github.com/vamseeachanta/llm-wiki/issues/79) | Watchlist lane covers this update. |

## Blocked/manual-review items
No blocked or manual-review items.

## Validation evidence
- `uv run pytest tests/test_oss_tool_watchlist.py tests/test_oss_tool_watchlist_artifacts.py -q`
- `uv run python scripts/validate_oss_tool_watchlist.py data/oss_tool_watchlist.json docs/reports/2026-05-15-oss-engineering-tool-watchlist.md`
"""


def _valid_manifest() -> dict:
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
                "update_relevance_rule": "Update when public release changes.",
                "last_checked": "2026-05-08",
                "last_seen_version": "v1.0.0",
                "last_seen_release_date": "2026-05-01",
                "last_seen_signal_summary": "Baseline release.",
                "status": "candidate",
                "confidence": "high",
                "why_it_matters": "Mooring dynamics coverage supports offshore code development.",
                "noise_policy": "release-only",
            }
        ],
    }


def test_validator_accepts_valid_manifest_and_report(tmp_path: Path) -> None:
    validator = _load_validator()
    manifest = tmp_path / "data" / "oss_tool_watchlist.json"
    report = tmp_path / "docs" / "reports" / "2026-05-15-oss-engineering-tool-watchlist.md"
    manifest.parent.mkdir(parents=True)
    report.parent.mkdir(parents=True)
    manifest.write_text(json.dumps(_valid_manifest()), encoding="utf-8")
    report.write_text(VALID_REPORT, encoding="utf-8")

    assert validator.validate_artifacts(manifest, report) == []


def test_validator_rejects_missing_required_report_section(tmp_path: Path) -> None:
    validator = _load_validator()
    manifest = tmp_path / "data" / "oss_tool_watchlist.json"
    report = tmp_path / "docs" / "reports" / "2026-05-15-oss-engineering-tool-watchlist.md"
    manifest.parent.mkdir(parents=True)
    report.parent.mkdir(parents=True)
    manifest.write_text(json.dumps(_valid_manifest()), encoding="utf-8")
    report.write_text(VALID_REPORT.replace("## Candidate wiki updates", "## Candidates"), encoding="utf-8")

    failures = validator.validate_artifacts(manifest, report)

    assert any("missing required section" in failure for failure in failures)


def test_validator_rejects_private_paths_and_secret_like_text(tmp_path: Path) -> None:
    validator = _load_validator()
    manifest = tmp_path / "data" / "oss_tool_watchlist.json"
    report = tmp_path / "docs" / "reports" / "2026-05-15-oss-engineering-tool-watchlist.md"
    manifest.parent.mkdir(parents=True)
    report.parent.mkdir(parents=True)
    data = _valid_manifest()
    data["tools"][0]["docs_url"] = "/" + "mnt" + "/" + "ace" + "/private/tool-docs"
    manifest.write_text(json.dumps(data), encoding="utf-8")
    report.write_text(VALID_REPORT + "\napi_key = forbidden\n", encoding="utf-8")

    failures = validator.validate_artifacts(manifest, report)

    assert any("public-safety" in failure for failure in failures)


def test_validator_requires_manifest_fields(tmp_path: Path) -> None:
    validator = _load_validator()
    manifest = tmp_path / "data" / "oss_tool_watchlist.json"
    report = tmp_path / "docs" / "reports" / "2026-05-15-oss-engineering-tool-watchlist.md"
    manifest.parent.mkdir(parents=True)
    report.parent.mkdir(parents=True)
    data = _valid_manifest()
    del data["tools"][0]["source_url"]
    manifest.write_text(json.dumps(data), encoding="utf-8")
    report.write_text(VALID_REPORT, encoding="utf-8")

    failures = validator.validate_artifacts(manifest, report)

    assert any("source_url" in failure for failure in failures)


def test_checked_in_manifest_has_at_least_ten_priority_tools() -> None:
    validator = _load_validator()
    manifest = ROOT / "data" / "oss_tool_watchlist.json"

    failures = validator.validate_manifest(manifest)

    assert failures == []
    data = json.loads(manifest.read_text(encoding="utf-8"))
    assert len(data["tools"]) >= 10
    assert {"moordyn", "moorpy", "openfast", "capytaine", "hams", "wec-sim", "opm", "openfoam", "gmsh", "freecad"}.issubset(
        {tool["slug"] for tool in data["tools"]}
    )


def test_checked_in_weekly_report_and_latest_state_are_valid() -> None:
    validator = _load_validator()
    manifest = ROOT / "data" / "oss_tool_watchlist.json"
    report = ROOT / "docs" / "reports" / "2026-05-16-oss-engineering-tool-watchlist.md"
    latest_state = ROOT / "artifacts" / "watchlist" / "latest-state.json"

    assert validator.validate_artifacts(manifest, report) == []
    state = json.loads(latest_state.read_text(encoding="utf-8"))
    assert state["schema_version"] == "oss-tool-watchlist-state/v1"
    assert state["run_date"] == "2026-05-16"
    assert state["totals"]["tools_checked"] >= 10
