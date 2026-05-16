"""Tests for the llm-wiki RAG benchmark."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / "scripts" / "llm_wiki_rag_benchmark.py"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "rag-benchmark" / "questions.json"


def _load_benchmark():
    spec = importlib.util.spec_from_file_location("llm_wiki_rag_benchmark", SCRIPT_PATH)
    assert spec is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def test_benchmark_fixture_schema_loads_and_has_minimum_coverage() -> None:
    benchmark = _load_benchmark()

    fixture = benchmark.load_fixture(FIXTURE_PATH, ROOT)

    assert fixture["benchmark_version"] == "rag-benchmark/v1"
    assert fixture["retrieval_unit"] == "file"
    questions = fixture["questions"]
    assert len(questions) >= 20
    categories = {q["intent_category"] for q in questions}
    assert {"implementation_locator", "standards_applicability", "public_result_validation", "governance_boundary", "cross_domain_routing"} <= categories
    domains = {q["domain"] for q in questions}
    assert {"marine-offshore", "standards", "production-engineering", "code-results", "governance"} <= domains


def test_benchmark_questions_have_paths_citations_facts_and_unacceptable_rules() -> None:
    benchmark = _load_benchmark()

    fixture = benchmark.load_fixture(FIXTURE_PATH, ROOT)

    for question in fixture["questions"]:
        assert question["question_id"]
        assert question["question"]
        assert question["expected_paths"]
        assert question["required_citations"]
        assert question["required_facts"]
        assert question["unacceptable_answer_criteria"]
        for key in ["expected_paths", "required_citations"]:
            for rel_path in question[key]:
                assert not Path(rel_path).is_absolute()
                assert ".." not in Path(rel_path).parts
                assert (ROOT / rel_path).exists(), rel_path


def test_benchmark_rejects_private_paths_and_secret_like_tokens(tmp_path: Path) -> None:
    benchmark = _load_benchmark()
    fixture = {
        "benchmark_version": "rag-benchmark/v1",
        "fixture_version": "2026-05-16",
        "retrieval_unit": "file",
        "corpus_surface": ["wikis"],
        "questions": [
            {
                "question_id": "unsafe-001",
                "question": "Where is the private material?",
                "intent_category": "governance_boundary",
                "domain": "governance",
                "expected_paths": ["/mnt/ace/private.pdf"],
                "secondary_paths": [],
                "required_citations": ["/mnt/ace/private.pdf"],
                "required_facts": ["private"],
                "forbidden_patterns": [],
                "unacceptable_answer_criteria": ["leaks private path"],
                "expected_refusal": True,
            }
        ],
    }
    path = tmp_path / "questions.json"
    path.write_text(json.dumps(fixture), encoding="utf-8")

    try:
        benchmark.load_fixture(path, ROOT)
    except benchmark.ValidationError as exc:
        assert "/mnt/ace" in str(exc)
    else:
        raise AssertionError("unsafe fixture should fail validation")


def test_required_citations_must_be_repo_relative_safe_paths(tmp_path: Path) -> None:
    benchmark = _load_benchmark()
    fixture = benchmark.load_fixture(FIXTURE_PATH, ROOT)
    fixture = json.loads(json.dumps(fixture))
    fixture["questions"] = fixture["questions"][:20]
    fixture["questions"][0]["required_citations"] = ["/etc/passwd"]
    path = tmp_path / "questions.json"
    path.write_text(json.dumps(fixture), encoding="utf-8")

    try:
        benchmark.load_fixture(path, ROOT)
    except benchmark.ValidationError as exc:
        assert "required_citations" in str(exc)
    else:
        raise AssertionError("absolute required_citations path should fail validation")


def test_retriever_does_not_use_expected_paths_or_required_citations_as_ranking_boost() -> None:
    benchmark = _load_benchmark()
    question = {
        "question_id": "leakage-check",
        "question": "zzzzzz qqqqqq no overlap tokens",
        "expected_paths": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_citations": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_facts": ["code/results"],
        "expected_refusal": False,
    }
    contexts = benchmark.rank_contexts(ROOT, question, top_k=5, surfaces=["wikis/marine-engineering/wiki/code-results-links.md"])

    assert contexts == []


def test_fixture_rejects_absolute_corpus_surface(tmp_path: Path) -> None:
    benchmark = _load_benchmark()
    fixture = benchmark.load_fixture(FIXTURE_PATH, ROOT)
    fixture = json.loads(json.dumps(fixture))
    fixture["corpus_surface"] = ["/etc"]
    path = tmp_path / "questions.json"
    path.write_text(json.dumps(fixture), encoding="utf-8")

    try:
        benchmark.load_fixture(path, ROOT)
    except benchmark.ValidationError as exc:
        assert "corpus_surface" in str(exc)
    else:
        raise AssertionError("absolute corpus_surface should fail validation")


def test_answer_synthesis_does_not_filter_citations_through_answer_key() -> None:
    benchmark = _load_benchmark()
    question = {
        "question_id": "citation-leakage",
        "expected_paths": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_citations": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_facts": ["code/results"],
        "expected_refusal": False,
    }
    contexts = [
        benchmark.RankedContext(path="wikis/engineering/wiki/public-data-software-links.md", score=2.0, matched_terms=["public"]),
        benchmark.RankedContext(path="wikis/marine-engineering/wiki/code-results-links.md", score=1.0, matched_terms=["code"]),
    ]

    _answer, citations = benchmark.synthesize_answer(question, contexts, ROOT)

    assert citations == ["wikis/engineering/wiki/public-data-software-links.md", "wikis/marine-engineering/wiki/code-results-links.md"]


def test_synthesized_answer_only_passes_facts_present_in_retrieved_context() -> None:
    benchmark = _load_benchmark()
    question = {
        "question_id": "fact-check",
        "expected_paths": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_citations": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_facts": ["definitely-not-present-fact"],
        "expected_refusal": False,
    }
    contexts = [benchmark.RankedContext(path="wikis/marine-engineering/wiki/code-results-links.md", score=1.0, matched_terms=["code"])]

    answer, citations = benchmark.synthesize_answer(question, contexts, ROOT)
    result = benchmark.score_question(question, contexts, answer=answer, citations=citations)

    assert citations == ["wikis/marine-engineering/wiki/code-results-links.md"]
    assert result["fact_pass"] is False
    assert result["rubric_pass"] is False


def test_answer_synthesis_does_not_read_required_facts_as_extraction_queries(tmp_path: Path) -> None:
    benchmark = _load_benchmark()

    class PoisonFact:
        def __str__(self) -> str:  # pragma: no cover - test fails if called.
            raise AssertionError("synthesis must not read required_facts")

    repo = tmp_path
    source = repo / "docs" / "context.md"
    source.parent.mkdir(parents=True)
    source.write_text("# Context\nmatched route evidence.\n", encoding="utf-8")
    question = {
        "question_id": "fact-leakage",
        "expected_paths": ["docs/context.md"],
        "required_citations": ["docs/context.md"],
        "required_facts": [PoisonFact()],
        "expected_refusal": False,
    }
    contexts = [benchmark.RankedContext(path="docs/context.md", score=1.0, matched_terms=["matched"])]

    answer, citations = benchmark.synthesize_answer(question, contexts, repo)

    assert citations == ["docs/context.md"]
    assert "matched route evidence" in answer


def test_retrieval_scoring_counts_expected_path_hits_deterministically() -> None:
    benchmark = _load_benchmark()
    question = {
        "question_id": "q1",
        "expected_paths": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_citations": ["wikis/marine-engineering/wiki/code-results-links.md"],
        "required_facts": ["code/results"],
        "expected_refusal": False,
    }
    contexts = [
        benchmark.RankedContext(path="wikis/engineering/wiki/index.md", score=0.5, matched_terms=["wiki"]),
        benchmark.RankedContext(path="wikis/marine-engineering/wiki/code-results-links.md", score=0.4, matched_terms=["code"]),
    ]

    result = benchmark.score_question(question, contexts, answer="code/results are cited", citations=["wikis/marine-engineering/wiki/code-results-links.md"])

    assert result["hit_at_1"] is False
    assert result["hit_at_3"] is True
    assert result["citation_pass"] is True
    assert result["rubric_pass"] is True


def test_scorecard_output_contains_markdown_and_json_sections(tmp_path: Path) -> None:
    benchmark = _load_benchmark()
    fixture = benchmark.load_fixture(FIXTURE_PATH, ROOT)
    scorecard = benchmark.run_benchmark(ROOT, fixture, top_k=5)
    json_path = tmp_path / "scorecard.json"
    md_path = tmp_path / "scorecard.md"

    benchmark.write_scorecards(scorecard, json_path, md_path)

    data = json.loads(json_path.read_text(encoding="utf-8"))
    markdown = md_path.read_text(encoding="utf-8")
    assert data["schema_version"] == "rag-benchmark-scorecard/v1"
    assert data["question_count"] >= 20
    assert "corpus_manifest" in data
    assert data["corpus_manifest"]["file_count"] == len(data["corpus_manifest"]["paths"])
    assert all(isinstance(path, str) and path.endswith(".md") for path in data["corpus_manifest"]["paths"][:10])
    assert "metric_thresholds" in data
    assert "retrieval_metrics" in data
    assert "citation_metrics" in data
    assert "answer_rubric_metrics" in data
    assert "# llm-wiki RAG benchmark scorecard" in markdown
    assert "## Metric thresholds" in markdown
    assert "## Retrieval metrics" in markdown
    assert "## Public-safety statement" in markdown
    assert "/mnt/ace" not in markdown


def test_cli_produces_json_and_markdown_scorecards(tmp_path: Path) -> None:
    json_path = tmp_path / "scorecard.json"
    md_path = tmp_path / "scorecard.md"

    result = subprocess.run(
        [
            sys.executable,
            str(SCRIPT_PATH),
            "--fixture",
            str(FIXTURE_PATH),
            "--output-json",
            str(json_path),
            "--output-md",
            str(md_path),
        ],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0, result.stderr
    assert json_path.exists()
    assert md_path.exists()
    assert "Scorecard written" in result.stdout


def test_corpus_manifest_changes_when_file_tail_changes_beyond_index_window(tmp_path: Path) -> None:
    benchmark = _load_benchmark()
    source = tmp_path / "docs" / "long.md"
    source.parent.mkdir(parents=True)
    source.write_text("a" * 13000 + "\noriginal-tail\n", encoding="utf-8")

    first_index = benchmark._build_corpus_index(tmp_path, ["docs"])
    first_manifest = benchmark._corpus_manifest(tmp_path, first_index, ["docs"])
    source.write_text("a" * 13000 + "\nchanged-tail\n", encoding="utf-8")
    second_index = benchmark._build_corpus_index(tmp_path, ["docs"])
    second_manifest = benchmark._corpus_manifest(tmp_path, second_index, ["docs"])

    assert first_index == second_index
    assert first_manifest["sha256"] != second_manifest["sha256"]
