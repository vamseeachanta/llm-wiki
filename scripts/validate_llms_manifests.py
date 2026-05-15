#!/usr/bin/env python3
"""Validate llms.txt AI-agent entrypoint manifests.

The validator is intentionally narrow and deterministic. It checks only curated
repo-local manifests, not raw source trees or external links.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

REQUIRED_SECTIONS: tuple[str, ...] = (
    "Purpose",
    "Safety Boundary",
    "Start Here",
    "Key Entry Paths",
    "How To Find X",
    "Do Not Scan Blindly",
    "Related Surfaces",
    "Last Updated",
)

FORBIDDEN_PATTERN = re.compile(
    "|".join(
        (
            "BE" + "GIN " + r"(?:RSA|OPENSSH|PRIVATE) " + "KEY",
            "pass" + r"word\s*=",
            "sec" + r"ret\s*=",
            "api" + r"[_-]?key\s*=",
            "social " + "security",
            r"\b" + "SS" + r"N\b",
            "bank " + "account",
            r"(?:/home|/mnt|/tmp|/var|/etc)/[^\s)`]+",
            "/" + "mnt" + "/" + "ace" + r"/(?!\s|`|$)",
            "/" + "mnt" + "/" + "ace-data" + r"/(?!\s|`|$)",
            r"wikis/[^\s)]+/raw/",
        )
    ),
    re.IGNORECASE,
)

MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
CODE_PATH_PATTERN = re.compile(r"`([^`]+)`")
ROUTE_PATTERN = re.compile(r"^-\s*([^:\n]+):\s*\[[^\]]+\]\(([^)]+)\)", re.MULTILINE)
REPO_PATH_PREFIXES = ("wikis/", "docs/", "scripts/", "tests/", "llms.txt", "README.md")


@dataclass(frozen=True)
class ManifestSpec:
    path: str
    required_phrases: tuple[str, ...]
    max_markdown_links: int


MANIFESTS: tuple[ManifestSpec, ...] = (
    ManifestSpec(
        path="llms.txt",
        required_phrases=(
            "Public/private boundary",
            "wikis/marine-engineering/llms.txt",
            "wikis/engineering/llms.txt",
            "wikis/engineering-standards/llms.txt",
            "docs/governance/service-provider-data-routing.md",
            "wikis/cross-links-tier1.md",
        ),
        max_markdown_links=45,
    ),
    ManifestSpec(
        path="wikis/marine-engineering/llms.txt",
        required_phrases=(
            "19k",
            "Do not scan blindly",
            "wikis/marine-engineering/wiki/portal.md",
            "wikis/marine-engineering/wiki/code-results-links.md",
        ),
        max_markdown_links=55,
    ),
    ManifestSpec(
        path="wikis/engineering/llms.txt",
        required_phrases=(
            "methodology",
            "wikis/engineering/wiki/public-data-software-links.md",
            "wikis/engineering/wiki/overview.md",
        ),
        max_markdown_links=45,
    ),
    ManifestSpec(
        path="wikis/engineering-standards/llms.txt",
        required_phrases=(
            "metadata-first standards navigation",
            "Do not quote or reconstruct",
            "wikis/engineering-standards/wiki/overview.md",
        ),
        max_markdown_links=55,
    ),
)


def _manifest_links(text: str) -> list[str]:
    return [link.strip() for link in MARKDOWN_LINK_PATTERN.findall(text)]


def _is_repo_relative_link(link: str) -> bool:
    if link.startswith(("http://", "https://", "mailto:", "#")):
        return False
    return not link.startswith("/") and "://" not in link


def _manifest_code_paths(text: str) -> list[str]:
    """Return code-span values that look like repo-relative paths."""
    paths: list[str] = []
    for value in CODE_PATH_PATTERN.findall(text):
        cleaned = value.strip()
        if "<" in cleaned or ">" in cleaned:
            continue
        if cleaned.startswith(REPO_PATH_PREFIXES):
            paths.append(cleaned)
    return paths


def _section_positions(text: str) -> dict[str, int]:
    positions: dict[str, int] = {}
    for section in REQUIRED_SECTIONS:
        match = re.search(rf"^## {re.escape(section)}\s*$", text, flags=re.MULTILINE)
        if match:
            positions[section] = match.start()
    return positions


def validate_existing_targets(root: Path) -> list[str]:
    """Return failures for manifest links and path references inside the repo."""
    failures: list[str] = []
    for spec in MANIFESTS:
        manifest_path = root / spec.path
        if not manifest_path.exists():
            failures.append(f"missing manifest {spec.path}")
            continue
        text = manifest_path.read_text(encoding="utf-8")
        for link in _manifest_links(text):
            target = link.split("#", 1)[0]
            if not target or not _is_repo_relative_link(target):
                continue
            resolved_target = (manifest_path.parent / target).resolve()
            try:
                resolved_target.relative_to(root.resolve())
            except ValueError:
                failures.append(f"{spec.path}: linked target escapes repo {target}")
                continue
            if not resolved_target.exists():
                failures.append(f"{spec.path}: missing linked target {target}")
        for target in _manifest_code_paths(text):
            resolved_target = (root / target).resolve()
            try:
                resolved_target.relative_to(root.resolve())
            except ValueError:
                failures.append(f"{spec.path}: code-path target escapes repo {target}")
                continue
            if not resolved_target.exists():
                failures.append(f"{spec.path}: missing code-path target {target}")
    return failures


def extract_routing_targets(manifest_path: Path) -> dict[str, str]:
    """Extract simple root-manifest intent routes from the How To Find X list."""
    text = manifest_path.read_text(encoding="utf-8")
    return {intent.strip().lower(): target.strip() for intent, target in ROUTE_PATTERN.findall(text)}


def validate(root: Path) -> list[str]:
    """Return validation failures for llms.txt manifests."""
    failures: list[str] = []
    for spec in MANIFESTS:
        manifest = root / spec.path
        if not manifest.exists():
            failures.append(f"missing manifest {spec.path}")
            continue
        text = manifest.read_text(encoding="utf-8")
        positions = _section_positions(text)
        for section in REQUIRED_SECTIONS:
            if section not in positions:
                failures.append(f"{spec.path}: missing required section {section!r}")
        ordered_positions = [positions[section] for section in REQUIRED_SECTIONS if section in positions]
        if ordered_positions != sorted(ordered_positions):
            failures.append(f"{spec.path}: required sections are not in contract order")
        for phrase in spec.required_phrases:
            if phrase not in text:
                failures.append(f"{spec.path}: missing phrase {phrase!r}")
        if FORBIDDEN_PATTERN.search(text):
            failures.append(f"{spec.path}: public-safety scan matched forbidden secret/private-path pattern")
        link_count = len(_manifest_links(text))
        if link_count > spec.max_markdown_links:
            failures.append(f"{spec.path}: too many markdown links ({link_count} > {spec.max_markdown_links})")
    failures.extend(validate_existing_targets(root))
    return failures


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    failures = validate(root)
    if failures:
        print("llms manifest validation failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(f"llms manifest validation passed: {len(MANIFESTS)} manifests")
    return 0


if __name__ == "__main__":
    sys.exit(main())
