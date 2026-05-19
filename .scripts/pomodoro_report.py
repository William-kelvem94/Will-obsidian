#!/usr/bin/env python3
"""
Pomodoro Report Generator — Gera um relatório semanal de pomodoros.
Lê as notas diárias (#diario) e extrai checklists com a tag #pomodoro.
Gera um resumo em JARVIS/03-Memory/Logs/Pomodoro-Report-YYYY-MM-DD.md.
"""

import re
from datetime import datetime, timedelta
from pathlib import Path
from collections import defaultdict

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
LOGS_DIR = VAULT_PATH / "JARVIS" / "03-Memory" / "Logs"
OUTPUT_FILE = LOGS_DIR / f"Pomodoro-Report-{datetime.now().strftime('%Y-%m-%d')}.md"


def find_daily_notes():
    """Encontra todas as notas diárias com #diario no frontmatter"""
    # Procura por arquivos com tag diario no frontmatter
    daily_notes = []
    for md_file in sorted(VAULT_PATH.rglob("*.md")):
        rel_path = md_file.relative_to(VAULT_PATH)
        # Ignora templates e scripts
        if str(rel_path).startswith("Templates") or str(rel_path).startswith(".scripts"):
            continue
        try:
            content = md_file.read_text(encoding="utf-8")
            # Verifica se tem #diario no frontmatter (entre ---)
            if "#diario" in content.split("---")[1] if content.startswith("---") else False:
                daily_notes.append((rel_path, content))
        except (IndexError, UnicodeDecodeError, OSError):
            continue
    return daily_notes


def extract_pomodoros(content):
    """Extrai checklists #pomodoro do conteúdo da nota"""
    tasks = []
    pattern = re.compile(
        r"^- \[([ x])\]\s*(.*?):\s*(\d+)\s*pomodoros?\s*#pomodoro",
        re.MULTILINE | re.IGNORECASE
    )
    for match in pattern.finditer(content):
        tasks.append({
            "completed": match.group(1) == "x",
            "project": match.group(2).strip(),
            "count": int(match.group(3)),
        })
    return tasks


def get_week_range(ref_date=None):
    """Retorna início (segunda) e fim (domingo) da semana"""
    if ref_date is None:
        ref_date = datetime.now()
    start = ref_date - timedelta(days=ref_date.weekday())
    end = start + timedelta(days=6)
    return start, end


def generate_report():
    """Gera o relatório semanal de pomodoros"""
    now = datetime.now()
    week_start, week_end = get_week_range(now)
    last_week_start = week_start - timedelta(days=7)
    last_week_end = week_start - timedelta(days=1)
    month_start = now.replace(day=1)

    daily_notes = find_daily_notes()
    all_by_date = []
    weekly_data = []
    last_week_data = []
    monthly_data = []

    for rel_path, content in daily_notes:
        date_match = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", content)
        if not date_match:
            continue
        try:
            note_date = datetime.strptime(date_match.group(1), "%Y-%m-%d")
        except ValueError:
            continue
        tasks = extract_pomodoros(content)
        if not tasks:
            continue
        for t in tasks:
            t["date"] = note_date
            t["file"] = str(rel_path)
            all_by_date.append(t)
            if week_start <= note_date <= week_end:
                weekly_data.append(t)
            if last_week_start <= note_date <= last_week_end:
                last_week_data.append(t)
            if note_date >= month_start:
                monthly_data.append(t)

    # Agregações
    total_week = sum(t["count"] for t in weekly_data)
    total_last_week = sum(t["count"] for t in last_week_data)
    total_month = sum(t["count"] for t in monthly_data)
    total_all = sum(t["count"] for t in all_by_date)

    # Por projeto (semana)
    proj_week = defaultdict(int)
    for t in weekly_data:
        proj_week[t["project"]] += t["count"]

    # Por projeto (total)
    proj_total = defaultdict(int)
    for t in all_by_date:
        proj_total[t["project"]] += t["count"]

    # Dias com pomodoro na semana
    days_with_pomodoro = set()
    for t in weekly_data:
        days_with_pomodoro.add(t["date"].strftime("%Y-%m-%d"))

    # Últimos 7 dias
    last_7 = []
    for i in range(6, -1, -1):
        day = now - timedelta(days=i)
        day_total = sum(
            t["count"] for t in all_by_date
            if t["date"].strftime("%Y-%m-%d") == day.strftime("%Y-%m-%d")
        )
        last_7.append((day.strftime("%a %d/%m"), day_total))

    # Tendência
    if total_week > total_last_week:
        trend = "📈 Aumento"
    elif total_week < total_last_week:
        trend = "📉 Queda"
    else:
        trend = "➡️ Estável"

    # Build markdown
    md = f"""---
title: "Relatório Pomodoro — {now.strftime('%Y-%m-%d')}"
description: "Relatório semanal de pomodoros de {week_start.strftime('%d/%m/%Y')} a {week_end.strftime('%d/%m/%Y')}"
tags: [log, pomodoro, produtividade, relatorio, auto-generated]
generated: {now.strftime('%Y-%m-%d %H:%M:%S')}
---

# 🍅 Relatório Pomodoro Semanal

**Período:** {week_start.strftime('%d/%m/%Y')} a {week_end.strftime('%d/%m/%Y')}
**Gerado em:** {now.strftime('%d/%m/%Y %H:%M')}

---

## 📊 Resumo da Semana

| Métrica | Valor |
|---------|-------|
| **Total de Pomodoros** | {total_week} |
| **Horas de Foco** | {(total_week * 25 / 60):.1f}h |
| **Dias com Pomodoro** | {len(days_with_pomodoro)}/7 |
| **Média por Dia** | {(total_week / 7):.1f} |
| **vs Semana Anterior** | {total_last_week} ({trend}) |
| **Total do Mês** | {total_month} |
| **Total Geral** | {total_all} |

"""

    if proj_week:
        md += "## 🎯 Por Projeto (esta semana)\n\n"
        md += "| Projeto | Pomodoros | Horas |\n"
        md += "|---------|-----------|-------|\n"
        for proj, qtd in sorted(proj_week.items(), key=lambda x: x[1], reverse=True):
            md += f"| {proj} | {qtd} | {(qtd * 25 / 60):.1f}h |\n"
        md += "\n"

    # Últimos 7 dias
    md += "## 📋 Últimos 7 Dias\n\n"
    md += "| Dia | Pomodoros |\n"
    md += "|-----|-----------|\n"
    for day_name, day_total in last_7:
        bar = "🍅" * min(day_total, 12) if day_total > 0 else "—"
        md += f"| {day_name} | {day_total} {bar} |\n"
    md += "\n"

    # Por projeto (total geral)
    if proj_total:
        md += "## 🏆 Por Projeto (total geral)\n\n"
        md += "| Projeto | Pomodoros | Horas |\n"
        md += "|---------|-----------|-------|\n"
        for proj, qtd in sorted(proj_total.items(), key=lambda x: x[1], reverse=True):
            md += f"| {proj} | {qtd} | {(qtd * 25 / 60):.1f}h |\n"
        md += "\n"

    md += f"""---

## 🔗 Links

- [[Will-Pessoal/03-Vida-Estilo/Vida/Produtividade|🍅 Pomodoro Dashboard]]
- [[JARVIS/03-Memory/Logs/Resumo-Semanal-{now.strftime('%Y-%m-%d')}|Resumo Semanal]]

---

*Relatório gerado automaticamente por `.scripts/pomodoro_report.py`*
*Para regenerar, execute: `python .scripts/pomodoro_report.py`*
"""

    return md


def main():
    """Execução principal"""
    print("[GEN] Gerando relatório pomodoro semanal...")

    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    content = generate_report()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"[OK] Relatório gerado: {OUTPUT_FILE.relative_to(VAULT_PATH)}")
    print("[INFO] Para executar manualmente: python .scripts/pomodoro_report.py")


if __name__ == "__main__":
    main()
