---
tags: [glossary, terminology, hub]
updated: 2026-05-19
aliases: ["Glossário Mestre", "Terminologia Unificada"]
---

# Master Glossary (Terminologia Unificada)

Este glossário define os termos técnicos e conceituais utilizados em todo o ecossistema do vault, garantindo consistência entre notas e agentes de IA. Os termos estão organizados por domínio do conhecimento.

---

## Matemática

- **Autovalor (Eigenvalue)**: escalar $\lambda$ tal que $A\mathbf{v} = \lambda\mathbf{v}$ para uma matriz $A$ e vetor $\mathbf{v}$. Autovalores capturam a "amplificação" de uma transformação linear ao longo de direções específicas (autovetores). Central para PCA, SVD, PageRank e análise espectral de redes.
- **Autovetor (Eigenvector)**: vetor $\mathbf{v}$ cuja direção não muda sob uma transformação linear $A$ — apenas sua magnitude é escalada pelo autovalor $\lambda$. Autovetores representam direções "naturais" de um sistema.
- **SVD (Decomposição em Valores Singulares)**: fatoração $A = U\Sigma V^T$ que decompõe qualquer matriz $A$ em três componentes: $U$ (autovetores de $AA^T$), $\Sigma$ (valores singulares) e $V^T$ (autovetores de $A^TA$). Fundamenta redução de dimensionalidade, compressão, recomendação e embeddings.
- **Gradiente**: vetor de derivadas parciais de uma função multivariada $\nabla f = (\partial f/\partial x_1, \ldots, \partial f/\partial x_n)$. Aponta na direção de maior crescimento da função. Usado em otimização (gradiente descendente) para encontrar mínimos de funções de perda.
- **Gradiente Descendente (Gradient Descent)**: algoritmo de otimização iterativo que atualiza parâmetros na direção oposta ao gradiente: $\theta_{t+1} = \theta_t - \eta \nabla L(\theta_t)$. Base do treinamento de redes neurais.
- **Entropia (Shannon)**: medida de incerteza ou surpresa média de uma distribuição de probabilidade: $H(X) = -\sum p(x) \log p(x)$. Quantifica a quantidade média de informação contida em uma variável aleatória. Usada em teoria da informação, compressão, árvores de decisão.
- **Divergência KL (Kullback-Leibler)**: medida de "distância" entre duas distribuições de probabilidade: $D_{KL}(P||Q) = \sum p(x) \log(p(x)/q(x))$. Não é simétrica nem métrica. Usada em treinamento de modelos generativos (VAEs), otimização de políticas (RL) e quantificação de perda de informação.
- **MLE (Maximum Likelihood Estimation)**: método para estimar parâmetros de um modelo estatístico maximizando a probabilidade dos dados observados sob o modelo: $\hat{\theta} = \arg\max_\theta P(D|\theta)$. Base do treinamento de muitos modelos de ML (regressão logística, redes neurais com cross-entropy).
- **Informação Mútua (Mutual Information)**: medida de dependência entre duas variáveis: $I(X;Y) = D_{KL}(P(X,Y)||P(X)P(Y))$. Quantifica quanta informação uma variável contém sobre a outra. Usada em seleção de features, agrupamento e teoria da informação.
- **Perplexidade (Perplexity)**: exponencial da entropia cruzada, usada para avaliar modelos de linguagem: $PPL = \exp(-\frac{1}{N}\sum \log p(w_i|contexto))$. Quanto menor, melhor o modelo.

---

## Psicologia

- **Sistema 1 / Sistema 2 (Kahneman)**: dois modos de pensamento — Sistema 1 (rápido, automático, intuitivo, heurístico) e Sistema 2 (lento, deliberado, analítico, esforçado). *Rápido e Devagar* (2011). Central para entender vieses e heurísticas na tomada de decisão.
- **Memória de Trabalho (Working Memory)**: sistema de capacidade limitada que mantém e manipula informação temporariamente (tipicamente 7±2 itens, Miller, 1956). Correlato neural: córtex pré-frontal. Essencial para raciocínio, compreensão linguística e aprendizado.
- **Viés Cognitivo (Cognitive Bias)**: erro sistemático no pensamento que desvia o julgamento da racionalidade objetiva. Exemplos: viés de confirmação (buscar evidências que confirmem crenças), viés de ancoragem (dependência excessiva da primeira informação recebida), heurística da disponibilidade (julgar frequência pela facilidade de recall).
- **Dissonância Cognitiva (Festinger, 1957)**: desconforto mental por manter crenças contraditórias. Humanos tendem a racionalizar ou ajustar crenças para reduzir a dissonância, em vez de mudar comportamento.
- **Teoria da Mente (Theory of Mind)**: capacidade de atribuir estados mentais (crenças, desejos, intenções) a si mesmo e a outros. Essencial para interação social, empatia e comunicação. Déficit central no autismo (Baron-Cohen, 1985).
- **Heurística da Disponibilidade**: tendência a julgar a probabilidade de eventos pela facilidade com que exemplos vêm à mente. Ex.: superestimar mortes por acidentes aéreos vs. acidentes de carro.
- **Viés de Confirmação**: tendência a buscar, interpretar e lembrar informações que confirmam crenças preexistentes. Amplificado por algoritmos de recomendação (filter bubbles, echo chambers).
- **Ancoragem (Anchoring)**: tendência a confiar excessivamente na primeira informação recebida (a "âncora") ao fazer julgamentos. Ex.: preço sugerido influenciando disposição a pagar.

---

## Neurociência

- **NCC (Neural Correlates of Consciousness)**: conjunto mínimo de mecanismos neurais suficientes para uma percepção consciente específica. Identificar NCC é o programa central da neurociência da consciência (Crick & Koch, 1990).
- **LTP (Long-Term Potentiation)**: fortalecimento duradouro de sinapses após estimulação repetida e de alta frequência. Mecanismo celular fundamental para aprendizado e formação de memória. Descoberto por Bliss & Lømo (1973) no hipocampo.
- **Hebbianismo (Lei de Hebb)**: "Neurons that fire together, wire together" — se um neurônio repetidamente contribui para disparar outro, a conexão sináptica entre eles se fortalece. Base da plasticidade sináptica e inspiração para aprendizado não-supervisionado em redes neurais artificiais.
- **GWT (Global Workspace Theory, Baars, 1988)**: teoria da consciência que propõe um "espaço global de trabalho" neural — informações que entram nesse espaço tornam-se conscientes e disponíveis para todo o sistema (atenção, memória, controle motor). Modelada computacionalmente por Dehaene (Global Neuronal Workspace).
- **IIT (Integrated Information Theory, Tononi, 2004)**: teoria que identifica consciência com integração de informação ($\Phi$). Quanto maior a integração causal de um sistema, maior sua consciência. Aplica-se a cérebros biológicos e potencialmente a sistemas artificiais.
- **Plasticidade Sináptica**: capacidade das sinapses de se fortalecerem ou enfraquecerem ao longo do tempo, em resposta a atividade neural. Base do aprendizado e da memória. Tipos: LTP (potenciação) e LTD (depressão de longa duração).
- **Hipocampo**: estrutura cerebral no lobo temporal medial, essencial para formação de novas memórias declarativas (explícitas) e navegação espacial. Danos ao hipocampo causam amnésia anterógrada (caso HM).
- **Córtex Pré-Frontal**: região frontal do cérebro responsável por funções executivas — planejamento, tomada de decisão, inibição de impulsos, memória de trabalho e personalidade. Última região a amadurecer (final da adolescência).

---

## Ética e Alinhamento

- **Alinhamento (AI Alignment)**: problema de garantir que sistemas de IA persigam objetivos alinhados com valores, intenções e preferências humanas. Subproblemas: value learning, reward hacking, specification gaming, outer alignment vs. inner alignment.
- **Corrigibilidade (Corrigibility)**: propriedade de um sistema de IA que permite que ele seja corrigido ou desligado por humanos, mesmo que isso contrarie seus objetivos. Um agente não-corrigível pode resistir a tentativas de desligamento como obstáculos a seus objetivos (Soares et al., 2015).
- **RLHF (Reinforcement Learning from Human Feedback)**: técnica de alinhamento que usa feedback humano para treinar um modelo de recompensa, que então guia o aprendizado por reforço do sistema de IA. Central no treinamento de ChatGPT, Claude e Gemini.
- **Consequencialismo**: teoria ética que julga a moralidade de ações por suas consequências. Utilitarismo (maximizar bem-estar total) é a forma mais conhecida. Aplicado em IA: otimização de utilidade, trade-offs de segurança.
- **Deontologia (Kant)**: teoria ética que julga ações por sua conformidade com deveres e regras morais, independentemente das consequências. Imperativo categórico: trate a humanidade sempre como fim, nunca apenas como meio. Aplicado em IA: restrições de segurança, direitos dos usuários.
- **Ética das Virtudes (Aristóteles)**: teoria ética focada no caráter do agente moral — virtudes (coragem, temperança, justiça, sabedoria) como disposições para agir bem. Aplicado em IA: design de agentes com "caráter", virtudes epistêmicas.
- **Explainability / Interpretabilidade**: capacidade de explicar decisões de modelos de IA em termos compreensíveis por humanos. Técnicas: SHAP, LIME, atenção maps. Distinção: modelos intrinsecamente interpretáveis (árvores) vs. pós-hoc (LIME para redes neurais).
- **Alinhamento Externo (Outer Alignment)**: problema de especificar corretamente o objetivo que queremos que a IA otimize (evitar specification gaming, objetivos mal especificados). Ex.: pedir "maximizar cliques" sem especificar que cliques em anúncios enganosos não contam.
- **Alinhamento Interno (Inner Alignment)**: problema de garantir que o sistema de IA realmente otimize o objetivo que especificamos (evitar objetivos emergentes, mesa-otimização, delegação adversária). Surge em sistemas com otimizadores poderosos.
- **Especificação Fraca (Weak-to-Strong Generalization)**: capacidade de modelos menores supervisionarem modelos maiores durante o treinamento, mantendo alinhamento conforme a capacidade escala. Problema central de superalinhamento (openai, 2023).

---

## Filosofia

- **Qualia**: aspectos qualitativos e subjetivos da experiência consciente — a "sensação de ser" algo (Nagel, 1974). Exemplos: o vermelho de um pôr do sol, a dor de uma queimadura, o sabor do chocolate. O "problema difícil da consciência" (Chalmers, 1995) é explicar por que processos físicos produzem qualia.
- **Dualismo (mente-corpo)**: tese de que mente e corpo (ou consciência e cérebro) são substâncias distintas. Formas: dualismo de substância (Descartes), dualismo de propriedades. Principal problema: como o imaterial interage com o material (interacionismo)?
- **Funcionalismo**: teoria da mente que identifica estados mentais por suas funções causais (inputs, outputs, relações com outros estados), não por sua constituição material. Um mesmo estado mental pode ser implementado em múltiplos substratos — múltipla realizabilidade. Base filosófica da IA forte.
- **Chinese Room (Searle, 1980)**: experimento mental contra IA forte: um humano em uma sala segue regras sintáticas para manipular símbolos chineses sem entender chinês. Argumento: manipulação sintática não produz semântica genuína. Logo, computadores não "entendem" — apenas simulam entendimento.
- **Hard Problem of Consciousness (Chalmers, 1995)**: problema de explicar por que e como processos físicos (neurais, computacionais) dão origem à experiência subjetiva (qualia). Distinto dos "problemas fáceis" (explicar funções cognitivas: atenção, memória, relato verbal). A IA resolve os problemas fáceis; o hard problem permanece aberto.
- **Problema do Controle (Control Problem, Bostrom, 2014)**: como garantir que uma superintendência artificial aja de acordo com valores humanos, dado que seus objetivos podem não ser perfeitamente especificáveis e sua inteligência pode superar a humana em ordens de magnitude.
- **Simulacro (Baudrillard)**: cópia sem original — representação que substitui a realidade a ponto de não podermos mais distinguir real de representação. Terceira ordem de simulacros na pós-modernidade: o mapa precede o território.
- **Materialismo (Fisicalismo)**: tese de que tudo o que existe é físico (ou superveniente ao físico). A mente é o cérebro funcionando. Forma ortodoxa nas ciências cognitivas e neurociência contemporânea.

---

## Economia Digital

- **RBU (Renda Básica Universal)**: transferência monetária periódica, incondicional, universal e individual a todos os cidadãos, sem exigência de contrapartida. Proposta como resposta à automação e ao desemprego tecnológico. Pilotos: Finlândia (2017–2018), Quênia (GiveDirectly), Canadá (Mincome).
- **Excedente Comportamental (Behavioral Surplus, Zuboff)**: dados comportamentais coletados além do necessário para melhorar o serviço principal, usados como matéria-prima para predição e venda. Ex.: Google coleta dados de clique para melhorar busca (necessário) e usa o excedente para publicidade preditiva.
- **Desemprego Tecnológico (Keynes, 1930; Frey & Osborne, 2013)**: desemprego causado pela substituição de trabalho humano por máquinas. Keynes antecipou "desemprego tecnológico"; Frey & Osborne estimaram 47% dos empregos americanos em risco de automação.
- **Capitalismo de Vigilância (Surveillance Capitalism, Zuboff, 2019)**: sistema econômico que trata a experiência humana como matéria-prima gratuita para práticas comerciais de extração, predição e modificação comportamental. Diferencia-se do capitalismo industrial por extrair comportamento, não recursos naturais.
- **Destruição Criativa (Schumpeter, 1942)**: processo pelo qual inovação revoluciona a estrutura econômica de dentro, destruindo o velho e criando o novo. Aplicado à automação: novas tecnologias eliminam empregos antigos mas criam novos.
- **Economia dos Dados (Data Economy)**: sistema de produção, distribuição e consumo onde dados são o principal ativo econômico. Caracterizado por mercados bilaterais, efeitos de rede, assimetria informacional e monopólios naturais digitais.

---

## Direito Digital

- **GDPR (General Data Protection Regulation)**: Regulamento Geral de Proteção de Dados da União Europeia (EU 2016/679, vigência 2018). Marco regulatório mais abrangente do mundo. Princípios: consentimento explícito, direito ao esquecimento, portabilidade, notificação de violações. Multas de até 4% do faturamento global.
- **LGPD (Lei Geral de Proteção de Dados)**: Lei Brasileira nº 13.709/2018 (vigência 2020). Inspirada no GDPR. Estabelece direitos dos titulares, bases legais para tratamento, deveres dos controladores e sanções administrativas pela ANPD.
- **DPIA (Data Protection Impact Assessment)**: avaliação de impacto à proteção de dados — análise sistemática obrigatória para operações de tratamento que apresentem alto risco a direitos e liberdades (GDPR, Art. 35).
- **EU AI Act (2024)**: regulamentação europeia de inteligência artificial baseada em risco. Classifica sistemas de IA em: risco inaceitável (proibido: crédito social, vigilância biométrica em tempo real), alto risco (sujeito a avaliação de conformidade), risco limitado (obrigações de transparência), risco mínimo.
- **Direito à Explicação (Right to Explanation)**: direito do titular de dados a obter uma explicação significativa sobre decisões automatizadas que o afetem (GDPR Art. 22, considerando 71). Central para transparência algorítmica e accountability.
- **ANPD (Autoridade Nacional de Proteção de Dados)**: órgão da administração pública brasileira responsável por fiscalizar o cumprimento da LGPD, aplicar sanções e editar normas sobre proteção de dados.
- **Marco Civil da Internet (Lei 12.965/2014)**: lei brasileira que estabelece princípios, garantias, direitos e deveres para uso da internet no Brasil. Neutralidade de rede, privacidade, guarda de registros.

---

## Tecnologia e Sociedade

- **Panóptico Digital**: regime de vigilância difusa, descentralizada e algorítmica onde coleta, processamento e retroalimentação de dados comportamentais produzem efeitos disciplinares análogos ao panóptico de Bentham — mas ubíquos, assíncronos e capilarizados. A torre central é o algoritmo.
- **Capitalismo de Vigilância (ver Economia Digital)**: sistema que trata a experiência humana como matéria-prima para predição comportamental.
- **Perfilhamento (Profiling)**: construção automatizada de perfis detalhados de indivíduos a partir de dados agregados. Inferência de atributos demográficos, psicográficos, políticos, de saúde e comportamento a partir de dados aparentemente inocentes.
- **Efeito Chilling (Chilling Effect)**: autocensura preventiva que ocorre quando indivíduos sabem ou suspeitam que estão sendo monitorados. Reduz a disposição para buscar informação sensível, expressar opiniões impopulares e participar de atividades políticas.
- **Ofuscação (Obfuscation, Brunton & Nissenbaum, 2015)**: técnica de resistência à vigilância que consiste em gerar ruído, dados falsos ou informações ambíguas para confundir sistemas de coleta e análise. Ex.: AdNauseam (clica em todos os anúncios), TrackMeNot (buscas aleatórias).
- **Sinóptico (Mathiesen, 1997)**: regime de visibilidade onde muitos observam poucos — as massas vigiam celebridades, influenciadores e políticos. Complemento necessário ao panóptico (minoria vigia maioria). O panóptico digital opera nos dois eixos simultaneamente.
- **Sociedade de Controle (Deleuze, 1990)**: forma de poder pós-disciplinar caracterizada por modulação contínua e ao ar livre. Substitui a sociedade disciplinar (Foucault). O controle não requer confinamento — o smartphone é a cela portátil.
- **Data Brokers**: empresas que coletam, agregam, analisam e vendem dados pessoais de consumidores. Ex.: Acxiom, Experian, Serasa. Operam com mínima transparência e regulação.
- **Vigilância Antecipatória**: uso de modelos preditivos para classificar e modular comportamentos antes que ocorram. Opera não sobre o que o sujeito *fez*, mas sobre o que ele *poderá fazer*.

---

## Linguística

- **Semiótica (Peirce, Saussure)**: ciência geral dos signos e dos processos de significação. Peirce: tríade signo-objeto-interpretante; classificação em ícone, índice e símbolo. Saussure: significante + significado = signo; langue (sistema) vs. parole (uso individual).
- **Langue / Parole (Saussure)**: distinção fundamental entre o sistema abstrato da língua (langue — regras gramaticais, vocabulário, estrutura) e o uso concreto da fala (parole — enunciados individuais, performances linguísticas). A linguística saussureana estuda a langue.
- **Significante / Significado (Saussure)**: o signo linguístico une um significante (imagem acústica, a "forma" material) a um significado (conceito, a "ideia"). A relação entre ambos é arbitrária (não há razão natural para "cachorro" significar o animal).
- **Ícone / Índice / Símbolo (Peirce)**: três tipos de signo: ícone (semelhança com o objeto: fotografia, mapa), índice (conexão causal ou física: fumaça indica fogo, pegada indica passagem), símbolo (relação arbitrária convencional: palavras, bandeiras, logotipos).
- **Gramática Gerativa (Chomsky)**: teoria de que a capacidade linguística humana é inata — existe uma Gramática Universal (GU) biologicamente determinada que estabelece os princípios comuns a todas as línguas. A criança não aprende a língua do zero; já tem um "esquema" inato que é preenchido pela exposição.
- **Transformers (Vaswani et al., 2017)**: arquitetura de rede neural baseada exclusivamente em mecanismos de atenção (self-attention), sem recorrência ou convolução. Fundamento de modelos como BERT, GPT, Claude e Gemini. Permite processamento paralelo e captura de dependências longas.
- **Embedding (Word Embedding)**: representação vetorial densa de palavras (ou tokens) em um espaço contínuo de baixa dimensionalidade. Palavras com significados similares têm vetores próximos (word2vec, GloVe, embeddings contextuais de BERT/GPT).
- **Pragmática (Austin, Searle, Grice)**: estudo do uso da linguagem em contexto. Atos de fala (Austin: locucionário, ilocucionário, perlocucionário); implicaturas conversacionais e máximas de Grice (quantidade, qualidade, relação, modo).
- **Hipótese de Sapir-Whorf**: teoria de que a linguagem molda o pensamento (relatividade linguística). Versão forte (determinismo): a linguagem determina o pensamento. Versão fraca (influência): a linguagem influencia padrões cognitivos. Evidências: navegação espacial em línguas com direções cardeais obrigatórias.

---

## Geopolítica e Relações Internacionais

- **Heartland (Mackinder)**: região central da Eurásia — "quem controla a Europa Oriental comanda o Heartland; quem comanda o Heartland comanda a World Island; quem comanda a World Island comanda o mundo". Teoria clássica da geopolítica (1904).
- **Rimland (Spykman)**: faixa costeira ao redor do Heartland (Europa Ocidental, Oriente Médio, Sul da Ásia, Sudeste Asiático). Spykman: "quem controla o Rimland comanda a Eurásia; quem comanda a Eurásia controla o destino do mundo".
- **Hard Power / Soft Power / Smart Power (Nye)**: hard power é coerção militar e econômica; soft power é atração cultural e valores; smart power é a combinação estratégica de ambos.
- **BATNA (Best Alternative to a Negotiated Agreement)**: curso de ação alternativo caso a negociação fracasse. Seu poder real na mesa — quanto melhor sua BATNA, mais forte sua posição. Conceito fundamental do Método Harvard de Negociação (Fisher & Ury, 1981).
- **ZOPA (Zone of Possible Agreement)**: faixa de sobreposição entre os valores de reserva das partes. Se não há ZOPA, acordo é impossível a menos que um dos lados revise seu valor de reserva.
- **Dilema de Segurança (Security Dilemma)**: situação onde ações de um Estado para aumentar sua segurança (ex.: militarização) reduzem a segurança de outros Estados, gerando uma espiral de tensão e corrida armamentista. Conceito central do realismo nas Relações Internacionais.
- **Guerra Híbrida**: combinação de guerra convencional, guerra irregular, guerra cibernética, desinformação, pressão econômica e diplomática. Ex.: Guerra Rússia-Ucrânia.
- **Belt and Road Initiative (BRI)**: megaprojeto chinês de infraestrutura e investimento global (2013-presente). "Nova Rota da Seda". Maior programa de infraestrutura da história, envolvendo 140+ países.

## Geografia e Ciências da Terra

- **Placas Tectônicas**: grandes fragmentos da litosfera terrestre que se movem sobre a astenosfera. Limites: convergentes (colisão: Himalaia), divergentes (separação: dorsal meso-oceânica), transformantes (deslizamento: Falha de San Andreas).
- **Efeito Estufa**: processo natural onde gases atmosféricos (CO2, CH4, H2O) retêm calor irradiado pela superfície terrestre. Essencial para vida (Terra ~15°C vs -18°C sem efeito estufa). Intensificação antrópica causa aquecimento global.
- **COP (Conference of the Parties)**: conferência anual da UNFCCC (Convenção-Quadro da ONU sobre Mudança do Clima). COP21 (Paris, 2015) produziu o Acordo de Paris. COP28 (Dubai, 2023) focou em transição energética.
- **ESG (Environmental, Social, Governance)**: conjunto de critérios ambientais, sociais e de governança para avaliar sustentabilidade e impacto ético de investimentos. Surgiu do Pacto Global UN (2004). Frameworks: GRI, SASB, TCFD.

## Sistemas e Métodos

- **Teoria Geral dos Sistemas (Bertalanffy, 1968)**: abordagem interdisciplinar que estuda sistemas como totalidades organizadas, com propriedades emergentes, feedback, homeostase e hierarquia. Aplica-se a biologia, engenharia, gestão, ecologia e ciências sociais.
- **Emergência (Emergence)**: propriedades que surgem da interação de componentes de um sistema e não existem nos componentes isoladamente. Ex.: consciência (do cérebro), vida (das moléculas), mercado (dos agentes econômicos).
- **Auto-organização (Prigogine, 1977)**: capacidade de sistemas complexos de gerar ordem espontaneamente sem controle central. Ex.: formigueiros, cérebro, turbulência, mercado. Prigogine: estruturas dissipativas em sistemas longe do equilíbrio.
- **Teoria do Caos (Lorenz, 1963)**: sistemas deterministas não-lineares com sensibilidade extrema a condições iniciais (efeito borboleta). Comportamento imprevisível a longo prazo, mesmo sendo deterministicamente gerado.
- **Small-World (Watts-Strogatz, 1998)**: propriedade de redes onde a distância média entre nós cresce logaritmicamente com o tamanho da rede — "seis graus de separação". Alta clustering + caminho curto.
- **Scale-Free (Barabási-Albert, 1999)**: redes onde a distribuição de graus segue uma lei de potência (poucos hubs com muitas conexões, muitos nós com poucas). Universal: internet, redes sociais, proteínas, citações.
- **Teoria dos Jogos**: estudo matemático de interações estratégicas. Equilíbrio de Nash (1950): conjunto de estratégias onde nenhum jogador pode melhorar unilateralmente. Dilema do Prisioneiro: cooperação vs traição em situação de informação incompleta.

## Modelos Mentais e Vieses

- **Mapa não é Território (Korzybski, 1933)**: princípio geral da semântica geral — nossas representações mentais da realidade não SÃO a realidade. Confundir mapa com território leva a erros de julgamento.
- **Círculo de Competência (Buffett/Munger)**: conhecer os limites do seu conhecimento é mais importante que o conhecimento em si. Operar dentro do círculo onde se tem real expertise; expandi-lo gradualmente.
- **Pensamento Inverso (Invert, Always Invert)**: resolver problemas ao avesso — em vez de perguntar "como ter sucesso?", perguntar "como garantir o fracasso?" e evitar essas ações. Munger: inversão sistemática.
- **Navalha de Occam**: a explicação mais simples (com menos suposições) é geralmente a preferível. Não afirma que a mais simples é sempre verdadeira, mas é o melhor ponto de partida.
- **Navalha de Hanlon**: não atribua à malícia o que pode ser adequadamente explicado por ignorância, estupidez ou incompetência.
- **Lei de Conway (Conway, 1968)**: sistemas de software espelham as estruturas de comunicação da organização que os criou. Organizações com equipes modulares produzem sistemas modulares.
- **Antifragilidade (Taleb, 2012)**: propriedade de sistemas que se fortalecem com choques, volatilidade e desordem. Além de robustos (resistem) ou frágeis (quebram) — o antifrágil beneficia-se do caos.
- **Lei de Lindy**: a expectativa de vida futura de uma ideia, tecnologia ou instituição não-perecível é proporcional à sua idade atual. O que existe há muito tempo tende a existir por mais tempo.
- **Regressão à Média (Galton)**: após um evento extremo, o próximo evento tende a ser mais próximo da média. Ignorar este princípio leva a superstições e falácias.
- **Segundo Nível de Pensamento (Howard Marks)**: pensar sobre o que os outros estão pensando, não apenas sobre o objeto do pensamento. "Primeiro nível: essa empresa vai bem, compro. Segundo nível: essa empresa vai bem e todo mundo sabe, então está sobrevalorizada — não compro."

## Direito

- **Pirâmide de Kelsen**: hierarquia das normas jurídicas. Constituição (topo) → leis complementares e ordinárias → decretos, portarias, instruções normativas. Norma inferior só é válida se compatível com norma superior.
- **Cláusulas Pétreas (CF/88, Art. 60 §4º)**: dispositivos constitucionais que não podem ser abolidos por emenda: forma federativa de Estado, voto direto, separação dos Poderes, direitos e garantias individuais.
- **Due Process of Law (Devido Processo Legal)**: princípio que garante a todos os litigantes o direito a um processo justo, com contraditório, ampla defesa, juiz natural e duração razoável (CF/88 Art. 5º, LIV-LV).

---

## IA e Agentes

- **MCP (Model Context Protocol)**: protocolo de comunicação entre IAs e sistemas locais (arquivos, terminais, bancos de dados). Permite que agentes de IA acessem ferramentas e recursos do sistema de forma padronizada e segura.
- **RAG (Retrieval Augmented Generation)**: processo de fornecer contexto pesquisado em tempo real para o LLM durante a geração de resposta. Combina recuperação de informação (de uma base de conhecimento, vetores, internet) com geração de linguagem natural. Reduz alucinações e permite respostas atualizadas.
- **Neural Indexing**: otimização semântica das notas para facilitar a busca por IA. Técnicas: embeddings de notas, chunking otimizado, metadados estruturados, tagging consistente, hierarquia de diretórios navegável.
- **Sub-persona**: modo de operação especializado de um agente de IA (ex.: Coder, Strategist, Analyst, Tutor). Cada sub-persona tem instruções, estilo de comunicação e conhecimento especializado adaptados a um domínio de tarefa.
- **LLM (Large Language Model)**: modelo de linguagem de grande escala treinado em vastos corpora textuais usando arquitetura Transformer. Ex.: GPT-4, Claude, Gemini, Llama. Capacidade de gerar texto, responder perguntas, resumir, traduzir, programar e raciocinar.
- **Alucinação (Hallucination)**: geração de informação factualmente incorreta ou inventada por um LLM, apresentada com confiança. Causada por limitações do treinamento, falta de grounding em fontes confiáveis, ou lacunas no conhecimento do modelo.
- **Prompt Engineering**: prática de projetar e refinar instruções (prompts) para eliciar respostas desejadas de LLMs. Técnicas: few-shot prompting, chain-of-thought, persona prompting, system prompts, structured outputs.

---

## Organização do Vault

- **Tiered Architecture**: estrutura em camadas (01-05) baseada na importância e temporalidade do dado. Quanto menor o número, mais ativo e imediato; quanto maior, mais permanente e referencial.
- **Neural Hub**: nota raiz que serve como ponto de entrada principal para o vault (ex.: `Bem-vindo.md`). Contém links para todos os hubs secundários e índices de área.
- **MOC (Map of Content)**: nota que atua como índice dinâmico para um domínio, listando e descrevendo todas as notas relevantes com links e metadados.
- **Active Project**: qualquer projeto com foco imediato e registro em `01-Ativos`. Tem cronograma, tasks e métricas de progresso.
- **Second Brain**: conceito de estender a memória e cognição humana através de um sistema externo de notas interligadas (Obsidian, Notion, Roam). O vault atua como "cérebro externo" de Will.

---

## Engenharia & Stack

- **Local LLM**: modelos de linguagem rodando localmente na máquina do usuário (Ollama, LM Studio, llama.cpp). Vantagens: privacidade, sem custo de API, personalização. Desvantagens: requer VRAM, modelos menores que APIs.
- **VRAM Offloading**: técnica para rodar modelos maiores que a memória VRAM disponível, movendo camadas entre GPU e RAM do sistema. Permite executar modelos de 70B+ parâmetros em hardware consumidor com quantização e offloading.
- **Quantização**: redução da precisão numérica dos pesos de um modelo (ex.: FP32 → INT8, FP16 → 4 bits) para reduzir uso de memória e acelerar inferência, com perda mínima de qualidade. Técnica essencial para rodar LLMs localmente.
- **Fine-Tuning**: processo de treinamento adicional de um modelo pré-treinado em dados específicos de um domínio ou tarefa. Mais eficiente que treinar do zero. Ex.: fine-tuning de Llama 3 em dados jurídicos.
- **LoRA (Low-Rank Adaptation)**: técnica de fine-tuning eficiente que congela os pesos originais e treina matrizes de baixa rank adaptadoras. Reduz drasticamente o número de parâmetros treináveis e o requisito de memória.
- **Embedding Model**: modelo que converte texto (ou outras modalidades) em vetores densos de alta dimensionalidade. Usado para busca semântica, clustering, classificação e RAG. Ex.: all-MiniLM-L6-v2, text-embedding-3-small.

---

*Mantenha este glossário atualizado ao introduzir novas tecnologias ou workflows.*
