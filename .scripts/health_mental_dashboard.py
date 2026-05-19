# health_mental_dashboard.py
'''
Script base para extração de sentimentos/humor a partir das notas de diário.
Detecta palavras-chave emocionais e classifica entries por humor, salvando resultados para consumo em dashboard DataviewJS.
'''
import os
import json
from datetime import datetime
from pathlib import Path
import re

diario_dir = Path('JARVIS/03-Memory/Logs')  # Ajuste se suas notas diárias ficam em outro local
saida_json = Path('dashboards/health_mental_report.json')

# Exemplo de palavras-humor básicas (expanda conforme quiser)
humor_map = {
    'feliz': 'positivo',
    'triste': 'negativo',
    'motivação': 'positivo',
    'frustração': 'negativo',
    'ansioso': 'negativo',
    'leve': 'positivo',
}

def classifica_humor(texto):
    for palavra, polaridade in humor_map.items():
        if re.search(fr'\b{palavra}\b', texto, re.IGNORECASE):
            return polaridade
    return 'neutro'

def processa_diarios():
    resultados = []
    for nota in diario_dir.glob('*.md'):
        with open(nota, 'r', encoding='utf-8') as f:
            texto = f.read()
        humor = classifica_humor(texto)
        resultados.append({'data': nota.name.split('.')[0], 'humor': humor, 'arquivo': str(nota)})
    with open(saida_json, 'w', encoding='utf-8') as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print(f'Resultado salvo em {saida_json}')

if __name__ == '__main__':
    processa_diarios()
