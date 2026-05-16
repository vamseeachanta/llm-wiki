#!/usr/bin/env python3
"""Validate weekly llm-wiki freshness report artifacts."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = (
    "# llm-wiki weekly freshness report",
    "## Run metadata",
    "## Repo freshness summary",
    "## Domain coverage deltas",
    "## Stale pages and structural findings",
    "## Concept watchlist",
    "## Issue recommendations",
    "## Blocked / approval-gated lanes",
    "## Validation evidence",
)
ROADMAP_URL = "https://github.com/vamseeachanta/llm-wiki/issues/13"

RAW_ROOT_PATTERNS = (
    "/" + "mnt" + "/" + "ace" + r"/(?!\s|`|$)",
    "/" + "mnt" + "/" + "ace-data" + r"/(?!\s|`|$)",
)
FORBIDDEN_TERMS = (
    "BE" + "GIN " + r"(?:RSA|OPENSSH|PRIVATE) " + "KEY",
    "pass" + r"word\s*=",
    "sec" + r"ret\s*=",
    "api" + r"[_-]?key\s*=",
    "social " + "security",
    r"\b" + "SS" + r"N\b",
    "bank " + "account",
)
FORBIDDEN_PATTERN = re.compile("|".join(FORBIDDEN_TERMS + RAW_ROOT_PATTERNS), re.IGNORECASE)


def companion_candidates(report_path: Path) -> list[Path]:
    date_prefix = report_path.name.split("-llm-wiki-weekly-freshness-report.md", 1)[0]
    return [
        report_path.with_suffix(".json"),
        report_path.parents[1] / "artifacts" / "freshness" / f"{date_prefix}-weekly-freshness-summary.json",
        report_path.parents[2] / "artifacts" / "freshness" / f"{date_prefix}-weekly-freshness-summary.json" if len(report_path.parents) > 2 else report_path.with_suffix(".json"),
    ]


def _validate_json_schema(path: Path) -> list[str]:
    failures: list[str] = []
    try:
        raw_text = path.read_text(encoding="utf-8")
        data = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        return [f"JSON companion is invalid JSON: {exc}"]
    match = FORBIDDEN_PATTERN.search(raw_text)
    if match:
        failures.append(f"JSON companion public-safety scan matched forbidden text: {match.group(0)!r}")
    for field in ("schema_version", "run_date", "baseline_run_date", "repo_totals", "domain_freshness", "recommendations", "validation"):
        if field not in data:
            failures.append(f"JSON companion missing {field}")
    totals = data.get("repo_totals", {})
    if "total_pages" not in totals:
        failures.append("JSON companion missing repo_totals.total_pages")
    if "missing_frontmatter" not in totals:
        failures.append("JSON companion missing repo_totals.missing_frontmatter")
    if not isinstance(data.get("domain_freshness", []), list):
        failures.append("JSON companion domain_freshness must be a list")
    validation = data.get("validation", {})
    for field in ("tests", "generate", "validator"):
        if field not in validation:
            failures.append(f"JSON companion validation missing {field}")
    for rec in data.get("recommendations", []):
        for field in ("issue_route", "reason_code", "confidence", "public_safe_summary"):
            if field not in rec:
                failures.append(f"JSON companion recommendation missing {field}")
                break
    return failures


def validate_report(report_path: Path) -> list[str]:
    failures: list[str] = []
    if not report_path.exists():
        return [f"missing report {report_path}"]
    text = report_path.read_text(encoding="utf-8", errors="replace")
    for section in REQUIRED_SECTIONS:
        if section not in text:
            failures.append(f"missing required section: {section}")
    if ROADMAP_URL not in text:
        failures.append("missing roadmap anchor issue link")
    if "public-safe" not in text.lower():
        failures.append("missing public-safe language")
    match = FORBIDDEN_PATTERN.search(text)
    if match:
        failures.append(f"public-safety scan matched forbidden text: {match.group(0)!r}")
    companions = [path for path in companion_candidates(report_path.resolve()) if path.exists()]
    if companions:
        failures.extend(_validate_json_schema(companions[0]))
    return failures


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if len(args) != 1:
        print("usage: validate_weekly_freshness_report.py <report.md>", file=sys.stderr)
        return 2
    failures = validate_report(Path(args[0]))
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print(f"OK: {args[0]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
