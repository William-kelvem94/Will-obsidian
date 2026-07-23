# revisao_ciclica.py
'''
Script para agendar revisões cíclicas de notas/projetos pouco acessados.
Gera uma lista rotativa de notas a revisar e registra log.
'''
import os
import random
import json
from datetime import datetime, timedelta
from pathlib import Path

notas_dir = Path('02-JARVIS/03-Memory/Logs')  # ajustar conforme local das notas
agenda_file = Path('dashboards/agenda_revisao.json')
quantidade_diaria = 2  # quantas revisar por dia

def listar_notas():
    arquivos = list(notas_dir.glob('*.md'))
    arquivos.sort(key=lambda f: f.stat().st_atime)
    return arquivos

def gera_agenda():
    arquivos = listar_notas()
    if not arquivos:
        return []
    agenda = arquivos[:quantidade_diaria]
    agenda_resultado = []
    for nota in agenda:
        agenda_resultado.append({'nota': nota.name, 'ultimo_acesso': datetime.fromtimestamp(nota.stat().st_atime).isoformat()})
    with open(agenda_file, 'w', encoding='utf-8') as f:
        json.dump(agenda_resultado, f, ensure_ascii=False, indent=2)
    print(f'Agenda salva em {agenda_file}')

if __name__ == '__main__':
    gera_agenda()
