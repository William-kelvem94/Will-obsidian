# inspiracoes_aleatorias.py
'''
Script para sugerir aleatoriamente uma nota/reflexão antiga no vault.
'''
import os
import random
from pathlib import Path

notas_paths = [Path('02-JARVIS/03-Memory/Logs')] # adicione mais pastas conforme necessidade
sugestoes_file = Path('dashboards/inspiracao_diaria.json')

# Pega uma nota aleatória do(s) diretório(s)
def pega_inspiracao():
    arquivos = []
    for d in notas_paths:
        arquivos.extend(list(d.glob('*.md')))
    if not arquivos:
        return None
    escolhida = random.choice(arquivos)
    sugestao = {'nota': escolhida.name, 'caminho': str(escolhida)}
    with open(sugestoes_file, 'w', encoding='utf-8') as f:
        import json
        json.dump(sugestao, f)
    print(f'Sugestão salva em {sugestoes_file}')
    return sugestao

if __name__ == '__main__':
    pega_inspiracao()
