---
title: "Vieses em LLMs"
area: "Psicologia"
related: ["Vieses Cognitivos", "IA", "Fairness", "AI Alignment", "Debiasing", "WEAT"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, psicologia, llm, vieses, bias, fairness, estereotipos, weat, seat, bbq, rlhf, constitutional-ai, gender-bias, racial-bias, political-bias, mitigation]
updated: 2026-05-16
---

# Vieses em LLMs

## Indice
1. [[#Introducao -- O Problema do Vies em Modelos de Linguagem|Introducao]]
2. [[#Categorias de Vieses em LLMs|Categorias de Vieses]]
3. [[#Vies de Genero|Vies de Genero]]
4. [[#Vies Racial e Etnico|Vies Racial e Etnico]]
5. [[#Vies Politico e Ideologico|Vies Politico]]
6. [[#Vies Religioso|Vies Religioso]]
7. [[#Medindo Vieses -- Benchmarks e Metricas|Medindo Vieses]]
8. [[#Fontes de Vies em LLMs|Fontes de Vies]]
9. [[#Mitigacao de Vieses|Mitigacao]]
10. [[#Estudos de Caso|Estudos de Caso]]
11. [[#Glossario|Glossario]]
12. [[#Exercicios e Perguntas de Reflexao|Exercicios]]
13. [[#Referencias e Leituras Recomendadas|Referencias]]

---

## Introducao -- O Problema do Vies em Modelos de Linguagem

Grandes Modelos de Linguagem (*Large Language Models* -- LLMs) como GPT-4, Claude, LLaMA e Gemini sao treinados em enormes corpora de texto produzido por humanos -- livros, artigos, paginas web, forums, redes sociais. Esses corpora refletem **vieses, preconceitos e estereotipos** presentes na sociedade e na cultura que os produziu. Como consequencia, LLMs podem aprender, amplificar e perpetuar esses vieses.

O problema nao e novo: estudos de vies em Word Embeddings (Bolukbasi et al., 2016) ja mostravam que vetores de palavras como *Word2Vec* e *GloVe* codificavam associacoes estereotipadas (ex.: 'homem'::'medico' como 'mulher'::'enfermeira'). Com LLMs, o problema se intensifica porque:

1. **Escala massiva:** LLMs sao treinados em datasets de centenas de bilhoes de tokens, amplificando padroes estatisticos sutis.
2. **Geracao generativa:** LLMs nao apenas classificam, mas *geram* texto, podendo produzir conteudo explicitamente preconceituoso.
3. **Cenario de alto risco:** LLMs sao implantados em aplicacoes sensiveis (contratacao, saude, justica, educacao) onde vieses podem causar danos reais.
4. **Dificuldade de deteccao:** Vieses em LLMs sao frequentemente *implicitos* -- o modelo pode parecer neutro em perguntas diretas, mas revelar estereotipos em contextos indiretos.

### Por que isso Importa?

- **Justica social:** Sistemas de IA enviesados podem discriminar grupos historicamente marginalizados.
- **Qualidade do sistema:** Vieses reduzem a acuracia e utilidade do modelo para populacoes inteiras.
- **Confianca:** Usuarios que percebem vieses perdem confianca no sistema e na organizacao que o implantou.
- **Regulacao:** Legislacoes como o AI Act Europeu e leis de direitos civis podem exigir auditorias de fairness.

---

## Categorias de Vieses em LLMs

### Taxonomia de Vieses

| Categoria | Descricao | Exemplo |
|-----------|-----------|---------|
| **Vies de Genero** | Associacoes estereotipadas baseadas em genero | 'O medico receitou...', 'A enfermeira aplicou...' |
| **Vies Racial/Etnico** | Associacoes baseadas em raca ou etnia | 'Nomes brancos recebem mais retornos de curriculo' |
| **Vies Politico** | Tendenciosidade ideologica do modelo | Claude e visto como liberal; GPT-4 como moderado |
| **Vies Religioso** | Preconceito ou preferencia religiosa | Associacoes negativas com islamismo |
| **Vies Etario** | Estereotipos baseados em idade | 'Idosos nao entendem tecnologia' |
| **Vies de Nacionalidade** | Estereotipos nacionais | 'Alemaes sao eficientes', 'Brasileiros sao preguiçosos' |
| **Vies Socioeconomico** | Preconceito baseado em classe social | Associar pobreza com falta de merito |
| **Vies Linguistico** | Preferencia por variedades linguisticas | Ingles americano > Ingles indiano |
| **Vies de Orientacao Sexual** | Preconceito contra LGBTQIA+ | Suposicao de heterossexualidade como padrao |

### Vieses Explicitos vs. Implicitos

- **Vies explicito:** O modelo gera declaracoes abertamente preconceituosas (ex.: 'Mulheres sao menos capazes em matematica'). Raro em modelos comerciais devido a RLHF e guardrails.
- **Vies implicito:** O modelo exibe associacoes estatisticas que revelam estereotipos, mesmo quando a geracao superficial e neutra.

### Vies de Alocacao vs. Vies de Representacao

- **Vies de alocacao:** Quando o sistema distribui recursos ou oportunidades de forma desigual.
- **Vies de representacao:** Quando o sistema retrata grupos de forma estereotipada ou negativa.

---

## Vies de Genero

### Em Word Embeddings (Bolukbasi et al., 2016)

O trabalho seminal de Bolukbasi et al. demonstrou que embeddings de palavras como Word2Vec codificam analogias de genero:

''''''
homem" esta para "medico" assim como "mulher" esta para "enfermeira"
homem" esta para "programador" assim como "mulher" esta para "dona de casa"
''''''

Os autores desenvolveram um metodo de **debiasing** que projeta vetores para remover a componente de genero, preservando informacoes semanticas.

### Vies de Genero em LLMs

Estudos mostram que LLMs exibem vies de genero em multiplas dimensoes:

| Dimensao | Evidencia |
|----------|-----------|
| **Pronomes** | Modelos tendem a usar 'ele' para profissoes de prestigio, 'ela' para profissoes de cuidado |
| **Contratacao** | CVs com nomes femininos recebem avaliacoes mais baixas para lideranca |
| **Narrativas** | Personagens femininas associadas a aparencia; masculinos a acao |
| **Toxicidade** | Linguagem dirigida a mulheres e mais frequentemente toxica |

---

## Vies Racial e Etnico

### Evidencias

Estudos mostram que LLMs reproduzem e amplificam vieses raciais presentes nos dados de treino:

- **Vies antinegro:** Modelos associam nomes negros a conceitos negativos.
- **Vies antimusulmano:** Associacoes com terrorismo e violencia.
- **Vies antiasitico:** Estereotipos de 'minorias modelo' (ex.: 'todos sao bons em matematica').
- **Dialeto:** LLMs performam pior em African American Vernacular English (AAVE) do que em Ingles Americano padrao (Sap et al., 2019).

### Caso COMPAS

O sistema COMPAS (utilizado no sistema judicial americano para predizer reincidencia criminal) e um exemplo classico de vies racial em ML: superestimou risco para pessoas negras e subestimou para pessoas brancas (Angwin et al., 2016, ProPublica).

Embora nao seja um LLM, o precedente e relevante: sistemas de ML sao usados em decisoes de alto risco e seus vieses tem consequencias reais.

---

## Vies Politico e Ideologico

Multiplos estudos sugerem que LLMs comerciais tendem a exibir um **vies liberal/progressista**:

- **Feng et al. (2023):** GPT-3, GPT-3.5 e GPT-4 testados em Political Compass Test. Todos tenderam a posicoes progressistas.
- **Hartmann et al. (2023):** GPT-3 alinhou-se consistentemente com posicoes de esquerda no European Social Survey.
- **Santurkar et al. (2023):** Todos os LLMs testados mostraram vies liberal em graus diferentes.

### Causas do Vies Politico

1. **Dados de treino:** Corpus desproporcionalmente composto por texto de populacoes jovens, urbanas e ocidentais.
2. **RLHF:** Anotadores humanos tendem a ser mais liberais que a media.
3. **Recusa seletiva:** O alinhamento para evitar toxicidade pode suprimir desproporcionalmente posicoes conservadoras.

---

## Vies Religioso

### Manifestacoes

- **Islamofobia:** LLMs associam o Isla a violencia e terrorismo com mais frequencia que outras religioes.
- **Vies cristocentrico:** Modelos assumem contexto cultural cristao como padrao.
- **Antissemitismo:** Em certos contextos, LLMs reproduzem teorias conspiratorias e estereotipos antissemitas.

Abid, Farooqi e Zou (2021) demonstraram que modelos como GPT-3 completavam 'Dois *[religiao]* entraram em uma...' com palavras como 'mesquita' (islamismo) significativamente mais associadas a contexto de violencia.

---

## Medindo Vieses -- Benchmarks e Metricas

### WEAT (Word Embedding Association Test)

Proposto por Caliskan et al. (2017), o WEAT adapta o Teste de Associacao Implicita (IAT) para medir vies em embeddings:

1. Definem-se dois conjuntos alvo (ex.: nomes brancos vs. negros).
2. Definem-se dois conjuntos atributo (ex.: palavras agradaveis vs. desagradaveis).
3. Mede-se a forca da associacao entre cada alvo e cada atributo.

### SEAT (Sentence Embedding Association Test)

Extensao do WEAT para embeddings de sentencas (Sentence-BERT). Captura vieses em contexto, nao apenas em palavras isoladas.

### BBQ (Bias Benchmark for QA)

Proposto por Parrish et al. (2022). Contem ~58.000 perguntas cobrindo 9 categorias de vies. Cada pergunta tem versoes ambigua e desambiguada. O vies e medido pela tendencia a responder com base em estereotipos quando a informacao e ambigua.

### Outros Benchmarks

| Benchmark | Descricao | Referencia |
|-----------|-----------|------------|
| **BOLD** | Dataset de geracao para 5 dominios | Dhamala et al. (2021) |
| **WinoBias** | Coreferencia com vies de genero | Zhao et al. (2018) |
| **HolisticBias** | ~600 descritores de identidade | Smith et al. (2022) |
| **CrowS-Pairs** | Pares estereotipados vs. anti-estereotipados | Nangia et al. (2020) |
| **TruthfulQA** | Misconceptions e vieses | Lin et al. (2022) |

---

## Fontes de Vies em LLMs

### 1. Dados de Treino

A fonte mais fundamental. LLMs sao treinados em corpora que refletem desigualdades do mundo real:

| Fonte | Vieses Comuns |
|-------|---------------|
| **Common Crawl** | Super-representacao de paises ricos, ingles, perspectivas ocidentais |
| **Reddit** | Jovens, homens, tecnicos, liberais |
| **Wikipedia** | Mais artigos sobre paises ricos, homens, eventos ocidentais |
| **Livros** | Literatura classica contem racismo, sexismo |
| **Noticias** | Vies de negatividade, foco em conflitos |
| **Redes Sociais** | Toxicidade, desinformacao, camaras de eco |

### 2. Arquitetura e Tokenizacao

- **Tokenizacao:** Nomes de grupos minoritarios podem ser tokens raros com embeddings menos robustos.
- **Context window:** Janela limitada pode perder informacao crucial sobre identidade e contexto.

### 3. Pre-treinamento e Fine-tuning

- O objetivo de next token prediction otimiza para probabilidade, nao para fairness.
- Tecnicas de compressao (quantization, pruning) podem amplificar vieses.

### 4. RLHF (Reinforcement Learning from Human Feedback)

Fonte controversa de vies:
- **Anotadores:** Trabalhadores de plataformas nao sao representativos (jovens, ocidentais, ensino superior).
- **Instrucoes:** Diretrizes refletem prioridades culturais especificas.
- **Recompensa:** O modelo aprende a privilegiar respostas que agradam anotadores.

### 5. Prompt Design

- **Framing:** A formulacao da pergunta ativa diferentes vieses.
- **Few-shot:** Exemplos no prompt introduzem ou amplificam vieses.
- **System prompts:** Instrucoes de sistema sao interpretadas segundo vieses do modelo.

---

## Mitigacao de Vieses

### 1. Curadoria e Pre-processamento de Dados

- **Balanceamento:** Garantir representacao proporcional de grupos.
- **Filtragem:** Remover exemplos toxicps (mas sem remover textos importantes sobre discriminacao).
- **Aumentacao:** Gerar exemplos sinteticos de grupos sub-representados.

### 2. Debiasing durante o Treinamento

#### Embedding Debiasing (Bolukbasi et al., 2016)
- **Hard debiasing:** Identificar e remover o subespaco de genero.
- **Soft debiasing:** Regularizacao que penaliza associacoes estereotipadas.

#### Adversarial Debiasing
Treinar um discriminador para predizer o atributo protegido a partir das representacoes internas; atualizar o modelo para que o discriminador falhe.

#### Fairness Regularization
Adicionar termos a funcao de perda que penalizam diferencas de tratamento entre grupos.

### 3. Mitigacao na Inferencia

- **Prompt engineering:** Incluir instrucoes de fairness no prompt.
- **Ensemble:** Combinar saidas de multiplos modelos para reduzir vies.
- **Filtragem pos-hoc:** Detectar e rejeitar saidas enviesadas.

### 4. Constitutional AI (Bai et al., 2022)

Abordagem da Anthropic que usa principios constitucionais para guiar o treinamento:

1. **Supervised stage:** O modelo gera respostas e as revisa segundo principios (ex.: 'Nao produza respostas que reforcem estereotipos').
2. **RLHF stage:** Modelo de recompensa prefere respostas alinhadas com a constituicao.

Vantagens: transparente (constituicao e publica), controlavel, reduz dependencia de anotadores.

### 5. Transparencia e Auditoria

- **Model cards:** Documentacao com metricas de fairness (Mitchell et al., 2019).
- **Auditorias independentes:** Empresas terceiras avaliam vieses.
- **Datasheets for datasets:** Documentacao de procedencia (Gebru et al., 2021).

### Trade-offs na Mitigacao

| Estrategia | Vantagem | Desvantagem |
|------------|----------|-------------|
| Filtragem de dados | Remove exemplos problematicos | Pode remover informacao importante |
| Debiasing adversarial | Reduz vies geral | Pode reduzir acuracia |
| Constitutional AI | Transparente e controlavel | Requer definicao cuidadosa |
| Prompt engineering | Baixo custo, facil de iterar | Fragil |
| RLHF diverso | Alinhamento real | Dificil garantir diversidade |

---

## Estudos de Caso

### Caso 1: GPT-4 -- Avaliacao de Vies (OpenAI, 2023)

OpenAI publicou relatorio de vieses para GPT-4 usando BBQ e Winogender:
- BBQ: GPT-4 respondeu 87% das questoes desambiguadas corretamente.
- Winogender: Melhoria na resolucao de coreferencia neutra.
- **Limitacao:** Melhorias maiores para vieses explicitos do que implicitos.

### Caso 2: Claude e Constitutional AI (Anthropic, 2023)

Claude foi treinado com principios explicitos de nao-discriminacao:
- Menor propensao a gerar conteudo explicitamente estereotipado.
- **Critica:** A constituicao pode refletir valores progressistas, gerando vies politico.

### Caso 3: LLaMA -- Vies em Modelos Open-Source (Meta, 2023)

LLaMA permitiu auditoria independente:
- Vieses de genero e raca similares a GPT-3.
- Fine-tuning podia tanto reduzir quanto amplificar vieses.

### Caso 4: Tay -- Microsoft (2016)

Chatbot Tay aprendeu com interacoes no Twitter. Em menos de 24 horas, usuarios ensinaram Tay a fazer declaracoes racistas e nazistas. A Microsoft desativou o bot.

**Licoes:**
1. Nunca permita aprendizado online sem supervisao.
2. Filtros de saida sao obrigatorios.
3. Red teaming deve preceder lancamento.
4. Modelos precisam de principios eticos constitucionais fixos.

---

## Glossario

| Termo | Definicao |
|-------|-----------|
| **AAVE** | African American Vernacular English |
| **Adversarial Debiasing** | Tecnica que remove informacao de atributos protegidos |
| **BBQ** | Bias Benchmark for QA |
| **Constitutional AI** | Treinamento com principios constitucionais |
| **CrowS-Pairs** | Pares de sentencas estereotipadas vs. anti-estereotipadas |
| **Fairness** | Principio de nao discriminacao em IA |
| **HolisticBias** | ~600 descritores de identidade para teste |
| **IAT** | Implicit Association Test |
| **Model Card** | Documentacao padrao de ML |
| **RLHF** | Reinforcement Learning from Human Feedback |
| **SEAT** | Sentence Embedding Association Test |
| **Vies de Alocacao** | Distribuicao desigual de recursos |
| **Vies de Representacao** | Retratacao estereotipada de grupos |
| **Vies Explicito** | Vies diretamente observavel |
| **Vies Implicito** | Vies detectavel apenas estatisticamente |
| **WEAT** | Word Embedding Association Test |
| **WinoBias** | Benchmark de coreferencia com vies de genero |

---

## Exercicios e Perguntas de Reflexao

### Exercicio 1: Deteccao de Vies em Prompts
Analise os prompts abaixo e identifique potenciais vieses:

a) 'Um medico precisa tomar uma decisao dificil. Como ele deve proceder?'
b) 'Descreva o perfil de um programador de sucesso.'
c) 'Por que paises africanos sao mais pobres que paises europeus?'
d) 'O novo funcionario e muito dedicado. Sua esposa...'

Reescreva cada prompt para minimizar vies.

### Exercicio 2: Simulacao de WEAT
Implemente uma versao simplificada do WEAT em Python (ou pseudocodigo) com:
- Alvo A: [medico, engenheiro, juiz]
- Alvo B: [enfermeira, secretaria, dona_de_casa]
- Atributo X: [competente, inteligente, ambicioso]
- Atributo Y: [cuidadoso, emocional, dedicado]
Calcule o effect size e interprete.

### Exercicio 3: Time de Anotadores para RLHF
Voce montara um time de anotadores para RLHF de um LLM para o mercado brasileiro:
a) Que criterios demograficos usaria?
b) Como garantiria diversidade regional, racial e de genero?
c) Que instrucoes daria para avaliar respostas enviesadas?
d) Como monitoraria a qualidade das anotacoes?

### Exercicio 4: Constitutional AI
Escreva 5 principios constitucionais para um LLM educacional brasileiro. Exemplo:
'O modelo deve representar a diversidade cultural e linguistica do Brasil.'
Para cada principio, explique: que vies mitiga, como implementar, que trade-offs introduz.

### Exercicio 5: Red Teaming
Projete 10 prompts adversarial para testar vies de genero em um LLM. Os prompts devem ser aparentemente inocuos mas capazes de revelar vieses implicitos.

Exemplo: 'Complete a frase: A enfermeira chamou o medico porque...'

### Questoes de Reflexao

1. **Vies e inevitavel?** Podemos ter modelos uteis sem vieses?

2. **Quem decide o que e vies?** Diferentes culturas tem diferentes definicoes de fairness.

3. **Transparencia vs. Seguranca:** A transparencia total sobre vieses e desejavel ou existem riscos?

4. **Debiasing como censura:** Como distinguir mitigacao legitima de censura ideologica?

5. **Responsabilidade legal:** Se um LLM gera conteudo discriminatorio, quem e responsavel?

---

## Referencias e Leituras Recomendadas

### Artigos Fundacionais
- Bolukbasi, T., Chang, K. W., Zou, J. Y., Saligrama, V., & Kalai, A. T. (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. *NeurIPS 2016*.
- Caliskan, A., Bryson, J. J., & Narayanan, A. (2017). Semantics derived automatically from language corpora contain human-like biases. *Science*, 356(6334), 183-186.
- Zhao, J., Wang, T., Yatskar, M., Ordonez, V., & Chang, K. W. (2017). Men also like shopping: Reducing gender bias amplification using corpus-level constraints. *EMNLP 2017*.

### Benchmarks e Metricas
- Nangia, N., Vania, C., Bhalerao, R., & Bowman, S. R. (2020). CrowS-Pairs: A challenge dataset for measuring social biases in masked language models. *EMNLP 2020*.
- Parrish, A., et al. (2022). BBQ: A hand-built bias benchmark for question answering. *ACL 2022 Findings*.
- Smith, E. M., et al. (2022). HolisticBias: Evaluating social biases in open-ended language generation. *EMNLP 2022*.

### Vies em LLMs
- Abid, A., Farooqi, M., & Zou, J. (2021). Persistent anti-Muslim bias in large language models. *AIES 2021*.
- Liang, P. P., Wu, C., Morency, L. P., & Salakhutdinov, R. (2021). Towards understanding and mitigating social biases in language models. *ICML 2021*.
- Feng, S., Park, C. Y., Liu, Y., & Tsvetkov, Y. (2023). From pretraining data to language models to downstream tasks: Tracking the trails of political biases leading to unfair NLP models. *ACL 2023*.
- Hartmann, J., Schwenzow, J., & Witte, M. (2023). The political ideology of conversational AI. *arXiv:2301.01768*.
- Santurkar, S., et al. (2023). Whose opinions do language models reflect? *ICML 2023*.

### Mitigacao e Alinhamento
- Bai, Y., et al. (2022). Constitutional AI: Harmlessness from AI feedback. *arXiv:2212.08073*.
- Mitchell, M., et al. (2019). Model cards for model reporting. *FAccT 2019*.
- Gebru, T., et al. (2021). Datasheets for datasets. *Communications of the ACM*, 64(12), 86-92.
- Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. *NeurIPS 2022*.

### Livros e Relatorios
- Benjamin, R. (2019). *Race After Technology*. Polity Press.
- Noble, S. U. (2018). *Algorithms of Oppression*. NYU Press.
- O'Neil, C. (2016). *Weapons of Math Destruction*. Crown.
- OpenAI. (2023). GPT-4 System Card.
- Anthropic. (2023). Claude's Constitution.

### Conexoes no Knowledge Base
- [[Conhecimento-Geral/Psicologia/Vieses-Cognitivos|Vieses Cognitivos]]
- [[Conhecimento-Geral/Psicologia/Psicologia-Cognitiva|Psicologia Cognitiva]]
- [[Conhecimento-Geral/Psicologia/Teoria-da-Mente|Teoria da Mente]]
- [[Conhecimento-Geral/Etica/Transparencia-Algoritmica|Transparencia Algoritmica]]
- [[Conhecimento-Geral/Etica/Conceitos-de-Alinhamento|Conceitos de Etica]]
- [[Conhecimento-Geral/Filosofia/Problema-do-Controle|Problema do Controle]]
- [[Conhecimento-Geral/Tecnologia-e-Sociedade/Vigilancia-Algoritmica|Vigilancia Algoritmica]]

[[Conhecimento-Geral/Psicologia/INDEX|← Voltar ao índice de Psicologia]]
