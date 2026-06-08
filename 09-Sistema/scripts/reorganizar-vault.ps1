<#
.SYNOPSIS
Reorganiza fisicamente as pastas do Will-obsidian com segurança.

.DESCRIPTION
Este script move pastas e alguns arquivos raiz para uma estrutura mais organizada.
Por padrão ele roda em modo simulação, sem mover nada.

Uso recomendado:
1. Abrir PowerShell na raiz do repositório Will-obsidian.
2. Rodar primeiro em simulação:
   .\09-Sistema\scripts\reorganizar-vault.ps1
3. Conferir o plano exibido.
4. Rodar a migração real:
   .\09-Sistema\scripts\reorganizar-vault.ps1 -Aplicar

IMPORTANTE:
- Faça backup antes de aplicar.
- Confira `git status` antes e depois.
- O script não apaga conteúdo automaticamente.
#>

param(
    [switch]$Aplicar
)

$ErrorActionPreference = "Stop"

function Escrever-Titulo($texto) {
    Write-Host ""
    Write-Host "=== $texto ===" -ForegroundColor Cyan
}

function Criar-Diretorio($caminho) {
    if (-not (Test-Path $caminho)) {
        if ($Aplicar) {
            New-Item -ItemType Directory -Path $caminho -Force | Out-Null
            Write-Host "Criado: $caminho" -ForegroundColor Green
        } else {
            Write-Host "[simulação] Criaria: $caminho" -ForegroundColor DarkYellow
        }
    }
}

function Mover-ItemSeguro($origem, $destino) {
    if (-not (Test-Path $origem)) {
        Write-Host "Ignorado, não existe: $origem" -ForegroundColor DarkGray
        return
    }

    if (Test-Path $destino) {
        Write-Host "Destino já existe, revisar manualmente: $destino" -ForegroundColor Yellow
        return
    }

    $pastaDestino = Split-Path $destino -Parent
    Criar-Diretorio $pastaDestino

    if ($Aplicar) {
        Move-Item -Path $origem -Destination $destino
        Write-Host "Movido: $origem -> $destino" -ForegroundColor Green
    } else {
        Write-Host "[simulação] Moveria: $origem -> $destino" -ForegroundColor DarkYellow
    }
}

Escrever-Titulo "Reorganização do Will-obsidian"

if ($Aplicar) {
    Write-Host "Modo: APLICAR mudanças reais" -ForegroundColor Red
} else {
    Write-Host "Modo: SIMULAÇÃO. Nada será movido." -ForegroundColor Yellow
}

Escrever-Titulo "Criando pastas finais"

$pastasFinais = @(
    "00-Inbox",
    "01-Hubs",
    "02-JARVIS",
    "03-Projetos",
    "04-Conhecimentos",
    "05-Skills",
    "06-Will-Pessoal",
    "07-Operacoes-do-Vault",
    "08-Arquivo",
    "09-Sistema",
    "09-Sistema\agents",
    "09-Sistema\benchmarks",
    "09-Sistema\config",
    "09-Sistema\schema",
    "09-Sistema\scripts",
    "09-Sistema\simuladores",
    "09-Sistema\tests",
    "10-Interfaces",
    "10-Interfaces\Canvases",
    "10-Interfaces\dashboards",
    "10-Interfaces\web-ui",
    "11-Dados-Brutos",
    "99-Templates"
)

foreach ($pasta in $pastasFinais) {
    Criar-Diretorio $pasta
}

Escrever-Titulo "Movendo pastas principais"

$movimentosPastas = @(
    @{ Origem = "Bases"; Destino = "11-Dados-Brutos\Bases" },
    @{ Origem = "benchmarks"; Destino = "09-Sistema\benchmarks" },
    @{ Origem = "Canvases"; Destino = "10-Interfaces\Canvases" },
    @{ Origem = "Clippings"; Destino = "11-Dados-Brutos\Clippings" },
    @{ Origem = "Conhecimento-Geral"; Destino = "04-Conhecimentos\07-Humanidades" },
    @{ Origem = "Conhecimentos-Gerais"; Destino = "04-Conhecimentos\Conhecimentos-Gerais" },
    @{ Origem = "dashboards"; Destino = "10-Interfaces\dashboards" },
    @{ Origem = "flashcards"; Destino = "04-Conhecimentos\06-Estudos-e-Aprendizagem\flashcards" },
    @{ Origem = "Ideias"; Destino = "00-Inbox\Ideias" },
    @{ Origem = "JARVIS"; Destino = "02-JARVIS\JARVIS" },
    @{ Origem = "Knowledge-Base"; Destino = "04-Conhecimentos\Knowledge-Base" },
    @{ Origem = "Projetos"; Destino = "03-Projetos\Projetos" },
    @{ Origem = "raw"; Destino = "11-Dados-Brutos\raw" },
    @{ Origem = "schema"; Destino = "09-Sistema\schema" },
    @{ Origem = "scripts"; Destino = "09-Sistema\scripts\legado" },
    @{ Origem = "simuladores"; Destino = "09-Sistema\simuladores" },
    @{ Origem = "skills"; Destino = "05-Skills\skills" },
    @{ Origem = "Templates"; Destino = "99-Templates\Legado" },
    @{ Origem = "tests"; Destino = "09-Sistema\tests" },
    @{ Origem = "web-ui"; Destino = "10-Interfaces\web-ui" },
    @{ Origem = "wiki"; Destino = "04-Conhecimentos\wiki" },
    @{ Origem = "Will-Pessoal"; Destino = "06-Will-Pessoal\Will-Pessoal" }
)

foreach ($mov in $movimentosPastas) {
    Mover-ItemSeguro $mov.Origem $mov.Destino
}

Escrever-Titulo "Movendo arquivos raiz selecionados"

$movimentosArquivos = @(
    @{ Origem = "Painel-Cockpit.md"; Destino = "10-Interfaces\Painel-Cockpit.md" },
    @{ Origem = "Projetos.md"; Destino = "03-Projetos\Projetos.md" },
    @{ Origem = "AGENTS.md"; Destino = "09-Sistema\agents\AGENTS.md" },
    @{ Origem = "CLAUDE.md"; Destino = "09-Sistema\agents\CLAUDE.md" },
    @{ Origem = "GEMINI.md"; Destino = "09-Sistema\agents\GEMINI.md" },
    @{ Origem = "CLI-BOOTSTRAP.md"; Destino = "09-Sistema\CLI-BOOTSTRAP.md" },
    @{ Origem = "claude_desktop_config.json"; Destino = "09-Sistema\config\claude_desktop_config.json" },
    @{ Origem = "indexer_config.json"; Destino = "09-Sistema\config\indexer_config.json" }
)

foreach ($mov in $movimentosArquivos) {
    Mover-ItemSeguro $mov.Origem $mov.Destino
}

Escrever-Titulo "Itens preservados na raiz"

$preservados = @(
    "Bem-vindo.md",
    "README.md",
    "INDEX.md",
    ".env.example",
    ".gitignore",
    ".mcp.json",
    ".pre-commit-config.yaml",
    "gitleaks.toml",
    "requirements.in",
    "requirements.txt",
    "requirements-locked.txt",
    "skills-lock.json",
    "start-web-ui.bat",
    ".git",
    ".github",
    ".obsidian",
    ".cursor",
    ".continue",
    ".openclaude",
    ".agents"
)

foreach ($item in $preservados) {
    Write-Host "Preservar na raiz: $item" -ForegroundColor DarkGray
}

Escrever-Titulo "Finalização"

if ($Aplicar) {
    Write-Host "Migração aplicada. Agora rode: git status" -ForegroundColor Green
    Write-Host "Depois abra o Obsidian e revise links/hubs." -ForegroundColor Green
} else {
    Write-Host "Simulação concluída. Nenhum arquivo foi movido." -ForegroundColor Yellow
    Write-Host "Para aplicar: .\09-Sistema\scripts\reorganizar-vault.ps1 -Aplicar" -ForegroundColor Yellow
}
