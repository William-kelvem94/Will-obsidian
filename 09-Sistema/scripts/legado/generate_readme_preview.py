from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'README_PROPOSAL.md'

content = '''# Setup Rápido (proposta)

Este documento propõe instruções de setup e boas práticas para desenvolvedores que usem este Vault.

## Python / Dependências
- Recomendado usar Python 3.10 ou 3.11.
- Para ambiente reprodutível use `pip-tools`:
  - `pip install pip-tools`
  - `pip-compile requirements.in --output-file=requirements-locked.txt`
  - `pip install -r requirements-locked.txt`
- Nota sobre FAISS: preste atenção à instalação em Windows. Recomendamos usar conda para `faiss-cpu`:
  - `conda install -c pytorch faiss-cpu`

## Node
- `cd .scripts/mcp-vault-server && npm install`
- É recomendado usar Node 18–20 em CI (a `package.json` especifica engines >=18 <21). Use nvm/Volta.

## GitHub Actions / Tokens
- A automação usa o token padrão `GITHUB_TOKEN` (armazenado automaticamente nos runners).
- Se precisar de um PAT, adicione secret `GH_TOKEN` e atualize o workflow explicitamente.

## Pre-commit & Segurança
- Instalando hooks locais:
  - `pip install pre-commit`
  - `pre-commit install`
- Recomendamos ativar gitleaks em PRs para evitar vazamento de segredos.

## Indexação RAG (boas práticas)
- Use `indexer_config.json` para controlar allow/deny de arquivos.
- Exclua `.agents/`, `.continue/`, `Templates/` e `Will-Pessoal/` do índice público.
- Pré-processamento: remover inline base64, chunk por headings, anexar metadata (source_path, heading_path, file_hash).

'''

OUT.write_text(content, encoding='utf-8')
print(f'Wrote README proposal to {OUT}')
