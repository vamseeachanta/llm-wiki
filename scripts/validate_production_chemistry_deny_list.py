#!/usr/bin/env python3
"""Scan llm-wiki content for production-chemistry + SCADA proprietary-IP deny-list patterns.

This validator enforces the vendor-IP discipline established by:
- PE Phase 4 epic #87 Codex r2 MAJOR-1 (production-chemistry commercial-product / dosage / performance-curve deny-list)
- PE Phase 5 epic #92 r1 MINOR-1 (SCADA + historian + measurement vendor-IP extension)

Discrimination criterion: GENERAL framing (vendor name + chemistry-class /
capability) = ALLOWED; SPECIFIC quantitative claims tied to commercial products
(vendor + SKU pattern + dosage / performance-curve transcription) = BLOCKED.

The validator scans wikis/<domain>/wiki/concepts/*.md and wikis/<domain>/wiki/standards/*.md
ONLY — plans (docs/plans/), reviews (scripts/review/results/), markers
(.planning/plan-approved/), governance docs (docs/governance/), and tests
themselves are intentionally OUT OF SCOPE because they legitimately discuss
deny-list patterns as anti-pattern examples.

Usage:
    python3 scripts/validate_production_chemistry_deny_list.py
    OR
    pytest tests/test_production_chemistry_deny_list.py
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DenyPattern:
    name: str
    pattern: re.Pattern[str]
    description: str
    rationale: str


def _compile(pattern: str, flags: int = re.IGNORECASE | re.MULTILINE) -> re.Pattern[str]:
    return re.compile(pattern, flags)


PRODUCTION_CHEMISTRY_SKU_PATTERNS: tuple[DenyPattern, ...] = (
    DenyPattern(
        name="champion-x-sku",
        pattern=_compile(r"\bChampion-?X\s+(?:XS|XSP|FW|EC|CP|AS|HI)[-_]?\d{3,5}\b"),
        description="Champion-X commercial-product SKU pattern",
        rationale="Per Phase 4 #87 Codex MAJOR-1: vendor name + commercial SKU (e.g. 'Champion-X XS-7000') leaks proprietary product identity; cite vendor + chemistry class only.",
    ),
    DenyPattern(
        name="nalco-sku",
        pattern=_compile(r"\bNalco(?:\s+Champion)?\s+(?:EC|EX|CP|XS|FW|VX)[-_]?\d{3,5}\b"),
        description="Nalco / Nalco Champion commercial-product SKU pattern",
        rationale="Per Phase 4 #87 Codex MAJOR-1: cite Nalco / Nalco Champion (Ecolab) + chemistry class only; never specific product codes.",
    ),
    DenyPattern(
        name="halliburton-multichem-sku",
        pattern=_compile(r"\b(?:Halliburton|MultiChem)\s+(?:MC|HC|MX)[-_]?\d{3,5}\b"),
        description="Halliburton MultiChem commercial-product SKU pattern",
        rationale="Per Phase 4 #87 Codex MAJOR-1: cite Halliburton MultiChem at service-line level only; no product codes.",
    ),
    DenyPattern(
        name="baker-hughes-productionquest-sku",
        pattern=_compile(r"\bBaker\s+Hughes\s+ProductionQuest[-_\s]?[A-Z]?\d{1,4}\b"),
        description="Baker Hughes ProductionQuest commercial-product SKU pattern",
        rationale="Per Phase 4 #87 Codex MAJOR-1: cite Baker Hughes ProductionQuest at service-line level only; no product codes.",
    ),
)


PRODUCTION_CHEMISTRY_PERFORMANCE_PATTERNS: tuple[DenyPattern, ...] = (
    DenyPattern(
        name="performance-curve-percent-at-dosage",
        pattern=_compile(
            r"\bachieves?\s+\d+(?:\.\d+)?\s*%\s+(?:[\w-]+\s+){1,4}at\s+\d+(?:\.\d+)?\s*(?:ppm|wt\s*%|wppm)"
        ),
        description="Quantitative inhibitor performance claim tied to specific dosage",
        rationale="Per Phase 4 #87 Codex MAJOR-1: 'achieves X% inhibition at Y ppm' reproduces vendor performance-curve content; describe inhibitor mechanism qualitatively instead.",
    ),
    DenyPattern(
        name="ldhi-subcooling-vendor-specific",
        pattern=_compile(
            r"\b(?:KHI|LDHI|AA)\s+(?:provides?|achieves?)\s+subcooling\s+(?:protection\s+)?(?:to|of)\s+(?:ΔT|delta[-\s]T)\s*=?\s*\d+(?:\.\d+)?\s*°?\s*C\s+at\s+\d+(?:\.\d+)?\s*(?:ppm|wt\s*%)"
        ),
        description="Vendor-tied LDHI subcooling-protection performance claim",
        rationale="Per Phase 4 #87 Codex MAJOR-1: 'KHI provides subcooling to ΔT = 10°C at 0.5 wt%' is vendor-specific kinetic-inhibitor performance; describe LDHI as a class.",
    ),
)


SCADA_PROPRIETARY_INTERNALS_PATTERNS: tuple[DenyPattern, ...] = (
    DenyPattern(
        name="pi-namespace-specific-convention",
        pattern=_compile(
            r"\bPI\s+(?:AF\s+)?(?:tag\s+)?(?:namespace|naming)\s+convention\s+[A-Z][A-Z0-9_\-]{2,}"
        ),
        description="Specific PI / PI AF namespace / tag-naming convention identifier",
        rationale="Per Phase 5 #92 MINOR-1: PI tag-naming schemas are operator-or-vendor proprietary; cite PI as a platform only.",
    ),
    DenyPattern(
        name="opc-ua-proprietary-node-id",
        pattern=_compile(
            r"\bOPC[-\s]?UA\s+(?:node[-\s]?id|address[-\s]?space)\s+(?:schema\s+)?[A-Z][A-Z0-9_\-]{2,}"
        ),
        description="Proprietary OPC-UA node-id / address-space schema identifier",
        rationale="Per Phase 5 #92 MINOR-1: cite OPC-UA as an open protocol only; do not transcribe vendor proprietary node-id structures.",
    ),
    DenyPattern(
        name="historian-binary-layout-internal",
        pattern=_compile(
            r"\b(?:PI|Uniformance(?:\s+PHD)?|InfoPlus(?:\.21)?|Proficy(?:\s+Historian)?|AVEVA\s+Historian|Wonderware\s+Historian)\s+(?:archive|historian)\s+(?:file[-\s]?format|binary[-\s]?layout)\s+internal"
        ),
        description="Historian-archive proprietary binary-layout / file-format internal reference",
        rationale="Per Phase 5 #92 MINOR-1: historian archive formats are vendor proprietary; describe at capability-class level only.",
    ),
    DenyPattern(
        name="swinging-door-specific-tolerance",
        pattern=_compile(
            r"\bswinging[-\s]door\s+(?:compression\s+)?tolerance\s+\d+(?:\.\d+)?\s*%?\s+(?:at\s+|bandwidth\s+|deadband\s+)\d"
        ),
        description="Specific swinging-door compression tolerance parameter (vendor-internal tuning)",
        rationale="Per Phase 5 #92 MINOR-1: swinging-door compression is a public algorithm class (Bristol 1990), but specific tolerance + bandwidth tuning values come from vendor-internal tuning guidance.",
    ),
    DenyPattern(
        name="rslogix-aoi-internal",
        pattern=_compile(r"\b(?:RSLogix|Allen[-\s]?Bradley)\s+AOI\s+internal"),
        description="RSLogix / Allen-Bradley AOI vendor-internal structure reference",
        rationale="Per Phase 5 #92 MINOR-1: Add-On Instruction internals are Rockwell proprietary; cite the IEC 61131-3 framework class only.",
    ),
    DenyPattern(
        name="modicon-firmware-version-internal",
        pattern=_compile(r"\bModicon\s+firmware\s+(?:internal\s+)?(?:v|version)?\s*\d+\.\d+\s+internal"),
        description="Modicon firmware version-specific internal reference",
        rationale="Per Phase 5 #92 MINOR-1: Modicon firmware internals are Schneider proprietary; cite at platform class only.",
    ),
)


SIMULATOR_INTERNALS_PATTERNS: tuple[DenyPattern, ...] = (
    DenyPattern(
        name="multiphase-simulator-algorithm-internal",
        pattern=_compile(
            r"\b(?:OLGA|LedaFlow|PIPESIM|K[-\s]?Spice|MEPO|FlowManager)\s+(?:algorithm|model|formulation|equation|kernel)\s+(?:internal|proprietary)"
        ),
        description="Multiphase-flow simulator algorithm / formulation / kernel internal reference",
        rationale="Per Phase 4 #87 Codex MAJOR-3 + Phase 5 carry-forward: industry-standard multiphase-flow simulators (OLGA, LedaFlow, PIPESIM, K-Spice) cited by name only; algorithm internals not reproduced.",
    ),
    DenyPattern(
        name="multiphase-simulator-proprietary-formulation",
        pattern=_compile(
            r"\b(?:OLGA|LedaFlow|PIPESIM|K[-\s]?Spice)\s+proprietary\s+(?:formulation|equation|kernel|model)"
        ),
        description="Explicit 'proprietary formulation' reference for named simulator",
        rationale="Per Phase 4 #87 Codex MAJOR-3: simulator content is consistently cite-by-name only.",
    ),
)


ALL_PATTERNS: tuple[DenyPattern, ...] = (
    *PRODUCTION_CHEMISTRY_SKU_PATTERNS,
    *PRODUCTION_CHEMISTRY_PERFORMANCE_PATTERNS,
    *SCADA_PROPRIETARY_INTERNALS_PATTERNS,
    *SIMULATOR_INTERNALS_PATTERNS,
)


def _content_files(root: Path) -> list[Path]:
    """Return wiki concept + standards .md files only (not plans, reviews, markers, governance)."""
    wikis_root = root / "wikis"
    if not wikis_root.is_dir():
        return []
    files: list[Path] = []
    for domain in sorted(wikis_root.iterdir()):
        if not domain.is_dir():
            continue
        for subdir in ("concepts", "standards"):
            target = domain / "wiki" / subdir
            if target.is_dir():
                files.extend(sorted(target.glob("*.md")))
    return files


def validate(root: Path) -> list[str]:
    """Return list of violation messages; empty list = clean.

    Each violation message is a multi-line string with:
    - Pattern name
    - File:line reference
    - Matched text excerpt
    - Rationale
    """
    violations: list[str] = []
    files = _content_files(root)
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        lines = text.splitlines()
        for deny in ALL_PATTERNS:
            for line_no, line in enumerate(lines, 1):
                match = deny.pattern.search(line)
                if match:
                    rel = f.relative_to(root)
                    excerpt = line.strip()[:200]
                    violations.append(
                        f"[{deny.name}] {rel}:{line_no}\n"
                        f"    match: {match.group(0)!r}\n"
                        f"    line: {excerpt}\n"
                        f"    rationale: {deny.rationale}"
                    )
    return violations


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    files = _content_files(root)
    violations = validate(root)
    domains = sum(1 for d in (root / "wikis").iterdir() if d.is_dir())
    print(
        f"Scanned {len(files)} wiki content files across {domains} domains "
        f"with {len(ALL_PATTERNS)} deny-list patterns."
    )
    if violations:
        print(f"\nFAIL — {len(violations)} violation(s):\n")
        for v in violations:
            print(v)
            print()
        return 1
    print("\nPASS — no deny-list violations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
