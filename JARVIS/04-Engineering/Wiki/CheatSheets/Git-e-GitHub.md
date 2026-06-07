---
title: "Git e GitHub — Cheat Sheet"
description: "Guia de referência rápida para Git e GitHub — comandos, workflows e boas práticas"
tags: [cheatsheet, git, github, versionamento, jarvis-engenharia]
updated: 2026-06-07
date: 2026-05-16
---

# Git e GitHub — Cheat Sheet

Referência completa de comandos Git, GitHub CLI e estratégias de branching para o dia a dia.

---

## 📋 Sumário

- [⚙️ Configuração Inicial](#-configuração-inicial)
- [📦 Repositórios](#-repositórios)
- [📝 Commits](#-commits)
- [🌿 Branches](#-branches)
- [🔀 Merge / Rebase / Squash](#-merge--rebase--squash)
- [📤 Push / Pull / Fetch](#-push--pull--fetch)
- [🧊 Stash](#-stash)
- [🏷️ Tags](#-tags)
- [🔍 Log e Reflog](#-log-e-reflog)
- [🎯 Bisect](#-bisect)
- [🍒 Cherry-Pick](#-cherry-pick)
- [🔧 GitHub CLI (gh)](#-github-cli-gh)
- [📄 .gitignore](#-gitignore)
- [📜 Convenções de Commit](#-convenções-de-commit)
- [🔀 Estratégias de Branching](#-estratégias-de-branching)
- [🔗 Pull Requests e Templates](#-pull-requests-e-templates)
- [🐛 Troubleshooting](#-troubleshooting)
- [🔗 Relacionados](#-relacionados)

---

## ⚙️ Configuração Inicial

```bash
# Identidade
git config --global user.name "Seu Nome"
git config --global user.email "seu@email.com"

# Editor padrão
git config --global core.editor "code --wait"

# Linha de comando
git config --global core.autocrlf input  # Linux/Mac
git config --global core.autocrlf true   # Windows

# Aliases úteis
git config --global alias.lg "log --oneline --graph --all --decorate"
git config --global alias.s "status -sb"
git config --global alias.df "diff"
git config --global alias.dfc "diff --cached"
git config --global alias.undo "reset --soft HEAD~1"
git config --global alias.amend "commit --amend --no-edit"

# Hub (GitHub CLI)
gh auth login
gh config set editor code
```

---

## 📦 Repositórios

```bash
# Criar novo repositório
git init
git init nome-do-projeto

# Clonar
git clone https://github.com/usuario/repo.git
git clone git@github.com:usuario/repo.git  # SSH
git clone --depth 1 https://github.com/usuario/repo.git  # Shallow clone
git clone --branch develop https://github.com/usuario/repo.git

# Verificar origem
git remote -v
git remote add origin https://github.com/usuario/repo.git
git remote set-url origin git@github.com:usuario/repo.git
git remote remove origin

# Fork (via gh)
gh repo fork
gh repo clone usuario/repo
```

---

## 📝 Commits

```bash
# Adicionar ao stage
git add arquivo.py
git add src/                        # Adiciona diretório
git add .                           # Adiciona tudo
git add -p                          # Adiciona interativamente (patch mode)

# Commitar
git commit -m "mensagem"
git commit -am "add e commit em um passo"  # Só para arquivos tracked
git commit --amend                  # Altera último commit
git commit --amend --no-edit        # Altera sem editar mensagem
git commit --allow-empty -m "trigger CI"

# Verificar status
git status
git status -sb                      # Formato curto
```

---

## 🌿 Branches

```bash
# Listar
git branch                          # Locais
git branch -r                       # Remotas
git branch -a                       # Todas

# Criar
git branch feature/login
git checkout -b feature/login       # Cria e muda

# Trocar
git checkout main
git switch main                     # Novo comando (Git 2.23+)
git switch -c feature/login         # Cria e troca

# Deletar
git branch -d feature/login         # Local (segura)
git branch -D feature/login         # Local (forçado)
git push origin --delete feature/login  # Remota

# Renomear
git branch -m old-name new-name

# Sincronizar branches remotas
git fetch --prune                   # Remove refs órfãs locais
git branch -vv                      # Ver relação local/remota
```

---

## 🔀 Merge / Rebase / Squash

### Merge

```bash
# Merge padrão (cria commit de merge)
git checkout main
git merge feature/login

# Merge com fast-forward (se possível)
git merge --ff feature/login

# Merge sem fast-forward (força commit de merge)
git merge --no-ff feature/login

# Squash merge (junta tudo em um commit)
git merge --squash feature/login
git commit -m "feat: adiciona login"
```

### Rebase

```bash
# Rebase simples
git checkout feature/login
git rebase main

# Rebase interativo
git rebase -i HEAD~3                # Últimos 3 commits
git rebase -i main                  # Desde o fork com main

# Comandos no rebase -i:
# pick    = mantém commit como está
# reword  = altera mensagem
# squash  = combina com anterior
# fixup   = combina e descarta mensagem
# drop    = remove commit
# edit    = pausa para editar

# Continuar/pular/abortar
git rebase --continue
git rebase --skip
git rebase --abort

# Atualizar feature branch (evita merge commits)
git checkout feature
git rebase main
git push --force-with-lease
```

### Comparação

| Operação  | Resultado                  | Histórico            | Quando usar                        |
|-----------|----------------------------|----------------------|-----------------------------------|
| merge     | Commit de merge            | Preserva ramificação | Feature compartilhada             |
| rebase    | Histórico linear           | Reescreve commits    | Feature local / antes do push     |
| squash    | Único commit               | Compacta histórico   | Feature pequena / cleanup         |

---

## 📤 Push / Pull / Fetch

```bash
# Push
git push origin main
git push -u origin feature/login  # Seta upstream
git push --force-with-lease       # Força seguro (preferir)
git push --force                  # Força bruto (perigoso!)
git push --tags                   # Envia tags

# Pull
git pull origin main
git pull --rebase                 # Pull com rebase (evita merge commit)
git pull --ff-only                # Só faz fast-forward

# Fetch
git fetch origin                  # Busca alterações sem aplicar
git fetch --prune                 # Fetch + limpa refs órfãs
git fetch origin pull/123/head:pr-123  # Busca PR específico

# Configurar pull com rebase por padrão
git config --global pull.rebase true
```

---

## 🧊 Stash

```bash
# Salvar trabalho temporário
git stash
git stash push -m "trabalho em progresso"

# Listar stashes
git stash list
git stash list --oneline

# Aplicar stash
git stash apply                    # Aplica sem remover
git stash pop                      # Aplica e remove
git stash pop stash@{1}            # Aplica stash específico

# Remover stash
git stash drop                     # Remove o último
git stash clear                    # Remove todos

# Criar branch a partir de stash
git stash branch fix-bug stash@{0}
```

---

## 🏷️ Tags

```bash
# Listar
git tag
git tag -l "v1.*"

# Criar
git tag v1.0.0                     # Lightweight
git tag -a v1.0.0 -m "Release 1.0.0"  # Anotada

# Push tags
git push origin v1.0.0
git push origin --tags

# Deletar
git tag -d v1.0.0                  # Local
git push origin --delete v1.0.0   # Remota

# Checkout tag
git checkout v1.0.0                # Estado detached HEAD
git checkout -b release-1.0 v1.0.0  # Criar branch da tag
```

---

## 🔍 Log e Reflog

```bash
# Log básico
git log
git log --oneline
git log --oneline --graph --all --decorate

# Log avançado
git log --since="2 weeks ago"
git log --author="William"
git log --grep="fix:"              # Busca na mensagem
git log -p                         # Mostra diff
git log --stat                     # Estatísticas
git log --follow arquivo.py        # Histórico incluindo renomeios

# Log de um arquivo
git log -p arquivo.py
git blame arquivo.py
git annotate arquivo.py

# Reflog (todas as ações locais)
git reflog
git reflog --relative-date
git reflog show HEAD@{2.days.ago}

# Recuperar com reflog
git reset HEAD@{1}                 # Volta para estado anterior
git checkout HEAD@{2}              # Acessa commit perdido
```

---

## 🎯 Bisect

```bash
# Iniciar busca binária
git bisect start
git bisect bad                     # Commit atual está quebrado
git bisect good v1.0.0             # Tag onde funcionava

# Testar cada commit
git bisect good                    # Se funcionar
git bisect bad                     # Se estiver quebrado

# Automático (com script de teste)
git bisect run npm test

# Encerrar
git bisect reset

# Exemplo completo
git bisect start HEAD v1.0.0
git bisect run python -m pytest tests/test_login.py
git bisect reset
```

---

## 🍒 Cherry-Pick

```bash
# Aplicar commit específico em outra branch
git checkout main
git cherry-pick abc1234

# Cherry-pick múltiplos commits
git cherry-pick abc1234 def5678

# Cherry-pick sem commitar
git cherry-pick -n abc1234

# Cherry-pick range
git cherry-pick main..feature     # Todos da feature após o fork
```

---

## 🔧 GitHub CLI (gh)

```bash
# Autenticação
gh auth login
gh auth status

# Repositórios
gh repo create myapp --public --clone
gh repo fork
gh repo view usuario/repo

# Issues
gh issue list
gh issue create --title "Bug" --body "Descrição"
gh issue view 123
gh issue close 123

# Pull Requests
gh pr list
gh pr create --base main --head feature --title "Nova feature" --body "Descrição"
gh pr view 456
gh pr checkout 456
gh pr review 456 --approve
gh pr merge 456 --squash

# CI/CD
gh run list
gh run watch
gh run rerun 789

# Gists
gh gist create arquivo.py
gh gist list

# Atalhos comuns
gh pr create -f                    # Cria PR com template
gh pr checks --watch               # Acompanha checks
gh release create v1.0.0 --generate-notes
```

---

## 📄 .gitignore

```gitignore
# Dependências
node_modules/
vendor/
.python-version
__pycache__/
*.pyc
.venv/
.env/

# Build
dist/
build/
*.tsbuildinfo
.next/
*.log

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# Sistema
.DS_Store
Thumbs.db
*.exe

# Secrets (NUNCA versionar)
.env
.env.local
*.key
*.pem

# Framework-specific
# Django
*.sqlite3
media/

# React Native
ios/Pods/
*.jks
*.keystore

# Terraform
*.tfstate
*.tfstate.*
.terraform/

# Docker
.dockerignore  # mas adicione os padrões lá também
```

---

## 📜 Convenções de Commit

### Conventional Commits

```
<tipo>(<escopo opcional>): <descrição>

<corpo opcional>

<rodapé opcional>
```

### Tipos

| Tipo       | Uso                                    |
|-----------|----------------------------------------|
| feat      | Nova funcionalidade                    |
| fix       | Correção de bug                        |
| docs      | Documentação                           |
| style     | Formatação (sem mudança lógica)       |
| refactor  | Refatoração (sem feature nem bugfix)  |
| test      | Adiciona/Corrige testes               |
| chore     | Tarefas de build, CI, dependências    |
| perf      | Melhoria de performance               |
| ci        | Configuração de CI/CD                |

### Exemplos

```
feat(auth): adiciona login com Google OAuth
fix(api): corrige validação de email no cadastro
docs: atualiza README com instruções de setup
refactor: extrai lógica de pagamento para serviço
test: adiciona testes unitários para UserService
BREAKING CHANGE: altera estrutura da API de /v1 para /v2
```

---

## 🔀 Estratégias de Branching

### Feature Branch

```bash
# Mais simples — cada feature em branch separada
git checkout -b feat/user-profile
# ... trabalho ...
git checkout main
git merge feat/user-profile
git push origin main
```

### Git Flow

```bash
# Branchs fixas: main, develop, feature/*, release/*, hotfix/*
git checkout -b feature/login develop
# ... desenvolvimento ...
git checkout develop
git merge feature/login

# Release
git checkout -b release/1.2.0 develop
# ... ajustes finais ...
git checkout main
git merge release/1.2.0
git tag v1.2.0
git checkout develop
git merge release/1.2.0

# Hotfix
git checkout -b hotfix/1.2.1 main
# ... corrige ...
git checkout main
git merge hotfix/1.2.1
git tag v1.2.1
git checkout develop
git merge hotfix/1.2.1
```

### Trunk-Based

```bash
# Branches curtas (< 1 dia), merge direto na main
git checkout -b feat-123
# ... pequena mudança ...
git checkout main
git pull --rebase
git merge --ff-only feat-123
git push origin main

# Feature flags para código incompleto
# if feature_flag_enabled("new_checkout"):
#     return new_checkout()
```

---

## 🔗 Pull Requests e Templates

### Template de PR (.github/PULL_REQUEST_TEMPLATE.md)

```markdown
## Descrição

<!-- Resumo claro e conciso do que foi feito -->

## Tipo de mudança

- [ ] feat: nova funcionalidade
- [ ] fix: correção de bug
- [ ] refactor: refatoração
- [ ] test: testes
- [ ] docs: documentação
- [ ] chore: manutenção

## Como testar

1. `npm run dev`
2. Acesse `/login`
3. Faça login com...

## Check-List

- [ ] Testes passam localmente
- [ ] Adicionei testes para cobrir a mudança
- [ ] Documentação foi atualizada
- [ ] Sem breaking changes não documentadas

## Screenshots

<!-- se aplicável -->

## Closes

Closes #123
```

---

## 🐛 Troubleshooting

### Issue: Detached HEAD

```bash
# Causa: você fez checkout de um commit/tag, não de uma branch
# Sintoma: "You are in 'detached HEAD' state"

# Solução 1: criar branch para salvar alterações
git switch -c temp-branch

# Solução 2: voltar para branch existente (perde alterações não commitadas)
git checkout main
```

### Issue: Conflito de Merge

```bash
# Sinais: <<<<<<<, =======, >>>>>>> no código

# Resolver manualmente:
# 1. Edite os arquivos conflitantes
# 2. git add <arquivos>
# 3. git commit

# Ou usar ferramenta visual
git mergetool  # Configurar: git config merge.tool vscode

# Abortar merge
git merge --abort

# Resolver aceitando um lado
git checkout --ours arquivo.py     # Mantém sua versão
git checkout --theirs arquivo.py   # Mantém versão deles
git add arquivo.py
git merge --continue
```

### Issue: Push rejeitado (divergência)

```bash
# Causa: branch remota avançou desde seu último pull

# Opção 1: rebase (histórico limpo)
git fetch origin
git rebase origin/main
git push --force-with-lease

# Opção 2: merge (preserva histórico)
git pull origin main
git push origin main

# NUNCA use --force em branches compartilhadas sem avisar o time
```

### Issue: Commit no branch errado

```bash
# Remove do branch atual e aplica no correto
git log --oneline -1               # Acha o hash
git reset HEAD~1 --soft            # Desfaz commit, mantém alterações
git stash                          # Guarda alterações
git checkout branch-correto
git stash pop
git add .
git commit -m "feat: no branch certo"

# Ou cherry-pick e reset
git cherry-pick abc1234            # Aplica no branch certo
git checkout branch-errado
git reset --hard HEAD~1            # Remove de lá
```

### Issue: Esqueceu de adicionar algo no último commit

```bash
git add -- arquivo-esquecido.py
git commit --amend --no-edit
```

### Issue: Force push acidental

```bash
# Recuperar usando reflog
git reflog
# Encontre o hash do commit antes do force push
git checkout -b recovery abc1234
git push origin recovery
# Agora crie um PR para restaurar
```

### Issue: Arquivo sensível commitado (.env, chaves)

```bash
# Remover do histórico (reescreve!)
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# Ou usar BFG Repo-Cleaner (mais rápido):
# java -jar bfg.jar --delete-files .env repo.git

# Depois do push:
# 1. Rolar chaves comprometidas
# 2. git push --force --all
# 3. Avisar o time
```

### Issue: Erro de permissão (SSH)

```bash
# Verificar chaves
ssh -T git@github.com

# Erro: "Permission denied (publickey)"
# Solução: adicionar chave ao ssh-agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Ou usar HTTPS com token
git remote set-url origin https://USERNAME:TOKEN@github.com/usuario/repo.git
```

---

## 🔗 Relacionados

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com)
- [[skills/02-software-engineering|Software Engineering Skills]]
- [[JARVIS/04-Engineering/Playbooks/Debug/Git-Merge-Conflict|Merge Conflict Playbook]]
- [[JARVIS/04-Engineering/Wiki/CheatSheets/Docker|Docker Cheat Sheet]]

[[JARVIS/README|← Voltar ao Command Center]]
