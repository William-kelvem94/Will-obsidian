#!/usr/bin/env python3
"""Generate a compact inventory report for the Will vault.

The script is intentionally dependency-free so it can run in the existing
Windows/Python setup and be reused by local agents or scheduled automation.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[2]
IGNORED_DIRS = {".git", ".obsidian", ".venv", "__pycache__", "node_modules"}


@dataclass
class InventoryItem:
    label: str
    path: str
    markdown_files: int
    total_files: int
    total_bytes: int


def walk_files(base: Path) -> Iterable[Path]:
    if not base.exists():
        return []
    for path in base.rglob("*"):
        if any(part in IGNORED_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def count_markdown_files(base: Path) -> int:
    return sum(1 for path in walk_files(base) if path.suffix.lower() == ".md")


def count_all_files(base: Path) -> int:
    return sum(1 for _ in walk_files(base))


def total_bytes(base: Path) -> int:
    size = 0
    for path in walk_files(base):
        try:
            size += path.stat().st_size
        except OSError:
            continue
    return size


def build_inventory() -> list[InventoryItem]:
    categories = [
        ("vault_root", ROOT),
        ("knowledge_raw", ROOT / "raw"),
        ("knowledge_wiki", ROOT / "wiki"),
        ("knowledge_schema", ROOT / "schema"),
        ("skills_canonical", ROOT / "05-Skills"),
        ("skills_legacy", ROOT / "skills"),
        ("skills_agents", ROOT / ".agents" / "skills"),
        ("skills_continue", ROOT / ".continue" / "skills"),
        ("ops", ROOT / "09-Sistema"),
        ("hubs", ROOT / "01-Hubs"),
        ("jarvis", ROOT / "02-JARVIS"),
        ("projects", ROOT / "03-Projetos"),
        ("personal", ROOT / "06-Will-Pessoal"),
        ("raw_data", ROOT / "11-Dados-Brutos"),
    ]
    return [
        InventoryItem(
            label=label,
            path=str(path.relative_to(ROOT)) if path != ROOT else ".",
            markdown_files=count_markdown_files(path),
            total_files=count_all_files(path),
            total_bytes=total_bytes(path),
        )
        for label, path in categories
    ]


def render_markdown(items: list[InventoryItem]) -> str:
    lines = [
        "# Vault Inventory",
        "",
        "| Label | Path | Markdown | Files | Bytes |",
        "|---|---|---:|---:|---:|",
    ]
    for item in items:
        lines.append(
            f"| {item.label} | `{item.path}` | {item.markdown_files} | {item.total_files} | {item.total_bytes} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a vault inventory report.")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of Markdown.")
    parser.add_argument("--output", type=Path, help="Optional file path to write the report.")
    args = parser.parse_args()

    items = build_inventory()
    if args.json:
        payload = json.dumps([asdict(item) for item in items], indent=2, ensure_ascii=False)
    else:
        payload = render_markdown(items)

    if args.output:
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

