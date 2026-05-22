---
title: "DEMANDAS_ORGANIZADAS_2.0"
source: "https://github.com/William-kelvem94/DEMANDAS_ORGANIZADAS_2.0"
private: true
tags: [projetos, privados, demandas, monorepo, docker, rust, electron]
updated: 2026-05-22
---

# DEMANDAS_ORGANIZADAS_2.0

Snapshot com forte perfil de monorepo tipo AFFiNE: web app, desktop Electron, backend, módulos nativos e infraestrutura pesada.

## Índice rápido
- [[README#Visão geral|Visão geral]]
- [[README#Estrutura principal|Estrutura]]
- [[README#Docs-chave|Docs]]
- [[README#Scripts relevantes|Scripts]]
- [[README#Infra relevante|Infra]]
- [[README#Setup resumido|Setup]]
- [[README#Notas|Notas]]

## Visão geral
- Base colaborativa com app web, desktop, backend server, packages nativos Rust e módulos auxiliares.
- Forte foco em CI/CD, Docker, Helm, testes e release automation.

## Estrutura principal
- `packages/backend`
- `packages/frontend`
- `blocksuite`
- `docs`
- `scripts`
- `tests`
- `tools`

## Docs-chave
- `docs/BUILDING.md`
- `docs/developing-server.md`
- `docs/building-desktop-client-app.md`
- `docs/issue-triaging.md`
- `docs/CONTRIBUTING.md`
- `docs/CODE_OF_CONDUCT.md`
- `docs/types-of-contributions.md`
- `.docker/dev/README.md`

## Scripts relevantes
- `dev`
- `build`
- `lint`
- `lint:fix`
- `test`
- `test:ui`
- `test:coverage`
- `typecheck`

## Infra relevante
- `.github/workflows/*`
- `.github/helm/*`
- `.github/actions/*`
- `.docker/dev/*`
- `rust-toolchain.toml`
- `tsconfig*.json`
- `eslint.config.mjs`
- `vitest.config.ts`

## Setup resumido
1. Node LTS + Rust.
2. Yarn 4 com Corepack.
3. `yarn install`.
4. Subir serviços dev via Docker.
5. Rodar init/dev do backend e frontend.

## Notas
- É mais um ecossistema grande do que um app simples.
- Ótimo candidato para notas separadas de build, server, desktop, release e infra.

## Notas complementares
### Arquitetura
- Monorepo com packages públicos e internos.
- Editor colaborativo via `blocksuite`.
- Back-end e native packages com Rust e Node juntos.

### Infra/Entrega
- GitHub Actions faz a maior parte do trabalho pesado.
- Helm e Docker cobrem cloud/self-host.
- Releases desktop e mobile têm pipelines dedicados.

### Atenção
- Docs podem estar desatualizadas em relação a scripts/nomes.
- Há complexidade alta de build e dependências cruzadas.

[[README|Voltar ao hub]]
