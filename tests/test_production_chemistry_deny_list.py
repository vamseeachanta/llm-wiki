"""Regression test for production-chemistry + SCADA vendor-IP deny-list.

Loads scripts/validate_production_chemistry_deny_list.py via importlib
(per workspace convention; mirrors test_governance_artifacts.py shape) and
asserts `validate(ROOT) == []` against the live wiki content.

Required by PE Phase 4 epic #87 Codex r2 MAJOR-1 (production-chemistry
deny-list) + PE Phase 5 epic #92 r1 MINOR-1 (SCADA + historian + measurement
vendor-IP extension).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_production_chemistry_deny_list.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location(
        "validate_production_chemistry_deny_list", VALIDATOR_PATH
    )
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_validator_module_loads() -> None:
    validator = _load_validator()
    assert hasattr(validator, "validate")
    assert hasattr(validator, "ALL_PATTERNS")
    assert len(validator.ALL_PATTERNS) > 0


def test_no_deny_list_violations_in_wiki_content() -> None:
    """Wiki concepts + standards must contain zero production-chemistry / SCADA proprietary-IP patterns."""
    validator = _load_validator()
    violations = validator.validate(ROOT)
    assert violations == [], (
        f"Found {len(violations)} deny-list violation(s) in wiki content:\n\n"
        + "\n\n".join(violations)
    )


def test_validator_excludes_plans_and_reviews() -> None:
    """Plans and review files legitimately discuss deny-list patterns as anti-patterns; scanner must skip them."""
    validator = _load_validator()
    files = validator._content_files(ROOT)
    paths = [str(f.relative_to(ROOT)) for f in files]
    assert not any("docs/plans/" in p for p in paths), "Validator must not scan docs/plans/"
    assert not any("scripts/review/" in p for p in paths), "Validator must not scan scripts/review/"
    assert not any(".planning/" in p for p in paths), "Validator must not scan .planning/"
    assert all("wikis/" in p for p in paths), "Validator must scan only wikis/"


def test_pattern_categories_present() -> None:
    """Confirm both Phase 4 (production-chemistry) and Phase 5 (SCADA) pattern categories are loaded."""
    validator = _load_validator()
    names = {p.name for p in validator.ALL_PATTERNS}
    # Phase 4 production-chemistry markers
    assert "champion-x-sku" in names
    assert "nalco-sku" in names
    assert "halliburton-multichem-sku" in names
    assert "baker-hughes-productionquest-sku" in names
    assert "performance-curve-percent-at-dosage" in names
    assert "ldhi-subcooling-vendor-specific" in names
    # Phase 5 SCADA markers
    assert "pi-namespace-specific-convention" in names
    assert "opc-ua-proprietary-node-id" in names
    assert "historian-binary-layout-internal" in names
    assert "swinging-door-specific-tolerance" in names
    # Phase 4 simulator markers
    assert "multiphase-simulator-algorithm-internal" in names
