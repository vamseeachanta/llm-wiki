#!/usr/bin/env python3
"""Validate llm-wiki RAG benchmark fixture and scorecard artifacts."""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RUNNER = ROOT / "scripts" / "llm_wiki_rag_benchmark.py"
REQUIRED_JSON_KEYS = {
    "schema_version",
    "benchmark_version",
    "fixture_version",
    "run_date",
    "retrieval_unit",
    "corpus_manifest",
    "metric_thresholds",
    "question_count",
    "retrieval_metrics",
    "citation_metrics",
    "answer_rubric_metrics",
    "domain_metrics",
    "failed_questions",
    "question_results",
    "public_safety_note",
}
REQUIRED_MD_SECTIONS = [
    "# llm-wiki RAG benchmark scorecard",
    "## Metric thresholds",
    "## Retrieval metrics",
    "## Citation metrics",
    "## Answer rubric metrics",
    "## Failed questions",
    "## Public-safety statement",
]


def _load_runner():
    spec = importlib.util.spec_from_file_location("llm_wiki_rag_benchmark", RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {RUNNER}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def _fail(message: str) -> int:
    print(message, file=sys.stderr)
    return 1


def _read_json(path: Path) -> dict[str, Any]:
    loaded = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(loaded, dict):
        raise ValueError("JSON artifact must be an object")
    return loaded


def _metric_value(data: dict[str, Any], key: str) -> float | None:
    for section in ["retrieval_metrics", "citation_metrics", "answer_rubric_metrics"]:
        value = data.get(section, {}).get(key)
        if isinstance(value, (int, float)):
            return float(value)
    domain_prefix_map = {
        "min_domain_hit_at_5": "hit_at_5",
        "min_domain_citation_pass_rate": "citation_pass_rate",
        "min_domain_rubric_pass_rate": "rubric_pass_rate",
    }
    if key in domain_prefix_map:
        metric = domain_prefix_map[key]
        values = [row.get(metric) for row in data.get("domain_metrics", {}).values() if isinstance(row, dict)]
        numeric_values = [float(value) for value in values if isinstance(value, (int, float))]
        if numeric_values:
            return min(numeric_values)
    return None


def validate(fixture_path: Path, markdown_path: Path, json_path: Path) -> list[str]:
    runner = _load_runner()
    failures: list[str] = []
    try:
        fixture = runner.load_fixture(fixture_path, ROOT)
    except Exception as exc:  # noqa: BLE001 - validator reports all fixture failures uniformly.
        failures.append(f"fixture validation failed: {exc}")
        fixture = None
    try:
        data = _read_json(json_path)
    except Exception as exc:  # noqa: BLE001
        failures.append(f"scorecard JSON invalid: {exc}")
        data = {}
    markdown = markdown_path.read_text(encoding="utf-8", errors="replace") if markdown_path.exists() else ""
    unsafe_md = runner._contains_unsafe(markdown)
    unsafe_json = runner._contains_unsafe(data) if data else None
    if unsafe_md:
        failures.append(f"unsafe markdown content matched {unsafe_md}")
    if unsafe_json:
        failures.append(f"unsafe JSON content matched {unsafe_json}")
    for key in sorted(REQUIRED_JSON_KEYS):
        if key not in data:
            failures.append(f"missing JSON key: {key}")
    for section in REQUIRED_MD_SECTIONS:
        if section not in markdown:
            failures.append(f"missing required markdown section: {section}")
    if data.get("schema_version") not in {None, runner.SCORECARD_SCHEMA}:
        failures.append(f"schema_version must be {runner.SCORECARD_SCHEMA}")
    if fixture and REQUIRED_JSON_KEYS <= set(data):
        expected = runner.run_benchmark(ROOT, fixture, top_k=5)
        comparable_keys = [
            "schema_version",
            "benchmark_version",
            "fixture_version",
            "run_date",
            "retrieval_unit",
            "corpus_manifest",
            "metric_thresholds",
            "question_count",
            "retrieval_metrics",
            "citation_metrics",
            "answer_rubric_metrics",
            "domain_metrics",
            "failed_questions",
            "question_results",
            "public_safety_note",
        ]
        for key in comparable_keys:
            if data.get(key) != expected.get(key):
                failures.append(f"scorecard {key} does not match recomputed benchmark")
        for key, threshold in data.get("metric_thresholds", {}).items():
            actual = _metric_value(data, key)
            if actual is None:
                failures.append(f"threshold references missing metric: {key}")
            elif actual < float(threshold):
                failures.append(f"metric {key}={actual} is below threshold {threshold}")
        expected_markdown = runner.render_markdown(data) if data else ""
        if markdown != expected_markdown:
            failures.append("markdown scorecard does not match JSON-rendered benchmark")
    return failures


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if len(argv) != 3:
        print("usage: validate_rag_benchmark.py <fixture.json> <scorecard.md> <scorecard.json>", file=sys.stderr)
        return 2
    failures = validate(Path(argv[0]), Path(argv[1]), Path(argv[2]))
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print("RAG benchmark validation OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
