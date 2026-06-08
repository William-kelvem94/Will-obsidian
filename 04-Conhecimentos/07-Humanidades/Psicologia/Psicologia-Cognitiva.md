---
title: "Psicologia Cognitiva e Emoções"
description: "Mapeamento completo dos processos mentais (atenção, memória, percepção, linguagem, tomada de decisão) e inteligência emocional para criar IAs empáticas e interfaces cognitivamente compatíveis."
tags: [psicologia-cognitiva, atencao, memoria, percepcao, linguagem, inteligencia-emocional, empatia, vieses, carga-cognitiva, modelo-atkinson-shiffrin, memoria-trabalho, baddeley, kahneman, sistema-1, sistema-2, atencao-seletiva, sweller]
updated: 2026-05-16
---

# Psicologia Cognitiva e Emoções Humanas

## Índice
1. [[#Introdução — A Mente como Processador de Informação|Introdução]]
2. [[#Modelo de Processamento de Atkinson-Shiffrin|Atkinson-Shiffrin]]
3. [[#Atenção: Seleção e Capacidade Limitada|Atenção]]
4. [[#Memória de Trabalho — O Modelo de Baddeley|Memória de Trabalho]]
5. [[#Modelos Mentais e Esquemas|Modelos Mentais]]
6. [[#Sistema 1 e Sistema 2 — Kahneman e Tversky|Sistema 1 e 2]]
7. [[#Teoria da Carga Cognitiva de Sweller|Carga Cognitiva]]
8. [[#Inteligência Emocional e Empatia em IA|Inteligência Emocional]]
9. [[#Aplicações em IA: Arquiteturas Cognitivas e Atenção|Aplicações em IA]]
10. [[#Glossário|Glossário]]
11. [[#Exercícios e Perguntas de Reflexão|Exercícios]]
12. [[#Referências e Leituras Recomendadas|Referências]]

---

## Introdução — A Mente como Processador de Informação

A Psicologia Cognitiva estuda como os seres humanos adquirem, processam, armazenam e recuperam informações. Inspirada pelo advento dos computadores na década de 1950, a chamada **revolução cognitiva** (Neisser, 1967) substituiu o behaviorismo radical por um modelo no qual a mente é compreendida como um sistema ativo de processamento simbólico.

Diferentemente de um computador digital, porém, o processador humano possui **capacidade limitada**, é **suscetível a interferências emocionais** e opera com **múltiplos canais paralelos** que competem por recursos atencionais. Essas características são fundamentais para o design de interfaces com usuário, sistemas de recomendação e, especialmente, agentes de inteligência artificial que precisam se comunicar de forma empática e eficiente.

### Pressupostos Fundamentais da Psicologia Cognitiva

1. **Processamento ativo:** O organismo não é um receptor passivo de estímulos; ele constrói ativamente representações internas do mundo.
2. **Estruturas de conhecimento:** Informações são organizadas em esquemas, frames e roteiros que guiam a interpretação e a ação.
3. **Natureza hierárquica:** Processos cognitivos ocorrem em múltiplos níveis, desde a detecção sensorial até o raciocínio abstrato.
4. **Limitantes computacionais:** A cognição é constrangida por recursos finitos de atenção, memória de trabalho e tempo de processamento.

Aplicações diretas desses princípios em IA incluem sistemas de [[05-Skills/skills/01-agentic-intelligence/reinforcement-learning|aprendizado por reforço]] que modelam a curiosidade, arquiteturas [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|neurais]] com mecanismos de atenção (Vaswani et al., 2017) e assistentes pessoais que adaptam seu tom com base no estado emocional do usuário.

---

## Modelo de Processamento de Atkinson-Shiffrin

Proposto por Richard Atkinson e Richard Shiffrin em 1968, o **modelo multissistema da memória** (também chamado de *modal model*) estabelece que a informação percorre três estágios sequenciais antes de ser armazenada permanentemente.

### Diagrama do Fluxo

```
Estímulo Sensorial → Memória Sensorial → Atenção → Memória de Curto Prazo → Revisão → Memória de Longo Prazo
                        ↓ (esquecimento)                  ↓ (esquecimento)                  ↓ (esquecimento)
```

### 1. Memória Sensorial

Registra informações dos sentidos por frações de segundo. Possui dois grandes sub-sistemas:

- **Memória Icônica (visual):** Persiste por ~250-500ms. Permite que enxerguemos continuidade no movimento (integração temporal).
- **Memória Ecóica (auditiva):** Persiste por ~2-4 segundos. É por isso que conseguimos "reouvir" mentalmente a última frase de alguém.

Sem atenção, o conteúdo da memória sensorial decai irreversivelmente.

### 2. Memória de Curto Prazo (MCP)

Armazena temporariamente informações por ~15-30 segundos. George Miller (1956) demonstrou que sua capacidade é de **7 ± 2 elementos** (chunks). O *chunking* — agrupamento de informação em unidades significativas — é a principal estratégia para expandir a capacidade efetiva.

Exemplo de chunking:
```
Sequência bruta: 1 9 1 4 1 8 1 8 2 1 8 3 6 2 0 0 0 (17 dígitos)
Sequência chunked: 1914 1818 2183 62000 (4 chunks → Ano da WWI, Ano do Frankenstein, Ano da morte de Beethoven, Salário mínimo atual)
```

### 3. Memória de Longo Prazo (MLP)

Capacidade virtualmente ilimitada com duração de minutos a décadas. Divide-se em:

- **Memória Explícita (Declarativa):** Fatos e eventos.
  - *Episódica:* Eventos autobiográficos (ex.: "meu aniversário de 15 anos").
  - *Semântica:* Conhecimento geral (ex.: "Paris é a capital da França").
- **Memória Implícita (Não-Declarativa):** Habilidades e condicionamento.
  - *Procedural:* Saber andar de bicicleta ou tocar piano.
  - *Priming:* Exposição prévia influencia o processamento posterior.
  - *Condicionamento Clássico:* Associações estímulo-resposta (Pavlov).

### Implicações para IA

- **Janela de contexto vs. MLP:** Modelos como GPT-4 possuem memória de curto prazo muito maior que a humana (128k tokens), mas carecem de um mecanismo nativo de longa duração — daí a necessidade de [[05-Skills/skills/04-knowledge-systems/advanced-rag-strategies|RAG]] (Retrieval-Augmented Generation).
- **Curva de esquecimento de Ebbinghaus:** Humanos esquecem ~50% do conteúdo em 1 hora sem revisão. Um assistente inteligente deve *repetir informações críticas* em vez de assumir que o usuário as lembra.

---

## Atenção: Seleção e Capacidade Limitada

A atenção é o mecanismo que seleciona, dentre o fluxo infinito de estímulos sensoriais, aqueles que serão processados em nível consciente. Três grandes teorias moldaram nossa compreensão:

### Teoria do Filtro Precoce (Broadbent, 1958)

Donald Broadbent propôs que toda informação sensorial entra em um **buffer paralelo**, mas um filtro seletivo bloqueia a maior parte antes do processamento semântico. A seleção é baseada em características físicas (tom de voz, cor, posição espacial).

- **Evidência:** Escuta dicótica (Cherry, 1953) — pessoas não lembram do conteúdo semântico da mensagem ignorada.
- **Problema:** O *cocktail party effect* (Moray, 1959) mostra que o próprio nome pode "passar" pelo filtro, indicando que pelo menos algum processamento semântico ocorre antes da seleção.

### Teoria da Atenuação (Treisman, 1964)

Anne Treisman revisou Broadbent: o filtro não bloqueia, mas **atenua** sinais não- atendidos. Palavras com limiar de ativação baixo (como o próprio nome) conseguem "vazar" e ser percebidas mesmo na mensagem ignorada.

- **Modelo de漏斗:** O estímulo relevante passa com ganho total; os irrelevantes são atenuados, mas não eliminados.

### Modelo de Recursos Múltiplos (Kahneman, 1973)

Daniel Kahneman propôs um **modelo de capacidade central limitada**: a atenção é um recurso único e limitado que pode ser alocado flexivelmente entre tarefas. A alocação depende de:

1. **Arousal (nível de alerta):** Quanto maior o arousal, maior a capacidade total disponível (até um ponto ótimo).
2. **Disposições duradouras:** Automáticas (ex.: orientar-se para um som alto).
3. **Intenções momentâneas:** Metas conscientes e instruções.
4. **Avaliação de demanda:** O sistema monitora o esforço requerido pela tarefa atual.

### Atenção Visual e Busca (Treisman & Gelade, 1980)

A **Teoria da Integração de Atributos** propõe que a atenção focalizada é necessária para *combinar* características visuais isoladas (cor, forma, orientação) em um objeto unificado.

- **Busca em paralelo:** Uma bola vermelha entre bolas azuis é detectada instantaneamente (pré-atentiva).
- **Busca serial:** Uma bola *vermelha* entre bolas azuis e quadrados vermelhos exige atenção focalizada para cada item (busca conjuntiva).

### Implicações para UX e IA

- **Carga atencional:** Interfaces com muitos elementos competem por recursos limitados.
- **Design de prompts:** Informações críticas devem vir no início (prioridade atencional).
- **Assistentes multi-tarefa:** Saber que o usuário está dirigindo exige respostas curtas e auditivas (evitando sobrecarga visual).

```python
# Simulação simplificada do modelo de Kahneman:
# Alocação de recursos atencionais entre tarefas

class ModeloAtencaoKahneman:
    def __init__(self, arousal=0.5):
        self.arousal = arousal  # 0.0 (sono) a 1.0 (pânico)
        self.capacidade_maxima = 0.3 + (arousal * 0.7)
        self.alocacao = {}

    def demanda_total(self, tarefas, demandas):
        """Calcula se a demanda total excede a capacidade disponível."""
        total = sum(demandas.values())
        if total > self.capacidade_maxima:
            print(f"Sobrecarga atencional! Demanda={total:.2f} > Capacidade={self.capacidade_maxima:.2f}")
            return self._priorizar(tarefas, demandas)
        else:
            return {t: d for t, d in demandas.items()}

    def _priorizar(self, tarefas, demandas):
        prioridades = sorted(tarefas, key=lambda t: demandas[t], reverse=True)
        alocadas = {}
        restante = self.capacidade_maxima
        for t in prioridades:
            alocadas[t] = min(demandas[t], restante)
            restante -= alocadas[t]
            if restante <= 0:
                break
        return alocadas

m = ModeloAtencaoKahneman(arousal=0.6)
resultado = m.demanda_total(
    ["dirigir", "ouvir_musica", "conversar"],
    {"dirigir": 0.7, "ouvir_musica": 0.1, "conversar": 0.4}
)
print(resultado)
```

---

## Memória de Trabalho — O Modelo de Baddeley

Alan Baddeley e Graham Hitch (1974) substituíram o conceito unitário de "memória de curto prazo" pelo modelo multicomponente da **memória de trabalho**: um sistema ativo que mantém e manipula informações temporariamente.

### Componentes

#### 1. Executivo Central
Sistema de controle atencional que coordena os subsistemas escravos. Funções:
- Foco e alternância atencional
- Inibição de respostas prepotentes
- Atualização de conteúdo (updating)
- Planejamento de sequências

#### 2. Alça Fonológica
Armazena informação verbal por ~2 segundos. Subdivide-se em:
- **Armazenamento fonológico:** Mantém traços de fala por decaimento temporal.
- **Processo de recapitulação subvocal (rehearsal):** Renova os traços através da repetição interna.

Efeitos clássicos: o **efeito de similaridade fonológica** (palavras que rimam são mais difíceis de lembrar) e o **efeito de extensão da palavra** (palavras longas ocupam mais espaço fonológico).

#### 3. Esboço Visuoespacial
Armazena e manipula informação visual e espacial. Divide-se em:
- **Cache visual:** Formas, cores, texturas.
- **Marcador interno (inner scribe):** Sequências de movimento e localização.

#### 4. Buffer Episódico (Baddeley, 2000)
Adição tardia ao modelo. Integra informação da alça fonológica, do esboço visuoespacial e da memória de longo prazo em uma representação episódica unitária. Capacidade limitada a ~4 chunks.

### Desenvolvimentos Recentes

- **Modelo de recursos contínuos** (Ma et al., 2014): Propõe que a memória de trabalho não tem *slots* discretos, mas recursos contínuos que se distribuem entre itens.
- **Modelo de atenção baseada em estado** (Olshausen et al., 1993): A memória de trabalho emerge de mecanismos atencionais que rotacionam ganhos em representações neurais.

### Aplicações

```python
# Simulação de rehearsals fonológicos na alça fonológica

import time

class AlcaFonologica:
    def __init__(self):
        self.buffer = []
        self.tempo_decaimento = 2.0  # segundos

    def adicionar_item(self, item, timestamp):
        self.buffer.append({"item": item, "timestamp": timestamp})

    def rehearsal(self, timestamp_atual):
        """Recapitulação subvocal: renova itens prestes a decair."""
        renovados = []
        for entry in self.buffer:
            idade = timestamp_atual - entry["timestamp"]
            if idade >= self.tempo_decaimento * 0.8:
                entry["timestamp"] = timestamp_atual  # renova
                renovados.append(entry["item"])
                print(f"Rehearsal: {entry['item']} renovado.")
        return renovados

    def esquecer(self, timestamp_atual):
        """Remove itens cujo traço decaiu completamente."""
        self.buffer = [
            e for e in self.buffer
            if (timestamp_atual - e["timestamp"]) < self.tempo_decaimento
        ]

    def conteudo(self, timestamp_atual):
        self.esquecer(timestamp_atual)
        return [e["item"] for e in self.buffer]

af = AlcaFonologica()
agora = 0.0
itens = ["cachorro", "gato", "elefante", "hipopotamo"]
for i, item in enumerate(itens):
    af.adicionar_item(item, agora + i * 0.5)
print("Conteúdo após 1.8s:", af.conteudo(agora + 1.8))
af.rehearsal(agora + 1.8)
print("Conteúdo após rehearsal:", af.conteudo(agora + 3.0))
```

---

## Modelos Mentais e Esquemas

### Teoria dos Esquemas (Bartlett, 1932; Piaget, 1954)

Frederic Bartlett demonstrou que a memória não é uma cópia fiel da realidade, mas uma **reconstrução** guiada por estruturas internas chamadas *esquemas*. Em seu famoso experimento "A Guerra dos Fantasmas", participantes reconstaram uma história nativa americana distorcendo-a para se adequar a expectativas culturais inglesas.

**Tipos de Esquemas:**
- **Esquemas de objeto:** Atributos típicos de um objeto (ex.: um "pássaro" tem asas, bico, penas).
- **Esquemas de evento (scripts):** Sequências típicas de ações (ex.: "ir ao restaurante" = entrar, sentar, pedir, comer, pagar, sair).
- **Esquemas de papel social:** Expectativas sobre comportamentos de médicos, professores, etc.

### Frames e Roteiros (Minsky, 1975; Schank & Abelson, 1977)

Marvin Minsky formalizou o conceito de **frame** na IA: uma estrutura de dados que representa uma situação estereotipada. Roger Schank estendeu o conceito para **scripts** — sequências causais de eventos.

```python
# Implementação de um script (Schank & Abelson)
class ScriptRestaurante:
    def __init__(self):
        self.papeis = ["cliente", "garcom", "cozinheiro", "caixa"]
        self.cenas = [
            "ENTRADA: cliente entra, escolhe mesa, senta",
            "PEDIDO: garcom traz menu, cliente escolhe, garcom leva pedido",
            "REFECAO: cozinheiro prepara, garcom serve, cliente come",
            "CONTA: garcom traz conta, cliente paga, garcom agradece",
            "SAIDA: pega casaco, sai do restaurante"
        ]

    def executar(self, interrupcao=None):
        print("=== Script: Restaurante ===")
        for cena in self.cenas:
            if interrupcao and interrupcao in cena:
                print(f"[INTERRUPCAO] {cena} -> chamar gerente")
                continue
            print(f"> {cena}")

    def inferir(self, acao):
        """Dada uma ação, infere o script e o papel do ator."""
        if "pedir" in acao.lower():
            return {"script": "restaurante", "papel": "cliente", "prox": "garcom_atende"}
        return None

script = ScriptRestaurante()
script.executar()
```

### Teoria dos Modelos Mentais (Johnson-Laird, 1983)

Philip Johnson-Laird propôs que raciocinamos não com regras lógicas abstratas, mas com **modelos mentais** — representações análogas (não proposicionais) de situações do mundo. Cada modelo mental corresponde a uma possibilidade.

- **Raciocínio dedutivo:** Constroem-se modelos das premissas; a conclusão é a que se mantém em todos os modelos.
- **Falácias:** Ocorrem quando nem todos os modelos possíveis são considerados (falha na *exaustão de modelos*).

### Implicações para Agentes de IA

- **Modelagem do usuário:** O agente deve inferir o modelo mental que o usuário tem do sistema e adaptar as explicações.
- **Detecção de surpresa:** Se o usuário age de forma inconsistente com o modelo inferido, o agente deve revisar seu modelo.
- **Narrativas e personas:** Personagens digitais podem ser implementados como conjuntos de scripts e frames.

---

## Sistema 1 e Sistema 2 — Kahneman e Tversky

Daniel Kahneman e Amos Tversky, a partir da década de 1970, mapearam sistematicamente as heurísticas e vieses que governam o julgamento humano sob incerteza. O trabalho rendeu a Kahneman o Prêmio Nobel de Economia em 2002.

### Arquitetura Dual

**Sistema 1:** Rápido, automático, intuitivo, emocional, associativo.
- Opera sem esforço consciente
- Processa informação em paralelo
- Suscetível a vieses
- Exemplos: Reconhecer um rosto, desviar de um obstáculo, interpretar uma expressão facial

**Sistema 2:** Lento, deliberado, analítico, racional, sequencial.
- Exige atenção voluntária e esforço mental
- Processa informação serialmente
- Capacidade limitada (recursos do executivo central)
- Exemplos: Resolver 27 × 43, estacionar de ré, calcular o imposto de renda

### Heurísticas Clássicas

1. **Heurística da Disponibilidade:** Julgamos a frequência de eventos pela facilidade com que exemplos vêm à mente. Ex.: Pessoas superestimam mortes por acidentes aéreos vs. acidentes de carro porque acidentes aéreos são mais noticiados.

2. **Heurística da Representatividade:** Julgamos a probabilidade de A pertencer à categoria B pelo grau de similaridade entre A e o protótipo de B. Ex.: "João é meticuloso e organizado. Ele é bibliotecário ou vendedor?" — a maioria responde bibliotecário, ignorando a base rate (muito mais vendedores que bibliotecários).

3. **Heurística da Ancoragem e Ajuste:** Estimativas numéricas são influenciadas por um valor inicial (âncora), mesmo que arbitrário. Ex.: Juízes que rolam dados com valor alto dão sentenças mais longas (Englich et al., 2006).

### Teoria do Prospecto (Kahneman & Tversky, 1979)

Alternativa à teoria da utilidade esperada. Postula que:

- As pessoas **enquadram** ganhos e perdas relativamente a um ponto de referência
- A função de valor é **côncava para ganhos** (aversão ao risco) e **convexa para perdas** (busca de risco)
- **Aversão à perda:** Perder dói ~2× mais do que ganhar alegra

```python
# Função de valor da Teoria do Prospecto
import math

def valor_prospecto(x, lam=2.25, alpha=0.88, beta=0.88):
    """
    x: desvio do ponto de referência (positivo = ganho, negativo = perda)
    lam: coeficiente de aversão à perda (~2.25)
    alpha: coeficiente de sensibilidade a ganhos
    beta: coeficiente de sensibilidade a perdas
    """
    if x >= 0:
        return x ** alpha
    else:
        return -lam * ((-x) ** beta)

# Exemplo: ganhar R$50 vs. perder R$50
print(f"Valor de ganhar R$50: {valor_prospecto(50):.2f}")
print(f"Valor de perder R$50: {valor_prospecto(-50):.2f}")
print(f"Aversão: {abs(valor_prospecto(-50) / valor_prospecto(50)):.2f}x")
```

### Implicações para o Design de Agentes

- **System 1 boosting:** Quando o usuário está sob estresse, o agente deve fornecer respostas que ativem o Sistema 1 (simples, diretas, intuitivas) em vez de exigir análise do Sistema 2.
- **Debiasing:** O agente pode atuar como *nudge* (Thaler & Sunstein, 2008), oferecendo contra-argumentos a vieses identificados.
- **Framing:** A IA deve ser neutra na apresentação de opções para não enviesar a decisão do usuário.

---

## Teoria da Carga Cognitiva de Sweller

John Sweller (1988) desenvolveu a Teoria da Carga Cognitiva (*Cognitive Load Theory* — CLT) para explicar como as limitações da memória de trabalho afetam a aprendizagem. A CLT é uma das teorias mais influentes em design instrucional e pode ser diretamente aplicada ao design de interações com IA.

### Tipos de Carga Cognitiva

#### 1. Carga Intrínseca (*Intrinsic Load*)
Imposta pela complexidade inerente do material. Depende do número de elementos que precisam ser processados simultaneamente na memória de trabalho (interatividade entre elementos).

- *Exemplo baixa carga intrínseca:* Aprender vocabulário em inglês (elementos independentes).
- *Exemplo alta carga intrínseca:* Aprender a sintaxe de um compilador (elementos altamente interconectados).

#### 2. Carga Estranha (*Extraneous Load*)
Imposta pela forma como a informação é apresentada ao aprendiz. É **contraproducente** — deve ser minimizada.

- Causas: Instruções mal formatadas, informação redundante, navegação confusa, split-attention (informação relacionada em locais separados).

#### 3. Carga Relevante (*Germane Load*)
Imposta pelo esforço mental dedicado à construção e automação de esquemas na memória de longo prazo. É **desejável** — deve ser maximizada.

- Exemplos: Elaboração, prática variada, auto-explicação.

### Efeitos da CLT

| Efeito | Descrição | Aplicação em IA |
|--------|-----------|-----------------|
| **Atenção dividida** | Informação distribuída em múltiplas fontes aumenta carga estranha | Respostas em bloco único com seções hierárquicas |
| **Modalidade** | Informação visual + auditiva é melhor que apenas visual com texto | Assistentes de voz podem complementar, não repetir, informação visual |
| **Redundância** | Informação idêntica em múltiplos formatos prejudica | Evitar narrar exatamente o que está escrito na tela |
| **Efeito de expertise** | Novatos precisam instrução direta; experts preferem mínima orientação | Adaptar o nível de detalhe ao usuário |
| **Exemplo trabalhado** | Novatos aprendem mais com exemplos resolvidos do que resolvendo problemas | Assistente que mostra soluções completas e depois pede prática |

### Carga Cognitiva no Design de Prompts

```python
class PromptOptimizer:
    """
    Aplica princípios da CLT para estruturar respostas de LLMs.
    """
    def __init__(self, nivel_usuario="iniciante", urgencia=0.0):
        self.nivel = nivel_usuario
        self.urgencia = urgencia

    def estruturar_resposta(self, explicacao, codigo, sumario=None):
        if self.urgencia > 0.7:
            return self._formato_tldr(explicacao, codigo)
        elif self.nivel == "iniciante":
            return self._formato_exemplo_trabalhado(explicacao, codigo)
        else:
            return self._formato_expert(sumario, codigo)

    def _formato_tldr(self, explicacao, codigo):
        return {
            "summary": f"**TL;DR:** {explicacao[:280]}...",
            "detalhes": f"<details><summary>Ver código</summary>\n\n```python\n{codigo}\n```\n</details>"
        }

    def _formato_exemplo_trabalhado(self, explicacao, codigo):
        return {
            "passo1": f"### 1. Problema\n{explicacao.split('.')[0]}.",
            "passo2": f"### 2. Solução\n```python\n{codigo}\n```",
            "passo3": f"### 3. Explicação linha a linha\n{self._explicar_linhas(codigo)}"
        }

    def _explicar_linhas(self, codigo):
        linhas = codigo.strip().split('\n')
        explicacoes = []
        for i, linha in enumerate(linhas, 1):
            if linha.strip() and not linha.strip().startswith('#'):
                explicacoes.append(f"**Linha {i}:** `{linha.strip()}` - (explicação contextual)")
        return '\n'.join(explicacoes[:5]) + '\n...'

optimizer = PromptOptimizer(nivel_usuario="iniciante")
print(optimizer.estruturar_resposta(
    "A função map aplica uma função a cada item de um iterável.",
    "list(map(str, [1, 2, 3]))"
))
```

---

## Inteligência Emocional e Empatia em IA

### Modelo de Daniel Goleman (1995)

Daniel Goleman popularizou o conceito de Inteligência Emocional, organizando-a em cinco domínios:

1. **Autoconsciência:** Reconhecer as próprias emoções no momento em que ocorrem.
2. **Autorregulação:** Gerenciar emoções para facilitar a tarefa em vez de interferir.
3. **Motivação:** Usar emoções para perseguir metas com persistência.
4. **Empatia:** Reconhecer emoções nos outros e sintonizar-se com elas.
5. **Habilidades Sociais:** Gerenciar relacionamentos e construir rapport.

### Empatia Cognitiva vs. Empatia Afetiva

- **Empatia Cognitiva (Theory of Mind):** Compreender o estado mental do outro — o que ele pensa, sente e acredita. Relaciona-se à [[04-Conhecimentos/07-Humanidades/Psicologia/Teoria-da-Mente|Teoria da Mente]].
- **Empatia Afetiva:** Compartilhar a experiência emocional do outro — sentir com ele.
- **Preocupação Empática (Compassion):** Sentir preocupação pelo bem-estar do outro sem necessariamente sentir a mesma emoção.

Para IAs, a **empatia cognitiva** é viável e útil; a **empatia afetiva** é simulada (a IA não *sente*, mas pode *expressar* compreensão emocional).

### Framework de Resposta Empática

```python
import re

class DetectorEmocional:
    """
    Detecta pistas emocionais no texto do usuário e adapta o tom da resposta.
    Baseado em análise lexical simples de palavras emocionais.
    """
    def __init__(self):
        self.emocoes = {
            "frustracao": [
                r"\b(puto|odi[eo]|infernal|horr[ií]vel|droga|merda|cansad[ao])\b",
                r"\b(n[aã]o\s+funciona|quebrou|bugou|péssimo)\b"
            ],
            "urgencia": [
                r"\b(urgente|corre|ajuda|socorro|preciso\s+agora|quanto\s+antes)\b"
            ],
            "confusao": [
                r"\b(n[aã]o\s+entendo|confus[ao]|n[aã]o\s+sei|como\s+assim)\b"
            ],
            "satisfacao": [
                r"\b(obrigad[ao]|funcionou|valeu|ótimo|perfeito|show)\b"
            ]
        }

    def detectar(self, texto):
        scores = {}
        for emocao, padroes in self.emocoes.items():
            score = sum(
                bool(re.search(p, texto.lower()))
                for p in padroes
            )
            if score > 0:
                scores[emocao] = score
        return scores

    def responder(self, texto_usuario):
        estado = self.detectar(texto_usuario)
        if "frustracao" in estado:
            return {
                "tom": "empatico_rapido",
                "mensagem": "Entendo sua frustração. Vamos resolver isso juntos.",
                "prioridade": "alta"
            }
        elif "urgencia" in estado:
            return {
                "tom": "direto",
                "mensagem": "Vou direto ao ponto para resolver isso rapidamente.",
                "prioridade": "altissima"
            }
        elif "confusao" in estado:
            return {
                "tom": "didatico",
                "mensagem": "Deixe-me explicar de forma mais clara.",
                "prioridade": "media"
            }
        return {
            "tom": "neutro",
            "mensagem": None,
            "prioridade": "baixa"
        }

detector = DetectorEmocional()
print(detector.responder("Tô preso nesse bug infernal faz 5 horas, pelo amor de deus me ajuda"))
```

### Assimetria Emocional

A maior força de um agente artificial em interações emocionais é a **assimetria emocional**: enquanto o usuário pode estar frustrado, ansioso ou irritado, o agente mantém-se calmo, racional e construtivo. Essa estabilidade funciona como uma âncora de regulação, ajudando o usuário a transitar do Sistema 1 (reativo) para o Sistema 2 (reflexivo).

---

## Aplicações em IA: Arquiteturas Cognitivas e Atenção

### Arquiteturas Cognitivas

Uma arquitetura cognitiva é a estrutura fundamental de um sistema inteligente que especifica os componentes de memória, os processos de aprendizagem e os mecanismos de percepção/ação. Três arquiteturas clássicas são particularmente relevantes:

#### ACT-R (Adaptive Control of Thought — Rational)
Desenvolvida por John Anderson (1993) na Carnegie Mellon University.
- **Módulos:** Visual, manual, declarativo, procedural, intencional.
- **Produções:** Regras IF-THEN que disparam quando condições são satisfeitas.
- **Memória declarativa:** Chunks ativados por um mecanismo de espalhamento de ativação baseado em frequência e recência.
- **Equação de ativação:** `A_i = B_i + Σ_j W_j S_ji + ε`
  - `B_i`: ativação basal (recência/frequência)
  - `W_j`: peso do contexto
  - `S_ji`: força de associação
  - `ε`: ruído

#### SOAR (State-Operator-And-Result)
Desenvolvida por John Laird, Allen Newell e Paul Rosenbloom (1987).
- **Arquitetura unificada:** Um único mecanismo para todos os comportamentos cognitivos.
- **Impasses:** Quando o conhecimento não é suficiente para resolver um problema, SOAR cria um subestado e busca resolver o impasse.
- **Chunking:** Mecanismo de aprendizado que compila soluções de subproblemas em regras permanentes.

#### Nengo e o Neural Engineering Framework (NEF)
- Modelos baseados em populações de neurônios spiking.
- Utilizados para simular circuitos neurais em larga escala (Spaun, Eliasmith et al., 2012).

### Mecanismos de Atenção em Redes Neurais

Inspirados na atenção seletiva humana, mecanismos de atenção em deep learning permitem que o modelo pondere seletivamente partes da entrada:

#### Attention Mechanism (Bahdanau et al., 2014)
```python
# Implementação conceitual de attention (Bahdanau)
import numpy as np

def attention_score(query, keys, values):
    """
    query: vetor decodificador atual (d_model)
    keys:  vetores codificadores (n_src, d_model)
    values: vetores de valor (n_src, d_model)
    """
    scores = np.dot(keys, query) / np.sqrt(len(query))  # scaled dot-product
    weights = np.exp(scores) / np.sum(np.exp(scores))    # softmax
    context = np.dot(weights, values)
    return context, weights

# Exemplo com dimensões reduzidas
query = np.array([1.0, 0.0, 1.0])
keys = np.array([[0.8, 0.2, 0.5], [0.1, 0.9, 0.3], [0.6, 0.4, 0.7]])
values = np.array([[1.0, 0.0], [0.0, 1.0], [0.5, 0.5]])

context, attn_weights = attention_score(query, keys, values)
print("Attention weights:", attn_weights)
print("Context vector:", context)
```

#### Self-Attention e Transformers (Vaswani et al., 2017)

O mecanismo de **self-attention** é a base dos Transformers — arquitetura dos modelos GPT, BERT, Claude, LLaMA e Gemini.

```
Attention(Q, K, V) = softmax(QK^T / √d_k) V
```

Onde Q, K e V são projeções lineares da mesma sequência de entrada. A divisão por √d_k (scaling) evita que gradientes fiquem muito pequenos.

#### Atenção Multi-cabeça (*Multi-Head Attention*)

Permite que o modelo aprenda diferentes tipos de relações atencionais em paralelo:

```
MultiHead(Q, K, V) = Concat(head_1, ..., head_h) W_O
head_i = Attention(Q W_i^Q, K W_i^K, V W_i^V)
```

### Aplicações Diretas

1. **Sistemas de Diálogo:** Atenção sobre o histórico da conversa (como a memória de trabalho humana).
2. **Resumo de Texto:** Atenção sobre sentenças relevantes (como a atenção seletiva humana).
3. **Tradução Automática:** Alinhamento entre palavras fonte e alvo.
4. **RAG:** Atenção entre a consulta e documentos recuperados.
5. **Modelagem do Usuário:** [[05-Skills/skills/01-agentic-intelligence/autonomous-workflow|Agentes reativos]] que ponderam informações contextuais sobre o usuário.

---

## Glossário

| Termo | Definição |
|-------|-----------|
| **Atenção Seletiva** | Mecanismo que filtra estímulos irrelevantes para focar em informações relevantes |
| **Alça Fonológica** | Componente da memória de trabalho de Baddeley responsável por informação verbal |
| **Carga Cognitiva** | Demanda imposta à memória de trabalho durante o processamento de informação |
| **Chunking** | Agrupamento de unidades de informação em blocos significativos |
| **Efeito de Posição Serial** | Tendência a lembrar melhor do primeiro (primazia) e do último (recência) item de uma lista |
| **Esquema** | Estrutura mental que organiza conhecimento sobre um conceito ou evento |
| **Esboço Visuoespacial** | Componente da memória de trabalho para informação visual e espacial |
| **Heurística** | Estratégia mental simplificada que produz julgamentos rápidos, mas potencialmente enviesados |
| **Memória de Trabalho** | Sistema de capacidade limitada que mantém e manipula informação temporariamente |
| **Modelo Mental** | Representação interna análoga à situação descrita |
| **Priming** | Ativação implícita de conceitos por exposição prévia |
| **Rehearsal** | Recapitulação subvocal para manter informação na alça fonológica |
| **Sistema 1** | Processamento rápido, automático, intuitivo e emocional |
| **Sistema 2** | Processamento lento, deliberado, analítico e racional |
| **Teoria da Carga Cognitiva** | Teoria instrucional baseada nas limitações da memória de trabalho |
| **Viés de Confirmação** | Tendência a buscar e interpretar informações que confirmam crenças pré-existentes |

---

## Exercícios e Perguntas de Reflexão

### Exercício 1: Mapeamento de Modelos
**Questão:** Dado o seguinte trecho de interação, identifique qual(is) componente(s) do modelo de Baddeley está(ão) sendo utilizado(s) e explique por que:

"O usuário pede ao assistente: 'Preciso comparar o PIB de Brasil, Argentina, Chile e Uruguai dos últimos 5 anos.' O assistente apresenta uma tabela."

### Exercício 2: Simulação de Atenção
Implemente uma simulação do modelo de atenção de Treisman (atenuação) em Python, onde palavras com baixo limiar (nome próprio, alarmes) passam pelo filtro mesmo na mensagem ignorada.

### Exercício 3: Análise de Carga Cognitiva
Analise o seguinte prompt de um assistente de IA e identifique fontes de carga estranha (extraneous load). Reescreva-o seguindo os princípios da CLT:

"Então, basicamente, o que acontece é que, como você deve saber, a função map em Python, que é uma função de ordem superior incorporada na linguagem, recebe como primeiro argumento uma função e como segundo argumento um iterável — e ela é útil para transformar dados, mas existem alternativas como list comprehensions que são consideradas mais pitônicas, enfim, depende do caso..."

### Exercício 4: Debiasing
Considere a seguinte situação: um usuário diz "Tenho certeza que esse time vai perder, eles nunca ganham fora de casa".
Identifique os vieses envolvidos e escreva uma resposta do assistente que:
1. Valide emocionalmente o usuário
2. Ofereça uma perspectiva alternativa sem invalidar a opinião

### Exercício 5: Arquiteturas Cognitivas
Compare ACT-R e Transformers ao responder:
- Como cada um lida com o trade-off entre capacidade de memória e velocidade?
- Qual mecanismo de aprendizado cada um possui?
- Em que tipo de tarefa cada um se destaca?

### Questões de Reflexão

1. **Atkinson-Shiffrin vs. Baddeley:** Em que aspectos o modelo de Baddeley é uma melhoria em relação ao modelo original de Atkinson-Shiffrin? Que fenômenos o primeiro explica que o segundo não consegue?

2. **Atenção em Humanos vs. Transformers:** A self-attention dos Transformers é um bom modelo da atenção humana? Quais são as diferenças fundamentais?

3. **Carga Cognitiva e LLMs:** Como o conceito de "carga cognitiva" pode ser estendido ao design de interações com modelos de linguagem? Um prompt muito longo aumenta a "carga cognitiva" do LLM?

4. **Sistema 1 na IA:** IAs como GPT-4 são predominantemente Sistemas 1 ou Sistemas 2? Ou a dicotomia não se aplica a sistemas neurais?

5. **Empatia Simulada:** Até que ponto uma IA que simula empatia pode ser considerada eticamente responsável? A empatia simulada é enganosa ou útil?

---

## Referências e Leituras Recomendadas

### Artigos Seminais
- Atkinson, R. C., & Shiffrin, R. M. (1968). Human memory: A proposed system and its control processes. *Psychology of Learning and Motivation*, 2, 89–195.
- Baddeley, A. D., & Hitch, G. (1974). Working memory. *Psychology of Learning and Motivation*, 8, 47–89.
- Baddeley, A. D. (2000). The episodic buffer: a new component of working memory? *Trends in Cognitive Sciences*, 4(11), 417–423.
- Broadbent, D. E. (1958). *Perception and Communication*. Pergamon Press.
- Kahneman, D. (1973). *Attention and Effort*. Prentice-Hall.
- Kahneman, D., & Tversky, A. (1979). Prospect theory: An analysis of decision under risk. *Econometrica*, 47(2), 263–292.
- Miller, G. A. (1956). The magical number seven, plus or minus two. *Psychological Review*, 63(2), 81–97.
- Neisser, U. (1967). *Cognitive Psychology*. Appleton-Century-Crofts.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science*, 12(2), 257–285.
- Treisman, A. M. (1964). Selective attention in man. *British Medical Bulletin*, 20(1), 12–16.
- Treisman, A. M., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97–136.
- Vaswani, A. et al. (2017). Attention is all you need. *Advances in Neural Information Processing Systems*, 30.

### Livros
- Anderson, J. R. (1993). *Rules of the Mind*. Lawrence Erlbaum.
- Eysenck, M. W., & Keane, M. T. (2015). *Cognitive Psychology: A Student's Handbook* (7th ed.). Psychology Press.
- Goleman, D. (1995). *Emotional Intelligence: Why It Can Matter More Than IQ*. Bantam Books.
- Johnson-Laird, P. N. (1983). *Mental Models: Towards a Cognitive Science of Language, Inference, and Consciousness*. Harvard University Press.
- Kahneman, D. (2011). *Thinking, Fast and Slow*. Farrar, Straus and Giroux.
- Laird, J. E. (2012). *The Soar Cognitive Architecture*. MIT Press.
- Schank, R. C., & Abelson, R. P. (1977). *Scripts, Plans, Goals, and Understanding*. Lawrence Erlbaum.
- Thaler, R. H., & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. Yale University Press.

### Conexões no Knowledge Base
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-Cognitivos|Vieses Cognitivos]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Teoria-da-Mente|Teoria da Mente]]
- [[04-Conhecimentos/07-Humanidades/Psicologia/Vieses-em-LLMs|Vieses em LLMs]]
- [[05-Skills/skills/01-agentic-intelligence/reinforcement-learning|Aprendizado por Reforço]]
- [[04-Conhecimentos/07-Humanidades/Neurociencia/Redes-Neurais-Biologicas|Redes Neurais]]
- [[05-Skills/skills/04-knowledge-systems/advanced-rag-strategies|Retrieval-Augmented Generation]]
- [[05-Skills/skills/01-agentic-intelligence/autonomous-workflow|Agentes Reativos]]

[[04-Conhecimentos/07-Humanidades/Psicologia/INDEX|← Voltar ao índice de Psicologia]]
