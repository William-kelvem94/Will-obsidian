# conexoes_implicitas.py
'''
Script para sugerir conexões temáticas não explícitas via similaridade de conteúdo
'''
import os
import json
import re
from pathlib import Path
from collections import defaultdict
from itertools import combinations

analisar_dir = Path('JARVIS/03-Memory/Logs')
output_file = Path('dashboards/conexoes_implicitas.json')

# Função rudimentar: similaridade por número de palavras em comum
notas = list(analisar_dir.glob('*.md'))
similaridades = defaultdict(list)

for a, b in combinations(notas, 2):
    with open(a, 'r', encoding='utf-8') as f:
        conteudo_a = set(re.findall(r'\w+', f.read().lower()))
    with open(b, 'r', encoding='utf-8') as f:
        conteudo_b = set(re.findall(r'\w+', f.read().lower()))
    inter = conteudo_a & conteudo_b
    if len(inter) > 20:  # Ajuste threshold
        similaridades[a.name].append({'com': b.name, 'palavras_comum': len(inter)})

with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(similaridades, f, ensure_ascii=False, indent=2)
print(f'Conexões ocultas salvas em {output_file}')
