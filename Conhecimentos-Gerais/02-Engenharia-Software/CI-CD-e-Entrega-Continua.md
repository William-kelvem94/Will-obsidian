---
title: "CI CD e Entrega Continua"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, cicd, devops, entrega-continua, automacao]
related: [[Git-e-Controle-de-Versao]], [[Testes-e-Qualidade-de-Software]], [[Docker-e-DevOps]], [[Observabilidade-Logs-e-Monitoramento]]
summary: "Guia de CI/CD, automação de build, testes, deploy, rollback e entrega confiável de software."
---

# CI/CD e Entrega Contínua

CI/CD é o conjunto de práticas que automatiza integração, testes, build e entrega de software.

## Conceitos

| Conceito | Significado |
|---|---|
| CI | integração contínua |
| CD | entrega ou deploy contínuo |
| pipeline | sequência automatizada de etapas |
| build | gerar artefato executável |
| artifact | resultado versionado do build |
| deploy | publicar em ambiente |
| rollback | voltar para versão anterior |
| environment | ambiente: dev, staging, produção |

## Pipeline básico

1. Receber push ou pull request.
2. Instalar dependências.
3. Rodar lint.
4. Rodar testes.
5. Buildar aplicação.
6. Gerar artefato ou imagem.
7. Publicar em ambiente.
8. Verificar saúde após deploy.

## Ambientes

| Ambiente | Uso |
|---|---|
| local | desenvolvimento individual |
| dev | integração inicial |
| staging | simular produção |
| produção | uso real |

## Boas práticas

- pipeline deve falhar cedo;
- testes críticos devem rodar antes do deploy;
- secrets devem ficar no gerenciador da plataforma;
- deploy deve ser rastreável;
- rollback precisa ser possível;
- logs pós-deploy devem ser acompanhados;
- migrações precisam de cuidado especial.

## Erros comuns

- deploy manual sem registro;
- pipeline lento demais;
- testes quebrados ignorados;
- secrets expostos;
- staging diferente demais de produção;
- rollback não testado;
- deploy junto de mudança grande de banco sem plano.

## Checklist

- [ ] O pipeline roda em pull request?
- [ ] Testes críticos passam?
- [ ] Build é reproduzível?
- [ ] Secrets estão protegidos?
- [ ] Ambiente de produção é separado?
- [ ] Existe rollback?
- [ ] Logs são acompanhados após deploy?

## Resumo para IA

CI/CD reduz risco e repetição ao automatizar validação e entrega. Ao analisar projeto, verificar pipeline, testes, secrets, deploy, rollback e observabilidade.

## Links internos

- [[Git-e-Controle-de-Versao]]
- [[Testes-e-Qualidade-de-Software]]
- [[Docker-e-DevOps]]
- [[Observabilidade-Logs-e-Monitoramento]]
