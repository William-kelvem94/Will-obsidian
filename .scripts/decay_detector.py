#!/usr/bin/env python3
"""
Detector de Decaimento de Conhecimento (B3)
Escaneia arquivos .md do vault e marca como stale/archived
com base no tempo desde a última modificação.
"""

import os
import sys
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
REPORT_FILE = VAULT_PATH / "decay_report.md"
BACKUP_DIR = SCRIPT_ROOT / "frontmatter_backups"

STALE_THRESHOLD = 60
ARCHIVED_THRESHOLD = 90

EXCLUDE_DIRS = {
    '.git', '.obsidian', '.scripts', '__pycache__',
    '.github', 'node_modules', '.pytest_cache',
}

REPORT_TEMPLATE = """# 🕰️ Relatório de Decaimento de Conhecimento

**Gerado em:** {generated}
**Threshold Stale:** > {stale} dias
**Threshold Archived:** > {archived} dias

---

## 📊 Visão Geral

| Status | Quantidade | Percentual |
|--------|------------|------------|
| **Saudável** (≤ {stale} dias) | {healthy} | {healthy_pct:.1f}% |
| **Stale** (> {stale} dias) | {stale_count} | {stale_pct:.1f}% |
| **Archived** (> {archived} dias) | {archived_count} | {archived_pct:.1f}% |
| **Total** | {total} | 100% |

---

## ⚠️ Notas Stale

> *Nenhuma nota stale encontrada.*
""" if False else ""  # placeholder — generated in code

NOTA_STALE_ROW = "| {path} | {days}d | {action} |\n"
NOTA_ARCHIVED_ROW = "| {path} | {days}d | {action} |\n"

STALE_ACTION = "Revisar e atualizar ou arquivar manualmente"
ARCHIVED_ACTION = "Revisar conteúdo; mover para archive se obsoleto"


def parse_frontmatter(content):
    """Retorna (frontmatter_dict, body_start_line, has_frontmatter)"""
    lines = content.split('\n')
    if not lines or lines[0].strip() != '---':
        return {}, 0, False

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == '---':
            end_idx = i
            break

    if end_idx is None:
        return {}, 0, False

    fm_lines = lines[1:end_idx]
    fm_dict = {}
    for line in fm_lines:
        if ':' in line:
            key, _, val = line.partition(':')
            fm_dict[key.strip()] = val.strip()

    return fm_dict, end_idx, True


def build_frontmatter(fm_dict):
    """Constrói string YAML a partir do dicionário"""
    if not fm_dict:
        return '---\n---\n'
    lines = ['---']
    for k, v in fm_dict.items():
        lines.append(f"{k}: {v}")
    lines.append('---')
    return '\n'.join(lines) + '\n'


def set_status_in_frontmatter(fm_dict, status):
    """Define/atualiza o campo status no frontmatter"""
    fm_dict['status'] = status
    return fm_dict


def should_skip(filepath):
    """Verifica se o arquivo deve ser ignorado"""
    rel = filepath.relative_to(VAULT_PATH)
    for part in rel.parts:
        if part in EXCLUDE_DIRS:
            return True
    if filepath.name == 'decay_report.md':
        return True
    return False


def read_file_safe(filepath):
    """Tenta ler arquivo com diferentes encodings"""
    for enc in ('utf-8', 'latin-1', 'cp1252'):
        try:
            return filepath.read_text(encoding=enc)
        except (UnicodeDecodeError, ValueError):
            continue
    return filepath.read_text(encoding='utf-8', errors='replace')


def get_file_info(filepath):
    """Retorna (days_since_mod, status_atual_do_frontmatter)"""
    mtime = datetime.fromtimestamp(filepath.stat().st_mtime, tz=timezone.utc)
    days_since = (datetime.now(timezone.utc) - mtime).days

    content = read_file_safe(filepath)
    fm_dict, _, _ = parse_frontmatter(content)
    current_status = fm_dict.get('status', '').strip().lower()

    return days_since, current_status, fm_dict, content


def backup_frontmatter(filepath, fm_dict):
    """Salva backup do frontmatter original antes de modificar"""
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)

    rel_path = str(filepath.relative_to(VAULT_PATH)).replace('\\', '/')
    safe_name = rel_path.replace('/', '__').replace('\\', '__')
    backup_file = BACKUP_DIR / f"{safe_name}.json"

    backup_data = {
        'file': rel_path,
        'backup_time': datetime.now().isoformat(),
        'frontmatter': fm_dict,
    }

    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(backup_data, f, ensure_ascii=False, indent=2)

    return backup_file


def update_file_frontmatter(filepath, new_fm_dict, dry_run=False):
    """Atualiza o frontmatter do arquivo com o novo dicionário"""
    content = read_file_safe(filepath)
    _, end_idx, has_fm = parse_frontmatter(content)

    new_fm = build_frontmatter(new_fm_dict)

    if has_fm:
        lines = content.split('\n')
        body = '\n'.join(lines[end_idx + 1:]).strip()
        new_content = new_fm + body + '\n'
    else:
        new_content = new_fm + content.strip() + '\n'

    if not dry_run:
        filepath.write_text(new_content, encoding='utf-8')

    return new_content


def scan_vault(dry_run=False, stale_threshold=STALE_THRESHOLD):
    """Escaneia todo o vault e processa arquivos"""
    archived_threshold = ARCHIVED_THRESHOLD

    healthy = []
    stale = []
    archived = []
    modified_files = []

    md_files = sorted(VAULT_PATH.rglob("*.md"))

    print(f"[SCAN] Escaneando {len(md_files)} arquivos .md...")

    for filepath in md_files:
        if should_skip(filepath):
            continue

        days_since, current_status, fm_dict, content = get_file_info(filepath)

        if days_since <= stale_threshold:
            healthy.append(filepath)
            continue

        if days_since > archived_threshold:
            new_status = 'archived'
        else:
            new_status = 'stale'

        if current_status == new_status:
            healthy.append(filepath)
            continue

        fm_dict = set_status_in_frontmatter(fm_dict, new_status)

        backup_frontmatter(filepath, fm_dict)

        update_file_frontmatter(filepath, fm_dict, dry_run=dry_run)

        modified_files.append((filepath, days_since, new_status))

        if new_status == 'stale':
            stale.append((filepath, days_since))
        else:
            archived.append((filepath, days_since))

    return healthy, stale, archived, modified_files


def generate_report(healthy, stale, archived, modified_files,
                    stale_threshold=STALE_THRESHOLD):
    """Gera o relatório markdown"""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    archived_threshold = ARCHIVED_THRESHOLD

    total = len(healthy) + len(stale) + len(archived)
    healthy_pct = (len(healthy) / total * 100) if total else 0
    stale_pct = (len(stale) / total * 100) if total else 0
    archived_pct = (len(archived) / total * 100) if total else 0

    md = f"""---
title: "Relatório de Decaimento de Conhecimento"
description: "Relatório automático de notas stale e archived no vault"
tags: [report, decay, auto-generated]
generated: {now}
---

# 🕰️ Relatório de Decaimento de Conhecimento

**Gerado em:** {now}
**Threshold Stale:** > {stale_threshold} dias
**Threshold Archived:** > {archived_threshold} dias

---

## 📊 Visão Geral

| Status | Quantidade | Percentual |
|--------|------------|------------|
| **Saudável** (≤ {stale_threshold} dias) | {len(healthy)} | {healthy_pct:.1f}% |
| **Stale** (> {stale_threshold} dias) | {len(stale)} | {stale_pct:.1f}% |
| **Archived** (> {archived_threshold} dias) | {len(archived)} | {archived_pct:.1f}% |
| **Total** | {total} | 100% |

"""

    if stale:
        md += "## ⚠️ Notas Stale\n\n"
        md += "| Arquivo | Dias sem edição | Ação Sugerida |\n"
        md += "|---------|----------------|---------------|\n"
        for filepath, days in sorted(stale, key=lambda x: x[1], reverse=True):
            rel = str(filepath.relative_to(VAULT_PATH)).replace('\\', '/')
            md += f"| `{rel}` | {days}d | Revisar e atualizar ou arquivar manualmente |\n"
        md += "\n"

    if archived:
        md += "---\n\n## 🗄️ Notas Archivadas\n\n"
        md += "| Arquivo | Dias sem edição | Ação Sugerida |\n"
        md += "|---------|----------------|---------------|\n"
        for filepath, days in sorted(archived, key=lambda x: x[1], reverse=True):
            rel = str(filepath.relative_to(VAULT_PATH)).replace('\\', '/')
            md += f"| `{rel}` | {days}d | Revisar conteúdo; mover para archive se obsoleto |\n"
        md += "\n"

    if not stale and not archived:
        md += "## ✅ Todas as notas estão saudáveis!\n\n"
        md += "Nenhuma nota stale ou archived encontrada.\n\n"

    if modified_files:
        md += "---\n\n## 📝 Arquivos Modificados\n\n"
        md += "| Arquivo | Status | Dias sem edição |\n"
        md += "|---------|--------|----------------|\n"
        for filepath, days, status in sorted(modified_files, key=lambda x: x[1], reverse=True):
            rel = str(filepath.relative_to(VAULT_PATH)).replace('\\', '/')
            md += f"| `{rel}` | `{status}` | {days}d |\n"
        md += "\n"

    md += f"""---

## 🔗 Links Relacionados

- [[JARVIS/02-Operational/Dashboard|Dashboard]] — Estado operacional
- [[JARVIS/03-Memory/Logs/INDEX|Índice de Logs]] — Todos os registros

---

*Relatório gerado automaticamente por `.scripts/decay_detector.py`*
*Para reexecutar: `python .scripts/decay_detector.py`*
"""

    return md


def main():
    """Execução principal"""
    import argparse

    parser = argparse.ArgumentParser(
        description='Detector de Decaimento de Conhecimento para Obsidian'
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Apenas simula as alterações sem modificar arquivos'
    )
    parser.add_argument(
        '--threshold', type=int, default=STALE_THRESHOLD,
        help=f'Threshold de dias para considerar stale (padrão: {STALE_THRESHOLD})'
    )
    args = parser.parse_args()

    stale_threshold = args.threshold
    dry_run = args.dry_run

    if dry_run:
        print("[DRY-RUN] Modo seco — Nenhum arquivo sera modificado\n")
    else:
        print("[SCAN] Iniciando deteccao de decaimento...\n")

    healthy, stale, archived, modified = scan_vault(
        dry_run=dry_run, stale_threshold=stale_threshold
    )

    if dry_run:
        print("\n[DRY-RUN] Alteracoes que seriam feitas:\n")
        if modified:
            for filepath, days, status in sorted(modified, key=lambda x: x[1], reverse=True):
                rel = str(filepath.relative_to(VAULT_PATH)).replace('\\', '/')
                print(f"  [{status:>8}] {rel} ({days} dias sem edição)")
        else:
            print("  Nenhuma alteração necessária.")
    else:
        print(f"\n[OK] Varredura concluida!")
        print(f"   Saudáveis: {len(healthy)}")
        print(f"   Stale:     {len(stale)}")
        print(f"   Archived:  {len(archived)}")
        print(f"   Modificados: {len(modified)}")

    report = generate_report(
        healthy, stale, archived, modified,
        stale_threshold=stale_threshold
    )

    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(report)

    rel_report = str(REPORT_FILE.relative_to(VAULT_PATH)).replace('\\', '/')
    print(f"\n[OK] Relatorio gerado: {rel_report}")


if __name__ == "__main__":
    main()
