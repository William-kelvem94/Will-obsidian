---
title: "Testes e Qualidade de Software"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, testes, qualidade, engenharia-software]
related: [[Arquitetura-Web-Moderna]], [[Git-e-Controle-de-Versao]], [[APIs-Backend-Banco]]
summary: "Guia prático sobre testes, qualidade, revisão e confiabilidade em projetos de software."
---

# Testes e Qualidade de Software

Testes reduzem incerteza. Eles não provam que um sistema é perfeito, mas ajudam a encontrar falhas antes do usuário.

## Tipos de teste

| Tipo | Objetivo |
|---|---|
| unitário | testar uma unidade pequena |
| integração | testar partes conectadas |
| ponta a ponta | simular fluxo real do usuário |
| contrato | validar comunicação entre sistemas |
| regressão | garantir que algo antigo não quebrou |
| carga | avaliar comportamento sob volume |
| manual exploratório | descobrir problemas fora do roteiro |

## Pirâmide de testes

A base deve ter muitos testes unitários, uma camada média de integração e poucos testes ponta a ponta.

## Qualidade além de teste

Qualidade também envolve:

- código legível;
- nomes claros;
- arquitetura simples;
- logs úteis;
- documentação mínima;
- validação de entrada;
- tratamento de erro;
- revisão de mudanças;
- monitoramento após deploy.

## O que testar primeiro

Priorizar:

1. regra de negócio crítica;
2. cálculo financeiro;
3. autenticação e permissão;
4. criação e alteração de dados;
5. integrações externas;
6. bugs que já aconteceram.

## Erros comuns

- testar só caminho feliz;
- não testar erro;
- testar detalhe de implementação;
- criar teste frágil;
- ignorar dados extremos;
- depender de ambiente instável;
- não rodar testes antes do deploy.

## Checklist de qualidade

- [ ] Existe teste para regra crítica?
- [ ] Erros são tratados?
- [ ] Dados inválidos são recusados?
- [ ] Logs ajudam diagnóstico?
- [ ] Código novo foi revisado?
- [ ] README explica como rodar?
- [ ] Mudança tem rollback simples?

## Relações

- [[Arquitetura-Web-Moderna]]
- [[Git-e-Controle-de-Versao]]
- [[APIs-Backend-Banco]]
