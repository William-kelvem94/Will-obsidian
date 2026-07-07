#!/usr/bin/env python3
"""
Recomendador de Proximo Estudo - sugere topicos para estudar com base em gaps,
skills pouco conectadas e historico recente de estudo.

Atualizado para a estrutura numerada canonica do WILL-OBSIDIAN.
"""

from __future__ import annotations

import re
import subprocess
from collections import defaultdict
from datetime import datetime, timedelta
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_PATH = SCRIPT_ROOT.parent.resolve()
OUTPUT_FILE = VAULT_PATH / "02-JARVIS" / "02-Operational" / "Proximo-Estudo.md"

CANONICAL_SKILLS_DIR = VAULT_PATH / "05-Skills"
LEGACY_SKILLS_DIR = VAULT_PATH / "skills"
CANONICAL_KNOWLEDGE_DIR = VAULT_PATH / "04-Conhecimentos"
LEGACY_KNOWLEDGE_DIR = VAULT_PATH / "Conhecimento-Geral"
GAPS_FILE = VAULT_PATH / "GAPS.md"
SKILLS_GAP_FILE = VAULT_PATH / ".logs" / "skills_gap.md"


def existing_dir(primary: Path, fallback: Path) -> Path:
    if primary.exists():
        return primary
    return fallback


def run(cmd: str, cwd: Path | None = None) -> str:
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or VAULT_PATH,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore",
        )
        return result.stdout.strip()
    except Exception:
        return ""


def parse_frontmatter(content: str) -> dict:
    fm = {"tags": [], "nivel": None, "level": None, "title": ""}
    match = re.match(r"^---\s*\n(.*?)\n(?:---|\.\.\.)", content, re.DOTALL)
    if not match:
        return fm

    block = match.group(1)
    title_match = re.search(r'^title:\s*"?(.+?)"?\s*$', block, re.MULTILINE)
    if title_match:
        fm["title"] = title_match.group(1).strip()

    tags_inline = re.search(r"^tags:\s*\[(.+?)\]", block, re.MULTILINE)
    if tags_inline:
        fm["tags"] = [tag.strip().strip("\"'") for tag in tags_inline.group(1).split(",") if tag.strip()]
    elif re.search(r"^tags:\s*$", block, re.MULTILINE):
        lines = block.splitlines()
        in_tags = False
        tags = []
        for line in lines:
            if line.startswith("tags:"):
                in_tags = True
                continue
            if in_tags and line.startswith("  - "):
                tags.append(line.replace("  - ", "", 1).strip())
            elif in_tags and line and not line.startswith(" "):
                break
        fm["tags"] = tags

    nivel_match = re.search(r"^nivel:\s*(.+)", block, re.MULTILINE)
    if nivel_match:
        fm["nivel"] = nivel_match.group(1).strip().lower()

    level_match = re.search(r"^level:\s*(\d+)", block, re.MULTILINE)
    if level_match:
        fm["level"] = int(level_match.group(1))

    return fm


def is_basic(fm: dict) -> bool:
    tags = [str(tag).lower() for tag in fm.get("tags", [])]
    if any(tag in ("level-basic", "level-init") for tag in tags):
        return True
    if fm.get("nivel") in ("basico", "básico", "iniciante"):
        return True
    if fm.get("level") is not None and fm["level"] <= 2:
        return True
    return False


def wiki_path(path: Path) -> str:
    rel = path.relative_to(VAULT_PATH)
    return rel.with_suffix("").as_posix()


def scan_low_skills() -> list[dict]:
    results = []
    skills_dir = existing_dir(CANONICAL_SKILLS_DIR, LEGACY_SKILLS_DIR)
    if not skills_dir.exists():
        return results

    for path in sorted(skills_dir.rglob("*.md")):
        if path.name.lower() in {"readme.md", "index.md"}:
            continue
        try:
            raw = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        fm = parse_frontmatter(raw)
        if is_basic(fm):
            title = fm["title"] or path.stem.replace("-", " ").title()
            results.append({
                "name": title,
                "source": "low-skill",
                "reason": "Skill em nivel basico ou inicial",
                "note_path": path,
                "priority": 3,
            })
    return results


def parse_gaps() -> list[dict]:
    if not GAPS_FILE.exists():
        return []
    try:
        text = GAPS_FILE.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    gaps = []
    sections = text.split("##")
    target = None
    for section in sections:
        first_line = section.splitlines()[0] if section.splitlines() else ""
        if "Skills/Áreas sem nota dedicada" in section or "Skills" in first_line:
            target = section
            break
    if not target:
        target = text

    for line in target.splitlines():
        line = line.strip()
        if not line.startswith("- "):
            continue
        content = line[2:].strip().lstrip("*").strip()
        if not content or "nenhum gap" in content.lower():
            continue
        if content.lower().startswith(("sugira", "anexe")):
            continue
        gaps.append({
            "name": content.strip(" *"),
            "source": "gaps-md",
            "reason": "Gap de conhecimento identificado no GAPS.md",
            "note_path": GAPS_FILE,
            "priority": 5,
        })
    return gaps


def parse_skills_gap() -> list[dict]:
    if not SKILLS_GAP_FILE.exists():
        return []
    try:
        text = SKILLS_GAP_FILE.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []

    results = []
    in_orphan = False
    for line in text.splitlines():
        if "Defined Skills Not Referenced by Projects" in line:
            in_orphan = True
            continue
        if line.startswith("##") and in_orphan and "Defined Skills" not in line:
            break
        if in_orphan and line.startswith("- "):
            name = line.lstrip("- ").strip()
            if name and name.lower() != "none found":
                results.append({
                    "name": name,
                    "source": "skills-gap",
                    "reason": "Skill definida mas pouco conectada a projetos ativos",
                    "note_path": SKILLS_GAP_FILE,
                    "priority": 4,
                })
    return results


def get_recent_studies() -> set[str]:
    recent_names: set[str] = set()
    since = (datetime.now() - timedelta(days=14)).isoformat()
    knowledge_dir = existing_dir(CANONICAL_KNOWLEDGE_DIR, LEGACY_KNOWLEDGE_DIR)
    rel_dir = knowledge_dir.relative_to(VAULT_PATH).as_posix() if knowledge_dir.exists() else "04-Conhecimentos"

    output = run(f'git log --since="{since}" --name-only --pretty=format: -- "{rel_dir}/*.md"')
    for line in output.splitlines():
        line = line.strip()
        if line.endswith(".md"):
            recent_names.add(Path(line).stem.lower().replace("-", " ").replace("_", " "))

    if knowledge_dir.exists():
        cutoff = datetime.now() - timedelta(days=14)
        for path in knowledge_dir.rglob("*.md"):
            try:
                if datetime.fromtimestamp(path.stat().st_mtime) >= cutoff:
                    recent_names.add(path.stem.lower().replace("-", " ").replace("_", " "))
            except Exception:
                continue
    return recent_names


def build_recommendations() -> list[dict]:
    candidates = []
    candidates.extend(scan_low_skills())
    candidates.extend(parse_gaps())
    candidates.extend(parse_skills_gap())

    if not candidates:
        print("[WARN] Nenhum candidato encontrado — tudo coberto ou fontes vazias.")
        return []

    recent = get_recent_studies()
    print(f"[INFO] {len(recent)} topicos recentes ignorados (estudados nos ultimos 14d)")

    seen: dict[str, dict] = {}
    for candidate in candidates:
        key = candidate["name"].lower().strip()
        if key in recent:
            continue
        if key in seen:
            if candidate["priority"] > seen[key]["priority"]:
                seen[key].update({
                    "priority": candidate["priority"],
                    "reason": candidate["reason"],
                    "source": candidate["source"],
                    "note_path": candidate["note_path"],
                })
            continue
        seen[key] = candidate

    return sorted(seen.values(), key=lambda item: (-item["priority"], item["name"]))


def estimate_time(name: str) -> str:
    lower = name.lower()
    if any(word in lower for word in ("kubernetes", "rag", "backend", "arquitetura", "orquestração", "multi-agent", "machine learning", "deep learning", "advanced")):
        return "2–3h"
    if any(word in lower for word in ("prompt", "mcp", "finops", "testes", "observabilidade", "monitoramento", "product")):
        return "1–2h"
    if any(word in lower for word in ("web", "component", "git", "python", "node", "docker")):
        return "45min–1h30"
    return "1–2h"


def find_existing_note(name: str) -> list[Path]:
    name_lower = name.lower()
    candidates = []
    roots = [existing_dir(CANONICAL_SKILLS_DIR, LEGACY_SKILLS_DIR), existing_dir(CANONICAL_KNOWLEDGE_DIR, LEGACY_KNOWLEDGE_DIR)]

    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*.md"):
            if path.name.lower() in {"index.md", "readme.md"}:
                try:
                    content = path.read_text(encoding="utf-8", errors="replace").lower()
                    if name_lower in content:
                        candidates.append(path)
                except Exception:
                    continue
                continue
            stem = path.stem.lower().replace("-", " ").replace("_", " ")
            if set(name_lower.split()) & set(stem.split()):
                candidates.append(path)

    def score(path: Path) -> int:
        stem = path.stem.lower().replace("-", " ").replace("_", " ")
        return len(set(name_lower.split()) & set(stem.split()))

    candidates.sort(key=score, reverse=True)
    return candidates[:3]


def pick_quick_win(recs: list[dict]) -> dict | None:
    if not recs:
        return None
    easy_keywords = ["web", "component", "prompt", "git", "testes", "monitoramento", "finops"]
    for rec in recs:
        if any(keyword in rec["name"].lower() for keyword in easy_keywords):
            return rec
    return recs[-1]


def format_link(note_path: Path | None) -> str:
    if not note_path:
        return ""
    if note_path == GAPS_FILE:
        return f"[[{wiki_path(note_path)}|GAPS]]"
    if note_path == SKILLS_GAP_FILE:
        return f"[[{wiki_path(note_path)}|skills_gap]]"
    return f"[[{wiki_path(note_path)}]]"


def generate_output(recs: list[dict]) -> str:
    now = datetime.now()
    top3 = recs[:3]
    quick = pick_quick_win(recs)

    table_rows = ""
    for index, rec in enumerate(top3, 1):
        table_rows += f"| {index} | **{rec['name']}** | {rec['reason']} | {format_link(rec['note_path'])} | {estimate_time(rec['name'])} |\n"

    details = ""
    for rec in recs:
        links = find_existing_note(rec["name"])
        if links:
            link_str = "\n".join(f"  - [[{wiki_path(path)}]]" for path in links)
        else:
            link_str = "  - *Nenhuma nota especifica encontrada ainda*"

        details += f"""
### {rec['name']}

| Campo | Valor |
|-------|-------|
| **Motivo** | {rec['reason']} |
| **Fonte** | `{rec['source']}` |
| **Estimativa** | {estimate_time(rec['name'])} |
| **Prioridade** | {rec['priority']}/5 |

**Notas relacionadas no vault:**
{link_str}

---
"""

    quick_section = ""
    if quick:
        quick_links = find_existing_note(quick["name"])
        quick_link_str = "\n".join(f"  - [[{wiki_path(path)}]]" for path in quick_links) if quick_links else "  - *Nenhuma nota especifica encontrada*"
        quick_section = f"""
## 🏆 Quick Win

**{quick['name']}** — {quick['reason']}

| Campo | Valor |
|-------|-------|
| **Estimativa** | {estimate_time(quick['name'])} |
| **Dificuldade** | Baixa |
| **Impacto** | Alto, por desbloquear uso prático em projetos |

**Notas relacionadas:**
{quick_link_str}
"""

    return f"""---
title: "Próximo Estudo — Recomendação Automática"
description: "Recomendação gerada automaticamente em {now.strftime('%Y-%m-%d')} com base em gaps, skills e histórico"
tags: [jarvis, recomendacao, estudo, auto-generated, jarvis-operacao]
generated: {now.strftime('%Y-%m-%d %H:%M:%S')}
updated: {now.strftime('%Y-%m-%d')}
---

# 🎯 Próximo Estudo — Recomendação Automática

**Gerado em:** {now.strftime('%Y-%m-%d %H:%M')}
**Total de recomendações:** {len(recs)}

---

## Top 3 Recomendações

| # | Tópico | Motivo | Nota Relacionada | Tempo Estimado |
|---|--------|--------|------------------|----------------|
{table_rows}
---

## Detalhamento das Recomendações

{details}
{quick_section}
---

## Fontes usadas

- Skills: `{existing_dir(CANONICAL_SKILLS_DIR, LEGACY_SKILLS_DIR).relative_to(VAULT_PATH).as_posix()}`
- Conhecimento: `{existing_dir(CANONICAL_KNOWLEDGE_DIR, LEGACY_KNOWLEDGE_DIR).relative_to(VAULT_PATH).as_posix()}`
- Gaps: `GAPS.md`
- Skills gap: `.logs/skills_gap.md`

*Gerado por `.scripts/study_recommender.py` com caminhos canônicos.*
"""


def main() -> None:
    recs = build_recommendations()
    if not recs:
        return
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(generate_output(recs), encoding="utf-8")
    print(f"✅ Recomendação gerada: {OUTPUT_FILE.relative_to(VAULT_PATH)}")
    print("\nTop 3:")
    for index, rec in enumerate(recs[:3], 1):
        print(f"  {index}. {rec['name']} — {rec['reason']}")


if __name__ == "__main__":
    main()
