# network_monitor.py
'''
Script para monitoramento de pessoas/colaborações (@menções, nomes) no vault.
Gera alerta de follow-up baseado em tempo desde a última menção.
'''
import re
import json
from pathlib import Path
from datetime import datetime

notas_dir = Path('JARVIS/03-Memory/Logs')  # altere conforme o local das notas
output_file = Path('dashboards/network_report.json')
padrao_mencao = r'@([\w\-]+)'

resultados = {}
for nota in notas_dir.glob('*.md'):
    with open(nota, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    for match in re.findall(padrao_mencao, conteudo):
        if match not in resultados or (datetime.strptime(nota.stem, '%Y-%m-%d') > resultados.get(match, {'data':'1900-01-01'})['data']):
            resultados[match] = {'data': nota.stem, 'arquivo': str(nota)}

# Formata para dashboard: há quanto tempo não fala com cada pessoa
hoje = datetime.now()
alertas = []
for pessoa, info in resultados.items():
    data_ult = datetime.strptime(info['data'], '%Y-%m-%d')
    dias = (hoje - data_ult).days
    alertas.append({'pessoa': pessoa, 'dias_desde_ultimo_contato': dias, 'ultimo_contato': info['data']})

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(alertas, f, ensure_ascii=False, indent=2)
print(f'Relatório de networking salvo em {output_file}')
