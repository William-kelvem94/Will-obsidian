---
title: "Workflows Práticos do Jarvis"
description: "Exemplos práticos de workflows, integrações e casos de uso reais implementados."
tags:
  - jarvis
  - jarvis-engenharia
  - workflows
  - praticos
  - exemplos
  - implementacao
updated: 2026-06-05
date: 2026-04-27
---

# Workflows Práticos do Jarvis

Este documento contém workflows práticos e implementações reais que o Jarvis pode executar, servindo como referência para treinamento e expansão do segundo cérebro.

## 1. Workflow: Desenvolvimento de Feature Completa

### Cenário
Usuário pede: "Jarvis, preciso implementar autenticação JWT no backend"

### Execução Passo a Passo

```python
# 1. ANÁLISE E PLANEJAMENTO
async def analisar_requisito(requisito: str):
    """Jarvis analisa o requisito e gera plano"""
    
    # Buscar conhecimento relevante
    contexto = await rag.buscar(requisito)
    
    # Gerar plano com LLM
    plano = await llm.completar([
        {"role": "system", "content": SYSTEM_PROMPTS["tecnico"]},
        {"role": "user", "content": f"""
            Com base neste contexto: {contexto}
            
            Gere um plano detalhado para: {requisito}
            
            Inclua:
            - Dependências necessárias
            - Arquivos a criar/modificar
            - Testes necessários
            - Possíveis riscos
        """}
    ])
    
    return plano

# 2. IMPLEMENTAÇÃO GUIADA
async def implementar_feature(plano: dict):
    """Executa implementação passo a passo"""
    
    for passo in plano["passos"]:
        # Mostrar passo atual
        await notificar_usuario(f"Executando: {passo['descricao']}")
        
        # Executar ação
        if passo["tipo"] == "instalar_dependencia":
            await executar_comando(f"pip install {passo['pacote']}")
        
        elif passo["tipo"] == "criar_arquivo":
            codigo = await gerar_codigo(passo["especificacao"])
            await criar_arquivo(passo["caminho"], codigo)
        
        elif passo["tipo"] == "modificar_arquivo":
            mudancas = await gerar_mudancas(passo["especificacao"])
            await aplicar_mudancas(passo["caminho"], mudancas)
        
        # Aguardar confirmação
        confirmacao = await perguntar_usuario("Continuar?")
        if not confirmacao:
            break

# 3. VALIDAÇÃO AUTOMÁTICA
async def validar_implementacao():
    """Valida código gerado"""
    
    resultados = {
        "lint": await executar_comando("ruff check ."),
        "type_check": await executar_comando("mypy ."),
        "testes": await executar_comando("pytest"),
        "security": await executar_comando("bandit -r .")
    }
    
    # Analisar resultados
    problemas = []
    for check, resultado in resultados.items():
        if resultado["exit_code"] != 0:
            problemas.append({
                "tipo": check,
                "detalhes": resultado["output"]
            })
    
    if problemas:
        # Corrigir automaticamente se possível
        for problema in problemas:
            correcao = await sugerir_correcao(problema)
            await aplicar_correcao(correcao)
    
    return len(problemas) == 0
```

### Exemplo Real: Implementação JWT

```python
# 1. Jarvis analisa e planeja
plano = {
    "feature": "Autenticação JWT",
    "passos": [
        {
            "ordem": 1,
            "descricao": "Instalar dependências",
            "tipo": "instalar_dependencia",
            "pacotes": ["python-jose[cryptography]", "passlib[bcrypt]"]
        },
        {
            "ordem": 2,
            "descricao": "Criar schemas Pydantic",
            "tipo": "criar_arquivo",
            "caminho": "app/models/auth.py",
            "conteudo": """
from pydantic import BaseModel, EmailStr

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None
    disabled: bool = False

class UserInDB(User):
    hashed_password: str
            """
        },
        {
            "ordem": 3,
            "descricao": "Implementar utilidades de segurança",
            "tipo": "criar_arquivo",
            "caminho": "app/core/security.py",
            "conteudo": """
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha_plana: str, senha_hash: str) -> bool:
    return pwd_context.verify(senha_plana, senha_hash)

def gerar_hash_senha(senha: str) -> str:
    return pwd_context.hash(senha)

def criar_token_acesso(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode,
        settings.SECRET_KEY,
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt
            """
        },
        # ... mais passos
    ],
    "testes": [
        "test_login_correto",
        "test_login_senha_incorreta",
        "test_token_expirado",
        "test_acesso_rota_protegida"
    ],
    "tempo_estimado": "4-6 horas",
    "riscos": [
        "Gerenciamento de secrets em produção",
        "Implementar refresh tokens",
        "Rate limiting no endpoint de login"
    ]
}

# 2. Jarvis executa implementação
await implementar_feature(plano)

# 3. Jarvis valida
validacao = await validar_implementacao()

# 4. Jarvis documenta
await criar_memoria_episodica({
    "titulo": "Implementação de Autenticação JWT",
    "data": "2026-04-17",
    "decisoes": [
        "Usar bcrypt para hashing de senhas",
        "Tokens com validade de 30 minutos",
        "Refresh tokens armazenados em Redis"
    ],
    "aprendizados": [
        "Rate limiting essencial para /token",
        "Testes de segurança evitaram 2 vulnerabilidades"
    ],
    "referencias": [
        "JARVIS/KnowledgeBase/Conhecimento.md",
        "JARVIS/KnowledgeBase/Arquitetura.md"
    ]
})
```

## 2. Workflow: Debugging Inteligente

### Cenário
Usuário: "Jarvis, o endpoint /users está retornando 500"

### Execução

```python
async def debug_endpoint(endpoint: str, status_code: int):
    """Debugging inteligente de API"""
    
    # 1. Coletar informações
    info = {
        "logs": await buscar_logs(endpoint, limit=50),
        "metricas": await buscar_metricas(endpoint),
        "codigo": await ler_codigo_endpoint(endpoint),
        "testes": await executar_testes(endpoint)
    }
    
    # 2. Analisar com LLM
    analise = await llm.completar([
        {"role": "system", "content": """
            Você é um especialista em debugging.
            Analise logs, métricas e código para identificar a causa.
        """},
        {"role": "user", "content": f"""
            Endpoint: {endpoint}
            Status: {status_code}
            
            Logs:
            {info['logs']}
            
            Código:
            {info['codigo']}
            
            Identifique:
            1. Causa raiz do erro
            2. Linha exata com problema
            3. Correção sugerida
            4. Prevenção futura
        """}
    ])
    
    # 3. Aplicar correção se aprovada
    if await confirmar_usuario(f"Aplicar correção: {analise['correcao']}?"):
        await aplicar_mudanca(
            arquivo=analise['arquivo'],
            linha=analise['linha'],
            correcao=analise['correcao']
        )
        
        # 4. Validar correção
        testes = await executar_testes(endpoint)
        if testes["sucesso"]:
            await notificar("✅ Erro corrigido e validado!")
        else:
            await notificar("⚠️ Correção aplicada mas testes falharam")
    
    return analise
```

## 3. Workflow: Interação Multimodal

### Cenário
Jarvis detecta frustração do usuário via câmera e ajusta comportamento

```python
class MultimodalInteraction:
    def __init__(self):
        self.perception = PerceptionManager()
        self.llm = LocalLLM()
        self.tts = PiperTTS()
    
    async def loop_interacao(self):
        """Loop principal de interação multimodal"""
        
        while True:
            # 1. Perceber ambiente
            snapshot = await self.perception.get_snapshot()
            
            # 2. Analisar contexto emocional
            contexto_emocional = self.analisar_emocao(snapshot)
            
            # 3. Aguardar comando
            comando = await self.aguardar_comando()
            
            if comando:
                # 4. Ajustar tom baseado em emoção
                tom = self.determinar_tom(contexto_emocional)
                
                # 5. Gerar resposta contextual
                resposta = await self.llm.completar([
                    {
                        "role": "system",
                        "content": f"""
                            Você é Jarvis. O usuário está {contexto_emocional['emocao']}.
                            Use tom {tom}. Contexto: {snapshot}
                        """
                    },
                    {"role": "user", "content": comando}
                ])
                
                # 6. Responder (voz + texto)
                await self.responder(resposta, tom)
    
    def analisar_emocao(self, snapshot: dict) -> dict:
        """Analisa estado emocional do usuário"""
        emocao = snapshot.get("emocao", "neutro")
        confianca = snapshot.get("confianca_emocao", 0.0)
        
        # Mapear para estratégia de resposta
        estrategias = {
            "frustrado": {
                "tom": "direto_empatico",
                "estilo": "objetivo e prático",
                "acoes": ["oferecer ajuda específica", "simplificar explicação"]
            },
            "feliz": {
                "tom": "entusiasta",
                "estilo": "descontraído e encorajador",
                "acoes": ["celebrar progresso", "sugerir próximo desafio"]
            },
            "confuso": {
                "tom": "didatico",
                "estilo": "passo a passo com exemplos",
                "acoes": ["quebrar em partes menores", "usar analogias"]
            }
        }
        
        return {
            "emocao": emocao,
            "confianca": confianca,
            "estrategia": estrategias.get(emocao, estrategias["feliz"])
        }
    
    def determinar_tom(self, contexto: dict) -> str:
        """Determina tom apropriado baseado no contexto"""
        return contexto["estrategia"]["tom"]
    
    async def responder(self, resposta: str, tom: str):
        """Envia resposta multimodal"""
        # Texto na UI
        await self.ui.mostrar_mensagem(resposta)
        
        # Voz com tom apropriado
        audio = await self.tts.sintetizar(resposta)
        await self.reproduzir_audio(audio)
        
        # Gesture visual (opcional)
        if tom == "entusiasta":
            await self.ui.mostrar_animacao("thumbs_up")
```

## 4. Workflow: Aprendizado Contínuo

### Jarvis aprende com interações e atualiza KB

```python
class ContinuousLearning:
    async def processar_interacao(self, interacao: dict):
        """Processa interação e extrai aprendizados"""
        
        # 1. Identificar se houve algo novo
        novidade = await self.detectar_novidade(interacao)
        
        if novidade:
            # 2. Extrair conhecimento
            conhecimento = await self.extrair_conhecimento(interacao)
            
            # 3. Validar com usuário
            if await self.confirmar_com_usuario(conhecimento):
                # 4. Atualizar KB
                await self.atualizar_knowledge_base(conhecimento)
                
                # 5. Reindexar RAG
                await self.rag.reindexar()
    
    async def detectar_novidade(self, interacao: dict) -> bool:
        """Detecta se interação contém informação nova"""
        
        # Buscar no RAG existente
        similar = await self.rag.buscar(interacao["conteudo"])
        
        # Se não encontrar similar, é novidade
        return len(similar) == 0 or similar[0]["score"] > 0.5
    
    async def extrair_conhecimento(self, interacao: dict) -> dict:
        """Extrai conhecimento estruturado da interação"""
        
        conhecimento = await self.llm.completar([
            {"role": "system", "content": """
                Extraia conhecimento estruturado desta interação.
                Formato:
                - Conceito principal
                - Categoria (técnico/processo/pessoal)
                - Detalhes importantes
                - Exemplos
                - Referências
            """},
            {"role": "user", "content": str(interacao)}
        ])
        
        return conhecimento
    
    async def atualizar_knowledge_base(self, conhecimento: dict):
        """Atualiza arquivos do Knowledge Base"""
        
        categoria = conhecimento["categoria"]
        arquivo_map = {
            "tecnico": "Conhecimento.md",
            "processo": "Workflows-Praticos.md",
            "pessoal": "Sobre-Will/Preferencias.md"
        }
        
        arquivo = arquivo_map[categoria]
        caminho = f"JARVIS/KnowledgeBase/{arquivo}"
        
        # Adicionar ao final do arquivo
        novo_conteudo = self.formatar_conhecimento(conhecimento)
        await self.append_arquivo(caminho, novo_conteudo)
        
        # Criar memória episódica
        await self.criar_memoria_episodica({
            "titulo": f"Aprendizado: {conhecimento['conceito']}",
            "data": datetime.now().isoformat(),
            "tipo": "aprendizado",
            "conteudo": conhecimento
        })
```

## 5. Workflow: Integração com Desenvolvimento Real

### Jarvis assiste em coding session real

```python
class DevAssistant:
    async def coding_session(self):
        """Sessão de programação assistida"""
        
        # 1. Monitor de arquivos
        watcher = FileWatcher("./src")
        
        async for evento in watcher:
            if evento["tipo"] == "modificacao":
                # 2. Analisar mudança
                analise = await self.analisar_mudanca(evento)
                
                # 3. Sugestões proativas
                if analise["complexidade"] > 0.7:
                    await self.sugerir(
                        "Esta função está ficando complexa. "
                        "Considere refatorar em funções menores?"
                    )
                
                if analise["falta_testes"]:
                    await self.sugerir(
                        "Gerar testes para esta função?",
                        acao=lambda: self.gerar_testes(evento["arquivo"])
                    )
                
                if analise["problemas_seguranca"]:
                    await self.alertar(
                        f"⚠️ Possível problema de segurança: "
                        f"{analise['problemas_seguranca']}"
                    )
            
            elif evento["tipo"] == "erro_execucao":
                # 4. Debug automático
                await self.debug_automatico(evento["erro"])
    
    async def analisar_mudanca(self, evento: dict) -> dict:
        """Analisa código modificado"""
        codigo = await self.ler_arquivo(evento["arquivo"])
        
        # Análise estática
        complexidade = self.calcular_complexidade(codigo)
        testes = self.verificar_testes(evento["arquivo"])
        seguranca = await self.verificar_seguranca(codigo)
        
        return {
            "complexidade": complexidade,
            "falta_testes": not testes,
            "problemas_seguranca": seguranca
        }
```

## Resumo

Este documento será continuamente atualizado com novos workflows práticos conforme o Jarvis evolui. Cada workflow demonstra:

1. **Entrada**: O que dispara o workflow
2. **Processamento**: Como Jarvis analisa e decide
3. **Ação**: O que Jarvis executa
4. **Validação**: Como verifica sucesso
5. **Aprendizado**: O que registra para o futuro

Estes padrões servem como referência para:
- Treinar o modelo de IA em comportamentos desejados
- Documentar capacidades existentes
- Planejar novas funcionalidades
- Manter consistência nas interações

[[JARVIS/README|← Voltar ao Command Center]]
