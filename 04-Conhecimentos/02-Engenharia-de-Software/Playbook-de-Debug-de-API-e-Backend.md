---
title: "Playbook de Debug de API e Backend"
date: 2026-06-07
updated: 2026-06-07
type: playbook
status: active
tags: [conhecimento-geral, backend, api, debug, logs]
related: [[APIs-Backend-Banco]], [[Observabilidade-Logs-e-Monitoramento]], [[Linux-Terminal-e-Shell]], [[../04-Seguranca-e-Redes/Redes-e-Internet]], [[../03-Dados-e-Analytics/Banco-de-Dados-Avancado]]
summary: "Playbook para diagnosticar erros de API e backend por camada: rota, validação, autenticação, banco, ambiente, rede e logs."
---

# Playbook de Debug de API e Backend

Use este playbook quando uma API não responde, retorna erro, grava dados incorretos ou se comporta diferente entre ambiente local e produção.

## Diagnóstico por sintoma

| Sintoma | Causa provável | Primeira ação |
|---|---|---|
| 404 | rota errada ou método errado | conferir URL, método e prefixo |
| 400 | payload inválido | validar body, query e headers |
| 401 | falta autenticação | conferir token, sessão ou cookie |
| 403 | falta permissão | checar regra de autorização |
| 409 | conflito de estado | verificar duplicidade ou regra de negócio |
| 422 | validação semântica | revisar schema e campos obrigatórios |
| 500 | erro interno | olhar logs e stack trace |
| timeout | serviço travado ou rede | conferir banco, fila, integração e porta |
| funciona local, falha em produção | ambiente diferente | comparar variáveis, build e permissões |

## Fluxo de investigação

1. Reproduzir o erro.
2. Registrar endpoint, método e payload.
3. Conferir status code.
4. Ler mensagem de erro.
5. Olhar logs do backend.
6. Confirmar variáveis de ambiente.
7. Testar dependências externas.
8. Validar consulta ou operação no banco.
9. Criar hipótese.
10. Testar uma correção por vez.

## Camada 1 - Rota

Checar:

- método HTTP;
- prefixo global;
- path real;
- parâmetro de rota;
- query string;
- versão da API;
- proxy ou gateway.

Erro comum: chamar `/users/1` quando o backend espera `/api/users/1`.

## Camada 2 - Payload

Checar:

- campos obrigatórios;
- nomes de campos;
- tipos;
- formato de data;
- valores nulos;
- arquivos anexados;
- tamanho do body.

## Camada 3 - Autenticação e autorização

Autenticação pergunta quem é. Autorização pergunta o que pode fazer.

Checar:

- token expirado;
- header ausente;
- cookie não enviado;
- usuário sem papel necessário;
- recurso pertence a outro usuário;
- regra só aplicada no frontend.

## Camada 4 - Banco de dados

Checar:

- conexão;
- migrações;
- constraints;
- transações;
- índices;
- locks;
- dados duplicados;
- query lenta.

## Camada 5 - Ambiente

Comparar:

- `.env` local e produção;
- versão do Node/Python;
- versão do banco;
- permissões de arquivo;
- portas;
- variáveis ausentes;
- Docker compose e comando de start.

## Logs úteis

Um log de debug precisa responder:

- qual operação falhou;
- qual usuário ou recurso estava envolvido;
- qual entrada foi recebida;
- qual erro foi lançado;
- onde ocorreu;
- qual correlação ou request id existe.

## Checklist rápido

- [ ] Endpoint e método estão corretos?
- [ ] Payload foi validado?
- [ ] Token ou sessão está presente?
- [ ] Permissão é checada no backend?
- [ ] Logs mostram stack trace?
- [ ] Banco está acessível?
- [ ] Migrações estão aplicadas?
- [ ] Variáveis de ambiente batem?
- [ ] O erro foi reproduzido com ferramenta externa?

## Registro de bug

```md
# Bug de API - título

## Endpoint

## Método

## Payload

## Resultado esperado

## Resultado obtido

## Logs

## Hipótese

## Correção

## Prevenção
```

## Resumo para IA

Ao depurar backend, investigar por camadas. Não pular direto para código. Primeiro confirmar rota, payload, autenticação, autorização, banco, ambiente e logs.

## Links internos

- [[APIs-Backend-Banco]]
- [[Observabilidade-Logs-e-Monitoramento]]
- [[Linux-Terminal-e-Shell]]
- [[../04-Seguranca-e-Redes/Redes-e-Internet]]
- [[../03-Dados-e-Analytics/Banco-de-Dados-Avancado]]
