---
tags: [map, hierarchy, vault, meta]
updated: 2026-04-21
---

# 📐 Vault Hierarchy Map

Visualização e descrição da hierarquia de pastas e domínios do vault.

## 🧱 A Pilha Tecnológica (Cofre)
O vault é estruturado em **5 Níveis de Profundidade Semântica**:

```mermaid
graph TD
    Root[Neural Hub] --> T1[Tier 01: Core & Identity]
    Root --> T2[Tier 02: Operational]
    Root --> T3[Tier 03: Experience]
    Root --> T4[Tier 04: Engineering]
    Root --> T5[Tier 05: System]

    T1 --> JARVIS_Core[JARVIS Core]
    T1 --> Will_Prof[Will Profile]
    T1 --> Active_Proj[Active Projects]

    T2 --> Context[Current Context]
    T2 --> Decisions[Decision Log]
    T2 --> Vision[Will Goals]

    T3 --> Logs[Daily Logs]
    T3 --> Learning[Learned Patterns]
    T3 --> Studies[Deep Studies]

    T4 --> Wiki[Tech Wiki]
    T4 --> Skills[AI Skills/MCP]
    T4 --> Network[Social/Redo]

    T5 --> Archive[Legacy Projects]
    T5 --> Blueprints[Templates]
    T5 --> Tools[Scripts/Github Sync]
```

## 🗺️ Mapeamento de Pastas
- `01-Identity` / `01-Ativos`: Dados fundamentais.
- `02-Operational` / `02-Visao`: Estratégia e estado atual.
- `03-Memory` / `03-Estudos` / `03-Vida-Estilo`: Registro temporal e crescimento.
- `04-Engineering` / `04-Social`: Implementação e rede.
- `05-System` / `05-Arquivo`: Manutenção e legado.

---
[[Bem-vindo]] | [[Vault-Ops]] | [[Master-Glossary]]
