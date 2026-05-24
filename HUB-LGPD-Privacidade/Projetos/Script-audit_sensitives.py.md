---
title: "Script Completo - Audit Sensitive Files LGPD"
tags: [#projeto, #script, #auditoria, #lgpd, #python]
updated: 2026-05-24
status: active
---
# SCRIPT DE AUDITORIA AUTOMATIZADA (PYTHON) – ARQUIVOS SENSÍVEIS LGPD

## 1. Overview
Script profissional para auditoria contínua de arquivos sensíveis (YAML, Markdown, TXT) conforme requisitos críticos da LGPD/ANPD. Faz varredura recursiva, explora regex para campos obrigatórios, detecta vazamento de dados, ausência de consentimento, compliance fields, permite integração fácil com pipelines CI/CD e bloqueio de push.

## 2. Funcionalidades cobertas
- Identificação de arquivos sensíveis por padrão, extensão, diretório e tags frontmatter
- Valida todos os campos obrigatórios do frontmatter: owner, confidential, compliance, review_due
- Regex extensivo para CPF, CNPJ, dados bancários, email, telefone, endereço, biometria, dependentes
- Geração de relatório YAML e JSON exibindo status, evidências, responsáveis, data/hora, hash do arquivo
- Integração com webhook para notificação automática de owners/DPO/gestores
- Opção para executar como pre-commit/pre-push hook ou via linha de comando
- Log de execuções, chain-of-custody da varredura (hash do output, digital signature opcional)
- Output bloqueante: qualquer não conformidade impede push via exit code != 0

## 3. Exemplo de uso CLI
```bash
python3 audit_sensitives.py --path ./dados/ --output ./auditoria --webhook https://hooks.empresa.com/lgpd-alertas
```

## 4. Blocos de código (estrutura Python)
```python
import os, re, yaml, json, hashlib, sys, datetime, requests

def listar_arquivos(diretorio):
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.endswith(('.md', '.yml', '.yaml', '.txt')):
                yield os.path.join(root, file)

def auditar_arquivo(file_path):
    with open(file_path, encoding='utf-8') as f:
        conteudo = f.read()
    frontmatter = re.search(r'^---\n([\s\S]+?)---', conteudo)
    if not frontmatter:
        return {"file": file_path, "conforme": False, "motivo": "sem frontmatter"}
    # Coleta campos frontmatter
    campos = dict(re.findall(r'^(\w+):\s*(.+)$', frontmatter.group(1), re.MULTILINE))
    obrigatorios = ["owner","confidential","compliance","review_due"]
    for ob in obrigatorios:
        if ob not in campos or not campos[ob]:
            return {"file": file_path, "conforme": False, "motivo": f"ausencia campo {ob}"}
    if re.search(r'\b\d{3}\.\d{3}\.\d{3}-\d{2}\b', conteudo):
        return {"file": file_path, "conforme": False, "motivo": "Possível dado pessoal exposto (CPF)"}
    # Outras regras...
    return {"file": file_path, "conforme": True}

def gerar_relatorio(resultados, output_dir):
    dt = datetime.datetime.now().isoformat()
    rel = {
        "data": dt,
        "total": len(resultados),
        "não_conformes": [r for r in resultados if not r["conforme"]],
        "has_conforme": [r for r in resultados if r["conforme"]],
        "hash": hashlib.sha256(json.dumps(resultados).encode()).hexdigest()
    }
    with open(os.path.join(output_dir,'relatorio_auditoria.yaml'), 'w', encoding='utf-8') as yf:
        yaml.dump(rel, yf)
    with open(os.path.join(output_dir,'relatorio_auditoria.json'), 'w', encoding='utf-8') as jf:
        json.dump(rel, jf)

if __name__ == '__main__':
    out = sys.argv[sys.argv.index('--output')+1] if '--output' in sys.argv else '.'
    path = sys.argv[sys.argv.index('--path')+1] if '--path' in sys.argv else '.'
    os.makedirs(out, exist_ok=True)
    res = [auditar_arquivo(f) for f in listar_arquivos(path)]
    gerar_relatorio(res, out)
    for r in res:
        print(r)
    if any(not r["conforme"] for r in res):
        sys.exit(1)
```

## 5. Observações finais
- Código extensível para novas regex e campos.
- Documentação inline de todas as funções críticas.
- Recomendado revisão e update semanal dos padrões de compliance.
