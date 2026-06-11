---
title: "Cronologia da Inteligência Artificial"
area: "Computacao"
tags: [conhecimento, conceito, ia, machine-learning, deep-learning, historia, cronologia, transformers]
related: ["Ciencia-da-Computacao", "Machine-Learning-Fundamentos", "Redes-Neurais", "Filosofia-da-Mente"]
aliases: ["AI Timeline", "História da IA", "História da Inteligência Artificial"]
created: 2026-05-19
updated: 2026-05-19
---

# Cronologia da Inteligência Artificial

## 1940–1959: Nascimento da IA

### 1943 — McCulloch & Pitts: Modelo de Neurônio Artificial
Warren McCulloch (neurofisiologista) e Walter Pitts (matemático) publicam **"A Logical Calculus of Ideas Immanent in Nervous Activity"** no *Bulletin of Mathematical Biophysics*. Propõem o primeiro modelo matemático de um neurônio artificial — uma unidade binária com limiar (threshold logic unit) capaz de computar funções lógicas (AND, OR, NOT). Este artigo funda a lógica neural e inspira diretamente o perceptron e toda a neurociência computacional.

- Publicação: McCulloch, W. S. & Pitts, W. (1943). *Bull. Math. Biophys.* 5, 115–133.
- Significado: Primeiro modelo formal de computação neural; demonstra que redes de neurônios podem computar qualquer função lógica.

### 1950 — Alan Turing: "Computing Machinery and Intelligence"
Publicado na revista *Mind*, Turing propõe a pergunta "Can machines think?" e introduz o **Jogo da Imitação** (Teste de Turing) como critério operacional para inteligência de máquina. O artigo antecipa objeções filosóficas (teológica, cabeças-de-avestruz, matemática, argumento da consciência, etc.) e refuta cada uma.

- Publicação: Turing, A. M. (1950). *Mind* 59(236), 433–460.
- Significado: Fundação filosófica e operacional da IA; define o debate sobre máquinas pensantes que persiste até hoje.

### 1951 — SNARC: Primeira Rede Neural Implementada
Marvin Minsky, então estudante em Princeton, constrói o **Stochastic Neural Analog Reinforcement Calculator (SNARC)** — uma máquina de 3000 tubos de vácuo e 40 neurônios artificiais com pesos ajustáveis manualmente. Simula uma rede neural que aprende a atravessar um labirinto por reforço estocástico.

- Significado: Primeira implementação física de uma rede neural; precursora do reinforcement learning.
- Curiosidade: Minsky usava conexões de bombardeiros B-24 descartados.

### 1956 — Dartmouth Conference: O Termo "Inteligência Artificial"
John McCarthy (então em Dartmouth), Marvin Minsky (Harvard), Nathaniel Rochester (IBM) e Claude Shannon (Bell Labs) organizam o **Dartmouth Summer Research Project on Artificial Intelligence** (junho–agosto de 1956). A proposta de McCarthy cunha o termo "Artificial Intelligence":

> "The study is to proceed on the basis of the conjecture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."

Participantes incluem Allen Newell, Herbert Simon, Arthur Samuel, Oliver Selfridge, Ray Solomonoff. Newell e Simon apresentam o **Logic Theorist** — considerado o primeiro programa de IA — capaz de provar teoremas de *Principia Mathematica* (Russell & Whitehead).

- Significado: Nascimento oficial da IA como campo de pesquisa acadêmica.
- Resultados: Logic Theorist, programa de damas de Samuel, primeiras discusses sobre raciocínio automatizado.

### 1957 — Perceptron: Frank Rosenblatt
Frank Rosenblatt (Cornell) desenvolve o **Perceptron Mark I** — uma máquina de reconhecimento de padrões baseada no neurônio de McCulloch-Pitts com pesos ajustáveis por aprendizado supervisionado. O Mark I era um hardware analógico de 400 fotocélulas conectadas a 512 motores potenciométricos.

- Publicação: Rosenblatt, F. (1958). *Psychological Review* 65(6), 386–408.
- Significado: Primeiro classificador neural prático; gera enorme entusiasmo na mídia (o *New York Times* chamou de "embrião de um cérebro eletrônico").

### 1958 — Lisp: Linguagem da IA
John McCarthy cria o **Lisp** (List Processor) no MIT. Primeira linguagem funcional de alto nível; introduz garbage collection, recursion, estruturas de listas como representação universal de dados e código.

- Significado: Linguagem dominante da pesquisa em IA por décadas (até o Python moderno).
- Influência: Lisp machines, sistemas expertos, processamento simbólico.

### 1959 — Arthur Samuel: "Machine Learning"
Arthur Samuel (IBM) publica **"Some Studies in Machine Learning Using the Game of Checkers"** — seu programa de damas aprende por auto-jogo (*self-play*) usando técnicas que hoje chamamos de reinforcement learning com avaliação de função heurística.

- Publicação: Samuel, A. L. (1959). *IBM Journal of Research and Development* 3(3), 210–229.
- Significado: Cunha o termo **"machine learning"**; primeiro sistema que aprende com experiência sem programação explícita.

---

## 1960–1979: Primeiros Avanços e Invernos da IA

### 1961 — Unimate: Primeiro Robô Industrial
George Devol e Joseph Engelberger instalam o **Unimate #001** na fábrica da General Motors em Trenton, Nova Jersey. Braço hidráulico de 1800 kg que realizava soldagem por ponto e manuseio de peças fundidas.

- Significado: Início da robótica industrial; marco da automação fabril.
- Legado: Engelberger é considerado o "pai da robótica industrial".

### 1964 — ELIZA: Processamento de Linguagem Natural
Joseph Weizenbaum (MIT) cria **ELIZA** — programa de conversação que simula um psicoterapeuta rogeriano. Usa reconhecimento de padrões e substituição de palavras-chave para gerar respostas aparentemente naturais.

- Publicação: Weizenbaum, J. (1966). *Communications of the ACM* 9(1), 36–45.
- Significado: Primeiro chatbot; demonstra o poder da ilusão linguística (Efeito ELIZA — pessoas atribuem consciência a programas simples).
- Curiosidade: A versão mais famosa, DOCTOR, foi considerada perturbadoramente convincente; Weizenbaum tornou-se crítico da IA.

### 1966 — Shakey: Primeiro Robô Móvel com Raciocínio
SRI International cria **Shakey** — robô móvel que combinava visão, planejamento (STRIPS) e navegação em ambiente controlado. Usava lógica de primeira ordem para raciocinar sobre ações.

- Significado: Primeiro sistema robótico integrado (visão + planejamento + controle); precursor do *intelligent agent*.
- Contribuições: Desenvolvimento do algoritmo A* (Hart, Nilsson, Raphael, 1968) e STRIPS (Fikes & Nilsson, 1971).

### 1969 — Minsky & Papert: "Perceptrons" e o Primeiro Inverno
Marvin Minsky e Seymour Papert publicam **"Perceptrons: An Introduction to Computational Geometry"** — demonstram matematicamente que o perceptron simples (camada única) não pode aprender funções não-linearmente separáveis (como XOR). Embora o livro não desconsidere redes multicamadas, seu tom pessimista e a demonstração formal das limitações do perceptron simples causam um efeito devastador.

- Publicação: Minsky, M. & Papert, S. (1969). MIT Press.
- Significado: Congela o financiamento de redes neurais por quase uma década; inaugura o **Primeiro Inverno da IA**.

### 1970 — MYCIN: Sistema Especialista em Diagnóstico Médico
Edward Feigenbaum (Stanford) lidera o desenvolvimento de **MYCIN** — sistema especialista que diagnostica infecções bacterianas no sangue e recomenda antibióticos. Usa ~450 regras (SE-ENTÃO) e raciocínio com incerteza (fatores de certeza).

- Significado: Demonstra que sistemas baseados em regras podem igualar ou superar médicos em domínios restritos.
- Performance: 69% de acurácia vs. 80% de especialistas; melhor que médicos não-especialistas.
- Limitação: MYCIN nunca foi usado na prática por questões éticas e legais.

### 1972 — PROLOG: Programação em Lógica
Alain Colmerauer e Robert Kowalski desenvolvem **PROLOG** (PROgrammation en LOGique) — linguagem baseada em lógica de primeira ordem e resolução SLD. Usa fatos, regras e consultas, com busca por backtracking.

- Significado: Linguagem dominante em IA simbólica e processamento de linguagem natural no Japão e Europa; base do projeto japonês **Fifth Generation Computer Systems** (década de 1980).

### 1974 — Shakey: Planejamento STRIPS
Richard Fikes e Nils Nilsson (SRI) formalizam **STRIPS** (Stanford Research Institute Problem Solver) — linguagem de representação de estados, ações e metas. Cada ação tem pré-condições e efeitos (add/delete lists).

- Publicação: Fikes, R. E. & Nilsson, N. J. (1971). *Artificial Intelligence* 2(3–4), 189–208.
- Significado: Fundação do planejamento automatizado; influencia até hoje (PDDL, planners modernos).

### 1974–1980: Primeiro Inverno da IA

Causas:
- **Relatório Lighthill** (1973): Sir James Lighthill publica uma crítica devastadora à pesquisa britânica em IA, concluindo que "em nenhuma parte do campo as descobertas feitas até agora produziram o grande impacto prometido". O governo britânico corta todo o financiamento de IA (exceto em algumas universidades).
- Minsky & Papert (1969) demonstram limitações do perceptron.
- Promessas não cumpridas: tradução automática, robôs domésticos, compreensão de linguagem natural.
- **DARPA** reduz drasticamente o financiamento nos EUA.

Consequências:
- Pesquisa em redes neurais praticamente para.
- Laboratórios de IA são fechados ou renomeados.
- Êxodo de pesquisadores para outras áreas.

---

## 1980–1999: Sistemas Especialistas e Redes Neurais

### 1980 — XCON: Sistema Especialista Comercial
**XCON** (eXpert CONfigurer) é implantado na DEC (Digital Equipment Corporation) para configurar sistemas VAX. Usando ~10.000 regras, XCON economiza ~$40 milhões/ano para a DEC.

- Significado: Primeiro grande sucesso comercial de sistemas especialistas; gera a "AI Industry" com empresas como IntelliCorp, Teknowledge, Inference.
- Lição: Manutenção de regras mostrou-se cara e frágil; base de conhecimento tornou-se difícil de gerenciar com o tempo.

### 1982 — Hopfield Networks
John Hopfield (Caltech) publica **"Neural networks and physical systems with emergent collective computational abilities"** — propõe redes recorrentes com energia decrescente (Lyapunov) que funcionam como memória associativa.

- Publicação: Hopfield, J. J. (1982). *PNAS* 79(8), 2554–2558.
- Significado: Renova o interesse em redes neurais ao mostrar que modelos físicos (spin glasses) podem computar.

### 1986 — Backpropagation: Rumelhart, Hinton, Williams
**"Learning representations by back-propagating errors"** publicado na *Nature*. David Rumelhart, Geoffrey Hinton e Ronald Williams demonstram que o algoritmo de retropropagação (backpropagation) — combinando gradiente descendente com a regra da cadeia — permite treinar redes neurais multicamadas.

- Publicação: Rumelhart, D. E., Hinton, G. E. & Williams, R. J. (1986). *Nature* 323, 533–536.
- Significado: Revoluciona o treinamento de redes neurais; torna possível aprender funções complexas (XOR, reconhecimento de padrões).
- Nota: O algoritmo foi descoberto independentemente por várias pessoas (Werbos 1974, Parker 1985, LeCun 1985).

### 1987–1993: Segundo Inverno da IA

Causas:
- **Mercado de Lisp Machines colapsa**: Empresas como Symbolics, LMI e Texas Instruments falem quando hardware genérico (SUN, Apple Mac) supera máquinas Lisp dedicadas.
- **Sistemas Especialistas falham**: Manutenção de regras exponencial, falta de senso comum (CYRC — Cyc de Lenat tenta capturar todo o "conhecimento comum" com verba bilionária), rigidez.
- **Fifth Generation Computer Project japonês** falha em produzir resultados significativos após investimento de $400M.
- **AI Winter**: DARPA corta financiamento; Stanford's SAIL e MIT AI Lab perdem recursos.

### 1988 — Q-Learning: Watkins
Chris Watkins (Cambridge) propõe o **Q-Learning** — algoritmo de reinforcement learning off-policy que aprende a função valor-ação ótima (Q*) sem modelo do ambiente.

- Publicação: Watkins, C. J. C. H. (1989). *Learning from Delayed Rewards* (PhD thesis, Cambridge).
- Significado: Fundação do RL moderno — sem necessidade de modelo da dinâmica, converge para a política ótima.

### 1989 — LeNet: CNNs para Reconhecimento de Dígitos
Yann LeCun (Bell Labs) publica **"Backpropagation Applied to Handwritten Zip Code Recognition"** — aplica backpropagation em redes convolucionais para ler códigos postais manuscritos. Usa convolução, subamostragem (pooling) e camadas totalmente conectadas.

- Publicação: LeCun, Y. et al. (1989). *Neural Computation* 1(4), 541–551.
- Significado: Primeira CNN prática; inventa arquitetura que domina visão computacional até hoje.
- Aplicação: Usado pelo US Postal Service e bancos americanos nos anos 1990.

### 1995 — Support Vector Machines (SVM)
Vladimir Vapnik e Corinna Cortes (Bell Labs) publicam o artigo seminal sobre **Support Vector Networks** — classificador de margem máxima com kernel trick para mapear dados a espaços de alta dimensão.

- Publicação: Cortes, C. & Vapnik, V. (1995). *Machine Learning* 20(3), 273–297.
- Significado: SVM torna-se o estado-da-arte em classificação por uma década; supera redes neurais em muitas tarefas até o deep learning.
- Conceito-chave: Kernel trick permite separação não-linear sem custo computacional explícito.

### 1997 — Deep Blue: Computador vence Kasparov
**Deep Blue** (IBM) derrota Garry Kasparov (campeão mundial de xadrez) em uma partida de 6 jogos (3.5–2.5). Deep Blue era um supercomputador RS/6000 SP com 30 nós P2SC e 480 chips VLSI especializados, avaliando ~200 milhões de posições/segundo.

- Significado: Primeira vez que uma máquina vence o campeão mundial de xadrez em match completo.
- Impacto: Momento de grande visibilidade pública da IA; debate sobre o que constitui "inteligência".

### 1997 — LSTM: Long Short-Term Memory
Sepp Hochreiter e Jürgen Schmidhuber publicam **"Long Short-Term Memory"** na *Neural Computation* — arquitetura recorrente com portas de entrada, esquecimento e saída que resolve o problema do vanishing gradient em RNNs.

- Publicação: Hochreiter, S. & Schmidhuber, J. (1997). *Neural Computation* 9(8), 1735–1780.
- Significado: Permite aprender dependências de longo prazo em sequências; base para reconhecimento de fala, tradução, series temporais.

### 1998 — MNIST e LeNet-5
Yann LeCun publica **"Gradient-Based Learning Applied to Document Recognition"** — estabelece o dataset **MNIST** (70.000 dígitos manuscritos 28x28) e a arquitetura **LeNet-5** (convoluções, pooling, fully connected).

- Publicação: LeCun, Y., Bottou, L., Bengio, Y. & Haffner, P. (1998). *Proceedings of the IEEE* 86(11), 2278–2324.
- Significado: MNIST torna-se o "Hello World" do aprendizado de máquina; LeNet-5 define o template das CNNs modernas.

---

## 2000–2011: Big Data e o Renascimento

### 2004 — ImageNet: O Projeto
Fei-Fei Li (Princeton, depois Stanford) inicia o **ImageNet** — um dataset em larga escala de imagens organizadas hierarquicamente segundo a WordNet. A motivação: redes neurais não funcionam bem com poucos dados; é preciso escala massiva.

- Significado: Visionário — enquanto a comunidade focava em algoritmos, Li argumentava que dados importam tanto quanto modelos.
- Coleta: Milhares de trabalhadores no Mechanical Turk anotaram imagens por anos.

### 2006 — Deep Learning: Camadas Profundas
Geoffrey Hinton publica **"A Fast Learning Algorithm for Deep Belief Nets"** — mostra que redes profundas (Deep Belief Networks) podem ser pré-treinadas camada por camada com Restricted Boltzmann Machines (RBMs) antes do fine-tuning com backpropagation.

- Publicação: Hinton, G. E., Osindero, S. & Teh, Y. W. (2006). *Neural Computation* 18(7), 1527–1554.
- Significado: Renascimento do deep learning; demonstra que camadas profundas são treináveis.
- Contexto: Yoshua Bengio e Yann LeCun publicam trabalhos complementares no mesmo período.

### 2009 — ImageNet Dataset Público
O dataset **ImageNet** é lançado publicamente: 3,2 milhões de imagens em 5.247 categorias (sin sets WordNet). Em 2010, o desafio **ILSVRC** (ImageNet Large Scale Visual Recognition Challenge) é criado com 1,2 milhão de imagens em 1000 categorias.

- Significado: Catalisador da revolução do deep learning; fornece a escala de dados que faltava para treinar redes profundas.

### 2010 — GPU Computing para Redes Neurais
O uso de **GPUs** (NVIDIA CUDA) acelera o treinamento de redes neurais em 10-50x. Trabalhos de Rajat Raina, Anand Madhavan e Andrew Ng (**"Large-scale deep unsupervised learning using graphics processors"**, 2009) demonstram que GPUs são ideais para a computação matricial de backpropagation.

- Hardware: NVIDIA GTX 280 (240 cores, 1 GB VRAM).
- Significado: Fator crítico para a viabilidade do deep learning em escala.

---

## 2012–2016: A Revolução do Deep Learning

### 2012 — AlexNet: A Virada
Alex Krizhevsky, Ilya Sutskever e Geoffrey Hinton (Toronto) vencem o **ILSVRC 2012** com a **AlexNet** — uma CNN de 8 camadas (5 convolucionais, 3 fully connected), 60M parâmetros, ReLU, dropout, data augmentation. A acurácia top-5 cai de 26.2% para 15.3%, uma melhoria de 10 pontos percentuais sobre o segundo colocado (que usava SVM+features manuais).

- Publicação: Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). *NeurIPS 2012*.
- Significado: **Marco zero da era moderna do deep learning.** Demonstra que redes neurais profundas superam métodos clássicos por larga margem; inicia a corrida de GPUs e dados.

### 2013 — Word2Vec: Embeddings de Palavras
Tomas Mikolov (Google) publica **"Efficient Estimation of Word Representations in Vector Space"** — introduz os modelos Skip-gram e CBOW (Continuous Bag-of-Words) para gerar embeddings densos de palavras a partir de grandes corpora.

- Publicação: Mikolov, T. et al. (2013). *arXiv:1301.3781*.
- Significado: Permite operações vetoriais semânticas (rei - homem + mulher = rainha); revoluciona NLP.
- Influência: Gera toda a área de representações distribuídas; antecessora direta de BERT, GPT.

### 2014 — GANs: Generative Adversarial Networks
Ian Goodfellow (então em Montreal) publica **"Generative Adversarial Nets"** — dois modelos (gerador e discriminador) treinados em jogo minimax adversário.

- Publicação: Goodfellow, I. et al. (2014). *NeurIPS 2014*.
- Significado: Novo paradigma generativo; gerador aprende a produzir dados indistinguíveis dos reais.
- Aplicações: Geração de imagens (DCGAN, StyleGAN), super-resolução, arte, dados sintéticos.

### 2014 — Seq2Seq + Attention
Ilya Sutskever (Google) publica **"Sequence to Sequence Learning with Neural Networks"** — encoder-decoder com LSTMs para tradução automática. Paralelamente, **Bahdanau et al.** publicam **"Neural Machine Translation by Jointly Learning to Align and Translate"** — introduz mecanismo de atenção que alinha palavras fonte e alvo durante a tradução.

- Publicações:
  - Sutskever, I., Vinyals, O. & Le, Q. V. (2014). *NeurIPS 2014*.
  - Bahdanau, D., Cho, K. & Bengio, Y. (2014). *arXiv:1409.0473*.
- Significado: Seq2Seq + Attention = base arquitetural dos Transformers (2017).

### 2015 — ResNet: Redes Profundas
Kaiming He, Xiangyu Zhang, Shaoqing Ren e Jian Sun (Microsoft Research) publicam **"Deep Residual Learning for Image Recognition"** — propõem skip connections (conexões residuais) para treinar redes de até 152 camadas.

- Publicação: He, K. et al. (2015). *CVPR 2016*.
- Significado: Resolve o problema de degradação em redes muito profundas; vence ILSVRC 2015 com erro top-5 de 3.57% (super-humano).
- Impacto: Arquitetura residual é adotada em virtualmente todos os modelos de visão.

### 2015 — AlphaGo: Marco no Go
DeepMind (adquirida pelo Google em 2014) publica **"Mastering the Game of Go with Deep Neural Networks and Tree Search"** na *Nature*. AlphaGo combina redes neurais profundas (policy network + value network) com Monte Carlo Tree Search (MCTS). Em outubro de 2015, derrota **Fan Hui** (campeão europeu) por 5-0.

- Publicação: Silver, D. et al. (2016). *Nature* 529, 484–489.
- Significado: Primeira vez que uma IA vence um profissional no Go — jogo considerado o santo graal da IA por sua complexidade combinatória (~10^170 posições).

### 2016 — AlphaGo vs. Lee Sedol
Em março de 2016, **AlphaGo** derrota **Lee Sedol** (9º dan, 18 títulos mundiais) por 4-1 em Seul. A partida é assistida por 200 milhões de pessoas. O movimento 37 (jogada 37 da partida 2) — uma invasão no topo do tabuleiro — é considerado "criativo" e "humano" pelos especialistas; o movimento 78 (jogada 78 de Lee, a única vitória) é chamado de "mão de Deus".

- Significado: Momento cultural; muda a percepção pública sobre IA. DeepMind posteriormente publica AlphaGo Zero (2017), que aprende sem dados humanos.

### 2016 — WaveNet: Síntese de Voz
DeepMind publica **WaveNet** — modelo autoregressivo baseado em convoluções dilatadas (*dilated causal convolutions*) que gera áudio raw (16kHz) com qualidade comparável à voz humana.

- Publicação: van den Oord, A. et al. (2016). *arXiv:1609.03499*.
- Significado: Revoluciona síntese de fala (Google Assistant, etc).
- Legado: Base para modelos generativos de áudio.

---

## 2017–2020: Era dos Transformers

### 2017 — "Attention Is All You Need": O Transformer
**Vaswani et al.** (Google) publicam **"Attention Is All You Need"** no NeurIPS 2017 — propõem a arquitetura **Transformer**, baseada exclusivamente em self-attention multi-cabeça, removendo completamente recorrência e convolução.

- Publicação: Vaswani, A. et al. (2017). *NeurIPS 2017*.
- Arquitetura: Encoder-decoder com self-attention, positional encoding, multi-head attention (8 cabeças), feed-forward networks, layer normalization.
- Significado: **O paper mais influente da década.** Transformer torna-se a arquitetura dominante em NLP, visão (ViT), áudio, biologia, etc.
- Vantagens: Paralelizável (diferente de RNNs); captura dependências longas; escala com dados e computação.

### 2018 — BERT: Bidirectional Encoder Representations from Transformers
Jacob Devlin e equipe (Google) publicam **BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding** — modelo encoder-only pré-treinado com masked language modeling (MLM) e next sentence prediction (NSP).

- Publicação: Devlin, J. et al. (2018). *NAACL 2019*.
- Arquitetura: Transformer encoder com 12 camadas (base) ou 24 (large), bidirecional.
- Resultado: SOTA em 11 benchmarks NLP (GLUE, SQuAD, etc); melhoria de 7.7 pontos no GLUE.
- Significado: Inaugura a era **pré-treino + fine-tuning** em NLP; democratiza o acesso a modelos poderosos.

### 2018 — GPT: Generative Pre-Training
Alec Radford e equipe (OpenAI) publicam **"Improving Language Understanding by Generative Pre-Training"** — modelo decoder-only pré-treinado com language modeling (autoregressivo) e fine-tuning supervisionado.

- Publicação: Radford, A. et al. (2018). OpenAI.
- Arquitetura: Transformer decoder com 12 camadas, 117M parâmetros.
- Significado: Demonstra que pré-treino generativo + fine-tuning funciona; antecede a escala massiva dos GPTs seguintes.

### 2019 — GPT-2: Preocupações Éticas
OpenAI publica **GPT-2** (1.5 bilhões de parâmetros) — inicialmente **não lança o modelo completo** por preocupações com uso malicioso (geração de fake news, spam, desinformação). Gerou intenso debate sobre publicação responsável em IA.

- Publicação: Radford, A. et al. (2019). *OpenAI Blog*.
- Capacidades: Geração de texto coerente em parágrafos longos; tradução, sumarização, Q&A sem fine-tuning (zero-shot).
- Significado: Primeiro alerta público sobre riscos de modelos generativos; estabelece o padrão de release gradual (staged release).

### 2020 — GPT-3: 175 Bilhões de Parâmetros
OpenAI publica **"Language Models are Few-Shot Learners"** — GPT-3 com 175B parâmetros, 96 camadas, 96 cabeças de atenção. Demonstra **few-shot learning** (in-context learning) sem fine-tuning.

- Publicação: Brown, T. et al. (2020). *NeurIPS 2020*.
- Arquitetura: Transformer decoder-only, treinado em 45 TB de texto.
- Significado: Escala massiva mostra emergência de capacidades; OpenAI lança API (paga) — abre o mercado de LLMs como serviço.
- Capacidades: Programação, tradução, criação de conteúdo, raciocínio básico.

### 2020 — AlphaFold 2: O Problema do Dobramento de Proteínas
DeepMind publica **"Highly accurate protein structure prediction with AlphaFold"** na *Nature*. AlphaFold 2 usa transformers (Evoformer) para prever a estrutura 3D de proteínas a partir da sequência de aminoácidos.

- Publicação: Jumper, J. et al. (2021). *Nature* 596, 583–589.
- Resultado: Atinge 90+ GDT (global distance test) no CASP14 — comparável à cristalografia experimental.
- Significado: Considerado o maior avanço científico da IA; resolvido um problema de 50 anos. Demis Hassabis e John Jumper recebem o **Nobel de Química 2024**.

### 2020 — DALL-E: Texto para Imagem
OpenAI publica **DALL-E** (12B parâmetros) — modelo generativo que combina GPT (autoregressivo) com VQ-VAE para gerar imagens a partir de descrições textuais.

- Publicação: Ramesh, A. et al. (2021). *arXiv:2102.12092*.
- Significado: Inaugura a geração de imagens por texto em alta qualidade; antecede DALL-E 2, DALL-E 3.

### 2020 — CLIP: Aprendizado Contrastivo Visão-Texto
OpenAI publica **CLIP** (Contrastive Language-Image Pre-training) — treinado contrastivamente em 400M pares (imagem, texto) da internet. Aprende representações multimodais que transferem zero-shot para classificação, detecção, etc.

- Publicação: Radford, A. et al. (2021). *ICML 2021*.
- Significado: Torna-se backbone de visão multimodal; fundação para geração guiada por texto (DALL-E, Stable Diffusion).

### 2020 — LaMDA / Meena: Chatbots Conversacionais
Google publica **Meena** (2020) e depois **LaMDA** (Language Model for Dialogue Applications, 2021) — modelos especializados em diálogo aberto. Em 2022, o engenheiro Blake Lemoine afirma que LaMDA é "senciente", gerando controvérsia global.

- Publicação: Adiwardana, D. et al. (2020). *arXiv:2001.09977* (Meena).
- Significado: Avanço em diálogo; a controvérsia LaMDA reacende debates sobre consciência em IA.

---

## 2021–2024: Geração e Multimodalidade

### 2021 — GitHub Copilot: Geração de Código
GitHub (Microsoft) e OpenAI lançam **Copilot** — modelo Codex (derivado do GPT-3, fine-tuned em código público do GitHub) que sugere código em tempo real no IDE.

- Tecnologia: **Codex** (12B params), fine-tuned em 54 milhões de repositórios públicos.
- Publicação: Chen, M. et al. (2021). *arXiv:2107.03374*.
- Significado: Primeiro assistente de programação generativo amplamente adotado (~1.8M assinantes em 2023); transforma a produtividade em software.

### 2022 — Stable Diffusion: Código Aberto
Stability AI lança **Stable Diffusion** — modelo de difusão latente (LDM) que gera imagens a partir de texto. Treinado em LAION-5B (5 bilhões de pares imagem-texto), com 860M parâmetros.

- Publicação: Rombach, R. et al. (2022). *CVPR 2022*.
- Significado: Democratização da geração de imagens: código aberto, rodava em GPUs de consumo (6-8 GB VRAM).

### 2022 — ChatGPT: O Produto que Mudou Tudo
OpenAI lança **ChatGPT** (30 de novembro de 2022) — interface de chat baseada no modelo GPT-3.5 turbo, fine-tuned com RLHF (Reinforcement Learning from Human Feedback). Atinge 100 milhões de usuários em **dois meses** — o crescimento mais rápido da história.

- Tecnologia: GPT-3.5 + InstructGPT (Ouyang et al., 2022 — "Training language models to follow instructions with RLHF").
- Significado: **Ponto de inflexão cultural.** IA generativa torna-se mainstream; inicia a corrida global de LLMs.
- Impacto: ChatGPT é o produto de crescimento mais rápido de todos os tempos; corpo docente, estudantes, escritores, programadores adotam imediatamente.

### 2023 — GPT-4: Multimodal
OpenAI lança **GPT-4** (março de 2023) — modelo multimodal (texto e imagem), estimado em 1.76 trilhões de parâmetros (8 experts de 220B — MoE, não confirmado oficialmente). Passa no **Uniform Bar Exam** no percentil 90; atinge performance humana ou superior em dezenas de benchmarks.

- Publicação: OpenAI (2023). *GPT-4 Technical Report*. arXiv:2303.08774.
- Capacidades: Raciocínio avançado, interpretação de imagens, codificação, criatividade.
- Significado: Primeiro modelo amplamente disponível com raciocínio próximo ao humano em domínios especializados.

### 2023 — Claude: Constitutional AI
Anthropic (ex-OpenAI: Dario Amodei, Daniela Amodei, etc.) lança **Claude** — modelos treinados com **Constitutional AI** (Bai et al., 2022 — "Constitutional AI: Harmlessness from AI Feedback"). Claude 1, Claude 2, Claude Instant.

- Significado: Abordagem alternativa ao RLHF; foco em alinhamento e segurança constitucional.
- Diferencial: Claude (especialmente Claude 3, 2024) compete diretamente com GPT-4; ênfase em helpfulness, honesty, harmlessness (HHH).

### 2023 — Gemini: Google DeepMind
Google funde **Google Brain** e **DeepMind** (abril de 2023) para formar **Google DeepMind**. Em dezembro de 2023, lança **Gemini** — modelo multimodal nativo (texto, imagem, áudio, vídeo, código). Gemini Ultra é o primeiro modelo a superar GPT-4 no MMLU (90.0%).

- Versões: Gemini Nano (mobile), Gemini Pro (produtos Google), Gemini Ultra (pesquisa).
- Significado: Reorganização do ecossistema Google; competição direta com OpenAI.

### 2023 — Llama 2: Open-Source Rival
Meta (Facebook) lança **Llama 2** — modelos de 7B, 13B, 70B parâmetros, open-source para pesquisa e uso comercial. Treinado em 2 trilhões de tokens.

- Publicação: Touvron, H. et al. (2023). *arXiv:2307.09288*.
- Significado: Catalisa o ecossistema open-source de LLMs; centenas de fine-tunes (Vicuna, Alpaca, Orca, etc.).

### 2023 — Mixtral 8x7B: Mixture of Experts
Mistral AI (França, fundada por ex-DeepMind/Meta) lança **Mixtral 8x7B** — modelo MoE (Mixture of Experts) sparse com 46.7B parâmetros totais mas apenas 12.9B ativos por token.

- Publicação: Jiang, A. Q. et al. (2024). *arXiv:2401.04088*.
- Significado: Eficiência computacional iguala performance de modelos muito maiores (70B+); populariza MoE em open-source.

### 2024 — Sora: Geração de Vídeo
OpenAI lança **Sora** (fevereiro de 2024) — modelo de difusão para geração de vídeo de até 60 segundos a partir de texto. Usa arquitetura de patches espaço-temporais (similar a transformers).

- Tecnologia: Diffusion transformer (DiT), treinado em vídeos de resolução e duração variadas.
- Significado: Avanço qualitativo em geração de vídeo; movimentos consistentes, física plausível, cenas complexas.

### 2024 — Claude 3 Opus
Anthropic lança **Claude 3** (março de 2024) — três modelos: Haiku (rápido), Sonnet (balanceado), **Opus** (topo-de-linha). Opus supera GPT-4 em vários benchmarks (MMLU, GPQA, HumanEval).

- Capacidades: Raciocínio matemático e científico avançado, visão, análise de documentos.
- Significado: Estabelece Anthropic como competidor direto de OpenAI; Claude torna-se preferido em tarefas analíticas e de segurança.

### 2024 — Llama 3: Meta
Meta lança **Llama 3** — modelos 8B, 70B e (anunciado) 400B. Treinado em 15 trilhões de tokens. 70B supera GPT-3.5 e compete com GPT-4.

- Publicação: AI @ Meta (2024). *The Llama 3 Herd of Models*. arXiv:2407.21783.
- Significado: Novo padrão open-source; fine-tunes imediatos (Llama 3.1, 3.2, 3.3).

### 2024 — GPT-4o: Omni Model
OpenAI lança **GPT-4o** ("omni", maio de 2024) — modelo nativamente multimodal (texto, áudio, visão) com latência de resposta de voz em 232ms (média humana: 320ms). Gratuito para usuários do ChatGPT.

- Capacidades: Fala em tempo real, tom de voz, canto, interpretação de emoções, visão simultânea.
- Significado: Primeiro modelo verdadeiramente omni; interação por voz natural, sem módulos separados (ASR -> NLU -> TTS).

### 2024 — Gemini 1.5 Pro: Janela de Contexto de 1M
Google DeepMind lança **Gemini 1.5 Pro** — janela de contexto de até 1 milhão de tokens (10 milhões para pesquisa). Arquitetura MoE (Mixture of Experts).

- Publicação: Gemini Team, Google (2024). *arXiv:2403.05530*.
- Significado: Possibilita análise de documentos inteiros (livros, codebases, vídeos longos) em uma única inferência.

### 2024 — EU AI Act: Regulação
A União Europeia aprova o **AI Act** (março de 2024) — primeira lei abrangente de regulação de IA no mundo. Classifica sistemas de IA por nível de risco (mínimo, limitado, alto, inaceitável). Proíbe sistemas de pontuação social, vigilância biométrica em tempo real (com exceções), manipulação subliminar. Exige transparência para modelos generativos (deepfakes, conteúdo gerado).

- Significado: Estabelece precedente regulatório global; influencia legislações nos EUA, Reino Unido, Japão, Brasil, Canadá, China.

### 2024 — US Executive Order on AI
Governo Biden assina **Executive Order on Safe, Secure, and Trustworthy Artificial Intelligence** (outubro de 2023, implementação 2024). Exige testes de segurança (red-teaming) de modelos de fronteira, padrões de biossíntese, marca d'água em conteúdo gerado, investimento em pesquisa de segurança.

- Significado: Primeira ação executiva abrangente dos EUA sobre IA; estabelece o AI Safety Institute (NIST).

---

## Marcos Adicionais (Contexto)

| Ano | Evento | Significado |
|-----|--------|-------------|
| 1943 | McCulloch & Pitts — modelo de neurônio | Fundação da computação neural |
| 1950 | Teste de Turing | Critério filosófico-operacional de inteligência |
| 1956 | Dartmouth Conference | Nascimento do termo "Inteligência Artificial" |
| 1957 | Perceptron Mark I | Primeiro classificador neural |
| 1959 | "Machine Learning" cunhado | Nascimento do termo |
| 1961 | Unimate | Primeiro robô industrial |
| 1964 | ELIZA | Primeiro chatbot |
| 1969 | Minsky & Papert — "Perceptrons" | Início do primeiro inverno da IA |
| 1970 | MYCIN | Sistema especialista médico |
| 1974-1980 | Primeiro inverno da IA | Cortes de funding |
| 1980 | XCON | Sistema especialista comercial |
| 1982 | Hopfield Networks | Memória associativa neural |
| 1986 | Backpropagation (Rumelhart, Hinton, Williams) | Treinamento de redes profundas |
| 1988 | Q-Learning | Base do reinforcement learning |
| 1989 | LeNet | Primeira CNN prática |
| 1987-1993 | Segundo inverno da IA | Colapso do mercado LISP |
| 1995 | SVM (Vapnik) | Kernel trick, classificador de margem máxima |
| 1997 | Deep Blue vs. Kasparov | Máquina vence campeão mundial de xadrez |
| 1997 | LSTM | Memória de longo prazo para RNNs |
| 1998 | MNIST + LeNet-5 | Dataset e arquitetura clássicos |
| 2004 | ImageNet inicia | Dataset massivo de imagens |
| 2006 | Deep Learning (Hinton) | Pré-treinamento camada a camada |
| 2010 | GPU computing | Aceleração de 10-50x para redes neurais |
| 2012 | **AlexNet** | **Virada do deep learning no ImageNet** |
| 2013 | Word2Vec | Embeddings densos de palavras |
| 2014 | GANs | Redes generativas adversárias |
| 2014 | Seq2Seq + Attention | Base dos transformers |
| 2015 | ResNet | Conexões residuais (152 camadas) |
| 2015 | AlphaGo (Fan Hui) | IA vence profissional no Go |
| 2016 | AlphaGo (Lee Sedol) | Marco cultural mundial |
| 2016 | WaveNet | Síntese de voz neural |
| 2017 | **"Attention Is All You Need"** | **Arquitetura Transformer** |
| 2018 | BERT | Encoders bidirecionais pré-treinados |
| 2018 | GPT | Generative Pre-Training |
| 2019 | GPT-2 (1.5B) | Preocupações éticas, staged release |
| 2020 | GPT-3 (175B) | Few-shot learning, OpenAI API |
| 2020 | AlphaFold 2 | Dobramento de proteínas (Nobel 2024) |
| 2020 | DALL-E, CLIP | Geração + compreensão multimodal |
| 2021 | GitHub Copilot | Geração de código em IDE |
| 2022 | Stable Diffusion | Geração de imagens open-source |
| 2022 | **ChatGPT** | **100M usuários em 2 meses** |
| 2023 | GPT-4 (multimodal) | ~1.8T params, bar exam 90% |
| 2023 | Claude (Anthropic) | Constitutional AI |
| 2023 | Gemini (Google DeepMind) | Multimodal nativo |
| 2023 | Llama 2 (Meta) | Open-source rival |
| 2023 | Mixtral 8x7B (Mistral) | Mixture of experts |
| 2024 | Sora (OpenAI) | Geração de vídeo |
| 2024 | Claude 3 Opus | Rival do GPT-4 |
| 2024 | Llama 3 (Meta) | 8B, 70B, 400B |
| 2024 | GPT-4o | Omni model (texto, áudio, visão) |
| 2024 | Gemini 1.5 Pro | 1M context window |
| 2024 | EU AI Act | Regulação aprovada |
| 2024 | US Executive Order | Segurança de IA |

---

## Conexões e Dependências Intelectuais

### Correntes de Pensamento

```
Lógica e Matemática
  ├── Gödel (1931) → Turing (1936) → Computabilidade
  ├── McCulloch & Pitts (1943) → Redes Neurais → Deep Learning
  └── Boole (1854) → Shannon (1938) → Computação digital

Cibernética (Wiener, 1948)
  ├── Feedback → Controle robótico (Unimate, Shakey)
  └── Informação → Entropia → Machine Learning

Cognitivismo (Chomsky, Miller, Newell & Simon)
  ├── Gramática gerativa → PNL simbólica → ELIZA, SHRDLU
  ├── Resolução de problemas → Sistemas Especialistas (MYCIN, XCON)
  └── Lógica → PROLOG → Programação lógica

Conexionismo (Rosenblatt, Rumelhart, Hinton, LeCun)
  ├── Perceptron (1957) → Backpropagation (1986) → Deep Learning (2006)
  ├── Hopfield (1982) → Boltzmann Machines → DBNs
  └── CNNs (LeCun 1989) → AlexNet (2012) → Revolução visual

Estatística e Probabilidade
  ├── Bayes → Naive Bayes, Redes Bayesianas
  ├── Markov → HMMs → CRFs → Structured Prediction
  └── Vapnik (1995) → SVM → Kernel Methods

Reforço e Controle
  ├── Bellman (1957) → MDPs → Dynamic Programming
  ├── Watkins (1988) → Q-Learning → DQN (2013) → RL moderno
  └── Tesauro (1992) → TD-Gammon → AlphaGo → RLHF
```

### Relações com outras notas

- [[Ciencia-da-Computacao]] — Turing, von Neumann, Chomsky, complexidade, P vs NP — fundamentação teórica para toda a IA.
- [[NLP-Fundamentos]] — Tokenização, embeddings, RNNs, Transformers, BERT, GPT, fine-tuning, RLHF — complemento prático de NLP.
- [[Algoritmos-e-Estruturas]] — Algoritmos de busca, DP, grafos — base para planejamento e raciocínio em IA.

### Relações externas sugeridas

- **Machine-Learning-Fundamentos** — Nota dedicada aos fundamentos matemáticos (regressão, classificação, árvores, ensembles, SVMs, clustering).
- **Redes-Neurais** — Nota dedicada a arquiteturas neurais (MLP, CNN, RNN, LSTM, Transformer, GNN) com implementações.
- **Filosofia-da-Mente** — Conexões com o problema mente-corpo, consciência, qualia, livre-arbítrio — debates tocados pela IA.

---

## Questões Abertas e Debates

### AGI (Artificial General Intelligence)
- Linha do tempo: Estimativas variam de 2027 (Altman, Musk) a 2050+ (LeCun) a "nunca" (alguns filósofos).
- Critérios: Transfer learning humano, senso comum, aprendizado contínuo, autonomia, metacognição.
- Abordagens: Escalar LLMs atuais (scale hypothesis), arquiteturas neuro-simbólicas, world models, embodiment.

### Alinhamento (Alignment Problem)
- Objetivo: Garantir que sistemas de IA ajam de acordo com intenções humanas.
- Desafios: Reward hacking, objetivos instrumentais (preservação, aquisição de recursos), especificação inadequada.
- Escolas: RLHF/DPO (OpenAI, Anthropic), Constitutional AI (Anthropic), value loading (MIRI), amplificação iterativa (Eliciting Latent Knowledge).

### Riscos Existenciais (X-Risk)
- Argumento: Uma AGI desalinhada poderia causar danos irreversíveis (Nick Bostrom, *Superintelligence*, 2014).
- Ceticismo: IA é apenas uma ferramenta; riscos reais estão em vieses, emprego, desinformação (Andrew Ng, Yann LeCun).
- Debate polarizado: Efetivismo (EA) vs. aceleracionismo (e/acc).

### Desinformação e Deepfakes
- Modelos generativos (GPT-4, Sora, Stable Diffusion) tornam trivial criar conteúdo falso convincente.
- Soluções: Marca d'água (C2PA, SynthID), detecção forense, regulação, educação midiática.
- Risco: Erosão da confiança pública em mídia, texto, evidências.

### Concentração de Poder
- Poucas empresas controlam os modelos mais avançados: OpenAI (MS), Google, Meta, Anthropic.
- Acesso a GPUs (NVIDIA monopoliza ~80% do mercado de treinamento) — hardware crítico.
- Implicações geopolíticas: EUA vs. China (Huawei, Baidu, Tencent, Alibaba); chips (sanções, CHIPS Act).

### Impactos Sociais e Econômicos
- **Emprego**: Automação de tarefas cognitivas (advocacia, contabilidade, jornalismo, programação, arte). Debate: substituição vs. aumento.
- **Produtividade**: GitHub Copilot aumenta produtividade em 55% (estudo de 2023). IA pode adicionar $4.4 trilhões/ano à economia global (McKinsey, 2023).
- **Desigualdade**: Quem possui/controla IA? Efeito sobre salários, concentração de capital.
- **Criatividade**: Arte generativa (Midjourney, DALL-E, Sora) redefine autoria, originalidade, direitos autorais.

### Sustentabilidade
- Treinamento do GPT-3: ~1.300 MWh (~600 toneladas de CO2).
- Inferência em larga escala consome energia significativa.
- Soluções: Hardware mais eficiente, modelos menores (distillation, quantization), energia renovável.

---

## Cronograma Visual Simplificado

```
1943 ─ ─ McCulloch & Pitts (neurônio)
1950 ─ ─ Teste de Turing
1956 ─ ─ Dartmouth (termo "IA")
1957 ─ ─ Perceptron (Rosenblatt)
1964 ─ ─ ELIZA
1966 ─ ─ Shakey
1969 ─ ─ "Perceptrons" (Minsky) ──> 1º inverno
1970 ─ ─ MYCIN
1974─1980 ── 1º inverno
1980 ─ ─ XCON (expert systems boom)
1986 ─ ─ Backpropagation
1987─1993 ── 2º inverno
1997 ─ ─ Deep Blue, LSTM
1998 ─ ─ MNIST, LeNet-5
2006 ─ ─ Deep Learning (Hinton)
2012 ─ ─ ⭐ AlexNet (revolução)
2014 ─ ─ GANs, Seq2Seq+Attention
2015 ─ ─ ResNet, AlphaGo
2017 ─ ─ ⭐ "Attention Is All You Need"
2018 ─ ─ BERT, GPT
2020 ─ ─ GPT-3, AlphaFold 2, DALL-E
2022 ─ ─ ⭐ ChatGPT (cultura)
2023 ─ ─ GPT-4, Claude, Gemini, Llama 2
2024 ─ ─ GPT-4o, Sora, Claude 3, Gemini 1.5
```

> *Nota: Esta cronologia está em constante evolução. Novos modelos, regulamentações e descobertas científicas são anunciados mensalmente. Consulte fontes atualizadas para marcos recentes.*

---

## Referências Selecionadas

1. Russell, S. & Norvig, P. (2021). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
2. Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press.
3. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press.
4. Marcus, G. & Davis, E. (2019). *Rebooting AI: Building Artificial Intelligence We Can Trust*. Pantheon.
5. Nilsson, N. J. (2010). *The Quest for Artificial Intelligence: A History of Ideas and Achievements*. Cambridge University Press.
6. Jumper, J. et al. (2021). "Highly accurate protein structure prediction with AlphaFold." *Nature* 596, 583–589.
7. Vaswani, A. et al. (2017). "Attention Is All You Need." *NeurIPS 2017*.
8. Devlin, J. et al. (2018). "BERT: Pre-training of Deep Bidirectional Transformers." *NAACL 2019*.
9. Brown, T. et al. (2020). "Language Models are Few-Shot Learners." *NeurIPS 2020*.
10. Krizhevsky, A., Sutskever, I. & Hinton, G. E. (2012). "ImageNet Classification with Deep Convolutional Neural Networks." *NeurIPS 2012*.
