# Will Vault - Obsidian Neural Hub

Este repositorio e o vault principal do Obsidian do Will. A estrutura numerada abaixo e a fonte canonica para navegacao, conhecimento, projetos, JARVIS, skills, vida pessoal, operacoes do vault, sistema tecnico, dados brutos e templates.

Para navegar, comece por:

- [[Bem-vindo|Neural Hub]]
- [[INDEX|INDEX global]]
- [[01-Hubs/README|Hubs Centrais do Vault]]
- [[07-Operacoes-do-Vault/README|Operacoes do Vault]]

## Estrutura fisica canonica

```txt
Will-obsidian/
├── 00-Inbox/              <- Entrada e triagem
├── 01-Hubs/               <- Navegacao superior e mapas
├── 02-JARVIS/             <- Identidade, memoria, arquitetura e playbooks
├── 03-Projetos/           <- Projetos ativos, estudo, documentos e arquivo de projeto
├── 04-Conhecimentos/      <- Conhecimento curado e wiki de dominio
├── 05-Skills/             <- Skills, capacidades e indices por dominio
├── 06-Will-Pessoal/       <- Contexto pessoal, rotina e informacoes sensiveis
├── 07-Operacoes-do-Vault/ <- Inventarios, migracao, auditoria e manutencao
├── 08-Arquivo/            <- Legado preservado e notas fora do fluxo ativo
├── 09-Sistema/            <- Regras, schemas, scripts e integracoes tecnicas
├── 11-Dados-Brutos/       <- Fontes, bases e clippings sem curadoria
└── 99-Templates/          <- Modelos reutilizaveis
```

## Papel de cada area

| Area | Papel |
|---|---|
| `00-Inbox/` | ponto de entrada para capturas, ideias e triagem inicial |
| `01-Hubs/` | camada superior de navegacao, dashboards e mapas |
| `02-JARVIS/` | nucleo operacional de IA: memoria, identidade, arquitetura e aprendizado |
| `03-Projetos/` | projetos por status, plano, suporte e historico |
| `04-Conhecimentos/` | conhecimento estavel organizado por dominio |
| `05-Skills/` | habilidades tecnicas, workflows e capacidades reutilizaveis |
| `06-Will-Pessoal/` | contexto pessoal, rotina, saude e informacoes sensiveis |
| `07-Operacoes-do-Vault/` | inventarios, status, migracao, auditoria e saude do vault |
| `08-Arquivo/` | legado preservado sem apagar historico |
| `09-Sistema/` | schema, agentes, scripts, validacoes e governanca tecnica |
| `11-Dados-Brutos/` | dados brutos, fontes originais e materiais ainda nao curados |
| `99-Templates/` | modelos canonicos para notas, projetos e operacao |

## Sistema tecnico

Os arquivos tecnicos do vault vivem em `09-Sistema/` e seguem a separacao:

- `11-Dados-Brutos/` para evidencia e fontes;
- `04-Conhecimentos/` para sintese e conhecimento curado;
- `09-Sistema/schema/` para regras, contratos e governanca;
- `09-Sistema/agents/` para instrucoes operacionais de modelos e agentes;
- `09-Sistema/scripts/` para automacoes e suporte tecnico.

## Governanca e migracao

A migracao fisica e a organizacao do vault sao acompanhadas por:

- [[07-Operacoes-do-Vault/README]]
- [[07-Operacoes-do-Vault/Reestruturacao-Geral-do-Vault]]
- [[07-Operacoes-do-Vault/Inventario-Inicial-do-Vault]]
- [[07-Operacoes-do-Vault/Mapa-de-Migracao-Fisica-do-Vault]]
- [[07-Operacoes-do-Vault/Status-da-Migracao-Fisica]]

## Regras rapidas

- preserve o legado em `08-Arquivo/` enquanto existirem links antigos;
- prefira um unico hub por dominio;
- mantenha metadados em notas centrais;
- nao misture dado bruto com sintese;
- nao mova em massa sem validar links e hubs.

## Como abrir

```bash
git clone https://github.com/William-kelvem94/Will-obsidian.git
cd Will-obsidian
pip install -r requirements.txt
```

Depois, abra a pasta no Obsidian.
