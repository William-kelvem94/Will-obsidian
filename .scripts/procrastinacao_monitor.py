# procrastinacao_monitor.py
'''
Script para detectar padrões recorrentes de procrastinação nas notas (tarefas adiadas).
'''
import re
import json
from pathlib import Path
from datetime import datetime

notas_dir = Path('JARVIS/03-Memory/Logs')
procrast_report = Path('dashboards/procrastinacao_report.json')
padrao_adiado = r'adiado|procrastinar|depois|amanha|postergar'

resultados = []
for nota in notas_dir.glob('*.md'):
    with open(nota, 'r', encoding='utf-8') as f:
        conteudo = f.read().lower()
    if re.search(padrao_adiado, conteudo):
        resultados.append({'nota': nota.name, 'data': nota.stem})

with open(procrast_report, 'w', encoding='utf-8') as f:
    json.dump(resultados, f, ensure_ascii=False, indent=2)
print(f'Relatório de procrastinação salvo em {procrast_report}')
