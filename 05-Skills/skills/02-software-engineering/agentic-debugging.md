---
title: "Agentic Debugging — O Método de Investigação Científica de Bugs por IAs"
description: "Guia completo de diagnóstico de falhas, formulação científica de hipóteses, isolamento de variáveis e validação baseada em evidência para agentes de IA."
tags: [skill, software-engineering, debug, agents, root-cause, telemetry, skills-eng]
updated: 2026-06-07
status: active
date: 2026-06-01
---

# Agentic Debugging (Método de Investigação Científica)

O depurador autônomo (Agentic Debugging) não tenta resolver problemas por tentativa e erro estocástica, aplicando *fixes* aleatórios de forma cega. Em vez disso, o agente adota o **método científico cartesiano**: coleta telemetria inicial, restringe a área de impacto, isola variáveis de contexto, formula hipóteses testáveis de forma independente e cria testes reproduzíveis mínimos (*minimal reproducers*) antes de propor patches.

Este guia estabelece o padrão profissional para o diagnóstico e mitigação sistemática de incidentes por agentes de IA e engenheiros humanos no vault.

---

## 🧭 1. O Método Científico de Depuração

```
┌─────────────────────────────────┐
│  Coleta de Evidências Iniciais  │
└────────────────┬────────────────┘
                 ▼
┌─────────────────────────────────┐
│     Isolamento de Variáveis     │
└────────────────┬────────────────┘
                 ▼
┌─────────────────────────────────┐
│     Formulação de Hipóteses     │
└────────────────┬────────────────┘
                 ▼
┌─────────────────────────────────┐
│ Criação do Reprodutor Mínimo(Rep)  │
└────────────────┬────────────────┘
                 ▼
┌─────────────────────────────────┐
│ Aplicação do Fix & Verificação  │
└─────────────────────────────────┘
```

### Passo 1: Coleta de Evidências Iniciais
O agente deve extrair a assinatura completa do erro:
*   **Pilhas de Execução (Stack Traces)**: O rastro do fluxo de chamadas que culminou na exceção.
*   **Logs de Telemetria**: Logs correlatos do sistema e dos serviços adjacentes no mesmo timestamp.
*   **Diferenças de Versão (Diffs/Metadata)**: Entender o que mudou no ecossistema (deploys recentes, esquemas modificados, versões de bibliotecas atualizadas).

### Passo 2: Isolamento de Variáveis e Limites
Eliminar o ruído instrumental. Limitar o escopo da falha por meio da identificação exata da camada afetada:
*   A falha reside na camada de **Interface (UI)**, na **Lógica de Aplicação (API)**, na persistência de **Dados (DB)** ou em uma **Integração Externa (Serviços/Third-Party)**?
*   É possível contornar a falha modificando apenas parâmetros locais de chamadas?

### Passo 3: Formulação de Hipóteses Pequenas
Criar uma árvore mental ou expressa de causas plausíveis. Uma hipótese útil é estritamente **específica** e **refutável**:
*   *Exemplo Inútil*: "O código do orquestrador está instável".
*   *Exemplo Útil*: "A função de parser falha ao processar strings JSON contendo caracteres unicode e quebras de linha cruas, disparando erro de decodificação na biblioteca nativa".

### Passo 4: Criação do Reprodutor Mínimo (Reproducible Harness)
Antes de editar qualquer linha do código de produção, o investigador deve construir uma prova de conceito que isole o fluxo problemático. No Python, isso geralmente envolve escrever um pequeno script síncrono isolado de teste:

```python
# tests/reproducers/repro_json_unicode_bug.py
import json

def parse_incoming_payload(raw_str):
    # Função correspondente simplificada para isolar o problema
    data = json.loads(raw_str)
    return data["message"]

def test_repro():
    # Payload com quebra de linha crua simulando entrada defeituosa do webhook
    malformed_payload = '{\n"message": "Linha 1\nLinha 2"\n}'
    
    try:
        parse_incoming_payload(malformed_payload)
        print("✅ PASSOU (Inesperado se houver bug!)")
    except json.JSONDecodeError as err:
        print(f"❌ REPRODUZIDO COM SUCESSO: {err}")
        # Isto é uma evidência irrefutável!

if __name__ == "__main__":
    test_repro()
```

### Passo 5: Aplicação do Patch Cirúrgico & Validação Dupla
A correção deve atacar a raiz da falha identificada, sem desencadear efeitos colaterais indesejáveis em outras seções do software. 
*   Rode o reprodutor para comprovar que ele agora retorna sucesso (Pass).
*   Execute a suíte geral de testes unitários adjacentes para certificar-se de que não houve regressão funcional.

---

## 🛠️ 2. Guia de Sandbox e Técnicas de Isolamento

Para identificar e debugar os bugs de forma limpa, utilize técnicas de rastreamento estrito de eventos:

| Técnica | Instrumento | Vantagem para o Agente |
|---------|-------------|-------------------------|
| **Log Trace Dinâmico** | `sys.settrace()` (Python) | Captura cada linha executada sob demanda |
| **Interceptação HTTP** | `mitmproxy` / Nock | Isola totalmente requisições de rede externas |
| **Execução Isolada** | Docker containers / Sandboxes | Evita destruição acidental ou poluição do SO host |
| **Injeção de Erros (Chaos)**| Monkey Patching | Simula falhas em conexões externas para testar tratamento de exceções |

### Exemplo de Monkey Patching para Teste de Conexão Rígida (Python)
```python
# Simular timeout de cache em produção de forma controlada
import redis
import pytest

def test_redis_timeout_resilience(monkeypatch):
    def mock_get(*args, **kwargs):
        raise redis.exceptions.TimeoutError("Simulated write timeout")
        
    # Intercepta dinamicamente a chamada do cliente Redis
    monkeypatch.setattr(redis.Redis, "get", mock_get)
    
    # Roda a função de aplicação e verifica se ela trata o erroElegantemente
    with pytest.raises(redis.exceptions.TimeoutError):
        # código resiliente da aplicação que deve repassar ou tratar
        resilient_fetch_cached_data()
```

---

## 📑 3. Estrutura de Relato de Diagnóstico (Incident Post-Mortem)

Sempre que concluir um depuração complexa, registre a análise de causa raiz usando este formato mínimo de post-mortem para preservar a lição no vault:

1.  **Sintoma**: O que foi experimentado de forma visível pelo usuário ou sistema?
2.  **Causa Raiz**: O que causou a falha operacional em nível técnico de detalhe?
3.  **Correção Adotada**: Como o patch resolveu o problema sem efeitos colaterais?
4.  **Prevenção Sistêmica**: O que foi feito ou sugerido (testes adicionais, logs estruturados extras) para impedir que esse bug específico retorne?
*Assegure-se de vincular a nota de post-mortem às notas de lições aprendidas correspondentes.*

