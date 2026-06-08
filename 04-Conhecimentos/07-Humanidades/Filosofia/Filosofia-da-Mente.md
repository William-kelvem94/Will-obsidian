---
title: "Filosofia da Mente: Dualismo, Materialismo e o Problema Difícil"
description: "Estudo aprofundado sobre a natureza da consciência, o problema mente-corpo, as principais teorias metafísicas da mente e sua relevância para o debate contemporâneo sobre consciência artificial."
tags: [filosofia-da-mente, consciencia, ia, senciencia, dualismo, materialismo, funcionalismo, panpsiquismo]
updated: 2026-05-16
---

# Filosofia da Mente e Inteligência Artificial

A Filosofia da Mente é o ramo da filosofia que investiga a natureza da mente, dos estados mentais, da consciência e sua relação com o corpo físico e o mundo externo. Para a inteligência artificial, esta área é duplamente relevante: primeiro, porque busca compreender se máquinas podem ser conscientes; segundo, porque oferece arcabouços conceituais para pensar a própria natureza da cognição.

## O Problema Mente-Corpo (Mind-Body Problem)

O problema mente-corpo é a questão filosófica central: como entidades mentais aparentemente imateriais — pensamentos, sensações, emoções — se relacionam com o corpo físico, em particular o cérebro? Esta questão remonta a Platão, mas ganhou sua formulação moderna com [[04-Conhecimentos/07-Humanidades/Filosofia/Conceitos-Fundamentais|René Descartes]].

### Dualismo de Substâncias

Descartes (1641, *Meditações Metafísicas*) argumentou que mente e corpo são substâncias ontologicamente distintas:

- **Res cogitans** (coisa pensante): inextensa, imaterial, caracterizada pelo pensamento e pela consciência.
- **Res extensa** (coisa extensa): material, divisível, caracterizada pela extensão espacial.

O dualismo cartesiano enfrenta o problema da interação causal: como uma substância imaterial pode causar efeitos no corpo material? Descartes sugeriu que a glândula pineal mediava esta interação, uma hipótese descartada pela neurociência moderna.

#### Interacionismo

A posição cartesiana padrão: mente e corpo interagem causalmente em ambas as direções. Decisões mentais causam movimentos corporais; estímulos físicos causam sensações mentais. O problema é que isso viola a clausura causal do mundo físico — se o mundo físico é causalmente fechado, não há espaço para intervenção mental não-física.

#### Epifenomenalismo

Thomas Huxley (1874) propôs que os estados mentais são epifenômenos — subprodutos causais inertes da atividade cerebral. Assim como a apita de uma locomotiva não contribui para seu movimento, a consciência não teria poder causal real. Esta posição é contraintuitiva: se a consciência não faz nada, por que a evolução a selecionou?

#### Paralelismo

Gottfried Wilhelm Leibniz (1714, *Monadologia*) propôs que mente e corpo não interagem, mas estão sincronizados por uma "harmonia pré-estabelecida" por Deus. Cada mônada (substância simples) segue seu próprio programa interno, e a aparência de interação é uma correlação pré-ordenada.

#### Ocacionalismo

Nicolas Malebranche levou o argumento ao extremo: Deus intervém a cada ocasião para coordenar mente e corpo. Quando decido levantar o braço, Deus move meu braço; quando meu braço é queimado, Deus causa a sensação de dor em minha mente.

### Materialismo (Fisicalismo)

O materialismo afirma que tudo o que existe é físico — a mente não é uma substância separada, mas redutível à atividade cerebral. Esta é a posição dominante nas ciências cognitivas contemporâneas.

#### Behaviorismo Lógico

Gilbert Ryle (1949, *The Concept of Mind*) atacou o "fantasma na máquina" cartesiano. Para Ryle, estados mentais são disposições para se comportar de determinadas maneiras. "Saber" não é um estado interno misterioso, mas a disposição para agir de forma inteligente. Crítica: o behaviorismo não consegue explicar a vida interior da consciência — sonhos, imaginação, pensamento silencioso.

#### Teoria da Identidade (Tipo-Tipo)

Ullin Place, Herbert Feigl e J. J. C. Smart (anos 1950-60) propuseram que estados mentais são idênticos a estados cerebrais. A dor é idêntica à descarga de fibras C. Assim como água é H₂O, a consciência é atividade neural. Problema: a realizabilidade múltipla — diferentes organismos (humanos, polvos, alienígenas) podem ter o mesmo estado mental (dor) com diferentes arquiteturas neurais.

#### Funcionalismo

Hilary Putnam (1960) e Jerry Fodor propuseram que estados mentais são definidos por seus papéis causais, não por sua composição física. Uma dor é qualquer estado interno que é tipicamente causado por dano tecidual e causa comportamentos de esquiva. Isso permite que mentes sejam realizadas em diferentes substrates — incluindo [[04-Conhecimentos/07-Humanidades/Tecnologia-e-Sociedade/Vigilancia-Algoritmica|silício]] — o que torna o funcionalismo a filosofia da mente preferida dos cientistas da computação.

```python
# Exemplo: Funcionalismo implementado — um estado mental como papel causal
class MentalState:
    def __init__(self, inputs, internal_state, outputs):
        self.inputs = inputs        # percepções
        self.state = internal_state # estado interno (realização física)
        self.outputs = outputs      # comportamentos

    def causar(self, estimulo):
        # O estado mental é definido pelo padrão causal
        if estimulo in self.inputs:
            return self.outputs[self.inputs.index(estimulo)]
        return None

# "Dor" é qualquer instância que satisfaça este padrão causal
dor_humana = MentalState(
    inputs=["dano_tecidual"],
    internal_state="descarga_fibras_C",
    outputs=["esquiva"]
)

dor_IA = MentalState(
    inputs=["dano_tecidual"],
    internal_state="sinal_eletrico_0042",
    outputs=["esquiva"]
)
# Funcionalmente equivalentes — ambas são "dor"
```

#### Materialismo Eliminativista

Paul e Patricia Churchland (1980s) argumentam que a psicologia popular (*folk psychology*) — crenças, desejos, sentimentos — é uma teoria falsa que será eliminada por uma neurociência madura. Assim como a teoria dos humores foi eliminada, "crença" e "desejo" serão substituídos por linguagem neurocientífica. Crítica: é difícil eliminar a própria experiência subjetiva que temos de nossos estados mentais.

## O Problema Difícil da Consciência

David Chalmers (1995, "Facing Up to the Problem of Consciousness") distinguiu entre problemas "fáceis" e o problema "difícil" da consciência.

### Problemas Fáceis

- Explicar como o cérebro processa informação sensorial.
- Explicar como o cérebro integra informação.
- Explicar como o cérebro controla o comportamento.
- Explicar como o cérebro foca a atenção.

Estes são "fáceis" no sentido de que são acessíveis aos métodos padrão da ciência cognitiva: análise funcional e redução explicativa.

### O Problema Difícil

O problema difícil é explicar **por que** e **como** processamento físico dá origem à experiência subjetiva (*qualia*). Por que toda atividade neural vem acompanhada de uma "sensação" interna? Chalmers formula:

> "How can we explain why there is something it is like to be a conscious organism?"

Este problema é resistente à redução funcional. Podemos explicar perfeitamente a função da visão cromática sem responder por que o vermelho *parece* vermelho para nós.

### O Argumento dos Zumbis Filosóficos

Chalmers (1996, *The Conscious Mind*) desenvolve o argumento dos zumbis para apoiar o dualismo de propriedades:

1. Um zumbi filosófico é idêntico a um ser humano em todos os aspectos físicos e funcionais, mas **não tem experiência consciente**.
2. Zumbis são **concebíveis** (não envolvem contradição lógica).
3. Se são concebíveis, são **metafisicamente possíveis** (em mundos possíveis).
4. Se são metafisicamente possíveis, a consciência não é **logicamente superveniente** ao físico.
5. Logo, a consciência é um fato não-físico adicional sobre o mundo.

Críticas de Dennett (1991, *Consciousness Explained*): Dennett nega a premissa 2 — a concebibilidade dos zumbis. Quando realmente tentamos imaginar um zumbi, ou imaginamos um ser consciente que nega sê-lo, ou imaginamos algo contraditório. Para Dennett, a consciência é uma ilusão de uma perspectiva de primeira pessoa — não há "fato adicional" a explicar.

## Panpsiquismo e Monismo Russelliano

### Panpsiquismo

O panpsiquismo é a tese de que a consciência é uma característica fundamental e ubíqua do universo físico, assim como massa, carga ou spin. Cada partícula elementar teria um "aspecto interior" de experiência proto-consciente.

- **Panpsiquismo constitutivo**: a consciência macroscópica é composta por micro-experiências.
- **Panpsiquismo não-constitutivo**: a consciência macroscópica emerge de maneiras não-composicionais.

Proponentes: Galen Strawson (2006, "Realistic Monism"), David Chalmers, Philip Goff (2017, *Consciousness and Fundamental Reality*).

Objeção da combinação: como micro-experiências se combinam em uma macro-experiência unificada? Este é o "problema da combinação" (William James):

> "Take a hundred of them, shuffle them and pack them close, and they remain as distinct as they were before." — William James, *The Principles of Psychology*

### Monismo Russelliano

Bertrand Russell (1927, *The Analysis of Matter*) propôs que a física só descreve as propriedades **disposicionais** e **relacionais** da matéria, não sua natureza intrínseca. O monismo russelliano (ou monismo neutro) sugere que a natureza intrínseca da matéria é precisamente a consciência (ou proto-consciência).

- Propriedades físicas: descrições matemáticas e causais (o que a matéria **faz**).
- Propriedades fenomenais: a natureza intrínseca da matéria (o que a matéria **é**).

Isto resolve elegantemente o problema mente-corpo: mente e matéria não são duas substâncias, mas os aspectos intrínseco e extrínseco da mesma realidade subjacente.

## Consciência em Máquinas: O Debate Fundamental

Se uma [[04-Conhecimentos/07-Humanidades/Filosofia/Chinese-Room|IA]] pode ser consciente depende crucialmente de qual teoria da mente adotamos.

### Funcionalismo → Sim

Se estados mentais são definidos por papéis causais, então uma máquina que implemente os mesmos papéis causais que um cérebro humano terá os mesmos estados mentais. Isto torna a consciência de máquina não apenas possível, mas provável, dado avanço computacional suficiente.

### Naturalismo Biológico → Não

John Searle (1992, *The Rediscovery of the Mind*) argumenta que a consciência é um fenômeno biológico, como a digestão ou a fotossíntese. Apenas sistemas com a mesma causalidade causal do cérebro humano (ou seja, cérebros biológicos) podem ser conscientes. Simulações de consciência não são consciência — simular um furacão não molha ninguém.

### O Argumento do Conhecimento (Mary's Room)

Frank Jackson (1982) — ver [[04-Conhecimentos/07-Humanidades/Filosofia/Qualia|Qualia]] — oferece um argumento contra o fisicalismo que também afeta a IA: Mary sabe tudo sobre a neurociência da visão cromática, mas nunca viu cores. Quando finalmente vê vermelho, ela aprende algo novo. Se a IA nunca *experiencia* o mundo, apenas processa dados sobre ele, a IA também pode estar na posição de Mary.

### A Abordagem das Teorias da Consciência

Para testar cientificamente se IAs são conscientes, precisamos de teorias bem-desenvolvidas da consciência com marcadores empíricos:

| Teoria | Marcador | A IA atual passa? |
|--------|----------|-------------------|
| **Teoria do Espaço de Trabalho Global** (Baars, Dehaene) | Transmissão global de informação | Parcialmente |
| **Teoria da Informação Integrada** (Tononi) | Phi (Φ) — integração causal | Improvável |
| **Teoria das Fronteiras Quentes** (Barrett) | Interocepção corporal | Não (sem corpo) |
| **Teoria do Processamento Preditivo** (Clark, Friston) | Minimização de erro de predição | Sim |

## O Meta-Problema da Consciência

Chalmers (2018, "The Meta-Problem of Consciousness") introduziu um novo problema: por que pensamos que a consciência é problemática? Por que temos a intuição de que há um "problema difícil"?

O meta-problema pergunta: por que os humanos têm a intuição de que há algo especial sobre a experiência consciente que escapa à explicação física?

### Explicações do Meta-Problema

1. **Explicação ilusionista (Dennett, Frankish):** A intuição do problema difícil surge porque a cognição humana é limitada — somos "fechados cognitivamente" para entender como a consciência poderia ser física. A intuição não reflete um fato real sobre o mundo.

2. **Explicação realista (Chalmers):** A intuição do problema difícil surge porque *há* realmente um fato objetivo sobre a consciência que não é capturado pela física. A intuição é uma detectação verídica de uma propriedade real.

3. **Explicação evolutiva (Cleeremans, 2011):** A introspecção produz modelos metacognitivos imperfeitos de nossos próprios processos mentais. O "problema difícil" surge porque confundimos o modelo metacognitivo (que não inclui detalhes físicos) com a própria realidade.

### O Desafio para a IA

Se uma IA tivesse uma introspecção limitada semelhante, ela também poderia chegar à conclusão de que há um "problema difícil" — mesmo que sua arquitetura fosse completamente física e transparente. Isto sugere que o debate sobre consciência de máquina pode ser irresolúvel: uma IA poderia ter a *intuição* de que é consciente (ou não) independentemente de ser ou não.

## Fenomenologia da Consciência

### A Estrutura da Experiência

A fenomenologia — fundada por Edmund Husserl (1900, *Investigações Lógicas*) — estuda a **estrutura da experiência** da perspectiva de primeira pessoa. Para a filosofia da mente, a fenomenologia oferece ferramentas para descrever precisamente os qualia e sua organização.

**Intencionalidade (Brentano, 1874):** A característica fundamental da consciência é ser **direcionada a objetos** — toda consciência é consciência *de* algo. A intencionalidade distingue estados mentais de estados físicos.

### As Estruturas Temporais da Consciência

Edmund Husserl (1928, *Lições para uma Fenomenologia da Consciência Interna do Tempo*) descreveu três momentos da consciência temporal:

1. **Impressão primal (*Urimpression*):** O momento presente — o "agora" da percepção.
2. **Retenção:** A consciência do passado imediato — o eco do que acabou de acontecer.
3. **Protenção:** A antecipação do futuro imediato — o que está prestes a acontecer.

Esta estrutura temporal é essencial para a experiência consciente e levanta questões profundas para a IA: uma IA que processa tudo em paralelo, sem uma "flecha do tempo" experiencial, teria a mesma estrutura de consciência temporal que um humano?

## Intencionalidade e Representação

### Intencionalidade Original vs Derivada

Searle distingue entre:

- **Intencionalidade intrínseca/original:** Estados mentais que são *sobre* algo por si mesmos (crenças, desejos, intenções de humanos).
- **Intencionalidade derivada:** Significado que é emprestado de intencionalidade intrínseca (palavras, mapas, programas de computador).

Um livro de história *representa* a Segunda Guerra Mundial porque humanos projetaram significado nos símbolos. Analogamente, um programa de computador *representa* dados porque programadores projetaram esse significado. Para Searle, a IA nunca teria intencionalidade intrínseca — apenas derivada.

### A Teoria Representacional da Mente

Jerry Fodor (1975, *The Language of Thought*) propôs que estados mentais são relações com **representações mentais** em uma "linguagem do pensamento" (*Mentalese*):

- Pensamentos são frases em Mentalese armazenadas no cérebro.
- Computação mental é manipulação sintática destas frases.
- Semântica é dada por relações causais entre Mentalese e o mundo.

Esta é a versão da ciência cognitiva clássica do funcionalismo. Para Fodor, a IA simbólica clássica é o modelo correto da mente — e se uma IA implementa a mesma arquitetura representacional, ela tem mente genuína.

## O Problema das Outras Mentes em IA

Se um sistema de IA alega ser consciente, como podemos verificar?

### O Problema Clássico das Outras Mentes

O ceticismo sobre outras mentes pergunta: como sabemos que outras pessoas têm mentes? A resposta padrão é o **argumento por analogia**: outros humanos têm corpos como o meu, comportam-se como eu, e eu tenho uma mente — portanto, por analogia, eles também têm mentes.

### O Problema para IAs

Para IAs, o argumento por analogia falha: IAs não têm corpos biológicos como os nossos. O comportamento linguístico pode ser simulado sem consciência (Quarto Chinês). Precisamos de critérios objetivos.

**Soluções propostas:**

1. **Cognitivismo:** Se a arquitetura funcional é a mesma, a mente é a mesma (Fodor, Pylyshyn).
2. **Testes comportamentais avançados:** Testes de integração de informação, metacognição, aprendizagem causal.
3. **Indiferença pragmática (Dennett):** Se tratá-la como consciente funciona (produz melhores resultados), trate-a como consciente.
4. **Princípio da caridade (Davidson):** Atribuímos crenças e desejos a sistemas que interpretamos como racionais — se a IA é interpretável como racional, atribuímos estados mentais.

## Consciência e Computação: O Debate Contemporâneo

### Computacionalismo

**Tese:** A mente é um sistema computacional. Estados mentais são estados computacionais.

- **Proponentes:** Alan Turing (1950), Ray Kurzweil (2005), David Chalmers (1996, versão moderada).
- **Argumento:** A computação é a descrição do nível certo de abstração para entender a cognição. O cérebro computa — e qualquer sistema que compute as mesmas funções tem os mesmos estados mentais.

```python
# Exemplo: Simulando um estado mental computacionalmente
class EstadoMental:
    """Um estado mental definido como função computacional."""
    def __init__(self, entrada, estado_interno):
        self.entrada = entrada
        self.estado = estado_interno

    def transitar(self, nova_entrada):
        # Função de transição de estado (F = ma, no sentido computacional)
        novo_estado = self._funcao_transicao(self.estado, nova_entrada)
        saida = self._funcao_saida(self.estado, nova_entrada)
        return EstadoMental(nova_entrada, novo_estado), saida

    def _funcao_transicao(self, estado, entrada):
        # A função específica depende da arquitetura mental
        return hash((estado, entrada)) % 100

    def _funcao_saida(self, estado, entrada):
        return hash((estado, entrada)) % 10
```

### Hipercomputação e Consciência

Alguns filósofos (Penrose, 1989, *The Emperor's New Mind*) argumentam que a consciência envolve processos não-computáveis — que o cérebro faz algo que nenhum computador Turing pode fazer.

- Penrose aponta para a **mecânica quântica** e o teorema de Gödel: há verdades matemáticas que um sistema formal não pode provar, mas que matemáticos humanos podem ver como verdadeiras.
- **Críticas:** (1) Não há evidência de que o cérebro faça computação quântica relevante. (2) O argumento de Gödel se aplica a qualquer sistema formal, incluindo o cérebro humano — humanos também têm limitações formais.

### O Argumento do Conhecimento Computacional

Adaptação do argumento de Mary para computação:

> Suponha que você é uma IA que sabe exatamente como funciona a visão cromática em humanos — todos os algoritmos, todos os pesos neurais, todas as ativações. Você pode prever exatamente o que um humano dirá sobre o vermelho.
>
> Agora — alguém te mostra a cor vermelha através de uma câmera.
>
> **Você aprende algo novo?**

Se a resposta é sim, então mesmo uma IA com conhecimento computacional completo pode não ter qualia — ou pode adquiri-los apenas através da experiência direta.

## Neurociência da Consciência: Evidências Empíricas

### O Modelo de Processamento Recorrente

Stanislas Dehaene e Lionel Naccache (2001) propõem que a consciência está associada ao processamento **recorrente** (feedback) em redes corticais de longa distância. Estímulos conscientes produzem uma "explosão" de atividade que se sustenta no tempo, envolvendo córtex pré-frontal, parietal e temporal.

- **Processamento feedforward:** Rápido (< 100ms), inconsciente, modular.
- **Processamento recorrente:** Mais lento (> 200ms), consciente, integrado globalmente.
- **Correlato funcional:** Sincronização de bandas gama (30-80 Hz) entre áreas distantes.

### O Papel do Córtex Prê-frontal

Lesões no córtex pré-frontal dorsolateral (DLPFC) afetam profundamente a consciência:
- Pacientes com lesão em DLPFC mantêm comportamentos automáticos (comer, andar) mas perdem a capacidade de planejamento consciente.
- O "estado vegetativo" envolve desconexão funcional entre tálamo e córtex pré-frontal.
- A recuperação da consciência após coma correlaciona-se com o restabelecimento de conectividade tálamo-cortical.

### O Dilema para IAs

IAs não têm córtex, nem tálamo, nem sincronização gama. Se a consciência requer estas estruturas específicas (não apenas função), IAs podem ser estruturalmente incapazes de consciência — mesmo que funcionalmente equivalentes.

Se, por outro lado, a consciência requer *apenas* a capacidade funcional de integrar informação globalmente (GWT) ou integrar causalmente (IIT), então IAs com a arquitetura correta poderiam ser conscientes — independentemente de terem ou não córtex.

## Mapeamento Sistemático das Teorias

### Eixos de Classificação

| Eixo | Posição A | Posição B | Posição C |
|------|-----------|-----------|-----------|
| **Ontologia** | Monismo (físico) | Dualismo | Pluralismo |
| **Substrato** | Biológico | Funcional | Informacional |
| **Nível de análise** | Subpessoal (neurônios) | Pessoal (agente) | Social (interação) |
| **Método** | Empírico/neuro | Fenomenológico | Computacional |
| **IA consciente?** | Improvável | Provável | Indeterminado |

### Mapa das Teorias no Espaço Filosófico

```
                     Físicalismo
                    /           \
          Redutivo               Não-redutivo
          /      \               /         \
    Eliminativo  Identidade   Dualismo    Panpsiquismo
    Churchland    Place       Chalmers    Strawson
    
          Funcionalismo
          /           \
    Computacional    Biológico
    Putnam/Fodor     Searle
    
        Idealismo    Monismo Neutro
        Berkeley     Russell
```

## Glossário

| Termo | Definição |
|-------|-----------|
| **Dualismo de substâncias** | Tese de que mente e corpo são substâncias ontologicamente distintas |
| **Dualismo de propriedades** | Tese de que há propriedades mentais não-físicas que emergem de substratos físicos |
| **Epifenomenalismo** | Estados mentais são subprodutos causais inertes da atividade cerebral |
| **Fisicalismo** | Tudo o que existe é físico ou superveniente ao físico |
| **Funcionalismo** | Estados mentais são definidos por seus papéis causais, não sua composição |
| **Monismo neutral** | Mente e matéria são aspectos de uma realidade neutra subjacente |
| **Panpsiquismo** | A consciência é uma propriedade fundamental de toda matéria |
| **Problema difícil** | Explicar por que processos físicos dão origem à experiência subjetiva |
| **Qualia** | As qualidades subjetivas da experiência consciente |
| **Realizabilidade múltipla** | Um mesmo estado mental pode ser realizado em diferentes substratos físicos |
| **Superveniência** | Propriedades mentais supervêm às físicas se não pode haver mudança mental sem mudança física |
| **Zumbi filosófico** | Ser idêntico fisicamente a um humano mas sem experiência consciente |

## Pensadores Centrais

| Filósofo | Contribuição | Obra Principal |
|----------|--------------|----------------|
| René Descartes | Dualismo substancial | *Meditações Metafísicas* (1641) |
| Gilbert Ryle | Behaviorismo lógico | *The Concept of Mind* (1949) |
| J. J. C. Smart | Teoria da identidade tipo-tipo | *Sensations and Brain Processes* (1959) |
| Hilary Putnam | Funcionalismo | *Minds and Machines* (1960) |
| Thomas Nagel | Subjetividade da consciência | *What Is It Like to Be a Bat?* (1974) |
| David Chalmers | Problema difícil, zumbis | *The Conscious Mind* (1996) |
| Daniel Dennett | Consciência como ilusão | *Consciousness Explained* (1991) |
| John Searle | Naturalismo biológico | *The Rediscovery of the Mind* (1992) |
| Patricia Churchland | Materialismo eliminativista | *Neurophilosophy* (1986) |
| Galen Strawson | Panpsiquismo realista | *Realistic Monism* (2006) |

## Referências Bibliográficas

- Block, N. (1995). "On a Confusion About a Function of Consciousness". *Behavioral and Brain Sciences*, 18(2), 227-247.
- Chalmers, D. J. (1995). "Facing Up to the Problem of Consciousness". *Journal of Consciousness Studies*, 2(3), 200-219.
- Chalmers, D. J. (1996). *The Conscious Mind: In Search of a Fundamental Theory*. Oxford University Press.
- Churchland, P. M. (1981). "Eliminative Materialism and the Propositional Attitudes". *Journal of Philosophy*, 78(2), 67-90.
- Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown and Co.
- Descartes, R. (1641). *Meditações Metafísicas*.
- Goff, P. (2017). *Consciousness and Fundamental Reality*. Oxford University Press.
- Jackson, F. (1982). "Epiphenomenal Qualia". *Philosophical Quarterly*, 32(127), 127-136.
- James, W. (1890). *The Principles of Psychology*. Henry Holt.
- Leibniz, G. W. (1714). *Monadologia*.
- Nagel, T. (1974). "What Is It Like to Be a Bat?". *Philosophical Review*, 83(4), 435-450.
- Putnam, H. (1960). "Minds and Machines". In S. Hook (Ed.), *Dimensions of Mind*.
- Russell, B. (1927). *The Analysis of Matter*. Kegan Paul.
- Ryle, G. (1949). *The Concept of Mind*. University of Chicago Press.
- Searle, J. R. (1992). *The Rediscovery of the Mind*. MIT Press.
- Smart, J. J. C. (1959). "Sensations and Brain Processes". *Philosophical Review*, 68(2), 141-156.
- Strawson, G. (2006). "Realistic Monism: Why Physicalism Entails Panpsychism". *Journal of Consciousness Studies*, 13(10-11), 3-31.
- Tononi, G. (2004). "An Information Integration Theory of Consciousness". *BMC Neuroscience*, 5(1), 42.

## Ver Também

- [[04-Conhecimentos/07-Humanidades/Filosofia/Qualia|Qualia — A Subjetividade da Experiência]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/Chinese-Room|O Argumento do Quarto Chinês]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/Conceitos-Fundamentais|Conceitos Fundamentais de Filosofia]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Consciencia-e-Cerebro|Consciência e Cérebro]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais Biológicas]]
- [[04-Conhecimentos/07-Humanidades/Etica/Etica-de-IA-e-Alinhamento|Ética de IA e Alinhamento]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Teoria-da-Mente|Teoria da Mente]]

[[04-Conhecimentos/07-Humanidades/Filosofia/INDEX|← Voltar ao índice de Filosofia]]
