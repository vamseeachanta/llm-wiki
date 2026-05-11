"""Tests for the aggregate-only source-family scanner."""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCANNER_PATH = ROOT / "scripts" / "scan_source_families_safe.py"


def _load_scanner():
    spec = importlib.util.spec_from_file_location("scan_source_families_safe", SCANNER_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_default_records_redact_family_labels_and_full_paths(tmp_path: Path) -> None:
    scanner = _load_scanner()
    family = tmp_path / "client-secret-family"
    nested = family / "nested"
    nested.mkdir(parents=True)
    (nested / "private-model.dat").write_text("synthetic fixture", encoding="utf-8")

    records = scanner.to_records(scanner.scan(tmp_path), reveal_labels=False, limit=5)
    rendered = scanner.render_markdown(records, root_label="/mnt/ace")

    assert len(records) == 1
    assert records[0]["family_id"].startswith("family-")
    assert "label" not in records[0]
    assert "client-secret-family" not in rendered
    assert "private-model.dat" not in rendered
    assert str(tmp_path) not in rendered
    assert ".dat=1" in rendered


def test_reveal_labels_is_explicit_local_mode(tmp_path: Path) -> None:
    scanner = _load_scanner()
    family = tmp_path / "oss-family"
    family.mkdir()
    (family / "README.md").write_text("synthetic fixture", encoding="utf-8")

    records = scanner.to_records(scanner.scan(tmp_path), reveal_labels=True, limit=5)

    assert records[0]["label"] == "oss-family"
    assert records[0]["files"] == 1
    assert records[0]["top_extensions"][0] == {"bucket": ".md", "count": 1}
