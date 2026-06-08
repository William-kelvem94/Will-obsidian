---
titulo: Caso de Uso: Integração de API Externa
contexto: Necessidade de consumir dados externos em tempo real
abordagem: Consumo REST API com autenticação e cache intermediário
exemplo: Conexão com API pública de clima usando requests + Obsidian plugin
resultados: Obtenção automatizada de dados, performance e cache aprimorados
---

# Caso de Uso: Integração de API Externa

## Contexto
Necessidade de consumir dados externos em tempo real para dashboards internos.

## Abordagem
Uso do plugin Obsidian Scripts + Python requests para buscar dados e gravar em nota automática. Autenticação por token e controle de limite de chamadas pelo próprio script e por log de acesso.

## Exemplo Prático
```python
import requests
from datetime import datetime
API = "https://api.weatherapi.com/v1/current.json?key=YOURKEY&q=SaoPaulo"
resp = requests.get(API)
data = resp.json()
... # processa e grava
```

## Resultados & Lições
Melhoria do tempo de resposta. Facilidade de automação para múltiplos tópicos. Checklist de segurança implementado.