#!/usr/bin/env python3
"""Aggregate-only source-family scanner for private/raw archives.

The scanner intentionally avoids reading file contents and avoids printing full paths.
By default it redacts top-level family labels to stable family IDs so the output can be
used in public planning artifacts without leaking private folder names.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

SIZE_BUCKETS = (
    (0, "empty"),
    (10 * 1024, "0-10KB"),
    (1024 * 1024, "10KB-1MB"),
    (100 * 1024 * 1024, "1MB-100MB"),
    (float("inf"), ">100MB"),
)


@dataclass
class FamilyStats:
    """Metadata-only aggregate statistics for one top-level source family."""

    label: str
    files: int = 0
    dirs: int = 0
    total_bytes: int = 0
    extensions: Counter[str] = field(default_factory=Counter)
    size_buckets: Counter[str] = field(default_factory=Counter)
    errors: int = 0


def family_id(label: str) -> str:
    """Return a stable public-safe ID for a source-family label."""

    digest = hashlib.sha256(label.encode("utf-8")).hexdigest()[:10]
    return f"family-{digest}"


def ext_bucket(path: Path) -> str:
    """Return a coarse extension bucket without exposing the filename."""

    suffix = path.suffix.lower()
    if not suffix:
        return "[no_ext]"
    if len(suffix) > 16:
        return "[long_ext]"
    return suffix


def size_bucket(size: int) -> str:
    """Return a coarse file-size bucket."""

    for upper, label in SIZE_BUCKETS:
        if size <= upper:
            return label
    raise AssertionError("unreachable size bucket")


def iter_children(root: Path) -> Iterable[Path]:
    """Yield top-level children in deterministic order."""

    yield from sorted(root.iterdir(), key=lambda item: item.name.lower())


def scan_family(child: Path) -> FamilyStats:
    """Scan one top-level family using metadata only."""

    stats = FamilyStats(label=child.name)
    if child.is_file():
        try:
            size = child.stat().st_size
        except OSError:
            stats.errors += 1
            return stats
        stats.files += 1
        stats.total_bytes += size
        stats.extensions[ext_bucket(child)] += 1
        stats.size_buckets[size_bucket(size)] += 1
        return stats

    for path in child.rglob("*"):
        try:
            if path.is_dir():
                stats.dirs += 1
                continue
            if not path.is_file():
                continue
            size = path.stat().st_size
        except OSError:
            stats.errors += 1
            continue
        stats.files += 1
        stats.total_bytes += size
        stats.extensions[ext_bucket(path)] += 1
        stats.size_buckets[size_bucket(size)] += 1
    return stats


def scan(root: Path) -> list[FamilyStats]:
    """Scan top-level families under root."""

    if not root.exists():
        raise FileNotFoundError(root)
    if not root.is_dir():
        raise NotADirectoryError(root)
    return [scan_family(child) for child in iter_children(root)]


def top(counter: Counter[str], limit: int) -> list[dict[str, int | str]]:
    """Convert a counter to a stable limited list for JSON/Markdown output."""

    return [
        {"bucket": key, "count": count}
        for key, count in sorted(counter.items(), key=lambda item: (-item[1], item[0]))[:limit]
    ]


def to_records(stats: list[FamilyStats], *, reveal_labels: bool, limit: int) -> list[dict[str, object]]:
    """Convert stats into path-free public-safe records."""

    records: list[dict[str, object]] = []
    for item in stats:
        public_id = family_id(item.label)
        record: dict[str, object] = {
            "family_id": public_id,
            "files": item.files,
            "dirs": item.dirs,
            "total_bytes": item.total_bytes,
            "top_extensions": top(item.extensions, limit),
            "size_buckets": top(item.size_buckets, limit=10),
            "metadata_errors": item.errors,
        }
        if reveal_labels:
            record["label"] = item.label
        records.append(record)
    return records


def render_markdown(records: list[dict[str, object]], *, root_label: str) -> str:
    """Render records as a Markdown report without full paths."""

    total_files = sum(int(record["files"]) for record in records)
    total_bytes = sum(int(record["total_bytes"]) for record in records)
    lines = [
        "---",
        'title: "Safe Source-Family Aggregate Scan"',
        "created: 2026-05-11",
        "last_updated: 2026-05-11",
        "public_safety: aggregate metadata only; no full paths; no file contents",
        "---",
        "",
        "# Safe Source-Family Aggregate Scan",
        "",
        f"Root label: `{root_label}` (top-level family names redacted unless explicitly requested).",
        "",
        f"- Families scanned: **{len(records)}**",
        f"- Files counted: **{total_files:,}**",
        f"- Bytes counted: **{total_bytes:,}**",
        "",
        "| Family ID | Files | Dirs | Bytes | Top extension buckets | Size buckets | Metadata errors |",
        "|---|---:|---:|---:|---|---|---:|",
    ]
    for record in records:
        ext_text = ", ".join(f"{entry['bucket']}={entry['count']}" for entry in record["top_extensions"]) or "n/a"
        size_text = ", ".join(f"{entry['bucket']}={entry['count']}" for entry in record["size_buckets"]) or "n/a"
        lines.append(
            f"| `{record['family_id']}` | {record['files']} | {record['dirs']} | {record['total_bytes']} | "
            f"{ext_text} | {size_text} | {record['metadata_errors']} |"
        )
    lines.extend(
        [
            "",
            "## Safety Contract",
            "",
            "This scan uses filesystem metadata only. It does not open file contents and does not emit full paths. "
            "The default family identifiers are stable hashes of top-level names, suitable for public planning records. "
            "Use `--reveal-labels` only for local/private review outputs.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path, help="Root directory to scan, e.g. /mnt/ace")
    parser.add_argument("--format", choices=("json", "md"), default="md")
    parser.add_argument("--reveal-labels", action="store_true", help="Include top-level labels; for private/local use only")
    parser.add_argument("--top", type=int, default=5, help="Number of top extension buckets to include")
    parser.add_argument("--root-label", default="/mnt/ace", help="Public-safe root label to print")
    args = parser.parse_args()

    records = to_records(scan(args.root), reveal_labels=args.reveal_labels, limit=args.top)
    if args.format == "json":
        print(json.dumps({"root_label": args.root_label, "families": records}, indent=2, sort_keys=True))
    else:
        print(render_markdown(records, root_label=args.root_label))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
