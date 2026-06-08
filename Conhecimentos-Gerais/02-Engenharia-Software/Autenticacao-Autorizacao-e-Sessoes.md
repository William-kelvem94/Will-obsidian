---
title: "Autenticação, Autorização e Sessões"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, backend, seguranca, autenticacao, autorizacao]
related: [[APIs-Backend-Banco]], [[../07-Seguranca/Seguranca-da-Informacao]], [[../07-Seguranca/OWASP-e-Seguranca-Web]], [[Playbook-de-Debug-de-API-e-Backend]]
summary: "Guia prático sobre autenticação, autorização, sessões, tokens, cookies, papéis, permissões e riscos comuns em aplicações web."
---

# Autenticação, Autorização e Sessões

Autenticação e autorização são pilares de qualquer sistema com usuários. Muitos bugs graves acontecem quando o sistema sabe quem é o usuário, mas não verifica corretamente o que ele pode acessar.

## Diferença essencial

| Conceito | Pergunta | Exemplo |
|---|---|---|
| autenticação | quem é o usuário? | login com e-mail e senha |
| autorização | o que ele pode fazer? | usuário pode editar este recurso? |
| sessão | como manter usuário reconhecido? | cookie de sessão |
| token | credencial carregada pelo cliente | JWT ou token opaco |

## Fluxo típico de login

1. Usuário envia credenciais.
2. Backend valida credenciais.
3. Backend cria sessão ou token.
4. Cliente armazena credencial de forma segura.
5. Próximas requisições enviam a credencial.
6. Backend identifica usuário.
7. Backend verifica permissão para cada ação.

## Sessão com cookie

Vantagens:

- controle centralizado no servidor;
- pode invalidar sessão;
- bom para aplicações web tradicionais;
- pode usar cookies `HttpOnly`.

Riscos:

- configuração incorreta de cookie;
- CSRF quando proteção é ausente;
- sessão longa demais;
- armazenamento inseguro.

## JWT

JWT carrega informações assinadas. Pode ser útil, mas não é magia.

Vantagens:

- stateless em alguns cenários;
- fácil de enviar entre serviços;
- contém claims.

Riscos:

- difícil invalidar antes de expirar;
- token grande;
- claims desatualizadas;
- armazenamento inseguro no frontend;
- confundir assinatura com criptografia.

## Papéis e permissões

Papéis agrupam permissões.

Exemplo:

| Papel | Permissões |
|---|---|
| admin | gerenciar usuários e configurações |
| operador | executar rotina operacional |
| leitor | visualizar dados |
| dono | editar recursos próprios |

## Regra importante

Permissão crítica deve ser checada no backend, nunca só no frontend.

Frontend pode esconder botão. Backend precisa negar ação.

## Erros comuns

- verificar apenas se usuário está logado;
- não verificar dono do recurso;
- confiar em `role` enviado pelo cliente;
- token sem expiração;
- guardar token em local inseguro;
- retornar dados demais;
- esquecer logout/invalidação;
- permissões duplicadas em lugares diferentes.

## Checklist

- [ ] Login valida credenciais com segurança?
- [ ] Senhas são armazenadas com hash adequado?
- [ ] Sessões ou tokens expiram?
- [ ] Permissão é checada por recurso?
- [ ] Frontend não é a única barreira?
- [ ] Dados sensíveis não vão para o cliente sem necessidade?
- [ ] Logout invalida o acesso quando aplicável?
- [ ] Rotas administrativas têm proteção extra?

## Resumo para IA

Ao revisar autenticação e autorização, separar identidade de permissão. Verificar sempre se a regra está no backend, se o usuário pode acessar aquele recurso específico e se sessão/token tem expiração e proteção adequada.

## Links internos

- [[APIs-Backend-Banco]]
- [[../07-Seguranca/Seguranca-da-Informacao]]
- [[../07-Seguranca/OWASP-e-Seguranca-Web]]
- [[Playbook-de-Debug-de-API-e-Backend]]
