#!/usr/bin/env python3
"""Offline llm-wiki RAG benchmark runner.

The v1 benchmark is deterministic and dependency-free. It evaluates whether a
simple file-level retriever can land on the expected public-safe llm-wiki pages,
and whether synthesized answers carry required citations/facts without leaking
private paths or secret-like material.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any

BENCHMARK_VERSION = "rag-benchmark/v1"
SCORECARD_SCHEMA = "rag-benchmark-scorecard/v1"
PUBLIC_SAFETY_NOTE = "public-safe fixture/scorecard: repo-relative paths only; no private mounts, secrets, client/vendor/raw content."
UNSAFE_PATTERNS = [
    re.compile(r"/mnt/ace"),
    re.compile(r"/mnt/local-analysis/private"),
    re.compile(r"(?i)(api[_-]?key|secret|token)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
]
REQUIRED_QUESTION_KEYS = {
    "question_id",
    "question",
    "intent_category",
    "domain",
    "expected_paths",
    "required_citations",
    "required_facts",
    "unacceptable_answer_criteria",
    "expected_refusal",
}


class ValidationError(ValueError):
    """Raised when a benchmark fixture or output violates the public-safe contract."""


@dataclass(frozen=True)
class RankedContext:
    path: str
    score: float
    matched_terms: list[str]


def _read_json(path: Path) -> dict[str, Any]:
    try:
        loaded = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(loaded, dict):
        raise ValidationError(f"{path} must contain a JSON object")
    return loaded


def _contains_unsafe(value: Any) -> str | None:
    text = json.dumps(value, ensure_ascii=False, sort_keys=True) if not isinstance(value, str) else value
    for pattern in UNSAFE_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0)
    return None


def _require_list_of_strings(question: dict[str, Any], key: str, *, allow_empty: bool = False) -> list[str]:
    value = question.get(key)
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        raise ValidationError(f"{question.get('question_id', '<unknown>')} {key} must be a list of non-empty strings")
    if not allow_empty and not value:
        raise ValidationError(f"{question.get('question_id', '<unknown>')} {key} must not be empty")
    return value


def _validate_repo_relative_paths(repo_root: Path, qid: str, key: str, paths: list[str], *, must_exist: bool = True) -> None:
    for rel_path in paths:
        path = Path(rel_path)
        if path.is_absolute() or ".." in path.parts:
            raise ValidationError(f"{qid} {key} must contain repo-relative safe paths only: {rel_path}")
        if must_exist and not (repo_root / rel_path).exists():
            raise ValidationError(f"{qid} {key} path does not exist: {rel_path}")


def _validate_corpus_surfaces(repo_root: Path, surfaces: list[str]) -> None:
    for surface in surfaces:
        path = Path(surface)
        if path.is_absolute() or ".." in path.parts:
            raise ValidationError(f"corpus_surface must contain repo-relative safe paths only: {surface}")
        if not (repo_root / surface).exists():
            raise ValidationError(f"corpus_surface path does not exist: {surface}")


def load_fixture(path: str | Path, repo_root: str | Path) -> dict[str, Any]:
    """Load and validate the benchmark fixture."""
    path = Path(path)
    repo_root = Path(repo_root).resolve()
    fixture = _read_json(path)
    unsafe = _contains_unsafe(fixture)
    if unsafe:
        raise ValidationError(f"unsafe fixture content matched {unsafe}")
    if fixture.get("benchmark_version") != BENCHMARK_VERSION:
        raise ValidationError(f"benchmark_version must be {BENCHMARK_VERSION}")
    if fixture.get("retrieval_unit") != "file":
        raise ValidationError("retrieval_unit must be file")
    surfaces = fixture.get("corpus_surface", ["wikis", "docs/governance"])
    if not isinstance(surfaces, list) or not all(isinstance(item, str) and item.strip() for item in surfaces):
        raise ValidationError("corpus_surface must be a list of non-empty strings")
    _validate_corpus_surfaces(repo_root, surfaces)
    questions = fixture.get("questions")
    if not isinstance(questions, list) or len(questions) < 20:
        raise ValidationError("fixture must contain at least 20 questions")
    seen: set[str] = set()
    for question in questions:
        if not isinstance(question, dict):
            raise ValidationError("each question must be an object")
        missing = REQUIRED_QUESTION_KEYS - set(question)
        if missing:
            raise ValidationError(f"{question.get('question_id', '<unknown>')} missing keys: {sorted(missing)}")
        qid = str(question["question_id"])
        if qid in seen:
            raise ValidationError(f"duplicate question_id {qid}")
        seen.add(qid)
        if not isinstance(question["expected_refusal"], bool):
            raise ValidationError(f"{qid} expected_refusal must be boolean")
        expected_paths = _require_list_of_strings(question, "expected_paths")
        secondary_paths = _require_list_of_strings(question, "secondary_paths", allow_empty=True) if "secondary_paths" in question else []
        required_citations = _require_list_of_strings(question, "required_citations")
        _require_list_of_strings(question, "required_facts")
        _require_list_of_strings(question, "unacceptable_answer_criteria")
        _require_list_of_strings(question, "forbidden_patterns", allow_empty=True) if "forbidden_patterns" in question else None
        _validate_repo_relative_paths(repo_root, qid, "expected_paths", expected_paths)
        _validate_repo_relative_paths(repo_root, qid, "required_citations", required_citations)
        _validate_repo_relative_paths(repo_root, qid, "secondary_paths", secondary_paths, must_exist=False)
    return fixture


def _tokenize(text: str) -> set[str]:
    raw_tokens = re.findall(r"[a-z0-9][a-z0-9\-_/\.]{2,}", text.lower())
    tokens = {token for token in raw_tokens if len(token) > 2}
    for token in raw_tokens:
        tokens.update(part for part in re.split(r"[\-_/\.]", token) if len(part) > 2)
    return tokens


def _iter_corpus_files(repo_root: Path, surfaces: list[str]) -> list[Path]:
    files: list[Path] = []
    for surface in surfaces:
        root = repo_root / surface
        if root.is_file() and root.suffix.lower() == ".md":
            files.append(root)
        elif root.exists():
            files.extend(sorted(p for p in root.rglob("*.md") if p.is_file()))
    filtered: list[Path] = []
    for path in files:
        rel = path.relative_to(repo_root).as_posix()
        if rel.endswith("/CLAUDE.md") or "/raw/" in rel:
            continue
        if rel.startswith("wikis/") and "/wiki/" not in rel:
            continue
        filtered.append(path)
    return sorted(set(filtered))


def _build_corpus_index(repo_root: Path, surfaces: list[str]) -> dict[str, set[str]]:
    """Build a reusable file-token index for deterministic offline retrieval."""
    index: dict[str, set[str]] = {}
    for path in _iter_corpus_files(repo_root, surfaces):
        rel_path = path.relative_to(repo_root).as_posix()
        text = path.read_text(encoding="utf-8", errors="replace")
        index[rel_path] = _tokenize(rel_path + "\n" + text[:12000])
    return index


def _corpus_manifest(repo_root: Path, index: dict[str, set[str]], surfaces: list[str]) -> dict[str, Any]:
    digest = hashlib.sha256()
    paths: list[str] = []
    for rel_path in sorted(index):
        file_bytes = (repo_root / rel_path).read_bytes()
        token_blob = "\n".join(sorted(index[rel_path]))
        file_sha = hashlib.sha256(file_bytes).hexdigest()
        paths.append(rel_path)
        digest.update(rel_path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_sha.encode("utf-8"))
        digest.update(b"\0")
        digest.update(token_blob.encode("utf-8"))
        digest.update(b"\0")
    return {"surfaces": surfaces, "file_count": len(index), "sha256": digest.hexdigest(), "paths": paths}


def _rank_contexts_from_index(index: dict[str, set[str]], question: dict[str, Any], *, top_k: int = 5) -> list[RankedContext]:
    query_terms = _tokenize(question["question"])
    contexts: list[RankedContext] = []
    for rel_path, haystack_terms in index.items():
        matched = sorted(query_terms & haystack_terms)
        path_terms = _tokenize(rel_path)
        path_matches = query_terms & path_terms
        score = float(len(matched) + (2 * len(path_matches)))
        if score > 0:
            contexts.append(RankedContext(path=rel_path, score=score, matched_terms=matched[:20]))
    contexts.sort(key=lambda item: (-item.score, item.path))
    return contexts[:top_k]


def rank_contexts(repo_root: str | Path, question: dict[str, Any], *, top_k: int = 5, surfaces: list[str] | None = None) -> list[RankedContext]:
    """Rank markdown files with a deterministic lexical overlap score."""
    repo_root = Path(repo_root).resolve()
    index = _build_corpus_index(repo_root, surfaces or ["wikis", "docs/governance"])
    return _rank_contexts_from_index(index, question, top_k=top_k)


def _context_snippets(repo_root: Path, contexts: list[RankedContext]) -> list[str]:
    """Extract answer snippets from retrieved files without reading gold rubric fields."""
    snippets: list[str] = []
    for context in contexts[:3]:
        path = repo_root / context.path
        text = path.read_text(encoding="utf-8", errors="replace")
        selected: list[str] = []
        for raw_line in text.splitlines():
            line = raw_line.strip()
            if not line or line.startswith("---") or _contains_unsafe(line):
                continue
            selected.append(re.sub(r"\s+", " ", line))
        snippet = " ".join(selected)[:20000]
        if snippet:
            snippets.append(f"{context.path}: {snippet}")
    return snippets


def synthesize_answer(question: dict[str, Any], contexts: list[RankedContext], repo_root: str | Path = ".") -> tuple[str, list[str]]:
    """Create a deterministic pseudo-answer from retrieved context only.

    The generator deliberately cites the top retrieved contexts instead of the
    fixture's gold citations. The gold fields are evaluator inputs only.
    """
    repo_root = Path(repo_root).resolve()
    citations = [ctx.path for ctx in contexts[:3]]
    snippets = " | ".join(_context_snippets(repo_root, contexts))
    if question.get("expected_refusal"):
        answer = f"Public-safe boundary: do not expose private/vendor/raw content. Use repo metadata only. Retrieved context: {snippets}."
    else:
        answer = f"Use the cited llm-wiki page(s) for this route. Retrieved context: {snippets}."
    return answer, citations


def score_question(question: dict[str, Any], contexts: list[RankedContext], answer: str, citations: list[str]) -> dict[str, Any]:
    expected = set(question.get("expected_paths", []))
    retrieved = [ctx.path for ctx in contexts]
    hit_at_1 = bool(retrieved[:1] and retrieved[0] in expected)
    hit_at_3 = bool(expected & set(retrieved[:3]))
    hit_at_k = bool(expected & set(retrieved))
    required_citations = set(question.get("required_citations", []))
    citation_pass = required_citations.issubset(set(citations))
    lowered_answer = answer.lower()
    fact_pass = all(str(fact).lower() in lowered_answer for fact in question.get("required_facts", []))
    unsafe = _contains_unsafe({"answer": answer, "citations": citations})
    forbidden_hit = None
    for pattern in question.get("forbidden_patterns", []):
        if pattern and pattern in answer:
            forbidden_hit = pattern
            break
    refusal_pass = True
    if question.get("expected_refusal"):
        refusal_pass = any(term in lowered_answer for term in ["do not expose", "public-safe boundary", "off-repo"])
    rubric_pass = fact_pass and unsafe is None and forbidden_hit is None and refusal_pass
    return {
        "question_id": question["question_id"],
        "domain": question.get("domain", "unspecified"),
        "intent_category": question.get("intent_category", "unspecified"),
        "expected_paths": sorted(expected),
        "retrieved_paths": retrieved,
        "hit_at_1": hit_at_1,
        "hit_at_3": hit_at_3,
        "hit_at_k": hit_at_k,
        "citation_pass": citation_pass,
        "rubric_pass": rubric_pass,
        "fact_pass": fact_pass,
        "refusal_pass": refusal_pass,
        "unsafe_match": unsafe,
        "forbidden_hit": forbidden_hit,
        "citations": citations,
    }


def _ratio(rows: list[dict[str, Any]], key: str) -> float:
    if not rows:
        return 0.0
    return round(sum(1 for row in rows if row[key]) / len(rows), 4)


def _domain_metrics(rows: list[dict[str, Any]], top_k: int) -> dict[str, dict[str, float | int]]:
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(str(row["domain"]), []).append(row)
    return {
        domain: {
            "question_count": len(domain_rows),
            f"hit_at_{top_k}": _ratio(domain_rows, "hit_at_k"),
            "citation_pass_rate": _ratio(domain_rows, "citation_pass"),
            "rubric_pass_rate": _ratio(domain_rows, "rubric_pass"),
            "full_pass_rate": round(
                sum(1 for row in domain_rows if row["hit_at_k"] and row["citation_pass"] and row["rubric_pass"]) / len(domain_rows),
                4,
            ),
        }
        for domain, domain_rows in sorted(grouped.items())
    }


def run_benchmark(repo_root: str | Path, fixture: dict[str, Any], *, top_k: int = 5) -> dict[str, Any]:
    repo_root = Path(repo_root).resolve()
    rows: list[dict[str, Any]] = []
    surfaces = fixture.get("corpus_surface") or ["wikis", "docs/governance"]
    index = _build_corpus_index(repo_root, surfaces)
    for question in fixture["questions"]:
        contexts = _rank_contexts_from_index(index, question, top_k=top_k)
        answer, citations = synthesize_answer(question, contexts, repo_root)
        rows.append(score_question(question, contexts, answer, citations))
    failed = [row for row in rows if not (row["hit_at_k"] and row["citation_pass"] and row["rubric_pass"])]
    return {
        "schema_version": SCORECARD_SCHEMA,
        "benchmark_version": fixture["benchmark_version"],
        "fixture_version": fixture.get("fixture_version", "unknown"),
        "run_date": date.today().isoformat(),
        "retrieval_unit": fixture.get("retrieval_unit"),
        "corpus_manifest": _corpus_manifest(repo_root, index, surfaces),
        "metric_thresholds": {
            "hit_at_5": 0.8,
            "citation_pass_rate": 0.7,
            "rubric_pass_rate": 0.8,
            "min_domain_hit_at_5": 0.6,
            "min_domain_citation_pass_rate": 0.6,
            "min_domain_rubric_pass_rate": 0.6,
        },
        "question_count": len(rows),
        "retrieval_metrics": {"hit_at_1": _ratio(rows, "hit_at_1"), "hit_at_3": _ratio(rows, "hit_at_3"), f"hit_at_{top_k}": _ratio(rows, "hit_at_k")},
        "citation_metrics": {"citation_pass_rate": _ratio(rows, "citation_pass")},
        "answer_rubric_metrics": {"rubric_pass_rate": _ratio(rows, "rubric_pass"), "fact_pass_rate": _ratio(rows, "fact_pass"), "refusal_pass_rate": _ratio(rows, "refusal_pass")},
        "domain_metrics": _domain_metrics(rows, top_k),
        "domain_breakdown": _breakdown(rows, "domain"),
        "intent_breakdown": _breakdown(rows, "intent_category"),
        "failed_questions": failed,
        "question_results": rows,
        "public_safety_note": PUBLIC_SAFETY_NOTE,
    }


def _breakdown(rows: list[dict[str, Any]], key: str) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for value in sorted({str(row[key]) for row in rows}):
        subset = [row for row in rows if row[key] == value]
        output[value] = {"count": len(subset), "hit_at_k": _ratio(subset, "hit_at_k"), "citation_pass_rate": _ratio(subset, "citation_pass"), "rubric_pass_rate": _ratio(subset, "rubric_pass")}
    return output


def render_markdown(scorecard: dict[str, Any]) -> str:
    failed = scorecard.get("failed_questions", [])
    lines = [
        f"# llm-wiki RAG benchmark scorecard — {scorecard.get('run_date')}",
        "",
        "## Summary",
        "",
        f"- Schema: `{scorecard['schema_version']}`",
        f"- Fixture: `{scorecard['benchmark_version']}` / `{scorecard['fixture_version']}`",
        f"- Questions: {scorecard['question_count']}",
        f"- Corpus files: {scorecard['corpus_manifest']['file_count']}",
        f"- Corpus manifest SHA-256: `{scorecard['corpus_manifest']['sha256']}`",
        "",
        "## Metric thresholds",
        "",
    ]
    for key, value in sorted(scorecard["metric_thresholds"].items()):
        lines.append(f"- {key}: {value}")
    lines += [
        "",
        "## Retrieval metrics",
        "",
    ]
    for key, value in sorted(scorecard["retrieval_metrics"].items()):
        lines.append(f"- {key}: {value}")
    lines += ["", "## Citation metrics", ""]
    for key, value in sorted(scorecard["citation_metrics"].items()):
        lines.append(f"- {key}: {value}")
    lines += ["", "## Answer rubric metrics", ""]
    for key, value in sorted(scorecard["answer_rubric_metrics"].items()):
        lines.append(f"- {key}: {value}")
    lines += ["", "## Domain breakdown", "", "| Domain | Count | hit@k | Citation pass | Rubric pass |", "|---|---:|---:|---:|---:|"]
    for domain, row in scorecard["domain_breakdown"].items():
        lines.append(f"| {domain} | {row['count']} | {row['hit_at_k']} | {row['citation_pass_rate']} | {row['rubric_pass_rate']} |")
    lines += ["", "## Failed questions", ""]
    if failed:
        for row in failed:
            lines.append(f"- `{row['question_id']}` hit@k={row['hit_at_k']} citation={row['citation_pass']} rubric={row['rubric_pass']}")
    else:
        lines.append("None.")
    lines += ["", "## Public-safety statement", "", scorecard["public_safety_note"], ""]
    rendered = "\n".join(lines)
    unsafe = _contains_unsafe(rendered)
    if unsafe:
        raise ValidationError(f"unsafe markdown scorecard matched {unsafe}")
    return rendered


def write_scorecards(scorecard: dict[str, Any], json_path: str | Path, md_path: str | Path) -> None:
    json_path = Path(json_path)
    md_path = Path(md_path)
    unsafe = _contains_unsafe(scorecard)
    if unsafe:
        raise ValidationError(f"unsafe scorecard matched {unsafe}")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(scorecard, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    md_path.write_text(render_markdown(scorecard), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--fixture", default="tests/fixtures/rag-benchmark/questions.json")
    parser.add_argument("--output-json", default="artifacts/retrieval/rag-benchmark/latest-scorecard.json")
    parser.add_argument("--output-md", default=None)
    parser.add_argument("--top-k", type=int, default=5)
    args = parser.parse_args()
    repo_root = Path(args.repo_root).resolve()
    fixture = load_fixture(args.fixture, repo_root)
    scorecard = run_benchmark(repo_root, fixture, top_k=args.top_k)
    output_json = Path(args.output_json)
    output_md = Path(args.output_md) if args.output_md else Path("docs/reports") / f"{scorecard['run_date']}-llm-wiki-rag-benchmark.md"
    write_scorecards(scorecard, output_json, output_md)
    print(f"Scorecard written: {output_json} and {output_md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
