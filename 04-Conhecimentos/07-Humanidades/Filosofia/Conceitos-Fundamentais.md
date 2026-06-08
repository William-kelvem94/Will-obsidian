---
title: "Conceitos Fundamentais de Filosofia"
area: "Filosofia"
related: ["Epistemologia", "Lógica", "Metafísica", "Filosofia da Ciência"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, filosofia, metafisica, epistemologia, causalidade, livre-arbitrio]
updated: 2026-05-16
---

# Conceitos Fundamentais de Filosofia

A filosofia (do grego *philosophia*, "amor à sabedoria") é a investigação racional das questões fundamentais sobre existência, conhecimento, valores, razão, mente e linguagem. Diferentemente das ciências empíricas, a filosofia opera através de argumentação lógica, análise conceitual e reflexão crítica, buscando fundamentos e pressupostos que outras disciplinas tomam como dados.

## Metafísica: O Estudo da Realidade

A metafísica (do grego *ta meta ta physica*, "o que vem depois da física") investiga a natureza fundamental da realidade, incluindo questões sobre existência, objetos, propriedades, espaço, tempo, causalidade e possibilidade.

### Ontologia

A ontologia é o estudo do **ser** enquanto ser — investiga quais tipos de coisas existem fundamentalmente.

#### Realismo vs Antirrealismo

- **Realismo metafísico:** O mundo existe independentemente de nossa percepção ou linguagem. Há um fato objetivo sobre como o mundo é.
- **Antirrealismo (idealismo):** O mundo depende, em algum sentido, de nossa mente ou linguagem.

Platão é o realista paradigmático — as Formas (Ideias) existem em um reino separado, eterno e imutável. George Berkeley (1710, *Tratado sobre os Princípios do Conhecimento Humano*) é o idealista radical — *esse est percipi* (ser é ser percebido). Para Berkeley, objetos materiais são coleções de ideias percebidas por mentes, incluindo a mente divina.

#### O Debate sobre Universais

- **Realismo:** Universais (como "vermelhidão" ou "humanidade") existem independentemente das coisas particulares.
- **Nominalismo:** Apenas particulares existem; universais são apenas nomes que agrupamos heuristicamente.
- **Conceitualismo:** Universais existem, mas apenas como conceitos mentais.

#### Estrutura da Realidade

| Posição | Tese | Proponente Principal |
|---------|------|----------------------|
| Monismo | Apenas um tipo de substância existe | Parmênides, Espinosa |
| Dualismo | Dois tipos de substância (mente e matéria) | Descartes |
| Pluralismo | Múltiplos tipos de substância | Aristóteles, Leibniz |
| Atomismo lógico | O mundo é composto por fatos atômicos | Russell, Wittgenstein (*Tractatus*) |

#### Mereologia (Teoria das Partes e do Todo)

A mereologia estuda a relação entre partes e todos:

- **Composição restrita:** Nem toda coleção de objetos forma um objeto (ex.: o nariz de Sócrates + Plutão ≠ um objeto).
- **Composição irrestrita (universalismo mereológico):** Qualquer soma de entidades forma um objeto.
- **Niilismo mereológico:** Apenas átomos (partes sem partes) existem — objetos compostos são ilusões.

### Epistemologia: O Estudo do Conhecimento

A epistemologia investiga a natureza, fontes e limites do conhecimento.

#### O Problema de Gettier

Até 1963, a definição padrão de conhecimento era **crença verdadeira justificada** (Platão, *Teeteto*). Edmund Gettier (1963, "Is Justified True Belief Knowledge?") mostrou contraexemplos:

> Você vê um relógio de parede que sempre funcionou perfeitamente. Baseado nisso, você forma a crença "são 15:30". De fato, são 15:30 — mas o relógio quebrou ontem e está parado exatamente em 15:30 por coincidência. Sua crença é verdadeira e justificada, mas não é conhecimento.

Gettier mostrou que a justificação pode ser "acidental" em relação à verdade. As respostas ao problema de Gettier incluem:

1. **Internalismo:** A justificação deve ser acessível à consciência do sujeito (Chisholm).
2. **Externalismo:** A justificação pode envolver fatores externos ao sujeito, como confiabilidade causal (Goldman, 1967 — teoria causal do conhecimento).
3. **Confiabilismo:** Uma crença é conhecimento se é produzida por um processo cognitivo confiável (Goldman, 1976).
4. **Virtude epistemológica:** Conhecimento é crença verdadeira produzida por uma faculdade intelectual virtuosa (Sosa, Zagzebski).

#### Fontes do Conhecimento

| Fonte | Descrição | Céticos |
|-------|-----------|---------|
| Percepção sensorial | Conhecimento através dos sentidos | Descartes (sonho, demônio maligno) |
| Razão | Conhecimento a priori (dedução, lógica) | Hume (ceticismo sobre causalidade) |
| Introspecção | Conhecimento dos próprios estados mentais | Wittgenstein (crítica da linguagem privada) |
| Testemunho | Conhecimento através da fala de outros | Reid (confiança no testemunho) |
| Memória | Conhecimento preservado do passado | Locke (identidade pessoal e memória) |

#### O Problema do Critério (Ciclo de Agripa)

O trilema de Agripa (cético grego, séc. I d.C.) mostra que toda justificação termina em uma de três opções:
1. **Regresso infinito:** Cada crença requer outra crença, ad infinitum.
2. **Circularidade:** A cadeia eventualmente retorna a si mesma.
3. **Fundacionalismo dogmático:** A cadeia termina em uma crença básica não-justificada.

O **fundacionalismo** (Aristóteles, Descartes) aceita a opção 3: há crenças básicas auto-evidentes. O **coerentismo** (Hegel, Quine) aceita a opção 2: a justificação é uma questão de coerência mútua entre crenças. O **ceticismo** aceita o regresso infinito como prova de que não há conhecimento.

## Causalidade

A causalidade é uma das noções mais fundamentais e controversas da metafísica.

### Hume e a Regularidade

David Hume (1748, *Investigação sobre o Entendimento Humano*) argumentou que não percebemos **conexões necessárias** entre causa e efeito — percebemos apenas **conjunções constantes**:

1. A causa (A) precede o efeito (B) no tempo.
2. A causa (A) é contígua ao efeito (B) no espaço.
3. Sempre que A ocorre, B ocorre (conjunção constante).

Para Hume, nossa crença na causalidade é um **hábito da imaginação**, não uma percepção racional da realidade. A necessidade causal está na mente, não no mundo.

```python
# Ilustração: Causalidade como correlação (Hume)
import numpy as np
from scipy.stats import pearsonr

# Dados de "causa" e "efeito"
causa = np.array([1, 2, 3, 4, 5])
efeito = np.array([2, 4, 6, 8, 10])  # perfeitamente correlacionado

r, p = pearsonr(causa, efeito)
print(f"Correlação: {r:.2f}")  # 1.00

# Hume diria: isso é TUDO que observamos.
# A "conexão necessária" é uma projeção mental.
```

### A Análise Contrafactual de Causação

David Lewis (1973, "Causation") propôs que a causação deve ser analisada em termos de **contrafactuais** — o que aconteceria se a causa não tivesse ocorrido:

> "C causa E" significa: se C não tivesse ocorrido, E não teria ocorrido.

Formalmente: **C → E** é verdade se no mundo possível mais próximo onde ~C, temos ~E.

### A Teoria de Processos de Salmon

Wesley Salmon (1984) propôs uma teoria física de causalidade: uma causa transmite **marca** ou **quantidade conservada** (momento, energia, carga) ao efeito. Isto conecta causalidade às leis da física, evitando o ceticismo humeano.

### Causalidade Descendente vs Ascendente

Na [[04-Conhecimentos/07-Humanidades/Filosofia/Filosofia-da-Mente|filosofia da mente]]:

- **Causalidade ascendente:** Micro-entidades (átomos, neurônios) causam macro-fenômenos (consciência).
- **Causalidade descendente:** Macro-fenômenos (consciência, intenções) causam mudanças micro (ativação neural).

O problema: causalidade descendente parece violar a clausura causal do nível micro. Se eventos macro realmente causam eventos micro, então o que as leis da física micro descrevem é incompleto.

## Livre Arbítrio

O problema do livre arbítrio investiga se agentes racionais têm controle genuíno sobre suas escolhas e ações.

### Determinismo

**Determinismo causal:** Todo evento tem uma causa suficiente anterior. Dado o estado do universo em t₀ e as leis da natureza, o estado em t₁ está fixado.

- **Determinismo nomológico:** Leis da natureza são deterministicas (mecânica clássica).
- **Determinismo lógico:** Proposições sobre o futuro já são verdadeiras ou falsas (Aristóteles, *De Interpretatione* 9).
- **Determinismo teológico:** Deus já sabe o que você fará (predestinação calvinista).

### Compatibilismo

**Tese:** Livre arbítrio é compatível com determinismo.

- **Hume (1748):** Liberdade não é ausência de causalidade, mas ausência de **coerção**. A ação é livre se é causada *pelas próprias crenças e desejos do agente*, não por força externa.
- **Harry Frankfurt (1969):** O que importa é a **estrutura hierárquica** da vontade. Uma ação é livre se o agente tem o desejo de *primeira ordem* (fazer X) consistente com seu desejo de *segunda ordem* (querer querer fazer X). O viciado que quer parar, mas não consegue, não age livremente.
- **Dennett (1984, *Elbow Room*):** A evolução nos deu a capacidade de **evitar** futuros indesejados — isto é livre arbítrio suficiente.

### Incompatibilismo

**Tese:** Determinismo e livre arbítrio são mutuamente exclusivos.

#### Determinismo Radical (Duro)

Se o determinismo é verdadeiro, ninguém tem livre arbítrio. A punição e a responsabilidade moral seriam injustificadas.

- **Barão d'Holbach (1770, *Sistema da Natureza*):** "O homem é uma máquina" — todas as escolhas são determinadas por causas físicas.
- **Galton Strawson (1994):** O argumento básico: para ser moralmente responsável por uma ação, você teria que ser responsável por *como você é* (seu caráter). Mas você não pode criar seu caráter a partir do zero — isso exigiria uma escolha prévia, e assim infinitamente.

#### Libertarianismo (Indeterminismo)

**Tese:** Temos livre arbítrio, portanto o determinismo é falso. A mente tem o poder de iniciar novas cadeias causais.

- **Agente causal:** O agente (como substância, não como evento) causa a ação. O livre arbítrio é uma propriedade irredutível do sujeito (Reid, Chisholm, O'Connor).
- **Indeterminismo quântico:** Eventos quânticos são genuinamente indeterminados. Se o cérebro amplifica flutuações quânticas, há espaço para liberdade (Eccles, Penrose).

**Problema do libertarianismo:** Se a ação é indeterminada, como ela é *sua*? Se não há causa suficiente, a ação é apenas um acaso — e acaso não é liberdade. Este é o problema do **argumento do acaso** (*chance argument*).

### Tabela Comparativa

| Posição | Determinismo? | Livre Arbítrio? | Responsabilidade Moral? |
|---------|---------------|-----------------|------------------------|
| Compatibilismo clássico | Sim | Sim | Sim |
| Determinismo radical | Sim | Não | Não |
| Libertarianismo | Não | Sim | Sim |
| Incompatibilismo brando (pessimista) | Sim | Não, infelizmente | Sim (por razões práticas) |
| Ceticismo do livre arbítrio (Pereboom) | Sim ou Não | Não em nenhum caso | Não |

## Identidade ao Longo do Tempo

O problema da identidade pessoal: o que faz de você, aos 40 anos, a mesma pessoa que você era aos 5?

### O Navio de Teseu

Plutarco (*Vidas Paralelas*, séc. I d.C.) narra o paradoxo: o navio de Teseu é preservado em Atenas, e cada tábua podre é substituída. Quando todas as tábuas forem substituídas, ainda é o mesmo navio? E se as tábuas originais forem remontadas em outro lugar — qual é o navio verdadeiro?

**Respostas possíveis:**
1. **Critério material:** É o mesmo navio se a matéria for a mesma (Hobbes).
2. **Critério formal/estrutural:** É o mesmo navio se a forma for a mesma (Aristóteles).
3. **Perdurantismo:** O navio é um objeto 4-dimensional estendido no espaço-tempo — ambos os "navios" são fatias temporais do mesmo objeto 4D (Lewis).
4. **Ceticismo identitário:** A identidade não é uma questão binária — há apenas continuidade, não identidade estrita (Parfit).

### Identidade Pessoal — Continuidade Psicológica

John Locke (1689, *Ensaio sobre o Entendimento Humano*) propôs que a identidade pessoal consiste na **continuidade da memória**. Você é a mesma pessoa que fez X se você se lembra de fazer X.

**Crítica de Thomas Reid (1785):** O "argumento do oficial valente":
1. Um menino (A) é açoitado por roubar frutas.
2. Ele cresce e se torna um oficial valente (B) que se lembra do açoite.
3. O oficial se torna um general (C) que não se lembra do açoite, mas se lembra de ser oficial.
4. Pela teoria de Locke: A = B (mesma memória), B = C (mesma memória), mas A ≠ C (sem memória).
5. Isso viola a transitividade da identidade (se A = B e B = C, então A = C).

### Derek Parfit e a Abordagem Reducionista

Derek Parfit (1984, *Reasons and Persons*) revolucionou o debate:

- A identidade pessoal **não é o que importa**. O que importa é a **sobrevivência psicológica** — continuidade de memória, caráter e intenções através de conexões psicologicamente contínuas.

**Experimento mental da teletransportação:** Se você entra em um teletransportador que destrói seu corpo em Marte e constrói uma réplica exata, o que acontece? Parfit argumenta que a réplica não é *você*, mas *é sua sobrevivência* no sentido que importa. A identidade é uma "caixa preta" — o que realmente nos importa é o feixe de conexões psicológicas.

Filosoficamente, Parfit defende:
- **Reducionismo:** A existência de uma pessoa consiste apenas na existência de um cérebro, corpo e conexões psicológicas. Não há um "eu" adicional (ego substancial).
- **Irrealismo sobre o eu:** A identidade pessoal não é um fato "mais profundo" — pode haver casos onde não há uma resposta certa sobre se A = B.

### A Abordagem dos 4D (Perdurantismo)

Para o objeto de 4 dimensões (David Lewis, Theodore Sider):

- Objetos são **worms** (vermes) espaço-temporais que se estendem no tempo.
- "Você" não é uma substância persistente, mas uma sequência de **fatias temporais** conectadas por relações de continuidade.
- A identidade não é um problema, é uma relação formal entre fatias.

## Filosofia da Ciência

A filosofia da ciência investiga os fundamentos, métodos e implicações da ciência.

### Karl Popper e o Falseacionismo

Popper (1934, *A Lógica da Pesquisa Científica*) propôs resolver o problema da **demarcação** (o que separa ciência de não-ciência):

- **Verificacionismo (Círculo de Viena):** Uma afirmação é científica se pode ser verificada empiricamente. Problema: leis universais ("todos os cisnes são brancos") nunca podem ser verificadas (Hume).
- **Falseacionismo:** Uma teoria é científica se faz previsões que podem ser falseadas por observações. Uma teoria não é rejeitada por ser falsa, mas por ser **irrefutável**.

Para Popper:
- Teorias científicas são **conjecturas** (hipóteses ousadas).
- A ciência progride por **eliminação de erros** (*conjectures and refutations*).
- Não há indução — a ciência não *prova* teorias, apenas *elimina* as falsas.
- **Verossimilitude:** Teorias mais próximas da verdade sobrevivem à falsificação.

**Crítica (Kuhn, Lakatos, Feyerabend):** Popper subestima a resistência das teorias à falsificação. Na prática científica, teorias não são abandonadas por uma única anomalia.

### Thomas Kuhn e os Paradigmas

Kuhn (1962, *A Estrutura das Revoluções Científicas*) descreveu a ciência como um processo histórico-social:

1. **Pré-paradigma:** Múltiplas escolas competindo; sem consenso metodológico.
2. **Ciência normal:** Um paradigma é estabelecido. Cientistas resolvem "quebra-cabeças" dentro do paradigma (ex.: mecânica newtoniana no séc. XVIII).
3. **Anomalias:** Problemas que o paradigma não consegue resolver (ex.: precessão do periélio de Mercúrio para a física newtoniana).
4. **Crise:** Acúmulo de anomalias leva à crise e ao questionamento do paradigma.
5. **Revolução:** Um novo paradigma substitui o antigo (ex.: relatividade geral substitui mecânica newtoniana).

#### Incomensurabilidade

Kuhn argumentou que paradigmas são **incomensuráveis** — não há medida neutra para compará-los. Conceitos mudam de significado: "massa" na física newtoniana não é o mesmo conceito que "massa" na relatividade. A escolha entre paradigmas não é puramente racional — envolve valores estéticos, sociais e psicológicos.

**Crítica:** Kuhn exagera a descontinuidade. Há continuidade conceitual significativa entre paradigmas (ex.: a relatividade geral reduz-se à newtoniana em condições limite).

### Paul Feyerabend e o Anarquismo Metodológico

Feyerabend (1975, *Contra o Método*) radicalizou Kuhn:

- **Tudo vale** (*anything goes*): Não há método científico universal. O progresso científico frequentemente violou regras metodológicas.
- Galileu venceu a Igreja não por método superior, mas por **retórica, propaganda e astúcia**.
- A separação entre ciência e Estado é tão importante quanto a separação entre Igreja e Estado. A ciência é apenas *uma* tradição entre muitas.
- A imposição do método científico como única forma válida de conhecimento é **imperialismo epistemológico**.

**Crítica (putnam, 1981):** Feyerabend confunde a descrição (como os cientistas *realmente* agem) com a prescrição (como *devem* agir). Que cientistas quebrem regras não mostra que regras são inúteis.

### Imre Lakatos e os Programas de Pesquisa

Lakatos (1970) buscou um meio-termo entre Popper e Kuhn:

- **Programas de pesquisa:** Estruturas teóricas com um **núcleo firme** (pressupostos irrefutáveis) e um **cinturão protetor** (hipóteses auxiliares que podem ser ajustadas).
- Um programa é **progressivo** se prevê fatos novos que são corroborados, e **degenerativo** se apenas explica fatos já conhecidos (ad hoc).
- Exemplo: O programa marxista foi degenerativo (previa pauperização crescente que não ocorreu) enquanto o programa darwinista foi progressivo (prevê descobertas paleontológicas).

### A Nova Filosofia Experimental da Ciência

A partir dos anos 1990, filósofos começaram a usar métodos empíricos para estudar a ciência:

- **Social epistemology of science** (Kitcher, 1993; Longino, 1990): A distribuição social do trabalho cognitivo afeta a confiabilidade da ciência.
- **Estudos de laboratório** (Latour & Woolgar, 1979): Observação etnográfica de como fatos científicos são construídos socialmente.
- **Filosofia experimental** (Knobe, Nichols, Machery): Experimentos sobre intuições filosóficas de não-filósofos.

## Filosofia da Linguagem

A filosofia da linguagem investiga a natureza, origem e uso da linguagem. Está intimamente ligada à epistemologia, metafísica e filosofia da mente.

### Significado e Referência

Gottlob Frege (1892, "Sobre Sentido e Referência") fez a distinção fundamental:

- **Referência (*Bedeutung*):** O objeto no mundo ao qual uma expressão se refere (Vênus, para "a Estrela da Manhã").
- **Sentido (*Sinn*):** O modo como a referência é apresentada (diferentes descrições do mesmo objeto).

"Estrela da Manhã" e "Estrela da Tarde" têm a mesma referência (Vênus) mas sentidos diferentes. Isto explica como identidades podem ser informativas (a = b não é trivial quando a e b têm sentidos diferentes).

### Teorias do Significado

1. **Teoria referencialista:** O significado de uma palavra é seu referente (Mill, Russell inicial).
   - Problema: palavras sem referente ("Pégaso", "o atual rei da França") teriam significado zero.

2. **Teoria do uso:** O significado de uma palavra é seu uso na linguagem (Wittgenstein, 1953, *Investigações Filosóficas*).
   - "O significado de uma palavra é seu uso na linguagem" — Wittgenstein rejeita que o significado seja uma entidade mental ou objeto no mundo.

3. **Teoria verificacionista:** O significado de uma proposição é o método de sua verificação (Círculo de Viena, Carnap, Ayer).
   - Problema: proposições sobre o passado ou leis universais não são verificáveis, mas têm significado.

4. **Semântica de mundos possíveis:** O significado de uma proposição é o conjunto de mundos possíveis onde ela é verdadeira (Kripke, 1963; Lewis, 1970).

### Pragmática

A pragmática (Grice, 1975; Austin, 1962; Searle, 1969) estuda como o contexto afeta o significado:

- **Atos de fala (*speech acts*):** Ao dizer algo, fazemos algo — prometer, ameaçar, declarar (Austin, *How to Do Things with Words*).
- **Implicaturas:** O que é comunicado mas não dito literalmente (Grice, "lógica e conversação").
- **Máximas conversacionais:** Quantidade, qualidade, relação, maneira — regras implícitas da comunicação cooperativa.

### Kripke e os Designadores Rígidos

Saul Kripke (1972, *O Nomear e a Necessidade*) revolucionou a filosofia da linguagem e metafísica:

- **Designadores rígidos:** Nomes próprios ("Aristóteles") referem-se ao mesmo objeto em todos os mundos possíveis onde ele existe.
- **Necessidade a posteriori:** "Água é H₂O" é necessariamente verdadeira (verdade em todos os mundos possíveis), mas descoberta empiricamente (a posteriori). Isto colapsa a distinção tradicional entre necessário/a priori e contingente/a posteriori.
- **Teoria causal da referência:** Nomes referem-se através de uma cadeia causal de batismo inicial, não através de descrições.

### A Linguagem Privada

Wittgenstein (1953, *Investigações Filosóficas*) argumenta contra a possibilidade de uma **linguagem privada** — uma linguagem que só o falante pode entender, referindo-se a suas sensações privadas:

> "Se um leão pudesse falar, não poderíamos entendê-lo." (§ 223)

O argumento contra a linguagem privada tem implicações profundas para: (1) qualia — experiências subjetivas são públicas através de critérios comportamentais; (2) IA — o significado de estados internos de IA é dado por seu uso público, não por "experiências internas".

## Metafísica da Modaliade

### Mundos Possíveis

A metafísica modal investiga necessidade, possibilidade e contingência.

- **Realismo modal (David Lewis, 1986):** Mundos possíveis são entidades concretas, causalmente isoladas do nosso. "Possível" significa "real em algum mundo possível".
- **Atualismo modal (Kripke, Plantinga):** Apenas o mundo atual é real. Mundos possíveis são descrições ou estados de coisas — não entidades concretas.

### O Problema dos Possibilia

O realismo modal explica elegantemente verdades modais (necessidade = verdade em todos os mundos, possibilidade = verdade em algum mundo), mas viola a navalha de Ockham: postula uma infinidade de mundos concretos.

## Glossário

| Termo | Definição |
|-------|-----------|
| **Anarquismo metodológico** | Tese de Feyerabend de que não há método científico universal |
| **Ceticismo** | Posição que questiona a possibilidade do conhecimento |
| **Compatibilismo** | Tese de que livre arbítrio e determinismo são compatíveis |
| **Contrafactual** | Condicional do tipo "se X tivesse sido diferente, Y seria diferente" |
| **Determinismo** | Tese de que todo evento tem uma causa suficiente anterior |
| **Epistemologia** | Estudo do conhecimento, suas fontes, natureza e limites |
| **Falseacionismo** | Método popperiano: teorias científicas devem ser falseáveis |
| **Fundacionalismo** | Crenças básicas auto-evidentes fundamentam o restante do conhecimento |
| **Incomensurabilidade** | Tese de Kuhn: teorias de paradigmas diferentes não são comparáveis por métrica neutra |
| **Metafísica** | Estudo da natureza fundamental da realidade |
| **Nominalismo** | Apenas particulares existem; universais são meros nomes |
| **Ontologia** | Estudo do ser — quais tipos de coisas existem |
| **Paradigma** | Estrutura conceitual que define a ciência normal em uma época |
| **Perdurantismo** | Objetos persistem no tempo como totalidades 4-dimensionais |
| **Programa de pesquisa** | Estrutura teórica lakatosiana com núcleo firme e cinturão protetor |
| **Verificacionismo** | Afirmações só têm significado se verificáveis empiricamente |

## Referências Bibliográficas

- Berkeley, G. (1710). *Tratado sobre os Princípios do Conhecimento Humano*.
- Chisholm, R. (1976). *Person and Object*. Open Court.
- Dennett, D. C. (1984). *Elbow Room: The Varieties of Free Will Worth Wanting*. MIT Press.
- Descartes, R. (1641). *Meditações Metafísicas*.
- Feyerabend, P. (1975). *Contra o Método*. Verso.
- Frankfurt, H. (1969). "Alternate Possibilities and Moral Responsibility". *Journal of Philosophy*, 66(23), 829-839.
- Gettier, E. (1963). "Is Justified True Belief Knowledge?". *Analysis*, 23(6), 121-123.
- Goldman, A. (1967). "A Causal Theory of Knowing". *Journal of Philosophy*, 64(12), 357-372.
- d'Holbach, P. (1770). *Sistema da Natureza*.
- Hume, D. (1739-40). *Tratado da Natureza Humana*.
- Hume, D. (1748). *Investigação sobre o Entendimento Humano*.
- Kitcher, P. (1993). *The Advancement of Science*. Oxford University Press.
- Kuhn, T. S. (1962). *A Estrutura das Revoluções Científicas*. University of Chicago Press.
- Lakatos, I. (1970). "Falsification and the Methodology of Scientific Research Programmes". In *Criticism and the Growth of Knowledge*.
- Latour, B., & Woolgar, S. (1979). *Laboratory Life*. Sage.
- Lewis, D. (1973). "Causation". *Journal of Philosophy*, 70(17), 556-567.
- Locke, J. (1689). *Ensaio sobre o Entendimento Humano*.
- Longino, H. (1990). *Science as Social Knowledge*. Princeton University Press.
- Parfit, D. (1984). *Reasons and Persons*. Oxford University Press.
- Platão. *Teeteto*.
- Plutarco. *Vidas Paralelas*.
- Popper, K. (1934). *A Lógica da Pesquisa Científica*.
- Putnam, H. (1981). *Reason, Truth and History*. Cambridge University Press.
- Reid, T. (1785). *Essays on the Intellectual Powers of Man*.
- Salmon, W. (1984). *Scientific Explanation and the Causal Structure of the World*. Princeton University Press.
- Sider, T. (2001). *Four-Dimensionalism*. Oxford University Press.
- Strawson, G. (1994). "The Impossibility of Moral Responsibility". *Philosophical Studies*, 75(1), 5-24.

## Ver Também

- [[04-Conhecimentos/07-Humanidades/Filosofia/Filosofia-da-Mente|Filosofia da Mente]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/INDEX|Índice de Filosofia]]
- [[04-Conhecimentos/07-Humanidades/Etica/Etica-de-IA-e-Alinhamento|Ética de IA e Alinhamento]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Psicologia-Cognitiva|Psicologia Cognitiva]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Consciencia-e-Cerebro|Consciência e Cérebro]]

[[04-Conhecimentos/07-Humanidades/Filosofia/INDEX|← Voltar ao índice de Filosofia]]
