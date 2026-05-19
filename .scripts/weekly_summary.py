#!/usr/bin/env python3
"""
Resumo Semanal Automático — Gera um resumo das atividades da semana no vault.
Execução: todo domingo (ou sob demanda).
"""

import os
import subprocess
import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import Counter

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
LOGS_DIR = VAULT_PATH / "JARVIS" / "03-Memory" / "Logs"
OUTPUT_FILE = LOGS_DIR / f"Resumo-Semanal-{datetime.now().strftime('%Y-%m-%d')}.md"


def run_command(cmd, cwd=None):
    """Executa comando shell e retorna a saída"""
    try:
        result = subprocess.run(
            cmd, shell=True, cwd=cwd or VAULT_PATH,
            capture_output=True, text=True, encoding='utf-8'
        )
        return result.stdout.strip()
    except Exception as e:
        print(f"Erro ao executar comando '{cmd}': {e}")
        return ""


def get_weekly_commits():
    """Obtém todos os commits dos últimos 7 dias"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --pretty=format:"%h|%s|%an|%ar" --all'
    output = run_command(cmd)

    commits = []
    if output:
        for line in output.split('\n'):
            if line:
                parts = line.split('|')
                if len(parts) == 4:
                    commits.append({
                        'hash': parts[0],
                        'message': parts[1],
                        'author': parts[2],
                        'time': parts[3]
                    })
    return commits


def get_weekly_stats():
    """Obtém estatísticas git da última semana"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --shortstat --all'
    output = run_command(cmd)

    total_files = 0
    total_insertions = 0
    total_deletions = 0

    for line in output.split('\n'):
        if 'changed' in line or 'alterado' in line:
            files_match = re.search(r'(\d+) ficheiro', line) or re.search(r'(\d+) file', line)
            ins_match = re.search(r'(\d+) inser', line) or re.search(r'(\d+) insertion', line)
            del_match = re.search(r'(\d+) dele', line) or re.search(r'(\d+) deletion', line)

            if files_match:
                total_files += int(files_match.group(1))
            if ins_match:
                total_insertions += int(ins_match.group(1))
            if del_match:
                total_deletions += int(del_match.group(1))

    return {'files': total_files, 'insertions': total_insertions, 'deletions': total_deletions}


def get_new_md_files():
    """Lista arquivos .md criados nos últimos 7 dias"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --diff-filter=A --name-only --pretty=format: --all -- "*.md"'
    output = run_command(cmd)

    files = set()
    if output:
        for line in output.split('\n'):
            if line.strip():
                files.add(line.strip())
    return sorted(files)


def get_folder_activity():
    """Conta alterações por pasta raiz"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --name-only --pretty=format: --all'
    output = run_command(cmd)

    folders = Counter()
    if output:
        for line in output.split('\n'):
            if line.strip() and not line.startswith(' '):
                parts = line.replace('\\', '/').split('/')
                if len(parts) >= 2:
                    folders[parts[0]] += 1
                else:
                    folders['Raiz'] += 1
    return folders.most_common()


def get_changed_files():
    """Lista todos os arquivos alterados na última semana"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --name-only --pretty=format: --all'
    output = run_command(cmd)

    files = set()
    if output:
        for line in output.split('\n'):
            if line.strip() and not line.startswith(' '):
                files.add(line.strip())
    return sorted(files)


def detect_active_projects(files):
    """Detecta projetos ativos a partir dos caminhos de arquivos"""
    projects = Counter()

    for filepath in files:
        parts = filepath.replace('\\', '/').split('/')
        if len(parts) < 2:
            continue

        if parts[0] == 'Projetos' and len(parts) >= 3:
            project = parts[2] if parts[1] in ('01-Ativos', 'Privados') else parts[1]
            projects[project] += 1
        elif parts[0] == 'JARVIS':
            projects['JARVIS'] += 1
        elif parts[0] == 'skills':
            projects['Skills'] += 1
        elif parts[0] in ('Conhecimento-Geral', 'Will-Pessoal', 'Templates', 'dashboards'):
            projects[parts[0]] += 1
        elif parts[0] == 'Projetos':
            projects['Projetos'] += 1

    return projects.most_common()


def get_authors():
    """Lista autores com contagem de commits na semana"""
    since = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    cmd = f'git log --since="{since}" --pretty=format:"%an" --all'
    output = run_command(cmd)

    authors = Counter()
    if output:
        for line in output.split('\n'):
            if line.strip():
                authors[line.strip()] += 1
    return authors.most_common()


def generate_weekly_summary():
    """Gera o resumo semanal em markdown"""
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    week_start = (now - timedelta(days=7)).strftime("%Y-%m-%d")

    commits = get_weekly_commits()
    stats = get_weekly_stats()
    new_md = get_new_md_files()
    folder_activity = get_folder_activity()
    changed_files = get_changed_files()
    active_projects = detect_active_projects(changed_files)
    authors = get_authors()
    total_commits = len(commits)

    md = f"""---
title: "Resumo Semanal — {date_str}"
description: "Resumo automático das atividades da semana de {week_start} a {date_str}"
tags: [log, weekly, resumo, auto-generated]
generated: {now.strftime("%Y-%m-%d %H:%M:%S")}
---

# 📊 Resumo Semanal — {date_str}

**Período:** {week_start} a {date_str}
**Gerado em:** {now.strftime("%H:%M:%S")}

---

## 📈 Estatísticas da Semana

| Métrica | Valor |
|---------|-------|
| **Total de Commits** | {total_commits} |
| **Arquivos Alterados** | {stats['files']} |
| **Linhas Adicionadas** | +{stats['insertions']} |
| **Linhas Removidas** | -{stats['deletions']} |
| **Saldo Líquido** | {stats['insertions'] - stats['deletions']:+d} |
| **Novas Notas (.md)** | {len(new_md)} |
| **Pastas com Atividade** | {len(folder_activity)} |

"""

    if authors:
        md += "### 👥 Autores\n\n"
        for author, count in authors:
            md += f"- **{author}** ({count} commits)\n"
        md += "\n"

    if active_projects:
        md += "---\n\n## 🎯 Top 5 Projetos em Atividade\n\n"
        for project, count in active_projects[:5]:
            md += f"- **{project}** ({count} toques)\n"
        md += "\n"

    if new_md:
        md += "---\n\n## 🆕 Novas Notas Criadas\n\n"
        for filepath in new_md[:25]:
            wiki_path = filepath.replace('\\', '/')[:-3]
            display_name = Path(filepath).stem
            md += f"- [[{wiki_path}|{display_name}]]\n"
        if len(new_md) > 25:
            md += f"- *...e mais {len(new_md) - 25} notas*\n"
        md += "\n"

    if folder_activity:
        md += "---\n\n## 📂 Pastas com Mais Atividade\n\n"
        md += "| Pasta | Arquivos Alterados |\n"
        md += "|-------|-------------------|\n"
        for folder, count in folder_activity[:10]:
            md += f"| **{folder}/** | {count} |\n"
        md += "\n"

    if commits:
        md += f"---\n\n## 📝 Commits da Semana ({total_commits} no total)\n\n"
        for commit in commits[:20]:
            md += f"### `{commit['hash']}` — {commit['author']} ({commit['time']})\n"
            md += f"{commit['message']}\n\n"
        if total_commits > 20:
            md += f"*...e mais {total_commits - 20} commits*\n\n"

    md += f"""---

## 🔗 Links Relacionados

- [[JARVIS/02-Operational/Dashboard|Dashboard]] — Estado operacional atual
- [[JARVIS/02-Operational/Context/Estado|Contexto]] — Foco atual
- [[JARVIS/03-Memory/Logs/INDEX|Índice de Logs]] — Todos os registros
- [[{date_str}|Log Diário — {date_str}]] — Log do dia

---

*Este resumo foi gerado automaticamente por `.scripts/weekly_summary.py`*
*Para regenerar, execute: `python .scripts/weekly_summary.py`*
"""

    return md


def main():
    """Execução principal"""
    print("[GEN] Gerando resumo semanal...")

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    content = generate_weekly_summary()

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"[OK] Resumo semanal gerado: {OUTPUT_FILE.relative_to(VAULT_PATH)}")
    print("[INFO] Para executar manualmente: python .scripts/weekly_summary.py")


if __name__ == "__main__":
    main()
