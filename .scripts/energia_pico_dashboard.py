# energia_pico_dashboard.py
'''
Script: checa hábitos/check-ins no diário para detectar horários/dias de pico produtivo.
'''
import json
import re
from pathlib import Path
from collections import Counter

notas_dir = Path('JARVIS/03-Memory/Logs')
saida = Path('dashboards/energia_pico_report.json')
horarios = []

for nota in notas_dir.glob('*.md'):
    h = re.findall(r'(\d{2}):(\d{2})', nota.read_text(encoding='utf-8'))
    if h:
        # Use o primeiro horário encontrado como proxy do log
        horarios.extend([':'.join(p) for p in h])
hc = Counter(horarios)

with open(saida, 'w', encoding='utf-8') as f:
    json.dump(hc.most_common(15), f, ensure_ascii=False, indent=2)
print(f'Relatório de pico de energia salvo em {saida}')
