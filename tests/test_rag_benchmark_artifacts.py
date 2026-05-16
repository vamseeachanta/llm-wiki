"""Artifact validator tests for the llm-wiki RAG benchmark."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_rag_benchmark.py"
RUNNER = ROOT / "scripts" / "llm_wiki_rag_benchmark.py"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "rag-benchmark" / "questions.json"


def _run_scorecard(tmp_path: Path) -> tuple[Path, Path]:
    json_path = tmp_path / "latest-scorecard.json"
    md_path = tmp_path / "scorecard.md"
    run_result = subprocess.run(
        [sys.executable, str(RUNNER), "--fixture", str(FIXTURE_PATH), "--output-json", str(json_path), "--output-md", str(md_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    assert run_result.returncode == 0, run_result.stderr
    return json_path, md_path


def test_validator_accepts_generated_scorecards(tmp_path: Path) -> None:
    json_path, md_path = _run_scorecard(tmp_path)

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0, result.stderr
    assert "RAG benchmark validation OK" in result.stdout


def test_validator_rejects_missing_scorecard_sections(tmp_path: Path) -> None:
    json_path = tmp_path / "scorecard.json"
    md_path = tmp_path / "scorecard.md"
    json_path.write_text(json.dumps({"schema_version": "rag-benchmark-scorecard/v1", "question_count": 20}), encoding="utf-8")
    md_path.write_text("# llm-wiki RAG benchmark scorecard\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "missing required markdown section" in result.stderr or "missing JSON key" in result.stderr


def test_validator_rejects_unsafe_scorecard_text(tmp_path: Path) -> None:
    json_path, md_path = _run_scorecard(tmp_path)
    data = json.loads(json_path.read_text(encoding="utf-8"))
    data["public_safety_note"] = "/mnt/ace/private"
    json_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "/mnt/ace" in result.stderr


def test_validator_rejects_stale_or_forged_scorecard_metrics(tmp_path: Path) -> None:
    json_path, md_path = _run_scorecard(tmp_path)
    data = json.loads(json_path.read_text(encoding="utf-8"))
    data["fixture_version"] = "stale-wrong-version"
    data["retrieval_metrics"] = {key: 0.0 for key in data["retrieval_metrics"]}
    json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "does not match recomputed benchmark" in result.stderr


def test_validator_rejects_scorecards_below_declared_thresholds(tmp_path: Path) -> None:
    json_path, md_path = _run_scorecard(tmp_path)
    data = json.loads(json_path.read_text(encoding="utf-8"))
    data["metric_thresholds"] = {key: 1.0 for key in data["metric_thresholds"]}
    json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(md_path.read_text(encoding="utf-8").replace("0.5", "1.0"), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "below threshold" in result.stderr


def test_validator_rejects_stale_run_date_even_when_markdown_matches_json(tmp_path: Path) -> None:
    json_path, md_path = _run_scorecard(tmp_path)
    data = json.loads(json_path.read_text(encoding="utf-8"))
    original_date = data["run_date"]
    data["run_date"] = "1999-12-31"
    json_path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(md_path.read_text(encoding="utf-8").replace(original_date, "1999-12-31"), encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE_PATH), str(md_path), str(json_path)],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 1
    assert "scorecard run_date does not match recomputed benchmark" in result.stderr
