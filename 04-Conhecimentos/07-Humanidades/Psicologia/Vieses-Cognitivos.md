---
title: "Vieses Cognitivos e Comportamento"
area: "Psicologia"
related: ["Tomada de Decisão", "Memória", "Heurísticas", "Economia Comportamental", "Racionalidade Limitada"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, psicologia, vieses-cognitivos, heuristicas, kahneman, tversky, sistema-1, sistema-2, dunning-kruger, confirmacao, ancoragem, disponibilidade, representatividade, gigerenzer, racionalidade-ecologica, debiasing, economia-comportamental]
updated: 2026-05-16
---

# Vieses Cognitivos e Comportamento

## Indice
1. [[#Introducao -- A Revolucao dos Vieses|Introducao]]
2. [[#O Programa Heuristicas e Vieses -- Kahneman e Tversky|Programa Heuristicas e Vieses]]
3. [[#Catalogo de Vieses Cognitivos|Catalogo de Vieses]]
4. [[#A Controversia -- Gigerenzer e a Racionalidade Ecologica|Controversia Gigerenzer]]
5. [[#Vieses na Era da Informacao e da IA|Vieses na Era Digital]]
6. [[#Debiasing -- Estrategias de Mitigacao|Debiasing]]
7. [[#Glossario|Glossario]]
8. [[#Exercicios e Perguntas de Reflexao|Exercicios]]
9. [[#Referencias e Leituras Recomendadas|Referencias]]

---

## Introducao -- A Revolucao dos Vieses

Vieses cognitivos sao **desvios sistematicos** da racionalidade normativa (logica, probabilidade, teoria da decisao) que ocorrem em contextos especificos de julgamento e tomada de decisao. Diferentemente de erros aleatorios, vieses sao **previsiveis**, **replicaveis** e **influenciaveis pelo contexto**, o que os torna objeto de estudo cientifico e, cada vez mais, de intervencao pratica.

O estudo moderno dos vieses cognitivos tem suas raizes no trabalho de **Daniel Kahneman** e **Amos Tversky** na decada de 1970, que mapearam as **heuristicas** -- atalhos mentais que, embora geralmente uteis, produzem erros sistematicos em situacoes de incerteza. Kahneman recebeu o Premio Nobel de Economia em 2002 por este trabalho (Tversky falecera em 1996).

### Por que os Vieses Importam?

1. **Decisoes cotidianas:** De investimentos financeiros a escolhas de saude, vieses distorcem sistematicamente nossas escolhas.
2. **Politicas publicas:** O design de politicas (nudges) pode mitigar ou explorar vieses da populacao (Thaler & Sunstein, 2008).
3. **Sistemas de IA:** Vieses humanos contaminam dados de treino e decisoes algoritmicas, amplificando desigualdades.
4. **Design de agentes:** Assistentes de IA que reconhecem vieses humanos podem oferecer contrapontos racionais, melhorando a qualidade das decisoes dos usuarios.

### Racionalidade Limitada (Bounded Rationality)

Herbert Simon (1956, 1982) introduziu o conceito de **racionalidade limitada**: diferentemente do *homo economicus* da teoria economica classica, os seres humanos possuem:
- **Limitacoes computacionais:** Capacidade de processamento e memoria finitas.
- **Limitacoes informacionais:** Acesso incompleto a informacao relevante.
- **Limitacoes temporais:** Decisoes precisam ser tomadas sob pressao de tempo.

Nesse quadro, heuristicas nao sao *falhas* da mente, mas **adaptacoes** evolutivas para navegar um mundo complexo com recursos cognitivos limitados. A pergunta central nao e "quao irracionais somos?", mas **"em que contextos nossas heuristicas funcionam bem e em que contextos falham?"**.

---

## O Programa Heuristicas e Vieses -- Kahneman e Tversky

### As Tres Heuristicas Fundacionais

Kahneman e Tversky (1972, 1973, 1974) identificaram tres heuristicas que explicam uma ampla gama de julgamentos probabilisticos:

#### 1. Heuristica da Disponibilidade (*Availability Heuristic*)

**Definicao:** Julgamos a frequencia ou probabilidade de eventos pela facilidade com que exemplos vem a mente.

**Mecanismo:** A mente usa a **fluencia de recuperacao** como um proxy para frequencia -- se exemplos sao facilmente recuperaveis, o evento parece mais comum.

**Efeitos documentados:**
- **Disponibilidade por recuperacao:** Pessoas superestimam mortes por acidente aereo vs. acidente de carro (Lichtenstein et al., 1978) porque acidentes aereos sao mais noticiados.
- **Disponibilidade por imaginabilidade:** Cenarios vividos e facilmente imaginaveis sao julgados mais provaveis, mesmo quando improvaveis.
- **Disponibilidade por experiencia pessoal:** Eventos que presenciamos ou vivenciamos tem peso desproporcional em nossas estimativas de frequencia.

`python
class ViesDisponibilidade:
    def __init__(self):
        self.memoria_eventos = {}
        self.frequencia_real = {}

    def registrar_evento(self, tipo, midia_impacto=1.0):
        self.memoria_eventos[tipo] = self.memoria_eventos.get(tipo, 0) + midia_impacto

    def registrar_frequencia_real(self, tipo, freq):
        self.frequencia_real[tipo] = freq

    def percepcao_frequencia(self, tipo):
        peso_memoria = self.memoria_eventos.get(tipo, 0)
        freq_real = self.frequencia_real.get(tipo, 0.01)
        distorcao = (peso_memoria / (peso_memoria + freq_real + 0.001)) - (freq_real / (sum(self.frequencia_real.values()) or 1))
        return {"distorcao": distorcao, "viess_presente": abs(distorcao) > 0.1}

vies = ViesDisponibilidade()
vies.registrar_evento("acidente_aereo", midia_impacto=10.0)
vies.registrar_evento("acidente_carro", midia_impacto=1.0)
vies.registrar_frequencia_real("acidente_aereo", 1)
vies.registrar_frequencia_real("acidente_carro", 500)
print("Vies em acidentes aereos:", vies.percepcao_frequencia("acidente_aereo"))
print("Vies em acidentes de carro:", vies.percepcao_frequencia("acidente_carro"))
`

#### 2. Heuristica da Representatividade (*Representativeness Heuristic*)

**Definicao:** Julgamos a probabilidade de um evento ou objeto pertencer a uma categoria pelo grau em que ele se assemelha ao prototipo (representante tipico) daquela categoria.

**Falacias associadas:**
- **Falacia da taxa base (*Base Rate Fallacy*):** Ignorar a probabilidade previa da categoria em favor da similaridade.
  - Ex.: "Joao e meticuloso, organizado e introvertido. Ele e bibliotecario ou vendedor?" -- ignoramos que ha muito mais vendedores que bibliotecarios.
- **Falacia da conjuncao (*Conjunction Fallacy*):** Julgar que uma conjuncao especifica e mais provavel que uma categoria mais geral.
  - Ex.: O famoso problema de **Linda** (Tversky & Kahneman, 1983).

`python
def problema_linda():
    descricao = "Linda tem 31 anos, e solteira, extrovertida e muito inteligente. Ela se formou em filosofia. Quando estudante, era muito engajada em causas sociais e participava de protestos antinucleares."
    opcoes = ["A: Linda e caixa de banco", "B: Linda e caixa de banco e ativa no movimento feminista"]
    print("Descricao:", descricao)
    for o in opcoes:
        print(o)
    print("(P(A) > P(A and B) sempre, mas a representatividade faz B parecer mais provavel)")

problema_linda()
`

#### 3. Heuristica da Ancoragem e Ajuste (*Anchoring and Adjustment*)

**Definicao:** Estimativas numericas sao influenciadas por um valor inicial (ancora), mesmo que arbitrario, e o ajuste a partir da ancora e tipicamente insuficiente.

**Demonstracoes classicas:**
- Roda da fortuna (Tversky & Kahneman, 1974): Participantes giram uma roda numerada (1-100) e depois estimam a porcentagem de nacoes africanas na ONU. A ancora aleatoria influenciava a estimativa.
- **Ancoragem em julgamentos judiciais:** Juizes a quem eram apresentadas ancora mais altas (via rolamento de dados) davam sentencas mais longas (Englich et al., 2006).

`python
import random

class ExperimentoAncoragem:
    def __init__(self, ancora):
        self.ancora = ancora
        self.respostas = []

    def coletar_estimativa(self, pid, ajuste_pct=0.3):
        valor_verdadeiro = 80
        estimativa = self.ancora + (valor_verdadeiro - self.ancora) * ajuste_pct
        ruido = random.uniform(-20, 20) * (1 - ajuste_pct)
        estimativa += ruido
        estimativa = max(0, min(100, estimativa))
        self.respostas.append({"participante": pid, "estimativa": round(estimativa, 1)})

    def efeito(self):
        media = sum(r["estimativa"] for r in self.respostas) / len(self.respostas)
        return f"Ancora={self.ancora}, Media={media:.1f} (real=80)"

exp_baixo = ExperimentoAncoragem(ancora=10)
exp_alto = ExperimentoAncoragem(ancora=90)
for pid in range(10):
    exp_baixo.coletar_estimativa(pid)
    exp_alto.coletar_estimativa(pid)
print(exp_baixo.efeito())
print(exp_alto.efeito())
`

### Teoria do Prospecto (1979)

A Teoria do Prospecto (*Prospect Theory*) e o modelo descritivo de tomada de decisao sob risco mais influente ja proposto. Seus elementos principais:

1. **Ponto de referencia:** Ganhos e perdas sao definidos relativamente a um ponto de referencia (status quo), nao em termos absolutos.
2. **Funcao de valor em S:** Curva concava para ganhos (aversao ao risco), convexa para perdas (busca de risco), e mais ingreme para perdas (aversao a perda).
3. **Funcao de ponderacao de probabilidade:** Pessoas superponderam probabilidades baixas e subponderam probabilidades moderadas e altas.
4. **Efeito de enquadramento (*Framing Effect*):** A mesma escolha, apresentada como ganho ou perda, inverte preferencias.

`python
class ProspectTheory:
    def __init__(self, lam=2.25, alpha=0.88, beta=0.88):
        self.lam = lam
        self.alpha = alpha
        self.beta = beta

    def valor(self, x):
        if x >= 0:
            return x ** self.alpha
        else:
            return -self.lam * ((-x) ** self.beta)

    def escolher(self, opcao_a, opcao_b):
        v_a = sum(p * self.valor(g) for g, p in opcao_a)
        v_b = sum(p * self.valor(g) for g, p in opcao_b)
        return "A" if v_a > v_b else "B", v_a, v_b

pt = ProspectTheory()
ganhos = [(200, 1.0)]
risco = [(600, 0.33), (0, 0.67)]
perdas = [(-400, 1.0)]
risco_perda = [(-600, 0.33), (0, 0.67)]
print("Enquadramento ganhos:", pt.escolher(ganhos, risco))
print("Enquadramento perdas:", pt.escolher(perdas, risco_perda))
`

---

## Catalogo de Vieses Cognitivos

O catalogo abaixo lista os vieses mais estudados e relevantes para interacao humano-IA, agrupados por dominio cognitivo.

### Vieses de Atencao e Percepcao

| Vies | Descricao | Exemplo |
|------|-----------|---------|
| **Vies de Confirmacao** | Buscar, interpretar e lembrar informacoes que confirmam crencas pre-existentes | Pesquisar apenas fontes que confirmam sua posicao politica |
| **Efeito Bandwagon** | Adotar crencas ou comportamentos porque "todo mundo esta fazendo" | Investir em criptomoedas porque amigos estao investindo |
| **Cegueira a Mudanca** | Falha em detectar mudancas no ambiente visual | Nao perceber que o interlocutor trocou de camisa durante uma conversa |
| **Efeito Negatividade** | Processar informacao negativa mais rapidamente que positiva | Um erro em uma avaliacao pesa mais que cinco acertos |

### Vieses de Memoria

| Vies | Descricao | Exemplo |
|------|-----------|---------|
| **Vies Retrospectivo (*Hindsight*)** | Ver eventos passados como mais previsiveis do que realmente foram | "Eu sabia que aquela acao ia cair" (depois que caiu) |
| **Efeito de Falsa Memoria** | Lembrar eventos que nao ocorreram | "Lembrar" de ter visto um objeto onde nao estava |
| **Efeito de Primazia e Recencia** | Lembrar melhor do primeiro e do ultimo item de uma lista | Lembrar do inicio e fim de uma apresentacao, esquecer o meio |

### Vieses de Julgamento e Decisao

| Vies | Descricao | Exemplo |
|------|-----------|---------|
| **Dunning-Kruger** | Incompetentes superestimam sua competencia; especialistas subestimam | Iniciante em Python acha que e "quase senior" apos 3 meses |
| **Vies Otimista** | Superestimar probabilidade de eventos positivos | 90% dos motoristas se consideram "acima da media" |
| **Aversao a Perda** | Perder doi ~2x mais que ganhar alegra | Recusar aposta 50% de ganhar R e 50% de perder R |
| **Custo Irrecuperavel** | Continuar investindo devido ao que ja foi investido | Permanecer em projeto falido por "ja investi 6 meses" |
| **Efeito de Enquadramento** | Escolhas influenciadas pela apresentacao das opcoes | "90% de sobrevivencia" vs. "10% de mortalidade" |
| **Efeito Halo** | Caracteristica positiva contamina outras avaliacoes | Pessoa bonita e tambem assumida como competente |
| **Vies de Atribuicao Fundamental** | Atribuir comportamento alheio a personalidade, o proprio a situacao | "Ele furou a fila porque e mal-educado"; "Eu furei porque estou atrasado" |
| **Heuristica do Afeto** | Decisoes guiadas por reacoes emocionais imediatas | Medo de voar leva a dirigir, estatisticamente mais perigoso |
| **Vies de Amostra Pequena** | Conclusoes gerais de amostras muito pequenas | "Conheci um frances mal-educado, todos os franceses sao mal-educados" |
| **Paradoxo da Escolha** | Muitas opcoes paralisam a decisao e reduzem satisfacao | 30 minutos escolhendo entre 40 marcas de molho de tomate |

### Vieses Sociais e de Grupo

| Vies | Descricao |
|------|-----------|
| **Vies Endogrupal** | Favorecer membros do proprio grupo |
| **Efeito de Homogeneidade do Exogrupo** | Perceber o proprio grupo como diverso e outros grupos como "todos iguais" |
| **Vies de Autoridade** | Atribuir maior credibilidade a figuras de autoridade |
| **Pensamento de Grupo (*Groupthink*)** | Busca de consenso suprime o debate critico |

### A Curva de Dunning-Kruger

`python
import numpy as np

def dunning_kruger(h):
    if h < 30:
        return 100 - (30 - h) * 0.5
    elif h > 70:
        return h * 0.6 + 20
    else:
        return 100 - (100 - h) * 0.7

habilidades = np.linspace(0, 100, 10)
for h in habilidades:
    p = dunning_kruger(h)
    print(f"  Habilidade: {h:3.0f} -> Percepcao: {p:3.0f} (diferenca: {p-h:+.0f})")
`

---

## A Controversia -- Gigerenzer e a Racionalidade Ecologica

### A Critica de Gerd Gigerenzer

Gerd Gigerenzer, do Instituto Max Planck para Desenvolvimento Humano, liderou uma critica vigorosa ao programa heuristicas-e-vieses de Kahneman e Tversky, argumentando que:

1. **O padrao normativo e artificial:** Comparar heuristicas humanas com a logica formal ou probabilidade bayesiana estabelece um padrao irrealista (racionalidade *teorica*, nao *ecologica*).
2. **Heuristicas sao "fast and frugal":** Em muitas situacoes do mundo real, heuristicas simples superam modelos complexos -- um fenomeno chamado **"less-is-more"** (menos e mais).
3. **O ambiente importa:** A racionalidade nao esta na heuristica isolada, mas no **acoplamento** entre a heuristica e o ambiente em que opera (racionalidade ecologica).

### Heuristicas Fast and Frugal (Gigerenzer et al., 1999)

#### Heuristica de Reconhecimento
- **Regra:** Se um de dois objetos e reconhecido e o outro nao, infere-se que o reconhecido tem o valor mais alto no criterio.
- **Exemplo:** Alemaes (que reconhecem apenas San Diego) acertam mais que americanos (que reconhecem ambas) ao perguntar qual cidade e maior: San Diego ou San Antonio?

#### Heuristica "Take The Best"
- **Regra:** Busque a pista mais valida; se ela discrimina entre as opcoes, pare; caso contrario, va para a proxima pista.
- **Caracteristica:** Ignora informacao, e nao-compensatoria, e rapida.
- **Performance:** Iguala ou supera regressao multipla em ambientes com baixa correlacao entre pistas.

`python
class TakeTheBest:
    def __init__(self, pistas):
        self.pistas = pistas

    def decidir(self, a, b):
        for nome, val in self.pistas:
            if a.get(nome, 0) > b.get(nome, 0):
                return a, nome
            elif b.get(nome, 0) > a.get(nome, 0):
                return b, nome
        return None, "empate"

ttb = TakeTheBest([("lucro", 0.85), ("endividamento", 0.78), ("fluxo", 0.72)])
emp_a = {"lucro": 0.8, "endividamento": 0.3, "fluxo": 0.9}
emp_b = {"lucro": 0.6, "endividamento": 0.7, "fluxo": 0.5}
venc, pista = ttb.decidir(emp_a, emp_b)
print(f"Vencedor: {'A' if venc == emp_a else 'B'}, Pista: {pista}")
`

### Sintese: Quando as Heuristicas Funcionam?

Dois fatores principais, segundo Gigerenzer:

1. **Estrutura do ambiente:** Heuristicas funcionam bem em ambientes com **incerteza** (nao apenas risco calculavel) e onde a informacao e **redundante** (pistas correlacionadas).
2. **Matching:** A heuristica deve ser pareada com a estrutura do ambiente -- nao existe heuristica universalmente otima.

### Relevancia Contemporanea

O debate Kahneman vs. Gigerenzer permanece ativo. Posicoes conciliadoras:
- **Modelo adaptativo:** O cerebro alterna entre heuristicas e analise deliberada dependendo do contexto, tempo disponivel e custo da informacao.
- **Duplo-processo revisitado:** Sistema 1 e Sistema 2 podem ser vistos como um espectro de estrategias, nao dicotomia rigida.
- **Relevancia para IA:** Agentes artificiais devem aprender *quando* usar heuristicas (rapidas, baixo custo) e *quando* usar analise completa (precisa, alto custo).

---

## Vieses na Era da Informacao e da IA

### Como Vieses Humanos Contaminam Sistemas de IA

1. **Dados de treino:** Dados gerados por humanos refletem vieses historicos e sociais.
   - CVs de empresas historicas sub-representam mulheres em cargos tecnicos.
   - Corpus de texto contem estereotipos (enfermeira = mulher, medico = homem).

2. **Rotulos e anotacoes:** A subjetividade dos anotadores humanos introduz vieses nos dados de supervisionado.
   - Conteudo ofensivo: varia por cultura, idade, background do anotador.
   - Relevancia de busca: julgamento de relevancia reflete preferencias do anotador.

3. **Design de features:** A escolha do que modelar (e do que ignorar) reflete prioridades dos desenvolvedores.

4. **RLHF (Reinforcement Learning from Human Feedback):** O feedback humano para alinhar modelos reflete preferencias e vieses dos avaliadores.
   - Preferencia por respostas mais polidas vs. mais precisas.
   - Vies de deferencia a linguagem tecnica.

### O Vies de Confirmacao em Recomendadores

Sistemas de recomendacao (YouTube, TikTok, redes sociais) exploram o **vies de confirmacao** para maximizar engajamento:

`python
class RecomendadorExplorador:
    def __init__(self):
        self.perfil = {}

    def registrar(self, tema, positivo=True):
        delta = 1.0 if positivo else -0.5
        self.perfil[tema] = self.perfil.get(tema, 0) + delta

    def recomendar(self, candidatos):
        com_peso = []
        for tema, desc, inclinacao in candidatos:
            peso = self.perfil.get(tema, 0)
            sim = 1.0 - abs(inclinacao - peso) / 10.0
            com_peso.append((sim, tema, desc))
        com_peso.sort(reverse=True)
        return [(t, d) for _, t, d in com_peso[:3]]

rec = RecomendadorExplorador()
rec.registrar("politica", positivo=True)
cands = [
    ("politica", "Artigo a favor da reforma", 0.5),
    ("politica", "Artigo contra a reforma", -0.5),
    ("politica", "Analise neutra da reforma", 0.0),
    ("esportes", "Final do brasileirao", 0.0),
]
print("Recomendacoes:")
for t, d in rec.recomendar(cands):
    print(f"  [{t}] {d}")
`

### Vieses em Modelos de Linguagem

Modelos de linguagem amplificam e perpetuam vieses sociais. Este topico e tratado em profundidade no artigo dedicado: [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-em-LLMs|Vieses em LLMs]].

---

## Debiasing -- Estrategias de Mitigacao

### Niveis de Intervencao

#### 1. Individual (consciencia e treinamento)
- **Educacao sobre vieses:** Consciencia metacognitiva reduz (mas nao elimina) o impacto.
- **Considerar o oposto:** Tecnica de gerar ativamente contra-argumentos (Larrick, 2004).
- **Desacelerar:** Ativar o Sistema 2 antes de decisoes importantes.

#### 2. Processual (mudanca de fluxo decisorio)
- **Checklists:** Lista de verificacoes padronizadas reduzem a influencia de ancora e frames.
- **Pre-compromisso:** Definir criterios de decisao *antes* de ver as opcoes.
- **Perspectiva do observador:** "O que eu recomendaria a um amigo nesta situacao?"

#### 3. Ambiental (design de escolhas -- *Choice Architecture*)
- **Nudges:** Pequenas alteracoes no ambiente de decisao que facilitam escolhas melhores (Thaler & Sunstein, 2008).
- **Defaults:** Opt-out vs. opt-in (ex.: doacao de orgaos).
- **Feedback:** Informar consequencias de decisoes passadas.

#### 4. Algoritmico (sistemas de IA)
- **Pre-processamento:** Balanceamento de datasets, remocao de proxies protegidas.
- **Treinamento com restricoes:** Funcoes de perda que penalizam discriminacao.
- **Pos-processamento:** Ajuste de limiares de decisao por grupo.
- **Transparencia:** Explicabilidade (XAI) para permitir auditoria humana.

### Framework de Debiasing para Agentes de IA

`python
import re

class AgenteDebiasing:
    def __init__(self):
        self.vieses = {
            "confirmacao": {
                "padrao": r"\b(ja sei|nao preciso ver|ja decidi)\b",
                "contraponto": "Uma perspectiva diferente que talvez voce nao tenha considerado:"
            },
            "ancoragem": {
                "padrao": r"\b(pelo menos|no minimo)\s*(\d+)\b",
                "contraponto": "Esse valor inicial pode estar influenciando sua estimativa."
            },
            "custo_irrecuperavel": {
                "padrao": r"\b(ja investi|nao posso parar agora|tempo perdido)\b",
                "contraponto": "O tempo ja investido nao deve influenciar decisoes futuras."
            },
            "otimismo": {
                "padrao": r"\b(com certeza|nunca vou falhar|so vai dar certo)\b",
                "contraponto": "Otimismo e bom, mas vamos considerar tambem cenarios negativos."
            }
        }

    def analisar(self, texto):
        encontrados = []
        for nome, config in self.vieses.items():
            if re.search(config["padrao"], texto.lower()):
                encontrados.append(nome)
        return encontrados

    def responder(self, texto, base):
        v = self.analisar(texto)
        if not v:
            return base
        partes = ["> **Nota:** Identifiquei padroes que podem indicar vieses no seu raciocinio."]
        for nome in v:
            partes.append(f"> **{nome}:** {self.vieses[nome]['contraponto']}")
        partes.append("---")
        partes.append(base)
        return "\n".join(partes)

agente = AgenteDebiasing()
print(agente.responder(
    "Ja investi 6 meses nesse projeto, nao posso parar agora.",
    "Sugiro reavaliar o ROI do projeto."
))
`

### Metricas de Efetividade de Debiasing

| Metrica | Descricao |
|---------|-----------|
| **Taxa de reconhecimento** | % de instancias enviesadas detectadas corretamente |
| **Taxa de intervencao** | % de instancias em que o agente ofereceu contraponto |
| **Impacto na decisao** | Mudanca na decisao final apos intervencao |
| **Satisfacao do usuario** | O usuario achou a intervencao util ou intrusiva? |

---

## Glossario

| Termo | Definicao |
|-------|-----------|
| **Ancoragem** | Influencia de um valor inicial arbitrario sobre estimativas subsequentes |
| **Aversao a Perda** | Tendencia a sentir mais intensamente perdas do que ganhos equivalentes |
| **Custo Irrecuperavel (Sunk Cost)** | Investimento passado que nao deve influenciar decisoes futuras, mas frequentemente influencia |
| **Debiasing** | Conjunto de tecnicas para reduzir ou eliminar o impacto de vieses cognitivos |
| **Disponibilidade** | Heuristica que julga frequencia pela facilidade de recuperacao de exemplos |
| **Dunning-Kruger** | Paradoxo no qual incompetentes superestimam e especialistas subestimam sua habilidade |
| **Efeito Halo** | Contaminacao de avaliacoes por uma caracteristica saliente |
| **Enquadramento (Framing)** | Influencia da apresentacao da informacao sobre a escolha |
| **Heuristica** | Atalho mental que produz julgamento rapido com esforco reduzido |
| **Nudge** | Alteracao sutil no ambiente de escolha que facilita decisoes melhores |
| **Racionalidade Ecologica** | Concepcao de que a racionalidade depende do acoplamento entre heuristica e ambiente |
| **Racionalidade Limitada** | Concepcao de que a cognicao humana e constrangida por recursos finitos |
| **Representatividade** | Heuristica que julga probabilidade por similaridade a prototipos |
| **Sistema 1** | Processamento rapido, automatico, intuitivo |
| **Sistema 2** | Processamento lento, deliberado, analitico |
| **Teoria do Prospecto** | Modelo descritivo de decisao sob risco com funcao de valor em S |
| **Vies de Confirmacao** | Tendencia a buscar e favorecer informacao que confirma crencas existentes |
| **Vies Retrospectivo** | Tendencia a ver eventos passados como mais previsiveis do que foram |

---

## Exercicios e Perguntas de Reflexao

### Exercicio 1: Identificacao de Vieses
Identifique o(s) vies(es) em cada cenario:

a) Maria comprou acoes que subiram 10%. Ela acredita que foi por sua analise brilhante, mas quando as acoes caem 15%, ela atribui ao "mercado irracional".

b) Joao escolhe entre dois planos de saude. Plano A: R/mes, cobre 90% dos procedimentos. Plano B: R/mes, deixa 10% sem cobertura. Ele prefere o B.

c) Uma startup com 3 meses anuncia "revolucao no mercado" com base em feedback de 5 usuarios.

d) Apos uma eleicao, todos dizem "sabia que ia dar nisso", embora as pesquisas indicassem empate tecnico.

### Exercicio 2: Aversao a Perda
Implemente uma simulacao em Python onde um agente escolhe entre ganho certo de R vs. 50% de ganhar R. Depois, perda certa de R vs. 50% de perder R. Use a funcao de valor da Teoria do Prospecto e explique por que a aversao a perda inverte as preferencias.

### Exercicio 3: Nudge Design
Projete tres nudges para um sistema de IA que ajuda usuarios a economizar dinheiro:
1. Baseado em defaults
2. Baseado em feedback social
3. Baseado em enquadramento positivo
Explique qual vies cada um mitiga.

### Exercicio 4: Debate Kahneman vs. Gigerenzer
Um medico precisa decidir se um paciente com sintomas X deve ser internado. A heuristica "se ha febre alta + dor no peito, interne" acerta 80%. Um modelo estatistico com 15 variaveis acerta 85%. Kahneman diria que o modelo e superior. Gigerenzer diria que a heuristica e mais rapida e quase tao boa. Quem esta certo?

### Exercicio 5: Auditoria de Vies
Analise as seguintes falas e proponha contrapontos:
1. "Esse candidato estudou em Harvard, entao deve ser muito competente."
2. "Nunca vi um app feito em Flutter que prestasse."
3. "Minha equipe ja gastou R mil nesse projeto. Nao da para desistir."
4. "O mercado de IA vai crescer 1000% no proximo ano, tenho certeza."

### Questoes de Reflexao

1. **Vieses sao sempre ruins?** Heuristicas sao adaptacoes uteis na maior parte do tempo. Como distinguir quando um vies e um erro vs. quando e uma estrategia eficiente?

2. **Debiasing funciona?** A literatura mostra que treinamento de vieses tem efeitos limitados. Por que e tao dificil "desenviesar" humanos?

3. **Vieses em IA vs. humanos:** Os vieses de sistemas de IA sao fundamentalmente diferentes dos vieses humanos? Eles sao mais perigosos?

4. **Responsabilidade:** Se um sistema de IA comete um erro enviesado, a responsabilidade e do algoritmo, dos dados, dos desenvolvedores ou do usuario?

---

## Referencias e Leituras Recomendadas

### Artigos Seminais
- Kahneman, D., & Tversky, A. (1972). Subjective probability: A judgment of representativeness. *Cognitive Psychology*, 3(3), 430-454.
- Tversky, A., & Kahneman, D. (1973). Availability: A heuristic for judging frequency and probability. *Cognitive Psychology*, 5(2), 207-232.
- Tversky, A., & Kahneman, D. (1974). Judgment under uncertainty: Heuristics and biases. *Science*, 185(4157), 1124-1131.
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263-291.
- Tversky, A., & Kahneman, D. (1981). The framing of decisions and the psychology of choice. *Science*, 211(4481), 453-458.
- Tversky, A., & Kahneman, D. (1983). Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. *Psychological Review*, 90(4), 293-315.

### Artigos sobre Heuristicas e Racionalidade Ecologica
- Gigerenzer, G., & Goldstein, D. G. (1996). Reasoning the fast and frugal way: Models of bounded rationality. *Psychological Review*, 103(4), 650-669.
- Gigerenzer, G., Todd, P. M., & the ABC Research Group (1999). *Simple Heuristics That Make Us Smart*. Oxford University Press.
- Simon, H. A. (1956). Rational choice and the structure of the environment. *Psychological Review*, 63(2), 129-138.

### Artigos sobre Vieses Especificos
- Nickerson, R. S. (1998). Confirmation bias: A ubiquitous phenomenon in many guises. *Review of General Psychology*, 2(2), 175-220.
- Kruger, J., & Dunning, D. (1999). Unskilled and unaware of it. *Journal of Personality and Social Psychology*, 77(6), 1121-1134.
- Englich, B., Mussweiler, T., & Strack, F. (2006). Playing dice with criminal sentences. *Journal of Experimental Social Psychology*, 42(4), 462-475.
- Larrick, R. P. (2004). Debiasing. In D. J. Koehler & N. Harvey (Eds.), *Blackwell Handbook of Judgment and Decision Making*.

### Livros
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Gigerenzer, G. (2007). *Gut Feelings: The Intelligence of the Unconscious*. Viking.
- Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale University Press.
- Ariely, D. (2008). *Predictably Irrational*. HarperCollins.
- Gilovich, T., Griffin, D., & Kahneman, D. (Eds.) (2002). *Heuristics and Biases: The Psychology of Intuitive Judgment*. Cambridge University Press.

### Conexoes no Knowledge Base
- [[04-Conhecimentos/07-Humanidades/Psicologia/Psicologia-Cognitiva|Psicologia Cognitiva]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Teoria-da-Mente|Teoria da Mente]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-em-LLMs|Vieses em LLMs]]
- [[04-Conhecimentos/07-Humanidades/Etica/Conceitos-de-Alinhamento|Conceitos de Etica]]
- [[04-Conhecimentos/07-Humanidades/Filosofia/Conceitos-Fundamentais|Conceitos de Filosofia]]

[[04-Conhecimentos/07-Humanidades/Psicologia/INDEX|← Voltar ao índice de Psicologia]]
