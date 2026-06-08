---
title: "OWASP e Seguranca Web"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, seguranca, owasp, web, backend]
related: [[Seguranca-da-Informacao]], [[Threat-Modeling-e-Gestao-de-Riscos]], [[../02-Engenharia-Software/APIs-Backend-Banco]], [[../02-Engenharia-Software/Testes-e-Qualidade-de-Software]]
summary: "Guia prático de segurança web inspirado em riscos OWASP, autenticação, autorização, validação, secrets e proteção de APIs."
---

# OWASP e Segurança Web

OWASP é uma referência importante em segurança de aplicações web. Para projetos práticos, o essencial é entender riscos comuns e aplicar controles desde o início.

## Riscos comuns

| Risco | Ideia |
|---|---|
| controle de acesso fraco | usuário acessa o que não deveria |
| falha criptográfica | dados sensíveis expostos |
| injeção | entrada vira comando ou consulta indevida |
| configuração insegura | ambiente expõe portas, logs ou dados |
| autenticação fraca | identidade pode ser comprometida |
| componentes vulneráveis | dependências antigas ou inseguras |
| logging insuficiente | ataques e falhas não são percebidos |

## Autenticação vs autorização

| Conceito | Pergunta |
|---|---|
| autenticação | quem é o usuário? |
| autorização | o que ele pode fazer? |

Erro comum: verificar login, mas não verificar permissão do recurso específico.

## Validação de entrada

Toda entrada externa deve ser tratada como não confiável:

- formulário;
- query string;
- body de API;
- arquivo;
- webhook;
- dado vindo de sistema externo.

## Secrets

Secrets incluem senhas, tokens, chaves privadas, strings de conexão e credenciais.

Boas práticas:

- não versionar;
- usar variáveis de ambiente;
- rotacionar quando vazar;
- limitar permissão;
- separar por ambiente;
- evitar mostrar em logs.

## Proteção de API

- validar payload;
- autenticar quando necessário;
- verificar permissão por recurso;
- limitar taxa quando fizer sentido;
- registrar eventos críticos;
- evitar retorno excessivo de dados;
- tratar erro sem expor detalhe sensível.

## Checklist rápido

- [ ] Rotas críticas exigem autenticação?
- [ ] Permissão é checada no backend?
- [ ] Entrada externa é validada?
- [ ] Secrets estão fora do Git?
- [ ] Logs não expõem dados sensíveis?
- [ ] Dependências são atualizadas?
- [ ] Erros não vazam stack em produção?

## Resumo para IA

Segurança web exige autenticação, autorização, validação, gestão de secrets, configuração segura e logs úteis. Ao revisar um projeto, procurar primeiro controle de acesso, dados sensíveis e entrada externa.

## Links internos

- [[Seguranca-da-Informacao]]
- [[Threat-Modeling-e-Gestao-de-Riscos]]
- [[../02-Engenharia-Software/APIs-Backend-Banco]]
- [[../02-Engenharia-Software/Testes-e-Qualidade-de-Software]]
