---
title: "Vigilância Algorítmica"
area: "Tecnologia e Sociedade"
related: ["Panóptico Digital", "Privacidade", "Capitalismo de Vigilância", "Viés Algorítmico", "Privacidade de Dados"]
embeddings_model: "all-MiniLM-L6-v2"
tags: [conhecimento, conceito, tecnologia, vigilancia, algoritmo, privacidade, biometria]
updated: 2026-05-16
---

# Vigilância Algorítmica

## Definição e Escopo

Vigilância algorítmica é o monitoramento automatizado de comportamentos, comunicações e movimentações por meio de sistemas computacionais que processam grandes volumes de dados em tempo real. Diferentemente da vigilância tradicional — exercida por seres humanos com recursos limitados de atenção e memória —, a vigilância algorítmica opera em **escala massiva**, com **velocidade instantânea** e de forma **invisível** para os sujeitos monitorados.

### Características Distintivas

| Aspecto | Vigilância Tradicional | Vigilância Algorítmica |
|---------|----------------------|------------------------|
| **Escala** | Centenas de pessoas | Milhões de pessoas simultaneamente |
| **Velocidade** | Tempo real humano | Processamento em milissegundos |
| **Custo marginal** | Alto (salários, infraestrutura física) | Próximo de zero (automatizado) |
| **Visibilidade** | Geralmente visível (câmeras, agentes) | Frequentemente invisível (rastreamento passivo) |
| **Memória** | Limitada, sujeita a falhas | Perfect recall, armazenamento indefinido |
| **Análise** | Manual, interpretativa | Automatizada, estatística, preditiva |

O escopo da vigilância algorítmica abrange desde o rastreamento de cliques em websites até o monitoramento biométrico em espaços públicos, passando pela análise preditiva de comportamentos futuros.

### Definição Operacional

Para fins analíticos, podemos definir vigilância algorítmica como:

> **VA** = (Coleta_Sistemática ∘ Agregação ∘ Análise ∘ Predição ∘ Modificação_Comportamental)

Onde cada operador representa a transformação de dados brutos em mecanismos de controle social.

## História e Evolução

### Pré-História (Século XIX — 1980)

As raízes da vigilância algorítmica remontam a sistemas analógicos de classificação e monitoramento:

- **Fichamento policial**: sistemas de arquivamento de suspeitos, impressões digitais (Galton, 1892)
- **Bertillonage**: sistema antropométrico de Alphonse Bertillon (1883) para identificação de criminosos reincidentes
- **Censos e estatísticas populacionais**: base para classificação demográfica (Foucault, *Segurança, Território, População*, 1977)
- **Cartões perfurados**: Herman Hollerith (1890) — tabulação mecânica de dados do censo norte-americano, precursora da IBM

O [[Conhecimento-Geral/Tecnologia-e-Sociedade/Panoptico-Digital|Panóptico Digital]] tem suas raízes nesses sistemas de classificação e vigilância.

### Década de 1950–1970: Computação e Burocracia

- **Computadores mainframe** para processamento de dados governamentais e corporativos
- **Bancos de dados centralizados** (bancos, governos, seguradoras)
- **Primeiros sistemas de matching** de registros entre agências governamentais
- Lyon (2001) descreve essa fase como "vigilância burocrática"

### Década de 1980–1990: Scoring e Risco

- **FICO** (Fair, Isaac and Company, 1956–1980s): credit scoring automatizado
- **Surgimento dos data brokers** (Acxiom, 1969; Experian, 1996)
- **Sistemas de scoring** para seguros, crédito, emprego
- Foucault (1978) associava essas práticas ao "biopoder" — gestão estatística das populações

### Década de 2000: Rastreamento Digital

- **Google** (1998): PageRank e rastreamento de cliques para publicidade
- **DoubleClick** (1996–2008): primeiros cookies de rastreamento cross-site
- **Facebook** (2004): perfilamento social, curtidas, rede de contatos
- **Target** (2002–2012): análise preditiva de compras para identificar gestantes (caso amplamente citado por Duhigg, 2012)
- **Cookies de terceiros**, pixels, web beacons

Essa década estabeleceu a infraestrutura técnica do que Zuboff (2019) chamaria de "capitalismo de vigilância".

### Década de 2010: Big Data e Aprendizado de Máquina

- Explosão de dados (volume, velocidade, variedade)
- **Machine learning** aplicado a perfis comportamentais
- **Facebook-Cambridge Analytica** (2013–2016): perfilamento psicológico para manipulação política
- **PRISM** (Edward Snowden, 2013): revelações sobre vigilância governamental em massa da NSA
- **Policiamento preditivo**: PredPol, HunchLab (2012–2018)
- **Sistemas de recomendação** como mecanismos de modulação comportamental (YouTube, TikTok, Netflix)
- Lançamento da **LGPD** (Brasil, 2018) em resposta à crescente vigilância

### Década de 2020: IA Generativa e Vigilância em Tempo Real

- **Reconhecimento facial ubíquo**: Clearview AI, AnyVision, NEC
- **IA generativa**: ChatGPT, modelos de linguagem como mecanismos de vigilância e modulação
- **Sistemas de crédito social**: implementação na China (Xinjiang, 2017–presente)
- **Vigilância pandêmica**: contato tracking durante COVID-19 (Apple/Google Exposure Notification, 2020)
- **Regulação**: EU AI Act (2024), LGPD em implementação, debate global
- **Emoção e afeto computacional**: análise de sentimentos em tempo real em call centers, salas de aula, entrevistas

## Métodos e Técnicas

### Tracking (Rastreamento)

O rastreamento comportamental é a camada fundamental da vigilância algorítmica:

- **Cookies HTTP**: cookies de sessão, cookies persistentes, cookies de terceiros (third-party cookies)
- **Pixels de rastreamento**: imagens invisíveis de 1×1 pixel embutidas em emails e páginas
- **Browser fingerprinting**: coleta de ~30+ parâmetros do navegador (Canvas fingerprint, WebGL, fontes instaladas, resolução de tela, timezone, plugins) para criar identificador único
- **Device fingerprinting**: IMEI, MAC address, advertising ID (IDFA no iOS, GAID no Android)
- **Supercookies**: identificadores inseridos por provedores de internet (ISP) no nível do protocolo HTTP
- **ETags** e **localStorage**: técnicas de re-spawning de cookies mesmo após exclusão
- **Cross-device tracking**: vinculação de múltiplos dispositivos ao mesmo usuário via login, WiFi, IP
- **IP tracking**: geolocalização aproximada, provedor, fingerprint de rede

Mayer-Schönberger & Cukier (2013) descrevem o tracking como "a digitalização da experiência humana".

### Profiling (Perfilamento)

O perfilamento envolve a inferência de atributos demográficos, psicológicos e comportamentais a partir de dados aparentemente inocentes:

- **Inferência demográfica**: idade, gênero, raça, renda, escolaridade
- **Inferência psicográfica**: personalidade (Big Five), valores, crenças
- **Inferência política**: orientação partidária, engajamento cívico
- **Inferência religiosa**: filiação, frequência, intensidade
- **Inferência de saúde**: condições médicas, medicações, risco de doenças
- **Inferência de orientação sexual**: baseada em padrões de navegação, curtidas, amizades
- **Inferência de redes sociais**: conexões, hierarquia social, influenciadores

Kosinski, Stillwell & Graepel (2013, *PNAS*) demonstraram que curtidas no Facebook permitem prever orientação sexual (88%), etnia (95%), religião (82%) e personalidade com alta acurácia.

### Scoring (Pontuação)

Sistemas de scoring atribuem pontuações numéricas a indivíduos para classificação e tomada de decisão automatizada:

| Tipo de Scoring | Exemplo | Aplicação |
|----------------|---------|-----------|
| **Credit scoring** | FICO, Serasa Score, Score Boa Vista | Aprovação de empréstimos, cartões de crédito |
| **Insurance scoring** | Insurance Risk Score | Cálculo de prêmios de seguro |
| **Employability score** | HireRight, GoodHire | Triagem de currículos, verificação de antecedentes |
| **Social credit** | Sistema de Crédito Social Chinês | Acesso a transporte, crédito, viagens |
| **Healthcare score** | Risk adjustment scores (e.g., HCC) | Priorização de pacientes, custos de plano de saúde |
| **Tenant score** | CoreLogic, TransUnion SmartMove | Aprovação de aluguel |
| **Fraud score** | FICO Falcon | Detecção de fraude em transações |
| **Education score** | ENEM, vestibulares, nota de corte | Acesso ao ensino superior |

Pasquale (2015) denomina essas pontuações de "reputação algorítmica": scores invisíveis que determinam oportunidades de vida sem transparência ou recurso.

### Classificação e Segmentação

- **Clusterização**: k-means, DBSCAN, hierárquico — agrupamento de perfis
- **Classificação supervisionada**: regressão logística, random forest, SVM, redes neurais
- **Labeling automático**: aplicação de tags sociodemográficas (e.g., "Millennial urbano", "Mãe trabalhadora")
- **Lookalike audiences**: expansão de audiências por similaridade (Facebook Lookalike, Google Similar Audiences)

Cada classificação cria aquilo que Bowker & Star (1999, *Sorting Things Out*) chamam de "infraestruturas de classificação": categorias que estruturam a percepção e ação social.

### Predição

Sistemas preditivos usam dados históricos para estimar comportamentos futuros:

- **Policiamento preditivo**: PredPol, HunchLab, CrimeScan — algoritmos que mapeiam "hotspots" de crime futuro
- **Predição de evasão escolar**: sistemas como Early Warning Systems detectam alunos com alto risco de abandono
- **Predição de churn**: identificação de clientes com alta probabilidade de cancelamento
- **Predição de desempenho**: análise de produtividade, risco de turnover
- **Predição de recidivismo**: COMPAS, PSA, LSI-R — sistemas usados no sistema judicial

O'Neil (2016) adverte que modelos preditivos aplicados a populações vulneráveis criam "armas de destruição matemática" — loops de feedback negativo que exacerbam desigualdades.

### Reconhecimento Biométrico

- **Reconhecimento facial**: FaceNet (Google), DeepFace (Facebook), ArcFace
- **Reconhecimento de íris**: sistemas Aadhaar (Índia, 1.2B cadastrados)
- **Reconhecimento de voz**: análise de tom, frequência, sotaque
- **Reconhecimento de emoções**: Affectiva, RealEyes — análise microexpressões
- **Reconhecimento de marcha**: análise do padrão de caminhada à distância
- **Reconhecimento de digitais**: integração em dispositivos móveis, controle de fronteiras

[[Conhecimento-Geral/Tecnologia-e-Sociedade/Vigilancia-Algoritmica|Vigilância Algorítmica]] biométrica representa a materialização mais visível do controle algorítmico sobre corpos no espaço público.

## Shoshana Zuboff e Capitalismo de Vigilância

### Definição Central

Shoshana Zuboff (2019) define capitalismo de vigilância como:

> *"Um novo ordem econômico que reivindica a experiência humana como matéria-prima gratuita para práticas comerciais ocultas de extração, predição e vendas."*

Diferentemente do capitalismo industrial — que extraía recursos naturais —, o capitalismo de vigilância extrai **comportamento humano** como matéria-prima.

### Mecanismos de Extração Comportamental

1. **Declaração unilateral**: empresas declaram unilateralmente que certos domínios da experiência humana (navegação, localização, interações sociais) pertencem a elas
2. **Ocultação**: a vigilância é invisível, os termos de serviço são ilegíveis, o consentimento é fictício
3. **Assimetria de poder**: o vigilante sabe quase tudo; o vigiado sabe quase nada sobre o que é coletado
4. **Coerção**: a participação é compulsória — "se não paga pelo produto, você é o produto"

### Excedentes Comportamentais (Behavioral Surplus)

Zuboff introduz o conceito de **excedente comportamental**:

> Dados comportamentais muito mais abundantes e granulares do que o necessário para melhorar o serviço principal.

- **Google Search**: usa dados de clique para melhorar resultados (propósito declarado). Excedente: cada clique não usado para melhoria do buscador vira matéria-prima para publicidade preditiva.
- **Facebook**: usa curtidas para melhorar feed (propósito declarado). Excedente: inferências sobre personalidade, humor, vulnerabilidades para vender anúncios direcionados.
- **Uber**: dados de corrida para melhorar rotas (propósito declarado). Excedente: previsão de demanda em tempo real para ajuste dinâmico de preços.

### Mercados de Comportamentos Futuros

A inovação radical do capitalismo de vigilância é a criação de **mercados de comportamentos futuros**:

> Não se trata de vender o que o usuário *quer* comprar, mas de modular o que ele *vai querer* comprar.

- **Economia da atenção**: captura e revenda da atenção humana como commodity
- **Economia da predição**: venda de previsões sobre comportamento futuro
- **Economia da modificação**: venda da capacidade de modificar comportamento

### Meios de Modificação Comportamental

Zuboff contrasta os **meios de produção** (Marx) com os **meios de modificação comportamental**:

| | Meios de Produção | Meios de Modificação Comportamental |
|---------------|------------------|-----------------------------------|
| **Recurso** | Matéria-prima natural | Experiência humana |
| **Processo** | Fabrico industrial | Extração de dados + predição + modificação |
| **Produto** | Bens materiais | Comportamentos futuros |
| **Controle** | Sobre trabalhadores | Sobre populações inteiras |
| **Conhecimento** | Técnico-operacional | Psicológico-preditivo |
| **Poder** | Econômico | Comportamental (nudging, manipulação) |

> *"O capitalismo de vigilância não é sobre o que 'fazemos' na internet. É sobre o que a internet faz conosco."* — Zuboff (2019)

A [[Conhecimento-Geral/Filosofia/Problema-do-Controle|Problema do Controle]] é redefinido aqui: o controle não é mais exercido pela coerção direta, mas pela modulação algorítmica de desejos e escolhas.

## Vigilância no Trabalho

### Contexto Histórico

O monitoramento do trabalho não é novo. Taylor (1911, *The Principles of Scientific Management*) já propunha a observação sistemática dos movimentos dos trabalhadores. Porém, a escala e granularidade da vigilância algorítmica são inéditas.

### Formas de Monitoramento

**Workplace surveillance technologies (WST)**:

- **Keylogging**: registro de cada tecla pressionada no teclado corporativo
- **Mouse tracking**: análise de movimentos do mouse, clicks, pausas
- **Screen capture**: captura de tela em intervalos regulares (ex.: Teramind, Time Doctor)
- **Webcam monitoring**: registro visual do trabalhador via câmera do notebook
- **Email and chat monitoring**: análise de conteúdo, tom, frequência de comunicações
- **Active window tracking**: registro de qual janela/software está em foco
- **Productivity scoring**: métricas de produtividade baseadas em atividade
- **Idle time detection**: detecção de inatividade (mouse jigglers como contra-medida)

### Casos Emblemáticos

**Amazon Warehouses (2014–presente)**:

- Rastreadores em cada funcionário monitoram ritmo de separação de produtos
- Sistema gera automaticamente **avisos de performance** sem intervenção humana
- Métricas de produtividade geram demissões automáticas com base em percentis
- Bloomberg (2019) reportou que a Amazon demitiu centenas de funcionários por não atingirem métricas geradas por IA
- Movimentos repetitivos monitorados: cada pausa é registrada como "time off task"

**Uber e Gig Economy**:

- Algoritmo define rotas, preços (surge pricing), aceitação de corridas
- **Algorithmic management**: o gerente é substituído por um algoritmo que aloca tarefas, avalia desempenho e toma decisões de desligamento
- **Deactivation**: motoristas podem ser desativados (demitidos) sem explicação humana
- **Rate scoring**: rating de 1-5 determina acesso à plataforma
- Rosenblat (2018, *Uberland*) documenta a assimetria de informação entre Uber e motoristas

**Call Centers**:

- Monitoramento de áudio em tempo real com análise de sentimentos
- Palavras-chave detectadas e sinalizadas para supervisores
- **Emotion AI**: detecção de frustração do cliente e estresse do atendente
- Métricas: tempo médio de atendimento (TMA), tempo de espera, resolução no primeiro contato

**Remote Work (Pós-2020)**:

- Explosão de ferramentas de monitoramento durante a pandemia
- Empresas como **Upwork**, **Fiverr**, **Toptal** monitoram horas trabalhadas via screenshots
- Ferramentas de **bossware** (ex.: ActivTrak, Hubstaff, Time Doctor) cresceram 200% entre 2020–2022
- **Mouse jigglers** (físicos e de software) como contra-medida popular

### Consequências

- **Estresse e ansiedade**: sensação constante de vigilância reduz bem-estar
- **Comportamento adaptativo**: trabalhadores otimizam métricas em vez de qualidade
- **Perda de autonomia**: erosão da discricionariedade profissional
- **Desumanização**: redução do trabalhador a métricas e scores
- **Falsa objetividade**: métricas são tratadas como objetivas, mas carregam vieses de design

> *"A métrica não é a coisa. É uma representação imperfeita e muitas vezes distorcida."* — Muller (2018, *The Tyranny of Metrics*)

## Vigilância Facial e Biométrica

### Tecnologias de Reconhecimento Facial

O reconhecimento facial (RF) evoluiu significativamente com deep learning:

- **DeepFace** (Facebook/Meta, 2014): acurácia de 97.35% no Labeled Faces in the Wild (LFW)
- **FaceNet** (Google, 2015): embeddings faciais de 128 dimensões, acurácia de 99.63%
- **ArcFace** (Deng et al., 2019): abordagem com additive angular margin loss
- **InsightFace** (2020): código aberto para RF, amplamente adotado

O pipeline típico:

```
Imagem → Detecção facial (MTCNN, RetinaFace) → Alinhamento → Embedding (FaceNet/ArcFace)
→ Matching (cosine similarity) → Identificação ou Verificação
```

### Empresas e Produtos

- **Clearview AI**: scraper de 30+ bilhões de imagens de redes sociais (Facebook, YouTube, LinkedIn) para criar banco de dados facial. Vendido para 2,400+ agências policiais nos EUA. Controversamente usado pelo FBI, ICE (Brandom, 2020, *The Verge*)
- **FaceFirst**: reconhecimento facial para varejo e segurança aeroportuária
- **NEC NeoFace**: usado em aeroportos (incluindo GRU em São Paulo), Olimpíadas Tóquio 2020
- **AnyVision**: RF em tempo real para câmeras de vigilância
- **SenseTime**, **Megvii (Face++)**: gigantes chineses de visão computacional

### Casos de Uso

**China — Xinjiang (2017–presente)**:

- O maior sistema de vigilância do mundo: ~2 milhões de câmeras em Xinjiang (uma para cada 4 pessoas)
- Reconhecimento facial combinado com pulseiras RFID e análise de movimento
- Sistema de crédito social integrado com RF para controle de populações uigures
- Adrian Zenz (2019, *Journal of Political Risk*) documenta campos de "re-educação" baseados em perfis algorítmicos

**Londres**:

- Met Police: sistema de RF em tempo real em eventos públicos (Notting Hill Carnival, Natal)
- Aproximadamente 1,500 câmeras de RF na cidade até 2023
- Estudo da Big Brother Watch (2020): 98% dos alertas de RF da polícia de Londres eram falsos positivos
- Lei de Segurança Pública (2022) expandiu uso de RF

**São Paulo — Metrô e Aeroportos**:

- Metrô de São Paulo: projeto de reconhecimento facial em 2021 (suspendido por questões legais)
- GRU Airport: sistema NEC NeoFace para imigração (e-Passport Gates)
- Lei Municipal 17.734/2022: proibição do uso de RF em espaços públicos por empresas privadas (ainda em debate)

**Estados Unidos**:

- **Porto de entrada**: RF em aeroportos para cidadãos americanos (fotografia obrigatória)
- **Polícia local**: Detroit, NYPD, Orlando — uso generalizado em operações
- **Moratória**: cidades de São Francisco (2019), Boston, Portland proibiram uso governamental de RF

### Vieses Raciais em Reconhecimento Facial

**Gender Shades (Buolamwini & Gebru, 2018, *Proceedings of FAT*)**:

Estudo seminal que testou três sistemas comerciais de RF (Microsoft, IBM, Face++):

| Grupo | Acurácia |
|-------|----------|
| Homens brancos | 99.0–100% |
| Homens negros | 88.0–99.3% |
| Mulheres brancas | 92.5–98.1% |
| Mulheres negras | 65.3–79.2% |

**Conclusões**:
- Quanto mais escura a pele e mais feminino o gênero, **menor a acurácia**
- Disparidade de até 34 pontos percentuais entre grupos
- Ausência de dados de treinamento diversos (75%+ rostos brancos, ~80% masculinos)

**Impactos**:
- Falsos positivos mais frequentes para pessoas negras em aplicações policiais → detenções injustas
- Caso Robert Williams (Detroit, 2020): preso por 30 horas devido a falso positivo de RF
- Caso Porcha Woodruff (Detroit, 2023): presa grávida de 8 meses por falso positivo

### Reconhecimento de Emoções

Tecnologia controversa que alega detectar emoções a partir de microexpressões faciais:

- **Criticada fortemente** por Barrett et al. (2019, *Psychological Science in the Public Interest*): emoções não têm assinaturas faciais universais confiáveis
- **Empresas**: Affectiva (fundada por Rosalind Picard, MIT Media Lab), RealEyes
- **Uso**: entrevistas de emprego (HireVue), call centers, salas de aula na China
- EU AI Act (2024) **proibiu** uso de sistemas de reconhecimento de emoções em locais de trabalho e educação na UE

[[Conhecimento-Geral/Psicologia/Vieses-em-LLMs|Vieses em LLMs]] compartilha raízes com o viés em RF: dados de treinamento não representativos levam a decisões discriminatórias.

## Vigilância Preditiva

### Definição e Base Teórica

Vigilância preditiva usa modelos estatísticos e de machine learning para prever eventos futuros — crimes, abuso infantil, evasão escolar, inadimplência — e intervir preventivamente.

O modelo conceitual:

```
Dados históricos → Treinamento de modelo → Predição → Intervenção → Novo dado → Retreinamento
```

### Policiamento Preditivo

**PredPol (Preditive Policing)**:

- Desenvolvido por pesquisadores da UCLA (2011)
- Usa dados de crimes passados (tipo, local, horário) para prever "hotspots" de crime futuro
- Baseado em algoritmos inicialmente usados para prever terremotos (Epidemic-Type Aftershock Sequence model)
- Adotado por 60+ departamentos de polícia nos EUA (LAPD, Chicago PD, Kent PD)

**HunchLab**:

- Similar ao PredPol, mas incorpora fatores socioeconômicos, clima, eventos locais
- Adquirido pela ShotSpotter (2014)
- Criticado por codificar viés policial histórico → profecias autorrealizáveis

**Críticas**:

1. **Profecias autorrealizáveis**: a polícia patrulha áreas apontadas pelo algoritmo → descobre mais crimes nos locais preditos → valida o modelo → ciclo vicioso
2. **Viés histórico**: dados de crimes históricos refletem vieses policiais (policiamento mais intenso em áreas negras e pobres)
3. **Deslocamento**: crime não é evitado, apenas deslocado para áreas não monitoradas
4. **Transparência zero**: PredPol e HunchLab são algoritmos proprietários sem auditoria independente
5. **Falsa precisão**: a precisão preditiva é frequentemente superestimada; Benjamin (2019) demonstra que alegações de 80%+ precisão são metodologicamente frágeis

**Estudo de caso — Chicago PD Strategic Subject List (2012–2019)**:

- Algoritmo que gerava "heat list" de indivíduos em maior risco de envolvimento em tiroteios
- Baseado em: prisões anteriores, associação com gangues, idade, histórico de violência
- Auditado pelo RAND Corporation (2019): acurácia preditiva marginalmente melhor que uma linha base simples (regra de 80/20)
- Levou a abordagens policiais preventivas, assédio, violação de direitos civis

### Allegheny Family Screening Tool (AFST)

Desenvolvido para o condado de Allegheny (Pensilvânia, EUA) para predição de risco de abuso infantil:

- Input: dados do sistema de saúde, assistência social, histórico criminal, uso de serviços públicos
- Output: score de risco de 1 a 20
- Usado para triagem de denúncias de abuso infantil

**Críticas de Eubanks (2018, *Automating Inequality*)**:

1. **Viés de classe**: famílias pobres são mais monitoradas por serviços públicos → mais dados no sistema → scores mais altos
2. **Falsos positivos**: famílias marcadas como "alto risco" são investigadas com mais frequência
3. **Erosão da privacidade**: para ser "invisível" ao sistema, é preciso não usar serviços públicos
4. **Ciclo de pobreza**: a vigilância preditiva pune a pobreza com mais vigilância

> *"Quando você automatiza a desigualdade, você a torna invisível e implacável."* — Eubanks (2018)

### Predição Educacional

Sistemas de **Early Warning** para evasão escolar:

- Input: frequência, notas, comportamento, dados demográficos
- Output: probabilidade de abandono escolar
- Uso: alocação de recursos de intervenção

Noble (2018, *Algorithms of Oppression*) documenta como esses sistemas podem canalizar alunos negros e latinos para programas vocacionais em vez de acadêmicos, reproduzindo segregação educacional.

## Vigilância Governamental e Espionagem

### Revelações de Snowden (2013)

Edward Snowden, ex-contratado da NSA, revelou programas globais de vigilância:

- **PRISM**: acesso direto da NSA a servidores de Google, Apple, Microsoft, Facebook, Yahoo, Skype, YouTube
- **XKEYSCORE**: sistema de busca e análise em massa de dados de internet
- **BULLRUN**: enfraquecimento proposital de padrões criptográficos
- **MUSCULAR**: interceptação de cabos de fibra óptica entre data centers do Google e Yahoo
- **TEMPESTA**: captura de emissões eletromagnéticas de computadores

Greenwald (2014, *No Place to Hide*) documenta o alcance global desses programas.

### Sistemas de Vigilância Estatal

- **China — Sistema de Crédito Social** (2014–presente): vigilância integrada com pontuação social que afeta acesso a crédito, viagens, empregos
- **Rússia — SORM** (Sistema de Medidas Operacionais de Investigação): interceptação legal de todas as comunicações
- **Índia — Aadhaar**: maior banco de dados biométrico do mundo (1.2 bilhão de registros), vinculado a serviços governamentais
- **Reino Unido — Investigatory Powers Act (2016)**: "Snoopers' Charter" — obriga ISPs a armazenar histórico de navegação
- **Brasil — ABIN e Monitoramento**: discussão sobre acesso a dados de cidadãos sem autorização judicial (ADI 6392 no STF)

## Resistência e Contra-Medidas

### Criptografia e Privacidade Tecnológica

- **Signal**: mensageiro com criptografia de ponta a ponta (Signal Protocol), código aberto, sem coleta de metadados
- **Tor (The Onion Router)**: rede de anonimização por roteamento em camadas (onion routing). Desenvolvido inicialmente pelo Naval Research Lab dos EUA
- **VPN (Virtual Private Network)**: túneis criptografados que escondem IP e tráfego do ISP (mas não necessariamente do provedor de VPN)
- **DNS over HTTPS (DoH)**: criptografia de consultas DNS para evitar monitoramento por ISPs
- **ProtonMail / Tutanota**: email criptografado de ponta a ponta
- **Brave Browser**: bloqueio de rastreadores e anúncios por padrão

### Obfuscação

Técnica que envolve "afogar" sistemas de vigilância com dados falsos ou ruído:

- **AdNauseam**: extensão que clica em todos os anúncios para confundir perfis publicitários
- **TrackMeNot**: plugin que realiza buscas aleatórias para ocultar padrões reais de pesquisa
- **Data Poisons**: técnicas adversarial ML que adicionam ruído sutil a dados para degradar modelos de perfilamento
- **Cadaveri di Dati (cadáveres de dados)**: geradores de dados sintéticos para confundir scraping
- **Face blurring**: uso de software como Image Scrubber para borrar rostos em fotos publicadas online

Brunton & Nissenbaum (2015, *Obfuscation: A User's Guide for Privacy and Protest*) argumentam que a obfuscação é uma forma legítima de resistência contra vigilância em massa.

### Regulamentação e Legislação

**GDPR (General Data Protection Regulation)** — União Europeia, 2018:

- Marco regulatório mais abrangente do mundo
- Consentimento explícito para coleta de dados
- Direito ao esquecimento (right to erasure)
- Portabilidade de dados
- Obrigação de notificação de violações
- Multas de até 4% do faturamento global
- Art. 22: direito a não ser submetido a decisões automatizadas exclusivamente

**LGPD (Lei Geral de Proteção de Dados)** — Brasil, Lei 13.709/2018 (vigência 2020):

- Inspirada no GDPR
- Bases legais para tratamento de dados (consentimento, legítimo interesse, etc.)
- Direitos do titular (acesso, correção, anonimização, portabilidade, exclusão)
- Autoridade Nacional de Proteção de Dados (ANPD)
- Sanções administrativas

**EU AI Act** — União Europeia, 2024:

- Classificação de risco para sistemas de IA (inaceitável, alto, limitado, mínimo)
- **Proibido**: sistemas de crédito social, reconhecimento de emoções no trabalho/escola, vigilância biométrica em tempo real em espaços públicos (com exceções)
- **Alto risco**: recrutamento, avaliação de crédito, policing preditivo — sujeitos a avaliação de conformidade
- Transparência obrigatória para sistemas de IA generativa

**Leis no Brasil em debate**:

- PL 2338/2023: regulamentação de IA inspirada no EU AI Act
- ADI 6392: análise de constitucionalidade do compartilhamento de dados de cidadãos
- Marco Civil da Internet (Lei 12.965/2014): neutralidade de rede, guarda de registros

### Movimentos Sociais e Ativismo

- **#DeleteFacebook** (2018): campanha pós-Cambridge Analytica
- **Apple Privacy Campaign**: "Privacy. That's iPhone" (2019–presente)
- **Mozilla Foundation**: campanhas por privacidade, Pocket, Firefox containers
- **Electronic Frontier Foundation (EFF)**: litígio e defesa de direitos digitais
- **Algorithmic Justice League** (Joy Buolamwini): combate a vieses algorítmicos
- **Data Justice Lab** (Cardiff University): pesquisa sobre justiça de dados
- **Direitos Humanos e Vigilância: Coalizão** de ONGs (Conectas, Artigo 19, InternetLab no Brasil)

### Resistência Individual vs. Coletiva

É importante distinguir:

| Resistência Individual | Resistência Coletiva |
|----------------------|---------------------|
| Usar VPN, Tor, Signal | Advocacia legislativa |
| Bloquear cookies | Litígio estratégico |
| Apagar dados de brokers | Boicotes organizados |
| Não usar plataformas vigilantes | Greves, protestos |
| Obfuscação pessoal | Alternativas comunitárias (fediverso, software livre) |

> *"A privacidade não pode ser resolvida como um problema de consumo individual. Ela exige ação política coletiva."* — Zuboff (2019)

## Panorama Legal e Ético

### Dilemas Éticos Fundamentais

1. **Consentimento informado vs. assimetria de poder**: é possível consentir livremente quando a alternativa é a exclusão digital?
2. **Segurança vs. privacidade**: a falsa dicotomia de que é preciso sacrificar um pelo outro
3. **Eficiência vs. justiça**: sistemas algorítmicos otimizam eficiência, mas à custa de quais valores?
4. **Transparência vs. segredo industrial**: algoritmos proprietários vs. direito de defesa
5. **Autonomia vs. modulação**: até que ponto nossas escolhas são realmente livres sob vigilância?

### Marcos Legais Comparativos

| País/Região | Lei Principal | Vigilância Biométrica | Proteção |
|-------------|--------------|----------------------|----------|
| **União Europeia** | GDPR + EU AI Act | Restrita (proibida em espaços públicos, com exceções) | Alta |
| **Brasil** | LGPD + Marco Civil | Em debate, restrições incipientes | Média |
| **EUA (federal)** | Sem lei federal abrangente | Permitida, regulação local fragmentada | Baixa |
| **China** | PIPL + CSL | Amplamente permitida e implementada | Mínima (perspectiva liberal); máxima (perspectiva estatal) |
| **Índia** | PDP Bill (2023) | Aadhaar obrigatório para serviços públicos | Em desenvolvimento |

### Teorias Éticas Aplicadas

- **Utilitarismo**: vigilância algorítmica maximiza bem-estar (menos crime, mais eficiência) vs. sofrimento causado por vieses e perda de liberdade
- **Deontologia kantiana**: tratamento de pessoas como fins, não meios — vigilância instrumentaliza o indivíduo
- **Ética do cuidado**: a vigilância algorítmica negligencia relações de confiança e vulnerabilidade
- **Teoria crítica (Foucault, Deleuze)**: do panóptico disciplinar à sociedades de controle — algoritmos como tecnologia de governo
- **Justiça distributiva (Rawls)**: vigilância algorítmica afeta desproporcionalmente os menos favorecidos

## Código Python: Exemplos Práticos

### 1. Simulação de Perfilamento Algorítmico

O exemplo abaixo demonstra como inferir atributos demográficos a partir de dados comportamentais simples — similar ao que data brokers e plataformas fazem:

```python
"""
Simulação de perfilamento algorítmico.
Autor: Baseado em conceitos de Kosinski et al. (2013) e Zuboff (2019)
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder

# Simula dados comportamentais de 5000 usuários
np.random.seed(42)
n_users = 5000

# Gera dados sintéticos
data = {
    "usuario_id": range(n_users),
    # Horas de navegação por dia
    "horas_online": np.random.exponential(scale=3, size=n_users),
    # Número de sites de notícias visitados
    "sites_noticias": np.random.poisson(lam=5, size=n_users),
    # Número de posts em redes sociais por dia
    "posts_por_dia": np.random.poisson(lam=2, size=n_users),
    # Frequência de compras online (por mês)
    "compras_mes": np.random.poisson(lam=1.5, size=n_users),
    # Número de buscas por dia
    "buscas_dia": np.random.poisson(lam=10, size=n_users),
    # Tempo gasto em sites de entretenimento (%)
    "pct_entretenimento": np.random.beta(a=2, b=5, size=n_users),
    # Tempo gasto em sites educacionais (%)
    "pct_educacao": np.random.beta(a=3, b=4, size=n_users),
    # Tempo gasto em redes sociais (%)
    "pct_social": np.random.beta(a=3, b=3, size=n_users),
    # Idade (para criar correlação com comportamentos)
    "idade_categoria": np.random.choice(
        ["18-24", "25-34", "35-44", "45-54", "55+"],
        size=n_users,
        p=[0.25, 0.30, 0.20, 0.15, 0.10]
    ),
    # Gênero (simulado com correlação comportamental)
    "genero": np.random.choice(["M", "F"], size=n_users, p=[0.48, 0.52]),
    # Orientação política simulada
    "orientacao_politica": np.random.choice(
        ["esquerda", "centro", "direita"],
        size=n_users,
        p=[0.35, 0.30, 0.35]
    ),
}

df = pd.DataFrame(data)

# Introduz correlações realistas
# Pessoas mais jovens passam mais tempo online
mask_jovens = df["idade_categoria"].isin(["18-24", "25-34"])
df.loc[mask_jovens, "horas_online"] *= 1.5
df.loc[mask_jovens, "pct_social"] *= 1.3

# Pessoas com mais educação passam mais tempo em sites educacionais
df.loc[df["pct_educacao"] > 0.5, "orientacao_politica"] = "esquerda"

# Pessoas mais velhas compram mais online
mask_velhos = df["idade_categoria"].isin(["45-54", "55+"])
df.loc[mask_velhos, "compras_mes"] *= 1.8

# Inferindo gênero a partir de padrões comportamentais (correlação artificial)
df.loc[df["genero"] == "F", "pct_social"] *= 1.4
df.loc[df["genero"] == "F", "compras_mes"] *= 1.3
df.loc[df["genero"] == "M", "pct_entretenimento"] *= 1.5

print("=== PERFILAMENTO ALGORÍTMICO ===")
print(f"Total de usuários: {n_users}")
print(f"Features comportamentais: {[c for c in df.columns if c not in ['usuario_id', 'idade_categoria', 'genero', 'orientacao_politica']]}")
print()

# Treina modelo para inferir idade a partir de comportamento
features = [
    "horas_online", "sites_noticias", "posts_por_dia",
    "compras_mes", "buscas_dia", "pct_entretenimento",
    "pct_educacao", "pct_social"
]

X = df[features]
y_idade = LabelEncoder().fit_transform(df["idade_categoria"])

X_train, X_test, y_train, y_test = train_test_split(
    X, y_idade, test_size=0.3, random_state=42
)

modelo_idade = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_idade.fit(X_train, y_train)
y_pred = modelo_idade.predict(X_test)

print("=== CLASSIFICAÇÃO: IDADE (a partir de dados comportamentais) ===")
print(classification_report(
    y_test, y_pred,
    target_names=["18-24", "25-34", "35-44", "45-54", "55+"]
))

# Feature importance
importancias = pd.DataFrame({
    "feature": features,
    "importancia": modelo_idade.feature_importances_
}).sort_values("importancia", ascending=False)

print("\n=== FEATURES MAIS IMPORTANTES PARA PREDIÇÃO DE IDADE ===")
print(importancias.to_string(index=False))
```

### 2. Exemplo de Viés em Classificação

```python
"""
Demonstração de como vieses em dados de treinamento
geram vieses em sistemas de classificação algorítmica.
Baseado nos conceitos de O'Neil (2016) e Buolamwini & Gebru (2018).
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score

# Simula um sistema de scoring de crédito com viés histórico
np.random.seed(42)

def simular_sistema_credito(n_amostras=2000, viés_racial=True):
    """
    Simula dados de concessão de crédito com viés histórico.
    
    A variável 'raça' não entra no modelo, mas correlaciona-se
    com features que entram (CEP, renda), gerando viés indireto.
    """
    # Gera dados demográficos
    raca = np.random.choice(
        ["branco", "negro", "pardo", "outro"],
        size=n_amostras,
        p=[0.45, 0.20, 0.25, 0.10]
    )
    
    # Renda correlacionada com raça (refletindo desigualdade real)
    renda_base = {
        "branco": 5000,
        "negro": 2800,
        "pardo": 3000,
        "outro": 4000,
    }
    renda = np.array([
        renda_base[r] + np.random.normal(0, 1000) for r in raca
    ])
    renda = np.maximum(renda, 0)
    
    # CEP com viés de segregação espacial
    cep_score = np.where(
        raca == "branco",
        np.random.normal(0.7, 0.15, n_amostras),
        np.random.normal(0.4, 0.2, n_amostras)
    )
    cep_score = np.clip(cep_score, 0, 1)
    
    # Histórico de crédito (correlacionado com renda)
    historico = np.random.beta(
        a=2 + renda / 5000,
        b=5 - renda / 10000,
        size=n_amostras
    )
    historico = np.clip(historico, 0, 1)
    
    # Rótulo real: capacidade de pagamento (desconhecida do modelo)
    # Determinada por renda e histórico, NÃO por raça
    capacidade_real = 0.3 * (renda / 10000) + 0.7 * historico
    capacidade_real = np.clip(capacidade_real, 0, 1)
    rotulo_real = (capacidade_real > 0.5).astype(int)
    
    # Rotulo histórico COM VIÉS: pessoas negras têm menos chance
    # de receber crédito mesmo com mesma capacidade
    rotulo_historico = rotulo_real.copy()
    mask_negro = raca == "negro"
    rotulo_historico[mask_negro] = (
        rotulo_historico[mask_negro] *
        np.random.binomial(1, 0.7, size=mask_negro.sum())
    )
    
    return pd.DataFrame({
        "renda": renda,
        "cep_score": cep_score,
        "historico": historico,
        "raca": raca,
        "rotulo_real": rotulo_real,
        "rotulo_historico": rotulo_historico
    })

df = simular_sistema_credito()

# Modelo TREINADO com dados históricos enviesados
features = ["renda", "cep_score", "historico"]

modelo_enviesado = LogisticRegression()
modelo_enviesado.fit(df[features], df["rotulo_historico"])

modelo_justo = LogisticRegression()
modelo_justo.fit(df[features], df["rotulo_real"])

print("=== COMPARAÇÃO DE MODELOS DE CRÉDITO ===")
print()

# Análise de viés
for nome, modelo, rotulo in [
    ("Modelo com Viés Histórico", modelo_enviesado, "rotulo_historico"),
    ("Modelo Ideal (sem viés)", modelo_justo, "rotulo_real")
]:
    pred = modelo.predict(df[features])
    print(f"\n--- {nome} ---")
    
    for grupo in ["branco", "negro", "pardo", "outro"]:
        mask = df["raca"] == grupo
        precision = precision_score(df[rotulo][mask], pred[mask], zero_division=0)
        recall = recall_score(df[rotulo][mask], pred[mask], zero_division=0)
        taxa_aprovacao = pred[mask].mean()
        
        print(f"  {grupo.capitalize()}:")
        print(f"    Taxa de aprovação: {taxa_aprovacao:.1%}")
        print(f"    Precisão: {precision:.1%}")
        print(f"    Recall: {recall:.1%}")
    
    cm_geral = confusion_matrix(df[rotulo], pred)
    print(f"  Matriz de confusão:")
    print(f"    VP: {cm_geral[1,1]}  FP: {cm_geral[0,1]}")
    print(f"    FN: {cm_geral[1,0]}  VN: {cm_geral[0,0]}")
```

### 3. Simulação de Vigilância em Tempo Real (Anomaly Detection)

```python
"""
Simulação simplificada de detecção de anomalias
para vigilância algorítmica em tempo real.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Simula dados de navegação de um usuário ao longo de 30 dias
np.random.seed(42)
n_pontos = 1000

# Comportamento normal (ruído gaussiano)
horario_normal = np.random.normal(loc=14, scale=4, size=n_pontos)  # 14h ± 4h
duracao_normal = np.random.exponential(scale=30, size=n_pontos)    # ~30 min

# Anomalias: comportamento fora do padrão
n_anomalias = 30
indices_anomalia = np.random.choice(n_pontos, n_anomalias, replace=False)

horario = horario_normal.copy()
horario[indices_anomalia] = np.random.uniform(0, 24, n_anomalias)

duracao = duracao_normal.copy()
duracao[indices_anomalia] = np.random.exponential(scale=120, n_anomalias)

# Feature engineering
dados_vigilancia = pd.DataFrame({
    "horario": horario,
    "duracao_minutos": duracao,
    "horario_ao_quadrado": horario ** 2,
    "horario_seno": np.sin(2 * np.pi * horario / 24),
    "horario_cosseno": np.cos(2 * np.pi * horario / 24),
})

# Detecção de anomalias
modelo_anomalia = IsolationForest(
    contamination=0.05,
    random_state=42
)
pred_anomalia = modelo_anomalia.fit_predict(dados_vigilancia)

# -1 = anomalia, 1 = normal
anomalias_detectadas = pred_anomalia == -1

print("=== SISTEMA DE DETECÇÃO DE ANOMALIAS COMPORTAMENTAIS ===")
print(f"Total de pontos monitorados: {n_pontos}")
print(f"Anomalias detectadas: {anomalias_detectadas.sum()}")
print(f"Taxa de alerta: {anomalias_detectadas.mean():.1%}")
print()

# Identifica as sessões mais suspeitas
dados_vigilancia["score_anomalia"] = modelo_anomalia.score_samples(dados_vigilancia)
top_suspeitas = dados_vigilancia.nsmallest(5, "score_anomalia")

print("Sessões mais suspeitas (score mais negativo = mais anômalo):")
for i, (_, sessao) in enumerate(top_suspeitas.iterrows()):
    print(f"  {i+1}. Horário: {sessao['horario']:.1f}h, "
          f"Duração: {sessao['duracao_minutos']:.0f}min, "
          f"Score: {sessao['score_anomalia']:.3f}")
```

### 4. Algoritmo de Proporcionalidade de Reconhecimento Facial (Viés)

```python
"""
Simulação da disparidade de acurácia em reconhecimento facial.
Baseado no estudo Gender Shades (Buolamwini & Gebru, 2018).
"""

import numpy as np
import pandas as pd

np.random.seed(42)

def simular_rf(grupo, n_amostras=5000, acuracia_base=0.95, penalidade=None):
    """
    Simula resultados de um sistema de reconhecimento facial
    com acurácia variável por grupo demográfico.
    """
    if penalidade is None:
        # Acurácia base (homens brancos: ~99%)
        acuracia = acuracia_base + 0.04
    else:
        # Penalidade aplicada (mulheres negras: ~65-79%)
        acuracia = acuracia_base - penalidade
    
    acuracia = np.clip(acuracia, 0, 1)
    
    # Gera predições baseadas na acurácia
    corretas = np.random.binomial(1, acuracia, n_amostras)
    
    # Falsos positivos e negativos
    falsos_positivos = np.random.binomial(
        1, (1 - acuracia) * 0.6, n_amostras  # FP ligeiramente mais comuns
    )
    
    return {
        "grupo": grupo,
        "n": n_amostras,
        "acuracia": acuracia,
        "corretas": corretas.sum(),
        "taxa_corretas": corretas.mean(),
        "falsos_positivos": falsos_positivos.mean(),
    }

# Dados do Gender Shades (aproximados)
grupos = [
    ("Homens Brancos", 0.0),
    ("Homens Negros", 0.08),
    ("Mulheres Brancas", 0.05),
    ("Mulheres Negras", 0.28),
]

resultados = []
for nome, penalidade in grupos:
    res = simular_rf(nome, n_amostras=5000, acuracia_base=0.97, penalidade=penalidade)
    resultados.append(res)

df_rf = pd.DataFrame(resultados)

print("=== DISPARIDADE EM RECONHECIMENTO FACIAL ===")
print("(Baseado em Buolamwini & Gebru, 2018 — Gender Shades)")
print()

for _, res in df_rf.iterrows():
    print(f"{res['grupo']}:")
    print(f"  Acurácia: {res['acuracia']:.1%}")
    print(f"  Taxa de acerto: {res['taxa_corretas']:.1%}")
    print(f"  Falsos positivos: {res['falsos_positivos']:.1%}")
    print()

print(f"Diferença máxima (homens brancos vs. mulheres negras):")
diferenca = (
    df_rf[df_rf['grupo'] == 'Homens Brancos']['acuracia'].values[0] -
    df_rf[df_rf['grupo'] == 'Mulheres Negras']['acuracia'].values[0]
)
print(f"  {diferenca:.1%} de disparidade")
print()
print("IMPLICAÇÕES: Em um sistema de vigilância com 1 milhão de")
print("indivíduos monitorados por RF, milhares de falsos positivos")
print("afetariam desproporcionalmente mulheres negras, resultando")
print("em abordagens policiais injustas e prisões equivocadas.")
```

## Exercícios Práticos

### Exercício 1: Análise Crítica de Algoritmo

Escolha um sistema algorítmico com o qual você interage diariamente (Instagram, TikTok, YouTube, Google Search, Uber) e analise:

1. Que dados sobre você esse sistema coleta?
2. Como esses dados são usados para perfilamento?
3. Que predições o sistema faz sobre seu comportamento?
4. Como essas predições afetam suas escolhas?
5. Existe alguma forma de resistência ou mitigação?

### Exercício 2: Cálculo de Excedente Comportamental

Se o Google processa ~8.5 bilhões de buscas por dia e coleta ~15 dados por busca (localização, dispositivo, tempo de clique, etc.), calcule:

1. Volume diário de dados comportamentais coletados
2. Volume que NÃO é usado para melhoria do buscador (assumindo 95% como excedente)
3. Valor estimado desse excedente (a $0.0001 por ponto de dado)

### Exercício 3: Auditando Viés

Usando o código de simulação de crédito fornecido:

1. Modifique os parâmetros de viés para simular diferentes cenários
2. Implemente uma métrica de "equidade" (disparate impact ratio)
3. Proponha uma correção (ex.: reweighting, fairness constraint)
4. Compare resultado do modelo corrigido vs. original

### Exercício 4: Mapa Conceitual

Desenhe um mapa conceitual relacionando os seguintes conceitos:

```
Capitalismo de Vigilância ──> Excedente Comportamental
       │                              │
       v                              v
Mercados de Comportamentos ──> Modificação Comportamental
       │                              │
       v                              v
Perfilamento Algorítmico ──> Viés e Discriminação
       │                              │
       v                              v
Resistência (Regulação) ──> Resistência (Tecnológica)
```

## Glossário

| Termo | Definição |
|-------|-----------|
| **Excedente comportamental** | Dados comportamentais que excedem o necessário para melhoria do serviço, extraídos como matéria-prima para predição |
| **Capitalismo de vigilância** | Sistema econômico que trata a experiência humana como matéria-prima gratuita para práticas comerciais de predição |
| **Meios de modificação comportamental** | Infraestrutura tecnológica e econômica para moldar comportamento humano em escala |
| **Perfilamento (profiling)** | Inferência automatizada de atributos pessoais a partir de dados |
| **Scoring** | Atribuição de pontuação numérica para classificação de indivíduos |
| **Obfuscação** | Técnica de resistência que consiste em gerar dados falsos ou ruído para confundir sistemas de vigilância |
| **Panóptico digital** | Sistema de vigilância onde os sujeitos sabem que podem ser observados, mas não sabem quando, internalizando o controle |
| **Viés algorítmico** | Erro sistemático em sistemas algorítmicos que produz resultados discriminatórios |
| **Falso positivo** | Classificação incorreta de um indivíduo como pertencente a uma categoria (ex.: "criminoso") quando não pertence |
| **Profecias autorrealizáveis** | Ciclo onde a predição de um evento leva a ações que tornam o evento mais provável |
| **Biopoder** | Conceito de Foucault sobre a gestão estatística e administrativa de populações |
| **Sociedade de controle** | Termo de Deleuze (1992) para descrever a substituição das sociedades disciplinares por controle contínuo e modulável |
| **Data broker** | Empresa que coleta, agrega e vende dados pessoais de consumidores |

## Mapa Conceitual

```
                         VIGILÂNCIA ALGORÍTMICA
                                │
              ┌─────────────────┼─────────────────┐
              │                 │                 │
         Coleta de          Análise           Modificação
           Dados           Algorítmica       Comportamental
              │                 │                 │
    ┌─────────┴────────┐    Predição      ┌──────┴──────┐
    │                  │       │          │             │
  Tracking        Biometria   │      Nudging       Controle
  (cookies,       (facial,    │      Social       Social
  fingerprinting)  voz,       │    (recomenda-     (crédito
    │              marcha)    │     ções, ads)     social,
    │                  │      │                   policing)
    v                  v      v                       │
    └──────────────────┴──────┘                       │
                │                                     │
          Perfilamento                          Decisões
          (profiling)                           Automatizadas
                │                                     │
                └────────────────┬────────────────────┘
                                 │
                            VIÉS E
                         DISCRIMINAÇÃO
                              │
                              v
                    ┌─────────────────┐
                    │   RESISTÊNCIA   │
                    │ ─────────────── │
                    │ Criptografia    │
                    │ Obfuscação      │
                    │ Regulamentação  │
                    │ Ativismo        │
                    │ Boicote         │
                    └─────────────────┘
```

## Linha do Tempo

| Ano | Evento |
|-----|--------|
| 1890 | Hollerith: tabulação mecânica do censo americano |
| 1956 | Nascimento da inteligência artificial (Dartmouth workshop) |
| 1972 | COINTELPRO: vigilância política nos EUA |
| 1984 | Orwell: "Big Brother is watching you" — referência cultural |
| 1996 | DoubleClick: primeiro grande sistema de publicidade tracking |
| 1998 | Google: PageRank e rastreamento de cliques |
| 2004 | Facebook: criação da maior plataforma de perfilamento social |
| 2007 | Target: análise preditiva de compras para identificar gestantes |
| 2011 | PredPol: primeiro sistema de policiamento preditivo |
| 2012 | Facebook-Cambridge Analytica: extração de dados de 87M usuários |
| 2013 | Revelações de Snowden: PRISM, XKEYSCORE, vigilância global |
| 2014 | China anuncia Sistema de Crédito Social |
| 2016 | Machine Bias (ProPublica): viés do sistema COMPAS |
| 2018 | GDPR na UE; Gender Shades (Buolamwini & Gebru) |
| 2018 | LGPD sancionada no Brasil |
| 2019 | Zuboff: *The Age of Surveillance Capitalism* |
| 2020 | COVID-19: vigilância pandêmica, contato tracking |
| 2021 | Clearview AI: multada por coleta ilegal de imagens |
| 2022 | Robert Williams: primeira prisão por falso positivo de RF nos EUA |
| 2024 | EU AI Act aprovado — marco regulatório de IA |
| 2026 | Debate global sobre regulamentação de vigilância algorítmica |

## Referências Completas

### Livros

- Benjamin, R. (2019). *Race After Technology: Abolitionist Tools for the New Jim Code*. Polity Press.
- Bridle, J. (2018). *New Dark Age: Technology and the End of the Future*. Verso.
- Browne, S. (2015). *Dark Matters: On the Surveillance of Blackness*. Duke University Press.
- Brunton, F., & Nissenbaum, H. (2015). *Obfuscation: A User's Guide for Privacy and Protest*. MIT Press.
- Deleuze, G. (1992). "Postscript on the Societies of Control." *October*, 59, 3–7.
- Eubanks, V. (2018). *Automating Inequality: How High-Tech Tools Profile, Police, and Punish the Poor*. St. Martin's Press.
- Foucault, M. (1975). *Discipline and Punish: The Birth of the Prison*. Vintage Books.
- Foucault, M. (1977–78). *Security, Territory, Population: Lectures at the Collège de France*. Palgrave Macmillan.
- Greenwald, G. (2014). *No Place to Hide: Edward Snowden, the NSA, and the U.S. Surveillance State*. Metropolitan Books.
- Lyon, D. (2001). *Surveillance Society: Monitoring Everyday Life*. Open University Press.
- Lyon, D. (2018). *The Culture of Surveillance: Watching as a Way of Life*. Polity Press.
- Mayer-Schönberger, V., & Cukier, K. (2013). *Big Data: A Revolution That Will Transform How We Live, Work, and Think*. Houghton Mifflin Harcourt.
- Muller, J. Z. (2018). *The Tyranny of Metrics*. Princeton University Press.
- Noble, S. U. (2018). *Algorithms of Oppression: How Search Engines Reinforce Racism*. NYU Press.
- O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.
- Pasquale, F. (2015). *The Black Box Society: The Secret Algorithms That Control Money and Information*. Harvard University Press.
- Rosenblat, A. (2018). *Uberland: How Algorithms Are Rewriting the Rules of Work*. University of California Press.
- Taylor, F. W. (1911). *The Principles of Scientific Management*. Harper & Brothers.
- Zuboff, S. (2019). *The Age of Surveillance Capitalism: The Fight for a Human Future at the New Frontier of Power*. PublicAffairs.

### Artigos Acadêmicos

- Angwin, J., Larson, J., Mattu, S., & Kirchner, L. (2016). "Machine Bias." *ProPublica*.
- Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., & Pollak, S. D. (2019). "Emotional Expressions Reconsidered: Challenges to Inferring Emotion From Human Facial Movements." *Psychological Science in the Public Interest*, 20(1), 1–68.
- Bowker, G. C., & Star, S. L. (1999). *Sorting Things Out: Classification and Its Consequences*. MIT Press.
- Buolamwini, J., & Gebru, T. (2018). "Gender Shades: Intersectional Accuracy Disparities in Commercial Gender Classification." *Proceedings of the 1st Conference on Fairness, Accountability and Transparency* (FAT*), 77–91.
- Duhigg, C. (2012). "How Companies Learn Your Secrets." *The New York Times Magazine*.
- Kosinski, M., Stillwell, D., & Graepel, T. (2013). "Private Traits and Attributes Are Predictable from Digital Records of Human Behavior." *Proceedings of the National Academy of Sciences*, 110(15), 5802–5805.
- Zenz, A. (2019). "Breakdown of the 'Xinjiang Work' — Policy and Practice in the Concentration Camps." *Journal of Political Risk*, 7(8).

### Relatórios e Documentos Legais

- Autoridade Nacional de Proteção de Dados (ANPD). (2020). *Guia Orientativo para Definições dos Agentes de Tratamento de Dados Pessoais*.
- Big Brother Watch. (2020). *Face Off: The Lawless Growth of Facial Recognition in UK Policing*.
- Comissão Europeia. (2024). *Regulation (EU) 2024/1689 — Artificial Intelligence Act*.
- Lei Geral de Proteção de Dados Pessoais — Lei nº 13.709, de 14 de agosto de 2018 (Brasil).
- Projeto de Lei nº 2338/2023 — Dispõe sobre a regulamentação de inteligência artificial no Brasil.
- RAND Corporation. (2019). *Evaluation of the Chicago Police Department's Predictive Risk Models*.

### Conexões Internas (Obsidian Wiki-Links)

- [[Conhecimento-Geral/Tecnologia-e-Sociedade/Panoptico-Digital|Panóptico Digital]]
- [[Conhecimento-Geral/Etica/Transparencia-Algoritmica|Transparência Algorítmica]]
- [[Conhecimento-Geral/Filosofia/Problema-do-Controle|Problema do Controle]]
- [[Conhecimento-Geral/Psicologia/Vieses-em-LLMs|Vieses em LLMs]]
- [[Conhecimento-Geral/Etica/Responsabilidade-de-IAs|Responsabilidade de IAs]]
- [[Conhecimento-Geral/Filosofia/Privacidade-e-Dados|Privacidade e Dados]]
- [[Conhecimento-Geral/Sociedade/Desigualdade-Digital|Desigualdade Digital]]
- [[Conhecimento-Geral/Tecnologia-e-Sociedade/Vigilancia-Algoritmica|Vigilância Algorítmica]]
- [[Conhecimento-Geral/Direito/LGPD-e-Governanca-de-Dados|LGPD e Governança de Dados]]

---

> *"We are not the customers of Google, Facebook, Amazon, or Microsoft. We are the raw material — the source of behavioral data that is the lifeblood of surveillance capitalism."* — Shoshana Zuboff (2019)

> *"The problem with big data is not that it's big. It's that the algorithms that process it embed the values of their creators."* — Cathy O'Neil (2016)

> *"Algorithms are opinions embedded in code."* — Cathy O'Neil (2016)

> *"Vigilância algorítmica não é sobre tecnologia. É sobre poder — quem sabe, quem decide, quem controla."* — Adaptado de Lyon (2018)
