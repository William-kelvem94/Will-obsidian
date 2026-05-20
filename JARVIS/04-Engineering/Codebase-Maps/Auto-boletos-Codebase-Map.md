---
title: "Auto-boletos Codebase Map"
description: "Mapa RAG-friendly do projeto Auto-boletos para agentes de programacao."
created: 2026-05-08
updated: 2026-05-08
type: codebase-map
project: Auto-boletos
domain: engineering
language_primary: Python
language_secondary: TypeScript
code_root: "D:/Documents/GitHub/Auto-boletos"
vault_sources:
  - "Projetos/01-Ativos/Privados/Auto-boletos.md"
  - "Projetos/03-Estudos/EstudosPesquisas/Auto-boletos.md"
confidence: vault-notes-only
tags:
  - auto-boletos
  - flask
  - playwright
  - ocr
  - docker
  - rag
  - codebase-map
---

# Auto-boletos Codebase Map

## One-liner

Auto-boletos e um sistema para associar imoveis a dados oficiais da Equatorial Energy, automatizar consulta de debitos/boletos e aplicar OCR/IA local para analise semantica.

## Fontes locais relevantes

- Nota de projeto: [[Projetos/01-Ativos/Privados/Auto-boletos]]
- Nota de evolucao: [[Projetos/03-Estudos/EstudosPesquisas/Auto-boletos]]
- Recursos locais relacionados: [[Projetos/03-Estudos/EstudosPesquisas/AI-Local-Gratuita]]
- Observacao: nesta rodada nao houve leitura do codigo real de `D:/Documents/GitHub/Auto-boletos`; este mapa consolida o que ja esta no vault.

## Stack documentada

| Camada | Tecnologia citada | Funcao provavel |
|---|---|---|
| Backend | Flask + SQLAlchemy | API, modelos e fluxo de automacao. |
| Banco | Migracao para Neon DB/Postgres | Persistencia de imoveis, contas, debitos e historico. |
| Automacao | Playwright + Equatorial Facade | Navegacao no portal da distribuidora e coleta de dados. |
| CAPTCHA | CAPTCHA handling | Ponto critico de confiabilidade da automacao. |
| OCR | Tesseract | Extracao inicial de dados de boletos/documentos. |
| IA local | Ollama/memoria local | Analise semantica de debitos e predicao de consumo. |
| Frontend | React/Vite + Tailwind/shadcn planejado | Dashboard e revisao humana dos boletos. |
| Infra | Docker, Traefik e Watchtower planejados | Deploy local/produto com reverse proxy e atualizacao de containers. |

## Estrutura esperada

| Caminho esperado | Papel para agentes |
|---|---|
| `src/` | Logica de automacao, modelos e servicos do backend. |
| `frontend/` | Dashboard de controle e revisao de boletos. |
| `docs/` | Infraestrutura, deploy e operacao. |
| `docker-compose.yml` | Orquestracao local se existir. |
| `.env` | Segredos e credenciais; nao abrir nem copiar. |

## Modelo mental para agentes

1. Usuario cadastra ou seleciona imovel/unidade consumidora.
2. Backend aciona facade Playwright para consultar a Equatorial.
3. Sistema baixa ou captura boleto/debito.
4. OCR extrai campos estruturados: vencimento, valor, codigo, unidade, referencia, status.
5. Camada de IA local valida e interpreta dados ambiguos.
6. Frontend apresenta revisao humana, status e possiveis acoes.
7. Banco guarda historico para auditoria e predicao de consumo.

## Entidades de dominio que devem existir ou emergir

- `Property` ou `Imovel`: identificacao interna, endereco, responsavel.
- `CustomerAccount` ou `UnidadeConsumidora`: dados exigidos pela Equatorial.
- `Bill` ou `Boleto`: valor, vencimento, codigo de barras, competencia, status.
- `ScrapingSession`: execucao Playwright, logs, tentativas, falhas.
- `OcrExtraction`: texto bruto, campos extraidos, confianca e arquivo origem.
- `ReviewTask`: fila para correcao humana quando OCR/IA estiver incerto.

## Areas que pedem cuidado

- Automacao de portal publico pode quebrar com mudanca de DOM, CAPTCHA ou politica de acesso.
- Credenciais, dados de imoveis, documentos e boletos sao sensiveis.
- OCR por regex puro tende a falhar em layouts diferentes; preferir extracao estruturada com confianca.
- Playwright headless/stealth deve ser tratado como dependencia fragil e testavel.
- Pagamentos/boletos exigem trilha de auditoria: nao sobrescrever historico sem log.

## Proximos probes seguros

- Rodar `rg --files` no projeto real e localizar `app.py`, `src/`, `models`, `playwright`, `tesseract`, `ocr` e `docker`.
- Ler README, Dockerfile e compose antes de executar qualquer coisa.
- Mapear rotas Flask com `rg -n "@app.route|Blueprint|Flask\\("`.
- Mapear automacao Equatorial com `rg -n "equatorial|playwright|captcha|browser|page\\."`.
- Mapear OCR/parser com `rg -n "tesseract|ocr|barcode|boleto|regex|codigo"`.
- Verificar testes existentes antes de tocar no parser.

## Tarefas provaveis para agentes

- Criar parser semantico com saida JSON e campo `confidence`.
- Separar Playwright facade de regras de negocio para facilitar mocks.
- Adicionar fixtures de boletos anonimizados para testes.
- Implementar fila de revisao humana no frontend.
- Preparar migracao controlada para Postgres/Neon sem perder historico.
- Documentar deploy Docker com volumes e backup.

## Perguntas abertas

- O banco atual ainda e SQLite/local ou ja ha Postgres configurado?
- O frontend atual e React legado ou Vite/TypeScript ja foi adotado?
- O OCR recebe PDF, imagem, screenshot ou HTML do portal?
- Existe modo mock para desenvolver sem acessar a Equatorial?

[[JARVIS/04-Engineering/Codebase-Maps/INDEX|← Voltar ao índice de Codebase-Maps]]
