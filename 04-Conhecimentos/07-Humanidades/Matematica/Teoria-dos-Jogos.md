---
title: "Teoria dos Jogos"
area: "Matematica"
tags: [conhecimento, conceito, jogos, nash, estrategia, cooperacao, equilibrio, mecanismos]
related: ["Teoria-dos-Sistemas", "Negociacao", "Economia-Digital", "Modelos-Mentais", "Evolucao-Biologica"]
aliases: ["Game Theory", "Teoria dos Jogos", "Decisão Estratégica"]
created: 2026-05-19
updated: 2026-05-19
---

# Teoria dos Jogos

## Fundamentos

### Definição

A teoria dos jogos é o estudo matemático das interações estratégicas entre agentes racionais. Cada agente (jogador) toma decisões que afetam não apenas seu próprio resultado, mas também os resultados dos outros jogadores. Diferentemente da otimização clássica (onde um agente maximiza uma função independente), na teoria dos jogos o resultado de cada jogador depende das escolhas conjuntas de todos os participantes.

O termo "jogo" não implica entretenimento — refere-se a qualquer situação onde exista interdependência estratégica: desde uma partida de xadrez até uma guerra nuclear, de um leilão de espectro de telecomunicações à evolução de uma espécie.

### Elementos fundamentais de um jogo

Todo jogo bem definido possui ao menos quatro componentes:

1. **Jogadores (players):** os agentes que tomam decisões. Podem ser indivíduos, empresas, países, genes, algoritmos ou qualquer entidade capaz de escolher entre alternativas.
2. **Ações/Estratégias (actions/strategies):** o conjunto de escolhas disponíveis para cada jogador. Uma estratégia é um plano completo de ação para todas as contingências possíveis.
3. **Payoffs (recompensas ou utilidades):** os resultados que cada jogador recebe, normalmente representados como números que refletem preferências (utilidade). Jogadores racionais buscam maximizar seus payoffs esperados.
4. **Informação:** o conhecimento que cada jogador possui sobre o jogo — as regras, os payoffs, as ações dos outros, e a estrutura do jogo como um todo.

Um jogo é formalmente representado como uma tripla G = (N, S, u), onde N é o conjunto de jogadores, S = S₁ × S₂ × ... × Sₙ é o espaço de perfis de estratégias, e u: S → ℝⁿ é a função de payoff que mapeia cada perfil estratégico a um vetor de utilidades.

### Representação: forma normal vs. extensiva

**Forma normal (estratégica):** representa o jogo como uma matriz de payoffs. Cada jogador escolhe uma estratégia simultaneamente (ou sem conhecimento das escolhas alheias). Útil para jogos simultâneos.

**Forma extensiva:** representa o jogo como uma árvore de decisão, com nós representando pontos de decisão, ramos representando ações, e informações sobre quem joga quando e o que sabe. Essencial para jogos sequenciais.

### Tipos de jogos

A classificação dos jogos segue várias dimensões:

**Cooperativos vs. Não-cooperativos**
- Jogos cooperativos permitem acordos vinculativos (binding agreements) entre jogadores. O foco está em como coalizões se formam e como dividem os ganhos (valor de Shapley, núcleo).
- Jogos não-cooperativos focam nas escolhas individuais de cada jogador, sem acordos externos que possam ser impostos. É o ramo dominante da teoria.

**Simultâneos vs. Sequenciais**
- Simultâneos: os jogadores escolhem suas ações ao mesmo tempo (ou sem conhecer a jogada alheia).
- Sequenciais: os jogadores se alternam, e quem joga depois pode observar (parcial ou totalmente) as ações anteriores.

**Soma-zero vs. Soma não-zero**
- Soma-zero: o ganho de um jogador é exatamente a perda de outro. O total de payoffs é constante (ex.: pôquer, xadrez).
- Soma não-zero: os jogadores podem ganhar ou perder juntos. A cooperação pode criar valor (ex.: comércio, acordos ambientais).

**Informação perfeita vs. imperfeita**
- Perfeita: todos os jogadores conhecem todas as ações anteriores do jogo.
- Imperfeita: algum jogador não sabe o que foi jogado antes (comum em jogos simultâneos).

**Informação completa vs. incompleta**
- Completa: todos conhecem a estrutura do jogo e os payoffs de todos.
- Incompleta: algum jogador não sabe os payoffs ou o tipo dos outros (Harsanyi, 1967-68).

### Racionalidade e utilidade esperada

A teoria dos jogos clássica assume que os jogadores são racionais: cada jogador tem preferências consistentes (completas e transitivas) sobre os resultados e escolhe a ação que maximiza sua utilidade esperada, dadas suas crenças sobre o comportamento alheio.

A hipótese de racionalidade é uma simplificação analítica, não uma descrição literal do comportamento humano. A economia comportamental (Kahneman, Tversky, Thaler) documenta inúmeros desvios sistemáticos desse ideal. Ainda assim, o modelo racional serve como benchmark — previsões teóricas são então comparadas com dados experimentais e empíricos.

## Jogos Clássicos

### Dilema do Prisioneiro (Prisoner's Dilemma)

O jogo mais influente da teoria. Dois suspeitos são interrogados separadamente. Cada um pode cooperar (ficar em silêncio) ou trair (confessar). A matriz de payoffs típica:

| | Cooperar | Trair |
|---|---|---|
| **Cooperar** | (3, 3) | (0, 5) |
| **Trair** | (5, 0) | (1, 1) |

**Análise:** Trair é uma estratégia estritamente dominante para ambos os jogadores — não importa o que o outro faça, trair produz um payoff maior. O equilíbrio resultante (trair, trair) com payoff (1, 1) é Pareto-inferior à cooperação mútua (3, 3). O dilema está na tensão entre racionalidade individual e racionalidade coletiva.

**Dilema do Prisioneiro Iterado (IPD):** Quando o jogo se repete indefinidamente (ou com probabilidade de continuação), a cooperação pode emergir. Robert Axelrod (1984) organizou um torneio computacional onde estratégias submetidas por especialistas competiam em IPD. A vencedora foi **tit-for-tat** (Anatol Rapoport): coopera na primeira rodada, depois imita a jogada anterior do oponente. Características-chave do tit-for-tat: é **gentil** (não trai primeiro), **provocável** (retalia imediatamente), **clemente** (perdoa após uma retaliação), e **clara** (fácil de reconhecer).

Axelrod extraiu lições gerais: não seja invejoso, não traia primeiro, reciproque cooperação e traição, e seja claro em sua estratégia. O torneio mostrou que a cooperação pode surgir em um mundo de egoístas sem autoridade central — desde que haja interação repetida.

### Batalha dos Sexos (Battle of the Sexes)

Um casal quer passar a noite juntos, mas prefere atividades diferentes (luta vs. ballet). Ambos preferem estar juntos a separados, mas cada um prefere sua atividade favorita.

| | Luta | Ballet |
|---|---|---|
| **Luta** | (2, 1) | (0, 0) |
| **Ballet** | (0, 0) | (1, 2) |

O jogo tem dois equilíbrios de Nash puros (Luta, Luta) e (Ballet, Ballet), além de um equilíbrio misto. O problema de coordenação é agravado pelo conflito distributivo — ambos querem coordenar, mas discordam sobre **como** coordenar. Este jogo modela situações de padronização tecnológica, negociações salariais, e qualquer cenário onde partes em conflito precisam coordenar.

### Chicken (Galinha)

Dois jovens dirigem um carro em rota de colisão. Quem desvia primeiro é o "galinha" (perde). Se nenhum desvia, ambos morrem.

| | Desvia | Reta |
|---|---|---|
| **Desvia** | (0, 0) | (-1, +1) |
| **Reta** | (+1, -1) | (-10, -10) |

Diferente do Dilema do Prisioneiro, Chicken não tem estratégia dominante. A pior situação é a colisão mútua. Este jogo captura a lógica da **bravata** (brinkmanship): cada jogador tenta convencer o outro de que está comprometido a seguir em frente, esperando que o outro pisque primeiro. É um modelo clássico para crises internacionais (Crise dos Mísseis de Cuba, 1962) e competição empresarial (guerra de preços). O filme _Rebel Without a Cause_ (1955) popularizou a metáfora com a cena do "jogo da galinha" com carros roubados.

### Caça ao Veado (Stag Hunt, Rousseau)

Inspirado na filosofia de Jean-Jacques Rousseau: dois caçadores podem caçar um veado juntos (cooperação) ou uma lebre sozinhos (segurança). Caçar o veado exige cooperação contínua; se um abandona, o veado escapa.

| | Veado | Lebre |
|---|---|---|
| **Veado** | (4, 4) | (0, 2) |
| **Lebre** | (2, 0) | (2, 2) |

Ao contrário do Dilema do Prisioneiro, a traição não é dominante — cooperar também pode ser racional se você confia que o outro cooperará. O jogo tem dois equilíbrios de Nash puros: (Veado, Veado) — o eficiente — e (Lebre, Lebre) — o seguro. A Caça ao Veado modela o problema social fundamental: como superar o medo da traição para realizar empreendimentos coletivos que beneficiam a todos. Tem aplicações em formação de estados, segurança cibernética, P&D colaborativo, e acordos climáticos.

### Jogo do Ultimato (Ultimatum Game)

Um proponente recebe uma quantia (ex.: R$ 100) e oferece uma divisão ao respondente. Se o respondente aceita, ambos recebem; se rejeita, ninguém recebe nada. O jogo é jogado uma única vez, sem repetição.

O equilíbrio de Nash padrão (subgame perfect) prevê: o proponente oferece o mínimo possível (R$ 1), e o respondente aceita qualquer oferta positiva. Na prática, experimentos replicados centenas de vezes mostram:
- Ofertas abaixo de 20-30% são frequentemente rejeitadas.
- A oferta modal é 50-50 (fairness).
- A rejeição é uma forma de punição altruísta — o respondente sacrifica ganho material para punir o que percebe como injustiça.

O Ultimatum Game é a principal evidência experimental contra a hipótese de racionalidade estrita. Explicações incluem: aversão à desigualdade (Fehr & Schmidt, 1999), reciprocidade forte (Gintis, Bowles, Boyd, Fehr), normas sociais internalizadas, e emoções como raiva e desprezo. Estudos transculturais (Henrich et al., 2001) mostram variações significativas: sociedades com alta cooperação em subsistência (ex.: machiguenga do Peru) rejeitam menos; sociedades com forte reciprocidade (ex.: lamalera da Indonésia) rejeitam mais.

### Jogo do Ditador (Dictator Game)

Variação do Ultimatum: o proponente simplesmente decide a divisão, e o respondente não pode rejeitar. O equilíbrio prevê: o ditador fica com tudo. Experimentalmente, muitos ditadores dão algo (20-30% em média), revelando altruísmo, aversão à desigualdade, ou efeito de demanda social (não querem parecer egoístas para o experimentador). A redução do anonimato aumenta a generosidade.

### Dilema do Voluntário (Volunteer's Dilemma)

Um bem público é produzido se **pelo menos um** jogador voluntaria um custo. Se ninguém voluntaria, todos perdem. Exemplos: alguém precisa chamar o bombeiro quando há fumaça, pagar a conta do jantar, ou assumir a liderança de um projeto.

O equilíbrio simétrico em estratégias mistas produz uma probabilidade de cada jogador se voluntariar que torna os outros indiferentes. Quanto mais jogadores, menor a probabilidade individual de voluntariar — mas maior a chance de que **alguém** o faça. O paradoxo: em grupos grandes, a probabilidade de que ninguém voluntarie é não-negligenciável (difusão de responsabilidade). Este jogo modela bystander effect (Genovese syndrome), free-riding em bens públicos, e participação em eleições.

### Centipede Game (Jogo da Centopeia)

Dois jogadores alternam entre "passar" (continuar o jogo) ou "pegar" (terminar com uma divisão desigual). O bolo cresce a cada rodada, mas a divisão se torna mais desigual para quem passa. Se passam até o final, ambos recebem altos payoffs.

| Rodada | Ação    | Payoff (A, B) |
|--------|---------|---------------|
| 1      | A passa | Continua      |
| 2      | B passa | Continua      |
| ...    | ...     | ...           |
| 100    | B pega  | (99, 100)     |
|        | A pega  | (100, 1)      |
|        | Ambos passam | (100, 100)|

A indução retroativa (backward induction) prevê que o jogador A pega na primeira rodada — pois, raciocinando de trás para frente, B pegaria na última, então A pega na penúltima, e assim sucessivamente. Experimentalmente, a maioria dos jogadores passa várias rodadas antes de pegar, obtendo payoffs muito maiores. O Centipede Game expõe a fragilidade da indução retroativa como descrição do comportamento humano — confiança, altruísmo e bounded rationality (racionalidade limitada) produzem resultados superiores.

## Conceitos-Chave

### Equilíbrio de Nash

O conceito mais central da teoria dos jogos não-cooperativos. Um perfil de estratégias (s₁*, s₂*, ..., sₙ*) é um equilíbrio de Nash se nenhum jogador pode obter um payoff maior **desviando unilateralmente** de sua estratégia, mantendo as estratégias dos demais fixas.

Formalmente: para cada jogador i, para toda estratégia sᵢ ∈ Sᵢ, uᵢ(sᵢ*, s₋ᵢ*) ≥ uᵢ(sᵢ, s₋ᵢ*).

John Nash provou (1950, 1951) que **todo jogo finito (número finito de jogadores e estratégias) possui pelo menos um equilíbrio de Nash** — possivelmente em estratégias mistas. Este teorema de existência, baseado no teorema do ponto fixo de Kakutani (depois Brouwer), é um dos resultados mais importantes da teoria econômica do século XX. Nash recebeu o Nobel de Economia em 1994 (com Harsanyi e Selten).

O equilíbrio de Nash não é necessariamente eficiente (Pareto-ótimo) — o Dilema do Prisioneiro é a demonstração clássica. Tampouco é único — Batalha dos Sexos tem dois equilíbrios puros. E não é auto-evidente como os jogadores coordenam em um equilíbrio particular quando há múltiplos (problema de seleção de equilíbrio).

### Estratégia dominante vs. dominada

**Estratégia estritamente dominante:** produz payoff estritamente maior que qualquer outra, independentemente do que os outros jogadores façam. Quando todos os jogadores têm uma estratégia dominante, o equilíbrio é trivial (ex.: Dilema do Prisioneiro).

**Estratégia estritamente dominada:** existe outra estratégia que produz payoff estritamente maior, independentemente do que os outros façam. Estratégias dominadas podem ser eliminadas iterativamente (eliminação iterada de estratégias estritamente dominadas) para simplificar jogos.

**Estratégia fracamente dominada:** existe outra estratégia que produz payoff pelo menos tão alto em todas as situações e estritamente maior em pelo menos uma. A eliminação de estratégias fracamente dominadas requer cuidado — a ordem de eliminação pode afetar o resultado.

### Equilíbrio em Estratégias Mistas

Nem todo jogo tem equilíbrio em estratégias puras. Par ou ímpar (Matching Pennies) — onde um jogador ganha se as moedas coincidem, o outro se diferem — não tem equilíbrio puro. A solução é uma **estratégia aleatória**: cada jogador escolhe cara ou coroa com probabilidade 50%.

Um **equilíbrio de Nash em estratégias mistas** é um perfil de distribuições de probabilidade sobre ações puras tal que a estratégia mista de cada jogador é uma melhor resposta às estratégias mistas dos outros. No equilíbrio, cada jogador deve ser indiferente entre as ações puras que atribui probabilidade positiva (elas devem ter o mesmo payoff esperado).

Estratégias mistas modelam situações de incerteza deliberada: pênaltis no futebol, pôquer, guerras de propaganda, inspeções fiscais aleatórias, e qualquer cenário onde a previsibilidade é prejudicial.

### Indução Retroativa (Backward Induction)

Método para resolver jogos sequenciais com informação perfeita. Comece pelos nós finais da árvore do jogo: para cada nó, determine a ação ótima do jogador que decide ali (dados os payoffs terminais). "Pode" a árvore substituindo cada nó pelo payoff resultante da ação ótima. Repita até a raiz.

O resultado é um **Equilíbrio de Nash Perfeito em Subjogos (Subgame Perfect Equilibrium — SPE)** , refinamento introduzido por Reinhard Selten (1965). SPE exclui ameaças não-creditíveis — ameaças que seriam irracionais de executar se o ponto de decisão fosse alcançado.

Exemplo: no jogo da entrada de mercado (entrante decide entrar ou não; incumbente decide lutar ou acomodar), a indução retroativa mostra que a ameaça de lutar não é creditível — se o entrante entra, o incumbente prefere acomodar (payoff maior que lutar). Portanto, o entrante entra.

### Compromisso (Commitment)

Thomas Schelling (The Strategy of Conflict, 1960) revolucionou a teoria dos jogos ao mostrar que a **capacidade de se comprometer** — de tornar uma ameaça ou promessa creditível — é uma fonte crucial de poder estratégico.

O paradoxo do compromisso: **limitar suas próprias opções pode fortalecer sua posição**. Exemplos clássicos:

- **Queimar pontes:** um exército queima a ponte atrás de si, tornando a retirada impossível. O inimigo sabe que o exército lutará até o fim, tornando mais provável a rendição inimiga (ou a negociação).
- **Negociações salariais:** um sindicato que promete greve "até o fim" — se a promessa é creditível, a empresa cede mais.
- **Dissuasão nuclear:** a ameaça de retaliação massiva é creditível apenas se o país fizer o compromisso público e irreversível.

A credibilidade depende de: irreversibilidade (queimar pontes), reputação (histórico de cumprir ameaças), delegação (agente com incentivos diferentes), e custos afundados (investimentos que seriam perdidos se a ameaça não for executada).

### Sinalização (Signaling)

Em jogos com informação assimétrica, um jogador pode **enviar um sinal** para revelar (ou dissimular) seu tipo privado. O modelo seminal é Spence's Job Market Signaling (1973): trabalhadores têm diferentes níveis de habilidade; empresas não observam habilidade diretamente. Trabalhadores podem adquirir educação (custo), que serve como sinal de habilidade se o custo da educação é menor para os mais habilidosos (condição de single-crossing).

**Sinalização custosa:** o sinal tem um custo que torna a separação possível. Educação, propaganda, garantias, e ofertas de IPO abaixo do preço são exemplos.

**Sinalização barata (cheap talk):** comunicação sem custo (mensagens, anúncios, promessas). Pode afetar o equilíbrio mesmo sem custos, desde que haja interesses comuns suficientes entre remetente e destinatário (Crawford & Sobel, 1982).

A sinalização está no coração de mercados com informação assimétrica: seguros (seleção adversa), finanças (underpricing de IPO), publicidade (gastos excessivos como sinal de qualidade), e certificações profissionais.

### Reputação e o Folk Theorem

Em **jogos repetidos**, a interação continuada permite que a cooperação seja sustentada como equilíbrio. O **Folk Theorem** (assim chamado por ser parte do folclore da teoria antes de ser formalizado) estabelece que, em jogos repetidos indefinidamente com fator de desconto suficientemente alto, **qualquer payoff viável e individualmente racional** pode ser sustentado como um equilíbrio perfeito em subjogos (Fudenberg & Maskin, 1986).

A **reputação** funciona como um ativo: um jogador coopera hoje porque um desvio destruiria ganhos futuros de cooperação. O equilíbrio depende de:

- **Fator de desconto (δ):** quão importante é o futuro. δ = 1/(1+r), onde r é a taxa de desconto. Quanto maior δ, mais a cooperação é sustentável.
- **Estratégia de gatilho (grim trigger):** cooperar até que o outro desvie; depois, punir para sempre. Sustenta cooperação, mas é frágil (um erro acidental causa colapso).
- **Tit-for-tat:** mais robusto e perdoador.

O Folk Theorem explica por que cartéis, normas sociais, e acordos informais podem persistir mesmo sem enforcement legal — desde que os participantes valorizem suficientemente o futuro.

### Informação Assimétrica

Situações onde um jogador sabe mais que o outro sobre algum aspecto relevante do jogo. Dois problemas clássicos:

**Seleção adversa (adverse selection):** ocorre **antes** da transação. O vendedor sabe mais que o comprador sobre a qualidade do produto. Mercado de carros usados (Akerlof, 1970): carros ruins (lemons) expulsam carros bons do mercado, levando ao colapso do mercado. Soluções: sinalização, garantias, certificação, regulação.

**Risco moral (moral hazard):** ocorre **depois** da transação. Uma parte toma ações não observáveis que afetam o resultado. Exemplo: segurado toma menos cuidado; gestor não se esforça. Soluções: contratos de incentivo, monitoramento, participação nos lucros.

George Akerlof ganhou o Nobel em 2001 (com Spence e Stiglitz) pelo artigo "The Market for Lemons" (1970), que fundou a economia da informação — uma das aplicações mais frutíferas da teoria dos jogos.

### Correlated Equilibrium

Introduzido por Robert Aumann (1974, 1987), o **equilíbrio correlacionado** generaliza o equilíbrio de Nash ao permitir que os jogadores coordenem suas estratégias com base em um **sinal público ou privado** correlacionado, gerado por um "mediador" ou mecanismo externo.

No Dilema do Prisioneiro, um dispositivo correlacionador que emite recomendações (Cooperar, Cooperar) com probabilidade 1/3, (Trair, Trair) com 1/3, e (C, T) e (T, C) com 1/6 cada pode expandir o conjunto de equilíbrios para payoffs superiores ao equilíbrio de Nash único.

O equilíbrio correlacionado é um conceito mais geral e computacionalmente mais tratável que Nash. Qualquer equilíbrio de Nash é também um equilíbrio correlacionado, mas a recíproca não é verdadeira. Aumann recebeu o Nobel de Economia em 2005 (com Schelling).

### Desconto Temporal em Jogos Repetidos

Em jogos repetidos, o valor presente de um fluxo futuro de payoffs é:

V = Σₜ₌₀^∞ δᵗ · uₜ

onde δ ∈ (0,1) é o fator de desconto. Quanto maior δ, mais o jogador valoriza payoffs futuros. O fator de desconto pode refletir:
- **Paciência temporal:** preferência por recompensas imediatas.
- **Probabilidade de continuação:** se o jogo termina a cada período com probabilidade p, então δ = (1-p).
- **Custo de capital:** taxa de juros usada para descontar fluxos futuros.

A condição para cooperação sustentável em um jogo repetido é que o ganho imediato do desvio (G) seja menor que o valor presente da perda futura de cooperação (L): G < L · δ/(1-δ). Resolvendo para δ, obtém-se o fator de desconto crítico acima do qual a cooperação é factível.

## Teóricos

### John von Neumann e Oskar Morgenstern (1944)

A teoria dos jogos nasce formalmente com a publicação de **Theory of Games and Economic Behavior** (1944, Princeton University Press). Von Neumann (matemático, criador da arquitetura de computadores moderna) e Morgenstern (economista) estabeleceram a axiomática dos jogos, introduziram a forma normal e extensiva, e desenvolveram a teoria dos jogos de soma-zero (minimax theorem: em jogos de soma-zero de dois jogadores, maxmin = minmax).

O livro é monumental não apenas pelo conteúdo, mas pela abordagem: propôs formalizar a economia como uma ciência dedutiva baseada na matemática, antecipando a matematização completa da teoria econômica nas décadas seguintes.

### John Nash (1950-1951)

Em dois artigos curtos e revolucionários — "Equilibrium Points in N-Person Games" (1950) e "Non-Cooperative Games" (1951) — Nash definiu o equilíbrio que leva seu nome e provou sua existência para qualquer jogo finito usando o teorema do ponto fixo de Kakutani (e depois Brouwer). O trabalho transformou a teoria dos jogos de um subcampo da matemática pura em uma ferramenta central para economia, ciência política, biologia e muito mais.

Nash também fez contribuições fundamentais em jogos cooperativos (programa Nash para a relação entre jogos cooperativos e não-cooperativos) e teoria da barganha (solução de barganha de Nash). Sua vida foi retratada no filme "Uma Mente Brilhante" (2001, Ron Howard). Recebeu o Nobel de Economia em 1994.

### Thomas Schelling (1960)

The Strategy of Conflict (1960) é um dos livros mais originais da teoria dos jogos. Schelling não usou matemática pesada — seu método era a análise lógica de situações estratégicas, com exemplos vívidos e contra-intuitivos. Ele introduziu:

- **Compromisso (commitment):** a vantagem paradoxal de limitar opções.
- **Pontos focais (focal points):** em jogos de coordenação, soluções salientes (ex.: encontrar alguém em Nova York — "na Grand Central Station ao meio-dia") resolvem o problema de coordenação sem comunicação.
- **Bravata (brinkmanship):** a arte de levar uma situação ao limite do desastre para forçar a concessão do oponente.
- **Dissuasão e guerra nuclear:** análise estratégica da Guerra Fria, incluindo a ameaça de "retaliação massiva" e o problema da estabilidade do equilíbrio do terror.

Schelling recebeu o Nobel de Economia em 2005 (com Aumann). Sua influência vai muito além da economia — é leitura obrigatória em relações internacionais, estratégia militar, e ciência política.

### Robert Axelrod (1984)

The Evolution of Cooperation (1984) usou o Dilema do Prisioneiro Iterado para investigar como a cooperação pode emergir e persistir em um mundo de egoístas sem autoridade central. O famoso torneio computacional de Axelrod mostrou que tit-for-tat vence — uma estratégia simples, cooperativa, retaliadora e perdoadora.

Contribuições principais:
- A cooperação pode surgir mesmo sem amizade ou previsão — basta interação repetida com probabilidade de encontro futuro.
- Estratégias bem-sucedidas são: não-invejosas (não buscam vencer o oponente, apenas obter bons resultados), não-traiçoeiras (cooperam primeiro), reciprocadoras (imitam o oponente), e claras.
- A evolução da cooperação tem três estágios: **emergência** (cooperação começa em pequenos clusters), **robustez** (cooperação resiste a invasão por traidores), e **estabilidade** (cooperação se torna a norma).

### John Harsanyi (1967-1968)

Harsanyi resolveu o problema de modelar **jogos com informação incompleta** (quando jogadores não conhecem os payoffs ou tipos dos outros). Sua inovação foi transformar um jogo de informação incompleta em um jogo de informação imperfeita através da introdução da **natureza** como um jogador que move primeiro, determinando o "tipo" de cada jogador segundo uma distribuição de probabilidade comum (common prior).

Este "truque de Harsanyi" tornou possível a análise formal de situações onde há incerteza sobre as características dos jogadores — essencial para leilões, negociações, e praticamente toda interação econômica real. Harsanyi compartilhou o Nobel de 1994 com Nash e Selten.

### Reinhard Selten (1965, 1975)

Selten introduziu o refinamento mais importante do equilíbrio de Nash para jogos sequenciais: o **Equilíbrio Perfeito em Subjogos (SPE)** , que exige que as estratégias constituam um equilíbrio de Nash em **cada subjogo** da árvore do jogo. SPE elimina ameaças não-creditíveis.

Mais tarde, Selten desenvolveu refinamentos ainda mais poderosos para jogos de forma extensiva com informação imperfeita: **equilíbrio perfeito em mão-tremulante (trembling-hand perfect equilibrium)** , onde jogadores podem cometer pequenos erros com probabilidade infinitesimal. Selten, alemão, é o único jogador (junto com Nash) mencionado entre os fundadores que também contribuiu para a psicologia econômica e a racionalidade limitada. Nobel em 1994.

### Lloyd Shapley (1953)

Shapley fez contribuições fundamentais em jogos cooperativos e matching theory:

- **Valor de Shapley (1953):** uma regra de divisão dos ganhos de uma coalizão baseada na contribuição marginal esperada de cada jogador, calculada sobre todas as ordens possíveis de entrada. É a única regra que satisfaz eficiência, simetria, linearidade e jogador nulo. Aplicações: divisão de custos, atribuição de crédito em aprendizado de máquina (Shapley values para explicabilidade de modelos — SHAP).

- **Algoritmo de Gale-Shapley (1962, com David Gale):** algoritmo de aceitação diferida para o problema do casamento estável (stable marriage). O algoritmo garante um matching estável e é ótimo para quem propõe. Base para mercados de matching: residência médica, escola pública (escolas de Boston, Nova York), doação de rins, e leilões de espectro.

Shapley recebeu o Nobel de Economia em 2012 (com Alvin Roth).

### Roger Myerson (1979-1981)

Myerson é figura central no **desenho de mecanismos (mechanism design)** — a engenharia reversa da teoria dos jogos. Dado um resultado social desejado, como desenhar as regras do jogo (mecanismo) para que a interação racional dos jogadores produza esse resultado?

Myerson provou o **princípio da revelação (revelation principle):** qualquer resultado implementável por algum mecanismo pode ser implementado por um mecanismo **direto e veraz** (onde cada jogador relata honestamente seu tipo privado). O teorema simplifica radicalmente o desenho de mecanismos, reduzindo a busca a mecanismos de revelação direta.

Contribuiu também para a teoria de leilões (Myerson-Satterthwaite theorem: nenhum mecanismo eficiente e balanceado no orçamento existe para troca bilateral com informação assimétrica — impossibilidade de comércio eficiente). Myerson recebeu o Nobel em 2007 (com Hurwicz e Maskin).

### Ariel Rubinstein (1982)

O modelo de barganha de Rubinstein (Rubinstein bargaining model) é um jogo sequencial onde dois jogadores alternam ofertas sobre a divisão de um bolo. Se o bolo encolhe com o tempo (desconto temporal), existe um único equilíbrio perfeito em subjogos: o primeiro a propor recebe (1 - δ₂)/(1 - δ₁δ₂), onde δ são os fatores de desconto.

O modelo mostra que a paciência relativa determina o poder de barganha — quem é mais paciente (maior δ) obtém mais. É a fundação teórica da análise de negociações (bargaining theory).

Rubinstein também contribuiu para jogos evolucionários, bounded rationality, e teoria dos contratos.

## Aplicações

### Economia

A teoria dos jogos é onipresente na economia moderna:

**Concorrência Oligopolista:**
- **Modelo de Cournot (1838):** duas empresas escolhem quantidades simultaneamente. O equilíbrio de Nash-Cournot produz preço e quantidade intermediários entre monopólio e concorrência perfeita.
- **Modelo de Bertrand (1883):** duas empresas escolhem preços simultaneamente. Com produtos homogêneos, o equilíbrio de Nash-Bertrand é o preço competitivo (custo marginal) — mesmo com apenas duas empresas. O paradoxo de Bertrand mostra que a concorrência em preço é muito mais intensa que em quantidade.
- **Modelo de Stackelberg (1934):** líder escolhe quantidade primeiro; seguidor observa e responde. O líder obtém vantagem (first-mover advantage).

**Leilões:**
A teoria de leilões (Vickrey, 1961; Milgrom & Weber, 1982) é uma das aplicações mais bem-sucedidas. Tipos: inglês (aberto ascendente), holandês (aberto descendente), selado de primeiro preço, selado de segundo preço (Vickrey — licitante vencedor paga o segundo maior lance). O **teorema da equivalência de receita** (Myerson, Riley & Samuelson) estabelece que, sob certas condições, todos os formatos geram a mesma receita esperada.

**Desenho de Mercado (Market Design):**
Alvin Roth aplicou teoria dos jogos para redesenhar mercados reais: residência médica americana (NRMP), escolas de Nova York e Boston, transplantes de rins (NEMIR). O princípio-chave é criar mercados **grossos** (muitos participantes), **seguros** (protegidos de manipulação), e **simples** (fáceis de navegar).

**Outras aplicações econômicas:**
- Precificação de derivativos financeiros (jogos com opções reais).
- Contratos e teoria da firma (incentivos, hierarquias, integração vertical).
- Regulação e defesa da concorrência.
- Crowdfunding, plataformas digitais, e economia de plataforma.

### Política e Relações Internacionais

**Corrida Armamentista:** modelada como Dilema do Prisioneiro — ambos os países preferem desarmamento mútuo, mas cada um teme que o outro traia. A Guerra Fria é o exemplo clássico.

**Votação Estratégica:** eleitores podem votar não em seu candidato preferido, mas naquele com mais chance de vencer (voto útil). Teorema de Gibbard-Satterthwaite (1973, 1975): nenhum sistema de votação com mais de duas alternativas é não-manipulável (à prova de votação estratégica).

**Formação de Coalizões:** em sistemas parlamentares, partidos formam coalizões para atingir maioria. A teoria dos jogos cooperativos (jogos de votação ponderada, índice de poder de Shapley-Shubik, índice de Banzhaf) analisa o poder relativo dos partidos.

**Conflitos e Guerras:** modelos de barganha de guerra (Fearon, 1995) explicam por que guerras ocorrem apesar de serem ineficientes — informação assimétrica (cada lado superestima suas chances) e problemas de compromisso (mudanças no poder relativo tornam promessas não-creditíveis).

**Política Ambiental:** aquecimento global como bem público global — Dilema do Prisioneiro em escala planetária. Acordos climáticos (Kyoto, Paris) enfrentam free-riding, enforcement, e problemas de compromisso entre gerações.

### Biologia Evolucionária

A teoria dos jogos foi importada para a biologia por John Maynard Smith e George R. Price (1973), que introduziram a **Estratégia Evolutivamente Estável (Evolutionary Stable Strategy — ESS)** .

**ESS:** uma estratégia é evolutivamente estável se, quando adotada por toda a população, nenhuma estratégia mutante rara pode invadir. Formalmente: seja E a estratégia residente e M uma mutante. E é ESS se:
1. u(E, E) > u(M, E) — E se sai melhor contra si mesma que M contra E.
2. Ou u(E, E) = u(M, E) e u(E, M) > u(M, M) — se M se sai igualmente bem contra E, então E deve se sair melhor contra M.

**Jogos clássicos na biologia:**
- **Hawk-Dove (Falcão-Pomba):** modelo de competição por recursos. Falcão luta até a vitória ou derrota severa; Pomba exibe mas recua se desafiada. O equilíbrio evolucionário é uma mistura de Falcões e Pombas — ESS.
- **Dilema do Prisioneiro:** cooperação entre animais (vampiros que regurgitam sangue, simbiose de limpeza em peixes).
- **Jogos de sinalização:** cauda do pavão como sinal custoso de qualidade (Zahavi, 1975; handicap principle).

**Mecanismos de evolução da cooperação (Nowak, 2006):**
1. **Parentesco (kin selection):** cooperar com parentes favorece genes compartilhados (Hamilton, 1964 — regra de Hamilton: r·b > c).
2. **Reciprocidade direta:** "eu ajudo você, você me ajuda" — IPD, tit-for-tat.
3. **Reciprocidade indireta:** "eu ajudo você, alguém me ajuda" — reputação.
4. **Seleção em rede:** cooperação emerge em redes espaciais ou complexas.
5. **Seleção de grupo:** grupos com mais cooperadores crescem mais.

**Dinâmica do Replicador (Replicator Dynamics — Taylor & Jonker, 1978):**
Modelo de dinâmica evolucionária onde a taxa de crescimento de uma estratégia é proporcional à diferença entre seu payoff e o payoff médio da população. Os equilíbrios da dinâmica do replicador correspondem a equilíbrios de Nash; os equilíbrios assintoticamente estáveis correspondem a ESS.

### Computação e Inteligência Artificial

**Mecanismos de Leilão:** algoritmos de leilão computacional (leilões combinatórios, leilões patrocinados — Google AdWords, Generalized Second Price Auction).

**Sistemas Multiagente (MAS):** em robótica e IA distribuída, múltiplos agentes autônomos interagem estrategicamente. Conceitos como Nash equilibrium, mechanism design, e leilões são usados para coordenar agentes sem autoridade central.

**Desenho de Mecanismos Algorítmicos (Algorithmic Mechanism Design — Nisan & Ronen, 1999):** intersecção de teoria dos jogos e ciência da computação. Como desenhar protocolos onde agentes racionais têm incentivo para seguir o protocolo? Aplicações: roteamento na internet, alocação de recursos em cloud computing, blockchains e criptomoedas (prova de trabalho, prova de aposta, mecanismos de consenso).

**Teoria dos Jogos e Aprendizado de Máquina:**
- **Jogos de duas pessoas e GANs (Generative Adversarial Networks):** o gerador e o discriminador jogam um jogo de soma-zero — o equilíbrio de Nash corresponde à distribuição real dos dados.
- **RLHF (Reinforcement Learning from Human Feedback):** modelado como jogo entre o modelo de linguagem e um "recompensador" (reward model).
- **Aprendizado por reforço multiagente (MARL):** múltiplos agentes aprendendo simultaneamente — convergência, não-estacionariedade, exploração vs. exploração em contexto multiagente.
- **Modelos de matching e recomendação:** alocação de recursos, publicidade online, sistemas de recomendação competitivos.

**Exploração vs. Exploração:** bandidos multi-braço (multi-armed bandits) — um jogador enfrenta k máquinas caça-níqueis com distribuições de recompensa desconhecidas e precisa equilibrar exploração (testar novas máquinas) e exploração (jogar na melhor conhecida). Formalizável como jogo contra a natureza.

**Outras aplicações computacionais:**
- Roteamento em redes (jogos de congestionamento — Roughgarden & Tardos, 2002).
- Preço de anarquia (Price of Anarchy): razão entre o pior equilíbrio e o ótimo social.
- Blockchains: mecanismos de consenso, leilões de gas fees (Ethereum), MEV (Maximal Extractable Value).
- Segurança cibernética: jogos de segurança, honeypots, defesa contra ataques DDoS.

### Negócios e Estratégia Empresarial

**Precificação:** guerras de preço (Bertrand), precificação predatória, discriminação de preço, bundling.

**Leilões Corporativos:** procurement reverso (empresas competem para vender a um comprador), leilões de espectro (governos alocam frequências de rádio), leilões de publicidade (Google Ads, Facebook Ads).

**Competição de Plataformas:** mercados de dois lados (two-sided markets — Rochet & Tirole, 2003). Plataformas como Uber, Airbnb, Amazon, e App Store conectam dois grupos (usuários e provedores). A teoria analisa externalidades de rede, precificação assimétrica, e estratégias de plataforma.

**Estratégia Competitiva:** o framework clássico de Porter (five forces) pode ser enriquecido com teoria dos jogos para analisar: compromissos estratégicos (investimentos irreversíveis), sinalização (anúncios de preços, capacity expansion), e jogos repetidos (colusão tácita).

**Inovação e P&D:** corridas de patentes (patent race como jogo de tournament), licenciamento de tecnologia, padrões abertos vs. proprietários.

### Outras Aplicações

**Direito:** análise econômica do direito (law and economics) — litígio como jogo, acordos extrajudiciais, responsabilidade civil, danos punitivos.

**Filosofia:** problemas de coordenação (Lewis, 1969 — convenções), contratualismo (Harsanyi, Rawls), ética e jogos evolucionários (Brian Skyrms, The Stag Hunt and the Evolution of Social Structure).

**Esportes:** pênalti como jogo de Matching Pennies (estratégia mista), seleção de times (draft como matching), e apostas esportivas.

**Saúde:** alocação de órgãos para transplante (matching), desenho de seguros de saúde (seleção adversa, risco moral), políticas de vacinação (Dilema do Voluntário).

## Conexões

- [[Economia-Digital]] — leilões online, plataformas, mecanismos de recomendação, mercados de dois lados.
- [[Negociacao]] — barganha (Rubinstein), BATNA, ZOPA, compromisso e credibilidade.
- [[Tomada-de-Decisao]] — racionalidade limitada, heurísticas, vieses, utilidade esperada.
- [[Modelos-Mentais]] — pensamento estratégico, modelagem de interações, teoria da mente.
- [[Evolucao-Biologica]] — ESS, dinâmica do replicador, seleção de parentesco, cooperação.

## Referências

- Von Neumann, J., & Morgenstern, O. (1944). *Theory of Games and Economic Behavior*. Princeton University Press.
- Nash, J. (1950). "Equilibrium Points in N-Person Games". *Proceedings of the National Academy of Sciences*, 36(1), 48-49.
- Nash, J. (1951). "Non-Cooperative Games". *Annals of Mathematics*, 54(2), 286-295.
- Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press.
- Selten, R. (1965). "Spieltheoretische Behandlung eines Oligopolmodells mit Nachfrageträgheit". *Zeitschrift für die gesamte Staatswissenschaft*, 121, 301-324.
- Aumann, R. J. (1974). "Subjectivity and Correlation in Randomized Strategies". *Journal of Mathematical Economics*, 1(1), 67-96.
- Harsanyi, J. C. (1967-68). "Games with Incomplete Information Played by Bayesian Players". *Management Science*, 14(3, 5, 7).
- Maynard Smith, J., & Price, G. R. (1973). "The Logic of Animal Conflict". *Nature*, 246, 15-18.
- Axelrod, R. (1984). *The Evolution of Cooperation*. Basic Books.
- Fudenberg, D., & Maskin, E. (1986). "The Folk Theorem in Repeated Games with Discounting or with Incomplete Information". *Econometrica*, 54(3), 533-554.
- Osborne, M. J., & Rubinstein, A. (1994). *A Course in Game Theory*. MIT Press.
- Myerson, R. B. (1991). *Game Theory: Analysis of Conflict*. Harvard University Press.
- Camerer, C. F. (2003). *Behavioral Game Theory*. Princeton University Press.
- Nowak, M. A. (2006). "Five Rules for the Evolution of Cooperation". *Science*, 314(5805), 1560-1563.
- Gintis, H. (2009). *Game Theory Evolving* (2nd ed.). Princeton University Press.
- Roughgarden, T. (2016). *Twenty Lectures on Algorithmic Game Theory*. Cambridge University Press.
- Binmore, K. (2007). *Playing for Real: A Text on Game Theory*. Oxford University Press.

[[04-Conhecimentos/07-Humanidades/Matematica/INDEX|← Voltar ao índice de Matemática]]
