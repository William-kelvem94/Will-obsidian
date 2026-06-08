# Will-obsidian — Guia de Setup, Padrões e Automação

## 1. Setup Rápido (Ambiente)

### Python / Dependências
- Recomendado Python 3.10+.
- Para ambiente reprodutível use `pip-tools`:
  - `pip install pip-tools`
  - `pip-compile requirements.in --output-file=requirements-locked.txt`
  - `pip install -r requirements-locked.txt`
- FAISS no Windows: `conda install -c pytorch faiss-cpu`

### Node
- `cd .scripts/mcp-vault-server && npm install`
- Use Node 18–20 (engines no package.json). Recomendado nvm/Volta.

### GitHub Actions / Tokens
- Token padrão `GITHUB_TOKEN` automático nos runners.
- PAT opcional: secret `GH_TOKEN`.

### Pre-commit & Segurança
```bash
pip install pre-commit
pre-commit install
```
**Hooks incluídos:**
- `black`, `ruff` (formatação/lint Python)
- `detect-secrets` (varredura de segredos)
- `trailing-whitespace`, `end-of-file-fixer`, `check-yaml`
- ⚠️ **audit-sensitives** (bloqueia push se `sensivel: true` fora da allowlist)
- 🔍 **enrich-frontmatter** (verifica frontmatter completo em todos .md)

## 2. Padrão Obrigatório de Frontmatter

Toda nota .md deve começar com:
```yaml
---
title: "Título"
tags: [tag1, tag2]
nivel: básico|intermediário|avançado
fonte: "Livro/Artigo/Site, Ano"
updated: YYYY-MM-DD
backlinks: [nota-relacionada]
assets:
  - type: pdf|image|audio|csv
    file: caminho/arquivo.ext
referencias:
  - "[Nome](url) DOI:10.x/abc.12.34"
sensivel: false
---
```

**Uso de templates:**
- `templates/frontmatter_padrao.md` — modelo completo
- `templates/case_template.md` — template para casos de uso
- `scripts/gen_skill.py "Nome" "Área"` — gera skill com frontmatter padronizado

## 3. Scripts de Automação

### Manutenção e Expansão

| Script | Função | Como usar |
|--------|--------|-----------|
| `scripts/enrich_frontmatter.py` | Escaneia e gera patches YAML para notas sem frontmatter completo | `python scripts/enrich_frontmatter.py` |
| `scripts/scan_gaps.py` | Compara taxonomia com notas existentes; gera GAPS.md | `python scripts/scan_gaps.py` |
| `scripts/gen_analytics.py` | Agrega tags e gera summary em ANALYTICS.md | `python scripts/gen_analytics.py` |
| `scripts/preprocess_incremental.py` | Indexação incremental (só arquivos alterados) | `python scripts/preprocess_incremental.py` |
| `scripts/preprocess_multimodal.py` | Indexa assets multimodais (PDF, img, audio) | `python scripts/preprocess_multimodal.py` |
| `scripts/audit_sensitives.py` | Bloqueia/audita arquivos sensíveis | `python scripts/audit_sensitives.py` (CI/pré-push) |
| `scripts/gen_skill.py "Nome" "Área"` | Gera nova skill padronizada | `python scripts/gen_skill.py "RAG Avançado" "IA"` |
| `scripts/test_embedding_queries.py` | Testa recall de queries sentinela | `python scripts/test_embedding_queries.py` |

### Pré-processamento RAG
```bash
# Indexação completa (já executada — 10.787 chunks)
python scripts/preprocess_full.py

# Indexação incremental (apenas mudados desde último hash)
python scripts/preprocess_incremental.py

# Workflow CI automático em pull requests
.github/workflows/test_embedding_retrieval.yml
```

## 4. Estruturas de Conhecimento

| Arquivo | Conteúdo |
|---------|----------|
| `TAXONOMY.md` | Áreas, skills, frameworks, personas do vault |
| `GAPS.md` | Gaps de conhecimento detectados automaticamente (executar `scan_gaps.py`) |
| `ROADMAP.md` | Roadmap do vault com prioridades e métricas |
| `SEGURANCA_PRIVACIDADE.md` | Checklist LGPD/GDPR e política de sensíveis |
| `BIBLIOGRAFIA.md` | Padrões de citação e referências |
| `MULTIMODALIDADE.md` | Como referenciar PDFs, imagens e áudio |
| `ANALYTICS.md` | Dashboard de tags, heatmap (autopopulado) |

## 5. Interface Web (Busca RAG)

A pasta `web-ui/` contém uma interface web leve para busca no vault:
```bash
# Servir localmente com Python
python -m http.server 8080 -d web-ui
# Ou com Node
npx serve web-ui
```
Acesse `http://localhost:8080` — digite queries para buscar nos 10.787 chunks.

## 6. Indexação RAG (Boas práticas)
- Use `indexer_config.json` para controlar allow/deny de arquivos.
- Excluir do índice público: `.agents/`, `.continue/`, `Templates/`, `Will-Pessoal/`.
- Pré-processamento: remover base64 inline, chunk por headings, anexar metadata.
- Teste de recall: `scripts/test_embedding_queries.py` valida respostas em CI.

## 7. Workflows CI/CD
- `vault-maintenance.yml` — manutenção periódica do vault
- `ci.yml` — lint e testes básicos
- `test_embedding_retrieval.yml` — testa recall de embeddings em PRs

## 8. Política de Contribuição
1. Use os templates para toda nova nota (frontmatter completo)
2. Sempre execute `enrich_frontmatter.py` antes de commits grandes
3. Nunca commite `sensivel: true` sem allowlist — o hook `audit-sensitives` bloqueia
4. Atualize `TAXONOMY.md` ao adicionar nova skill/área ou execute `scan_gaps.py`
5. Prefira `gen_skill.py` para criar skills — garante padronização
6. Revise `GAPS.md` periodicamente para identificar oportunidades de expansão
