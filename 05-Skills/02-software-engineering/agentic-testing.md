---
title: "Agentic Testing — Playbook de Arquitetura e Engenharia de Testes para IAs"
description: "Estratégias estruturadas de testes unitários, integração e ponta a ponta (E2E), pirâmide realista de testes, padrões de asserts e prevenção a suítes frágeis."
tags: [skill, software-engineering, testing, pytest, jest, agents, quality, skills-eng]
updated: 2026-06-10
status: active
date: 2026-06-01
---

# Agentic Testing (Playbook de Engenharia de Testes)

Sistemas inteligentes ou de base de código escaláveis necessitam de uma suíte de testes robusta, rápida e previsível. No contexto de **Agentic Testing**, a criação e refinamento de testes guiada por IA não deve focar em inflar artificialmente a cobertura de código (*coverage*) com testes redundantes ou frágeis que quebram a cada pequena refatoração estrutural de design.

O manifesto e heurisitcas abaixo orientam agentes e engenheiros a projetar testes com máxima fidelidade e baixo ruído instrumental de manutenção.

---

## 📐 1. A Pirâmide Realista de Testes para Agentes

```
          / \          ◄── E2E (Simula Fluxos Críticos / Playwright)
         /   \
        /     \        ◄── Integração (Valida Fronteiras Reais: Banco, APIs, Filas)
       /_______\
      /         \      ◄── Unitário (Lógica Pura de Métodos, Domínios Isolados, Utilitários)
     /___________\
```

### 1.1 Testes Unitários: Lógica de Domínio Isolado (Alta Velocidade)
*   **Foco**: Testar funções puras, controladores de lógica matemática, parses, transformações, regras de negócios autocontidas e gerenciamento de estado isolado.
*   **Velocidade**: Milissegundos por teste. Devem executar inteiramente em memória, livres de chamadas de rede ou IO de disco.
*   **Garantia**: Isolar e documentar condições limites, entradas malformadas e regras matemáticas limpas.

### 1.2 Testes de Integração: Boundaries Reais (Alta Fidelidade)
*   **Foco**: Validar a conectividade, transações de banco de dados, mapeamentos de ORM, orquestrações de middleware HTTP e integrações sistêmicas (ex: comunicação com instâncias Docker reais localmente via Testcontainers).
*   **Heurística de Mocks**: **Não crie mocks de banco de dados locais**. Utilize instâncias leves (SQLite em memória ou contêineres efémeros de PostgreSQL) para validar o comportamento real do SQL. Reserve mocks apenas para terceiros inacessíveis (APIs de cobrança externa, gateways de envio de SMS).

### 1.3 Testes Ponta-a-Ponta (E2E): Jornada Central do Usuário (Alta Segurança)
*   **Foco**: Simular workflows complexos, interfaces interativas (UI) com renderização real e múltiplos micro-serviços encadeados.
*   **Princípio**: Mantenha a suíte de E2E o mais direta e concisa possível (apenas as jornadas geradoras de receita e caminhos críticos). Testes E2E são caros, suscetíveis a flutuações e lentos.

---

## 🚫 2. Catálogo de Anti-padrões Sistêmicos

### 2.1 Excesso de Mocking (Mock Explosion)
*   **O Problema**: Quando um método precisa mocar 12 dependências diferentes para validar uma única linha de comportamento logicamente simples. O teste consome tempos de carregamento severos e falha em detectar erros quando a assinatura do método mocado real é alterada.
*   **A Solução**: Aplicar os princípios SOLID para reduzir o acoplamento do método. Se os acoplamentos forem inevitáveis, converta para um teste de integração real.

### 2.2 Asserts Genéricos e Fracos
*   **O Problema**: Testes que utilizam validações que confirmam apenas se a função executou, mas não o dado que retornou.
    ```python
    # ❌ RUIM: Asserts genéricos desprovidos de precisão semântica
    assert response is not None
    assert response.status_code == 200
    ```
*   **A Solução**: Garantir que as propriedades lógicas internas dos objetos de retorno correspondam explicitamente ao esperado.
    ```python
    # ✅ BOM: Validação exata de dados e contratos
    assert response.status_code == 200
    assert response.json()["user"]["email"] == "test@user.com"
    assert response.json()["user"]["is_active"] is True
    ```

### 2.3 Acoplamento de Detalhes Internos (Whitebox Overtesting)
*   **O Problema**: Escrever testes que dependem de atributos internos protegidos ou privados de bibliotecas. Se o desenvolvedor refatora de forma impecável a estrutura interna mantendo o retorno público idêntico, a suite quebra mesmo sem regressão.
*   **A Solução**: Teste a API pública exposta pelo módulo (métodos públicos e outputs esperados). Trate o componente como uma caixa-preta funcional sempre que aplicável.

---

## 💻 3. Padrões de Implementação Prática

### 3.1 Padrão Exemplo: Pytest com Database Efêmero (Python)

Este modelo exemplifica o uso correto de fixtures efêmeras de banco de dados para evitar vazamento de dados entre execuções parciais:

```python
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from myapp.database import Base
from myapp.models import User

# Cria banco SQLite em memória totalmente limpo p/ a suite
DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(engine):
    """Garante isolamento: cada teste roda sob uma transação limpa que é revertida (rollback)."""
    connection = engine.connect()
    transaction = connection.begin()
    
    Session = sessionmaker(bind=connection)
    session = Session()
    
    yield session
    
    session.close()
    transaction.rollback()
    connection.close()

# Teste unitário/integração usando a fixture
def test_create_user_stores_properly(db_session):
    # Setup
    new_user = User(name="William", email="will@kelvem.com")
    db_session.add(new_user)
    db_session.commit()
    
    # Act
    retrieved = db_session.query(User).filter_by(email="will@kelvem.com").first()
    
    # Assert
    assert retrieved is not None
    assert retrieved.name == "William"
    assert retrieved.id is not None  # Garante autoincremento do DB real em memória
```

---

## 📈 4. Critério Estrito de Cobertura e "Regra de Ouro"

> 🎯 **Regra de Ouro de Qualidade**: 
> Um teste automatizado só demonstra sua eficácia real quando **falha** antes da aplicação do patch estrutural, e passa a **dar sucesso** (Pass) imediatamente após a injeção do patch correto.

### O Teste de Mutação (Mutation Testing)
Surgimento de novos testes pode ser avaliado sob a técnica de testes de mutação. Se mudarmos um operador lógico simples no código de `>` para `>=` e nenhum teste quebrar, a suíte de testes correspondente é considerada cega sobre essa variável lógica, expondo uma fresta de cobertura real sob manipulações de fronteira de entrada.
*   Ferramenta sugerida para Python: `mutmut`
*   Ferramenta sugerida para JavaScript/TS: `Stryker Mutator`


