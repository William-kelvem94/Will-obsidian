---
title: "CI CD e Entrega Continua"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, cicd, devops, entrega-continua, automacao]
related: [[Git-e-Controle-de-Versao]], [[Testes-e-Qualidade-de-Software]], [[Docker-e-DevOps]], [[Observabilidade-Logs-e-Monitoramento]]
summary: "Conhecimento geral sobre CI/CD, pipelines, testes automatizados, build, deploy e rollback, sem configurar automação neste repositório."
---

# CI/CD e Entrega Contínua

Esta nota é apenas **conhecimento geral**. Ela não cria, ativa nem configura GitHub Actions ou qualquer automação no projeto.

CI/CD é o conjunto de práticas que automatiza integração, testes, build e entrega de software.

## Diferença importante

| Coisa | O que é |
|---|---|
| nota de conhecimento | documentação em Markdown para estudo |
| workflow de projeto | arquivo em `.github/workflows/` que executa automações reais |

Esta nota pertence ao Obsidian como estudo. Workflows reais só devem existir em projetos quando houver intenção clara de rodar automações.

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

## Pipeline conceitual

Um pipeline comum pode ter:

1. receber push ou pull request;
2. instalar dependências;
3. rodar lint;
4. rodar testes;
5. gerar build;
6. publicar artefato;
7. fazer deploy;
8. verificar saúde após deploy.

## Quando usar CI/CD real

Usar quando:

- o projeto tem testes estáveis;
- há deploy frequente;
- há equipe colaborando;
- falhas automatizadas geram valor real;
- notificações são desejadas;
- o custo de manutenção compensa.

## Quando não usar CI/CD real

Evitar quando:

- projeto está em fase experimental;
- testes ainda quebram por estrutura incompleta;
- notificações viram ruído;
- não há intenção de deploy automático;
- o workflow foi criado só por padrão e não por necessidade.

## Boas práticas

- pipeline deve ter nome claro;
- jobs precisam ser úteis;
- falhas precisam ser acionáveis;
- notificações devem ser desejadas;
- secrets devem ficar protegidos;
- deploy deve ter rollback;
- documentação deve explicar o motivo do workflow.

## Riscos

| Risco | Exemplo | Mitigação |
|---|---|---|
| ruído | e-mails de falha sem importância | desativar workflow ou notificações |
| falso negativo | teste falha por ambiente | estabilizar pipeline antes de ativar |
| custo de manutenção | pipeline quebra mais que ajuda | simplificar ou remover |
| segredo exposto | token em arquivo | usar secrets da plataforma |
| deploy acidental | publicação sem revisão | exigir aprovação manual |

## Checklist antes de criar workflow real

- [ ] O projeto precisa mesmo de automação?
- [ ] Os testes são confiáveis?
- [ ] As falhas geram ação clara?
- [ ] As notificações são úteis?
- [ ] Secrets estão protegidos?
- [ ] O workflow está documentado?
- [ ] Existe forma de desativar sem prejuízo?

## Resumo para IA

CI/CD como conhecimento é útil para estudar automação e entrega. CI/CD como workflow real só deve existir quando o projeto precisa executar ações automáticas. Não confundir documentação com automação ativa.

## Links internos

- [[Git-e-Controle-de-Versao]]
- [[Testes-e-Qualidade-de-Software]]
- [[Docker-e-DevOps]]
- [[Observabilidade-Logs-e-Monitoramento]]
