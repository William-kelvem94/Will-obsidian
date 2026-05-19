"""
Gerador de Desafios Semanais (E2)
Escaneia o vault, identifica pontos de melhoria
e gera um note com 3-5 desafios acionáveis para a semana.

Uso:
    python .scripts/challenge_generator.py              # gera desafio desta semana
    python .scripts/challenge_generator.py --force       # regera mesmo se ja existir
"""

import argparse
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_DIR.parent
CHALLENGES_DIR = VAULT_ROOT / "JARVIS" / "02-Operational" / "Challenges"

EXCLUDED_DIRS = {
    ".git", "__pycache__", "node_modules", ".obsidian", ".trash",
    ".scripts", ".agents", "templates",
}

EXCLUDED_FILES = {
    "README.md", "INDEX.md", "LICENSE",
}


def collect_all_notes(vault_root: Path) -> list[dict]:
    """Walk the vault and collect all .md notes with metadata."""
    notes = []
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        parts = set(rel.parts)
        if parts & EXCLUDED_DIRS:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            if f in EXCLUDED_FILES:
                continue
            fpath = Path(root) / f
            notes.append(parse_note(fpath, vault_root))
    return notes


def parse_note(fpath: Path, vault_root: Path) -> dict:
    """Parse a markdown note: frontmatter, body, stats."""
    rel = fpath.relative_to(vault_root)
    raw = fpath.read_text(encoding="utf-8", errors="replace")
    fm, body = split_frontmatter(raw)
    name = fpath.stem

    # Incoming links: search raw for [[name]] and [[path/to/name]]
    # (populated later by scan_links)

    mtime = datetime.fromtimestamp(fpath.stat().st_mtime, tz=timezone.utc)

    return {
        "path": fpath,
        "rel": str(rel),
        "name": name,
        "body": body,
        "frontmatter": fm,
        "raw": raw,
        "raw_length": len(raw),
        "body_length": len(body.strip()),
        "mtime": mtime,
    }


def split_frontmatter(raw: str) -> tuple[str, str]:
    """Return (frontmatter_text, body_text)."""
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n?", raw, re.DOTALL)
    if fm_match:
        return fm_match.group(1), raw[fm_match.end():]
    return "", raw


def has_frontmatter_field(fm: str, field: str) -> bool:
    """Check if frontmatter contains a given field (at line start)."""
    return bool(re.search(rf"^{field}\s*:", fm, re.MULTILINE))


def scan_incoming_links(notes: list[dict]):
    """Populate 'incoming' set for each note by searching [[name]] across all notes."""
    name_to_note = {}
    for n in notes:
        name_to_note[n["name"]] = n
        # also index all path variants
        name_to_note[n["rel"].replace("\\", "/").removesuffix(".md")] = n

    for n in notes:
        n["incoming"] = set()
        n["referenced_by"] = []

    for n in notes:
        # Find [[...]] links in raw content
        for match in re.finditer(r"\[\[([^\]]+?)\]\]", n["raw"]):
            target_raw = match.group(1)
            # Strip display text: [[link|display]] -> link
            target = target_raw.split("|")[0].strip()
            # Normalize: remove .md, handle paths
            target_clean = target.removesuffix(".md").replace("\\", "/")
            # Try full path, then basename
            if target_clean in name_to_note:
                tgt = name_to_note[target_clean]
                tgt["incoming"].add(n["name"])
                tgt.setdefault("referenced_by", []).append(n["name"])
            else:
                # Try just basename
                base = Path(target_clean).stem
                if base in name_to_note:
                    tgt = name_to_note[base]
                    tgt["incoming"].add(n["name"])
                    tgt.setdefault("referenced_by", []).append(n["name"])


def find_orphans(notes: list[dict]) -> list[dict]:
    """Notes with zero incoming links."""
    return [n for n in notes if len(n.get("incoming", set())) == 0]


def find_missing_status(notes: list[dict]) -> list[dict]:
    """Notes without 'status' in frontmatter."""
    result = []
    for n in notes:
        if not has_frontmatter_field(n["frontmatter"], "status"):
            result.append(n)
    return result


def find_old_notes(notes: list[dict], days: int = 30) -> list[dict]:
    """Notes last modified more than `days` ago."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    return [n for n in notes if n["mtime"] < cutoff]


def find_empty_notes(notes: list[dict], min_chars: int = 50) -> list[dict]:
    """Notes with body shorter than min_chars."""
    return [n for n in notes if n["body_length"] < min_chars]


def generate_challenges(
    orphans: list,
    no_status: list,
    old_notes: list,
    empty_notes: list,
    total_notes: int,
) -> list[dict]:
    """Generate 3-5 specific challenges based on vault scan results."""
    challenges = []

    # Challenge 1: Orphan notes
    if orphans:
        n = min(len(orphans), 10)
        examples = [o["name"] for o in orphans[:5]]
        challenges.append({
            "title": "🔗 Vincular notas órfãs ao grafo de conhecimento",
            "description": (
                f"**{len(orphans)} notas** não têm nenhum link de entrada (órfãs). "
                f"Exemplos: {', '.join(examples)}. "
                "Revise cada uma e adicione links de/para outras notas relevantes no vault."
            ),
            "criteria": f"Vincular ao menos {n} notas órfãs a notas existentes via [[wiki-links]].",
            "time": "30–60 min",
            "priority": "🟡",
            "emoji": "🟡",
            "checkbox": "- [ ] ",
        })
    else:
        challenges.append({
            "title": "🔗 Verificação de notas órfãs",
            "description": "Nenhuma nota órfã encontrada. O grafo está saudável!",
            "criteria": "Manter a situação atual (zero órfãs).",
            "time": "5 min",
            "priority": "🟢",
            "emoji": "🟢",
            "checkbox": "- [ ] ",
        })

    # Challenge 2: Missing status
    if no_status:
        n = min(len(no_status), 10)
        examples = [o["name"] for o in no_status[:5]]
        challenges.append({
            "title": "📋 Adicionar status ao frontmatter das notas",
            "description": (
                f"**{len(no_status)} notas** não possuem o campo `status` no frontmatter. "
                f"Exemplos: {', '.join(examples)}. "
                "Adicione `status: rascunho | em_andamento | concluído` conforme o estágio de cada uma."
            ),
            "criteria": f"Adicionar `status` a pelo menos {n} notas.",
            "time": "20–40 min",
            "priority": "🟡",
            "emoji": "🟡",
            "checkbox": "- [ ] ",
        })

    # Challenge 3: Old notes
    if old_notes:
        n = min(len(old_notes), 10)
        examples = [o["name"] for o in old_notes[:5]]
        challenges.append({
            "title": "🕰️ Revisar notas desatualizadas (+30 dias)",
            "description": (
                f"**{len(old_notes)} notas** não são modificadas há mais de 30 dias. "
                f"Exemplos: {', '.join(examples)}. "
                "Revise o conteúdo, atualize informações desatualizadas e marque como revisado."
            ),
            "criteria": f"Revisar e atualizar ao menos {n} notas antigas.",
            "time": "30–60 min",
            "priority": "🟡",
            "emoji": "🟡",
            "checkbox": "- [ ] ",
        })

    # Challenge 4: Empty notes
    if empty_notes:
        n = min(len(empty_notes), 10)
        examples = [o["name"] for o in empty_notes[:5]]
        challenges.append({
            "title": "📝 Expandir notas vazias ou quase vazias",
            "description": (
                f"**{len(empty_notes)} notas** têm menos de 50 caracteres de conteúdo. "
                f"Exemplos: {', '.join(examples)}. "
                "Adicione conteúdo relevante: resumo, referências, links e exemplos práticos."
            ),
            "criteria": f"Expandir ao menos {n} notas com conteúdo significativo.",
            "time": "20–40 min",
            "priority": "🟡",
            "emoji": "🟡",
            "checkbox": "- [ ] ",
        })

    # Challenge 5: General health (always present if there are enough issues)
    total_issues = len(orphans) + len(no_status) + len(old_notes) + len(empty_notes)
    if total_issues > 30:
        challenges.append({
            "title": "🏗️ Limpeza geral e padronização do vault",
            "description": (
                f"No total, **{total_issues} pontos de melhoria** foram identificados "
                f"({len(orphans)} órfãs, {len(no_status)} sem status, "
                f"{len(old_notes)} desatualizadas, {len(empty_notes)} vazias). "
                "Reserve um bloco de tempo para tratar os lotes mais críticos."
            ),
            "criteria": f"Resolver ao menos 15 itens entre todas as categorias.",
            "time": "60–120 min",
            "priority": "🔴",
            "emoji": "🔴",
            "checkbox": "- [ ] ",
        })
    else:
        challenges.append({
            "title": "🏗️ Manutenção preventiva do vault",
            "description": (
                f"Vault saudável: apenas {total_issues} pontos de melhoria "
                f"({len(orphans)} órfãs, {len(no_status)} sem status, "
                f"{len(old_notes)} desatualizadas, {len(empty_notes)} vazias). "
                "Mantenha o ritmo de revisões regulares."
            ),
            "criteria": "Nenhuma ação corretiva urgente necessária.",
            "time": "15 min",
            "priority": "🟢",
            "emoji": "🟢",
            "checkbox": "- [ ] ",
        })

    # Limit to 5 challenges max
    return challenges[:5]


def format_date(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%d")


def generate_note_content(
    challenges: list[dict],
    orphans: list,
    no_status: list,
    old_notes: list,
    empty_notes: list,
    total_notes: int,
    week_start: str,
) -> str:
    """Generate the full markdown note content."""
    lines = []
    lines.append("---")
    lines.append(f'title: "Desafio Semanal — {week_start}"')
    lines.append(f'week: {week_start}')
    lines.append(f'generated: {format_date(datetime.now())}')
    lines.append(f'total_notes: {total_notes}')
    lines.append(f'orphans_found: {len(orphans)}')
    lines.append(f'no_status_found: {len(no_status)}')
    lines.append(f'old_notes_found: {len(old_notes)}')
    lines.append(f'empty_notes_found: {len(empty_notes)}')
    lines.append("tags: [desafio, semanal, manutencao, vault]")
    lines.append("status: rascunho")
    lines.append("---")
    lines.append("")
    lines.append(f"# 🎯 Desafio Semanal — Semana de {week_start}")
    lines.append("")
    lines.append("> Desafios gerados automaticamente com base no scan do vault.")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 📊 Resumo do Scan")
    lines.append("")
    lines.append(f"| Métrica | Valor |")
    lines.append(f"|---------|:-----:|")
    lines.append(f"| Total de notas | {total_notes} |")
    lines.append(f"| 🔗 Notas órfãs (sem incoming links) | {len(orphans)} |")
    lines.append(f"| 📋 Notas sem status | {len(no_status)} |")
    lines.append(f"| 🕰️ Notas desatualizadas (+30 dias) | {len(old_notes)} |")
    lines.append(f"| 📝 Notas vazias / quase vazias | {len(empty_notes)} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## ✅ Desafios da Semana")
    lines.append("")

    for i, ch in enumerate(challenges, 1):
        lines.append(f"### {ch['emoji']} Desafio {i}: {ch['title']}")
        lines.append("")
        lines.append(f"**Descrição:** {ch['description']}")
        lines.append("")
        lines.append(f"**Critério de conclusão:** {ch['criteria']}")
        lines.append("")
        lines.append(f"**Tempo estimado:** {ch['time']}  ·  **Prioridade:** {ch['priority']}")
        lines.append("")
        lines.append(f"{ch['checkbox']} Concluído")
        lines.append("")
        lines.append("---")
        lines.append("")

    lines.append("## 📋 Detalhamento dos Achados")
    lines.append("")

    if orphans:
        lines.append("### 🔗 Notas Órfãs")
        lines.append("")
        for o in orphans[:15]:
            lines.append(f"- `{o['rel']}`")
        if len(orphans) > 15:
            lines.append(f"- *...e mais {len(orphans) - 15} notas*")
        lines.append("")

    if no_status:
        lines.append("### 📋 Notas sem Status")
        lines.append("")
        for o in no_status[:15]:
            lines.append(f"- `{o['rel']}`")
        if len(no_status) > 15:
            lines.append(f"- *...e mais {len(no_status) - 15} notas*")
        lines.append("")

    if old_notes:
        lines.append("### 🕰️ Notas Desatualizadas (+30 dias)")
        lines.append("")
        for o in sorted(old_notes, key=lambda x: x["mtime"])[:15]:
            days_ago = (datetime.now(timezone.utc) - o["mtime"]).days
            lines.append(f"- `{o['rel']}` (última modificação: {format_date(o['mtime'])}, {days_ago}d atrás)")
        if len(old_notes) > 15:
            lines.append(f"- *...e mais {len(old_notes) - 15} notas*")
        lines.append("")

    if empty_notes:
        lines.append("### 📝 Notas Vazias ou Quase Vazias")
        lines.append("")
        for o in empty_notes[:15]:
            lines.append(f"- `{o['rel']}` ({o['body_length']} caracteres)")
        if len(empty_notes) > 15:
            lines.append(f"- *...e mais {len(empty_notes) - 15} notas*")
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("*Desafio gerado automaticamente pelo script `.scripts/challenge_generator.py`*")
    lines.append("")

    return "\n".join(lines)


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(
        description="Gera desafios semanais com base no scan do vault"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Regera o desafio mesmo se já existir um para esta semana"
    )
    args = parser.parse_args()

    # Calculate current week start (Monday)
    today = datetime.now()
    monday = today - timedelta(days=today.weekday())
    week_start_str = monday.strftime("%Y-%m-%d")

    # Output path
    ensure_dir(CHALLENGES_DIR)
    out_file = CHALLENGES_DIR / f"Desafio-Semanal-{week_start_str}.md"

    if out_file.exists() and not args.force:
        print(f"[AVISO] Desafio semanal ja existe: {out_file}")
        print(f"   Use --force para regenerar.")
        sys.exit(0)

    # ----- Scan vault -----
    print("[SCAN] Escaneando vault...")
    notes = collect_all_notes(VAULT_ROOT)
    total_notes = len(notes)
    print(f"   -> {total_notes} notas encontradas")

    # Link analysis
    scan_incoming_links(notes)

    # Find issues
    orphans = find_orphans(notes)
    no_status = find_missing_status(notes)
    old_notes = find_old_notes(notes, days=30)
    empty_notes = find_empty_notes(notes, min_chars=50)

    print(f"   -> {len(orphans)} orfas, {len(no_status)} sem status, "
          f"{len(old_notes)} desatualizadas, {len(empty_notes)} vazias")

    # Generate challenges
    challenges = generate_challenges(orphans, no_status, old_notes, empty_notes, total_notes)

    # Generate note content
    content = generate_note_content(
        challenges, orphans, no_status, old_notes, empty_notes,
        total_notes, week_start_str,
    )

    # Write file
    out_file.write_text(content, encoding="utf-8")
    print(f"[OK] Desafio semanal gerado: {out_file}")
    print(f"   -> {len(challenges)} desafios criados")


if __name__ == "__main__":
    main()
