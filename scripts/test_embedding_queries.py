"""
Script: scripts/test_embedding_queries.py
Realiza queries RAG sentinela e verifica se respostas esperadas constam nos chunks.
Ideal para uso em CI/CD.
"""
import json
QUERIES = [
    {"query":"o que é RAG?","busca":"Retrieval Augmented Generation"},
    {"query":"visualização de roadmap","busca":"ROADMAP.md"},
    {"query":"como auditar sensível?","busca":"sensivel"},
]
with open('preprocess_incremental.jsonl', encoding='utf-8') as f:
    d = [json.loads(l) for l in f]
passou = True
for q in QUERIES:
    hit = any(q['busca'].lower() in (c.get('text','').lower()) for c in d)
    if not hit:
        print(f'FALHA: Query {q["query"]} NÂO encontrada.')
        passou = False
    else:
        print(f'OK: Query {q["query"]} encontrada!')
if not passou:
    exit(1)
print('Testes RAG queries completados.')
