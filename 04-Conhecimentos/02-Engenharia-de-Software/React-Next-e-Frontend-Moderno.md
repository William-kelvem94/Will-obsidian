---
title: "React, Next e Frontend Moderno"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, react, nextjs, frontend, ui]
related: [[TypeScript-e-JavaScript-Moderno]], [[Arquitetura-Web-Moderna]], [[Testes-e-Qualidade-de-Software]], [[../05-Produto-UX-e-Carreira/Produto-UX-e-Validacao]]
summary: "Guia de frontend moderno com React, Next.js, componentes, estado, dados, UX, performance e organização."
---

# React, Next e Frontend Moderno

Frontend moderno não é só tela bonita. É a camada onde usuário entende, decide e interage com o sistema.

## Conceitos centrais

| Conceito | Função |
|---|---|
| componente | bloco reutilizável de interface |
| props | dados recebidos por componente |
| state | dados internos e mutáveis da UI |
| effect | reação a mudanças externas |
| route | página ou caminho da aplicação |
| server rendering | renderização no servidor |
| client rendering | renderização no navegador |
| hydration | ativação da UI no cliente |

## React

React organiza interfaces em componentes. Um bom componente tem responsabilidade clara, props compreensíveis e pouco acoplamento.

## Next.js

Next.js adiciona estrutura para rotas, renderização, build, otimização e integração com backend.

## Organização recomendada

```txt
src/
├── app/
├── components/
├── features/
├── hooks/
├── lib/
├── services/
├── styles/
└── types/
```

## Estado

Tipos de estado:

- estado local: modal aberto, input, aba selecionada;
- estado remoto: dados vindos de API;
- estado global: autenticação, tema, preferências;
- estado derivado: calculado a partir de outros dados.

Evitar estado global sem necessidade.

## Performance

Boas práticas:

- evitar renderização desnecessária;
- dividir componentes grandes;
- paginar listas grandes;
- otimizar imagens;
- carregar dados no lugar certo;
- usar cache quando apropriado;
- medir antes de otimizar.

## UX técnica

Toda ação importante precisa de feedback:

- loading;
- sucesso;
- erro;
- estado vazio;
- confirmação;
- validação.

## Erros comuns

- componente gigante;
- lógica de negócio na tela;
- estado duplicado;
- loading inexistente;
- erro silencioso;
- formulário sem validação;
- layout bonito, mas fluxo confuso;
- acoplamento forte com API.

## Checklist

- [ ] Componentes têm nomes claros?
- [ ] Estados de loading/erro/vazio existem?
- [ ] Formulários validam entrada?
- [ ] Dados remotos são tratados com cache ou refetch?
- [ ] Interface funciona em tela pequena?
- [ ] A regra crítica fica fora da UI?
- [ ] A experiência do usuário foi considerada?

## Resumo para IA

Frontend moderno combina componente, estado, dados e experiência. Ao analisar projeto React/Next, verificar organização, responsabilidade dos componentes, tratamento de estados, validação, performance e UX.

## Links internos

- [[TypeScript-e-JavaScript-Moderno]]
- [[Arquitetura-Web-Moderna]]
- [[Testes-e-Qualidade-de-Software]]
- [[../05-Produto-UX-e-Carreira/Produto-UX-e-Validacao]]
