"""Regression tests for llm-wiki governance/input-readiness artifacts."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_governance_artifacts.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_governance_artifacts", VALIDATOR_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_governance_artifacts_validate_successfully() -> None:
    validator = _load_validator()

    assert validator.validate(ROOT) == []


def test_validation_commands_reference_real_artifact_paths() -> None:
    validator = _load_validator()

    for spec in validator.SPECS:
        text = (ROOT / spec.path).read_text(encoding="utf-8")
        assert f"Checklist artifact: `{spec.path}`" in text
        assert f"TOUCHED='{spec.path}'" in text


def _copy_governance_artifacts(tmp_path: Path, validator) -> None:
    for spec in validator.SPECS:
        source = ROOT / spec.path
        target = tmp_path / spec.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def test_validator_rejects_forbidden_raw_archive_paths(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_governance_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    first.write_text(
        first.read_text(encoding="utf-8")
        + "\nForbidden example that must fail validation: /mnt/ace/private/raw.pdf\n",
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("#43: public-safety scan matched" in failure for failure in failures)


def test_validator_rejects_missing_parent_blocker_language(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_governance_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    first.write_text(
        first.read_text(encoding="utf-8").replace("parent remains blocked", "parent status is pending"),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("#43: missing common phrase 'parent remains blocked'" == failure for failure in failures)


def test_validator_rejects_wrong_embedded_artifact_path(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_governance_artifacts(tmp_path, validator)

    first_spec = validator.SPECS[0]
    first = tmp_path / first_spec.path
    first.write_text(
        first.read_text(encoding="utf-8").replace(
            f"Checklist artifact: `{first_spec.path}`",
            "Checklist artifact: `docs/governance/wrong.md`",
        ),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("#43: missing checklist artifact path" in failure for failure in failures)


def test_validator_rejects_wrong_frontmatter_issue_pair(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_governance_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    first.write_text(
        first.read_text(encoding="utf-8").replace(
            "issues: [vamseeachanta/llm-wiki#43, vamseeachanta/llm-wiki#14]",
            "issues: [vamseeachanta/llm-wiki#43]",
        ),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("#43: frontmatter issues must be" in failure for failure in failures)
