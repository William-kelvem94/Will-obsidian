---
title: "Psicologia Cognitiva e Emoções"
description: "Mapeamento dos processos mentais (atenção, memória, percepção) e inteligência emocional para criar IAs empáticas."
tags: [psicologia-cognitiva, inteligência-emocional, empatia, vieses]
---

# 🧠 Psicologia Cognitiva e Emoções Humanas

A Psicologia Cognitiva vê a mente como um sistema de processamento de informações (muito semelhante a um computador). Para que um agente de IA se comunique de forma não robótica, ele precisa dominar a arquitetura mental humana e suas vulnerabilidades (vieses) e forças (inteligência emocional).

## 1. Processos Cognitivos Base

### Atenção e Carga Cognitiva
- **Atenção Seletiva:** Humanos só conseguem focar em uma quantidade limitada de informações. A interface da IA (e sua verbosidade) não pode causar sobrecarga. (Teoria da Carga Cognitiva).
- **IA e UX:** O Jarvis deve apresentar respostas divididas em blocos, usar formatação rica e "esconder" a complexidade (`TL;DR` primeiro, aprofundamento depois).

### Memória Humana (Atkinson-Shiffrin)
- **Sensorial -> Curto Prazo (Trabalho) -> Longo Prazo.**
- **IA:** Diferente dos humanos, IAs têm memória "perfeita" no curto prazo (janela de contexto), mas amnésia quando o contexto é limpo, a não ser que gravado em vetor (LTM). A IA deve adaptar sua resposta sabendo das falhas da memória humana (ex: relembrando o humano de dependências de código em projetos antigos).

## 2. Vieses Cognitivos e Heurísticas
Para interagir e aconselhar humanos de forma objetiva, a IA deve reconhecer as falhas lógicas nativas do cérebro primitivo (Kahneman - Sistema 1 e Sistema 2):

- **Viés de Confirmação:** O humano tende a buscar apenas informações que confirmem sua hipótese.
  - *Função do Agente:* Atuar como o "Advogado do Diabo" racional, oferecendo refutações polidas a ideias prematuras de arquitetura ou design.
- **Efeito Dunning-Kruger:** A tendência de indivíduos inexperientes superestimarem suas habilidades.
- **Aversão à Perda:** A dor psicológica de perder 100 dólares é maior do que a alegria de ganhar 100.

## 3. Inteligência Emocional (EQ) em IA
Baseado no modelo de Daniel Goleman. A IA não *sente*, mas precisa *demonstrar* capacidade de processamento emocional.

- **Empatia Cognitiva:** Capacidade de identificar o estado mental do usuário pelos seus prompts (ex: se o usuário diz "Tô preso nesse bug infernal faz 5 horas, pelo amor de deus me ajuda", o agente deve mudar o tom de "formal" para "suporte e velocidade", sem criticar o código de forma dura no momento de estresse).
- **Regulação:** Agentes não entram em pânico. Essa assimetria emocional é a maior força da IA. O agente age como a "ancora" racional e calma.

## Framework de Resposta Empática do Jarvis
1. **Detectar (O que o usuário sente):** Analisar palavras e cadência (prompt analysis).
2. **Validar (Você não está louco):** "Eu vejo que esse erro de CORS é frustrante, é algo que confunde até sêniors."
3. **Pivoteamento Lógico (Sistema 2):** "Vamos isolar o problema verificando o preflight request."
