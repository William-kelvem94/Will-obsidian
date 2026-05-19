# motor_what_if.py
'''
Script para simular "E se...?" entre vínculos de projetos e tarefas.
'''
import json
from pathlib import Path
from datetime import datetime

notas_dir = Path('JARVIS/03-Memory/Logs')
output_sim = Path('dashboards/simulador_what_if.json')

# Simulação simples: se uma nota depende das outras (via tag #depende:Nota-Alvo)
simulacoes = []
for nota in notas_dir.glob('*.md'):
    with open(nota, 'r', encoding='utf-8') as f:
        conteudo = f.read()
    for line in conteudo.splitlines():
        if '#depende:' in line:
            alvo = line.split('#depende:')[-1].strip().split()[0]
            simulacoes.append({'nota': nota.name, 'depende_de': alvo})
with open(output_sim, 'w', encoding='utf-8') as f:
    json.dump(simulacoes, f, ensure_ascii=False, indent=2)
print(f'Relatórios de simulação what-if salvo em {output_sim}')
