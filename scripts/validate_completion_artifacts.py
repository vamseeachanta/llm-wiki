#!/usr/bin/env python3
"""Validate public-safe llm-wiki practical-completion control-plane artifacts.

The validator checks only committed markdown control artifacts. It intentionally
avoids raw archives and rejects private raw path leakage beyond explicit safe
root labels used in governance prose.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

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

FORBIDDEN_PATTERN = re.compile(
    "|".join(FORBIDDEN_TERMS + RAW_ROOT_PATTERNS),
    re.IGNORECASE,
)


@dataclass(frozen=True)
class CompletionArtifactSpec:
    path: str
    required_phrases: tuple[str, ...]
    required_issue_links: tuple[str, ...]
    required_repo_links: tuple[str, ...] = ()


SPECS: tuple[CompletionArtifactSpec, ...] = (
    CompletionArtifactSpec(
        path="docs/reports/2026-05-11-llm-wiki-completion-control-plane.md",
        required_phrases=(
            "Raw/private boundary",
            "Historic GitHub issue portfolio",
            "Tier-1 ecosystem linkage",
            "Completion lanes",
            "Codex spend-forward lanes",
            "No duplicate umbrella issue",
            "Practical completion definition",
            "Blocked pending approval/clearance",
            "Safe to execute now",
            "Do not copy raw/vendor/client content",
        ),
        required_issue_links=(
            "https://github.com/vamseeachanta/llm-wiki/issues/13",
            "https://github.com/vamseeachanta/llm-wiki/issues/19",
            "https://github.com/vamseeachanta/llm-wiki/issues/40",
            "https://github.com/vamseeachanta/llm-wiki/issues/43",
            "https://github.com/vamseeachanta/llm-wiki/issues/48",
        ),
        required_repo_links=(
            "https://github.com/vamseeachanta/workspace-hub",
            "https://github.com/vamseeachanta/digitalmodel",
            "https://github.com/vamseeachanta/assetutilities",
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/llm-wiki",
            "https://github.com/vamseeachanta/assethold",
            "https://github.com/vamseeachanta/aceengineer-website",
            "https://github.com/vamseeachanta/aceengineer-strategy",
        ),
    ),
    CompletionArtifactSpec(
        path="docs/reports/2026-05-11-tier1-ecosystem-link-map.md",
        required_phrases=(
            "Data layer",
            "Software layer",
            "Results layer",
            "Wiki exposure rule",
            "Public-safe link targets",
            "GTM/private boundary",
            "Do not copy raw/vendor/client content",
        ),
        required_issue_links=(
            "https://github.com/vamseeachanta/llm-wiki/issues/13",
            "https://github.com/vamseeachanta/llm-wiki/issues/19",
        ),
        required_repo_links=(
            "https://github.com/vamseeachanta/workspace-hub",
            "https://github.com/vamseeachanta/digitalmodel",
            "https://github.com/vamseeachanta/assetutilities",
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/llm-wiki",
            "https://github.com/vamseeachanta/assethold",
            "https://github.com/vamseeachanta/aceengineer-website",
            "https://github.com/vamseeachanta/aceengineer-strategy",
        ),
    ),
    CompletionArtifactSpec(
        path="docs/reports/2026-05-11-safe-source-family-aggregate-scan.md",
        required_phrases=(
            "Safe Source-Family Aggregate Scan",
            "Families scanned",
            "Files counted",
            "Bytes counted",
            "Top extension buckets",
            "Safety Contract",
            "does not open file contents",
            "does not emit full paths",
        ),
        required_issue_links=(),
    ),
    CompletionArtifactSpec(
        path="docs/reports/2026-05-11-tier1-practical-completeness-gap-report.md",
        required_phrases=(
            "Repo-by-repo authoritative targets",
            "Data/software/results layer map",
            "Wiki cross-link gaps addressed now",
            "Public/private/GTM boundary",
            "Safe next artifacts and validation checklist",
            "No raw archive subpaths",
        ),
        required_issue_links=(
            "#20/#21/#27/#28/#29/#30/#38/#39",
            "#40/#41/#42",
        ),
        required_repo_links=(
            "https://github.com/vamseeachanta/workspace-hub",
            "https://github.com/vamseeachanta/digitalmodel",
            "https://github.com/vamseeachanta/assetutilities",
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/llm-wiki",
            "https://github.com/vamseeachanta/assethold",
            "https://github.com/vamseeachanta/aceengineer-website",
            "https://github.com/vamseeachanta/aceengineer-strategy",
        ),
    ),
    CompletionArtifactSpec(
        path="wikis/cross-links-tier1.md",
        required_phrases=(
            "Tier-1 Code/Data/Results Cross-Links",
            "Engineering Methods",
            "Data Sources",
            "Utility/Extraction Stack",
            "Asset Lifecycle",
            "Public Results/Demos",
            "Operational rule",
        ),
        required_issue_links=(),
        required_repo_links=(
            "https://github.com/vamseeachanta/workspace-hub",
            "https://github.com/vamseeachanta/digitalmodel",
            "https://github.com/vamseeachanta/assetutilities",
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/llm-wiki",
            "https://github.com/vamseeachanta/assethold",
            "https://github.com/vamseeachanta/aceengineer-website",
            "https://github.com/vamseeachanta/aceengineer-strategy",
        ),
    ),
    CompletionArtifactSpec(
        path="wikis/marine-engineering/wiki/code-results-links.md",
        required_phrases=(
            "Marine Engineering Code and Results Links",
            "Implementation anchors",
            "Result/demo anchors",
            "Link-back targets",
        ),
        required_issue_links=(),
        required_repo_links=(
            "https://github.com/vamseeachanta/digitalmodel",
            "https://github.com/vamseeachanta/aceengineer-website",
        ),
    ),
    CompletionArtifactSpec(
        path="wikis/engineering/wiki/public-data-software-links.md",
        required_phrases=(
            "Engineering Public Data and Software Links",
            "Data provenance anchors",
            "Software utility anchors",
            "Exposure contract",
        ),
        required_issue_links=(),
        required_repo_links=(
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/assetutilities",
        ),
    ),
    CompletionArtifactSpec(
        path="wikis/asset-management/wiki/software-and-method-links.md",
        required_phrases=(
            "Asset Management Software and Method Links",
            "Method/software anchors",
            "Boundary",
        ),
        required_issue_links=(),
        required_repo_links=(
            "https://github.com/vamseeachanta/assethold",
            "https://github.com/vamseeachanta/worldenergydata",
            "https://github.com/vamseeachanta/aceengineer-website",
        ),
    ),
)


def validate(root: Path) -> list[str]:
    """Return validation failures for completion control-plane artifacts."""
    failures: list[str] = []
    for spec in SPECS:
        artifact = root / spec.path
        if not artifact.exists():
            failures.append(f"missing {spec.path}")
            continue
        text = artifact.read_text(encoding="utf-8")
        for phrase in spec.required_phrases:
            if phrase not in text:
                failures.append(f"{spec.path}: missing phrase {phrase!r}")
        for link in spec.required_issue_links:
            if link not in text:
                failures.append(f"{spec.path}: missing issue link {link}")
        for link in spec.required_repo_links:
            if link not in text:
                failures.append(f"{spec.path}: missing repo link {link}")
        scannable_text = "\n".join(
            line for line in text.splitlines()
            if "safe root label" not in line.lower()
            and "Root label" not in line
        )
        if FORBIDDEN_PATTERN.search(scannable_text):
            failures.append(f"{spec.path}: public-safety scan matched forbidden secret/private-path pattern")
    return failures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = validate(root)
    if failures:
        print("completion artifact validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"completion artifact validation passed: {len(SPECS)} artifacts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
