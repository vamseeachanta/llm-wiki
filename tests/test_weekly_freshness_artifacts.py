"""Regression tests for weekly freshness report artifacts."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_weekly_freshness_report.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_weekly_freshness_report", VALIDATOR_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


VALID_REPORT = """# llm-wiki weekly freshness report — 2026-05-15

## Run metadata
- Date: 2026-05-15
- Roadmap anchor: https://github.com/vamseeachanta/llm-wiki/issues/13
- Public-safety note: public-safe metadata-only report; no raw/private/vendor/client content.

## Repo freshness summary
| Metric | Value |
|---|---:|
| Total pages | 1 |

## Domain coverage deltas
| Domain | Pages | Δ pages | Missing frontmatter | Δ missing FM | Missing `last_updated` | Δ missing updated | Stale pages | Δ stale | Broken links | Δ broken |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| engineering | 1 | +0 | 0 | +0 | 0 | +0 | 0 | +0 | 0 | +0 |

## Stale pages and structural findings
No stale pages or structural findings above the configured threshold.

## Concept watchlist
| Concept | Why it matters | Public reference |
|---|---|---|
| llms.txt | Entry points | https://llmstxt.org/ |

## Issue recommendations
| Action | Issue | Issue route | Reason code | Confidence | Title | Public-safe summary |
|---|---|---|---|---|---|---|
| comment-on-roadmap | #13 | `portfolio-roadmap` | `portfolio-weekly-summary` | high | Weekly freshness summary | Keep roadmap current |

## Blocked / approval-gated lanes
- #77, #78, and #80 remain approval-gated unless explicitly moved to `status:plan-approved`.

## Validation evidence
- `uv run pytest tests/test_llm_wiki_weekly_freshness.py tests/test_weekly_freshness_artifacts.py -q`
- `uv run python scripts/validate_weekly_freshness_report.py docs/reports/2026-05-15-llm-wiki-weekly-freshness-report.md`
"""


def test_validator_accepts_valid_report(tmp_path: Path) -> None:
    validator = _load_validator()
    report = tmp_path / "report.md"
    report.write_text(VALID_REPORT, encoding="utf-8")

    assert validator.validate_report(report) == []


def test_validator_rejects_missing_roadmap_anchor(tmp_path: Path) -> None:
    validator = _load_validator()
    report = tmp_path / "report.md"
    report.write_text(VALID_REPORT.replace("https://github.com/vamseeachanta/llm-wiki/issues/13", ""), encoding="utf-8")

    failures = validator.validate_report(report)

    assert any("roadmap anchor" in failure for failure in failures)


def test_validator_rejects_private_paths(tmp_path: Path) -> None:
    validator = _load_validator()
    report = tmp_path / "report.md"
    private_path = "/" + "mnt" + "/" + "ace" + "/private/raw.pdf"
    report.write_text(VALID_REPORT + f"\nForbidden: {private_path}\n", encoding="utf-8")

    failures = validator.validate_report(report)

    assert any("public-safety scan matched" in failure for failure in failures)


def test_validator_rejects_private_paths_in_json_companion(tmp_path: Path) -> None:
    validator = _load_validator()
    report = tmp_path / "2026-05-15-llm-wiki-weekly-freshness-report.md"
    companion = tmp_path / "2026-05-15-llm-wiki-weekly-freshness-report.json"
    report.write_text(VALID_REPORT, encoding="utf-8")
    private_path = "/" + "mnt" + "/" + "ace" + "/private/raw.pdf"
    companion.write_text(
        '{"schema_version":"weekly-freshness/v1","run_date":"2026-05-15","baseline_run_date":"2026-05-15","repo_totals":{"total_pages":1,"missing_frontmatter":0},"domain_freshness":[],"recommendations":[{"issue_route":"portfolio-roadmap","reason_code":"portfolio-weekly-summary","confidence":"high","public_safe_summary":"' + private_path + '"}],"validation":{"tests":"pytest","generate":"generate","validator":"validate"}}',
        encoding="utf-8",
    )

    failures = validator.validate_report(report)

    assert any("JSON companion public-safety scan matched" in failure for failure in failures)


def test_validator_requires_json_companion_schema(tmp_path: Path) -> None:
    validator = _load_validator()
    report = tmp_path / "2026-05-15-llm-wiki-weekly-freshness-report.md"
    companion = tmp_path / "2026-05-15-llm-wiki-weekly-freshness-report.json"
    report.write_text(VALID_REPORT, encoding="utf-8")
    companion.write_text(
        '{"schema_version":"weekly-freshness/v1","run_date":"2026-05-15","baseline_run_date":"2026-05-15","repo_totals":{"total_pages":1,"missing_frontmatter":0},"domain_freshness":[],"totals":{"total_pages":1,"missing_frontmatter":0},"domains":{},"recommendations":[],"validation":{"tests":"pytest","generate":"generate","validator":"validate"}}',
        encoding="utf-8",
    )

    assert validator.validate_report(report) == []
    companion.write_text(
        '{"schema_version":"weekly-freshness/v1","run_date":"2026-05-15","baseline_run_date":"2026-05-15","repo_totals":{},"domain_freshness":[],"totals":{},"domains":{},"recommendations":[],"validation":{"tests":"pytest","generate":"generate","validator":"validate"}}',
        encoding="utf-8",
    )
    failures = validator.validate_report(report)
    assert any("JSON companion missing repo_totals.total_pages" in failure for failure in failures)

