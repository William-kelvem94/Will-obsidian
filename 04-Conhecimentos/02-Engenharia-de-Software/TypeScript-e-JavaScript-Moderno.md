---
title: "TypeScript e JavaScript Moderno"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, typescript, javascript, frontend, backend]
related: [[React-Next-e-Frontend-Moderno]], [[APIs-Backend-Banco]], [[Testes-e-Qualidade-de-Software]], [[Design-Patterns-e-Arquitetura-Limpa]]
summary: "Guia de JavaScript moderno e TypeScript para projetos frontend, backend, tipagem, módulos, async e qualidade."
---

# TypeScript e JavaScript Moderno

JavaScript é a linguagem base da web. TypeScript adiciona tipagem estática gradual, ajudando a encontrar erros antes da execução.

## Por que TypeScript importa

TypeScript melhora:

- autocomplete;
- refatoração;
- documentação implícita;
- contratos entre funções;
- prevenção de erros simples;
- manutenção em projetos maiores.

## Conceitos de JavaScript moderno

| Conceito | Uso |
|---|---|
| `let` e `const` | declaração de variáveis |
| arrow functions | funções compactas |
| destructuring | extrair valores de objetos e arrays |
| spread/rest | copiar, combinar e receber múltiplos valores |
| promises | lidar com operações assíncronas |
| async/await | escrever assíncrono de forma legível |
| modules | organizar código em arquivos |
| map/filter/reduce | transformar coleções |

## Conceitos de TypeScript

| Conceito | Uso |
|---|---|
| type | definir formato de dado |
| interface | contrato de objeto |
| union | aceitar mais de um tipo |
| generic | tipo flexível e reutilizável |
| enum | conjunto nomeado de valores |
| optional | campo opcional |
| narrowing | refinar tipo por condição |
| utility types | transformar tipos existentes |

## Exemplo simples

```ts
type User = {
  id: string;
  name: string;
  email?: string;
};

function formatUser(user: User): string {
  return `${user.name} (${user.id})`;
}
```

## Boas práticas

- evitar `any` sem justificativa;
- tipar entradas e saídas importantes;
- manter nomes claros;
- separar tipos compartilhados;
- validar dados externos em runtime;
- usar TypeScript como contrato, não como enfeite;
- preferir simplicidade antes de tipos muito complexos.

## TypeScript não substitui validação

TypeScript protege em tempo de desenvolvimento. Dados vindos de API, banco, formulário ou arquivo ainda precisam ser validados em runtime.

## Erros comuns

- usar `any` para fugir do problema;
- criar tipos complexos demais;
- confiar em tipo para dado externo;
- misturar lógica e transformação sem clareza;
- não tratar promise rejeitada;
- ignorar null e undefined.

## Checklist

- [ ] Entradas externas são validadas?
- [ ] Funções críticas têm retorno tipado?
- [ ] `any` foi evitado?
- [ ] Tipos estão em lugar fácil de achar?
- [ ] Erros assíncronos são tratados?
- [ ] Código pode ser refatorado com segurança?

## Resumo para IA

TypeScript ajuda a tornar projetos JavaScript mais seguros e legíveis, mas não substitui validação real. Para projetos fullstack, usar tipos como contrato entre frontend, backend e dados.

## Links internos

- [[React-Next-e-Frontend-Moderno]]
- [[APIs-Backend-Banco]]
- [[Testes-e-Qualidade-de-Software]]
- [[Design-Patterns-e-Arquitetura-Limpa]]
