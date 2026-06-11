---
title: "NLP — Fundamentos de Processamento de Linguagem Natural"
date: 2026-05-16
area: "Computação e Programação"
tags: [computacao, nlp, pln, transformers, bert, gpt, word-embeddings, deep-learning]
aliases: ["Natural Language Processing", "PLN", "Processamento de Linguagem Natural"]
---

# NLP — Fundamentos de Processamento de Linguagem Natural

> *"You shall know a word by the company it keeps."* — J. R. Firth (1957)

---

## 1. Pré-processamento de Texto

### 1.1 Tokenização

Tokenização é o processo de dividir um texto em unidades menores (tokens): palavras, subpalavras ou caracteres.

```python
import re

def tokenize_simples(texto):
    """Tokenização ingênua por espaços e pontuação."""
    return re.findall(r"\b\w+\b", texto.lower())

# Tokenização mais robusta
def tokenize_avancada(texto):
    tokens = re.findall(r"[A-Za-zÀ-ÿ]+|\d+|[^\w\s]", texto)
    return tokens

texto = "Olá, mundo! NLP é fascinante — 2026 será incrível."
print(tokenize_avancada(texto))
# ['Olá', 'mundo', 'NLP', 'é', 'fascinante', '—', '2026', 'será', 'incrível']
```

**Tokenizadores modernos** (subword tokenization):

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("neuralmind/bert-base-portuguese-cased")
tokens = tokenizer.tokenize("Processamento de linguagem natural!")
print(tokens)
# Exemplo de saída (subword): ['Processamento', 'de', 'linguagem', 'natural', '!']

ids = tokenizer.encode("Processamento de linguagem natural!")
print(ids)  # IDs dos tokens no vocabulário do BERT
```

**Algoritmos de subword tokenization**:

| Algoritmo | Usado por | Descrição |
|-----------|-----------|-----------|
| **BPE** (Byte-Pair Encoding) | GPT, BART, LLaMA | Funde pares de tokens mais frequentes iterativamente |
| **WordPiece** | BERT, DistilBERT | Similar ao BPE, mas maximiza likelihood |
| **SentencePiece** | T5, ALBERT, Llama 2 | Unigram LM tokenization; opera sem pré-tokenização |
| **Unigram** | XLNet, ALBERT | Modelo probabilístico que encontra segmentação ótima |

```python
# Demonstração: BPE no estilo tiktoken
def bpe_simples(corpus, n_merges=10):
    from collections import Counter
    # Inicialização: cada caractere é um token
    vocab = {c for palavra in corpus for c in palavra}
    vocab.add('</w>')
    palavras = [list(p) + ['</w>'] for p in corpus]

    for _ in range(n_merges):
        # Contar pares
        pares = Counter()
        for p in palavras:
            for i in range(len(p) - 1):
                pares[(p[i], p[i+1])] += 1
        if not pares:
            break
        # Merge do par mais frequente
        melhor_par = pares.most_common(1)[0][0]
        novo_token = ''.join(melhor_par)
        vocab.add(novo_token)

        # Aplicar merge
        novas_palavras = []
        for p in palavras:
            np = []
            i = 0
            while i < len(p):
                if i < len(p) - 1 and (p[i], p[i+1]) == melhor_par:
                    np.append(novo_token)
                    i += 2
                else:
                    np.append(p[i])
                    i += 1
            novas_palavras.append(np)
        palavras = novas_palavras
    return vocab

corpus = ["ba", "ab", "aba", "bab", "baab"]
vocab = bpe_simples(corpus, n_merges=5)
print(f"Vocabulário BPE: {vocab}")
```

### 1.2 Stemming e Lemmatization

| Técnica | Descrição | Exemplo |
|---------|-----------|---------|
| **Stemming** | Corta sufixos heuristicamente | "correndo" → "corr", "correu" → "corr" |
| **Lemmatization** | Reduz à forma canônica (lemma) usando dicionário | "correndo" → "correr", "melhor" → "bom" |

```python
from nltk.stem import PorterStemmer, SnowballStemmer
from nltk.stem import WordNetLemmatizer

# Stemming (inglês)
stemmer_en = PorterStemmer()
palavras_en = ["running", "better", "studies", "happiness", "lying"]
for p in palavras_en:
    print(f"{p} → {stemmer_en.stem(p)}")

# Stemming para português (Snowball)
stemmer_pt = SnowballStemmer("portuguese")
palavras_pt = ["correndo", "estudávamos", "felizmente", "gato", "gatinho"]
for p in palavras_pt:
    print(f"{p} → {stemmer_pt.stem(p)}")

# Lemmatization com spaCy
import spacy
nlp = spacy.load("pt_core_news_sm")
doc = nlp("Os gatos estavam correndo rapidamente pelos telhados")
for token in doc:
    print(f"{token.text:15} → lemma: {token.lemma_:15} POS: {token.pos_}")
```

### 1.3 Stop Words, Normalização e Regex

```python
from nltk.corpus import stopwords
import string

stop_words = set(stopwords.words("portuguese"))
print(f"Stop words (português, primeiras 10): {list(stop_words)[:10]}")

def limpar_texto(texto, remover_stopwords=True):
    texto = texto.lower()
    texto = re.sub(r"http\S+", "", texto)  # URLs
    texto = re.sub(r"@\w+", "", texto)     # Menções
    texto = re.sub(r"[^\w\s]", "", texto)  # Pontuação
    tokens = texto.split()
    if remover_stopwords:
        tokens = [t for t in tokens if t not in stop_words]
    return tokens
```

---

## 2. Representações Clássicas de Texto

### 2.1 Bag-of-Words (BoW)

Representa cada documento como um vetor de contagem de palavras (ordem ignorada).

```python
from sklearn.feature_extraction.text import CountVectorizer

documentos = [
    "o gato está no telhado",
    "o cachorro correu atrás do gato",
    "o pássaro voou sobre o telhado",
]

vectorizer = CountVectorizer()
bow = vectorizer.fit_transform(documentos)

print("Vocabulário:", vectorizer.get_feature_names_out())
print("Matriz BoW:")
print(bow.toarray())
```

### 2.2 TF-IDF (Term Frequency — Inverse Document Frequency)

TF-IDF pondera a importância de um termo em um documento:

$$TF(t,d) = \frac{\text{frequência de } t \text{ em } d}{\text{total de termos em } d}$$

$$IDF(t) = \log \frac{N}{\text{número de documentos com } t}$$

$$TFIDF(t,d) = TF(t,d) \times IDF(t)$$

```python
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer()
matriz_tfidf = tfidf.fit_transform(documentos)

print("Vocabulário:", tfidf.get_feature_names_out())
print("Matriz TF-IDF (arredondada):")
import numpy as np
np.set_printoptions(precision=3, suppress=True)
print(matriz_tfidf.toarray())
```

### 2.3 N-grams

N-grams capturam sequências de $n$ tokens consecutivos.

```python
from collections import Counter

def gerar_ngrams(tokens, n=2):
    return [tuple(tokens[i:i+n]) for i in range(len(tokens) - n + 1)]

def modelo_ngram( corpus, n ):
    """Modelo de linguagem simples baseado em n-grams."""
    ngrams = Counter()
    contextos = Counter()
    for doc in corpus:
        tokens = doc.lower().split()
        ngrams_list = gerar_ngrams(['<s>'] * (n-1) + tokens + ['</s>'], n)
        for ng in ngrams_list:
            ngrams[ng] += 1
            contextos[ng[:-1]] += 1
    return ngrams, contextos

def probabilidade_ngram(ngrams, contextos, gram):
    context = gram[:-1]
    if contextos[context] == 0:
        return 0.0
    return ngrams[gram] / contextos[context]

corpus = [
    "o gato está no telhado",
    "o cachorro está no jardim",
    "o gato correu no telhado",
]
ngrams, ctx = modelo_ngram(corpus, n=2)
print("Prob('gato' | 'o'):", probabilidade_ngram(ngrams, ctx, ('o', 'gato')))
```

### 2.4 PMI (Pointwise Mutual Information)

PMI mede a associação entre duas palavras:

$$PMI(w_1, w_2) = \log \frac{P(w_1, w_2)}{P(w_1) P(w_2)}$$

```python
def pmi(palavras, w1, w2):
    from collections import Counter
    import math
    total = sum(palavras.values())
    p_w1 = sum(v for k, v in palavras.items() if w1 in k) / total
    p_w2 = sum(v for k, v in palavras.items() if w2 in k) / total
    p_w1w2 = palavras.get((w1, w2), 0) / total
    if p_w1w2 == 0:
        return float('-inf')
    return math.log2(p_w1w2 / (p_w1 * p_w2))

# Bigramas do corpus
bigramas = Counter()
for doc in corpus:
    tokens = doc.lower().split()
    for bg in gerar_ngrams(tokens, 2):
        bigramas[bg] += 1

print(f"PMI(gato, telhado): {pmi(bigramas, 'gato', 'telhado'):.2f}")
print(f"PMI(gato, jardim): {pmi(bigramas, 'gato', 'jardim'):.2f}")
```

---

## 3. Word Embeddings

### 3.1 Word2Vec (Mikolov et al., 2013)

Word2Vec produz embeddings densos de palavras usando redes neurais rasas. Duas arquiteturas:

**Skip-gram**: prediz contexto a partir da palavra alvo

**CBOW** (Continuous Bag-of-Words): prediz palavra alvo a partir do contexto

```python
from gensim.models import Word2Vec

sentencas = [
    ["o", "gato", "está", "no", "telhado"],
    ["o", "cachorro", "correu", "no", "jardim"],
    ["o", "pássaro", "voou", "sobre", "o", "telhado"],
    ["o", "gato", "correu", "atrás", "do", "cachorro"],
]

# Treino com CBOW (sg=0) ou Skip-gram (sg=1)
modelo = Word2Vec(sentencas, vector_size=50, window=3, sg=1, min_count=1)
vetor_gato = modelo.wv["gato"]
print(f"Vetor 'gato' (primeiras 10 dims): {vetor_gato[:10]}")

# Analogias clássicas: rei - homem + mulher ≈ rainha
# (precisa de corpus grande para analogias funcionarem)
similares = modelo.wv.most_similar("gato", topn=3)
print(f"Palavras similares a 'gato': {similares}")
```

**Limitações do Word2Vec**:
- Embedding estático (mesmo vetor independente do contexto)
- Não captura polissemia
- Vocabulário fixo (OOV: out-of-vocabulary)
- Treino consome muito corpus

### 3.2 GloVe (Pennington et al., 2014)

GloVe (Global Vectors for Word Representation) combina matriz de co-ocorrência com fatoração de matriz:

$$J = \sum_{i,j=1}^V f(X_{ij}) (w_i^T \tilde{w}_j + b_i + \tilde{b}_j - \log X_{ij})^2$$

Onde $X_{ij}$ é a contagem de co-ocorrência das palavras $i$ e $j$, e $f$ é uma função de ponderação.

GloVe é treinado em estatísticas globais da matriz de co-ocorrência, diferente do Word2Vec que usa janelas locais.

```python
# Carregar GloVe pré-treinado (requer download)
import gensim.downloader as api
try:
    glove = api.load("glove-wiki-gigaword-50")  # 50 dimensões
    print(f"Dimensão do embedding: {glove.vector_size}")
    print(f"Tamanho do vocabulário: {len(glove.key_to_index)}")

    # Melhores análogias
    analogia = glove.most_similar(positive=["king", "woman"], negative=["man"])
    print(f"rei - homem + mulher: {analogia}")
except Exception as e:
    print(f"Erro ao carregar GloVe: {e}")
```

### 3.3 FastText (Bojanowski et al., 2017)

FastText estende Word2Vec representando cada palavra como um **saco de n-grams de caracteres**. Vantagem: gera embeddings para palavras OOV.

```python
from gensim.models import FastText

# Treino rápido de FastText
modelo_ft = FastText(
    sentences=sentencas,
    vector_size=50,
    window=3,
    min_count=1,
    min_n=2,     # n-gram mínimo
    max_n=5,     # n-gram máximo
)

# Embedding para palavra vista
print(f"Vetor 'gato' (primeiras 5 dims): {modelo_ft.wv['gato'][:5]}")

# Embedding para palavra NÃO vista (OOV) — possível graças a subwords
vetor_oov = modelo_ft.wv["gatíneo"]  # palavra inventada
print(f"Vetor OOV 'gatíneo' (primeiras 5 dims): {vetor_oov[:5]}")
```

**Comparação de Embeddings**:

| Modelo | Contexto | OOV | Polissemia | Treino |
|--------|----------|-----|------------|--------|
| Word2Vec | Estático (único vetor) | ❌ | ❌ | Rápido (grande corpus) |
| GloVe | Estático + co-ocorrência global | ❌ | ❌ | Médio |
| FastText | Estático + subwords | ✅ | ❌ | Médio |
| BERT/GPT | **Contextual** (multi-vetor) | ✅ (subword) | ✅ | Lento (muito data) |

---

## 4. Modelos Sequenciais (RNNs, LSTMs, GRUs)

### 4.1 RNN (Recurrent Neural Network)

Uma RNN processa sequências mantendo um estado oculto $h_t$:

$$h_t = \tanh(W_{hh} h_{t-1} + W_{xh} x_t + b_h)$$

$$y_t = W_{hy} h_t + b_y$$

```python
import torch
import torch.nn as nn

class RNNSimples(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.hidden_size = hidden_size
        self.i2h = nn.Linear(input_size + hidden_size, hidden_size)
        self.i2o = nn.Linear(input_size + hidden_size, output_size)
        self.softmax = nn.LogSoftmax(dim=1)

    def forward(self, x, hidden):
        combined = torch.cat((x, hidden), dim=1)
        hidden = torch.tanh(self.i2h(combined))
        output = self.i2o(combined)
        output = self.softmax(output)
        return output, hidden

    def init_hidden(self, batch_size=1):
        return torch.zeros(batch_size, self.hidden_size)

# Uso conceitual
rnn = RNNSimples(input_size=10, hidden_size=128, output_size=5)
input_emb = torch.randn(1, 10)
hidden = rnn.init_hidden()
output, next_hidden = rnn(input_emb, hidden)
print(f"Output shape: {output.shape}, Hidden shape: {next_hidden.shape}")
```

### 4.2 LSTM (Long Short-Term Memory) — Hochreiter & Schmidhuber, 1997

LSTM resolve o problema do **desaparecimento do gradiente** (vanishing gradient) das RNNs simples usando portas (gates):

- **Forget gate**: $f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f)$ — o que esquecer
- **Input gate**: $i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i)$ — o que atualizar
- **Candidate**: $\tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C)$ — novo valor candidato
- **Cell state**: $C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t$
- **Output gate**: $o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o)$ — o que emitir
- **Hidden state**: $h_t = o_t \odot \tanh(C_t)$

```python
class LSTMCustom(nn.Module):
    def __init__(self, input_size, hidden_size):
        super().__init__()
        self.hidden_size = hidden_size
        # Portas combinadas
        self.forget = nn.Linear(input_size + hidden_size, hidden_size)
        self.input_gate = nn.Linear(input_size + hidden_size, hidden_size)
        self.candidate = nn.Linear(input_size + hidden_size, hidden_size)
        self.output_gate = nn.Linear(input_size + hidden_size, hidden_size)

    def forward(self, x, h, c):
        combined = torch.cat((x, h), dim=1)
        f = torch.sigmoid(self.forget(combined))
        i = torch.sigmoid(self.input_gate(combined))
        c_tilde = torch.tanh(self.candidate(combined))
        o = torch.sigmoid(self.output_gate(combined))
        c_new = f * c + i * c_tilde
        h_new = o * torch.tanh(c_new)
        return h_new, c_new

# usando PyTorch nativo
lstm = nn.LSTM(input_size=10, hidden_size=128, num_layers=2, batch_first=True)
x = torch.randn(32, 20, 10)  # (batch, seq_len, input_size)
output, (h_n, c_n) = lstm(x)
print(f"LSTM output: {output.shape}, h_n: {h_n.shape}, c_n: {c_n.shape}")
```

### 4.3 GRU (Gated Recurrent Unit) — Cho et al., 2014

GRU simplifica LSTM com apenas duas portas (reset, update):

- **Reset gate**: $r_t = \sigma(W_r \cdot [h_{t-1}, x_t])$
- **Update gate**: $z_t = \sigma(W_z \cdot [h_{t-1}, x_t])$
- **Candidate**: $\tilde{h}_t = \tanh(W \cdot [r_t \odot h_{t-1}, x_t])$
- **Hidden**: $h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t$

```python
gru = nn.GRU(input_size=10, hidden_size=128, num_layers=2, batch_first=True)
output, h_n = gru(x)
print(f"GRU output: {output.shape}")
```

**Comparação RNN vs LSTM vs GRU**:

| Modelo | Portas | Params | Vanishing Grad | Performance típica |
|--------|--------|--------|----------------|---------------------|
| RNN simples | 0 | Menos | ❌ Severo | Baixa (seqs longas) |
| LSTM | 3 (forget, input, output) | Mais | ✅ Resolve | Alta |
| GRU | 2 (reset, update) | Médio | ✅ Resolve | Similar LSTM |

### 4.4 RNNs Bidirecionais (BiRNN)

Processam a sequência da esquerda para a direita E da direita para a esquerda, capturando contexto futuro e passado.

```python
bilstm = nn.LSTM(
    input_size=10, hidden_size=128,
    num_layers=2, bidirectional=True, batch_first=True
)
output, (h_n, c_n) = bilstm(x)
print(f"BiLSTM output: {output.shape}")  # (batch, seq_len, 256 = 2 * 128)
```

---

## 5. Mecanismo de Attention e Transformers

### 5.1 Attention (Bahdanau et al., 2015)

Antes do Transformer, attention foi introduzida para alinhamento em tradução automática:

$$e_{ij} = a(s_{i-1}, h_j) \quad\quad \alpha_{ij} = \frac{\exp(e_{ij})}{\sum_k \exp(e_{ik})} \quad\quad c_i = \sum_j \alpha_{ij} h_j$$

Onde $a$ é um modelo de alinhamento (feed-forward), $\alpha_{ij}$ são pesos de atenção, e $c_i$ é o contexto.

### 5.2 Self-Attention (Vaswani et al., 2017)

O artigo *"Attention Is All You Need"* (Vaswani et al., NeurIPS 2017) propôs o **Transformer**, eliminando completamente recorrência.

**Scaled Dot-Product Attention**:

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right) V$$

Onde:
- $Q$ (Query): o que estou procurando
- $K$ (Key): o que eu ofereço
- $V$ (Value): o que eu entrego
- $d_k$: dimensão das keys (escalonamento evita gradientes pequenos)

```python
import torch
import torch.nn.functional as F

def scaled_dot_product_attention(Q, K, V, mask=None):
    d_k = Q.size(-1)
    scores = torch.matmul(Q, K.transpose(-2, -1)) / (d_k ** 0.5)
    if mask is not None:
        scores = scores.masked_fill(mask == 0, float('-inf'))
    attention_weights = F.softmax(scores, dim=-1)
    output = torch.matmul(attention_weights, V)
    return output, attention_weights

# Exemplo: 1 cabeça de atenção para 4 tokens
Q = K = V = torch.randn(1, 4, 64)  # (batch, seq_len, d_model)
output, weights = scaled_dot_product_attention(Q, K, V)
print(f"Attention output: {output.shape}")
print(f"Attention weights: {weights.shape}")  # (1, 4, 4) — pesos entre tokens
# weights[0, i, j] = quanto o token i "presta atenção" ao token j
```

### 5.3 Multi-Head Attention

Múltiplas cabeças de atenção em paralelo permitem capturar diferentes tipos de relações:

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, ..., \text{head}_h) W^O$$

$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, n_heads):
        super().__init__()
        assert d_model % n_heads == 0
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_k = d_model // n_heads

        self.W_Q = nn.Linear(d_model, d_model)
        self.W_K = nn.Linear(d_model, d_model)
        self.W_V = nn.Linear(d_model, d_model)
        self.W_O = nn.Linear(d_model, d_model)

    def forward(self, Q, K, V, mask=None):
        batch_size = Q.size(0)

        # Projeções lineares + reshape para múltiplas cabeças
        Q = self.W_Q(Q).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        K = self.W_K(K).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)
        V = self.W_V(V).view(batch_size, -1, self.n_heads, self.d_k).transpose(1, 2)

        # Scaled dot-product attention
        scores = torch.matmul(Q, K.transpose(-2, -1)) / (self.d_k ** 0.5)
        if mask is not None:
            scores = scores.masked_fill(mask == 0, float('-inf'))
        attn = F.softmax(scores, dim=-1)

        # Concatenação e projeção final
        context = torch.matmul(attn, V).transpose(1, 2).contiguous()
        context = context.view(batch_size, -1, self.d_model)
        output = self.W_O(context)
        return output

mha = MultiHeadAttention(d_model=512, n_heads=8)
x = torch.randn(2, 10, 512)  # (batch, seq_len, d_model)
out = mha(x, x, x)
print(f"Multi-Head output: {out.shape}")
```

### 5.4 Positional Encoding

Como o Transformer não tem recorrência, precisa de informação posicional:

$$PE_{(pos, 2i)} = \sin\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

$$PE_{(pos, 2i+1)} = \cos\left(\frac{pos}{10000^{2i/d_{model}}}\right)$$

```python
def positional_encoding(seq_len, d_model):
    pe = torch.zeros(seq_len, d_model)
    position = torch.arange(0, seq_len, dtype=torch.float).unsqueeze(1)
    div_term = torch.exp(
        torch.arange(0, d_model, 2).float() *
        (-torch.log(torch.tensor(10000.0)) / d_model)
    )
    pe[:, 0::2] = torch.sin(position * div_term)
    pe[:, 1::2] = torch.cos(position * div_term)
    return pe.unsqueeze(0)  # (1, seq_len, d_model)

pe = positional_encoding(100, 512)
import matplotlib.pyplot as plt
# Visualização conceitual: print das primeiras dimensões
print(f"PE shape: {pe.shape}")
print(f"PE[0, :5, 0]: {pe[0, :5, 0]}")
```

### 5.5 Bloco Transformer Completo

```python
class TransformerBlock(nn.Module):
    def __init__(self, d_model, n_heads, d_ff, dropout=0.1):
        super().__init__()
        self.attention = MultiHeadAttention(d_model, n_heads)
        self.norm1 = nn.LayerNorm(d_model)
        self.norm2 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.ReLU(),
            nn.Linear(d_ff, d_model),
        )
        self.dropout = nn.Dropout(dropout)

    def forward(self, x, mask=None):
        # Sub-layer 1: Multi-Head Attention
        attn_out = self.attention(x, x, x, mask)
        x = self.norm1(x + self.dropout(attn_out))

        # Sub-layer 2: Feed-Forward
        ffn_out = self.ffn(x)
        x = self.norm2(x + self.dropout(ffn_out))
        return x

# Transformer com 6 blocos (como no artigo original)
class TransformerEncoder(nn.Module):
    def __init__(self, d_model=512, n_heads=8, d_ff=2048, n_layers=6):
        super().__init__()
        self.layers = nn.ModuleList([
            TransformerBlock(d_model, n_heads, d_ff)
            for _ in range(n_layers)
        ])

    def forward(self, x, mask=None):
        for layer in self.layers:
            x = layer(x, mask)
        return x

transformer = TransformerEncoder(d_model=512, n_heads=8, n_layers=6)
x = torch.randn(2, 20, 512)
out = transformer(x)
print(f"Transformer output: {out.shape}")
```

---

## 6. Modelos Pré-treinados

### 6.1 BERT (Bidirectional Encoder Representations from Transformers)

Devlin et al., 2018. **Encoder-only**: usa contexto bidirecional para representar cada token.

**Características**:
- Treinado com **Masked Language Model (MLM)**: 15% dos tokens mascarados, modelo prediz
- **Next Sentence Prediction (NSP)**: prediz se duas sentenças são consecutivas
- Contexto **bidirecional** (ao contrário do GPT)
- $BERT_{BASE}$: 12 layers, 768 hidden, 110M parâmetros
- $BERT_{LARGE}$: 24 layers, 1024 hidden, 340M parâmetros

```python
from transformers import BertTokenizer, BertModel, BertForSequenceClassification
import torch

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

texto = "Natural language processing is fascinating."
inputs = tokenizer(texto, return_tensors="pt",
                   padding=True, truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)

# [CLS] token embedding (útil para classificação)
cls_embedding = outputs.last_hidden_state[:, 0, :]
print(f"[CLS] embedding shape: {cls_embedding.shape}")  # (1, 768)

# Classificação com BERT
classifier = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased", num_labels=2
)
logits = classifier(**inputs).logits
print(f"Logits: {logits}")
```

**BERT em português**:

```python
tokenizer_pt = AutoTokenizer.from_pretrained(
    "neuralmind/bert-base-portuguese-cased"
)
model_pt = BertModel.from_pretrained("neuralmind/bert-base-portuguese-cased")

texto_pt = "Processamento de linguagem natural é fascinante."
inputs_pt = tokenizer_pt(texto_pt, return_tensors="pt")
with torch.no_grad():
    outputs_pt = model_pt(**inputs_pt)

print(f"Embeddings BERT pt: {outputs_pt.last_hidden_state.shape}")
```

### 6.2 GPT (Generative Pre-trained Transformer)

Radford et al., 2018. **Decoder-only**: autoregressivo, prediz o próximo token.

**Arquitetura**:
- GPT-1: 12 layers, 117M params
- GPT-2: 48 layers, 1.5B params
- GPT-3: 96 layers, 175B params
- GPT-4: arquitetura Mixture of Experts (MoE), ~1.8T params (rumores)

**Principais características**:
- **Causal LM**: cada token só vê tokens anteriores (masked self-attention)
- Treinado em next-token prediction
- **In-context learning**: capacidade de aprender tarefas pelos exemplos no prompt

```python
from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer_gpt = GPT2Tokenizer.from_pretrained("gpt2")
model_gpt = GPT2LMHeadModel.from_pretrained("gpt2")

prompt = "The future of AI is"
inputs = tokenizer_gpt(prompt, return_tensors="pt")

with torch.no_grad():
    outputs = model_gpt.generate(
        **inputs,
        max_length=50,
        temperature=0.7,
        do_sample=True,
        top_k=50,
    )

generated = tokenizer_gpt.decode(outputs[0], skip_special_tokens=True)
print(f"Generated: {generated}")
```

### 6.3 LLaMA (Meta AI, 2023–2024)

**LLaMA** (Large Language Model Meta AI) e suas variantes:

| Modelo | Parâmetros | Contexto | Inovação |
|--------|-----------|----------|----------|
| LLaMA-1 | 7B, 13B, 33B, 65B | 2K | Treinado em mais tokens que o esperado |
| LLaMA-2 | 7B, 13B, 70B | 4K | Fine-tuning com RLHF |
| LLaMA-3 | 8B, 70B | 8K (3.1: 128K) | Tokenizador melhorado, GQA |
| LLaMA-3.1 | 8B, 70B, 405B | 128K | MoE no 405B, suporte multilíngue |

**Inovações arquiteturais do LLaMA**:
- **RMSNorm** (Root Mean Square Layer Normalization) em vez de LayerNorm
- **SwiGLU** activation function (Swish + Gated Linear Unit)
- **Rotary Position Embedding (RoPE)**: codificação posicional rotativa
- **Grouped Query Attention (GQA)**: múltiplas queries compartilham keys/values

### 6.4 Modelos Recentes e Mistral/Mixtral

**Mistral 7B** (2023): 7.3B parâmetros, sliding window attention, supera LLaMA-2 13B.

**Mixtral 8x7B** (2024): **Mixture of Experts (MoE)**, 46.7B total mas apenas 12.9B ativos por token. Cada token é processado por 2 dos 8 "experts".

```python
# Exemplo com modelo causal moderno
from transformers import AutoModelForCausalLM, AutoTokenizer

# Nota: requer download real — exemplo conceitual
model_name = "mistralai/Mistral-7B-v0.1"
# tokenizer = AutoTokenizer.from_pretrained(model_name)
# model = AutoModelForCausalLM.from_pretrained(
#     model_name, torch_dtype=torch.float16
# )
print(f"Modelo {model_name} requer download prévio (2,5 GB+).")
print("Uso: AutoModelForCausalLM.from_pretrained('...')")
```

---

## 7. Fine-tuning e Alinhamento

### 7.1 Transfer Learning para NLP

Pipeline padrão:

1. **Pré-treino** (pre-training): modelo treinado em corpus gigante (linguagem geral)
2. **Fine-tuning**: modelo adaptado para tarefa específica com dados rotulados menores
3. **Inferência**: predição em novos dados

```python
# Fine-tuning de BERT para classificação de sentimento
from transformers import (
    BertForSequenceClassification,
    Trainer,
    TrainingArguments,
)

model = BertForSequenceClassification.from_pretrained(
    "bert-base-uncased", num_labels=3  # positivo, neutro, negativo
)

training_args = TrainingArguments(
    output_dir="./resultados",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
)
```

### 7.2 PEFT (Parameter-Efficient Fine-Tuning)

**LoRA** (Low-Rank Adaptation) — Hu et al., 2021:

Em vez de atualizar todos os pesos ($W$), treina matrizes de baixo rank ($B, A$):

$$W' = W + BA$$

Onde $W \in \mathbb{R}^{d \times k}$, $B \in \mathbb{R}^{d \times r}$, $A \in \mathbb{R}^{r \times k}$, com $r \ll d, k$.

```python
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=8,              # rank de LoRA
    lora_alpha=32,    # scaling factor
    lora_dropout=0.1,
    target_modules=["q_proj", "v_proj"],  # módulos adaptados
)

# model_base = AutoModelForCausalLM.from_pretrained(...)
# model_lora = get_peft_model(model_base, lora_config)
# model_lora.train()
print("LoRA: congela pesos originais, treina apenas BA.")
```

**Vantagens do LoRA**:
- Reduz memória em ~70% para fine-tuning
- Checkpoints com poucos MB (vs GB do modelo completo)
- Troca rápida entre tarefas (swap de adaptadores)

### 7.3 RLHF (Reinforcement Learning from Human Feedback)

**Pipeline do RLHF** (InstructGPT, ChatGPT):

1. **SFT** (Supervised Fine-Tuning): ajuste em dados de demonstração humana
2. **Reward Modeling** (RM): treina modelo para avaliar qualidade das respostas
3. **PPO** (Proximal Policy Optimization): otimiza o modelo usando o reward model

$$\text{Objetivo PPO: } \mathbb{E}_{t}\left[\min(r_t(\theta) \hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t)\right]$$

**DPO** (Direct Preference Optimization) — Rafailov et al., 2023:

Alternativa mais simples que dispensa o reward model explícito:

$$\mathcal{L}_{DPO} = -\mathbb{E}_{(x,y_w,y_l)} \left[\log \sigma\left(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}\right)\right]$$

Onde $y_w$ é a resposta preferida e $y_l$ a não-preferida.

### 7.4 Prompt Engineering e In-Context Learning

**Técnicas de prompting**:

| Técnica | Descrição | Exemplo |
|---------|-----------|---------|
| **Zero-shot** | Instrução direta | "Classifique: 'Filme excelente!' → Positivo" |
| **Few-shot** | Exemplos no prompt | "Bom: Positivo. Ruim: Negativo. Excelente: ?" |
| **Chain-of-Thought** | Raciocínio passo-a-passo | "Pense passo a passo: ..." |
| **Self-Consistency** | Amostrar múltiplos COT → votar | Múltiplos chains, resposta majoritária |
| **Tree-of-Thoughts** | Explorar múltiplos caminhos de raciocínio | BFS/DFS sobre pensamentos |
| **ReAct** | Raciocínio + Ações (chamar ferramentas) | "Pensamento: preciso buscar. Ação: search(...)" |

```python
# Exemplo conceitual de Chain-of-Thought
prompt_cot = """P: João tem 3 maçãs. Maria tem o dobro de João.
Pedro come 2 maçãs de Maria. Quantas maçãs Maria tem agora?

Vamos passo a passo:
1. João tem 3 maçãs.
2. Maria tem o dobro: 2 × 3 = 6 maçãs.
3. Pedro come 2: 6 - 2 = 4 maçãs.
4. Portanto, Maria tem 4 maçãs.

R: 4

P: Ana tem 5 livros. Carlos tem 3 livros a mais que Ana.
Ana dá 1 livro para Carlos. Quantos livros Carlos tem?

Vamos passo a passo:"""

# O modelo geraria o raciocínio e a resposta
print(prompt_cot + "\n... (modelo gera o raciocínio)")
```

---

## 8. Exemplos Integrados com HuggingFace

### 8.1 Pipeline de Sentimento

```python
from transformers import pipeline

sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="neuralmind/bert-base-portuguese-cased",
)

textos = [
    "Este filme é simplesmente maravilhoso!",
    "Que experiência terrível, recomendo não ir.",
    "O produto é ok, nada de especial.",
]

resultados = sentiment_pipeline(textos)
for texto, resultado in zip(textos, resultados):
    print(f"Texto: '{texto}' → {resultado['label']} (score: {resultado['score']:.3f})")
```

### 8.2 Perguntas e Respostas

```python
qa_pipeline = pipeline("question-answering",
                       model="pierreguillou/bert-base-cased-squad-v1.1-portuguese")

contexto = """
Alan Turing foi um matemático, cientista da computação e criptoanalista britânico.
Ele é considerado o pai da ciência da computação teórica e da inteligência artificial.
Durante a Segunda Guerra Mundial, Turing trabalhou em Bletchley Park quebrando
o código Enigma alemão. Ele também propôs o Teste de Turing em 1950.
"""

perguntas = [
    "Quem foi Alan Turing?",
    "O que Turing fez durante a Segunda Guerra Mundial?",
    "Quando foi proposto o Teste de Turing?",
]

for pergunta in perguntas:
    resultado = qa_pipeline(question=pergunta, context=contexto)
    print(f"P: {pergunta}")
    print(f"R: {resultado['answer']} (score: {resultado['score']:.3f})\n")
```

### 8.3 Classificação Zero-Shot

```python
zero_shot = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli",
)

texto = "O novo modelo de linguagem alcançou performance superior em benchmarks."
candidatos = ["tecnologia", "esportes", "política", "ciência", "economia"]

resultado = zero_shot(texto, candidate_labels=candidatos)
print(f"Texto: {texto}")
for label, score in zip(resultado['labels'], resultado['scores']):
    print(f"  {label}: {score:.3f}")
```

### 8.4 Geração de Texto

```python
generator = pipeline("text-generation", model="gpt2")

prompt = "Artificial intelligence will"
output = generator(
    prompt,
    max_length=100,
    temperature=0.8,
    top_p=0.9,
    do_sample=True,
    num_return_sequences=2,
)

for i, seq in enumerate(output):
    print(f"\n--- Geração {i+1} ---\n{seq['generated_text']}")
```

---

## 9. Glossário

| Termo | Definição |
|-------|-----------|
| **Attention** | Mecanismo que pondera a importância relativa entre elementos de uma sequência |
| **BERT** | Modelo encoder-only da Google com atenção bidirecional e MLM |
| **BPE** | Byte-Pair Encoding; algoritmo de tokenização subword que funde pares frequentes |
| **CBOW** | Continuous Bag-of-Words; arquitetura Word2Vec que prediz palavra do contexto |
| **Causal LM** | Modelo que só vê tokens anteriores (autoregressivo) |
| **DPO** | Direct Preference Optimization; alinhamento sem reward model explícito |
| **Embedding** | Representação vetorial densa de um token em espaço contínuo |
| **Fine-tuning** | Ajuste de modelo pré-treinado para tarefa específica |
| **GPT** | Generative Pre-trained Transformer; modelo decoder-only |
| **GRU** | Gated Recurrent Unit; simplificação da LSTM com 2 portas |
| **LLaMA** | Large Language Model Meta AI; arquitetura decoder-only eficiente |
| **LoRA** | Low-Rank Adaptation; fine-tuning eficiente com matrizes de baixo rank |
| **LSTM** | Long Short-Term Memory; RNN com portas para evitar vanishing gradient |
| **MLM** | Masked Language Model; treino BERT que mascara tokens |
| **MoE** | Mixture of Experts; apenas parte dos parâmetros ativados por token |
| **Multi-Head Attention** | Múltiplas atenções paralelas capturando diferentes relações |
| **Perplexidade** | $e^{H(p)}$; mede quão bem o modelo prediz uma sequência |
| **RLHF** | Reinforcement Learning from Human Feedback; alinhamento com feedback humano |
| **RoPE** | Rotary Position Embedding; codificação posicional rotativa |
| **Self-Attention** | Atenção entre tokens da mesma sequência |
| **Skip-gram** | Arquitetura Word2Vec que prediz contexto da palavra alvo |
| **TF-IDF** | Ponderação de termos por frequência no documento e raridade no corpus |
| **Transformer** | Arquitetura baseada em atenção, sem recorrência (Vaswani et al., 2017) |
| **Word2Vec** | Modelo de embeddings estáticos (Mikolov et al., 2013) |

---

## 10. Referências

### Artigos Fundacionais
- Mikolov, T. et al. (2013). *Efficient Estimation of Word Representations in Vector Space*. ICLR Workshop.
- Mikolov, T. et al. (2013). *Distributed Representations of Words and Phrases and their Compositionality*. NeurIPS.
- Pennington, J., Socher, R. & Manning, C. D. (2014). *GloVe: Global Vectors for Word Representation*. EMNLP.
- Bojanowski, P. et al. (2017). *Enriching Word Vectors with Subword Information*. TACL.
- Hochreiter, S. & Schmidhuber, J. (1997). *Long Short-Term Memory*. Neural Computation, 9(8).
- Cho, K. et al. (2014). *Learning Phrase Representations using RNN Encoder-Decoder for Statistical Machine Translation*. EMNLP.
- Bahdanau, D., Cho, K. & Bengio, Y. (2015). *Neural Machine Translation by Jointly Learning to Align and Translate*. ICLR.
- Vaswani, A. et al. (2017). *Attention Is All You Need*. NeurIPS.
- Devlin, J. et al. (2019). *BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding*. NAACL.
- Radford, A. et al. (2018). *Improving Language Understanding by Generative Pre-Training* (GPT-1). OpenAI.
- Radford, A. et al. (2019). *Language Models are Unsupervised Multitask Learners* (GPT-2). OpenAI.
- Brown, T. et al. (2020). *Language Models are Few-Shot Learners* (GPT-3). NeurIPS.
- Touvron, H. et al. (2023). *LLaMA: Open and Efficient Foundation Language Models*. arXiv:2302.13971.
- Touvron, H. et al. (2023). *Llama 2: Open Foundation and Fine-Tuned Chat Models*. arXiv:2307.09288.

### Fine-tuning e Alinhamento
- Hu, E. J. et al. (2021). *LoRA: Low-Rank Adaptation of Large Language Models*. ICLR.
- Ouyang, L. et al. (2022). *Training language models to follow instructions with human feedback* (InstructGPT). NeurIPS.
- Rafailov, R. et al. (2023). *Direct Preference Optimization: Your Language Model is Secretly a Reward Model*. NeurIPS.
- Wei, J. et al. (2022). *Chain-of-Thought Prompting Elicits Reasoning in Large Language Models*. NeurIPS.

### Livros e Cursos
- Jurafsky, D. & Martin, J. H. (2023). *Speech and Language Processing* (3ª ed. draft). Stanford.
- Goldberg, Y. (2017). *Neural Network Methods for Natural Language Processing*. Morgan & Claypool.
- Eisenstein, J. (2019). *Introduction to Natural Language Processing*. MIT Press.
- Goodfellow, I., Bengio, Y. & Courville, A. (2016). *Deep Learning*. MIT Press. (Capítulos 10, 12)

### Conexões com Outras Notas
- [[04-Conhecimentos/07-Humanidades/Computacao/Ciencia-da-Computacao]] — hierarquia de Chomsky, autômatos, fundamentos teóricos
- [[04-Conhecimentos/07-Humanidades/Computacao/Algoritmos-e-Estruturas]] — implementação de algoritmos de treino e inferência
- [[04-Conhecimentos/07-Humanidades/Linguistica/Linguistica-e-Semiotica]] — linguística estrutural, semiótica, pragmática
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial]] — vetores, matrizes, SVD para embeddings
- [[04-Conhecimentos/07-Humanidades/Matematica/Teoria-da-Informacao]] — entropia, divergência KL, perplexidade
- [[04-Conhecimentos/07-Humanidades/Matematica/Probabilidade-e-Estatistica]] — MLE, distribuições, inferência
