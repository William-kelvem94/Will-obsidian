---
title: "Advanced Reasoning Patterns: ReAct, ToT e Reflexion"
description: "Análise profunda dos padrões de raciocínio avançado utilizados por agentes LLM para tomada de decisão e resolução de problemas complexos."
tags: [agentic, reasoning, react, tot, reflexion]
---

# 🧠 Padrões de Raciocínio Avançado para Agentes de IA

Para que agentes como o JARVIS superem respostas genéricas e atinjam o nível de resolução de problemas de um engenheiro sênior, é essencial a implementação de padrões estruturados de raciocínio.

## 1. ReAct (Reasoning + Acting)

ReAct é um framework que intercala passos de raciocínio (pensamento) com ações concretas no ambiente (uso de ferramentas).

### Como funciona
Em vez de simplesmente gerar uma resposta final com base no prompt, o agente opera em um loop:
- **Thought (Pensamento):** O agente reflete sobre o estado atual e o que precisa ser feito. Ex: "Eu preciso encontrar o erro no arquivo de log."
- **Action (Ação):** O agente escolhe e invoca uma ferramenta. Ex: `read_file(error.log)`.
- **Observation (Observação):** O agente recebe o resultado da ferramenta. Ex: "Erro de NullPointer na linha 42".
- **Repetição:** O ciclo recomeça até que o agente tenha certeza da resposta ou da solução (`Final Answer`).

### Por que é superior?
- **Correção de curso:** Se uma ação falhar, o próximo "Thought" permite que a IA perceba o erro e tente uma abordagem alternativa.
- **Transparência:** O log de "Thoughts" mostra exatamente como a IA chegou à conclusão.

## 2. Tree of Thoughts (ToT)

O *Tree of Thoughts* expande o paradigma do Chain of Thought permitindo que a IA explore múltiplos caminhos de raciocínio em paralelo, como uma árvore de busca em ciência da computação.

### Como funciona
1. **Geração de passos (Branches):** Dada uma etapa de um problema, a IA gera várias ideias possíveis sobre como prosseguir.
2. **Avaliação de estado (Heurística):** O modelo LLM avalia (pontua) cada um desses ramos, estimando a probabilidade de chegarem a uma solução válida.
3. **Busca e Backtracking:** O sistema explora os melhores caminhos (usando busca em largura ou profundidade). Se um caminho se provar inviável (beco sem saída), ele faz "backtracking" para o último nó viável.

### Aplicações ideais
- Otimização de arquiteturas complexas.
- Planejamento de código massivo onde escolhas iniciais afetam o final.
- Problemas matemáticos ou lógicos intensos.

## 3. Reflexion

Reflexion é um mecanismo que permite que agentes aprendam com seus próprios erros iterativamente, sem precisar de retreinamento de pesos (apenas no contexto).

### O Loop de Reflexão
1. **Tentativa Inicial:** O agente executa uma tarefa e falha (ex: código que não compila).
2. **Feedback/Evaluator:** Uma função externa (ou outro LLM) analisa a saída (ex: saída do compilador).
3. **Reflexão:** O agente é instruído a analisar *por que* falhou. O prompt de reflexão força o modelo a gerar uma "memória" do erro. Ex: "Eu chamei a função com um array em vez de um objeto."
4. **Tentativa subsequente:** Na próxima iteração, a "memória de reflexão" é injetada no prompt, evitando que o agente cometa o mesmo erro.

---
**Integração no JARVIS:**
Esses padrões devem ser encapsulados no orquestrador principal do Jarvis, combinando ToT para planejamento inicial ("set_plan") e ReAct + Reflexion para execução e debug autônomo.
