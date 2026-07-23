# topicos_emergentes.py
'''
Script para analisar a frequência de tags e tópicos emergentes no vault.
Salva tendências recentes para uso em dashboard/alerta.
'''
import re
import json
from pathlib import Path
from collections import Counter

pastas_busca = [Path('02-JARVIS/03-Memory/Logs')]
output_emergentes = Path('dashboards/topicos_emergentes.json')
tag_regex = r'#([\w\-]+)'

contagem = Counter()
for pasta in pastas_busca:
    for nota in pasta.glob('*.md'):
        with open(nota, 'r', encoding='utf-8') as f:
            conteudo = f.read()
            contagem.update(re.findall(tag_regex, conteudo))

emergentes = contagem.most_common(10)

with open(output_emergentes, 'w', encoding='utf-8') as f:
    json.dump(emergentes, f, ensure_ascii=False, indent=2)
print(f'Tópicos emergentes salvos em {output_emergentes}')
