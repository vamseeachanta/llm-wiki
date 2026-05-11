"""Regression tests for practical-completion control-plane artifacts."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_completion_artifacts.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_completion_artifacts", VALIDATOR_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_completion_artifacts_validate_successfully() -> None:
    validator = _load_validator()

    assert validator.validate(ROOT) == []


def _copy_completion_artifacts(tmp_path: Path, validator) -> None:
    for spec in validator.SPECS:
        source = ROOT / spec.path
        target = tmp_path / spec.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def test_validator_rejects_forbidden_raw_archive_subpaths(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_completion_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    forbidden_path = "/" + "mnt" + "/" + "ace" + "/private/raw.pdf"
    first.write_text(
        first.read_text(encoding="utf-8")
        + f"\nForbidden example that must fail validation: {forbidden_path}\n",
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("public-safety scan matched" in failure for failure in failures)


def test_validator_requires_all_tier1_repo_links(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_completion_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    first.write_text(
        first.read_text(encoding="utf-8").replace(
            "https://github.com/vamseeachanta/digitalmodel",
            "https://example.invalid/digitalmodel",
        ),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("missing repo link https://github.com/vamseeachanta/digitalmodel" in failure for failure in failures)


def test_validator_requires_no_duplicate_umbrella_language(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_completion_artifacts(tmp_path, validator)

    first = tmp_path / validator.SPECS[0].path
    first.write_text(
        first.read_text(encoding="utf-8").replace("No duplicate umbrella issue", "Replacement roadmap issue"),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("missing phrase 'No duplicate umbrella issue'" in failure for failure in failures)
