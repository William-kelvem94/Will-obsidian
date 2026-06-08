---
title: "Generative Models"
category: "AI"
level: 3
description: "Arquiteturas de modelos generativos: Transformers, Difusao, GANs e VAEs para geracao e sintese de dados."
projects:
  - "JARVIS Core"
related_skills:
  - "MLOps"
  - "Reinforcement Learning"
  - "Engenharia de Prompts"
resources:
  - "Attention is All You Need (Vaswani et al., 2017)"
  - "Denoising Diffusion Probabilistic Models (Ho et al., 2020)"
  - "Tutoriais de geracao multimodal"
date: 2026-04-29
tags: [skills, ai, generative-models]
updated: 2026-06-07
---

# Generative Models

Modelos generativos aprendem a criar novos exemplos semelhantes aos dados de treinamento — imagens, texto, audio e representacoes latentes. Este documento cobre as principais arquiteturas, tecnicas de treinamento e estrategias de prompt para geracao.

## Arquiteturas Principais

### Transformer (Geracao de Texto)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("microsoft/phi-3-mini-4k-instruct")
tokenizer = AutoTokenizer.from_pretrained("microsoft/phi-3-mini-4k-instruct")

def generate_text(prompt: str, max_tokens: int = 512) -> str:
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_tokens,
        temperature=0.7,
        top_p=0.9,
        do_sample=True
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
```

### Modelo de Difusao (Geracao de Imagens)

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16
).to("cuda")

def generate_image(prompt: str, steps: int = 30) -> Image:
    return pipe(
        prompt,
        num_inference_steps=steps,
        guidance_scale=7.5,
        negative_prompt="baixa qualidade, distorcido"
    ).images[0]
```

### VAE (Variational Autoencoder)

```python
import torch.nn as nn

class VAE(nn.Module):
    def __init__(self, input_dim: int = 784, latent_dim: int = 20):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, 256),
            nn.ReLU(),
            nn.Linear(256, latent_dim * 2)  # mu e log_var
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.ReLU(),
            nn.Linear(256, input_dim),
            nn.Sigmoid()
        )

    def reparameterize(self, mu: Tensor, log_var: Tensor) -> Tensor:
        std = torch.exp(0.5 * log_var)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x: Tensor) -> tuple[Tensor, Tensor, Tensor]:
        params = self.encoder(x)
        mu, log_var = params.chunk(2, dim=1)
        z = self.reparameterize(mu, log_var)
        return self.decoder(z), mu, log_var
```

### GAN (Generative Adversarial Network)

```python
class Generator(nn.Module):
    def __init__(self, latent_dim: int = 100):
        super().__init__()
        self.model = nn.Sequential(
            nn.Linear(latent_dim, 256),
            nn.LeakyReLU(0.2),
            nn.Linear(256, 512),
            nn.LeakyReLU(0.2),
            nn.Linear(512, 1024),
            nn.LeakyReLU(0.2),
            nn.Linear(1024, 784),
            nn.Tanh()
        )

    def forward(self, z: Tensor) -> Tensor:
        return self.model(z)
```

## Tabela Comparativa

| Arquitetura | Tipo de Dado | Qualidade | Diversidade | Estabilidade Treino |
|-------------|-------------|-----------|-------------|-------------------|
| Transformer | Texto, Codigo | Alta | Alta | Estavel |
| Diffusion | Imagem, Audio | Muito Alta | Media | Estavel |
| VAE | Imagem, Dados tabulares | Media | Alta | Muito Estavel |
| GAN | Imagem, Video | Alta | Baixa | Instavel |

## Tecnicas de Prompt para Modelos Generativos

### Chain-of-Thought para Geracao

```
Sistema: Voce e um assistente de codigo. Explique o raciocinio passo a passo.
Usuario: Gere uma funcao que valide CPF em Python.
```

### Negative Prompting (Difusao)

```python
prompt = "fotografia de paisagem, alta resolucao, 4k"
negative = "desfocado, agua, texto, assinatura, baixa qualidade"
image = pipe(prompt, negative_prompt=negative).images[0]
```

## Treinamento e Fine-Tuning

```python
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./modelo-gerativo",
    per_device_train_batch_size=4,
    gradient_accumulation_steps=4,
    learning_rate=2e-5,
    num_train_epochs=3,
    fp16=True,
    save_steps=500,
    logging_steps=100,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=collator,
)
trainer.train()
```

## Casos de Uso para JARVIS

- **Dados Sinteticos**: Aumentar dataset de treino para modelos de classificacao
- **Aumentacao de Contexto RAG**: Gerar variacoes de chunks para enriquecer indices
- **Geracao de UI**: Produzir mockups de interfaces a partir de descricoes textuais
- **Sumarizacao Multimodal**: Converter imagens em descricoes textuais para indexacao

## Referencias

- [[05-Skills/skills/ai/Engenharia-de-Prompts|Engenharia de Prompts]] — Tecnicas de prompt para modelos generativos
- [[05-Skills/skills/ai/MLOps|MLOps]] — Pipeline de treino e deploy de modelos
- [[05-Skills/skills/04-knowledge-systems/advanced-rag-strategies|RAG Avancado]] — Aumentacao de contexto com dados sinteticos
- [[04-Conhecimentos/07-Humanidades/Matematica/Algebra-Linear-Essencial|Algebra Linear]] — Fundamentos de espacos latentes
