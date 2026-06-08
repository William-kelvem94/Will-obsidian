---
title: "Template-Prompt-Otimizado"
tags: [template, prompt, token-economy, otimizado, eficiencia]
date: 2026-06-01
updated: 2026-06-01
category: template
---

# Template de Prompt Otimizado para Máxima Economia de Tokens

> Use este template sempre que interagir com IAs para garantir máxima densidade informacional.

---

## 🧩 1. System Prompt Format (YAML)

```yaml
---
role: <analyst|coder|writer|planner|critic>
model: <modelo_alvo>
ctx_window: <tamanho>
expertise: [<area1>, <area2>]
constraints:
  output_lang: pt-br
  max_tokens: <N>
  tone: <direct|concise|technical>
  format: <text|json|yaml|table>
output_schema:
  - key: <field_name>
    type: <string|int|bool|list>
    desc: "<descrição>"
rules:
  - "<regra1>"
  - "<regra2>"
---
```

---

## 📝 2. Task Prompt Format

```yaml
---
task: <TASK_TYPE>
  - <"Descricao_da_tarefa">
input:
  <key>: <value>
ctx_refs:
  - "[[link_para_contexto_relevante]]"
output:
  format: <json|yaml|text>
  schema:
    - field1
    - field2
constraints:
  - "regra1"
  - "regra2"
---
```

---

## 🔄 3. Few-Shot Otimizado

```
## EXEMPLOS
IN: <input_concise>
OUT: <output_concise>
---
IN: <input_concise>
OUT: <output_concise>
---
IN: <entrada_real>
OUT:
```

---

## 🔗 4. Cross-Reference Format

```
## REFS
- [[04-Conhecimentos/Knowledge-Base/TOKEN-ECONOMY]] # token-opt
- [[04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND]] # abbreviations
- [[02-JARVIS/JARVIS/TOKEN-COMPRESSION]] # ctx-compress

## CHUNKS
- <caminho_nota>:<linhas>
- <caminho_nota>:<linhas>
```

---

## ⚡ 5. Quick Command Format

```
/CMD <comando_base>
  --flag1 <val1>
  --flag2 <val2>

/QUERY <pergunta_direta>

/FORMAT <json|yaml>

/REF [[nota]]
```

---

## 📐 6. Exemplo Real

**❌ Antes (~350 tokens):**
```
Olá, poderia me ajudar com uma análise? Eu preciso que você analise o documento 
que está neste link e me diga quais são os principais pontos, considerando 
também o histórico do projeto. Seria ótimo se você pudesse fornecer uma 
análise detalhada com recomendações...
```

**✅ Depois (~80 tokens):**
```yaml
task: analyze
  - "Extract key points from [[PRJ/relatorio.pdf]]"
ctx_refs:
  - "[[02-JARVIS/JARVIS/Estado.md]]"
output:
  format: yaml
  schema:
    - top_3_findings
    - risks
    - recommendations
```

---

## 🔗 Crosslinks

- [[04-Conhecimentos/Knowledge-Base/TOKEN-ECONOMY]]
- [[04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND]]
- [[02-JARVIS/JARVIS/TOKEN-COMPRESSION]]
- [[99-Templates/Legado/Template Base]]
- [[INDEX]]
