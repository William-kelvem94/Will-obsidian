---
title: "Instruções de Importação — Anki"
deck: "XAI Fairness Accountability"
created: 2026-05-18
lang: pt-BR
---

# Instruções para Importar Flashcards no Anki

## Passo a Passo

1. **Abra o Anki** e clique em **"Create Deck"** (Criar Baralho) no canto inferior direito.
   - Nomeie o baralho como: **XAI Fairness Accountability**

2. **Vá em File > Import** (Arquivo > Importar).
   - Selecione o arquivo `XAI-Fairness-Deck.csv`.

3. **Configurações de Importação:**
   - **Separator (Separador):** Semicolon `;` (Ponto e vírgula)
   - **Character set (Codificação):** UTF-8
   - **Deck (Baralho):** XAI Fairness Accountability
   - **Model (Modelo):** Basic (ou "Basic (and reversed card)" se preferir)

4. **Mapeamento de Campos (Field Mapping):**
   - Coluna 1 → **Front** (Frente) — a pergunta
   - Coluna 2 → **Back** (Verso) — a resposta
   - Coluna 3 → **Tags** — etiquetas para organização

   ⚠️ Certifique-se de que o Anki reconhece 3 campos. Se necessário, ajuste manualmente no menu suspenso ao lado de cada coluna.

5. **Clique em "Import"** (Importar).

## Estrutura do Arquivo

- Formato: CSV sem cabeçalho (separador `;`)
- Colunas: `Front;Back;Tags`
- Exemplo de linha:
  ```
  O que significa a sigla SHAP?;SHAP significa SHapley Additive exPlanations...;xai,shap
  ```

## Tags Incluídas

| Tag       | Assunto                         |
|-----------|---------------------------------|
| `xai`     | Explainable AI (geral)          |
| `shap`    | SHAP theory e prática           |
| `lime`    | LIME theory e prática           |
| `fairness`| Métricas de fairness            |
| `compas`  | Caso COMPAS / ProPublica        |
| `ethics`  | Ética e accountability          |
| `accountability`| Responsabilidade em IA    |
| `law`     | Regulamentação (AI Act, GDPR)   |

## Verificação Pós-Importação

- Total esperado: **~60 cartões**
- Navegue pelo baralho e estude alguns cartões para confirmar formatação
- Para revisar por tag, use o navegador do Anki (Browse > Tags)

## Dicas

- Ative o modo **"Card Browser"** para ver todos os cartões do baralho.
- Considere criar um **"Filtered Deck"** por tag se quiser estudar apenas SHAP ou apenas fairness.
- Para melhor retenção, estude 15-20 novos cartões por dia com o algoritmo SM-2 (padrão do Anki).
