---
title: "Design Patterns e Arquitetura Limpa"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, arquitetura, design-patterns, clean-architecture]
related: [[Arquitetura-Web-Moderna]], [[APIs-Backend-Banco]], [[TypeScript-e-JavaScript-Moderno]], [[Testes-e-Qualidade-de-Software]]
summary: "Guia prático sobre padrões de projeto, arquitetura limpa, separação de responsabilidades e código sustentável."
---

# Design Patterns e Arquitetura Limpa

Design patterns são soluções recorrentes para problemas recorrentes. Arquitetura limpa organiza dependências para manter regras de negócio protegidas de detalhes externos.

## Ideia central

Código bom não é só código que funciona. É código que pode mudar sem quebrar tudo.

## Princípios

| Princípio | Ideia |
|---|---|
| responsabilidade única | cada parte tem motivo claro para mudar |
| baixo acoplamento | partes dependem pouco umas das outras |
| alta coesão | coisas relacionadas ficam juntas |
| inversão de dependência | regra não depende de detalhe externo |
| fronteiras claras | cada camada sabe seu papel |

## Camadas comuns

```txt
Interface / Controller
  ↓
Use Case / Service
  ↓
Domain
  ↓
Repository Interface
  ↓
Infrastructure
```

## Patterns úteis

| Pattern | Uso |
|---|---|
| Repository | abstrair acesso a dados |
| Factory | criar objetos com regra |
| Adapter | integrar sistema externo |
| Strategy | trocar comportamento por configuração |
| Observer | reagir a eventos |
| Decorator | adicionar comportamento sem alterar base |
| Command | representar ação como objeto |

## Quando aplicar pattern

Aplicar quando existe dor real:

- duplicação recorrente;
- regra espalhada;
- dificuldade de testar;
- troca provável de implementação;
- integração externa instável;
- crescimento do domínio.

## Quando não aplicar

Evitar quando:

- projeto é pequeno;
- problema ainda não existe;
- pattern deixa código mais obscuro;
- abstração custa mais que repetição;
- equipe não entende a estrutura.

## Erros comuns

- usar pattern para parecer avançado;
- criar camadas demais;
- esconder regra em lugar errado;
- depender de framework no domínio;
- transformar tudo em interface;
- perder simplicidade.

## Checklist

- [ ] A regra de negócio está clara?
- [ ] A infraestrutura está separada?
- [ ] É possível testar sem banco real?
- [ ] A abstração tem motivo real?
- [ ] O código ficou mais fácil de entender?
- [ ] Novas mudanças cabem sem reescrever tudo?

## Resumo para IA

Design patterns e arquitetura limpa devem reduzir acoplamento e proteger regras de negócio. Só aplicar abstrações quando resolvem dor real, não por estética arquitetural.

## Links internos

- [[Arquitetura-Web-Moderna]]
- [[APIs-Backend-Banco]]
- [[TypeScript-e-JavaScript-Moderno]]
- [[Testes-e-Qualidade-de-Software]]
