---
title: "Teoria de Redes"
area: "Matematica"
tags: [conhecimento, conceito, redes, grafos, network-science, small-world, scale-free, complexidade]
related: ["Teoria-dos-Sistemas", "Ciencia-da-Computacao", "Sociologia", "Redes-Neurais"]
aliases: ["Network Science", "Network Theory", "Ciência de Redes"]
created: 2026-05-19
updated: 2026-05-19
---

# Teoria de Redes

## Visão Geral

A teoria de redes (network science) é o estudo matemático e computacional de **grafos** que representam sistemas compostos por elementos interconectados. Ela fornece as ferramentas para analisar desde a estrutura da World Wide Web até as conexões neurais do cérebro, de redes sociais a interações entre proteínas. Sua tese central é que **a estrutura das conexões determina o comportamento e a função do sistema** — tão importante quanto os próprios elementos.

Esta nota compila os fundamentos da teoria de grafos, modelos de topologia de rede, fenômenos de propagação, detecção de comunidades, métricas de centralidade e as principais redes do mundo real, conectando cada conceito a aplicações em IA, biologia, sociologia, economia e tecnologia.

---

# Parte I — Fundamentos

## Definição Formal: G = (V, E)

Um **grafo** (ou rede) é definido como um par ordenado G = (V, E), onde:

- **V** = conjunto de **vértices** (nós, nodos, nodes) — as entidades do sistema
- **E** = conjunto de **arestas** (edges, links) — as conexões entre entidades

Cada aresta e ∈ E conecta um par de vértices (u, v). Dependendo da natureza da conexão, a aresta pode ser:

- **Direcionada** (arco): u → v, a relação tem sentido (ex: A segue B no Twitter)
- **Não-direcionada**: u — v, a relação é simétrica (ex: amizade no Facebook)

Além disso, arestas podem ter **pesos** (fortaleza da conexão) ou ser **não-ponderadas** (presença/ausência binária).

### Tipos de Grafos

| Tipo | Descrição | Exemplo |
|---|---|---|
| Simples | Sem laços (self-loops) ou arestas múltiplas | Amizade |
| Multigrafo | Permite arestas múltiplas entre mesmo par | Colaboração científica |
| Direcionado (dígrafo) | Arestas têm direção | Web (hiperlinks) |
| Ponderado | Arestas têm pesos | Distância entre cidades |
| Bipartido | Vértices divididos em dois grupos, arestas só entre grupos | Autores-artigos |
| Acíclico (DAG) | Dígrafo sem ciclos | Fluxo de dependências |

## Grau e Distribuição de Graus

O **grau** k(v) de um vértice v é o número de arestas incidentes a ele. Em dígrafos, distingue-se:

- **Grau de entrada** (in-degree): k_in(v) — arestas que chegam em v
- **Grau de saída** (out-degree): k_out(v) — arestas que partem de v

A **distribuição de graus** P(k) é a probabilidade de um vértice escolhido aleatoriamente ter grau k. A forma de P(k) é a assinatura mais importante de uma rede:

- **Poisson**: típica de redes aleatórias (Erdős–Rényi)
- **Lei de potência**: P(k) ~ k^(-γ), típica de redes scale-free (Barabási–Albert)

## Caminho, Distância e Diâmetro

- **Caminho**: sequência de vértices onde cada par consecutivo é conectado por uma aresta
- **Distância** d(u, v): comprimento do menor caminho entre u e v (geodésica)
- **Diâmetro**: a maior distância entre qualquer par de vértices na rede
- **Caminho médio** ⟨d⟩: média das distâncias entre todos os pares

Redes small-world têm caminho médio curto (⟨d⟩ ~ ln N), onde N é o número de vértices.

## Componentes Conectados, Clusters e Cliques

- **Componente conectado**: subgrafo maximal onde todo par de vértices está conectado por algum caminho
- **Componente gigante** (giant component): componente que contém uma fração significativa dos vértices — típico de redes acima do limiar de percolação
- **Clique**: subgrafo onde todos os pares de vértices são adjacentes (subgrafo completo)
- **k-clique**: clique com k vértices

Redes sociais exibem alta densidade de cliques de tamanhos variados, refletindo a estrutura de grupos coesos.

## Matriz de Adjacência vs Lista de Adjacência

### Matriz de Adjacência A

Matriz N × N onde A_ij = 1 se há aresta de i para j, 0 caso contrário (ou o peso, em redes ponderadas).

Vantagens:
- Acesso O(1) para verificar existência de aresta
- Permite álgebra linear: A^k revela caminhos de comprimento k
- Autovalores de A revelam propriedades espectrais da rede

Desvantagens:
- Armazenamento O(N²) — inviável para redes grandes (ex: Facebook: ~10⁶ GB)
- Matriz é esparsa na prática (a maioria das entradas é zero)

### Lista de Adjacência

Para cada vértice, armazena uma lista de seus vizinhos.

Vantagens:
- Armazenamento O(N + E) — eficiente para redes esparsas
- Iteração sobre vizinhos é rápida

Desvantagens:
- Verificar existência de aresta leva O(k(v)) no pior caso

Na prática, redes do mundo real são armazenadas como listas de adjacência ou formatos especializados (EdgeList, GraphML, GEXF).

## Centralidade

Centralidade mede a **importância** de um vértice na rede. Existem múltiplas definições, cada uma capturando um aspecto diferente de "importância".

### Degree Centrality

C_deg(v) = k(v) / (N - 1)

A centralidade de grau é a medida mais simples: um vértice é importante se tem muitas conexões. Em dígrafos, distingue-se in-degree centralidade (popularidade) de out-degree centralidade (influência).

### Betweenness Centrality

C_bet(v) = Σ_{s ≠ v ≠ t} σ_st(v) / σ_st

onde σ_st é o número de menores caminhos entre s e t, e σ_st(v) é o número desses caminhos que passam por v. Mede o quanto um vértice atua como **ponte** entre diferentes partes da rede. Hubs de betweenness controlam o fluxo de informação.

### Closeness Centrality

C_clo(v) = 1 / Σ_{u ≠ v} d(v, u)

Um vértice tem alta closeness se está perto (em distância geodésica) de todos os outros. Mede a **eficiência** com que um nó pode espalhar informação.

### Eigenvector Centrality (PageRank)

C_eig(v) ∝ Σ_{u ∈ N(v)} C_eig(u)

A centralidade de um vértice é proporcional à soma das centralidades de seus vizinhos — uma definição recursiva. O vetor próprio associado ao maior autovalor da matriz de adjacência dá a centralidade de cada nó.

**PageRank** (Google) é uma variante da eigenvector centrality que:
- Usa uma matriz normalizada (cada vértice distribui sua importância igualmente entre seus vizinhos de saída)
- Incorpora um fator de amortecimento (damping factor) d ≈ 0.85, que modela a probabilidade de um usuário seguir um link vs. pular para um nó aleatório
- Resolve o problema de dead ends (nós sem saída) e spider traps

PageRank foi o algoritmo que fundou o Google e revolucionou a recuperação de informação na web.

## Coeficiente de Agrupamento (Clustering Coefficient)

Mede o quanto os vizinhos de um vértice estão conectados entre si — o grau de **transitividade** local.

### Coeficiente Local de Agrupamento (Watts-Strogatz)

C_i = (número de arestas entre vizinhos de i) / (k_i · (k_i - 1) / 2)

Para k_i = 0 ou 1, define-se C_i = 0. C_i varia de 0 (nenhuma conexão entre vizinhos) a 1 (todos os vizinhos conectados entre si — o nó está no centro de um clique).

### Coeficiente Médio de Agrupamento

⟨C⟩ = (1/N) · Σ_i C_i

Redes sociais têm ⟨C⟩ tipicamente entre 0.1 e 0.7 (alto clustering). Redes aleatórias Erdős–Rényi têm ⟨C⟩ = p (baixo para N grande).

## Homofilia e Assortatividade

**Homofilia** (homophily) é a tendência de vértices similares se conectarem ("pássaros da mesma pena voam juntos" / "cada qual com seu igual"). É medida pelo **coeficiente de assortatividade** (assortativity coefficient, Newman, 2002):

r = (Σ_i e_ii - Σ_i a_i b_i) / (1 - Σ_i a_i b_i)

onde e_ij é a fração de arestas que conectam vértices de tipo i a tipo j, a_i = Σ_j e_ij, b_j = Σ_i e_ij.

- r > 0: rede assortativa (vértices similares se conectam) — típico de redes sociais
- r < 0: rede disassortativa (vértices diferentes se conectam) — típico de redes biológicas e tecnológicas

A homofilia é um dos mecanismos mais poderosos de formação de comunidades (echo chambers, bolhas sociais).

---

# Parte II — Topologias e Modelos de Rede

## Redes Aleatórias (Erdős–Rényi)

O modelo **Erdős–Rényi** (ER), proposto por Paul Erdős e Alfréd Rényi em 1959, é o modelo mais simples de rede aleatória. Existem duas variantes:

- **G(n, p)**: grafo com n vértices onde cada par é conectado com probabilidade p independente
- **G(n, M)**: grafo com n vértices e M arestas escolhidas uniformemente ao acaso

### Propriedades

- **Distribuição de grau**: binomial (aproximadamente Poisson para n grande): P(k) = e^(-⟨k⟩) · ⟨k⟩^k / k!
- **Coeficiente de agrupamento**: ⟨C⟩ = p (muito baixo para redes grandes)
- **Diâmetro**: d ~ ln(n) / ln(⟨k⟩) — cresce logaritmicamente com n (pequeno mundo)
- **Componente gigante**: surge quando ⟨k⟩ > 1 (limiar de percolação)

### Transição de Fase (Percolação)

O modelo ER exibe uma transição de fase nítida em ⟨k⟩ = 1:
- ⟨k⟩ < 1: todos os componentes são pequenos (O(log n))
- ⟨k⟩ = 1: transição — maior componente escala como O(n^(2/3))
- ⟨k⟩ > 1: componente gigante emerge, contendo fração finita dos vértices

Esta transição é análoga à percolação em física e tem implicações profundas para a robustez de redes.

## Small-World (Watts-Strogatz, 1998)

Duncan Watts e Steven Strogatz (1998) propuseram um modelo que captura duas propriedades omnipresentes em redes reais:

1. **Alto coeficiente de agrupamento**: seus amigos provavelmente são amigos entre si
2. **Caminho médio curto**: qualquer pessoa está a poucos passos de qualquer outra

### Construção do Modelo Watts-Strogatz (WS)

1. Comece com um anel regular de n vértices, cada um conectado a k vizinhos mais próximos (k/2 de cada lado)
2. Para cada aresta, com probabilidade β, reconecte-a a um vértice aleatório (rewiring)

- **β = 0**: rede regular — alto clustering, alto diâmetro
- **β = 1**: rede aleatória — baixo clustering, baixo diâmetro
- **0 < β ≪ 1**: small-world — alto clustering, baixo diâmetro (a zona mágica)

### O Experimento de Milgram (1967)

Stanley Milgram conduziu o experimento clássico de "mundo pequeno": cartas foram entregues a pessoas em Nebraska e Kansas com a instrução de enviá-las a um alvo em Boston, repassando para conhecidos que pudessem se aproximar. O resultado: a mediana do número de intermediários foi **6** — daí "seis graus de separação".

Travers e Milgram (1969) replicaram o experimento com mais rigor, confirmando a estimativa de ~6 passos. Estudos modernos (Facebook, 2016, com 1.6 bilhão de usuários) encontraram distância média de 4.57 — o mundo nunca foi tão pequeno.

### Críticas ao Small-World

O modelo WS tem limitações: distribuição de grau homogênea (todos têm ~k conexões), diferente de redes reais que são scale-free. Além disso, a rede WS não é dinâmica — não captura crescimento e preferential attachment.

## Scale-Free (Barabási–Albert, 1999)

Albert-László Barabási e Réka Albert (1999) analisaram a topologia da World Wide Web e descobriram que a distribuição de graus segue uma **lei de potência**:

P(k) ~ k^(-γ), com γ tipicamente entre 2 e 3

Isto significa: muitos nós com poucas conexões e **poucos hubs** com muitas conexões. Não há uma escala típica — daí o nome **scale-free** (livre de escala).

### Preferential Attachment (Apego Preferencial)

O mecanismo gerador proposto por Barabási e Albert é o **preferential attachment** (ou "the rich get richer"):

1. **Crescimento**: a rede começa com m₀ vértices e cresce com a adição de novos vértices um a um
2. **Apego preferencial**: cada novo vértice se conecta a m ≤ m₀ vértices existentes com probabilidade proporcional ao grau do vértice alvo: Π(k_i) = k_i / Σ_j k_j

O resultado é que hubs crescem mais rápido que nós periféricos — o **efeito Mateus** ("aos que têm, mais será dado").

### Universalidade

Redes scale-free são onipresentes na natureza e na sociedade:
- Internet (roteadores): γ ≈ 2.5
- World Wide Web (páginas): γ ≈ 2.1
- Rede de citações acadêmicas: γ ≈ 2.5
- Rede metabólica (E. coli): γ ≈ 2.2
- Rede de coautoria científica: γ ≈ 2.5
- Rede de atores de Hollywood: γ ≈ 2.3

### Propriedades

- **Robustez a falhas aleatórias**: remover nós aleatórios raramente desconecta a rede, pois a maioria dos nós tem grau baixo
- **Vulnerabilidade a ataques direcionados**: remover os hubs (maiores graus) fragmenta a rede rapidamente
- **Diâmetro ultra-pequeno**: d ~ ln ln N (ainda menor que em redes aleatórias)
- **Ausência de limiar epidêmico**: mesmo patógenos com baixa transmissibilidade podem se espalhar (ver seção de propagação)

## Modelos Geográficos e Espaciais

Em muitas redes reais, a **distância física** entre os nós importa. Exemplos:
- **Redes de transporte**: aeroportos, rodovias, ferrovias, metrô
- **Redes de infraestrutura**: rede elétrica, tubulações de água/gás, fibra óptica
- **Redes de sensores**: redes de dispositivos IoT com alcance limitado

Nestas redes, a probabilidade de conexão decai com a distância: P(conexão) ~ f(d), tipicamente uma função de potência ou exponencial.

O modelo **gravitacional** (inspirado na lei da gravidade de Newton) postula que a força da conexão entre dois locais é proporcional ao produto de suas massas (população, PIB) e inversamente proporcional à distância ao quadrado. Este modelo é usado em economia regional e planejamento de transporte.

## Redes Bipartidas e Multipartidas

- **Rede bipartida**: vértices pertencem a dois tipos distintos; arestas só existem entre tipos diferentes
- **Rede multipartida**: mais de dois tipos de vértices

Exemplos clássicos:
- **Autores ↔ Artigos**: um autor escreve um artigo (rede de coautoria projetada)
- **Usuários ↔ Filmes**: Netflix, IMDb (sistemas de recomendação)
- **Pacientes ↔ Sintomas**: diagnóstico médico
- **Genes ↔ Doenças**: genômica

Redes bipartidas são frequentemente **projetadas** em uma das partições. Por exemplo, da rede autores-artigos, projeta-se a rede de coautoria onde dois autores são conectados se co-escreveram um artigo.

## Redes Hierárquicas

Muitos sistemas complexos exibem **modularidade hierárquica**: módulos dentro de módulos dentro de módulos. Exemplos:
- **Biologia**: célula → tecido → órgão → organismo
- **Organizações**: equipe → departamento → divisão → corporação
- **Internet**: roteadores → AS (sistemas autônomos) → continentes

A **estrutura hierárquica** pode ser quantificada pelo coeficiente de agrupamento dependente do grau: C(k) ~ k^(-1) — os hubs têm menor clustering que nós periféricos, indicando um agrupamento aninhado.

---

# Parte III — Fenômenos em Redes

## Propagação em Redes

A propagação em redes modela como entidades (doenças, informação, comportamentos) se espalham através das conexões.

### Modelo SIR (Epidemias)

O modelo **SIR** (Kermack-McKendrick, 1927) é o framework clássico para epidemias:

- **S** (Susceptível): indivíduo saudável, pode ser infectado
- **I** (Infectado): indivíduo doente, transmite a doença
- **R** (Recuperado/Removido): indivíduo imune ou morto

Em redes, cada nó é S, I ou R. A transmissão ocorre com probabilidade β por aresta S-I, e a recuperação com probabilidade μ.

O **número básico de reprodução** R₀ = (β/μ) · ⟨k⟩ determina o comportamento:
- R₀ < 1: epidemia morre (subcrítico)
- R₀ > 1: epidemia se espalha (supercrítico)

Em redes scale-free, **não há limiar epidêmico**: R₀ crítico → 0, ou seja, mesmo doenças de baixa transmissibilidade podem se tornar pandêmicas.

### Contágio Complexo

Diferente de doenças biológicas, a propagação de comportamentos, tecnologias ou ideias frequentemente requer **múltiplas exposições** para que um nó adote o novo comportamento. Isto é chamado de **contágio complexo** (Centola & Macy, 2007).

Características:
- O nó precisa de um número t (threshold) de vizinhos infectados para se tornar infectado
- A rede precisa de alta **densidade de clustering** para permitir a propagação
- Contágio complexo é mais sensível à estrutura que contágio simples (SIR)

Exemplos: ativismo político, adoção de tecnologias, mudança de comportamento social.

### Difusão de Inovação (Rogers, 1962)

Everett Rogers categorizou adotantes de inovações em cinco grupos ao longo de uma curva S (sigmoide):

1. **Inovadores** (2.5%): aventureiros, tomam risco
2. **Early adopters** (13.5%): líderes de opinião, respeitados
3. **Maioria inicial** (34%): deliberativos, adotam após ver benefícios
4. **Maioria tardia** (34%): céticos, adotam sob pressão social
5. **Retardatários** (16%): tradicionalistas, resistentes à mudança

O **tipping point** (ponto de inflexão) ocorre quando a adoção atinge ~15-20% da população — a partir daí, a inovação se espalha por contágio social.

## Cascatas e Comportamento de Manada

### Information Cascades

Uma **cascata de informação** ocorre quando indivíduos racionais ignoram sua própria informação privada e imitam o comportamento observado dos outros — levando a decisões subótimas em grupo (Bikhchandani, Hirshleifer & Welch, 1992).

Mecanismo:
1. Agentes decidem sequencialmente com base em sinal privado + observação de decisões anteriores
2. Após algumas decisões, a informação pública (observada) domina a privada
3. Agentes passam a imitar — a cascata começa

Exemplos: bolhas financeiras, moda, sucesso de livros/filmes.

### Herd Behavior

Comportamento de manada é o fenômeno psicológico/social onde indivíduos seguem a multidão. Em redes, é amplificado por:
- **Prova social**: se muitas pessoas fazem algo, deve ser correto
- **Reforço de sinal**: múltiplas fontes confirmam a mesma informação
- **Custo de dissenso**: discordar do grupo tem custo social

## Robustez e Resiliência

### Ataque Aleatório vs. Ataque Direcionado

Uma descoberta central de Barabási e colaboradores:

- **Redes aleatórias (ER)**: ataque aleatório e direcionado têm efeito similar — a rede fragmenta gradualmente
- **Redes scale-free (BA)**: são **extremamente robustas** a falhas aleatórias (precisam perder ~80% dos nós para fragmentar) mas **extremamente frágeis** a ataques direcionados a hubs (poucos hubs removidos fragmentam a rede)

Esta propriedade tem implicações profundas para:
- Segurança cibernética: ataques a hubs (DNS, AS) podem derrubar a Internet
- Epidemias: vacinação de hubs é a estratégia mais eficiente
- Infraestrutura: proteger hubs é crítico para resiliência

### Percolação

A **percolação** é a transição de fase onde uma rede globalmente conectada se fragmenta em componentes isolados quando uma fração crítica de nós ou arestas é removida. O **limiar de percolação** p_c é a fração de nós/arestas que precisa ser removida para quebrar o componente gigante.

- Redes ER: p_c = 1 - 1/(⟨k⟩ - 1)
- Redes scale-free: p_c → 0 para γ < 3 (são tão resistentes a falhas aleatórias que o limiar de percolação tende a zero — nunca fragmentam completamente)

## Imunização

Estratégias de **imunização** em redes buscam proteger a população com o mínimo de vacinas possível, explorando a topologia:

1. **Imunização aleatória**: escolhe nós ao acaso — ineficiente em redes scale-free
2. **Imunização de hubs**: vacina os nós de maior grau — extremamente eficiente
3. **Imunização por acquaintances**: escolhe um nó aleatório e vacina um de seus vizinhos (sem precisar conhecer a topologia global) — quase tão eficiente quanto vacinar hubs diretamente
4. **Imunização por betweenness**: vacina nós com maior betweenness centralidade — eficaz mas computacionalmente cara

O princípio: em redes scale-free, a imunização de uma fração mínima de hubs pode proteger toda a rede (imunidade de rebanho), enquanto imunização aleatória exigiria vacinar quase toda a população.

## Fecho Triádico

O **fecho triádico** (triadic closure) é o mecanismo pelo qual dois vértices que compartilham um vizinho em comum tendem a se conectar diretamente. Em redes sociais, traduz-se no ditado: "o amigo do meu amigo é meu amigo".

O fecho triádico explica:
- O alto coeficiente de agrupamento em redes sociais
- A formação de triângulos (cliques de tamanho 3)
- A evolução de comunidades a partir de sobreposição de vizinhanças

Rapoport (1953) foi o primeiro a formalizar este mecanismo, que mais tarde foi quantificado pelo **coeficiente de agrupamento** de Watts-Strogatz.

## Força dos Laços Fracos (Granovetter, 1973)

Mark Granovetter, no artigo seminal "The Strength of Weak Ties" (1973), mostrou que **laços fracos** (conhecidos, não amigos próximos) são frequentemente mais valiosos que laços fortes para a difusão de informação nova.

O argumento:
- Laços fortes criam **clusters densos** onde todos sabem o que todos sabem — a informação é redundante
- Laços fracos atuam como **pontes** entre clusters diferentes, trazendo informação não-redundante

A descoberta surpreendente: quando as pessoas encontram empregos através de contatos pessoais, é mais provável que o contato seja um **conhecido** (laço fraco) do que um amigo próximo (laço forte). Granovetter chamou isso de "the strength of weak ties".

Aplicações:
- **Mercado de trabalho**: networking importa mais que currículo
- **Inovação**: novas ideias vêm de fora do cluster imediato
- **Difusão**: laços fracos são os canais de informação entre comunidades

---

# Parte IV — Comunidades

## Detecção de Comunidades

Comunidades (ou módulos, clusters) em redes são grupos de vértices densamente conectados entre si e esparsamente conectados ao resto da rede. A detecção de comunidades é um dos problemas centrais da ciência de redes.

### Algoritmo de Louvain (Blondel et al., 2008)

O algoritmo de Louvain é o método mais popular de detecção de comunidades devido à sua eficiência O(N log N) e qualidade dos resultados.

Fases:
1. **Otimização local**: para cada nó i, move i para a comunidade do vizinho que maximiza o ganho de modularidade ΔQ
2. **Agregação**: contrai cada comunidade em um super-nó, criando uma nova rede
3. Repete até que nenhum movimento aumente Q

Louvain é guloso e pode produzir comunidades desconectadas. A variante **Louvain refinado** corrige este problema.

### Algoritmo de Girvan-Newman (2002)

Girvan e Newman propuseram um método divisivo baseado em **betweenness de arestas** (edge betweenness):

1. Calcule a betweenness de todas as arestas
2. Remova a aresta com maior betweenness
3. Recalcule as betweenness
4. Repita até que a rede se fragmente em componentes

O resultado é uma **dendrograma** hierárquico de comunidades. O custo computacional é O(N³) — inviável para redes grandes.

### Clique Percolation (Palla et al., 2005)

O método de **clique percolation** detecta comunidades sobrepostas (um nó pode pertencer a múltiplas comunidades):

1. Encontre todos os k-cliques (subgrafos completos de k vértices)
2. Dois k-cliques são adjacentes se compartilham k-1 vértices
3. Comunidades são componentes conectados no grafo de k-cliques

Diferente de Louvain e Girvan-Newman (que produzem partições disjuntas), clique percolation permite que um nó pertença a várias comunidades — o que é mais realista para redes sociais.

## Modularidade (Newman, 2006)

A **modularidade** Q é a métrica mais usada para avaliar a qualidade de uma partição de comunidades. Mede a fração de arestas dentro das comunidades menos a fração esperada em uma rede aleatória equivalente (modelo nulo):

Q = (1/2E) · Σ_ij [A_ij - (k_i k_j / 2E)] · δ(c_i, c_j)

Onde:
- A_ij = matriz de adjacência
- k_i, k_j = graus dos vértices
- E = número total de arestas
- δ(c_i, c_j) = 1 se i e j estão na mesma comunidade, 0 caso contrário

Q varia de -1 a 1. Valores típicos:
- Q > 0.3: indica estrutura comunitária significativa
- Q > 0.7: comunidades muito bem definidas
- Q < 0: partição pior que aleatória

### Limitações da Modularidade

- **Resolução limite**: a modularidade não detecta comunidades menores que ~√(2E) — módulos pequenos são fundidos (Fortunato & Barthelemy, 2007)
- **Ótimos múltiplos**: a paisagem de modularidade tem muitos ótimos locais próximos
- **Viés de tamanho**: tende a favorecer comunidades de tamanho similar

## Sobreposição de Comunidades (Palla, 2005)

Gergely Palla e colaboradores mostraram que em redes sociais reais, comunidades são **sobrepostas** — um vértice pertence a múltiplas comunidades simultaneamente (ex: uma pessoa pertence à família, ao trabalho, ao clube esportivo).

A **matriz de afiliação comunidade-membro** modela esta sobreposição: cada nó tem um vetor de pertencimento a comunidades. Métodos como **BigCLAM** (Yang & Leskovec, 2013) e clique percolation detectam estas estruturas.

## Estrutura de Core-Periferia

A estrutura **core-periferia** (Borgatti & Everett, 2000) descreve redes onde um grupo central densamente conectado (core) é cercado por uma periferia esparsamente conectada:

- **Core**: nós altamente conectados entre si e com a periferia
- **Periferia**: nós conectados principalmente ao core, não entre si

Diferente de comunidades (que são grupos coesos separados), core-periferia é uma estrutura hierárquica de centralidade. O **k-core** de um grafo é o subgrafo maximal onde todos os vértices têm grau ≥ k dentro do subgrafo.

Aplicações: redes de citação, redes de comércio global, redes de colaboração científica.

---

# Parte V — Redes do Mundo Real

## Redes Sociais

### Facebook (~2.9B usuários)

A maior rede social do mundo. Em 2016, pesquisadores do Facebook (Backstrom et al.) analisaram 1.6 bilhão de usuários e encontraram:
- Distância média: 4.57 (três graus e meio de separação)
- 99.9% dos pares estão conectados em até 5 passos
- Alta assortatividade (homofilia etária, geográfica, educacional)
- Estrutura de comunidades fortemente sobrepostas

### Twitter / X

Rede de microblogging (direcionada — seguir ≠ ser seguido). Fenômenos estudados:
- **Influência**: identificação de usuários influentes (degree, PageRank, Klout)
- **Echo chambers**: homofilia política cria câmaras de eco onde a informação é reforçada dentro do grupo e raramente desafiada
- **Propagação de desinformação**: notícias falsas se espalham mais rápido que verdadeiras (Vosoughi, Roy & Aral, 2018 — Science)
- **Hashtags como marcadores de comunidade**

### LinkedIn

Rede profissional focada em conexões de negócios. Características:
- Laços mais fracos que Facebook (rede de contatos profissionais)
- Uso intensivo de homofila por indústria, cargo, educação
- Recomendação de conexões baseada em similaridade estrutural (SimRank)

## Redes Biológicas

### Rede de Interação Proteína-Proteína (PPI)

Proteínas raramente funcionam isoladamente — elas interagem formando complexos e vias de sinalização. A PPI network tem:
- Nós: proteínas (~20.000 no humano)
- Arestas: interações físicas entre proteínas
- Propriedades: scale-free (poucas proteínas "hub" interagem com muitas), alto clustering
- Aplicações: identificação de alvos farmacológicos, predição de funções de proteínas

### Redes Metabólicas

Representam as reações bioquímicas do metabolismo:
- Nós: metabólitos (substratos, produtos)
- Arestas: reações que convertem um metabólito em outro
- Propriedades: hierárquicas, scale-free, alto clustering
- Aplicações: engenharia metabólica, design de fármacos

### Redes Neurais

O cérebro é uma rede massivamente paralela:
- Nós: neurônios (~86B no humano) ou regiões cerebrais (conectoma)
- Arestas: sinapses (~10¹⁵)
- Propriedades: small-world, scale-free (parcialmente), alto custo energético
- **Conectoma**: o mapa completo das conexões neurais — o Projeto Conectoma Humano (HCP) mapeia a conectividade estrutural e funcional do cérebro
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]] — veja nota dedicada

## Redes Tecnológicas

### Internet (Roteadores e AS)

A Internet tem duas camadas principais:
- **Nível de roteadores**: ~10⁶ nós, γ ≈ 2.5
- **Nível de AS** (Sistemas Autônomos): ~10⁴ nós, γ ≈ 2.1

A Internet é a maior rede projetada por humanos e exibe:
- Topologia scale-free (poucos AS conectam a maioria)
- Alto custo de conexão (física, contratual)
- **Protocolo BGP**: gerencia as rotas entre AS
- Vulnerabilidade a ataques DDoS em hubs (DNS root servers)

### World Wide Web

Não confundir com Internet. A Web é a rede de **páginas e hiperlinks**:
- Nós: ~10⁹ páginas
- Arestas: ~10¹¹ hiperlinks
- Direcionada: links de saída (outgoing) e de entrada (incoming)
- A topologia da Web inspirou PageRank e a fundação do Google

### Redes de Telefonia e Energia

- **Rede telefônica**: historicamente a primeira rede global de comunicação. Estrutura hierárquica com centrais de comutação
- **Rede elétrica**: nós = subestações/geradores, arestas = linhas de transmissão. Propriedades: alta vulnerabilidade a cascatas (apagões de 2003 nos EUA e Europa)

## Redes Econômicas

### Rede de Comércio Global (World Trade Network)

- Nós: países (~200)
- Arestas: fluxos de exportação/importação (ponderadas por valor ou volume)
- Propriedades: scale-free (poucos países dominam o comércio), alta densidade
- Análise: centralidade revela países centrais (EUA, China, Alemanha) vs. periféricos

### Rede Financeira (Interbancária)

- Nós: bancos e instituições financeiras
- Arestas: empréstimos, derivativos, exposições
- Propriedades: densa, com alta conectividade entre grandes bancos
- Fenômeno: **contágio financeiro** — a falência de um banco pode se propagar pela rede (crise de 2008, Lehman Brothers)
- Regulação: Basileia III exige testes de estresse baseados em topologia de rede

### Cadeia de Suprimentos (Supply Chain)

- Nós: empresas (fornecedores, fabricantes, distribuidores, varejistas)
- Arestas: fluxo de materiais/produtos
- Fenômeno: **efeito chicote** (bullwhip effect) — pequenas flutuações na demanda do consumidor são amplificadas ao longo da cadeia (Forrester, 1961)

## Redes Linguísticas

### Redes Semânticas

- Nós: conceitos/palavras
- Arestas: relações semânticas (sinonímia, hiperonímia, meronímia)
- **WordNet**: a maior rede semântica do inglês (~155k palavras, ~117k relações)
- **WordNet em português**: OpenWordNet-PT, WordNet.BR
- Propriedades: small-world, scale-free (lei de Zipf para frequência de palavras)
- Aplicações: word sense disambiguation, embeddings de palavras (Word2Vec captura similaridade semântica)

### Redes de Co-ocorrência

- Nós: palavras
- Arestas: duas palavras co-ocorrem em uma janela de contexto (ex: 5 palavras)
- Usadas para: análise de estilo autoral, evolução de linguagem, modelagem de tópicos

## Redes Criminais

### Terrorismo

- Análise de redes terroristas (Krebs, 2002): mapeamento das conexões entre os sequestradores do 11/09
- Objetivos: identificar lideranças ocultas (betweenness), células dormentes, vulnerabilidades na rede
- Técnicas: centralidade, detecção de comunidades, análise de buracos estruturais

### Crime Organizado

- Redes de tráfico de drogas, armas, pessoas
- Características: estruturas celulares (células independentes para resiliência), alta adaptabilidade
- Métodos: análise de comunicação (telefonia, dark web), reconstrução de hierarquia

### Dark Web

- Redes anônimas (Tor, I2P) usadas para atividades ilícitas
- Nós: sites .onion (serviços ocultos)
- Arestas: hiperlinks entre sites
- Desafios: mapeamento da dark web é difícil devido ao anonimato

---

# Parte VI — Métricas e Métodos

## PageRank (Google, 1998)

O **PageRank**, desenvolvido por Larry Page e Sergey Brin, foi o algoritmo que fundou o Google. A ideia central: uma página é importante se páginas importantes apontam para ela.

Formalmente, o PageRank PR(v) de uma página v é:

PR(v) = (1 - d) + d · Σ_{u ∈ B_v} PR(u) / k_out(u)

onde:
- d = damping factor (≈ 0.85): probabilidade de seguir um link
- B_v = conjunto de páginas que apontam para v
- k_out(u) = número de links de saída de u

O PageRank é resolvido iterativamente (ou por autovalor) e converge rapidamente. Foi o algoritmo que tornou possível a busca em escala web.

## HITS (Kleinberg, 1999)

O algoritmo **HITS** (Hyperlink-Induced Topic Search), de Jon Kleinberg, distingue dois papéis em uma rede direcionada:

- **Hub**: página que aponta para muitas autoridades (diretório, portal)
- **Authority**: página apontada por muitos hubs (fonte de informação)

As pontuações são calculadas recursivamente:
- a(v) = Σ_{u → v} h(u)
- h(v) = Σ_{v → u} a(u)

Diferente do PageRank (que dá uma pontuação única), HITS dá duas pontuações complementares. Foi a base do algoritmo do Ask.com (Teoma).

## SimRank (Jeh & Widom, 2002)

**SimRank** mede similaridade estrutural entre dois nós com base na premissa: **dois objetos são similares se estão relacionados a objetos similares**. A similaridade entre a e b é:

s(a, b) = (C / |N(a)| · |N(b)|) · Σ_{x ∈ N(a)} Σ_{y ∈ N(b)} s(x, y)

onde C é um fator de decaimento (0 < C < 1). SimRank é computado iterativamente.

Aplicações: sistemas de recomendação, mecanismos de busca (similaridade entre páginas), detecção de spam.

## Motifs (Alon, 2002)

**Motifs** de rede são padrões de interconexão que ocorrem com frequência significativamente maior que o esperado em redes aleatórias. Uri Alon demonstrou que redes biológicas (regulação gênica, metabolismo) exibem motifs característicos:

| Motif | Descrição | Exemplo |
|---|---|---|
| Feed-forward loop (FFL) | A → B → C, A → C | Regulação gênica |
| Bi-fan | A, B → C, D | Sinalização celular |
| Feedback loop | A → B → C → A | Osciladores |

A presença de motifs sugere **pressão seletiva**: a rede evoluiu para ter estas estruturas porque elas conferem vantagem funcional.

## Graphlets (Pržulj, 2004)

**Graphlets** são uma generalização de motifs: subgrafos conectados de tamanhos pequenos (2-5 nós) considerando **todas** as configurações possíveis — não apenas as frequentes. Cada nó em um graphlet ocupa uma posição distinta chamada **automorfismo** (orbit), e a **assinatura de graphlets** de um nó conta quantas vezes ele aparece em cada orbit.

Enquanto motifs analisam o padrão global, graphlets fornecem uma **assinatura local** para cada nó, útil para:
- Comparar redes (alignamento topológico)
- Classificar nós
- Identificar funcionalidade de proteínas em PPI networks

## Embeddings de Nós

Embeddings de nós mapeiam cada vértice da rede a um vetor em ℝ^d (d << N) preservando propriedades estruturais — similar ao que Word2Vec faz com palavras.

### DeepWalk (Perozzi et al., 2014)

**DeepWalk** gera embeddings de nós usando random walks + Word2Vec (Skip-Gram):

1. Realiza random walks curtos a partir de cada nó (sequências de vértices)
2. Trata cada walk como uma "frase" e cada nó como uma "palavra"
3. Treina Skip-Gram para prever vizinhos no walk dado um nó central

DeepWalk preserva similaridade estrutural de segunda ordem: nós com vizinhanças similares têm embeddings próximos.

### Node2Vec (Grover & Leskovec, 2016)

**Node2Vec** estende DeepWalk introduzindo dois parâmetros de busca:
- **p** (return parameter): controla probabilidade de revisitar o nó anterior
- **q** (in-out parameter): controla se o walk prefere explorar a vizinhança local (BFS) ou global (DFS)

Com p e q ajustáveis, Node2Vec pode aprender embeddings que capturam desde homofilia (BFS) até papéis estruturais (DFS). É um dos métodos mais flexíveis e usados.

### GraphSAGE (Hamilton et al., 2017)

**GraphSAGE** (Graph SAmple and aggreGatE) é um método de aprendizado indutivo: em vez de treinar embeddings para nós específicos, treina **funções agregadoras** que geram embeddings para qualquer nó (mesmo não visto durante treinamento).

A cada iteração:
1. Amostra uma vizinhança do nó alvo
2. Agrega os embeddings dos vizinhos (média, LSTM, pooling)
3. Concatena com o embedding do nó da iteração anterior
4. Passa por uma rede neural (transformação não-linear)

GraphSAGE é a base de sistemas de recomendação em larga escala (Pinterest, Uber).

### Graph Neural Networks (GNNs)

**GNNs** são a generalização mais poderosa de embeddings de nós. Uma GNN é uma rede neural que opera diretamente na estrutura do grafo, atualizando embeddings de nós através de **propagação de mensagens**:

h_v^{(l+1)} = f^{(l)}(h_v^{(l)}, Σ_{u ∈ N(v)} g^{(l)}(h_v^{(l)}, h_u^{(l)}))

Variantes populares:
- **GCN** (Graph Convolutional Network): agregação ponderada por grau
- **GAT** (Graph Attention Network): agregação com pesos de atenção (Vaswani-style)
- **GIN** (Graph Isomorphism Network): agregação soma (mais expressiva)

Aplicações: predição de ligações (link prediction), classificação de nós, classificação de grafos, geração de moléculas (drug discovery).

---

# Parte VII — Teoremas Fundamentais

## "It's a Small World" (Milgram, 1967; Travers & Milgram, 1969)

O experimento de Milgram demonstrou que a sociedade humana é uma rede small-world com distância média de ~6 passos. O teorema não é formal no sentido matemático, mas o fenômeno é robusto: centenas de replicações em diferentes contextos confirmam que redes sociais têm caminhos médios curtos.

## Preferential Attachment Gera Power Law (Barabási-Albert, 1999)

Barabási e Albert demonstraram formalmente que o mecanismo de crescimento + preferential attachment gera uma distribuição de graus que segue lei de potência P(k) ~ k^(-3) no limite de N grande. O expoente γ = 3 é universal para o modelo BA; variações (envelhecimento, custo de conexão, fitness) produzem γ entre 2 e 3.

A prova utiliza a **equação mestra** (master equation) para a evolução do grau médio de um nó:

∂k_i / ∂t = m · k_i / Σ_j k_j

que integrada dá k_i(t) ~ (t / t_i)^(1/2), onde t_i é o tempo de nascimento do nó. A distribuição de graus resultante é P(k) ~ 2m² · k^(-3).

## Lei de Metcalfe: Valor de Rede ~ n²

**Robert Metcalfe** (co-inventor do Ethernet) propôs que o valor de uma rede de comunicação é proporcional ao quadrado do número de usuários: V ~ n².

A justificativa: cada novo usuário pode se conectar com todos os existentes, criando n(n-1)/2 conexões potenciais. Exemplos:
- **Fax**: um fax sozinho é inútil; com n faxes, o valor é ~n²
- **Facebook**: o valor para os usuários cresce com o quadrado da base de usuários
- **Efeito de rede**: startups de plataforma buscam escalar rápido para atingir o tipping point

Críticas: o valor real depende da estrutura da rede (não é n² para redes segmentadas ou com capacidade limitada). Versões refinadas (Briscoe, Odlyzko, Tilly, 2006) propõem V ~ n · log n.

## Número de Dunbar: ~150 Relações Estáveis

**Robin Dunbar**, antropólogo, propôs que o neocórtex humano impõe um limite cognitivo ao número de relações sociais estáveis que uma pessoa pode manter. Baseado em correlações entre tamanho do neocórtex e tamanho de grupo social em primatas, Dunbar estimou:

- **~150**: número máximo de relações estáveis (grupo de confiança)
- **~50**: círculo de amigos próximos
- **~15**: círculo íntimo de confiança
- **~5**: suporte emocional próximo (melhores amigos, familiares)

O número de Dunbar é consistente com:
- Tamanho de vilas neolíticas (~150)
- Tamanho de unidades militares (companhia ~150)
- Número médio de seguidores no Twitter/Facebook que recebem interação regular
- Redes de Natal (envio de cartões)

---

# Conexões

- [[Teoria-dos-Sistemas|Teoria dos Sistemas e Sistemas Complexos]] — Redes são a topologia subjacente de todo sistema complexo; small-world e scale-free são discutidos na nota de sistemas
- [[Ciencia-da-Computacao|Ciência da Computação]] — PageRank, HITS, GNNs são contribuições da computação; teoria de grafos é fundacional
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]] — O cérebro como rede complexa: conectoma, small-world, plasticidade
- [[04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao|Teoria da Informação]] — Entropia de Shannon conecta-se à compressão de redes e overlap de comunidades
- [[04-Conhecimentos/07-Humanidades/Matematica/Probabilidade-e-Estatistica|Probabilidade e Estatística]] — Distribuições de grau (Poisson, power law), modelos de percolação
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial|Álgebra Linear Essencial]] — Matriz de adjacência, autovalores, SVD, eigenvector centrality
- [[04-Conhecimentos/07-Humanidades/Matematica/Calculo-e-Otimizacao|Cálculo e Otimização]] — Otimização em GNNs, gradiente descendente em GraphSAGE

---

# Referências

- Barabási, A.-L. (2016). *Network Science*. Cambridge University Press.
- Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393(6684), 440-442.
- Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509-512.
- Granovetter, M. S. (1973). The strength of weak ties. *American Journal of Sociology*, 78(6), 1360-1380.
- Milgram, S. (1967). The small world problem. *Psychology Today*, 1(1), 61-67.
- Newman, M. E. J. (2010). *Networks: An Introduction*. Oxford University Press.
- Newman, M. E. J. (2006). Modularity and community structure in networks. *Proceedings of the National Academy of Sciences*, 103(23), 8577-8582.
- Blondel, V. D., et al. (2008). Fast unfolding of communities in large networks. *Journal of Statistical Mechanics*, P10008.
- Perozzi, B., Al-Rfou, R., & Skiena, S. (2014). DeepWalk: Online learning of social representations. *KDD*.
- Grover, A., & Leskovec, J. (2016). Node2Vec: Scalable feature learning for networks. *KDD*.
- Hamilton, W., Ying, Z., & Leskovec, J. (2017). Inductive representation learning on large graphs. *NeurIPS*.
- Page, L., et al. (1999). The PageRank citation ranking: Bringing order to the web. *Stanford Technical Report*.
- Kleinberg, J. (1999). Authoritative sources in a hyperlinked environment. *JACM*, 46(5), 604-632.
- Palla, G., et al. (2005). Uncovering the overlapping community structure of complex networks in nature and society. *Nature*, 435(7043), 814-818.
- Centola, D., & Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology*, 113(3), 702-734.
- Rogers, E. M. (1962). *Diffusion of Innovations*. Free Press.
- Alon, U. (2007). Network motifs: theory and experimental approaches. *Nature Reviews Genetics*, 8(6), 450-461.
- Pržulj, N. (2007). Biological network comparison using graphlet degree signature. *Bioinformatics*, 23(2), e177-e183.
- Dunbar, R. I. M. (1992). Neocortex size as a constraint on group size in primates. *Journal of Human Evolution*, 22(6), 469-493.
- Fortunato, S., & Barthelemy, M. (2007). Resolution limit in community detection. *Proceedings of the National Academy of Sciences*, 104(1), 36-41.
- Kermack, W. O., & McKendrick, A. G. (1927). A contribution to the mathematical theory of epidemics. *Proceedings of the Royal Society A*, 115(772), 700-721.

[[04-Conhecimentos/07-Humanidades/Matematica/INDEX|← Voltar ao índice de Matemática]]
