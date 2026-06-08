---
title: "DEMANDAS_ORGANIZADAS"
source: "https://github.com/William-kelvem94/DEMANDAS_ORGANIZADAS"
private: true
tags: [projetos, privados, demandas, node, react, docker]
updated: 2026-06-08
date: 2026-06-01
---

# DEMANDAS_ORGANIZADAS

Sistema de gestão de demandas com backend Node/Express, frontend React/Vite, PostgreSQL, Redis, JWT e Docker.

## Índice rápido
- [[README#Visão geral|Visão geral]]
- [[README#Estrutura principal|Estrutura]]
- [[README#Documentação importante|Documentação]]
- [[README#Scripts relevantes|Scripts]]
- [[README#Configs-chave|Configs]]
- [[README#Setup resumido|Setup]]
- [[README#Notas|Notas]]

## Visão geral
- Monorepo com foco em operação local e deploy via Docker.
- Stack observada: Node, Express, React, Vite, PostgreSQL, Redis, Winston, Knex, JWT, Google OAuth opcional.

## Estrutura principal
- `backend/`
- `frontend/`
- `documentation/`
- `scripts/`
- `tests/`
- `database/`
- `logs/`

## Documentação importante
- `README.md`
- `documentation/README.md`
- `documentation/ORGANIZACAO_COMPLETA.md`
- `documentation/ESTRUTURA_FINAL_OTIMIZADA.md`
- `documentation/INICIO_RAPIDO.md`
- `documentation/PREMIUM_SETUP.md`
- `documentation/DOCKER_README.md`
- `documentation/COMANDOS_UTEIS.md`

## Scripts relevantes
- `setup`
- `dev:services`
- `dev:backend`
- `dev:frontend`
- `dev`
- `validate`
- `test`
- `build`
- `start`
- `stop`
- `logs`
- `restart`

## Configs-chave
- `docker-compose.yml`
- `docker-compose.dev.yml`
- `backend/knexfile.js`
- `backend/jest.config.cjs`
- `frontend/vite.config.js`
- `frontend/nginx.conf`
- `database/pg_hba.conf`

## Setup resumido
1. Copiar `.env` dos exemplos.
2. Instalar dependências.
3. Subir serviços com Docker.
4. Rodar migrações e seeds.
5. Iniciar backend e frontend.

## Notas
- Há artefatos gerados e arquivos de ambiente que não devem ser republicados sem revisão.
- O projeto tem documentação rica e vale manter links internos no Obsidian.

## Notas complementares
### Arquitetura
- Backend HTTP separado do frontend SPA.
- Persistência híbrida com SQLite em dev/test e PostgreSQL em produção.
- Redis usado para cache/sessão/filas.

### Segurança
- JWT obrigatório.
- Google OAuth opcional.
- Rate limiting, headers de segurança e auditoria.
- Cuidado com `.env` versionado.

### Operação
- Docker Compose é o caminho principal.
- Adminer está incluso para inspeção rápida do banco.
- Há scripts para logs, limpeza e restart.

[[README|Voltar ao hub]]
