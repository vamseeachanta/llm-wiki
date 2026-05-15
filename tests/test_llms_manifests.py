"""Regression tests for llms.txt AI-agent entrypoint manifests."""
from __future__ import annotations

import importlib.util
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR_PATH = ROOT / "scripts" / "validate_llms_manifests.py"


def _load_validator():
    spec = importlib.util.spec_from_file_location("validate_llms_manifests", VALIDATOR_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def _copy_manifest_tree(tmp_path: Path, validator) -> None:
    for manifest in validator.MANIFESTS:
        source = ROOT / manifest.path
        target = tmp_path / manifest.path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source.read_text(encoding="utf-8"), encoding="utf-8")


def test_llms_manifests_validate_successfully() -> None:
    validator = _load_validator()

    assert validator.validate(ROOT) == []


def test_root_llms_manifest_contains_repo_boundary_and_domain_entrypoints() -> None:
    root_manifest = (ROOT / "llms.txt").read_text(encoding="utf-8")

    for required in (
        "Public/private boundary",
        "wikis/marine-engineering/llms.txt",
        "wikis/engineering/llms.txt",
        "wikis/engineering-standards/llms.txt",
        "wikis/cross-links-tier1.md",
        "docs/governance/service-provider-data-routing.md",
    ):
        assert required in root_manifest


def test_domain_llms_manifests_link_only_to_existing_repo_paths() -> None:
    validator = _load_validator()

    failures = validator.validate_existing_targets(ROOT)

    assert failures == []


def test_llms_validator_rejects_raw_private_or_vendor_path_patterns(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_manifest_tree(tmp_path, validator)

    manifest = tmp_path / "llms.txt"
    manifest.write_text(
        manifest.read_text(encoding="utf-8")
        + "\nForbidden examples that must fail validation: /mnt/ace/private/raw.pdf and /mnt/local-analysis/private-notes.md\n",
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("public-safety scan matched" in failure for failure in failures)


def test_llms_validator_rejects_missing_required_sections(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_manifest_tree(tmp_path, validator)

    manifest = tmp_path / "wikis" / "engineering" / "llms.txt"
    manifest.write_text(
        manifest.read_text(encoding="utf-8").replace("## Safety Boundary", "## Boundary"),
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any("wikis/engineering/llms.txt: missing required section 'Safety Boundary'" == failure for failure in failures)


def test_llms_validator_rejects_missing_manifest_targets(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_manifest_tree(tmp_path, validator)
    shutil.copytree(ROOT / "wikis", tmp_path / "wikis", dirs_exist_ok=True)
    shutil.copytree(ROOT / "docs", tmp_path / "docs", dirs_exist_ok=True)
    for path in ("README.md", "CLAUDE.md", "LICENSE", "LICENSE-CONTENT"):
        shutil.copy2(ROOT / path, tmp_path / path)

    target = tmp_path / "wikis" / "engineering" / "wiki" / "overview.md"
    target.unlink()

    failures = validator.validate(tmp_path)

    assert any("wikis/engineering/llms.txt: missing linked target wiki/overview.md" in failure for failure in failures)


def test_llms_validator_rejects_missing_code_span_path_targets(tmp_path: Path) -> None:
    validator = _load_validator()
    _copy_manifest_tree(tmp_path, validator)
    shutil.copytree(ROOT / "wikis", tmp_path / "wikis", dirs_exist_ok=True)
    shutil.copytree(ROOT / "docs", tmp_path / "docs", dirs_exist_ok=True)
    for path in ("README.md", "CLAUDE.md", "LICENSE", "LICENSE-CONTENT"):
        shutil.copy2(ROOT / path, tmp_path / path)

    manifest = tmp_path / "wikis" / "marine-engineering" / "llms.txt"
    manifest.write_text(
        manifest.read_text(encoding="utf-8")
        + "\n- `wikis/marine-engineering/wiki/workflows/` — intentionally missing path.\n",
        encoding="utf-8",
    )

    failures = validator.validate(tmp_path)

    assert any(
        "wikis/marine-engineering/llms.txt: missing code-path target wikis/marine-engineering/wiki/workflows/"
        in failure
        for failure in failures
    )


def test_llms_routing_smoke_tests_cover_canonical_intents() -> None:
    validator = _load_validator()

    routes = validator.extract_routing_targets(ROOT / "llms.txt")

    assert routes["marine engineering"] == "wikis/marine-engineering/llms.txt"
    assert routes["engineering methods"] == "wikis/engineering/llms.txt"
    assert routes["standards"] == "wikis/engineering-standards/llms.txt"
    assert routes["governance"] == "docs/governance/service-provider-data-routing.md"
    assert routes["code and results links"] == "wikis/cross-links-tier1.md"


def test_marine_manifest_is_bounded_and_warns_against_blind_scanning() -> None:
    marine_manifest = (ROOT / "wikis" / "marine-engineering" / "llms.txt").read_text(encoding="utf-8")
    markdown_links = [line for line in marine_manifest.splitlines() if "](" in line]

    assert "19k" in marine_manifest
    assert "Do not scan blindly" in marine_manifest
    assert len(markdown_links) <= 55
