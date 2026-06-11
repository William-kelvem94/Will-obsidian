---
title: "Threat Modeling e Gestao de Riscos"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, seguranca, riscos, threat-modeling]
related: [[Seguranca-da-Informacao]], [[OWASP-e-Seguranca-Web]], [[../../08-Vida-Pratica/Produtividade/Decisao-e-Priorizacao]], [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]]
summary: "Guia para identificar ameaças, ativos, riscos, controles e decisões de segurança de forma prática."
---

# Threat Modeling e Gestão de Riscos

Threat modeling é o processo de pensar antes no que pode dar errado, quem poderia explorar, qual impacto teria e quais controles reduzem o risco.

## Perguntas centrais

1. O que estamos protegendo?
2. De quem estamos protegendo?
3. Como poderia ser atacado ou abusado?
4. Qual seria o impacto?
5. O que já reduz esse risco?
6. O que falta fazer?

## Ativos

Ativo é algo que tem valor e precisa proteção.

Exemplos:

- dados pessoais;
- credenciais;
- banco de dados;
- código-fonte;
- arquivos internos;
- logs;
- disponibilidade do sistema;
- reputação;
- dinheiro.

## Ameaças comuns

| Ameaça | Exemplo |
|---|---|
| vazamento | token exposto no Git |
| acesso indevido | usuário vê dado de outro usuário |
| alteração indevida | dado crítico é modificado |
| indisponibilidade | serviço cai |
| abuso de recurso | API usada em excesso |
| engenharia social | alguém entrega credencial |
| erro operacional | backup perdido ou deploy errado |

## Matriz de risco

| Impacto | Probabilidade | Prioridade |
|---|---|---|
| alto | alta | agir rápido |
| alto | baixa | planejar controle |
| baixo | alta | reduzir ruído |
| baixo | baixa | aceitar ou monitorar |

## Controles

| Controle | Reduz |
|---|---|
| autenticação forte | acesso indevido |
| autorização por recurso | vazamento interno |
| validação de entrada | injeção e dados inválidos |
| backup | perda de dados |
| logs | falta de rastreabilidade |
| rate limit | abuso de API |
| revisão de código | erro humano |
| separação de ambiente | dano acidental |

## Registro de risco

```md
# Risco: nome

## Ativo afetado

## Ameaça

## Impacto

## Probabilidade

## Controle atual

## Ação recomendada

## Dono

## Status
```

## Erros comuns

- pensar segurança só no final;
- proteger só login e esquecer autorização;
- não mapear dados sensíveis;
- não testar recuperação;
- não registrar risco aceito;
- tratar todo risco como igual;
- criar controle impossível de manter.

## Checklist

- [ ] Ativos foram listados?
- [ ] Dados sensíveis foram identificados?
- [ ] Rotas críticas têm permissão?
- [ ] Existe backup?
- [ ] Logs registram eventos relevantes?
- [ ] Riscos altos têm ação definida?
- [ ] Riscos aceitos foram documentados?

## Resumo para IA

Threat modeling ajuda a pensar segurança como decisão, não pânico. Identifique ativo, ameaça, impacto, probabilidade e controle antes de escolher ação.

## Links internos

- [[Seguranca-da-Informacao]]
- [[OWASP-e-Seguranca-Web]]
- [[../../08-Vida-Pratica/Produtividade/Decisao-e-Priorizacao]]
- [[../../02-Engenharia-de-Software/Arquitetura-Web-Moderna]]
