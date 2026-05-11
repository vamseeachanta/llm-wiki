#!/usr/bin/env python3
"""Validate approved llm-wiki governance/input-readiness artifacts.

This validator is intentionally deterministic and narrow: it checks only the
public-safe docs artifacts approved for issues #43-#48. It does not inspect raw
source trees and does not require network access.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

SECRET_PATTERN = re.compile(
    r"BEGIN (?:RSA|OPENSSH|PRIVATE) KEY|"
    r"password\s*=|secret\s*=|api[_-]?key\s*=|"
    r"social security|\bSSN\b|bank account|"
    r"/mnt/ace(?:/|\b)|/mnt/ace-data(?:/|\b)",
    re.IGNORECASE,
)

REQUIRED_COMMON_PHRASES = [
    "Raw/private boundary",
    "Required clearance/input-readiness fields",
    "Allowed evidence/output types",
    "Disallowed evidence/output types",
    "Future implementation issue template",
    "Validation checklist",
    "Parent issue update requirement",
    "parent remains blocked",
    "Do not read, copy, OCR, summarize, or ingest raw source files",
]


@dataclass(frozen=True)
class ArtifactSpec:
    issue: int
    path: str
    parent_issue: int
    source_family: str
    required_fields: tuple[str, ...]


SPECS: tuple[ArtifactSpec, ...] = (
    ArtifactSpec(
        43,
        "docs/governance/sesa-extraction-clearance-checklist.md",
        14,
        "SESA FLNG Terminal / DORIS 62092_sesa",
        (
            "candidate artifact id",
            "source-family label only",
            "proposed public output type",
            "evidence type",
            "license/copyright class",
            "client/project sensitivity class",
            "standards-derived flag",
            "approval owner/date",
            "allowed/disallowed fields",
            "validator result",
        ),
    ),
    ArtifactSpec(
        44,
        "docs/governance/bsee-source-family-clearance-checklist.md",
        19,
        "BSEE/offshore source metadata and summary candidates",
        (
            "candidate artifact id",
            "public source citation or source-family label",
            "data sensitivity class",
            "client/project sensitivity class",
            "allowed metadata fields",
            "disallowed extracted fields",
            "archive/spreadsheet flag",
            "approval owner/date",
            "target wiki domain/page type",
            "validator result",
        ),
    ),
    ArtifactSpec(
        45,
        "docs/governance/hse-dataset-clearance-checklist.md",
        19,
        "HSE/safety dataset metadata and wiki candidates",
        (
            "dataset/artifact id",
            "dataset citation/source-family label",
            "aggregation level",
            "PII/sensitive incident flag",
            "raw-row exclusion proof",
            "allowed aggregate/public metadata",
            "disallowed row-level fields",
            "approval owner/date",
            "target wiki page type",
            "secret/PII scan result",
        ),
    ),
    ArtifactSpec(
        46,
        "docs/governance/frontier-deepwater-clearance-checklist.md",
        19,
        "Frontier Deepwater/offshore operations source candidates",
        (
            "candidate artifact id",
            "bibliographic/public citation",
            "copyright class",
            "image/figure flag",
            "archive flag",
            "allowed metadata fields",
            "allowed authored synthesis scope",
            "disallowed copied text/figures",
            "approval owner/date",
            "validator result",
        ),
    ),
    ArtifactSpec(
        47,
        "docs/governance/batch-pack-1-input-readiness.md",
        25,
        "Batch Pack 1 repo-qualified plan ref",
        (
            "approved plan artifact path or replacement approval",
            "registry/subset artifact path",
            "source SHA/provenance",
            "drift check result",
            "duplicate-check command",
            "generated output path contract",
            "public/raw boundary check",
            "future issue 25 execution command for vamseeachanta/llm-wiki#25",
            "approval owner/date",
        ),
    ),
    ArtifactSpec(
        48,
        "docs/governance/batch-pack-4-input-readiness.md",
        26,
        "Batch Pack 4 repo-qualified plan ref",
        (
            "approved plan artifact path or replacement approval",
            "transfer ledger artifact path",
            "topic-cluster artifact path",
            "alias input artifact path",
            "source SHA/provenance",
            "drift check result",
            "duplicate/extend-vs-create check",
            "public/raw/vendor boundary check",
            "future issue 26 execution command for vamseeachanta/llm-wiki#26",
            "approval owner/date",
        ),
    ),
)


def validate(root: Path) -> list[str]:
    failures: list[str] = []
    for spec in SPECS:
        artifact = root / spec.path
        if not artifact.exists():
            failures.append(f"#{spec.issue}: missing {spec.path}")
            continue
        text = artifact.read_text(encoding="utf-8")
        for phrase in REQUIRED_COMMON_PHRASES:
            if phrase not in text:
                failures.append(f"#{spec.issue}: missing common phrase {phrase!r}")
        required_links = [f"vamseeachanta/llm-wiki#{spec.issue}", f"vamseeachanta/llm-wiki#{spec.parent_issue}"]
        frontmatter_issues = f"issues: [vamseeachanta/llm-wiki#{spec.issue}, vamseeachanta/llm-wiki#{spec.parent_issue}]"
        if frontmatter_issues not in text:
            failures.append(f"#{spec.issue}: frontmatter issues must be {frontmatter_issues!r}")
        for link in required_links:
            if link not in text:
                failures.append(f"#{spec.issue}: missing repo-qualified issue link {link}")
        if spec.source_family not in text:
            failures.append(f"#{spec.issue}: missing source family {spec.source_family!r}")
        for field in spec.required_fields:
            if field not in text:
                failures.append(f"#{spec.issue}: missing required field {field!r}")
        if f"Checklist artifact: `{spec.path}`" not in text:
            failures.append(f"#{spec.issue}: missing checklist artifact path {spec.path}")
        if f"TOUCHED='{spec.path}'" not in text:
            failures.append(f"#{spec.issue}: validation command does not target {spec.path}")
        scannable_text = "\n".join(
            line for line in text.splitlines()
            if "grep -RInE" not in line and "api[_-]?key" not in line
        )
        if SECRET_PATTERN.search(scannable_text):
            failures.append(f"#{spec.issue}: public-safety scan matched forbidden secret/private-path pattern")
    return failures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = validate(root)
    if failures:
        print("governance artifact validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"governance artifact validation passed: {len(SPECS)} artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
