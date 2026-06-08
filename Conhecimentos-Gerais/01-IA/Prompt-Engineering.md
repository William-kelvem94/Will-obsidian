---
title: "Prompt Engineering"
date: 2026-06-07
updated: 2026-06-07
type: guide
status: active
tags: [conhecimento-geral, ia, prompt-engineering, llm, produtividade]
related: [[../00-Como-usar-este-vault-com-IA]], [[RAG-e-Memoria-para-Agentes]], [[Token-Economy]]
summary: "Fundamentos práticos de prompt engineering para obter respostas mais precisas, úteis e econômicas de modelos de linguagem."
---

# Prompt Engineering

Prompt engineering é a prática de formular pedidos para modelos de linguagem de modo que a resposta fique mais correta, útil, verificável e adequada ao objetivo.

## Fórmula base

Um bom pedido geralmente contém:

1. **Objetivo:** o que precisa ser produzido.
2. **Contexto:** informações necessárias.
3. **Critérios:** como avaliar se ficou bom.
4. **Formato:** estrutura de saída desejada.
5. **Limites:** o que não deve ser feito.
6. **Exemplos:** quando possível, exemplos de entrada e saída.

## Estrutura recomendada

```txt
Tarefa: ...
Contexto: ...
Objetivo final: ...
Restrições: ...
Formato de resposta: ...
Critérios de qualidade: ...
```

## Princípios

### 1. Especificidade vence tamanho

Um prompt curto e preciso costuma ser melhor do que um texto enorme e confuso.

### 2. Contexto deve ser selecionado, não despejado

Enviar todo o histórico pode piorar a resposta. O ideal é enviar o trecho certo, com objetivo claro.

### 3. O modelo precisa saber o que priorizar

Quando houver conflito, definir a ordem de prioridade. Exemplo: segurança > precisão > velocidade > estilo.

### 4. Saída precisa ter forma

Modelos respondem melhor quando sabem se devem entregar tabela, checklist, JSON, plano, resumo, código, diagnóstico ou parecer.

## Padrões úteis

### Análise técnica

- problema observado;
- ambiente;
- logs ou sintomas;
- tentativas já feitas;
- resultado esperado;
- resultado obtido.

### Revisão de código

- linguagem e framework;
- arquivo ou trecho;
- objetivo do código;
- erros conhecidos;
- critérios: segurança, performance, legibilidade, manutenção.

### Estudo

- tema;
- nível atual;
- objetivo;
- prazo;
- estilo de aprendizagem;
- tipo de entrega: plano, resumo, exercícios ou mapa mental.

### Decisão

- opções;
- critérios;
- restrições;
- riscos;
- reversibilidade;
- recomendação desejada.

## Erros comuns

| Erro | Consequência | Correção |
|---|---|---|
| pedido vago | resposta genérica | definir objetivo e formato |
| contexto demais | perda de foco | resumir antes |
| ausência de critérios | resposta bonita, mas inútil | dizer como avaliar |
| múltiplas tarefas misturadas | resposta incompleta | dividir em etapas |
| pedir certeza absoluta | risco de falsa confiança | pedir grau de incerteza |

## Prompt compacto para tarefas complexas

```txt
Analise o contexto abaixo e entregue:
1. resumo;
2. diagnóstico;
3. riscos;
4. recomendações;
5. próximos passos.
Se faltar informação, liste lacunas sem inventar.
```

## Prompt para transformar notas em conhecimento

```txt
Transforme este conteúdo em uma nota Obsidian com:
- YAML;
- resumo;
- conceitos principais;
- exemplos;
- links internos sugeridos;
- perguntas de revisão;
- próximos estudos.
```

## Links internos

- [[../00-Como-usar-este-vault-com-IA]]
- [[RAG-e-Memoria-para-Agentes]]
- [[Token-Economy]]
- [[../03-Estudos/Metodo-de-Estudo-Ativo]]
