---
tags: [skills, devops, cicd, semantic-release, versionamento]
updated: 2026-06-08
title: "Semantic Release"
date: 2026-06-01
---

# Semantic Release

Guia sobre automacao de versionamento semantico, geracao de changelog e publicacao de releases usando conventional commits e ferramentas como semantic-release.

## Introducao

Semantic Release automatiza todo o fluxo de versionamento de software:
1. Analisa commits desde a ultima release
2. Determina o tipo de bump (major, minor, patch)
3. Gera changelog automaticamente
4. Cria uma Git tag e GitHub Release
5. Publica pacotes em registries (npm, PyPI, Docker)

### Semver (Semantic Versioning)

```
MAJOR.MINOR.PATCH
   |      |      |
   |      |      +-- Patch: bug fixes (backward compatible)
   |      +--------- Minor: new features (backward compatible)
   +---------------- Major: breaking changes (incompatible)
```

```python
# Exemplo de versionamento semantico
from semver import Version

v = Version(major=1, minor=2, minor=3)
# v.major = 1
# v.minor = 2
# v.patch = 3

# Bump
v_major = v.bump_major()   # 2.0.0
v_minor = v.bump_minor()   # 1.3.0
v_patch = v.bump_patch()   # 1.2.4

# Pre-release
v_rc = Version(2, 0, 0, prerelease="rc.1")  # 2.0.0-rc.1
v_beta = Version(2, 0, 0, prerelease="beta.1")  # 2.0.0-beta.1

# Comparacao
v1 = Version.parse("1.0.0")
v2 = Version.parse("2.0.0")
print(v1 < v2)  # True
```

## Conventional Commits

### Estrutura

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### Tipos

| Tipo | Descricao | Bump |
|------|-----------|------|
| `fix` | Correcao de bug | PATCH |
| `feat` | Nova funcionalidade | MINOR |
| `BREAKING CHANGE` | Mudanca incompativel | MAJOR |
| `build` | Mudancas no build | No release |
| `chore` | Tarefas rotineiras | No release |
| `ci` | Mudancas em CI/CD | No release |
| `docs` | Documentacao | No release |
| `perf` | Melhoria de performance | No release |
| `refactor` | Refatoracao | No release |
| `style` | Estilo de codigo | No release |
| `test` | Testes | No release |

### Exemplos

```
feat: adiciona autenticacao por biometria

Implementa verificacao de impressao digital para login mobile.
A autenticacao usa a API nativa do dispositivo.

Closes #123

---

feat(api): adiciona endpoint de health check

GET /health retorna status do servico e dependencias.

---

fix(auth): corrige timeout na renovacao de token

O token expirava antes do refresh ser concluido,
causando erro 401 em requisicoes concorrentes.

Fixes #456

---

feat: implementa cache Redis

BREAKING CHANGE: A interface de cache foi alterada.
Agora e necessario inicializar o cache com `CacheManager.setup(config)`.

Migration guide:
  Antes: `cache.get(key)`
  Depois: `CacheManager.get(key)`

---

docs: atualiza README com instrucoes de deploy
```

### Validacao com commitlint

```javascript
// commitlint.config.js
module.exports = {
  extends: ["@commitlint/config-conventional"],
  rules: {
    "type-enum": [
      2,
      "always",
      [
        "feat",
        "fix",
        "docs",
        "style",
        "refactor",
        "perf",
        "test",
        "build",
        "ci",
        "chore",
        "revert",
      ],
    ],
    "scope-case": [2, "always", "kebab-case"],
    "subject-case": [0], // Disable subject case rule
    "subject-max-length": [2, "always", 100],
  },
};
```

```bash
# Instalar commitlint
npm install --save-dev @commitlint/{cli,config-conventional}

# Husky hook
npx husky add .husky/commit-msg 'npx --no -- commitlint --edit "$1"'
```

## Configuracao do Semantic Release

### Instalacao

```bash
# Node.js (recomendado)
npm install --save-dev semantic-release @semantic-release/{git,changelog,github,npm}

# Python (alternativa)
pip install python-semantic-release
```

### Configuracao

```javascript
// release.config.js (ou .releaserc.json)
module.exports = {
  branches: [
    "+([0-9])?(.{+([0-9]),x}).x",
    "main",
    "next",
    { name: "beta", prerelease: true },
    { name: "alpha", prerelease: true },
  ],
  repositoryUrl: "https://github.com/will/myproject",
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        releaseRules: [
          { type: "refactor", release: "patch" },
          { type: "style", release: "patch" },
          { type: "perf", release: "patch" },
          { breaking: true, release: "major" },
        ],
        parserOpts: {
          noteKeywords: ["BREAKING CHANGE", "BREAKING"],
        },
      },
    ],
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
        presetConfig: {
          types: [
            { type: "feat", section: "Features", hidden: false },
            { type: "fix", section: "Bug Fixes", hidden: false },
            { type: "perf", section: "Performance", hidden: false },
            { type: "docs", section: "Documentation", hidden: true },
            { type: "chore", section: "Miscellaneous", hidden: true },
          ],
        },
      },
    ],
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG.md",
        changelogTitle: "# Changelog\n\nAll notable changes to this project.",
      },
    ],
    "@semantic-release/npm",
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG.md",
          "package.json",
          "package-lock.json",
        ],
        message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
      },
    ],
    [
      "@semantic-release/github",
      {
        assets: [
          { path: "dist/*.tar.gz", label: "Source (${nextRelease.version})" },
        ],
      },
    ],
  ],
};
```

### Para Projetos Python

```toml
# pyproject.toml
[tool.semantic_release]
version_variable = "src/myapp/__init__.py:__version__"
version_toml = "pyproject.toml:project.version"
branch = "main"
build_command = "python -m build"
changelog_file = "CHANGELOG.md"

[tool.semantic_release.commit_parser_options]
allowed_tags = ["fix", "feat", "docs", "style", "refactor", "perf", "test", "build", "ci", "chore"]
minor_tag = "feat"
patch_tag = "fix"
major_tags = ["BREAKING CHANGE"]

[tool.semantic_release.git]
assets = ["CHANGELOG.md", "pyproject.toml", "src/myapp/__init__.py"]
commit_message = "chore(release): {version}\n\nAutomated release."

[tool.semantic_release.remote]
name = "origin"
token_type = "gh-token"
```

## Workflow GitHub Actions

### Semantic Release Workflow

```yaml
name: Release
on:
  push:
    branches:
      - main
      - next
      - beta
      - alpha

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: write
      pull-requests: write
      packages: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          persist-credentials: false

      - uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install dependencies
        run: npm ci

      - name: Build
        run: npm run build

      - name: Semantic Release
        uses: cycjimmy/semantic-release-action@v4
        with:
          branch: main
          extra_plugins: |
            @semantic-release/git
            @semantic-release/changelog
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          NPM_TOKEN: ${{ secrets.NPM_TOKEN }}
```

### Python Semantic Release Workflow

```yaml
name: Python Release
on:
  push:
    branches: [main]

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install semantic-release
        run: pip install python-semantic-release

      - name: Run semantic release
        run: semantic-release publish
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          REPOSITORY_URL: https://github.com/${{ github.repository }}
```

## CHANGELOG Generation

### Exemplo de Changelog

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [2.1.0] - 2026-05-16

### Features
- **api**: Adiciona endpoint de health check com dependencias
- **auth**: Implementa autenticacao biometrica para mobile
- **cache**: Adiciona suporte a Redis como cache secundario

### Bug Fixes
- **auth**: Corrige timeout na renovacao de token (#456)
- **api**: Corrige encoding de caracteres especiais em respostas
- **database**: Corrige conexao pool esgotada em alta concorrencia

### Performance
- Otimiza query de busca de usuarios com indexacao
- Reduz tamanho de pacotes de assets estaticos

## [2.0.0] - 2026-04-20

### Breaking Changes
- **cache**: Interface de cache alterada. Migration guide abaixo.

### Features
- Implementa arquitetura baseada em eventos
- Adiciona suporte a WebSockets para notificacoes em tempo real

## [1.3.2] - 2026-03-15

### Bug Fixes
- Corrige vazamento de memoria em conexoes WebSocket
```

## Automated Version Bump

```python
# Script para versionamento manual (fallback)
import re
from pathlib import Path

class VersionBumper:
    def __init__(self, version_file: str):
        self.version_file = Path(version_file)

    def read_version(self) -> str:
        content = self.version_file.read_text()
        match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
        if not match:
            raise ValueError("Versao nao encontrada")
        return match.group(1)

    def write_version(self, new_version: str):
        content = self.version_file.read_text()
        content = re.sub(
            r'__version__\s*=\s*["\']([^"\']+)["\']',
            f'__version__ = "{new_version}"',
            content
        )
        self.version_file.write_text(content)

    def bump(self, part: str) -> str:
        current = self.read_version()
        major, minor, patch = map(int, current.split("."))

        if part == "major":
            new_version = f"{major + 1}.0.0"
        elif part == "minor":
            new_version = f"{major}.{minor + 1}.0"
        elif part == "patch":
            new_version = f"{major}.{minor}.{patch + 1}"
        else:
            raise ValueError(f"Parte invalida: {part}")

        self.write_version(new_version)
        return new_version

# Uso
bumper = VersionBumper("src/myapp/__init__.py")
print(f"Versao atual: {bumper.read_version()}")
print(f"Nova versao: {bumper.bump('minor')}")
```

## Multi-Branch Strategy

```yaml
# Estrategia de branches para releases
branches_config = {
    "main": "Stable releases (latest)",
    "next": "Next major version (pre-release)",
    "beta": "Beta features (pre-release)",
    "alpha": "Alpha features (pre-release)",
    "1.x": "Maintenance releases for v1",
}

# Fluxo
# feature/ -> develop (pre-release)
# develop -> main (stable)
# main -> tag vX.Y.Z (release)
# main -> 1.x (backport)
```

### Configuracao Multi-Branch

```javascript
// .releaserc.json
{
  "branches": [
    { "name": "main" },
    { "name": "next", "channel": "next", "prerelease": true },
    { "name": "beta", "channel": "beta", "prerelease": "beta" },
    { "name": "alpha", "channel": "alpha", "prerelease": "alpha" },
    { "name": "1.x", "range": "1.x", "channel": "1.x" }
  ]
}
```

## Comparacao de Ferramentas

| Ferramenta | Linguagem | Vantagens | Desvantagens |
|------------|-----------|-----------|--------------|
| semantic-release | Node.js | Mais popular, muitos plugins | Requer Node.js runtime |
| python-semantic-release | Python | Nativo Python, pyproject.toml | Menos plugins |
| go-semantic-release | Go | Rapido, binario unico | Comunidade menor |
| standard-version | Node.js | Simples, sem CI requirement | Manual |

## Melhores Praticas

```python
BEST_PRACTICES = {
    "Commit Messages": [
        "Usar sempre conventional commits",
        "Mensagens curtas e descritivas",
        "Incluir referencias a issues (#123)",
        "Usar escopos para modulos (feat(api):)"
    ],
    "Branches": [
        "Manter main sempre deployavel",
        "Usar branches de pre-release (beta, alpha)",
        "Proteger branches de release com rules",
        "Nunca fazer commit direto em main"
    ],
    "CI/CD": [
        "Executar semantic-release apenas em branches de release",
        "Configurar permissions corretas (contents: write)",
        "Usar fetch-depth: 0 para analise de commits",
        "Testar antes de liberar release"
    ],
    "Versioning": [
        "Seguir semver estritamente",
        "Documentar breaking changes claramente",
        "Manter changelog automatizado",
        "Incluir migration guides para breaking changes"
    ]
}
```

## Referencias Cruzadas

- [[ci-cd/INDEX]] - Index de CI/CD
- [[ci-cd/github-actions]] - GitHub Actions workflow
- [[ci-cd/environment-promotion]] - Promocao entre ambientes
- [[devops/FinOps]] - Otimizacao de custos
- [[02-software-engineering/seguranca/supply-chain-security]] - Seguranca em pipelines