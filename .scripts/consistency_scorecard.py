#!/usr/bin/env python3
"""
Scorecard de Consistência Semanal — Analisa o histórico git do vault
e produz métricas de consistência (streaks, commits por dia/hora,
notas criadas por dia). Gera JSON em dashboards/consistency_data.json
e pode atualizar automaticamente o dashboard.
"""

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timedelta, date
from pathlib import Path

SCRIPT_ROOT = Path(__file__).parent
VAULT_PATH = SCRIPT_ROOT.parent
OUTPUT_FILE = VAULT_PATH / "dashboards" / "consistency_data.json"
DASHBOARD_FILE = VAULT_PATH / "dashboards" / "Scorecard-Consistencia.md"

DIAS_SEMANA = ["Seg", "Ter", "Qua", "Qui", "Sex", "Sáb", "Dom"]
DIAS_SEMANA_EXT = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]


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


def get_all_commits():
    """Obtém todos os commits com hash e data ISO"""
    cmd = 'git log --all --format="%H|%ai"'
    output = run_command(cmd)
    commits = []
    if output:
        for line in output.split('\n'):
            line = line.strip()
            if line and '|' in line:
                parts = line.split('|', 1)
                if len(parts) == 2:
                    commits.append({
                        'hash': parts[0].strip(),
                        'iso_date': parts[1].strip()
                    })
    return commits


def get_notes_per_day():
    """Conta notas .md criadas por dia através do histórico git"""
    cmd = 'git log --all --diff-filter=A --format="%H|%ai" --name-only -- "*.md"'
    output = run_command(cmd)

    notes_per_day = Counter()
    current_date = None

    if output:
        for line in output.split('\n'):
            line = line.strip()
            if not line:
                continue
            if '|' in line and len(line) > 25:
                parts = line.split('|', 1)
                if len(parts) == 2:
                    current_date = parts[1].strip()[:10]
            elif current_date and line.endswith('.md'):
                notes_per_day[current_date] += 1

    return dict(notes_per_day)


def parse_date(date_str):
    """Converte string ISO para objeto date, tolerando timezone"""
    clean = date_str[:10]
    return datetime.strptime(clean, '%Y-%m-%d').date()


def compute_streaks(date_strings):
    """Computa streak atual e maior streak de dias consecutivos com commit"""
    dates = sorted(set(date_strings))
    if not dates:
        return {'current': 0, 'longest_ever': 0, 'longest_streak_end': None}

    dt_objs = [parse_date(d) for d in dates]

    longest = 1
    run = 1
    longest_end_idx = 0
    for i in range(1, len(dt_objs)):
        if (dt_objs[i] - dt_objs[i-1]).days == 1:
            run += 1
            if run > longest:
                longest = run
                longest_end_idx = i
        else:
            run = 1

    today = date.today()
    last = dt_objs[-1]

    if (today - last).days > 1:
        current = 0
    else:
        current = 1
        for i in range(len(dt_objs) - 2, -1, -1):
            if (last - dt_objs[i]).days == current:
                current += 1
            else:
                break

    return {
        'current': current,
        'longest_ever': longest,
        'longest_streak_end': str(dt_objs[longest_end_idx])
    }


def compute_weekly_heatmap(commits):
    """Gera dados de calor semanal para as últimas 4 semanas (Seg–Dom)"""
    commits_per_date = Counter()
    for c in commits:
        try:
            commits_per_date[parse_date(c['iso_date'][:10])] += 1
        except (ValueError, IndexError):
            continue

    today = datetime.now()
    current_weekday = today.weekday()
    last_monday = today - timedelta(days=current_weekday)

    weeks = []
    for w in range(4):
        week_start = last_monday - timedelta(weeks=w)
        days = {}
        for d in range(7):
            day_date = (week_start + timedelta(days=d)).date()
            count = commits_per_date.get(day_date, 0)
            days[DIAS_SEMANA[d]] = count
        weeks.append({
            'week_start': week_start.strftime('%Y-%m-%d'),
            'week_label': week_start.strftime('%d/%m'),
            'days': days
        })

    weeks.reverse()
    return weeks


def find_best(commits, notes_per_day):
    """Encontra recordes pessoais: mais commits/dia e mais notas/dia"""
    commit_dates = [c['iso_date'][:10] for c in commits]
    commits_por_dia = Counter(commit_dates)

    most_commits_day = max(commits_por_dia, key=commits_por_dia.get) if commits_por_dia else None
    most_notes_day = max(notes_per_day, key=notes_per_day.get) if notes_per_day else None

    return {
        'most_commits_in_day': {
            'date': most_commits_day or '',
            'count': commits_por_dia.get(most_commits_day, 0)
        },
        'most_notes_in_day': {
            'date': most_notes_day or '',
            'count': notes_per_day.get(most_notes_day, 0)
        }
    }


def compute_productivity(commits):
    """Computa commits por dia da semana e por hora"""
    by_day = Counter()
    by_hour = Counter()

    for c in commits:
        raw = c['iso_date']
        try:
            dt_str = raw[:19]
            dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
            by_day[DIAS_SEMANA[dt.weekday()]] += 1
            by_hour[str(dt.hour)] += 1
        except (ValueError, IndexError):
            continue

    for d in DIAS_SEMANA:
        by_day[d] = by_day.get(d, 0)

    ordered_days = {d: by_day.get(d, 0) for d in DIAS_SEMANA}
    return {
        'by_day_of_week': ordered_days,
        'by_hour': dict(sorted(by_hour.items()))
    }


def collect_metrics():
    """Coleta todas as métricas de consistência"""
    print("[GEN] Coletando commits do git...")
    commits = get_all_commits()
    print(f"[INFO] Total de commits encontrados: {len(commits)}")

    if not commits:
        print("[WARN] Nenhum commit encontrado no repositório.")
        return None

    print("[GEN] Analisando notas criadas...")
    notes_per_day = get_notes_per_day()

    print("[GEN] Computando streaks...")
    commit_dates = sorted(set(c['iso_date'][:10] for c in commits))
    streaks = compute_streaks(commit_dates)

    today = date.today()
    last_30 = today - timedelta(days=30)
    last_90 = today - timedelta(days=90)

    commits_30 = [c for c in commits if parse_date(c['iso_date'][:10]) >= last_30]
    commits_90 = [c for c in commits if parse_date(c['iso_date'][:10]) >= last_90]

    notes_30 = {
        k: v for k, v in notes_per_day.items()
        if datetime.strptime(k, '%Y-%m-%d').date() >= last_30
    }

    print("[GEN] Computando produtividade...")
    productivity = compute_productivity(commits_90)

    print("[GEN] Gerando heatmap semanal...")
    weekly_heatmap = compute_weekly_heatmap(commits_90)

    print("[GEN] Calculando recordes...")
    best = find_best(commits, notes_per_day)
    best['longest_streak_ever'] = streaks['longest_ever']
    best['longest_streak_end'] = streaks['longest_streak_end']

    metrics = {
        'generated_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'total_commits_all_time': len(commits),
        'last_30_days': {
            'days_with_commits': len(set(c['iso_date'][:10] for c in commits_30)),
            'total_commits': len(commits_30),
            'notes_created': sum(notes_30.values()),
            'total_possible_days': 30,
            'consistency_pct': round(
                len(set(c['iso_date'][:10] for c in commits_30)) / 30 * 100, 1
            )
        },
        'last_90_days': {
            'days_with_commits': len(set(c['iso_date'][:10] for c in commits_90)),
            'total_commits': len(commits_90),
            'total_possible_days': 90,
            'consistency_pct': round(
                len(set(c['iso_date'][:10] for c in commits_90)) / 90 * 100, 1
            )
        },
        'streaks': streaks,
        'productivity': productivity,
        'weekly_heatmap': weekly_heatmap,
        'notes_per_day': notes_30,
        'best': best
    }

    return metrics


def write_json(metrics):
    """Escreve o JSON de métricas no diretório dashboards"""
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)
    print(f"[OK] Dados salvos em: {OUTPUT_FILE.relative_to(VAULT_PATH)}")


def generate_js_data_block(metrics):
    """Gera o bloco JavaScript com os dados para embutir no dashboard"""
    js = json.dumps(metrics, ensure_ascii=False, indent=2)
    return f"const DATA = {js};"


def update_dashboard(metrics):
    """Atualiza o arquivo do dashboard com dados frescos entre os marcadores"""
    if not DASHBOARD_FILE.exists():
        print(f"[ERR] Dashboard não encontrado: {DASHBOARD_FILE}")
        print("[INFO] Crie o arquivo dashboards/Scorecard-Consistencia.md primeiro.")
        return False

    content = DASHBOARD_FILE.read_text(encoding='utf-8')
    js_block = generate_js_data_block(metrics)

    start_marker = "// <DATA_START>"
    end_marker = "// <DATA_END>"

    if start_marker not in content:
        print("[ERR] Marcador <DATA_START> não encontrado no dashboard.")
        print("[INFO] Adicione os marcadores ao arquivo do dashboard.")
        return False

    new_content = re.sub(
        f"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        f"{start_marker}\n{js_block}\n{end_marker}",
        content,
        flags=re.DOTALL
    )

    DASHBOARD_FILE.write_text(new_content, encoding='utf-8')
    print(f"[OK] Dashboard atualizado: {DASHBOARD_FILE.relative_to(VAULT_PATH)}")
    return True


def mock_metrics():
    """Retorna métricas de consistência simuladas para teste rápido e dashboards."""
    now = datetime.now()
    return {
        'generated_at': now.strftime('%Y-%m-%dT%H:%M:%S'),
        'total_commits_all_time': 1234,
        'last_30_days': {
            'days_with_commits': 22,
            'total_commits': 150,
            'notes_created': 29,
            'total_possible_days': 30,
            'consistency_pct': 73.3
        },
        'last_90_days': {
            'days_with_commits': 65,
            'total_commits': 410,
            'total_possible_days': 90,
            'consistency_pct': 72.2
        },
        'streaks': {
            'current': 4,
            'longest_ever': 15,
            'longest_streak_end': (now - timedelta(days=10)).strftime('%Y-%m-%d')
        },
        'productivity': {
            'by_day_of_week': {
                'Seg': 18, 'Ter': 22, 'Qua': 21, 'Qui': 20, 'Sex': 23, 'Sáb': 30, 'Dom': 16
            },
            'by_hour': {str(h): (h % 6) + 1 for h in range(24)}
        },
        'weekly_heatmap': [
            {
                'week_start': (now - timedelta(days=7*i)).strftime('%Y-%m-%d'),
                'week_label': (now - timedelta(days=7*i)).strftime('%d/%m'),
                'days': {d: (i*2+j)%6 for j,d in enumerate(["Seg","Ter","Qua","Qui","Sex","Sáb","Dom"])}
            } for i in range(4)
        ],
        'notes_per_day': {
            (now - timedelta(days=d)).strftime('%Y-%m-%d'): (1 if d%3==0 else 0) for d in range(30)
        },
        'best': {
            'most_commits_in_day': {'date': (now - timedelta(days=5)).strftime('%Y-%m-%d'), 'count': 12},
            'most_notes_in_day': {'date': (now - timedelta(days=3)).strftime('%Y-%m-%d'), 'count': 3},
            'longest_streak_ever': 15,
            'longest_streak_end': (now - timedelta(days=10)).strftime('%Y-%m-%d'),
        },
    }

def main():
    """Execução principal"""
    parser = argparse.ArgumentParser(description='Scorecard de Consistência Semanal')
    parser.add_argument(
        '--mock', action='store_true',
        help='Usa dados simulados/mocks para teste rápido ou dashboard dummy.'
    )
    parser.add_argument(
        '--update-dashboard', action='store_true',
        help='Atualiza o arquivo do dashboard com os dados gerados'
    )
    parser.add_argument(
        '--no-json', action='store_true',
        help='Não gera o arquivo JSON (apenas atualiza o dashboard)'
    )
    args = parser.parse_args()

    if args.mock:
        metrics = mock_metrics()
    else:
        metrics = collect_metrics()
        if metrics is None:
            sys.exit(1)

    if not args.no_json:
        write_json(metrics)

    if args.update_dashboard:
        update_dashboard(metrics)

    print("[OK] Scorecard de Consistência concluído!")


if __name__ == "__main__":
    main()
