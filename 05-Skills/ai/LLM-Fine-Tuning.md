---
title: "LLM Fine-Tuning"
description: "Guia completo de fine-tuning de LLMs: quando fine-tuning e necessario vs RAG vs prompting, tecnicas eficientes (LoRA, QLoRA, adapters), preparacao de datasets, SFT, RLHF, DPO, avaliacao e ferramentas praticas para Llama, Mistral e Gemma."
tags: [fine-tuning, lora, qlora, sft, rlhf, dpo, huggingface, llm, transformers, skills]
nivel: avancado
fonte: ""
updated: 2026-06-08
backlinks: ["05-Skills/ai/INDEX"]
assets: []
referencias: []
sensivel: false
date: 2026-06-01
---

# LLM Fine-Tuning

## Por que Fine-Tuning?

Fine-tuning e o processo de ajustar os pesos de um modelo pre-treinado para uma tarefa ou dominio especifico. E uma das tres estrategias principais para adaptar LLMs:

| Estrategia | Quando usar | Custo | Qualidade | Exemplo |
|-----------|-------------|-------|-----------|---------|
| **Prompt Engineering** | Tarefas simples, sem dados rotulados, prototipagem | $ | Boa | Classificar sentimento de reviews |
| **RAG** | Conhecimento factual, documentos atualizaveis, citacao | $$ | Boa-alta | Chat sobre documentacao interna |
| **Fine-Tuning** | Estilo/tom especifico, tarefas estruturadas, latencia baixa | $$$ | Alta | Assistente juridico com vocabulario tecnico |
| **Pre-Training** | Dominio totalmente novo, sem modelo base adequado | $$$$$ | Maxima | Modelo especifico para quimica |

### Quando fine-tuning e necessario

- O modelo precisa aprender um formato de saida estruturado especifico (JSON schema complexo)
- O dominio tem vocabulario ou conceitos que o modelo base nao conhece (codigo legado, jargao medico)
- A tarefa exige consistencia em estilo/tom que prompting nao alcanca
- Custos de inferencia precisam ser reduzidos (modelo menor fine-tunado supera modelo maior com prompting)
- Latencia e critica (fine-tuning permite usar modelos menores com performance de modelos maiores)

### Quando NAO fazer fine-tuning

- Conhecimento factual atualizavel (use RAG)
- Prototipagem ou validacao de hipotese (comece com prompting)
- Falta de dados rotulados de qualidade
- Tarefa que o modelo base ja executa bem com prompting simples

## Tecnicas Eficientes (Parameter-Efficient Fine-Tuning - PEFT)

### LoRA (Low-Rank Adaptation)

LoRA congela os pesos originais e injeta matrizes de baixo rank treinaveis em camadas de atencao.

```
W_original (d x k)  →  congelado
B (d x r) * A (r x k)  →  treinavel, r << d
W_finetuned = W_original + B * A

Com r=8 e d=4096:
  Parametros originais: 4096 * 4096 = 16.7M
  Parametros LoRA: 4096*8 + 8*4096 = 65K (0.39% dos originais)
```

```python
import torch
import torch.nn as nn

class LoRALinear(nn.Module):
    """Camada linear com adaptacao LoRA."""
    def __init__(self, in_features, out_features, rank=8, alpha=16):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.linear.weight.requires_grad = False  # Congelar

        # Matrizes LoRA de baixo rank
        self.lora_A = nn.Parameter(torch.randn(in_features, rank) * 0.01)
        self.lora_B = nn.Parameter(torch.zeros(rank, out_features))
        self.scaling = alpha / rank

    def forward(self, x):
        # Saida original + adaptacao LoRA
        return self.linear(x) + (x @ self.lora_A @ self.lora_B) * self.scaling
```

### QLoRA (Quantized LoRA)

LoRA + quantizacao de 4 bits (NF4) para caber modelos grandes em GPUs consumer.

```python
# QLoRA com bitsandbytes - cabe Llama-70B em 48GB VRAM
from transformers import BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
```

### Adapters e Prefix Tuning

```python
# IA3 (Infused Adapter by Inhibiting and Amplifying)
# Similar ao LoRA mas com learning por camada (lora_scalar)
from peft import IA3Config, get_peft_model

ia3_config = IA3Config(
    target_modules=["q_proj", "v_proj"],
    feedforward_modules=["down_proj"],
)
model = get_peft_model(base_model, ia3_config)

# Prefix Tuning: tokens virtuais no inicio do prompt
# (p_theta = MLP([eos] * n_prefix))
from peft import PrefixTuningConfig, TaskType

prefix_config = PrefixTuningConfig(
    task_type=TaskType.CAUSAL_LM,
    num_virtual_tokens=20,
    encoder_hidden_size=512,
)
model = get_peft_model(base_model, prefix_config)
```

### Tabela Comparativa PEFT

| Tecnica | Parametros extras | % treinavel | Performance (relativa a full FT) | Memory |
|---------|------------------|-------------|----------------------------------|--------|
| Full FT | 100% | 100% | 1.0x | Muita |
| LoRA (r=8) | 0.1-1% | <1% | 0.95-1.0x | Baixa |
| QLoRA (r=8) | 0.1-1% | <1% | 0.93-0.98x | Minima |
| IA3 | ~0.01% | 0.01% | 0.85-0.95x | Minima |
| Prefix Tuning | Virtual tokens | 0.1% | 0.80-0.95x | Baixa |
| Adapter | Pequenos blocos | 3-5% | 0.90-0.98x | Media |

## Preparacao de Datasets

### Formatacao

O formato do dataset depende do tipo de fine-tuning:

**Chat / Instrucao**:
```json
[
  {
    "conversations": [
      {"role": "system", "content": "Voce e um assistente juridico especializado em direito imobiliario."},
      {"role": "user", "content": "Quais documentos sao necessarios para registrar um contrato de aluguel?"},
      {"role": "assistant", "content": "Para registrar um contrato de aluguel no Brasil, sao necessarios: ..."}
    ]
  }
]
```

**Completacao (texto unico)**:
```json
[
  {"text": "### Instrucao: Explique o que e fine-tuning\n### Resposta: Fine-tuning e o processo de ...</s>"}
]
```

**ChatML**:
```json
[
  {"messages": [
    {"role": "user", "content": "O que e QLoRA?"},
    {"role": "assistant", "content": "QLoRA combina quantizacao de 4 bits com LoRA..."}
  ]}
]
```

### Qualidade e Balancing

```python
import pandas as pd
from datasets import Dataset, load_dataset
from collections import Counter

def prepare_dataset(csv_path: str, min_length: int = 10, max_length: int = 4096):
    """Prepara e valida dataset para fine-tuning."""
    df = pd.read_csv(csv_path)

    # Estatisticas basicas
    print(f"Total de exemplos: {len(df)}")
    print(f"Tamanho medio: {df['text'].str.len().mean():.0f} chars")

    # Remover exemplos muito curtos ou vazios
    df = df[df['text'].str.len() >= min_length]
    df = df.dropna(subset=['text'])

    # Verificar balanceamento (se houver labels)
    if 'label' in df.columns:
        label_dist = Counter(df['label'])
        print(f"Distribuicao: {dict(label_dist)}")

    # Amostragem estrategica para evitar overfitting em classes majoritarias
    if 'label' in df.columns:
        min_count = min(label_dist.values())
        balanced = df.groupby('label').apply(
            lambda x: x.sample(min(len(x), min_count * 2), random_state=42)
        ).reset_index(drop=True)
        print(f"Dataset balanceado: {len(balanced)} exemplos")
        df = balanced

    # Split treino/validacao
    split = int(len(df) * 0.9)
    train = Dataset.from_pandas(df.iloc[:split])
    val = Dataset.from_pandas(df.iloc[split:])

    return train, val
```

### Tokenizacao e Formatting

```python
from transformers import AutoTokenizer

def format_and_tokenize(examples, tokenizer, max_length=2048):
    """Formata e tokeniza exemplos para causal LM."""
    texts = []
    for conv in examples['conversations']:
        formatted = tokenizer.apply_chat_template(
            conv, tokenize=False, add_generation_prompt=False
        )
        texts.append(formatted)

    tokenized = tokenizer(
        texts,
        truncation=True,
        padding='max_length',
        max_length=max_length,
        return_tensors='pt',
    )

    # Para causal LM, labels sao iguais aos input_ids
    # Mascarar tokens do prompt (opcional)
    tokenized['labels'] = tokenized['input_ids'].clone()
    return tokenized
```

## Supervised Fine-Tuning (SFT)

### Exemplo Completo com TRL

```python
# install: pip install transformers datasets accelerate peft trl bitsandbytes

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
)
from datasets import load_dataset
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from trl import SFTTrainer
from transformers import BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)

model_name = "mistralai/Mistral-7B-Instruct-v0.3"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token
tokenizer.padding_side = "right"

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    quantization_config=bnb_config,
    device_map="auto",
    trust_remote_code=True,
)

model = prepare_model_for_kbit_training(model)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_dropout=0.1,
    bias="none",
    task_type="CAUSAL_LM",
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()

dataset = load_dataset("json", data_files="contratos_aluguel.jsonl")
dataset = dataset["train"].train_test_split(test_size=0.1)

training_args = TrainingArguments(
    output_dir="./mistral-contratos",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=4,
    gradient_checkpointing=True,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True,
    bf16=False,
    save_strategy="epoch",
    evaluation_strategy="epoch",
    logging_steps=10,
    report_to="wandb",
    warmup_ratio=0.03,
    lr_scheduler_type="cosine",
    optim="paged_adamw_8bit",
    max_grad_norm=0.3,
    save_total_limit=2,
    remove_unused_columns=False,
    ddp_find_unused_parameters=False,
)

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"],
    max_seq_length=2048,
    dataset_text_field="text",
    packing=False,
)

trainer.train()
trainer.save_model("./mistral-contratos-final")
tokenizer.save_pretrained("./mistral-contratos-final")
```

### Dicas Praticas para SFT

- **Learning rate**: 1e-4 a 5e-4 para LoRA, 1e-5 a 5e-5 para full FT
- **Batch size**: maior possivel sem OOM (gradient accumulation ajuda)
- **Epochs**: 2-5 normalmente; mais epochs pode causar overfitting
- **Warmup**: 3-10% do total de steps
- **Cosine scheduler**: geralmente melhor que linear
- **Gradient checkpointing**: reduz memoria em 30-50%
- **Packing**: concatenar sequencias curtas para preencher max_seq_length

## RLHF e DPO

### RLHF (Reinforcement Learning from Human Feedback)

Pipeline em 3 etapas:

```
1. SFT → Modelo base fine-tunado em demonstracoes
2. Reward Model → Modelo treinado para rankear respostas
3. PPO → Otimizar o modelo SFT contra o reward model

RMS = SFT(theta) + lambda_r * R(theta) - lambda_kl * KL(SFT || theta)
```

```python
# Passo 1: SFT
# (codigo acima)

# Passo 2: Treinar Reward Model
from trl import RewardTrainer

reward_model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=1
)
reward_trainer = RewardTrainer(
    model=reward_model,
    args=training_args,
    train_dataset=preference_dataset,
    tokenizer=tokenizer,
)
reward_trainer.train()

# Passo 3: PPO (Proximal Policy Optimization)
from trl import PPOConfig, PPOTrainer

ppo_config = PPOConfig(
    model_name=model_name,
    learning_rate=1e-5,
    batch_size=16,
    mini_batch_size=4,
)

ppo_trainer = PPOTrainer(
    config=ppo_config,
    model=sft_model,
    tokenizer=tokenizer,
    reward_model=reward_model,
)
```

### DPO (Direct Preference Optimization)

DPO simplifica RLHF eliminando o reward model explicito.

```python
from trl import DPOTrainer

dpo_config = DPOConfig(
    output_dir="./modelo-dpo",
    beta=0.1,  # Controle de KL divergence
    max_length=2048,
    max_prompt_length=1024,
    learning_rate=5e-6,
    per_device_train_batch_size=4,
    num_train_epochs=3,
)

dpo_trainer = DPOTrainer(
    model=model,
    ref_model=None,  # Se None, usa o modelo base como referencia
    args=dpo_config,
    train_dataset=dpo_dataset,  # Formato: {prompt, chosen, rejected}
    tokenizer=tokenizer,
)

dpo_trainer.train()
```

### DPO vs RLHF

| Aspecto | RLHF (PPO) | DPO |
|---------|-----------|-----|
| Complexidade | Alta (3 modelos) | Baixa (apenas o modelo) |
| Estabilidade | Instavel (hiperparametros sensiveis) | Estavel |
| Qualidade | Potencialmente melhor | Comparavel |
| Custo de treino | Alto (online) | Baixo (offline) |
| Dados necessarios | Preferencias + prompts | Preferencias apenas |
| Adocao industrial | Claude, GPT-4 | Llama 3, Gemma 2 |

### Dataset de Preferencias

```json
[
  {
    "prompt": "Explique o que e fine-tuning em uma frase.",
    "chosen": "Fine-tuning e o processo de ajustar os pesos de um modelo pre-treinado para uma tarefa especifica usando dados rotulados.",
    "rejected": "Fine-tuning e quando voce mexe nos parametros do modelo para ele funcionar melhor."
  }
]
```

## Avaliacao

### Benchmarks

```python
from lm_eval import evaluator

results = evaluator.simple_evaluate(
    model="hf",
    model_args="pretrained=./modelo-finetunado",
    tasks=["hellaswag", "arc_easy", "mmlu"],
    num_fewshot=5,
    batch_size=8,
)

print(f"Media: {results['results']['mmlu']['acc']*100:.1f}%")
```

### Perplexity

```python
import math

def calculate_perplexity(model, tokenizer, texts, max_length=2048):
    model.eval()
    total_loss = 0
    total_tokens = 0

    with torch.no_grad():
        for text in texts:
            inputs = tokenizer(text, return_tensors="pt", truncation=True,
                               max_length=max_length)
            inputs = {k: v.to(model.device) for k, v in inputs.items()}
            outputs = model(**inputs, labels=inputs["input_ids"])
            total_loss += outputs.loss.item() * inputs["input_ids"].size(1)
            total_tokens += inputs["input_ids"].size(1)

    return math.exp(total_loss / total_tokens)
```

### Avaliacao Humana e LLM-as-Judge

```python
import openai

def llm_as_judge(prompt: str, response_a: str, response_b: str) -> dict:
    """Usa GPT-4 como juiz para comparar duas respostas."""
    judge_prompt = f"""
    Compare as duas respostas para o prompt abaixo.
    A: {response_a}
    B: {response_b}

    Criterios (1-5): relevancia, precisao, clareza, utilidade, seguranca
    Qual resposta e melhor? Justifique.
    """

    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": judge_prompt}],
    )
    return response.choices[0].message.content

# Avaliacao automatica em lote
def batch_evaluate(dataset, model, judge_fn, sample_size=100):
    """Avalia modelo contra dataset de teste usando LLM-as-Judge."""
    import random
    sample = random.sample(dataset, sample_size)
    scores = []

    for item in sample:
        prompt = item["prompt"]
        ground_truth = item["chosen"]
        model_response = generate(model, prompt)

        score = judge_fn(prompt, ground_truth, model_response)
        scores.append(score)

    return {
        "mean_score": sum(scores) / len(scores),
        "scores": scores,
    }
```

## Ferramentas

### Hugging Face Transformers + TRL

```bash
pip install transformers datasets accelerate peft trl bitsandbytes scipy wandb
```

TRL (Transformer Reinforcement Learning) e a biblioteca oficial da HF para SFT, reward modeling, PPO e DPO.

### Axolotl

Framework opinativo que simplifica fine-tuning com config YAML.

```yaml
# axolotl_config.yaml
base_model: mistralai/Mistral-7B-Instruct-v0.3

lora:
  r: 16
  lora_alpha: 32
  target_modules:
    - q_proj
    - k_proj
    - v_proj
    - o_proj
    - gate_proj
    - up_proj
    - down_proj
  lora_dropout: 0.1

datasets:
  - path: dados/contratos_aluguel.jsonl
    type: sharegpt
    conversation: chats

dataset_prepared_path: last_run_prepared
val_set_size: 0.1
output_dir: ./output

sequence_len: 2048
sample_packing: true
pad_to_sequence_len: true

wandb_project: finetune-contratos
wandb_watch: gradients

gradient_accumulation_steps: 4
micro_batch_size: 2
num_epochs: 3
optimizer: adamw_8bit
lr_scheduler: cosine
learning_rate: 2e-4

train_on_inputs: false
group_by_length: false
bf16: auto
fp16: false

gradient_checkpointing: true
early_stopping_patience: 3
resume_from_checkpoint:
logging_steps: 1
xformers_attention:
flash_attention: true
```

```bash
# Treinar com Axolotl
accelerate launch -m axolotl.cli.train axolotl_config.yaml

# Merge LoRA + export (merge dos adapters no modelo base)
accelerate launch -m axolotl.cli.merge_lora axolotl_config.yaml
```

### Unsloth

Framework otimizado para fine-tuning rapido (2x mais rapido, 50% menos memoria).

```python
import torch
from unsloth import FastLanguageModel, is_bfloat16_supported
from datasets import load_dataset

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="unsloth/mistral-7b-instruct-v0.3-bnb-4bit",
    max_seq_length=4096,
    dtype=None,
    load_in_4bit=True,
)

model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=[
        "q_proj", "k_proj", "v_proj", "o_proj",
        "gate_proj", "up_proj", "down_proj",
    ],
    lora_alpha=16,
    lora_dropout=0,
    bias="none",
    use_gradient_checkpointing="unsloth",
    random_state=42,
)

# Treinamento 2x mais rapido que HF TRL padrao
from trl import SFTTrainer, SFTConfig

trainer = SFTTrainer(
    model=model,
    tokenizer=tokenizer,
    train_dataset=dataset,
    max_seq_length=4096,
    args=SFTConfig(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=5,
        num_train_epochs=1,
        learning_rate=2e-4,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=42,
        output_dir="outputs",
    ),
)
trainer.train()

# Salvar modelo fine-tunado em 16 bits (nao 4 bits!)
model.save_pretrained_merged("modelo-final", tokenizer, save_method="merged_16bit")
```

## Pratica: Fine-Tuning de Modelos Populares

### Llama 3.1 (Meta)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

model_name = "meta-llama/Llama-3.1-8B-Instruct"

# Tokenizer com pad_token
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# Carregar em 8-bit (requer 16GB VRAM para 8B)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    load_in_8bit=True,
)

lora_config = LoraConfig(
    r=16,
    lora_alpha=32,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    lora_dropout=0.1,
)

model = get_peft_model(model, lora_config)

# Train...
```

**Requisitos**:
- Llama 3.1 8B: ~16GB VRAM (QLoRA 4-bit), ~24GB (LoRA 8-bit)
- Llama 3.1 70B: ~48GB VRAM (QLoRA 4-bit)

### Mistral

```python
model_name = "mistralai/Mistral-7B-Instruct-v0.3"
# Mesmo padrao do Llama. Mistral e mais leve e rapido de fine-tunar.

# Dica: Mistral nao tem pad_token por padrao
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = "<PAD>"
```

### Gemma (Google)

```python
model_name = "google/gemma-2-9b-it"

# Gemma usa attention com RoPE e sliding window
# Recomendado: QLoRA com target_modules=["q_proj", "v_proj"]

tokenizer = AutoTokenizer.from_pretrained(model_name)
# Gemma ja vem com chat template configurado
```

### Google Colab

```python
# Script completo para rodar no Google Colab (GPU T4 - 16GB VRAM)
# @title Instalar dependencias
!pip install -qU transformers datasets accelerate peft trl bitsandbytes

# @title Carregar modelo (QLoRA 4-bit)
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

model = AutoModelForCausalLM.from_pretrained(
    "unsloth/Mistral-7B-Instruct-v0.3-bnb-4bit",
    quantization_config=bnb_config,
    device_map="auto",
)

# @title Configurar LoRA e treinar
from peft import LoraConfig, get_peft_model
from trl import SFTTrainer, SFTConfig

# ... (mesmo codigo SFT acima)

# @title Salvar para Hugging Face Hub
from huggingface_hub import notebook_login
notebook_login()

model.push_to_hub("seu-usuario/mistral-contratos-aluguel")
tokenizer.push_to_hub("seu-usuario/mistral-contratos-aluguel")
```

### Dicas de GPU e Custo

| Modelo | Tecnica | GPU Minima | VRAM | Custo Colab (1 epoca) | Custo A100 (1 epoca) |
|--------|---------|-----------|------|----------------------|---------------------|
| Llama 3.1 8B | QLoRA r=16 | T4 | 12-14GB | $0 | ~$0.50 |
| Llama 3.1 8B | LoRA r=16 | L4 | 20GB | - | ~$1 |
| Llama 3.1 8B | Full FT | A100 40GB | 40GB+ | - | ~$5-10 |
| Mistral 7B | QLoRA r=16 | T4 | 10-12GB | $0 | ~$0.40 |
| Gemma 9B | QLoRA r=16 | T4 | 14GB | $0 | ~$0.60 |
| Llama 3.1 70B | QLoRA r=16 | A100 80GB | 48GB | - | ~$8-15 |
| Llama 3.1 405B | QLoRA | 8x A100 | 384GB | - | ~$200+ |

## Conexoes com o Vault

- [[05-Skills/ai/INDEX]] - Indice central de IA
- [[05-Skills/rag]] - RAG e fine-tuning sao complementares
- [[05-Skills/ai/Engenharia-de-Prompts]] - Prompting vs fine-tuning
- [[skill/ai/MLOps]] - MLOps para LLMs fine-tunados
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial]] - Algebra linear das matrizes LoRA
