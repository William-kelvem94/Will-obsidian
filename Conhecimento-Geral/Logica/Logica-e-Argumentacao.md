---
title: "Lógica e Argumentação"
description: "Estudo abrangente da lógica formal, informal e dialética, abrangendo lógica proposicional, lógica de predicados, falácias formais e informais, teorias da argumentação, lógicas não-clássicas e suas conexões com inteligência artificial."
tags: [logica, argumentacao, raciocinio, logica-formal, logica-informal, falacias, proposicional, predicados, silogismos, deducao, inducao, abducao, logica-modal, logica-epistemica, logica-deontica, logica-temporal, logica-fuzzy, raciocinio-automatizado, ia]
updated: 2026-05-18
related: ["Conhecimento-Geral/Filosofia/Epistemologia", "Conhecimento-Geral/Matematica/Matematica-Discreta", "Conhecimento-Geral/Filosofia/Filosofia-da-Ciencia", "Conhecimento-Geral/Psicologia/Vieses-Cognitivos", "Conhecimento-Geral/Filosofia/Conceitos-Fundamentais"]
---

# Lógica e Argumentação

## Índice

1. [[#O Que e Logica|O Que e Logica]]
2. [[#Logica Formal vs Informal vs Dialetica|Logica Formal vs Informal vs Dialetica]]
3. [[#Logica Proposicional|Logica Proposicional]]
4. [[#Logica de Predicados|Logica de Predicados]]
5. [[#Falacias Formais|Falacias Formais]]
6. [[#Falacias Informais|Falacias Informais]]
7. [[#Argumentacao -- Estrutura e Tipos de Raciocinio|Argumentacao]]
8. [[#Logicas Nao-Classicas|Logicas Nao-Classicas]]
9. [[#Conexoes com Inteligencia Artificial|Conexoes com IA]]
10. [[#Glossario|Glossario]]
11. [[#Exercicios de Raciocinio Logico|Exercicios]]
12. [[#Referencias|Referencias]]

---

## O Que e Logica

A logica (do grego *logos* — palavra, razao, discurso) e o estudo dos **principios do raciocinio valido**. E a disciplina que investiga como inferencias sao feitas, quais estruturas de argumentacao preservam a verdade das premissas e como distinguir argumentos corretos de incorretos.

Diferentemente da psicologia (que estuda *como* as pessoas realmente pensam), a logica e uma disciplina **normativa**: ela prescreve *como* se *deve* pensar para raciocinar corretamente. A logica nao descreve processos mentais; ela estabelece padroes de inferencia valida.

### Perguntas Fundamentais da Logica

1. O que faz um argumento ser **valido**?
2. Como distinguir raciocinio **correto** de **incorreto**?
3. Quais sao as **regras formais** que governam a inferencia?
4. Como a **verdade** das premissas se relaciona com a **validade** do argumento?
5. O que significa "seguir-logicamente-de"?

### Breve Historia da Logica

A logica tem uma historia de mais de dois milenios, geralmente dividida em tres periodos:

**Logica antiga e medieval:** Aristoteles (384-322 a.C.) e o fundador da logica como disciplina sistematica. Seu *Organon* (conjunto de seis tratados) estabeleceu a teoria do silogismo, o estudo dos termos, proposicoes e inferencias categoricas. Logicos estoicos (Crisipo, sec. III a.C.) desenvolveram a logica proposicional, antecipando conectivos e regras de inferencia. Na Idade Media, logica aristotelica foi refinada por filosofos como Pedro Abelardo, Tomas de Aquino e Guilherme de Ockham, e integrada a teologia e a filosofia escolastica.

**Logica moderna (seculos XVII-XIX):** Leibniz (1646-1716) sonhou com uma *characteristica universalis* — uma linguagem universal que permitiria resolver disputas por calculo. G. W. F. Hegel desenvolveu uma logica dialetica. Mas foi no seculo XIX que a logica passou por uma revolucao.

**Logica contemporanea (pos-1847):** George Boole (1847, *The Mathematical Analysis of Logic*) inaugurou a algebra booleana, conectando logica a matematica. Gottlob Frege (1879, *Begriffsschrift*) criou a logica de predicados de primeira ordem — a linguagem formal que domina a logica contemporanea. Bertrand Russell e Alfred North Whitehead (1910-1913, *Principia Mathematica*) tentaram reduzir a matematica a logica. Kurt Godel (1931) provou os teoremas da incompletude, que limitam o que sistemas formais podem provar. Alfred Tarski (1933) desenvolveu a teoria semântica da verdade. Alan Turing (1936) conectou logica a computacao.

### Logica e Linguagem

A logica contemporanea opera em duas dimensoes:

**Sintaxe:** Regras formais para construcao de formulas e inferencias, independentemente de significado. A sintaxe define o que conta como uma formula bem-formada e quais sequencias de formulas constituem provas validas.

**Semântica:** Atribuicao de significado as formulas. Na logica classica, a semântica e tipicamente **teorico-conjuntural** (teoria de modelos): formulas sao interpretadas em estruturas matematicas (modelos), e a verdade de uma formula e definida em relacao a um modelo.

---

## Logica Formal vs Informal vs Dialetica

### Logica Formal

A logica formal estuda a **forma** dos argumentos, abstraindo-se do conteudo. Ela analisa se a conclusao segue necessariamente das premissas com base exclusivamente na estrutura logica, independentemente do assunto tratado.

Exemplo de argumento formalmente valido:
- Premissa 1: Todo homem e mortal.
- Premissa 2: Socrates e homem.
- Conclusao: Socrates e mortal.

A validade deste argumento depende da forma (Todo A e B; C e A; logo C e B), nao do conteudo (homens, mortalidade, Socrates). A logica formal utiliza linguagens artificiais (simbolos, regras precisas) para eliminar ambiguidades da linguagem natural.

### Logica Informal

A logica informal estuda o **uso da logica na linguagem natural**, considerando contexto, retorica, dialectica e pragmatica. Ela se concentra na analise e avaliacao de argumentos cotidianos — aqueles encontrados em debates politicos, textos academicos, conversas do dia a dia.

A logica informal nao substitui a formal; ela a complementa, oferecendo ferramentas para:
- Identificar e reconstruir argumentos em linguagem natural
- Avaliar a **solidez** (verdade das premissas + validade) de argumentos
- Detectar **falacias** informais
- Analisar **supressoes** (premissas nao explicitadas) e ambiguidades
- Considerar o **contexto dialogico** do argumento

O campo foi formalmente estabelecido com o trabalho de Stephen Toulmin (1958, *The Uses of Argument*), que propoe um modelo pragmatico de argumentacao com seis componentes: pretensao (*claim*), dados (*data*), garantia (*warrant*), apoio (*backing*), qualificador modal (*modal qualifier*) e condicoes de refutacao (*rebuttal*).

### Logica Dialetica

A logica dialetica, cujas raizes estao em Heraclito e que foi sistematizada por Hegel e Marx, ve a oposicao e a contradicao como motor do desenvolvimento do pensamento e da realidade. Diferentemente da logica formal (que rejeita contradicoes — principio da nao-contradicao), a dialetica ve as contradicoes como **imanentes** e **produtivas**.

A estrutura classica: **tese** (afirmacao) → **antitese** (negacao) → **sintese** (superacao que preserva os aspectos validos de ambas).

A logica dialetica e frequentemente contrastada com a logica formal por ser:
- **Processual:** O raciocinio se desenvolve no tempo, atraves de confronto de posicoes
- **Contextual:** A verdade e situada historica e socialmente
- **Transformadora:** A contradicao e motor de mudanca, nao obstaculo

Enquanto a logica formal busca **consistencia** e **validade dedutiva**, a dialetica busca **compreensao** e **sintese** de opostos. Ambas tem papeis distintos mas complementares na investigacao intelectual.

---

## Logica Proposicional

### Sintaxe da Logica Proposicional

A logica proposicional trabalha com **proposicoes** (sentencas declarativas que podem ser verdadeiras ou falsas) e **conectivos logicos** que as combinam.

**Atomos proposicionais:** Variaveis que representam proposicoes simples: p, q, r, s, ...

**Conectivos logicos:**

| Conectivo | Simbolo | Leitura | Exemplo |
|-----------|---------|---------|---------|
| Negacao | ¬ | "nao" | ¬p: "nao p" |
| Conjuncao | ∧ | "e" | p ∧ q: "p e q" |
| Disjuncao | ∨ | "ou" | p ∨ q: "p ou q" |
| Condicional | → | "se...entao" | p → q: "se p entao q" |
| Bicondicional | ↔ | "...se e somente se..." | p ↔ q: "p se e somente se q" |

**Formacao de formulas:**
1. Toda variavel proposicional e uma formula bem-formada (fbf).
2. Se φ e uma fbf, entao ¬φ e uma fbf.
3. Se φ e ψ sao fbfs, entao (φ ∧ ψ), (φ ∨ ψ), (φ → ψ), (φ ↔ ψ) sao fbfs.
4. Nada mais e fbf.

### Semântica: Tabelas-Verdade

A semântica da logica proposicional e definida por **tabelas-verdade**, que atribuem valores de verdade (V = verdadeiro, F = falso) a cada formula para todas as combinacoes possiveis de suas variaveis.

**Tabela do condicional (p → q):**

| p | q | p → q |
|---|---|-------|
| V | V | V |
| V | F | F |
| F | V | V |
| F | F | V |

Um aspecto contra-intuitivo do condicional material: quando o antecedente e falso, o condicional e **verdadeiro** independentemente do consequente. Isso captura a ideia de que uma promessa condicional so e violada quando o antecedente e verdadeiro e o consequente falso.

**Tabela do bicondicional (p ↔ q):**

| p | q | p ↔ q |
|---|---|-------|
| V | V | V |
| V | F | F |
| F | V | F |
| F | F | V |

O bicondicional e verdadeiro quando p e q tem o mesmo valor de verdade.

### Tautologias, Contradicoes e Contingencias

**Tautologia:** Formula que e verdadeira em **todas** as interpretacoes (todas as linhas da tabela-verdade). Exemplo: p ∨ ¬p (principio do terceiro excluido).

**Contradicao:** Formula que e falsa em **todas** as interpretacoes. Exemplo: p ∧ ¬p.

**Contingencia:** Formula que e verdadeira em algumas interpretacoes e falsa em outras. Exemplo: p ∧ q.

Tautologias sao particularmente importantes porque representam **verdades logicas** — proposicoes que sao verdadeiras em virtude de sua forma logica, independentemente do conteudo.

### Equivalencias Logicas Notaveis

Duas formulas φ e ψ sao **logicamente equivalentes** (φ ≡ ψ) quando tem o mesmo valor de verdade em toda interpretacao.

**Leis fundamentais:**
1. **Dupla negacao:** ¬¬p ≡ p
2. **Idempotencia:** p ∧ p ≡ p; p ∨ p ≡ p
3. **Comutatividade:** p ∧ q ≡ q ∧ p; p ∨ q ≡ q ∨ p
4. **Associatividade:** (p ∧ q) ∧ r ≡ p ∧ (q ∧ r); (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)
5. **Distributividade:** p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r); p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
6. **Leis de De Morgan:** ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q
7. **Contrapositiva:** p → q ≡ ¬q → ¬p
8. **Eliminacao do condicional:** p → q ≡ ¬p ∨ q
9. **Exportacao:** (p ∧ q) → r ≡ p → (q → r)
10. **Absorcao:** p ∧ (p ∨ q) ≡ p

### Regras de Inferencia

Regras de inferencia sao padroes de raciocinio que garantem que, se premissas sao verdadeiras, a conclusao tambem sera.

**Regras fundamentais:**

1. **Modus Ponens (MP):**
   p → q
   p
   ∴ q

2. **Modus Tollens (MT):**
   p → q
   ¬q
   ∴ ¬p

3. **Silogismo Hipotetico (SH):**
   p → q
   q → r
   ∴ p → r

4. **Silogismo Disjuntivo (SD):**
   p ∨ q
   ¬p
   ∴ q

5. **Simplificacao (SIMP):**
   p ∧ q
   ∴ p

6. **Conjuncao (CONJ):**
   p
   q
   ∴ p ∧ q

7. **Adicao (AD):**
   p
   ∴ p ∨ q

8. **Dilema Construtivo:**
   (p → q) ∧ (r → s)
   p ∨ r
   ∴ q ∨ s

9. **Dilema Destrutivo:**
   (p → q) ∧ (r → s)
   ¬q ∨ ¬s
   ∴ ¬p ∨ ¬r

### Formas Normais

**Forma normal conjuntiva (FNC):** Conjuncao de disjuncoes (clausulas). Exemplo: (p ∨ q) ∧ (¬p ∨ r) ∧ (q ∨ ¬r)

**Forma normal disjuntiva (FND):** Disjuncao de conjuncoes. Exemplo: (p ∧ q) ∨ (¬p ∧ r) ∨ (q ∧ ¬r)

Toda formula da logica proposicional pode ser convertida para FNC ou FND. A FNC e particularmente importante em raciocinio automatizado porque muitos algoritmos de prova (como resolucao) operam sobre clausulas.

### Satisfabilidade e Validade

Uma formula φ e **satisfativel** se existe pelo menos uma interpretacao na qual φ e verdadeira.

Uma formula φ e **insatisfativel** (contradicao) se e falsa em toda interpretacao.

Uma formula φ e **valida** (tautologia) se e verdadeira em toda interpretacao.

**Relação fundamental:** φ e valida se e somente se ¬φ e insatisfativel. Isso conecta prova (demonstrar que algo e tautologia) a refutacao (demonstrar que sua negacao e contraditoria).

---

## Logica de Predicados

### Sintaxe

A logica de predicados (ou logica de primeira ordem) estende a logica proposicional com:
- **Termos:** constantes (a, b, c...), variaveis (x, y, z...), funcoes (f(x), g(a,b)...)
- **Predicados:** P(x), Q(a,b), R(x,y,z)... representam propriedades e relacoes
- **Quantificadores:** Universal (∀) e Existencial (∃)

**Formula bem-formada:**
1. Se P e um predicado n-ario e t1...tn sao termos, entao P(t1...tn) e uma formula (formula atomica).
2. Se φ e ψ sao formulas, entao ¬φ, φ ∧ ψ, φ ∨ ψ, φ → ψ, φ ↔ ψ sao formulas.
3. Se φ e uma formula e x e uma variavel, entao ∀x φ e ∃x φ sao formulas.
4. Nada mais e formula.

### Semântica: Modelos e Interpretacao

A semântica da logica de predicados e definida em termos de **modelos** (ou estruturas). Um modelo M = ⟨D, I⟩ consiste em:
- **D:** Um dominio (conjunto nao-vazio de objetos)
- **I:** Uma funcao de interpretacao que mapeia:
  - Constantes para elementos de D
  - Predicados n-arios para relacoes n-arias em D
  - Funcoes n-arias para funcoes n-arias em D

A verdade de uma formula e definida recursivamente em relacao a um modelo M e uma atribuicao de variaveis s:

- M ⊨ P(t1...tn)[s] se ⟨I(t1)...I(tn)⟩ ∈ I(P)
- M ⊨ ¬φ[s] se M ⊭ φ[s]
- M ⊨ φ ∧ ψ[s] se M ⊨ φ[s] e M ⊨ ψ[s]
- M ⊨ ∀x φ[s] se para todo d ∈ D, M ⊨ φ[s(x/d)] (onde s(x/d) e s com x reatribuido a d)
- M ⊨ ∃x φ[s] se existe d ∈ D tal que M ⊨ φ[s(x/d)]

### Quantificadores em Profundidade

**Quantificador universal (∀):** ∀x P(x) significa "para todo x, P(x)" — verdadeiro se todos os elementos do dominio satisfazem P.

**Quantificador existencial (∃):** ∃x P(x) significa "existe x tal que P(x)" — verdadeiro se pelo menos um elemento do dominio satisfaz P.

**Negacao de quantificadores:**
- ¬∀x P(x) ≡ ∃x ¬P(x)
- ¬∃x P(x) ≡ ∀x ¬P(x)

**Escopo e variaveis ligadas/livres:**
- Em ∀x P(x), x esta **ligada** (bound) pelo quantificador
- Em P(x) sem quantificador, x esta **livre** (free)
- Uma formula sem variaveis livres e chamada **sentenca** (ou proposicao fechada)

### Silogismos na Logica de Predicados

O silogismo classico de Aristoteles pode ser formalizado em logica de predicados:

**Silogismo categorico (Barbara):**
- Premissa maior: Todo M e P → ∀x (M(x) → P(x))
- Premissa menor: Todo S e M → ∀x (S(x) → M(x))
- Conclusao: Todo S e P → ∀x (S(x) → P(x))

**Outros silogismos:**
- **Celarent:** Nenhum M e P, Todo S e M → Nenhum S e P
- **Darii:** Todo M e P, Algum S e M → Algum S e P
- **Ferio:** Nenhum M e P, Algum S e M → Algum S nao e P

### Validade vs Verdade

Na logica de predicados, e crucial distinguir:

**Validade:** Um argumento e **valido** se, e somente se, sempre que as premissas sao verdadeiras, a conclusao e necessariamente verdadeira. Validade e uma propriedade da **forma** do argumento, nao do conteudo.

**Verdade:** A verdade de uma premissa ou conclusao depende do **modelo** (da interpretacao). E uma propriedade **semântica** que varia conforme o mundo (ou modelo) considerado.

Exemplo:
- Premissa 1: ∀x (Gato(x) → Felino(x))
- Premissa 2: Gato(Mimi)
- Conclusao: Felino(Mimi)

O argumento e **valido** (a forma garante a conclusao). A **verdade** das premissas depende do mundo: se Mimi e de fato um gato e todo gato e felino, entao a conclusao e verdadeira. Mas a validade independe disso — o argumento permaneceria valido mesmo se Mimi fosse um cachorro (nesse caso, a premissa 2 seria falsa, mas o argumento continuaria formalmente valido).

**Solidez:** Um argumento e **solido** (*sound*) quando e valido **e** todas as suas premissas sao verdadeiras. Solidez combina validade formal com verdade factual.

### Teoria da Prova

Sistemas de deducao natural para logica de predicados estendem as regras da logica proposicional com regras para quantificadores:

**Introducao do universal:** Se Γ ⊢ P(c) para uma constante arbitraria c que nao aparece em Γ, entao Γ ⊢ ∀x P(x).

**Eliminacao do universal:** ∀x P(x) ⊢ P(t) para qualquer termo t.

**Introducao do existencial:** P(t) ⊢ ∃x P(x).

**Eliminacao do existencial:** Se ∃x P(x) e P(c) ⊢ Q, onde c e uma constante nova que nao aparece em Q nem em premissas nao-descartadas, entao ⊢ Q.

### Indecidibilidade e Incompletude

A logica de predicados de primeira ordem e:
- **Semidecidivel:** Nao existe algoritmo que, dada uma formula, sempre determine corretamente se ela e valida. Mas existe procedimento que, se a formula e valida, eventualmente confirma isso (teorema da completude de Godel).
- **Completa:** Todo argumento valido na logica de predicados possui uma prova formal (Godel, 1929).
- **Nao-compacta** no sentido mais amplo: existem conjuntos infinitos de formulas que sao insatisfativeis mas cujos subconjuntos finitos sao todos satisfativeis (o que motiva logicas nao-classicas).

---

## Falacias Formais

Falacias formais sao erros de raciocinio que ocorrem devido a uma **forma invalida** do argumento — a conclusao nao se segue logicamente das premissas, independentemente do conteudo.

### 1. NEGACAO DO ANTECEDENTE (*Denying the Antecedent*)

**Forma:** p → q; ¬p; ∴ ¬q

**Exemplo:** "Se chover, a rua ficara molhada. Nao choveu. Logo, a rua nao esta molhada." (A rua poderia estar molhada por outro motivo — caminhao-pipa, mangueira, etc.)

**Explicacao:** O condicional p → q estabelece que p e suficiente para q. Mas nao estabelece que ¬p seja suficiente para ¬q. q poderia ser verdadeiro por outras razoes.

### 2. AFIRMACAO DO CONSEQUENTE (*Affirming the Consequent*)

**Forma:** p → q; q; ∴ p

**Exemplo:** "Se ele e brasileiro, fala portugues. Ele fala portugues. Logo, ele e brasileiro." (Portugues tambem e falado em Portugal, Angola, Mocambique, etc.)

**Explicacao:** p → q estabelece p como suficiente para q, mas nao como necessario. q poderia ser verdadeiro mesmo sem p.

### 3. SILOGISMO DISJUNTIVO FALSO

**Forma:** p ∨ q; ¬p; ∴ q — e valida (esta e a forma correta).

O erro ocorre quando se usa **ou exclusivo** (xor) como se fosse **ou inclusivo**, ou vice-versa.

Exemplo: "O interruptor esta ligado ou desligado. Nao esta desligado. Logo, esta ligado." — Isto e correto para ou exclusivo. Mas em "Voce pode ficar ou sair" a inferencia pode ser enganosa.

### 4. FALACIA DA COMPOSICAO

**Forma:** Todo elemento de X tem propriedade P. Logo, X tem propriedade P.

**Exemplo:** "Cada atomo do muro e invisivel. Logo, o muro e invisivel."

**Explicacao:** Propriedades das partes nem sempre se transferem para o todo. A composicao e uma falacia formal quando se assume que o que vale para individuais vale para o coletivo.

### 5. FALACIA DA DIVISAO

**Forma:** X tem propriedade P. Logo, todo elemento de X tem propriedade P.

**Exemplo:** "O Brasil e um pais violento. Logo, todo brasileiro e violento."

**Explicacao:** Propriedades do todo nem sempre se aplicam as partes.

### 6. CIRCULO VICIOSO (*Petitio Principii*)

**Forma:** A conclusao aparece (disfarcada) entre as premissas.

**Exemplo:** "Deus existe, porque a Bíblia diz que Deus existe. E a Bíblia e a palavra de Deus, portanto inspirada e infalivel."

**Explicacao:** A justificativa pressupoe aquilo que se pretende provar. Nao ha progresso inferencial.

### 7. QUESTION BEGGING

Forma sutil de peticao de principio onde a premissa ja contem a conclusao, mas de forma menos obvia. Exemplo: "O aborto e assassinato, e assassinato e sempre errado, portanto aborto e errado." A premissa ja define aborto como assassinato, o que ja inclui a conclusao moral.

---

## Falacias Informais

Falacias informais sao erros de raciocinio que dependem do **conteudo** ou **contexto** do argumento, nao apenas de sua forma. Elas sao frequentes em debates cotidianos, discurso politico, propaganda e midia.

### 1. AD HOMINEM (Ataque a Pessoa)

**Definicao:** Atacar a pessoa que apresenta o argumento em vez de refutar o argumento em si.

**Tipos:**
- **Abusivo:** "Voce nao tem credibilidade porque e ignorante."
- **Circunstancial:** "Voce so defende isso porque trabalha na area."
- **Tu quoque:** "Voce tambem faz isso." (apontar hipocrisia)

Exemplo: "Nao devemos levar a serio as criticas de Chomsky ao capitalismo. Ele e um intelectual da elite academica." — Isto ignora o conteudo das criticas.

A falacia ad hominem NAO se aplica quando atacamos a credibilidade de uma testemunha em contexto juridico (isso e legitimo no processo adversarial). O erro e substituir a analise do argumento pelo ataque a pessoa.

### 2. HOMEM DE PALHA (*Straw Man*)

**Definicao:** Distorcer, exagerar ou simplificar o argumento do oponente para torna-lo mais facil de refutar, e entao atacar essa versao distorcida.

**Exemplo:** "Os defensores do aquecimento global dizem que devemos abandonar toda a civilizacao moderna e viver em cavernas." — Isto e uma caricatura da posicao ambientalista, que tipicamente defende transicao energetica, nao a eliminacao da tecnologia.

**Por que funciona:** E mais facil atacar uma posicao fraca do que a posicao real. O estrategema e desonesto porque nao enfrenta o melhor argumento do oponente.

### 3. APELO A AUTORIDADE (*Argument from Authority*)

**Definicao:** Usar a opiniao de uma autoridade para apoiar uma conclusao em um contexto onde essa autoridade nao e relevante ou competente.

**Forma correta vs falaciosa:**
- Correto: "O Premio Nobel de Fisica afirma que a relatividade geral esta bem testada." (Autoridade relevante)
- Falacioso: "Um famoso ator de cinema diz que este remedio funciona." (Autoridade irrelevante)

O apelo a autoridade nao e intrinsecamente falacioso — e razoavel confiar em especialistas em suas areas. A falacia ocorre quando:
- A autoridade nao e especialista no assunto
- Especialistas discordam entre si
- A autoridade tem conflito de interesses
- A autoridade nao e identificavel

### 4. LADEIRA ESCORREGADIA (*Slippery Slope*)

**Definicao:** Argumentar que uma acao levara inevitavelmente a uma sequencia de eventos que culminara em um resultado indesejavel, sem fornecer evidencia adequada da conexao causal.

**Exemplo:** "Se legalizarmos a maconha, logo as pessoas vao querer heroina, e em pouco tempo estaremos vivendo em um pais de dependentes quimicos."

**Quando e falacioso:** A falacia ocorre quando a corrente causal e fraca ou implausivel. Uma ladeira escorregadia nao e falaciosa se as conexoes causais sao bem estabelecidas por evidencia.

### 5. FALSA DICOTOMIA (*False Dilemma*)

**Definicao:** Apresentar apenas duas opcoes como se fossem as unicas possiveis, ignorando alternativas intermediarias ou complexas.

**Exemplo:** "Ou voce apoia esta guerra, ou e antipatriota." — Ignora a possibilidade de apoiar o pais mas se opor a guerra especifica.

**Estrutura:** p ∨ q; ¬p; ∴ q — mas a disjunçao e falsa porque ha outras alternativas r, s, t...

### 6. APELO A EMOCAO (*Appeal to Emotion*)

**Definicao:** Manipular as emocoes do interlocutor em vez de apresentar razoes logicas.

**Subtipos:**
- **Apelo a medo:** "Se nao aprovarmos esta lei, terroristas vao nos atacar."
- **Apelo a piedade:** "Como voce pode negar ajuda a esta crianca inocente?"
- **Apelo a orgulho/vaidade:** "Pessoas inteligentes como voce certamente concordam que..."
- **Apelo a novidade:** "E a tecnologia mais recente, entao deve ser melhor."

### 7. GENERALIZACAO APRESSADA (*Hasty Generalization*)

**Definicao:** Extrair uma conclusao geral a partir de evidencias insuficientes ou amostra nao representativa.

**Exemplo:** "Conheci tres pessoas de Sao Paulo e todas eram grossas. Logo, paulistas sao pessoas grossas."

**Risco:** E a base de muitos estereotipos e preconceitos. Um exemplo extremo e o racismo — generalizar caracteristicas negativas a todo um grupo a partir de casos isolados.

### 8. APELO A IGNORANCIA (*Argument from Ignorance*)

**Definicao:** Afirmar que algo e verdadeiro porque nao foi provado falso (ou vice-versa).

**Exemplo:** "Nao ha evidencia de que Deus nao existe. Logo, Deus existe."

**Contextos:** A falacia nao se aplica em contextos juridicos (presuncao de inocencia) ou cientificos onde a carga da prova segue regras especificas. Em geral, a ausencia de evidencia nao e evidencia de ausencia (embora, em alguns contextos, possa ser, como quando se esperaria encontrar evidencia se a hipotese fosse verdadeira).

### 9. CORRELAÇÃO NAO IMPLICA CAUSACAO (*Cum Hoc Ergo Propter Hoc*)

**Definicao:** Assumir que, porque dois eventos ocorrem juntos ou em sequencia, um causa o outro.

**Exemplo:** "O consumo de sorvete aumenta no verao, e tambem aumentam os afogamentos. Logo, sorvete causa afogamento."

**Problema:** Correlacao pode ser espuria — uma terceira variavel (calor) causa ambos. A correlacao e condicao necessaria mas nao suficiente para inferir causalidade.

### 10. CARREGAMENTO DO FARDAL (*Begging the Question* repaginada)

**Definicao informal:** Formular a pergunta de modo a ja assumir a conclusao.

**Exemplo:** "Por que o ovo azul e mais bonito?" — Ja pressupoe que o ovo azul e mais bonito.

### 11. FALACIA DO ATIRADOR TEXANO (*Texas Sharpshooter*)

**Definicao:** Selecionar arbitrariamente os dados ou o criterio de analise depois de ja conhecer os resultados, para fazer parecer que havia um padrao preditivo.

**Exemplo:** Um investidor faz muitas apostas diferentes, depois destaca apenas aquelas que deram certo e diz "minha estrategia funciona".

**Conexao:** Relacionada ao problema do *multiple comparisons* em estatistica e ao *data dredging* em ciencia de dados.

### 12. APELO A NATUREZA

**Definicao:** Argumentar que algo e bom porque e "natural" ou mau porque e "artificial".

**Exemplo:** "Este remedio e natural, entao e seguro." (Cicuta e natural e letal.)

**Explicacao:** O fato de algo ser natural ou artificial nao diz nada sobre seu valor moral ou eficacia. A falacia comete a "guilhotina de Hume": deriva "dever" de "ser".

### 13. AD POPULUM (*Bandwagon*)

**Definicao:** Afirmar que algo e verdadeiro (ou bom) simplesmente porque muitas pessoas acreditam ou fazem.

**Exemplo:** "Milhoes de pessoas usam este produto, entao ele deve ser bom."

**Problema:** A verdade nao e determinada por voto popular.

### 14. FALACIA DO JOGADOR (*Gambler's Fallacy*)

**Definicao:** Acreditar que eventos aleatorios independentes tem memoria — que resultados passados afetam a probabilidade de resultados futuros.

**Exemplo:** "A moeda deu cara 5 vezes seguidas, entao o proximo lancamento tem mais chance de dar coroa." (Na verdade, a probabilidade continua 50%.)

### 15. APELO A CONSEQUENCIA

**Definicao:** Argumentar que uma crenca e falsa (ou verdadeira) por causa das consequencias de acreditar nela.

**Exemplo:** "Se as pessoas acreditarem que nao ha livre-arbitrio, a sociedade entrara em colapso. Logo, ha livre-arbitrio." — A consequencia social nao determina a verdade da proposicao.

---

## Argumentacao -- Estrutura e Tipos de Raciocinio

### Estrutura Basica de um Argumento

Um argumento e um conjunto de **premissas** que supostamente apoiam uma **conclusao**. A estrutura minima:

1. **Premissas:** Proposicoes oferecidas como razoes ou evidencias.
2. **Conclusao:** Proposicao que se pretende estabelecer com base nas premissas.
3. **Inferencia:** A conexao logica entre premissas e conclusao.

**Exemplo:**
- Premissa 1: Todos os humanos sao mortais.
- Premissa 2: Socrates e humano.
- Conclusao: Socrates e mortal.

### Argumentos Dedutivos

Na **deducao**, a conclusao segue **necessariamente** das premissas. Se as premissas sao verdadeiras, a conclusao deve ser verdadeira. A deducao fornece **certeza condicional**: a conclusao e garantida se as premissas forem verdadeiras.

**Caracteristicas:**
- A conclusao esta contida (implicitamente) nas premissas
- O raciocinio e **ampliativo** em sentido logico, mas nao em sentido informacional
- O padrao de avaliacao e **validade** (a conclusao segue?) e **solidez** (premissas verdadeiras?)

**Formas dedutivas classicas:**
- Silogismo categorico (Todo A e B; C e A; ∴ C e B)
- Modus ponens (p → q; p; ∴ q)
- Modus tollens (p → q; ¬q; ∴ ¬p)
- Raciocinio matematico (provas teorema)

### Argumentos Indutivos

Na **inducao**, a conclusao e **provavel** (mas nao certa) dadas as premissas. A inducao generaliza a partir de observacoes particulares para conclusoes gerais.

**Caracteristicas:**
- A conclusao vai **alem** do conteudo das premissas
- O raciocinio e **ampliativo** — adiciona informacao
- O padrao de avaliacao e **forca** (quao provavel a conclusao e dadas as premissas)

**Formas indutivas:**
- **Generalizacao indutiva:** "Observei 100 cisnes e todos eram brancos. Logo, todos os cisnes sao brancos." (Cuidado: cisnes negros existem na Australia.)
- **Inducao por enumeracao:** Similar a generalizacao, mas baseada em contagem exaustiva
- **Inferencia causal:** "Toda vez que fumei, tive tosse. Logo, fumar causa tosse."
- **Inducao analogica:** "O medicamento X funcionou em ratos; humanos sao fisiologicamente similares; logo, funcionara em humanos."
- **Inducao estatistica:** "80% dos alunos aprovam este professor; Joao e aluno; logo, Joao provavelmente aprova o professor."

### Argumentos Abdutivos

A **abducao** (ou inferencia para a melhor explicacao) e o raciocinio que vai de um fenomeno observado para sua **melhor explicacao** causal.

**Estrutura:**
- Fenomeno surpreendente P e observado.
- Se Hipostese H fosse verdadeira, P seria explicado (seria esperado).
- Logo, ha razao para acreditar que H e verdadeira.

**Exemplo:** Voce ve grama molhada pela manha. A melhor explicacao e que choveu durante a noite (em vez de, digamos, que um vizinho regou o jardim as 4h da manha).

**Diferenca dos outros tipos:**
- Deducao: garante a conclusao (se premissas verdadeiras)
- Inducao: generaliza a partir de dados
- Abducao: propoe explicacao para dados

Charles Sanders Peirce (1839-1914) foi quem distinguiu formalmente os tres modos de inferencia. Para Peirce, a abducao e o unico tipo de raciocinio que introduz **novas ideias** — e o motor da descoberta cientifica.

### Tipos de Argumentacao

**Argumentacao monologica:** Apresentacao de argumentos por um unico orador (artigo, palestra, ensaio).

**Argumentacao dialogica:** Troca de argumentos entre dois ou mais participantes (debate, dialogo socratico, disputatio medieval).

**Argumentacao retorica:** Visa persuadir uma audiencia especifica, usando ethos (credibilidade), pathos (emocao) e logos (razao) — classificacao aristotelica.

**Argumentacao dialectica:** Busca a verdade atraves do confronto critico de posicoes opostas.

### Modelo de Toulmin (1958)

Stephen Toulmin propoe um modelo de argumentacao mais flexivel que o silogismo classico, com seis componentes:

1. **Pretensao** (*Claim*): A tese que se quer estabelecer.
2. **Dados** (*Data*): As evidencias que apoiam a pretensao.
3. **Garantia** (*Warrant*): A regra ou principio que conecta os dados a pretensao.
4. **Apoio** (*Backing*): A fundamentacao da garantia (autoridade, lei, teoria).
5. **Qualificador modal** (*Modal Qualifier*): Palavras que indicam forca — "provavelmente", "necessariamente", "possivelmente".
6. **Condicoes de refutacao** (*Rebuttal*): Circunstancias em que a pretensao nao se sustenta.

**Exemplo:** "Joao deve ter nascido no Brasil (pretensao), porque ele fala portugues como nativo (dados). Sabemos que quem nasce no Brasil geralmente fala portugues (garantia), baseado em dados censitarios e leis de nacionalidade (apoio). Certamente (qualificador), a menos que ele tenha aprendido portugues de outra forma ou tenha dupla nacionalidade (refutacao)."

---

## Logicas Nao-Classicas

As logicas nao-classicas relaxam ou modificam principios da logica classica para lidar com fenomenos que ela nao captura adequadamente.

### 1. Logica Modal

A logica modal estende a logica classica com operadores modais:

- **□** (necessidade): □P significa "e necessario que P"
- **◇** (possibilidade): ◇P significa "e possivel que P"

Os operadores sao interdefiniveis: □P ≡ ¬◇¬P; ◇P ≡ ¬□¬P.

**Sistemas axiomáticos:**

- **Sistema K (Kripke):** O sistema basico. Axioma: □(P → Q) → (□P → □Q).
- **Sistema T:** K + T (□P → P).
- **Sistema S4:** T + 4 (□P → □□P).
- **Sistema S5:** S4 + B (P → □◇P) — todos os mundos sao mutuamente acessiveis.

**Semântica de mundos possiveis (Kripke, 1963):**
Um modelo M = ⟨W, R, V⟩ onde:
- W: conjunto de mundos possiveis
- R ⊆ W × W: relacao de acessibilidade
- V: W → (prop → {V,F}): funcao de valoração

M, w ⊨ □P se para todo v tal que wRv, M, v ⊨ P.
M, w ⊨ ◇P se existe v tal que wRv e M, v ⊨ P.

### 2. Logica Epistemica

A logica epistemica formaliza raciocinio sobre **conhecimento e crenca**.

**Operador de conhecimento:** K_aP significa "a sabe que P".
**Operador de crenca:** B_aP significa "a acredita que P".

**Axiomas caracteristicos:**
- K_a(P → Q) → (K_aP → K_aQ) — distribuicao
- K_aP → P — conhecimento implica verdade
- K_aP → K_aK_aP — introspeção positiva (conhecimento do conhecimento)
- ¬K_aP → K_a¬K_aP — introspecao negativa

**Problemas classicos:**
- **Problema da onisciencia logica:** Agentes epistemicos ideais conhecem todas as consequencias logicas do que conhecem — irrealista para agentes reais.
- **Problema do saber-que vs saber-como:** K_aP captura "saber que" mas nao "saber como" (*know-how*).
- **Raciocinio sobre conhecimento multiplo:** "Eu sei que voce sabe que eu sei..." — crencas comuns e conhecimento comum (*common knowledge*).

**Conexões com IA:**
- Logica epistemica e usada em protocolos de comunicacao entre agentes (sistemas multiagente)
- Modelagem de crenca e conhecimento em agentes racionais (BDI: Belief-Desire-Intention)
- Raciocinio sobre conhecimento em jogos (logica epistemic game theory)

### 3. Logica Deontica

A logica deontica formaliza raciocinio sobre **obrigacoes, permissoes e proibicoes**.

**Operadores:**
- OB(P): "e obrigatorio que P"
- PE(P): "e permitido que P"
- PR(P): "e proibido que P"

Relações: PR(P) ≡ OB(¬P); PE(P) ≡ ¬OB(¬P).

**Sistema padrao de logica deontica (SDL):**
- OB(P → Q) → (OB(P) → OB(Q))
- OB(P) → ¬OB(¬P) — consistencia deontica (nao se pode dever o impossivel)
- OB(P) ∨ PE(P) — completude deontica

**Paradoxos da logica deontica:**
- **Paradoxo de Ross:** OB(P) → OB(P ∨ Q). "Devo enviar a carta" implica "devo enviar a carta ou queima-la". Formalmente correto, mas contra-intuitivo.
- **Paradoxo de Chisholm:** Obrigacoes contrafatuais — "deve-se fazer X, mas se nao fizer X, deve-se fazer Y" e dificil de formalizar consistentemente.
- **Paradoxo do bom samaritano:** OB(P) ∧ (P → Q) → OB(Q) pode gerar obrigacoes absurdas.

**Aplicações em IA:** Codificacao de principios eticos em agentes autonomos, seguranca de AGI, governanca algoritmica.

### 4. Logica Temporal

A logica temporal formaliza raciocinio sobre tempo e ordem temporal.

**Operadores temporais:**

- **G** (sempre futuro): GP significa "sempre (a partir de agora), P"
- **F** (eventualmente futuro): FP significa "eventualmente no futuro, P"
- **H** (sempre passado): HP significa "sempre no passado, P"
- **O** (eventualmente passado): OP significa "em algum momento no passado, P"

**LTL (Linear Temporal Logic):** Opera sobre uma unica linha temporal linear.
- **X** (next): XP significa "no proximo instante, P"
- **U** (until): P U Q significa "P ate que Q"

**CTL (Computation Tree Logic):** Opera sobre arvores de tempo ramificado, permitindo raciocinio sobre possibilidades futuras alternativas.

**Aplicações:** Verificacao formal de hardware e software (*model checking*); protocolos de sistemas distribuidos; especificacao de sistemas reativos; logica temporal em sistemas multiagente.

### 5. Logica Paraconsistente

Logicas paraconsistentes permitem raciocinar com **contradicoes** sem que o sistema se torne trivial (explosivo). Na logica classica, de uma contradicao (P ∧ ¬P) segue-se qualquer conclusao — o **principio da explosao** (ex contradictione quodlibet). Logicas paraconsistentes rejeitam este principio.

**Motivação:** Situacoes reais frequentemente envolvem informacao inconsistente. Bases de dados podem conter contradicoes. Teorias cientificas podem ser inconsistentes mas ainda uteis. Conjuntos fuzzy de regras podem conflitar.

**Logica paraconsistente dialetica (DL):** Inspirada na logica de Hegel e Marx, ve a contradicao como produtiva.

**Sistemas notaveis:**
- Logica de da Costa (**Cn**): Família de logicas paraconsistentes hierarquicas
- **Logica de relevancia:** Exige conexao relevante entre antecedente e consequente para inferencia
- **Logica nao-monotonica:** Novas informacoes podem retirar conclusoes anteriores

**Aplicações:** IA juridica (sistemas legais sao inerentemente inconsistentes); gestao de conflitos em bases de conhecimento; raciocinio com crencas contraditorias.

### 6. Logica Fuzzy

Proposta por Lotfi Zadeh (1965), a logica fuzzy generaliza a logica booleana permitindo valores de verdade **continuos** no intervalo [0,1].

**Diferencas da logica classica:**
- Valor de verdade: nao e binario (V/F), mas **grau de pertinencia** (ex.: "0.8 verdadeiro")
- Conectivos sao generalizados para operacoes em [0,1]

**Operacoes fuzzy tipicas:**
- ¬x = 1 - x (negacao)
- x ∧ y = min(x, y) (conjuncao)
- x ∨ y = max(x, y) (disjuncao)
- x → y = min(1, 1 - x + y) (implicacao de Lukasiewicz)

**Aplicações:**
- Controle fuzzy (eletrodomesticos, automoveis, processos industriais)
- Sistemas especialistas fuzzy
- Tomada de decisao com incerteza
- Processamento de linguagem natural (categorias difusas)

### 7. Logica Nao-Monotonica

Na logica classica, se Γ ⊢ P, entao Γ ∪ {Q} ⊢ P para qualquer Q — **monotonicidade**: novas informacoes nunca invalidam conclusoes anteriores. A logica nao-monotonica relaxa este principio.

**Exemplo classico:** "Passaros voam." Sabendo que Tweety e um passaro, conclui-se que Tweety voa. Se descobre-se que Tweety e um pinguim, retira-se a conclusao. Isto e nao-monotonico.

**Sistemas:**
- **Default logic (Reiter, 1980):** Regras default — "se P e consistente, entao normalmente Q".
- **Circunscricao (McCarthy, 1980):** Minimiza excecoes — assume que objetos normais sao a regra.
- **Logica autoepistemica (Moore, 1985):** Raciocinio sobre o proprio conhecimento e ignorancia.
- **Programacao em logica com negacao como falha:** Prolog — "assume-se ¬p se nao se pode provar p".

**Importancia para IA:** Raciocinio de senso comum, planejamento, interpretacao de linguagem natural — todos exigem inferencias que podem ser retiradas com nova informacao.

---

## Conexoes com Inteligencia Artificial

### Raciocinio Automatizado

O raciocinio automatizado e o uso de computadores para realizar inferencias logicas. Divide-se em:

**Prova automatica de teoremas (ATP):** Algoritmos que buscam provas de formulas em sistemas logicos.
- **Resolucao (Robinson, 1965):** Regra de inferencia unica que, combinada com unificacao, e completa para logica de primeira ordem.
- **Tableaux semânticos:** Metodo de prova por refutacao — constroi arvore de possibilidades, fecha ramos contraditorios.
- **Deducao natural e calculo de sequentes:** Sistemas que simulam raciocinio humano.
- **SAT solving:** Satisfabilidade de formulas proposicionais — base das tecnologias modernas de verificacao.

**ATP em logica de predicados:**
- O problema da **parada** para ATP: a logica de predicados e indecidivel, mas semidecidivel — algoritmos de prova podem nunca terminar para formulas nao-validas.
- **Prazo e heurísticas:** ATPs eficientes usam heuristicas para guiar a busca (ex.: orientacao a objetivos, *set of support*, ponderacao de clausulas).
- ATPs modernos como Vampire, E, Z3 e Lean podem provar teoremas complexos em segundos.

### Sistemas Especialistas

Sistemas especialistas sao programas de IA que usam **regras logicas** para capturar conhecimento especializado em um dominio restrito.

**Arquitetura:**
- **Base de conhecimento:** Fatos + Regras (SE-ENTAO)
- **Motor de inferencia:** Encadeamento para frente (*forward chaining*) ou para tras (*backward chaining*)
- **Interface de usuario:** Entrada de perguntas, saida de diagnosticos e justificativas

**Exemplos classicos:**
- **MYCIN (1976):** Diagnostico de infeccoes bacterianas — cerca de 600 regras; desempenho superior a medicos juniores.
- **DENDRAL (1965):** Identificacao de moleculas organicas a partir de espectrometria de massa.
- **PROSPECTOR (1976):** Prospeccao mineral — descobriu um deposito de molibdenio.
- **XCON/R1 (1980):** Configuracao de sistemas VAX da DEC — economizou US$ 40 milhoes/ano.

**Limitações:**
- Aquisição de conhecimento e gargalo (knowledge bottleneck)
- Dificuldade com incerteza e excecoes
- Falta de aprendizado autonomo
- Escalabilidade limitada em dominios complexos

### Logica em Programacao

**Prolog (1972):** Linguagem de programacao logica fundada na logica de predicados de primeira ordem, com resolucao SLD (Selective Linear Definite) e negacao como falha.

**Programacao em logica indutiva (ILP):** Sintese de programas logicos a partir de exemplos — learning by doing, no sentido de aprender regras logicas de dados.

**Logica de descricao (Description Logics):** Família de linguagens de representacao de conhecimento, base de ontologias OWL para Web Semantica. Exemplo: o raciocinador Pellet ou HermiT pode inferir classificacao automatica de conceitos.

### Logica em LLMs

Os Grandes Modelos de Linguagem (LLMs) como GPT-4, Claude e LLaMA representam um paradigma **diferente** da logica classica para raciocinio:

**Como LLMs "raciocinam":**
- Nao ha inferencia logica explicita (no sentido de modus ponens ou resolucao)
- O raciocinio emerge de padroes estatisticos aprendidos em grandes corpus textuais
- A "inferencia" e um processo de previsao do proximo token condicionada ao contexto

**Forcas dos LLMs em raciocinio:**
- Raciocinio analogico e por similaridade
- Recuperacao e combinacao de conhecimento factual
- Traducao entre linguagem natural e formal
- Generalizacao a partir de exemplos (in-context learning)

**Fraquezas dos LLMs em raciocinio:**
- Inconsistencia logica: respostas contraditorias para perguntas similares
- Falta de garantia de validade: nao ha mecanismo para assegurar que a conclusao segue das premissas
- Dificuldade com raciocinio multi-passos complexos (melhorada com chain-of-thought)
- Sensibilidade a formulacao: pequenas mudancas na pergunta alteram a resposta
- Alucinacoes: inferencia de "fatos" que nao estao nos dados de treino

**Abordagens hibridas atuais:**
- **Neuro-simbólica:** Combinar LLMs com motores de inferencia logicos (ex.: LLM gera formalizacao logica, motor faz inferencia, LLM traduz de volta)
- **Chain-of-thought:** Prompting que estimula o modelo a gerar passos intermediarios de raciocinio (Wei et al., 2022)
- **Tool use:** LLMs que chamam provadores automaticos (ex.: Lean, Z3) para inquirir inferencias
- **Raciocinio simbolico-guia:** Usar logica formal como esqueleto que o LLM preenche com conteudo

### O Debate: Simbolico vs Conexionista

O debate entre IA simbolica (logica) e IA conexionista (redes neurais) e uma das tensoes fundacionais da inteligencia artificial:

**IA Simbolica:**
- Representacao explicita de conhecimento em linguagens logicas
- Inferencia formal com garantias de correcao
- Interpretabilidade e explicabilidade inerentes
- Dificuldade com aprendizagem autonoma e incerteza
- Limitada a dominios bem-definidos e completos

**IA Conexionista:**
- Representacao distribuida em vetores numericos
- Aprendizagem a partir de dados (exemplos)
- Robustez a ruido e generalizacao
- Dificuldade com raciocinio logico, causalidade e explicabilidade
- "Caixa preta": resultados sem justificativa formal

**Síntese:** A tendencia atual e a integracao — sistemas neuro-simbolicos que combinam o melhor dos dois mundos: aprendizado estatistico com garantias logicas.

---

## Glossario

**Abducao:** Tipo de inferencia que vai de um fenomeno observado para sua melhor explicacao causal.

**Argumento:** Conjunto de premissas que supostamente apoiam uma conclusao.

**Atomo proposicional:** Unidade minima de significado na logica proposicional (variavel p, q, r...).

**Axioma:** Proposicao assumida como verdadeira sem prova, ponto de partida de um sistema formal.

**Clausula:** Disjuncao de literais (ex.: p ∨ ¬q ∨ r). Forma basica da resolucao.

**Completude:** Propriedade de um sistema formal em que toda formula valida tem uma prova.

**Condicional:** Conectivo logico "se...entao" (→).

**Conectivo logico:** Simbolo que conecta formulas (¬, ∧, ∨, →, ↔).

**Consequencia logica:** Relacao entre premissas e conclusao: a conclusao e consequencia logica das premissas se nao e possivel que as premissas sejam verdadeiras e a conclusao falsa.

**Consistencia:** Propriedade de um conjunto de formulas onde nenhuma contradicao pode ser derivada.

**Contradicao:** Formula que e falsa em todas as interpretacoes (p ∧ ¬p).

**Deducao:** Tipo de inferencia onde a conclusao segue necessariamente das premissas.

**Disjuncao:** Conectivo logico "ou" (∨).

**Equivalencia logica:** Duas formulas sao logicamente equivalentes se tem o mesmo valor de verdade em toda interpretacao.

**Falacia:** Erro de raciocinio que torna um argumento invalido ou fraco. Pode ser formal (erro na forma) ou informal (erro no conteudo/contexto).

**Formula bem-formada (fbf):** Expressao sintaticamente correta em uma linguagem logica.

**Indecidibilidade:** Propriedade de um problema para o qual nao existe algoritmo que sempre responda sim/nao corretamente.

**Inducao:** Tipo de inferencia que generaliza de observacoes particulares para conclusoes gerais.

**Inferencia:** Processo de derivar conclusoes a partir de premissas.

**Interpretacao:** Atribuicao de valores de verdade as formulas de uma linguagem logica.

**Literal:** Formula atomica (p) ou sua negacao (¬p).

**Modelo:** Estrutura matematica (dominio + interpretacao) na qual formulas logicas sao avaliadas como verdadeiras ou falsas.

**Modus ponens:** Regra de inferencia: p → q; p; ∴ q.

**Modus tollens:** Regra de inferencia: p → q; ¬q; ∴ ¬p.

**Negacao:** Conectivo logico "nao" (¬).

**Premissa:** Proposicao oferecida como razao ou evidencia em um argumento.

**Quantificador:** Operador que especifica a quantidade de elementos do dominio que satisfazem uma propriedade (∀ para todos, ∃ para algum).

**Resolucao:** Regra de inferencia unica que e completa para logica de predicados quando combinada com unificacao.

**Satisfabilidade:** Propriedade de uma formula: existe pelo menos uma interpretacao na qual ela e verdadeira.

**Semântica:** Estudo da relacao entre simbolos e seus significados (valores de verdade) em um modelo.

**Silogismo:** Argumento dedutivo composto por duas premissas e uma conclusao, tipicamente envolvendo quantificacao categorica.

**Sintaxe:** Regras para construcao de formulas e provas em um sistema formal.

**Solidez (*soundness*):** Propriedade de um argumento que e valido E tem premissas verdadeiras.

**Tabela-verdade:** Representacao tabular de todos os valores de verdade de uma formula para todas as interpretacoes possiveis.

**Tautologia:** Formula verdadeira em todas as interpretacoes (verdade logica).

**Teorema:** Formula que pode ser provada em um sistema formal a partir dos axiomas.

**Teoria da prova:** Estudo das provas formais como objetos matematicos.

**Teoria de modelos:** Estudo da relacao entre linguagens formais e suas interpretacoes em estruturas matematicas.

**Terceiro excluido:** Principio logico: p ∨ ¬p (toda proposicao e verdadeira ou falsa).

**Unificacao:** Algoritmo que encontra substituicoes de variaveis que tornam duas formulas identicas.

**Validade:** Propriedade de um argumento: se as premissas sao verdadeiras, a conclusao deve ser verdadeira.

---

## Exercicios de Raciocinio Logico

### Logica Proposicional

1. **Tabelas-verdade:** Construa a tabela-verdade para: (p → q) ∧ (q → r) → (p → r).

2. **Equivalencias:** Mostre que p → (q → r) ≡ (p ∧ q) → r, usando tabelas-verdade e usando as leis de equivalencia.

3. **Circuitos logicos:** Um sistema de alarme dispara se (a) a porta estiver aberta e o sensor de movimento ativado, OU (b) a janela estiver aberta e o sensor de vibracao ativado. Expressar como formula proposicional.

4. **Problema dos guardioes:** Duas portas, dois guardioes — um sempre mente, um sempre diz a verdade. Uma porta leva a liberdade, outra a morte. Que pergunta fazer para descobrir a porta correta?

### Falacias

5. **Identifique a falacia em cada argumento:**
   - "Se voce e contra a pena de morte, voce apoia assassinos."
   - "Meu medico diz que este remedio e eficaz. E medico, entao confio."
   - "Nao podemos legalizar a eutanasia porque isso levara a eugenia."

6. **Reconstrucao de argumentos:** Reconstrua o argumento abaixo em forma logica, identificando premissas e conclusao, e avalie se e valido/solido:

   "Se o aquecimento global for causado por atividades humanas, entao reduzir emissoes de carbono e uma prioridade. O aquecimento global e causado por atividades humanas. Logo, reduzir emissoes de carbono e uma prioridade."

### Logica de Predicados

7. **Formalizacao:** Formalize em logica de predicados:
   - "Todo filosofo e mortal."
   - "Alguns gatos sao pretos."
   - "Nenhum numero par e primo maior que 2."
   - "Toda crianca ama alguem."

8. **Validade:** Verifique se este argumento e valido (formalize e tente provar):
   - Todos os mamiferos sao animais.
   - Todos os caes sao mamiferos.
   - Logo, todos os caes sao animais.

### Raciocinio Dedutivo vs Indutivo

9. **Classifique como dedutivo ou indutivo:**
   - "Todas as bolas nesta urna sao vermelhas. Esta bola veio da urna. Logo, e vermelha."
   - "90% das bolas nesta urna sao vermelhas. Esta bola veio da urna. Logo, provavelmente e vermelha."
   - "O sol nasceu todos os dias ate hoje. Logo, o sol nascera amanha."

---

## Referencias

- Aristoteles. *Organon* (c. 350 a.C.).
- Boole, G. (1847). *The Mathematical Analysis of Logic*.
- Copi, I. & Cohen, C. (2018). *Introduction to Logic* (15th ed.). Routledge.
- Frege, G. (1879). *Begriffsschrift*.
- Godel, K. (1931). "Sobre Proposicoes Formalmente Indecidiveis dos Principia Mathematica e Sistemas Relacionados".
- Hurley, P. (2014). *A Concise Introduction to Logic* (12th ed.). Cengage.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Kripke, S. (1963). "Semantical Considerations on Modal Logic".
- Peirce, C. S. (1903). *Lectures on Pragmatism*.
- Priest, G. (2008). *An Introduction to Non-Classical Logic* (2nd ed.). Cambridge University Press.
- Quine, W. V. O. (1950). *Methods of Logic*.
- Russell, B. & Whitehead, A. N. (1910). *Principia Mathematica*.
- Tarski, A. (1933). *The Concept of Truth in Formalized Languages*.
- Toulmin, S. (1958). *The Uses of Argument*. Cambridge University Press.
- Turing, A. (1936). "On Computable Numbers, with an Application to the Entscheidungsproblem".
- Walton, D. (2008). *Informal Logic: A Pragmatic Approach* (2nd ed.). Cambridge University Press.
- Wei, J. et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models". *NeurIPS*.
- Zadeh, L. (1965). "Fuzzy Sets". *Information and Control*, 8(3), 338-353.

---

*Logica e a anatomia do pensamento.*
