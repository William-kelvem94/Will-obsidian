#!/usr/bin/env python3
"""
Sistema de Conquistas e Badges (E4)
Escaneia o vault, checa condições e desbloqueia badges
quando marcos são atingidos pela primeira vez.

Uso:
    python .scripts/achievement_system.py             # checa e desbloqueia
    python .scripts/achievement_system.py --force      # re-checa todos
    python .scripts/achievement_system.py --dry-run    # só preview
"""

import argparse
import json
import os
import re
import subprocess
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_DIR.parent
STATE_FILE = SCRIPT_DIR / "achievements_state.json"
CONQUISTAS_DIR = VAULT_ROOT / "Will-Pessoal" / "Conquistas"
README_PATH = CONQUISTAS_DIR / "README.md"

EXCLUDED_DIRS = {
    ".git", "__pycache__", "node_modules", ".obsidian", ".trash",
    ".scripts", ".agents", ".continue",
}

BADGES = [
    {
        "id": "primeiro-commit",
        "emoji": "\U0001F3C6",
        "name": "Primeiro Commit",
        "description": "Primeiro commit de todos no vault — o marco zero desta jornada.",
        "xp": 5,
        "condition": "check_primeiro_commit",
    },
    {
        "id": "100-notas",
        "emoji": "\U0001F331",
        "name": "100 Notas",
        "description": "O vault atingiu 100 notas .md. A semente foi plantada.",
        "xp": 10,
        "condition": "check_100_notas",
    },
    {
        "id": "500-notas",
        "emoji": "\U0001F33F",
        "name": "500 Notas",
        "description": "500 notas .md no vault. O conhecimento começa a florescer.",
        "xp": 25,
        "condition": "check_500_notas",
    },
    {
        "id": "1000-notas",
        "emoji": "\U0001F333",
        "name": "1000 Notas",
        "description": "Mil notas .md! Uma floresta de conhecimento.",
        "xp": 50,
        "condition": "check_1000_notas",
    },
    {
        "id": "streak-7",
        "emoji": "\U0001F525",
        "name": "Streak 7 Dias",
        "description": "Sete dias consecutivos com edições no vault. O hábito está se formando.",
        "xp": 15,
        "condition": "check_streak_7",
    },
    {
        "id": "streak-30",
        "emoji": "\U0001F525",
        "name": "Streak 30 Dias",
        "description": "30 dias consecutivos de atividade no vault. Disciplina inabalável.",
        "xp": 50,
        "condition": "check_streak_30",
    },
    {
        "id": "mestre-conexoes",
        "emoji": "\U0001F517",
        "name": "Mestre das Conexões",
        "description": "100 ou mais wikilinks espalhados pelo vault. As ideias estão se conectando.",
        "xp": 10,
        "condition": "check_mestre_conexoes",
    },
    {
        "id": "arquiteto-grafos",
        "emoji": "\U0001F517",
        "name": "Arquiteto de Grafos",
        "description": "500 ou mais wikilinks. O grafo de conhecimento está tomando forma.",
        "xp": 30,
        "condition": "check_arquiteto_grafos",
    },
    {
        "id": "bibliotecario",
        "emoji": "\U0001F4DA",
        "name": "Bibliotecário",
        "description": "10 ou mais domínios mapeados em Conhecimento-Geral. A biblioteca está organizada.",
        "xp": 15,
        "condition": "check_bibliotecario",
    },
    {
        "id": "polimata",
        "emoji": "\U0001F9E0",
        "name": "Polímata",
        "description": "5 ou mais domínios com status concluído. Conhecimento multidisciplinar.",
        "xp": 40,
        "condition": "check_polimata",
    },
    {
        "id": "primeiro-gap",
        "emoji": "\U0001F3AF",
        "name": "Primeiro Gap Fechado",
        "description": "O primeiro gap de conhecimento foi resolvido no GAPS.md.",
        "xp": 10,
        "condition": "check_primeiro_gap",
    },
    {
        "id": "escritor-fertil",
        "emoji": "\U0001F4DD",
        "name": "Escritor Fértil",
        "description": "Mais de 10.000 linhas de conteúdo escritas no vault.",
        "xp": 30,
        "condition": "check_escritor_fertil",
    },
    {
        "id": "consistencia-mensal",
        "emoji": "\U0001F504",
        "name": "Consistência Mensal",
        "description": "20 ou mais dias com edições em um único mês.",
        "xp": 25,
        "condition": "check_consistencia_mensal",
    },
    {
        "id": "power-user",
        "emoji": "\u26A1",
        "name": "Power User",
        "description": "Utiliza 5 ou mais funcionalidades diferentes do vault.",
        "xp": 20,
        "condition": "check_power_user",
    },
    {
        "id": "cartografo",
        "emoji": "\U0001F5FA\uFE0F",
        "name": "Cartógrafo",
        "description": "Três ou mais notas MOC/Índice criadas no vault.",
        "xp": 10,
        "condition": "check_cartografo",
    },
]


def run_command(cmd, cwd=None):
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd or VAULT_ROOT,
            capture_output=True, text=True, encoding="utf-8",
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"  [AVISO] Erro ao executar: {cmd} — {e}")
        return ""


def split_frontmatter(raw):
    fm_match = re.match(r"^---\s*\n(.*?)\n(?:---|\.\.\.)\s*\n?", raw, re.DOTALL)
    if fm_match:
        return fm_match.group(1), raw[fm_match.end():]
    return "", raw


def parse_frontmatter_value(fm_text, key):
    pattern = re.compile(
        rf"^{re.escape(key)}\s*:\s*(.*?)$", re.MULTILINE | re.IGNORECASE
    )
    m = pattern.search(fm_text)
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None


def collect_all_notes(vault_root):
    notes = []
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        parts = set(rel.parts)
        if parts & EXCLUDED_DIRS:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            try:
                raw = fpath.read_text(encoding="utf-8", errors="replace")
                notes.append({
                    "path": fpath,
                    "rel": str(rel / f),
                    "raw": raw,
                })
            except Exception:
                continue
    return notes


def count_md_files(vault_root):
    count = 0
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        if set(rel.parts) & EXCLUDED_DIRS:
            continue
        for f in files:
            if f.endswith(".md"):
                count += 1
    return count


def count_wikilinks(vault_root):
    total = 0
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        if set(rel.parts) & EXCLUDED_DIRS:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
                total += len(re.findall(r"\[\[.*?\]\]", text))
            except Exception:
                continue
    return total


def count_lines_of_content(vault_root):
    total = 0
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        if set(rel.parts) & EXCLUDED_DIRS:
            continue
        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            try:
                raw = fpath.read_text(encoding="utf-8", errors="replace")
                _, body = split_frontmatter(raw)
                total += len(body.strip().splitlines())
            except Exception:
                continue
    return total


def get_git_dates():
    output = run_command('git log --all --format="%ai"')
    if not output:
        return []
    dates = set()
    for line in output.splitlines():
        line = line.strip()
        if line:
            dates.add(line[:10])
    return sorted(dates)


def get_longest_streak(dates):
    if not dates:
        return 0
    date_objs = sorted(
        datetime.strptime(d, "%Y-%m-%d").date() for d in dates
    )
    longest = 1
    current = 1
    for i in range(1, len(date_objs)):
        diff = (date_objs[i] - date_objs[i - 1]).days
        if diff == 1:
            current += 1
            longest = max(longest, current)
        elif diff > 1:
            current = 1
    return longest


def get_days_per_month(dates):
    months = defaultdict(set)
    for d in dates:
        month_key = d[:7]
        months[month_key].add(d)
    return {k: len(v) for k, v in months.items()}


def detect_vault_features(vault_root):
    features = set()
    has_wikilink = False
    has_frontmatter = False
    has_tag = False
    has_dataview = False
    has_template = False
    has_mermaid = False
    has_checklist = False
    has_callout = False
    has_codeblock = False
    has_embed = False
    has_kanban = False

    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        if set(rel.parts) & EXCLUDED_DIRS:
            continue

        for f in files:
            if not f.endswith(".md"):
                continue
            fpath = Path(root) / f
            try:
                text = fpath.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue

            if not has_wikilink and re.search(r"\[\[.*?\]\]", text):
                has_wikilink = True
                features.add("wikilinks")
            if not has_frontmatter and re.match(r"^---\s*\n", text):
                has_frontmatter = True
                features.add("frontmatter")
            if not has_tag and re.search(r"(?:^|\s)#[a-zA-Z\u00C0-\u017F][\w\u00C0-\u017F-]*", text):
                has_tag = True
                features.add("tags")
            if not has_dataview and re.search(
                r"```(dataview|dataviewjs)\b", text, re.IGNORECASE
            ):
                has_dataview = True
                features.add("dataview")
            if not has_mermaid and re.search(r"```mermaid\b", text, re.IGNORECASE):
                has_mermaid = True
                features.add("mermaid")
            if not has_checklist and re.search(r"- \[[ x]\]", text):
                has_checklist = True
                features.add("checklists")
            if not has_callout and re.search(r">\s*\[!\w+\]", text):
                has_callout = True
                features.add("callouts")
            if not has_codeblock and re.search(r"```\w*$", text, re.MULTILINE):
                has_codeblock = True
                features.add("codeblocks")
            if not has_embed and re.search(r"!\[\[.*?\]\]", text):
                has_embed = True
                features.add("embeds")
            if not has_kanban and re.search(r"---\s*\n.*?kanban", text[:500], re.DOTALL | re.IGNORECASE):
                has_kanban = True
                features.add("kanban")

    if not has_template:
        template_dir = vault_root / "Templates"
        if template_dir.exists():
            has_template = True
            features.add("templates")

    return features


def count_index_notes(vault_root):
    count = 0
    for root, dirs, files in os.walk(vault_root):
        rel = Path(root).relative_to(vault_root)
        if set(rel.parts) & EXCLUDED_DIRS:
            continue
        for f in files:
            if f.lower() in ("index.md", "moc.md", "mapa.md", "indice.md", "índice.md"):
                count += 1
            elif "index" in f.lower() and f.endswith(".md"):
                count += 1
    return count


def check_primeiro_commit():
    output = run_command('git log --all --oneline')
    return bool(output and len(output.splitlines()) >= 1)


def check_100_notas():
    return count_md_files(VAULT_ROOT) >= 100


def check_500_notas():
    return count_md_files(VAULT_ROOT) >= 500


def check_1000_notas():
    return count_md_files(VAULT_ROOT) >= 1000


def check_streak_7():
    dates = get_git_dates()
    return get_longest_streak(dates) >= 7


def check_streak_30():
    dates = get_git_dates()
    return get_longest_streak(dates) >= 30


def check_mestre_conexoes():
    return count_wikilinks(VAULT_ROOT) >= 100


def check_arquiteto_grafos():
    return count_wikilinks(VAULT_ROOT) >= 500


def check_bibliotecario():
    conhecimento_dir = VAULT_ROOT / "Conhecimento-Geral"
    if not conhecimento_dir.exists():
        return False
    domains = [
        d for d in conhecimento_dir.iterdir()
        if d.is_dir() and not d.name.startswith(".")
    ]
    return len(domains) >= 10


def check_polimata():
    conhecimento_dir = VAULT_ROOT / "Conhecimento-Geral"
    if not conhecimento_dir.exists():
        return False
    domains_concluidos = 0
    for domain_dir in conhecimento_dir.iterdir():
        if not domain_dir.is_dir() or domain_dir.name.startswith("."):
            continue
        for root, dirs, files in os.walk(domain_dir):
            for f in files:
                if not f.endswith(".md"):
                    continue
                fpath = Path(root) / f
                try:
                    raw = fpath.read_text(encoding="utf-8", errors="replace")
                except Exception:
                    continue
                fm, _ = split_frontmatter(raw)
                if fm:
                    status_val = parse_frontmatter_value(fm, "status")
                    if status_val and re.search(
                        r"conclu[ií]do", status_val, re.IGNORECASE
                    ):
                        domains_concluidos += 1
                        break
    return domains_concluidos >= 5


def check_primeiro_gap():
    gaps_path = VAULT_ROOT / "GAPS.md"
    if not gaps_path.exists():
        return False
    raw = gaps_path.read_text(encoding="utf-8", errors="replace")
    has_resolved = re.search(
        r"(?:gap|lacuna|resolvido|fechado|concluído).*?:?\s*\d+",
        raw, re.IGNORECASE
    )
    if has_resolved:
        return True
    if re.search(r"Nenhum gap detectado", raw) or re.search(
        r"100% coberta", raw
    ):
        output = run_command('git log --all --oneline -- "GAPS.md"')
        if output:
            return True
        return False
    return False


def check_escritor_fertil():
    return count_lines_of_content(VAULT_ROOT) >= 10000


def check_consistencia_mensal():
    dates = get_git_dates()
    days_per_month = get_days_per_month(dates)
    return any(v >= 20 for v in days_per_month.values())


def check_power_user():
    features = detect_vault_features(VAULT_ROOT)
    return len(features) >= 5


def check_cartografo():
    return count_index_notes(VAULT_ROOT) >= 3


CONDITION_MAP = {
    "check_primeiro_commit": check_primeiro_commit,
    "check_100_notas": check_100_notas,
    "check_500_notas": check_500_notas,
    "check_1000_notas": check_1000_notas,
    "check_streak_7": check_streak_7,
    "check_streak_30": check_streak_30,
    "check_mestre_conexoes": check_mestre_conexoes,
    "check_arquiteto_grafos": check_arquiteto_grafos,
    "check_bibliotecario": check_bibliotecario,
    "check_polimata": check_polimata,
    "check_primeiro_gap": check_primeiro_gap,
    "check_escritor_fertil": check_escritor_fertil,
    "check_consistencia_mensal": check_consistencia_mensal,
    "check_power_user": check_power_user,
    "check_cartografo": check_cartografo,
}


def load_state():
    if STATE_FILE.exists():
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return data
        except (json.JSONDecodeError, ValueError):
            pass
    return {}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(
        json.dumps(state, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def generate_badge_note(badge, date_unlocked):
    content = f"""---
title: "{badge['emoji']} {badge['name']}"
date: {date_unlocked}
tags: [conquista, badge]
xp_reward: {badge['xp']}
---

# {badge['emoji']} {badge['name']}

**Desbloqueado em:** {date_unlocked}
**Recompensa:** +{badge['xp']} XP

---

{badge['description']}

## O que isso significa

Esta conquista representa um marco importante na jornada de conhecimento dentro deste vault. Cada badge é um lembrete do progresso contínuo e da dedicação em construir um segundo cérebro cada vez mais rico e conectado.

## Próximos Passos

Continue explorando, escrevendo e conectando ideias. Novas conquistas esperam por você!
"""
    return content


def generate_badge_note_content(badge, date_unlocked):
    return f"""---
title: "{badge['emoji']} {badge['name']}"
date: {date_unlocked}
tags: [conquista, badge]
xp_reward: {badge['xp']}
---

# {badge['emoji']} {badge['name']}

**Desbloqueado em:** {date_unlocked}
**Recompensa:** +{badge['xp']} XP

---

{badge['description']}

## O que isso significa

Esta conquista representa um marco importante na jornada de conhecimento dentro deste vault. Cada badge é um lembrete do progresso contínuo e da dedicação em construir um segundo cérebro cada vez mais rico e conectado.

## Próximos Passos

Continue explorando, escrevendo e conectando ideias. Novas conquistas esperam por você!
"""


def generate_readme(unlocked_badges, locked_badges, total_xp):
    unlocked_count = len(unlocked_badges)
    total_count = len(unlocked_badges) + len(locked_badges)

    unlocked_sorted = sorted(unlocked_badges, key=lambda b: b["date_unlocked"])
    locked_sorted = sorted(locked_badges, key=lambda b: b["name"])

    lines = [
        "---",
        "title: \"\U0001F3C6 Central de Conquistas\"",
        "description: \"Galeria de todas as conquistas e badges desbloqueados no vault.\"",
        "tags: [conquista, badge, hub, galeria]",
        f"updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d')}",
        f"total_badges: {unlocked_count}/{total_count}",
        f"total_xp: {total_xp}",
        "---",
        "",
        "# \U0001F3C6 Central de Conquistas",
        "",
        f"> **{unlocked_count} de {total_count} badges desbloqueados** | **{total_xp} XP total**",
        "",
        "---",
        "",
        "## \U0001F514 Badges Desbloqueados",
        "",
    ]

    for b in unlocked_sorted:
        lines.append(f"- {b['emoji']} **{b['name']}** — {b['date_unlocked']} (+{b['xp']} XP)")

    if locked_sorted:
        lines.extend([
            "",
            "---",
            "",
            "## \U0001F512 Badges Bloqueados",
            "",
        ])
        for b in locked_sorted:
            lines.append(f"- ~~{b['emoji']} {b['name']}~~ (+{b['xp']} XP)")

    lines.extend([
        "",
        "---",
        "",
        "*Atualizado automaticamente em "
        f"{datetime.now(timezone.utc).strftime('%d/%m/%Y %H:%M')}*",
        "",
    ])

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Sistema de Conquistas e Badges do Vault"
    )
    parser.add_argument(
        "--force", action="store_true",
        help="Re-checa todos os badges mesmo se já desbloqueados"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Apenas mostra o que seria desbloqueado, sem criar nada"
    )
    args = parser.parse_args()

    state = load_state()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    sys.stdout.reconfigure(encoding="utf-8")
    print("=" * 50)
    print("  [TROFEU] SISTEMA DE CONQUISTAS E BADGES")
    print("=" * 50)

    if args.dry_run:
        print("  [DRY RUN] Nenhuma alteracao sera feita.\n")
    if args.force:
        print("  [FORCE] Re-checando todos os badges.\n")

    newly_unlocked = []
    already_unlocked = []
    not_unlocked = []

    for badge in BADGES:
        badge_id = badge["id"]
        check_fn = CONDITION_MAP[badge["condition"]]
        is_unlocked = check_fn()

        already_in_state = badge_id in state

        if already_in_state and not args.force:
            already_unlocked.append({
                **badge,
                "date_unlocked": state[badge_id]["date_unlocked"],
            })
            continue

        if is_unlocked:
            if not already_in_state or args.force:
                newly_unlocked.append(badge)
            else:
                already_unlocked.append({
                    **badge,
                    "date_unlocked": state[badge_id]["date_unlocked"],
                })
        else:
            not_unlocked.append(badge)

    CONQUISTAS_DIR.mkdir(parents=True, exist_ok=True)

    for badge in newly_unlocked:
        note_content = generate_badge_note_content(badge, today)
        filename = f"{badge['name'].replace(' ', '-').replace('/', '-')}.md"
        filepath = CONQUISTAS_DIR / filename

        if args.dry_run:
                print(f"  [PREVIEW] Desbloquearia: {badge['emoji']} {badge['name']} (+{badge['xp']} XP)")
        else:
                filepath.write_text(note_content, encoding="utf-8")
                print(f"  [OK] Desbloqueado: {badge['emoji']} {badge['name']} (+{badge['xp']} XP)")
                state[badge["id"]] = {
                "name": badge["name"],
                "date_unlocked": today,
                "xp": badge["xp"],
            }

    if newly_unlocked and not args.dry_run:
        save_state(state)

    all_unlocked = [
        {**b, "date_unlocked": state[b["id"]]["date_unlocked"]}
        for b in BADGES
        if b["id"] in state
    ]
    xp_total = sum(b["xp"] for b in BADGES if b["id"] in state)
    locked_badges = [b for b in BADGES if b["id"] not in state]

    readme_content = generate_readme(all_unlocked, locked_badges, xp_total)

    if args.dry_run:
        print(f"\n  [PREVIEW] Geraria README com {len(all_unlocked)} badges desbloqueados e {xp_total} XP")
        print("  [PREVIEW] Badges bloqueados:", len(locked_badges))
    else:
        README_PATH.write_text(readme_content, encoding="utf-8")
        print(f"\n  [OK] README atualizado: {len(all_unlocked)}/{len(BADGES)} badges, {xp_total} XP total")

    if not newly_unlocked and not args.dry_run:
        print("\n  Nenhum badge novo desbloqueado desta vez.")

    print("=" * 50)
    print("  Concluído!")
    print("=" * 50)


if __name__ == "__main__":
    main()
