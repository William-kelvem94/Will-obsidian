# rituais_microhabitos.py
'''
Script para orquestração automatizada de micro-rituais e hábitos curtos.
Agenda lembretes e registra execuções.
'''
import json
from datetime import datetime
from pathlib import Path

habitos = ['beber_agua', 'alongar', 'descansar_olhos', 'respirar', 'anotar_aprendizado']
registro_file = Path('dashboards/rituais_microhabitos.json')

# Simula registro diário (mock)
registro = {habito: {'feito': False, 'ultima_execucao': None} for habito in habitos}

for habito in habitos:
    registro[habito]['ultima_execucao'] = datetime.now().isoformat()
    registro[habito]['feito'] = True

with open(registro_file, 'w', encoding='utf-8') as f:
    json.dump(registro, f, ensure_ascii=False, indent=2)
print(f'Status dos rituais/hábitos salvo em {registro_file}')
