---
title: Auditoria de commits GitHub
type: dados-brutos-github
status: atual
updated: 2026-08-23
classe_privacidade: operacional
indexavel: true
uso_ia: permitido
---

# Auditoria de commits

Coleta realizada em 23/08/2026. A busca autenticada retornou amostras recentes por repositório. O conector não fornece contagem histórica total diretamente; portanto, a quantidade abaixo é **amostra retornada**, não total de commits.

## 1. William-kelvem94/ada_v2---jarvis

- **Registros retornados:** 1
- **Amostra:**
  - `97aa1f4b46513f4423dd979ef8c585a3ba020b66` — Initial commit — data não informada
\n## 2. William-kelvem94/ADB_Android-s_Will

- **Registros retornados:** 6
- **Amostra:**
  - `b0d6aea2a2a92c394c4cbad54f919a894be7596c` — fix: torna coleta de identidade ADB resiliente durante operações de IA

Corrige a falha de atualização do painel observada enquanto o runtime de IA é extraído/enviado ao Android.

Detalhes:
- deixa de depender exclusivamente do lote adb_bundle para propriedades de identidade;
- coleta modelo, fabricante, Android, patch, fingerprint e build em chamadas ADB independentes;
- tolera falhas transitórias em propriedades individuais sem derrubar toda a telemetria;
- usa os metadados de `adb devices -l` como fallback para o modelo quando necessário;
- preserva as demais leituras de bateria, memória, CPU e temperatura;
- mantém histórico e cache do dispositivo funcionando normalmente;
- aplica a correção no ponto de inicialização compartilhado por Windows, Linux e Docker.

A alteração evita o erro `Propriedades ADB indisponíveis: model, manufacturer, android, security_patch, fingerprint, build` durante carga concorrente de ADB, como instalação do llama.cpp e transferência de modelos. — data não informada\n  - `3b206d402fecea601092ce9ea9227f1d9232be39` — feat: adiciona build Docker automático para Windows e Linux

Adiciona inicializadores de build e subida automática do Android Hub via Docker Compose, mantendo o fluxo alinhado com a versão 1.3.0 e com o novo gerenciador de IA local.

Principais mudanças:
- cria BUILD-DOCKER.cmd para execução com duplo clique no Windows;
- cria BUILD-DOCKER.sh executável para Linux;
- valida se Docker está instalado e acessível antes de iniciar;
- valida disponibilidade do Docker Compose v2;
- cria o diretório runtime quando necessário;
- executa docker compose build --pull para reconstruir a imagem com as bases atualizadas;
- executa docker compose up -d --remove-orphans sem remover volumes persistentes;
- aguarda o endpoint /api/health responder antes de declarar sucesso;
- exibe os últimos logs do serviço quando build, inicialização ou healthcheck falham;
- mostra o estado final dos containers com docker compose ps;
- abre automaticamente o painel no Windows e tenta abrir via xdg-open no Linux;
- preserva os dados persistidos em runtime e não utiliza down -v ou qualquer operação destrutiva de volume.

Com isso, o projeto passa a ter fluxo de build Docker de um clique no Windows e equivalente direto no Linux. — data não informada\n  - `2b8d826461f8d8ea87b2c812d0e4396ea08e3f42` — feat: evolui Android Hub com IA local e suporte nativo multiplataforma

Adiciona um gerenciador de IA local integrado ao Android Hub para instalar, monitorar e controlar o llama.cpp diretamente no Android via ADB, com suporte inicial ao Qwen2.5-Coder 7B Q4_K_M e API compatível com OpenAI/OpenCode.

Principais mudanças:
- cria a nova tela IA Local com instalação de runtime e modelo, início/parada do servidor, logs, teste de prompt e configuração do OpenCode;
- monitora RAM, memória disponível, swap/ZRAM, PSI, GPU, temperatura e processo do llama-server em tempo real;
- valida origem HTTPS, tamanho e SHA-256 conhecido do GGUF antes do envio ao aparelho;
- mantém confirmação explícita e registro de auditoria para operações que alteram o Android;
- utiliza backend CPU por padrão e não anuncia OpenCL/Adreno antes de validação real no dispositivo;
- corrige o módulo Diagnóstico, que existia na navegação mas não era aberto corretamente pelo fluxo principal;
- corrige a navegação responsiva para não esconder módulos em telas pequenas;
- remove o flash inicial de métricas demonstrativas antes da primeira telemetria ADB real;
- ajusta a ação Desconectar para Pausar/Retomar monitoramento, refletindo o comportamento verdadeiro da função;
- corrige a identificação do modo Linux nativo no frontend;
- adiciona descoberta automática do ADB e execução nativa de primeira classe no Windows e Linux;
- adiciona inicializadores dedicados para Windows e Linux;
- atualiza a imagem Docker para incluir o gerenciador de IA e o diretório persistente de runtime;
- adiciona GitHub Actions com validação de sintaxe Python, JavaScript, scripts Linux e execução dos testes;
- adiciona testes estáticos do catálogo e das rotas do gerenciador de IA;
- atualiza o README para a versão 1.3.0 com arquitetura, execução multiplataforma, API e fluxo de IA;
- registra a auditoria técnica de 20/08/2026 com problemas encontrados, correções e limitações ainda dependentes de teste físico.

Validações realizadas antes do commit:
- compilação de sintaxe dos módulos Python;
- node --check no frontend JavaScript;
- bash -n nos inicializadores Linux;
- testes do gerenciador de IA aprovados;
- revisão dos contratos entre frontend e endpoints de IA.

A aceleração Adreno/OpenCL permanece propositalmente desabilitada até existir validação prática de um binário Android confiável. — data não informada\n  - `da8ea2eb4973b985c12dd6a647c71675e40c3755` — feat: moderniza o Android Hub com segurança e atualização em tempo real — data não informada\n  - `08ab69ce516e545d9c785d2da1a93e9e4a96a12c` — feat: consolidar Android Hub e catálogo técnico ADB

Implementa backend FastAPI com telemetria, histórico local por dispositivo, catálogo pesquisável, diagnósticos seguros e cache de leituras ADB.

Adiciona interface web, execução via Docker, scripts de smoke test e validação determinística das fichas técnicas.

Integra 1.234 modelos das seis marcas ativas e protege dados de runtime, serial do aparelho, ferramentas baixadas e materiais de referência por meio do .gitignore. — data não informada\n  - `28fa6dfc74d2eadda1ff186f77df21e1e51eae4e` — Initial commit — data não informada
\n## 3. William-kelvem94/AFFiNE-Will

- **Registros retornados:** 100
- **Amostra:**
  - `5b9d51b41b2f513ec8611e454dc2a70b2ff0379a` — chore: bump up RevenueCat/purchases-ios-spm version to from: "5.75.0" (#15048)

This PR contains the following updates:

| Package | Update | Change |
|---|---|---|
|
[RevenueCat/purchases-ios-spm](https://redirect.github.com/RevenueCat/purchases-ios-spm)
| minor | `from: "5.74.0"` → `from: "5.75.0"` |

---

### Release Notes

<details>
<summary>RevenueCat/purchases-ios-spm
(RevenueCat/purchases-ios-spm)</summary>

###
[`v5.75.0`](https://redirect.github.com/RevenueCat/purchases-ios-spm/compare/5.74.0...5.75.0)

[Compare
Source](https://redirect.github.com/RevenueCat/purchases-ios-spm/compare/5.74.0...5.75.0)

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4yMDIuMSIsInVwZGF0ZWRJblZlciI6IjQzLjIwMi4xIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `18471ef9b221689e9874514d6aac2000142f2eb0` — chore: bump up oxlint version to v1.67.0 (#15047)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [oxlint](https://oxc.rs/docs/guide/usage/linter)
([source](https://redirect.github.com/oxc-project/oxc/tree/HEAD/npm/oxlint))
| [`1.66.0` →
`1.67.0`](https://renovatebot.com/diffs/npm/oxlint/1.66.0/1.67.0) |
![age](https://developer.mend.io/api/mc/badges/age/npm/oxlint/1.67.0?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/oxlint/1.66.0/1.67.0?slim=true)
|

---

### Release Notes

<details>
<summary>oxc-project/oxc (oxlint)</summary>

###
[`v1.67.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1670---2026-05-26)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.66.0...oxlint_v1.67.0)

##### 🚀 Features

-
[`b84941e`](https://redirect.github.com/oxc-project/oxc/commit/b84941e)
linter/vue: Implement no-expose-after-await rule
([#&#8203;22675](https://redirect.github.com/oxc-project/oxc/issues/22675))
(bab)
-
[`98b98c1`](https://redirect.github.com/oxc-project/oxc/commit/98b98c1)
linter/vue: Implement no-computed-properties-in-data rule
([#&#8203;22674](https://redirect.github.com/oxc-project/oxc/issues/22674))
(bab)
-
[`2d4c919`](https://redirect.github.com/oxc-project/oxc/commit/2d4c919)
oxlint: Support `vite-plus/resolveConfig` for vite.config.ts
([#&#8203;22456](https://redirect.github.com/oxc-project/oxc/issues/22456))
(leaysgur)
-
[`2a60012`](https://redirect.github.com/oxc-project/oxc/commit/2a60012)
linter/vue: Implement require-render-return rule
([#&#8203;22613](https://redirect.github.com/oxc-project/oxc/issues/22613))
(bab)
-
[`9f227fd`](https://redirect.github.com/oxc-project/oxc/commit/9f227fd)
linter/vue: Implement no-deprecated-props-default-this rule
([#&#8203;21892](https://redirect.github.com/oxc-project/oxc/issues/21892))
(bab)
-
[`87f065e`](https://redirect.github.com/oxc-project/oxc/commit/87f065e)
linter/vue: Implement return-in-emits-validator rule
([#&#8203;21935](https://redirect.github.com/oxc-project/oxc/issues/21935))
(bab)
-
[`ea0380c`](https://redirect.github.com/oxc-project/oxc/commit/ea0380c)
linter/unicorn: Implement `import-style` rule
([#&#8203;22173](https://redirect.github.com/oxc-project/oxc/issues/22173))
(Hao Chen)
-
[`dde40fe`](https://redirect.github.com/oxc-project/oxc/commit/dde40fe)
linter/vue: Implement no-watch-after-await rule
([#&#8203;22006](https://redirect.github.com/oxc-project/oxc/issues/22006))
(bab)
-
[`a735eb0`](https://redirect.github.com/oxc-project/oxc/commit/a735eb0)
linter/vue: Implement valid-next-tick rule
([#&#8203;22531](https://redirect.github.com/oxc-project/oxc/issues/22531))
(bab)
-
[`6dc615d`](https://redirect.github.com/oxc-project/oxc/commit/6dc615d)
linter/vue: Implement no-shared-component-data rule
([#&#8203;21842](https://redirect.github.com/oxc-project/oxc/issues/21842))
(bab)
-
[`a656418`](https://redirect.github.com/oxc-project/oxc/commit/a656418)
linter/vue: Implement valid-define-options rule
([#&#8203;22107](https://redirect.github.com/oxc-project/oxc/issues/22107))
(bab)
-
[`bb6f1b2`](https://redirect.github.com/oxc-project/oxc/commit/bb6f1b2)
linter/vue: Implement require-slots-as-functions rule
([#&#8203;22244](https://redirect.github.com/oxc-project/oxc/issues/22244))
(bab)
-
[`5fa4774`](https://redirect.github.com/oxc-project/oxc/commit/5fa4774)
linter/n: Implement `callback-return` rule
([#&#8203;22470](https://redirect.github.com/oxc-project/oxc/issues/22470))
(Mikhail Baev)

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4yMDIuMSIsInVwZGF0ZWRJblZlciI6IjQzLjIwMi4xIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `7a575a4a5b3db1ddcb8157be62ae4c1e5f841558` — fix: hide experimental settings for doc and folder icons (#15021)

should fix #13955
The emoji doc and folder icons have been officially released with v0.25
but the experimental settings were still available with no effect if
switched.

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->

## Summary by CodeRabbit

* **Chores**
* Feature flags for emoji folder and document icons are no longer
user-configurable.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15021?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `f5fc7c8c003dc7b07e42ad17055161afbcfbf148` — chore: bump up eslint-plugin-oxlint version to v1.67.0 (#15036)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
|
[eslint-plugin-oxlint](https://redirect.github.com/oxc-project/eslint-plugin-oxlint)
| [`1.66.0` →
`1.67.0`](https://renovatebot.com/diffs/npm/eslint-plugin-oxlint/1.66.0/1.67.0)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/eslint-plugin-oxlint/1.67.0?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/eslint-plugin-oxlint/1.66.0/1.67.0?slim=true)
|

---

### Release Notes

<details>
<summary>oxc-project/eslint-plugin-oxlint
(eslint-plugin-oxlint)</summary>

###
[`v1.67.0`](https://redirect.github.com/oxc-project/eslint-plugin-oxlint/releases/tag/v1.67.0)

[Compare
Source](https://redirect.github.com/oxc-project/eslint-plugin-oxlint/compare/v1.66.0...v1.67.0)

*No significant changes*

#####     [View changes on
GitHub](https://redirect.github.com/oxc-project/eslint-plugin-oxlint/compare/v1.66.0...v1.67.0)

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `7d3e38d65263ebf35ed22040fb59d1b3f43990c4` — chore: bump up nestjs (#15035)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [@nestjs-cls/transactional](https://papooch.github.io/nestjs-cls/)
([source](https://redirect.github.com/Papooch/nestjs-cls)) | [`3.2.0` →
`3.2.1`](https://renovatebot.com/diffs/npm/@nestjs-cls%2ftransactional/3.2.0/3.2.1)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs-cls%2ftransactional/3.2.1?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs-cls%2ftransactional/3.2.0/3.2.1?slim=true)
|
|
[@nestjs-cls/transactional-adapter-prisma](https://papooch.github.io/nestjs-cls/)
([source](https://redirect.github.com/Papooch/nestjs-cls)) | [`1.3.4` →
`1.3.5`](https://renovatebot.com/diffs/npm/@nestjs-cls%2ftransactional-adapter-prisma/1.3.4/1.3.5)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs-cls%2ftransactional-adapter-prisma/1.3.5?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs-cls%2ftransactional-adapter-prisma/1.3.4/1.3.5?slim=true)
|
| [@nestjs/common](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/common))
| [`11.1.23` →
`11.1.24`](https://renovatebot.com/diffs/npm/@nestjs%2fcommon/11.1.23/11.1.24)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fcommon/11.1.24?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fcommon/11.1.23/11.1.24?slim=true)
|
| [@nestjs/core](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/core))
| [`11.1.23` →
`11.1.24`](https://renovatebot.com/diffs/npm/@nestjs%2fcore/11.1.23/11.1.24)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fcore/11.1.24?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fcore/11.1.23/11.1.24?slim=true)
|
| [@nestjs/platform-express](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/platform-express))
| [`11.1.23` →
`11.1.24`](https://renovatebot.com/diffs/npm/@nestjs%2fplatform-express/11.1.23/11.1.24)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fplatform-express/11.1.24?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fplatform-express/11.1.23/11.1.24?slim=true)
|
| [@nestjs/platform-socket.io](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/platform-socket.io))
| [`11.1.23` →
`11.1.24`](https://renovatebot.com/diffs/npm/@nestjs%2fplatform-socket.io/11.1.23/11.1.24)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fplatform-socket.io/11.1.24?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fplatform-socket.io/11.1.23/11.1.24?slim=true)
|
| [@nestjs/websockets](https://redirect.github.com/nestjs/nest)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/websockets))
| [`11.1.23` →
`11.1.24`](https://renovatebot.com/diffs/npm/@nestjs%2fwebsockets/11.1.23/11.1.24)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fwebsockets/11.1.24?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fwebsockets/11.1.23/11.1.24?slim=true)
|

---

### Release Notes

<details>
<summary>Papooch/nestjs-cls (@&#8203;nestjs-cls/transactional)</summary>

###
[`v3.2.1`](https://redirect.github.com/Papooch/nestjs-cls/releases/tag/v3.2.1)

[Compare
Source](https://redirect.github.com/Papooch/nestjs-cls/compare/@nestjs-cls/transactional@3.2.0...@nestjs-cls/transactional@3.2.1)

- fix: `has` method respects falsy values
([#&#8203;57](https://redirect.github.com/Papooch/nestjs-cls/issues/57))
[`69f06e7`](https://redirect.github.com/Papooch/nestjs-cls/commit/69f06e7)

</details>

<details>
<summary>nestjs/nest (@&#8203;nestjs/common)</summary>

###
[`v11.1.24`](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

</details>

<details>
<summary>nestjs/nest (@&#8203;nestjs/core)</summary>

###
[`v11.1.24`](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

</details>

<details>
<summary>nestjs/nest (@&#8203;nestjs/platform-express)</summary>

###
[`v11.1.24`](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

</details>

<details>
<summary>nestjs/nest (@&#8203;nestjs/platform-socket.io)</summary>

###
[`v11.1.24`](https://redirect.github.com/nestjs/nest/releases/tag/v11.1.24)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.23...v11.1.24)

##### v11.1.24 (2026-05-25)

##### Bug fixes

- `core`
- [#&#8203;17009](https://redirect.github.com/nestjs/nest/pull/17009)
fix(core): reset dependency-tree cache on metadata changes
([@&#8203;puneetdixit200](https://redirect.github.com/puneetdixit200))

##### Enhancements

- `core`
- [#&#8203;16997](https://redirect.github.com/nestjs/nest/pull/16997)
feat(core): warn on late websocket adapter registration
([@&#8203;hbinhng](https://redirect.github.com/hbinhng))

##### Dependencies

- `platform-ws`
- [#&#8203;17011](https://redirect.github.com/nestjs/nest/pull/17011)
chore(deps): bump ws from 8.20.1 to 8.21.0
([@&#8203;dependabot\[bot\]](https://redirect.github.com/apps/dependabot))

##### Committers: 2

- Nguyễn Hải Bình
([@&#8203;hbinhng](https://redirect.github.com/hbinhng))
- Puneet Dixit
([@&#8203;puneetdixit200](https://redirect.github.com/puneetdixit200))

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

👻 **Immortal**: This PR will be recreated if closed unmerged. Get
[config
help](https://redirect.github.com/renovatebot/renovate/discussions) if
that's undesired.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `b05c387f96fe629aab69bd0e7cb15c978684f3d1` — fix(server): mail test & retry (#15044)

#### PR Dependency Tree


* **PR #15044** 👈

This tree was auto-generated by
[Charcoal](https://github.com/danerwilliams/charcoal)

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->
## Summary by CodeRabbit

* **Bug Fixes**
* Stop sending notifications to disabled users; skip member invites when
workspace names contain URLs/domains
* Improve mail retry handling (per-recipient exhaustion, expiry, and
cache cleanup)
  * Make many email headers/lead lines more generic and consistent
  * Fail-safe workspace content parsing to avoid crashes

* **New Features**
* 24-hour signup protection for sharing, invites, and invite-link
creation
  * Job-queue: remove jobs by payload predicate

* **Tests**
* Expanded tests for mail jobs, SMTP hostname handling, payment
checkout, job-queue removal, and abuse-detection utilities
  * Updated test fixtures to set createdAt timestamps for new users

* **Chores**
  * Added required name input for test-email mutation
  * Database flush retry with deadlock detection/backoff

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15044?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `2bd920fea6dcbde56536c38145dcce2ddbf0151f` — chore: bump up @inquirer/prompts version to v8 (#15025)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
|
[@inquirer/prompts](https://redirect.github.com/SBoudrias/Inquirer.js/blob/main/packages/prompts/README.md)
([source](https://redirect.github.com/SBoudrias/Inquirer.js)) |
[`^7.10.1` →
`^8.0.0`](https://renovatebot.com/diffs/npm/@inquirer%2fprompts/7.10.1/8.5.0)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@inquirer%2fprompts/8.5.0?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@inquirer%2fprompts/7.10.1/8.5.0?slim=true)
|

---

### Release Notes

<details>
<summary>SBoudrias/Inquirer.js (@&#8203;inquirer/prompts)</summary>

###
[`v8.5.0`](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.4.3...5ca6d1101d5d3f8fb066cd5b389bccfdafbbe0c0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.4.3...@inquirer/prompts@8.5.0)

###
[`v8.4.3`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.4.3)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.4.2...@inquirer/prompts@8.4.3)

- Fix: Windows rendering bug
- Fix: Preserve exact literal types in `choices` array (Typescript only)
- Fix: Allow input `default` value to be of type `undefined` (Typescript
only)
- Bump dependencies

###
[`v8.4.2`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.4.2)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.4.1...@inquirer/prompts@8.4.2)

- Fix: some Windows terminals would freeze and not react to keypresses.

###
[`v8.4.1`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.4.1)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.4.0...@inquirer/prompts@8.4.1)

- Improve `expand` prompt type inferrence.

###
[`v8.4.0`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.4.0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.3.2...@inquirer/prompts@8.4.0)

- Feat: Added a loading message while validating editor prompt input.
- Type improvement: Better type inference with checkbox, search and
expand prompts.
- Fix: `editor` prompt not always properly handling editor path on
windows.

###
[`v8.3.2`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.3.2)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.3.1...@inquirer/prompts@8.3.2)

- Fix broken 8.3.1 release process.

###
[`v8.3.1`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.3.1)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.3.0...@inquirer/prompts@8.3.1)

- Bump dependencies

###
[`v8.3.0`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.3.0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.2.1...@inquirer/prompts@8.3.0)

- Fix: Keypresses happening before a prompt is rendered are now ignored.
- Fix (checkbox): Element who're both checked and disabled are now
always included in the returned array.
- Feat (select/checkbox): Cursor will now hover disabled options of the
list; but they still cannot be interacted with. This prevents the cursor
jumping ahead in ways that can be confusing.
- Feat: various new theme options to make all prompts content
localizable.

Finally, see our new [`@inquirer/i18n`
package](https://redirect.github.com/SBoudrias/Inquirer.js/tree/main/packages/i18n)!

###
[`v8.2.1`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.2.1)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.2.0...@inquirer/prompts@8.2.1)

- chore: Switch `wrap-ansi` with `fast-wrap-ansi`

###
[`v8.2.0`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.2.0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.1.0...@inquirer/prompts@8.2.0)

- feat(`search`): Add support for `default`.
- feat(`rawlist`): Add support for `description` of choices. That
information is displayed under the list when the choice is highlighted.
- Bump dependencies

###
[`v8.1.0`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.1.0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.0.2...@inquirer/prompts@8.1.0)

- Feat: `rawlist` now supports `default` option.
- Fix: `select` now infer return type properly when passing a `choices`
array of string literals.

###
[`v8.0.2`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.0.2)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.0.1...@inquirer/prompts@8.0.2)

- Fix Typescript not discovering types when `moduleResolution` is set to
`commonjs` (you probably want to fix that in your project if it's still
in your tsconfig)

###
[`v8.0.1`](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.0.0...@inquirer/prompts@8.0.1)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@8.0.0...@inquirer/prompts@8.0.1)

###
[`v8.0.0`](https://redirect.github.com/SBoudrias/Inquirer.js/releases/tag/%40inquirer/prompts%408.0.0)

[Compare
Source](https://redirect.github.com/SBoudrias/Inquirer.js/compare/@inquirer/prompts@7.10.1...@inquirer/prompts@8.0.0)

### Release Notes

#### 🚨 Breaking Changes

This is a major release that modernizes the codebase for Node.js ≥ 20.

##### ESM Only - No More CommonJS Support

**Impact:** All packages are now ESM-only. CommonJS imports are no
longer supported.

If you're on modern Node versions (≥ 20), this should be transparent and
have no impact.

##### Node.js Version Requirement

**Minimum Node.js version is now 20.x**

Node.js versions below 20 are no longer supported. Please upgrade to
Node.js 20 or later.

Node min versions: `>=23.5.0 || ^22.13.0 || ^21.7.0 || ^20.12.0`

##### Deprecated APIs Removed

The following deprecated APIs have been removed after being deprecated
in previous releases:

##### `list` prompt alias removed (affects `inquirer` package only)

The `list` alias has been removed from the `inquirer` package. This only
impacts users of the legacy `inquirer` package, not users of
`@inquirer/prompts` or individual prompt packages.

```js
// ❌ No longer available (inquirer package only)
import inquirer from 'inquirer';
const answer = await inquirer.prompt([
  { type: 'list', name: 'choice', message: 'Pick one:', choices: ['a', 'b'] }
]);

// ✅ Use 'select' instead
import inquirer from 'inquirer';
const answer = await inquirer.prompt([
  { type: 'select', name: 'choice', message: 'Pick one:', choices: ['a', 'b'] }
]);
```

##### `helpMode` theme property removed

```js
// ❌ No longer available
const answer = await select({
  theme: { helpMode: 'never' }
});

// ✅ Use theme.style.keysHelpTip instead
const answer = await select({
  theme: {
    style: {
      keysHelpTip: () => undefined // or your custom styling function
    }
  }
});
```

This affects the following prompts:

- `@inquirer/checkbox`
- `@inquirer/search`
- `@inquirer/select`

##### `instructions` config property removed

```js
// ❌ No longer available
const answer = await checkbox({
  instructions: 'Custom instructions'
});

// ✅ Use theme.style.keysHelpTip instead
const answer = await checkbox({
  theme: {
    style: {
      keysHelpTip: (text) => 'Custom instructions'
    }
  }
});
```

This affects the following prompts:

- `@inquirer/checkbox`
- `@inquirer/search`
- `@inquirer/select`

##### `cancel()` method removed

The `cancel()` method on prompt return custom `Promise` has been
removed.

```js
// ❌ No longer available
const answerPromise = input({ message: 'Name?' });
answerPromise.cancel();
const answer = await answerPromise;

// ✅ Use AbortSignal instead
const controller = new AbortController();
const answer = await input(
  { message: 'Name?' },
  { signal: controller.signal }
);
controller.abort();
```

##### Color Library Change: yoctocolors → Node.js `styleText`

**Internal change:** The project now uses Node.js built-in
`util.styleText()` instead of the `yoctocolors` package for terminal
colors. This makes Inquirer smaller and reduces risks of vulnerabilities
coming from transitive dependencies.

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `b3b9c54a89f94786b5f5b2f9b2888d4e8922d36a` — chore: bump up @types/nodemailer version to v8 (#15026)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
|
[@types/nodemailer](https://redirect.github.com/DefinitelyTyped/DefinitelyTyped/tree/master/types/nodemailer)
([source](https://redirect.github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/nodemailer))
| [`^7.0.0` →
`^8.0.0`](https://renovatebot.com/diffs/npm/@types%2fnodemailer/7.0.9/8.0.0)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@types%2fnodemailer/8.0.0?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@types%2fnodemailer/7.0.9/8.0.0?slim=true)
|

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `1d08e1d8c0feb40c631de8a8484669fc2fbdad70` — fix(server): dirty data handle (#15034)

#### PR Dependency Tree


* **PR #15034** 👈

This tree was auto-generated by
[Charcoal](https://github.com/danerwilliams/charcoal)

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->
## Summary by CodeRabbit

* **Refactor**
* Consolidated subscription visibility and “active” selection logic so
all subscription queries use a shared, consistent filter across the
platform.

* **Tests**
* Added a test to ensure expired subscriptions are excluded from active
subscription results.
* Updated test fixtures to differentiate expired, unexpired, and onetime
subscriptions for more accurate coverage.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15034?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `66a6a5fffc491dab1248754d5d17fab12a63c5fa` — feat(i18n): add missing zh-Hans translations (#15032)

## Summary

This PR completes the missing Simplified Chinese (`zh-Hans`) i18n
resource coverage.

The current i18n completeness calculation is based on key coverage
between `en.json` and each locale resource file. Before this change,
`zh-Hans.json` contained 2331 keys while `en.json` contained 2406 keys,
resulting in a displayed completeness of 97%.

This change adds the 75 missing `zh-Hans` translation entries and
updates the generated completeness value for `zh-Hans` from 97% to 100%.

## Changes

- Added 75 missing Simplified Chinese translations to
`packages/frontend/i18n/src/resources/zh-Hans.json`.
- Updated `packages/frontend/i18n/src/i18n-completenesses.json` so
`zh-Hans` now reports 100% completeness.
- Kept the scope limited to missing i18n resource keys only.

## Notes

This PR does not modify existing `zh-Hans` translations, terminology
choices, or hardcoded English UI strings outside the i18n resource
files.

## Verification

- Confirmed `zh-Hans.json` parses successfully.
- Confirmed `zh-Hans.json` now has full key coverage against `en.json`.
- Confirmed missing key count is 0.
- Confirmed computed `zh-Hans` completeness is 100%.
- Ran pre-commit checks:
  - `yarn lint-staged`
  - `yarn lint:ox`

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->

## Summary by CodeRabbit

* **Chores**
* Completed Chinese (Simplified) translations with 100% coverage for the
application.
* Added new translations across multiple areas: appearance and image
settings, export functionality, document import from Bear and Obsidian,
analytics and viewer information, editor settings including auto-date
titles and icon options, workspace sharing controls, calendar
integration with CalDAV support, share menu tooltips, and comprehensive
error messages.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15032?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `4f14e8840cd40a9e69095bb0209bcce9bd93f9ef` — chore: bump up RevenueCat/purchases-ios-spm version to from: "5.74.0" (#15024)

This PR contains the following updates:

| Package | Update | Change |
|---|---|---|
|
[RevenueCat/purchases-ios-spm](https://redirect.github.com/RevenueCat/purchases-ios-spm)
| minor | `from: "5.73.0"` → `from: "5.74.0"` |

---

### Release Notes

<details>
<summary>RevenueCat/purchases-ios-spm
(RevenueCat/purchases-ios-spm)</summary>

###
[`v5.74.0`](https://redirect.github.com/RevenueCat/purchases-ios-spm/compare/5.73.1...5.74.0)

[Compare
Source](https://redirect.github.com/RevenueCat/purchases-ios-spm/compare/5.73.1...5.74.0)

###
[`v5.73.1`](https://redirect.github.com/RevenueCat/purchases-ios-spm/blob/HEAD/CHANGELOG.md#5731)

[Compare
Source](https://redirect.github.com/RevenueCat/purchases-ios-spm/compare/5.73.0...5.73.1)

#### 5.73.1

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `95dd8d03bef8c3fa2b3557a1bdb4fc44d81b682f` — chore: bump up nestjs (#15023)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [@nestjs/apollo](https://redirect.github.com/nestjs/graphql) |
[`13.4.1` →
`13.4.2`](https://renovatebot.com/diffs/npm/@nestjs%2fapollo/13.4.1/13.4.2)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fapollo/13.4.2?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fapollo/13.4.1/13.4.2?slim=true)
|
| [@nestjs/common](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/common))
| [`11.1.21` →
`11.1.23`](https://renovatebot.com/diffs/npm/@nestjs%2fcommon/11.1.21/11.1.23)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fcommon/11.1.23?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fcommon/11.1.21/11.1.23?slim=true)
|
| [@nestjs/core](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/core))
| [`11.1.21` →
`11.1.23`](https://renovatebot.com/diffs/npm/@nestjs%2fcore/11.1.21/11.1.23)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fcore/11.1.23?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fcore/11.1.21/11.1.23?slim=true)
|
| [@nestjs/graphql](https://redirect.github.com/nestjs/graphql) |
[`13.4.1` →
`13.4.2`](https://renovatebot.com/diffs/npm/@nestjs%2fgraphql/13.4.1/13.4.2)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fgraphql/13.4.2?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fgraphql/13.4.1/13.4.2?slim=true)
|
| [@nestjs/platform-express](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/platform-express))
| [`11.1.21` →
`11.1.23`](https://renovatebot.com/diffs/npm/@nestjs%2fplatform-express/11.1.21/11.1.23)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fplatform-express/11.1.23?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fplatform-express/11.1.21/11.1.23?slim=true)
|
| [@nestjs/platform-socket.io](https://nestjs.com)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/platform-socket.io))
| [`11.1.21` →
`11.1.23`](https://renovatebot.com/diffs/npm/@nestjs%2fplatform-socket.io/11.1.21/11.1.23)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fplatform-socket.io/11.1.23?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fplatform-socket.io/11.1.21/11.1.23?slim=true)
|
| [@nestjs/swagger](https://redirect.github.com/nestjs/swagger) |
[`11.4.3` →
`11.4.4`](https://renovatebot.com/diffs/npm/@nestjs%2fswagger/11.4.3/11.4.4)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fswagger/11.4.4?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fswagger/11.4.3/11.4.4?slim=true)
|
| [@nestjs/websockets](https://redirect.github.com/nestjs/nest)
([source](https://redirect.github.com/nestjs/nest/tree/HEAD/packages/websockets))
| [`11.1.21` →
`11.1.23`](https://renovatebot.com/diffs/npm/@nestjs%2fwebsockets/11.1.21/11.1.23)
|
![age](https://developer.mend.io/api/mc/badges/age/npm/@nestjs%2fwebsockets/11.1.23?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/@nestjs%2fwebsockets/11.1.21/11.1.23?slim=true)
|

---

### Release Notes

<details>
<summary>nestjs/graphql (@&#8203;nestjs/apollo)</summary>

###
[`v13.4.2`](https://redirect.github.com/nestjs/graphql/releases/tag/v13.4.2)

[Compare
Source](https://redirect.github.com/nestjs/graphql/compare/v13.4.1...v13.4.2)

##### v13.4.2 (2026-05-21)

##### Bug fixes

- `graphql`
- [#&#8203;4007](https://redirect.github.com/nestjs/graphql/pull/4007)
fix(graphql): preserve PickType fields for dual-decorated inputs
([@&#8203;yudin-s](https://redirect.github.com/yudin-s))

##### Committers: 1

- Serge Yudin ([@&#8203;yudin-s](https://redirect.github.com/yudin-s))

</details>

<details>
<summary>nestjs/nest (@&#8203;nestjs/common)</summary>

###
[`v11.1.23`](https://redirect.github.com/nestjs/nest/releases/tag/v11.1.23)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.22...v11.1.23)

##### v11.1.23 (2026-05-21)

##### Bug fixes

- `core`
- [#&#8203;16998](https://redirect.github.com/nestjs/nest/issues/16998)
fix snapshot: true eagerly instantiates Terminus transient indicators
since 11.1.20

##### Committers: 1

- Kamil Mysliwiec
([@&#8203;kamilmysliwiec](https://redirect.github.com/kamilmysliwiec))

###
[`v11.1.22`](https://redirect.github.com/nestjs/nest/releases/tag/v11.1.22)

[Compare
Source](https://redirect.github.com/nestjs/nest/compare/v11.1.21...v11.1.22)

##### v11.1.22 (2026-05-21)

##### Bug fixes

- `core`
- [#&#8203;16993](https://redirect.github.com/nestjs/nest/pull/16993)
fix(core): inflight request injection bug
[#&#8203;16989](https://redirect.github.com/nestjs/nest/issues/16989)
([@&#8203;kamilmysliwiec](https://redirect.github.com/kamilmysliwiec))

##### Enhancements

- `core`
- [#&#8203;16967](https://redirect.github.com/nestjs/nest/pull/16967)
fix(core): identify decorator type in invalid-class-module error
([@&#8203;HarrierOnChain](https://redirect.github.com/HarrierOnChain))
  -

##### Committers: 2

- Harrier
([@&#8203;HarrierOnChain](https://redirect.github.com/HarrierOnChain))
- Kamil Mysliwiec
([@&#8203;kamilmysliwiec](https://redirect.github.com/kamilmysliwiec))

</details>

<details>
<summary>nestjs/swagger (@&#8203;nestjs/swagger)</summary>

###
[`v11.4.4`](https://redirect.github.com/nestjs/swagger/releases/tag/11.4.4)

[Compare
Source](https://redirect.github.com/nestjs/swagger/compare/11.4.3...11.4.4)

#### 11.4.4 (2026-05-21)

##### Bug fixes

- [#&#8203;3930](https://redirect.github.com/nestjs/swagger/pull/3930)
fix: top-level nullable with discriminator issue
([@&#8203;kamilmysliwiec](https://redirect.github.com/kamilmysliwiec))

##### Enhancements

- [#&#8203;3921](https://redirect.github.com/nestjs/swagger/pull/3921)
feat(swagger): add summary field to Tag Object (OpenAPI 3.2)
([@&#8203;frbuceta](https://redirect.github.com/frbuceta))
- [#&#8203;3924](https://redirect.github.com/nestjs/swagger/pull/3924)
feat(swagger): warn when
[@&#8203;ApiTags](https://redirect.github.com/ApiTags) receives
hierarchy fields
([@&#8203;frbuceta](https://redirect.github.com/frbuceta))
- [#&#8203;3925](https://redirect.github.com/nestjs/swagger/pull/3925)
fix(swagger): type Tag Object kind as a free-form string
([@&#8203;frbuceta](https://redirect.github.com/frbuceta))

##### Committers: 4

- Alexander Scholz
([@&#8203;LucidityDesign](https://redirect.github.com/LucidityDesign))
- Francisco Buceta
([@&#8203;frbuceta](https://redirect.github.com/frbuceta))
- Kamil Mysliwiec
([@&#8203;kamilmysliwiec](https://redirect.github.com/kamilmysliwiec))
- Natanael dos Santos Feitosa
([@&#8203;natanfeitosa](https://redirect.github.com/natanfeitosa))

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

👻 **Immortal**: This PR will be recreated if closed unmerged. Get
[config
help](https://redirect.github.com/renovatebot/renovate/discussions) if
that's undesired.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xOTQuMCIsInVwZGF0ZWRJblZlciI6IjQzLjE5NC4wIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `6d1172ba445fde179ff0a46797b1875150126d9d` — chore: bump deps — data não informada\n  - `2aa56cbccd76685b6d09b57fcc53a1f92ade0f01` — chore: bump toolchain & fix lint — data não informada\n  - `adfa51a3724af123db845af3fbc1533129508ddd` — chore: bump up oxlint version to v1.66.0 (#14974)

This PR contains the following updates:

| Package | Change |
[Age](https://docs.renovatebot.com/merge-confidence/) |
[Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|
| [oxlint](https://oxc.rs/docs/guide/usage/linter)
([source](https://redirect.github.com/oxc-project/oxc/tree/HEAD/npm/oxlint))
| [`1.58.0` →
`1.66.0`](https://renovatebot.com/diffs/npm/oxlint/1.58.0/1.66.0) |
![age](https://developer.mend.io/api/mc/badges/age/npm/oxlint/1.66.0?slim=true)
|
![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/oxlint/1.58.0/1.66.0?slim=true)
|

---

### Release Notes

<details>
<summary>oxc-project/oxc (oxlint)</summary>

###
[`v1.66.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1660---2026-05-18)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.65.0...oxlint_v1.66.0)

##### 🚀 Features

-
[`0440b0f`](https://redirect.github.com/oxc-project/oxc/commit/0440b0f)
linter/eslint: Implement `id-match` rule
([#&#8203;22379](https://redirect.github.com/oxc-project/oxc/issues/22379))
(Vladislav Sayapin)
-
[`65bf119`](https://redirect.github.com/oxc-project/oxc/commit/65bf119)
linter: Implement react no-object-type-as-default-prop
([#&#8203;22481](https://redirect.github.com/oxc-project/oxc/issues/22481))
(uhyo)
-
[`2a6ddce`](https://redirect.github.com/oxc-project/oxc/commit/2a6ddce)
linter/eslint: Implement `no-implied-eval` rule
([#&#8203;22391](https://redirect.github.com/oxc-project/oxc/issues/22391))
(Vladislav Sayapin)
-
[`625758a`](https://redirect.github.com/oxc-project/oxc/commit/625758a)
linter/vitest: Implement padding-around-after-all-blocks rule
([#&#8203;21788](https://redirect.github.com/oxc-project/oxc/issues/21788))
(kapobajza)
-
[`37680b0`](https://redirect.github.com/oxc-project/oxc/commit/37680b0)
linter: Implement react no-unstable-nested-components
([#&#8203;22248](https://redirect.github.com/oxc-project/oxc/issues/22248))
(Jovi De Croock)
-
[`d8d9c74`](https://redirect.github.com/oxc-project/oxc/commit/d8d9c74)
linter: Implement import/newline-after-import rule
([#&#8203;19142](https://redirect.github.com/oxc-project/oxc/issues/19142))
(Ryuya Yanagi)

###
[`v1.65.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1650---2026-05-15)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.64.0...oxlint_v1.65.0)

##### 🚀 Features

-
[`5478fb5`](https://redirect.github.com/oxc-project/oxc/commit/5478fb5)
linter/jsdoc: Implement `require-throws-description` rule
([#&#8203;22386](https://redirect.github.com/oxc-project/oxc/issues/22386))
(Mikhail Baev)
-
[`c73225e`](https://redirect.github.com/oxc-project/oxc/commit/c73225e)
linter/eslint: Implement `prefer-arrow-callback` rule
([#&#8203;22312](https://redirect.github.com/oxc-project/oxc/issues/22312))
(박천(Cheon Park))
-
[`de82b59`](https://redirect.github.com/oxc-project/oxc/commit/de82b59)
linter: Add support for `eslint-plugin-jsx-a11y-x`
([#&#8203;22356](https://redirect.github.com/oxc-project/oxc/issues/22356))
(mehm8128)
-
[`f44b6c8`](https://redirect.github.com/oxc-project/oxc/commit/f44b6c8)
linter: Fill schemas `DummyRuleMap` with built-in rules
([#&#8203;22288](https://redirect.github.com/oxc-project/oxc/issues/22288))
(Sysix)

###
[`v1.64.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1640---2026-05-11)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.63.0...oxlint_v1.64.0)

##### 🚀 Features

-
[`fbb8f22`](https://redirect.github.com/oxc-project/oxc/commit/fbb8f22)
linter: Support `ignores` in overrides
([#&#8203;22148](https://redirect.github.com/oxc-project/oxc/issues/22148))
(camc314)

##### 🐛 Bug Fixes

-
[`25b7017`](https://redirect.github.com/oxc-project/oxc/commit/25b7017)
linter: Undocument override `ignores` option
([#&#8203;22213](https://redirect.github.com/oxc-project/oxc/issues/22213))
(camc314)

###
[`v1.63.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1630---2026-05-05)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.62.0...oxlint_v1.63.0)

##### 📚 Documentation

-
[`cacbc4a`](https://redirect.github.com/oxc-project/oxc/commit/cacbc4a)
linter: Fix jest settings docs.
([#&#8203;22127](https://redirect.github.com/oxc-project/oxc/issues/22127))
(connorshea)

###
[`v1.62.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1620---2026-04-27)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/7a75f0d0555ee8e5012874eeb3f06f7272804e37...oxlint_v1.62.0)

##### 🚀 Features

-
[`348f46c`](https://redirect.github.com/oxc-project/oxc/commit/348f46c)
linter: Add `respectEslintDisableDirectives` option
([#&#8203;21384](https://redirect.github.com/oxc-project/oxc/issues/21384))
(Christian Vuerings)

##### 🐛 Bug Fixes

-
[`8c425db`](https://redirect.github.com/oxc-project/oxc/commit/8c425db)
linter: Allow string for jest version in config schema
([#&#8203;21649](https://redirect.github.com/oxc-project/oxc/issues/21649))
(camc314)

###
[`v1.61.1`](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.61.0...7a75f0d0555ee8e5012874eeb3f06f7272804e37)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.61.0...7a75f0d0555ee8e5012874eeb3f06f7272804e37)

###
[`v1.61.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1610---2026-04-20)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.60.0...oxlint_v1.61.0)

##### 🚀 Features

-
[`38d8090`](https://redirect.github.com/oxc-project/oxc/commit/38d8090)
linter/jest: Implemented jest `version` settings in config file.
([#&#8203;21522](https://redirect.github.com/oxc-project/oxc/issues/21522))
(Said Atrahouch)

###
[`v1.60.0`](https://redirect.github.com/oxc-project/oxc/blob/HEAD/npm/oxlint/CHANGELOG.md#1600---2026-04-13)

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.59.0...oxlint_v1.60.0)

##### 📚 Documentation

-
[`cfd8a4f`](https://redirect.github.com/oxc-project/oxc/commit/cfd8a4f)
linter: Don't rely on old eslint doc for available globals
([#&#8203;21334](https://redirect.github.com/oxc-project/oxc/issues/21334))
(Nicolas Le Cam)

### [`v1.59.0`]()

[Compare
Source](https://redirect.github.com/oxc-project/oxc/compare/oxlint_v1.58.0...oxlint_v1.59.0)

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xNzkuMyIsInVwZGF0ZWRJblZlciI6IjQzLjE4NS4xIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `4f0d9aff302662e70f3dd9584d081e97e276905b` — chore: bump up rustc version to v1.95.0 (#15009)

This PR contains the following updates:

| Package | Update | Change |
|---|---|---|
| [rustc](https://redirect.github.com/rust-lang/rust) | minor | `1.94.0`
→ `1.95.0` |

---

### Release Notes

<details>
<summary>rust-lang/rust (rustc)</summary>

###
[`v1.95.0`](https://redirect.github.com/rust-lang/rust/blob/HEAD/RELEASES.md#Version-1950-2026-04-16)

[Compare
Source](https://redirect.github.com/rust-lang/rust/compare/1.94.1...1.95.0)

\===========================

<a id="1.95-Language"></a>

## Language

- [Stabilize `if let` guards on match
arms](https://redirect.github.com/rust-lang/rust/pull/141295)
- [`irrefutable_let_patterns` lint no longer lints on let
chains](https://redirect.github.com/rust-lang/rust/pull/146832)
- [Support importing path-segment keywords with
renaming](https://redirect.github.com/rust-lang/rust/pull/146972)
- [Stabilize inline assembly for PowerPC and
PowerPC64](https://redirect.github.com/rust-lang/rust/pull/147996)
- [const-eval: be more consistent in the behavior of padding during
typed copies](https://redirect.github.com/rust-lang/rust/pull/148967)
- [Const blocks are no longer evaluated to determine if expressions
involving fallible operations can implicitly be
constant-promoted.](https://redirect.github.com/rust-lang/rust/pull/150557).
Expressions whose ability to implicitly be promoted would depend on the
result of a const block are no longer implicitly promoted.
- [Make operational semantics of pattern matching independent of crate
and module](https://redirect.github.com/rust-lang/rust/pull/150681)

<a id="1.95-Compiler"></a>

## Compiler

- [Stabilize `--remap-path-scope` for controlling the scoping of how
paths get remapped in the resulting
binary](https://redirect.github.com/rust-lang/rust/pull/147611)
- [Apply patches for CVE-2026-6042 and CVE-2026-40200 to vendored
musl](https://redirect.github.com/rust-lang/rust/pull/155171)

<a id="1.95-Platform-Support"></a>

## Platform Support

- [Promote `powerpc64-unknown-linux-musl` to Tier 2 with host
tools](https://redirect.github.com/rust-lang/rust/pull/149962)
- [Promote `aarch64-apple-tvos` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-tvos-sim` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-watchos` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-watchos-sim` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-visionos` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)
- [Promote `aarch64-apple-visionos-sim` to Tier
2](https://redirect.github.com/rust-lang/rust/pull/152021)

Refer to Rust's [platform support page][platform-support-doc]
for more information on Rust's tiered platform support.

[platform-support-doc]:
https://doc.rust-lang.org/rustc/platform-support.html

<a id="1.95-Libraries"></a>

## Libraries

- [`thread::scope`: document how join interacts with TLS
destructors](https://redirect.github.com/rust-lang/rust/pull/149482)
- [Speed up `str::contains` on aarch64 targets with `neon` target
feature enabled by
default](https://redirect.github.com/rust-lang/rust/pull/152176)

<a id="1.95-Stabilized-APIs"></a>

## Stabilized APIs

- [`MaybeUninit<[T; N]>: From<[MaybeUninit<T>;
N]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-From%3CMaybeUninit%3C%5BT;+N%5D%3E%3E-for-%5BMaybeUninit%3CT%3E;+N%5D)
- [`MaybeUninit<[T; N]>: AsRef<[MaybeUninit<T>;
N]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsRef%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>:
AsRef<[MaybeUninit<T>]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsRef%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>: AsMut<[MaybeUninit<T>;
N]>`](https://doc.rust-lang.org/beta/std/mem/union.MaybeUninit.html#impl-AsMut%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`MaybeUninit<[T; N]>:
AsMut<[MaybeUninit<T>]>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-AsMut%3C%5BMaybeUninit%3CT%3E%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`[MaybeUninit<T>; N]: From<MaybeUninit<[T;
N]>>`](https://doc.rust-lang.org/stable/std/mem/union.MaybeUninit.html#impl-From%3C%5BMaybeUninit%3CT%3E;+N%5D%3E-for-MaybeUninit%3C%5BT;+N%5D%3E)
- [`Cell<[T; N]>: AsRef<[Cell<T>;
N]>`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html#impl-AsRef%3C%5BCell%3CT%3E;+N%5D%3E-for-Cell%3C%5BT;+N%5D%3E)
- [`Cell<[T; N]>:
AsRef<[Cell<T>]>`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT;+N%5D%3E)
- [`Cell<[T]>:
AsRef<[Cell<T>]>`](https://doc.rust-lang.org/stable/std/cell/struct.Cell.html#impl-AsRef%3C%5BCell%3CT%3E%5D%3E-for-Cell%3C%5BT%5D%3E)
- [`bool:
TryFrom<{integer}>`](https://doc.rust-lang.org/stable/std/primitive.bool.html#impl-TryFrom%3Cu128%3E-for-bool)
-
[`AtomicPtr::update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicPtr.html#method.update)
-
[`AtomicPtr::try_update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicPtr.html#method.try_update)
-
[`AtomicBool::update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicBool.html#method.update)
-
[`AtomicBool::try_update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicBool.html#method.try_update)
-
[`AtomicIn::update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicIsize.html#method.update)
-
[`AtomicIn::try_update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicIsize.html#method.try_update)
-
[`AtomicUn::update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicUsize.html#method.update)
-
[`AtomicUn::try_update`](https://doc.rust-lang.org/stable/std/sync/atomic/struct.AtomicUsize.html#method.try_update)
-
[`cfg_select!`](https://doc.rust-lang.org/stable/std/macro.cfg_select.html)
- [`mod
core::range`](https://doc.rust-lang.org/stable/core/range/index.html)
-
[`core::range::RangeInclusive`](https://doc.rust-lang.org/stable/core/range/struct.RangeInclusive.html)
-
[`core::range::RangeInclusiveIter`](https://doc.rust-lang.org/stable/core/range/struct.RangeInclusiveIter.html)
-
[`core::hint::cold_path`](https://doc.rust-lang.org/stable/core/hint/fn.cold_path.html)
- [`<*const
T>::as_ref_unchecked`](https://doc.rust-lang.org/stable/std/primitive.pointer.html#method.as_ref_unchecked)
- [`<*mut
T>::as_ref_unchecked`](https://doc.rust-lang.org/stable/std/primitive.pointer.html#method.as_ref_unchecked-1)
- [`<*mut
T>::as_mut_unchecked`](https://doc.rust-lang.org/stable/std/primitive.pointer.html#method.as_mut_unchecked)
-
[`Vec::push_mut`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html#method.push_mut)
-
[`Vec::insert_mut`](https://doc.rust-lang.org/stable/std/vec/struct.Vec.html#method.insert_mut)
-
[`VecDeque::push_front_mut`](https://doc.rust-lang.org/stable/std/collections/struct.VecDeque.html#method.push_front_mut)
-
[`VecDeque::push_back_mut`](https://doc.rust-lang.org/stable/std/collections/struct.VecDeque.html#method.push_back_mut)
-
[`VecDeque::insert_mut`](https://doc.rust-lang.org/stable/std/collections/struct.VecDeque.html#method.insert_mut)
-
[`LinkedList::push_front_mut`](https://doc.rust-lang.org/stable/std/collections/struct.LinkedList.html#method.push_front_mut)
-
[`LinkedList::push_back_mut`](https://doc.rust-lang.org/stable/std/collections/struct.LinkedList.html#method.push_back_mut)
-
[`Layout::dangling_ptr`](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html#method.dangling_ptr)
-
[`Layout::repeat`](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html#method.repeat)
-
[`Layout::repeat_packed`](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html#method.repeat_packed)
-
[`Layout::extend_packed`](https://doc.rust-lang.org/stable/std/alloc/struct.Layout.html#method.extend_packed)

These previously stable APIs are now stable in const contexts:

-
[`fmt::from_fn`](https://doc.rust-lang.org/stable/std/fmt/fn.from_fn.html)
-
[`ControlFlow::is_break`](https://doc.rust-lang.org/stable/core/ops/enum.ControlFlow.html#method.is_break)
-
[`ControlFlow::is_continue`](https://doc.rust-lang.org/stable/core/ops/enum.ControlFlow.html#method.is_continue)

<a id="1.95-Rustdoc"></a>

## Rustdoc

- [In search results, rank unstable items
lower](https://redirect.github.com/rust-lang/rust/pull/149460)
- [Add new "hide deprecated items" setting in
rustdoc](https://redirect.github.com/rust-lang/rust/pull/151091)

<a id="1.95-Compatibility-Notes"></a>

## Compatibility Notes

- [Array coercions may now result in less inference constraints than
before](https://redirect.github.com/rust-lang/rust/pull/140283)
- Importing `$crate` without renaming, i.e. `use $crate::{self};`, is
now no longer permitted due to stricter error checking for `self`
imports.
- [const-eval: be more consistent in the behavior of padding during
typed copies.](https://redirect.github.com/rust-lang/rust/pull/148967)
In very rare cases, this may cause compilation errors due to bytes from
parts of a pointer ending up in the padding bytes of a `const` or
`static`.
- [A future-incompatibility warning lint
`ambiguous_glob_imported_traits` is now reported when using an
ambiguously glob imported
trait](https://redirect.github.com/rust-lang/rust/pull/149058)
- [Check lifetime bounds of types mentioning only type
parameters](https://redirect.github.com/rust-lang/rust/pull/149389)
- [Report more visibility-related ambiguous import
errors](https://redirect.github.com/rust-lang/rust/pull/149596)
- [Deprecate `Eq::assert_receiver_is_total_eq` and emit future
compatibility warnings on manual
impls](https://redirect.github.com/rust-lang/rust/pull/149978)
- [powerpc64: Use the ELF ABI version set in target spec instead of
guessing](https://redirect.github.com/rust-lang/rust/pull/150468) (fixes
the ELF ABI used by the OpenBSD target)
- Matching on a `#[non_exhaustive]` enum [now reads the discriminant,
even if the enum has only one
variant](https://redirect.github.com/rust-lang/rust/pull/150681). This
can cause closures to capture values that they previously wouldn't.
- `mut ref` and `mut ref mut` patterns, part of the unstable [Match
Ergonomics 2024
RFC](https://redirect.github.com/rust-lang/rust/issues/123076), were
accidentally allowed on stable within struct pattern field shorthand.
These patterns are now correctly feature-gated as unstable in this
position.
- [Add future-compatibility warning for derive helper attributes which
conflict with built-in
attributes](https://redirect.github.com/rust-lang/rust/pull/151152)
- [JSON target
specs](https://doc.rust-lang.org/rustc/targets/custom.html) have been
destabilized and now require `-Z unstable-options` to use. Previously,
they could not be used without the standard library, which has no stable
build mechanism. In preparation for the `build-std` project adding that
support, JSON target specs are being proactively gated to ensure they
remain unstable even if `build-std` is stabilized. Cargo now includes
the `-Z json-target-spec` CLI flag to automatically pass `-Z
unstable-options` to the compiler when needed. See
[#&#8203;150151](https://redirect.github.com/rust-lang/rust/pull/150151),
[#&#8203;151534](https://redirect.github.com/rust-lang/rust/pull/150151),
and
[rust-lang/cargo#16557](https://redirect.github.com/rust-lang/cargo/pull/16557).
- [The arguments of `#[feature]` attributes on invalid targets are now
checked](https://redirect.github.com/rust-lang/rust/issues/153764)

<a id="1.95-Internal-Changes"></a>

## Internal Changes

These changes do not affect any public interfaces of Rust, but they
represent
significant improvements to the performance or internals of rustc and
related
tools.

- [Update to LLVM
22](https://redirect.github.com/rust-lang/rust/pull/150722)

###
[`v1.94.1`](https://redirect.github.com/rust-lang/rust/blob/HEAD/RELEASES.md#Version-1941-2026-03-26)

[Compare
Source](https://redirect.github.com/rust-lang/rust/compare/1.94.0...1.94.1)

\===========================

<a id="1.94.1"></a>

- [Fix `std::thread::spawn` on
wasm32-wasip1-threads](https://redirect.github.com/rust-lang/rust/pull/153634)
- [Remove new methods added to
`std::os::windows::fs::OpenOptionsExt`](https://redirect.github.com/rust-lang/rust/pull/153491)
The new methods were unstable, but the trait itself is not sealed and so
  cannot be extended with non-default methods.
- [Clippy: fix ICE in
`match_same_arms`](https://redirect.github.com/rust-lang/rust-clippy/pull/16685)
- [Cargo: update tar to
0.4.45](https://redirect.github.com/rust-lang/cargo/pull/16769)
This resolves CVE-2026-33055 and CVE-2026-33056. Users of crates.io are
not affected.
See [blog](https://blog.rust-lang.org/2026/03/21/cve-2026-33056/) for
more details.

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you
are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the
rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about this update
again.

---

- [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check
this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/).
View the [repository job
log](https://developer.mend.io/github/toeverything/AFFiNE).

<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0My4xODUuMSIsInVwZGF0ZWRJblZlciI6IjQzLjE4NS4xIiwidGFyZ2V0QnJhbmNoIjoiY2FuYXJ5IiwibGFiZWxzIjpbImRlcGVuZGVuY2llcyJdfQ==-->

Co-authored-by: renovate[bot] <29139614+renovate[bot]@users.noreply.github.com> — data não informada\n  - `eecd0a2169d85a61ecdbf7782ad6ef458537ae41` — feat(i18n): add Turkish translation (#15000)

This pull request introduces support for the Turkish language to the
frontend internationalization system and adds a new pull request
template to standardize PR descriptions. The main changes are grouped
below:

**Internationalization: Turkish Language Support**
* Added `'tr'` (Turkish) to the `Language` type and
`SUPPORTED_LANGUAGES` object in `index.ts`, including its display name,
native name, flag emoji, and resource loader.
[[1]](diffhunk://#diff-ba5f665c3490d0f5acb2cb70f08314c5373137fa8085ab05175047f10cb7fdf8L26-R27)
[[2]](diffhunk://#diff-ba5f665c3490d0f5acb2cb70f08314c5373137fa8085ab05175047f10cb7fdf8R183-R188)
* Updated `i18n-completenesses.json` to include Turkish (`"tr": 6`).

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->
## Summary by CodeRabbit

* **New Features**
  * Turkish language can now be selected in the app.

* **Localization**
* Initial Turkish translations added and translation completeness set to
100%.
* Locale metadata added (display name, original name, flag) for Turkish.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15000?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `f2980503b4b4fa4d32b212f12b76be753a2a8326` — fix(editor): sorting of page emoji display toggle (#15020)

Fixes the order of the new setting toggle introduced in #14999.
It appeared between "Auto-title new docs with current date" and "New doc
date format" which both belong together.

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->

## Summary by CodeRabbit

* **Style**
* Repositioned the "display add icon option" setting within General
settings for improved interface organization and logical grouping.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15020?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `925c95ce88f273e1da69e717c148400fa779af54` — feat(i18n): update German translation (#15011)

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->
## Summary by CodeRabbit

* **Localization**
  * German language completeness raised to 100%.
* Added German translations for Markdown export/copy labels and success
text, import formats (including Bear backup and Word .docx), editor
settings (auto-date-title formats, add-icon option), AI BYOK
workspace/provider-key UI and notifications, and a recording/importing
UI prompt.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15011?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada\n  - `3098b3b14bc42ebc77e68675407166fa05d664a4` — feat(server): bump models (#15013)

#### PR Dependency Tree


* **PR #15013** 👈

This tree was auto-generated by
[Charcoal](https://github.com/danerwilliams/charcoal)

<!-- This is an auto-generated comment: release notes by coderabbit.ai
-->

## Summary by CodeRabbit

* **New Features**
* Expanded AI capabilities with the addition of Gemini 3.5 Flash model,
providing enhanced options for AI-powered features.

* **Updates**
* Updated Claude Sonnet to the latest version for improved performance.
  * Refreshed pro models configuration with optimized selections.

<!-- review_stack_entry_start -->

[![Review Change
Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/toeverything/AFFiNE/pull/15013?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->

<!-- end of auto-generated comment: release notes by coderabbit.ai --> — data não informada
\n## 4. William-kelvem94/AGENTE-IA

- **Registros retornados:** 10
- **Amostra:**
  - `9e9eb909fd47d75b6199c42fb0de131f3aa2e06b` — 🚀 Refatoração de Emergência V5.0 & V6.0: Estabilização do Core e Interface

- 🔧 Correção de roteamento WebSocket (/ws/chat/{session_id}) para suportar múltiplas sessões.
- 🧵 Adição de thread-safety no broadcast_sync para comunicações assíncronas seguras.
- 📂 Implementação de caminhos absolutos para assets estáticos e templates, garantindo compatibilidade no Windows.
- 🧠 Integração total dos eventos do Agente (agent_thought, tool_call, tool_result) no frontend.
- 🐛 Resgate V6.0: Correção de erro de importação fatal em command_processor.py que impedia o boot do servidor.
- �� Limpeza de caches obsoletos e encerramento de processos órfãos na porta 8000.
- 📡 Adição de feedback visual de execução de ferramentas no terminal da IDE. — data não informada\n  - `e8d5996b18539b9270ffe8752834c3883c90dc8b` — Automated commit via Dashboard — data não informada\n  - `a4300a1f36322a62717720db66c8fdc0bb97febc` — 🚀 Feat: Concluída a Refatoração V2 do AGENTE-IA (Phases 1-4)

✨ O que mudou:
- 🏗️ Reestruturação completa do `agent/` em `api`, `core` e `tools`
- 🌐 Interface Web Unificada (Glassmorphism UI) rodando em WebSockets bidirecionais
- 🧠 NLP Avançado: o `command_processor.py` agora entende comandos naturais para construir rotinas de ferramentas em JSON
- 🗂️ Expansão de Habilidades: ferramentas de sistema de arquivos (`create_file`, `mkdir`, `delete_file`, `move_file`) e `web_fetch` embutidas no ciclo ReAct
- 💻 Gestão Inteligente de Hardware: `resource_manager.py` ativo que gerencia o uso de RAM para rotear as chamadas LLM entre tarefas de raciocínio leve e tarefas intensivas de codificação no Ollama
- 🧹 Remoção de arquivos legados (incluindo `tmp.patch`, pastas defasadas, e dependências não mais usadas)
- ✅ Refatoração de todos os imports das suítes de teste de acordo com os novos contratos da arquitetura

Uma evolução gigantesca, transformando de CLI utilitária para assistente Autônomo e Multimodal. — data não informada\n  - `4180cfda68ee2029ca09abffbd7be8c2a7a7cf8b` — 🔁 release: resumo das melhorias recentes — UI, Ollama auto‑start, estabilidade e testes — data não informada\n  - `b002a87d86ec94ab55d012145dd53f62808a9f6d` — 🔁 infra: garantir Ollama ao iniciar (detectar → iniciar → opcional instalar) + testes — data não informada\n  - `aa81b883c50ca4446cc6a5560f5213fb36c43031` — ✨ UI: redesign parcial — modal de confirmação acessível, atalhos, toasts e melhorias de UX — data não informada\n  - `f658f5f4af35cec1efc008be64c9837c4953ec7b` — 🔧 UI/UX: toasts, Ollama health badge + fallback streaming; melhorias no fluxo de aplicação de patch — data não informada\n  - `445a5f9f61c48d2921fae2279c9d30045d7ab289` — 🔧 chore: renomear .venv-ml + atualizar .gitignore e VS Code settings

- Renomeado `.venv-1` → `.venv-ml` para separar o ambiente ML (contém: torch, transformers, openvino, sentence_transformers, numpy, scipy, etc.).
- Atualizado `/.gitignore` para ignorar `/.venv-ml/` e evitar commits acidentais de ambientes virtuais.
- Adicionado `/.vscode/settings.json` apontando o interpretador para `./.venv` (padronização do editor).

Motivação: preservar um ambiente ML pesado separado, reduzir risco de commitar artefatos binários e melhorar experiência de desenvolvimento local. — data não informada\n  - `6a1a1f063fa04759067ce043a2d27d8d0ebdc2e6` — ﻿✨ Feat/UI e UX — Chat persistente, visualizador de diffs e melhorias de fluxo

Resumo das alterações:
- Adicionado painel de Chat com histórico persistente por repositório (SQLite) e endpoints: /api/chat/message, /api/chat/list, /api/chat/sessions.
- Implementado visualizador de diffs lado-a-lado com navegação por hunks e botão "Ver Diff" (preview rápido no chat).
- Sessões de chat: sidebar, criar/selecionar/pin, pesquisa por sessão e busca dentro da sessão atual.
- Quick-actions no chat: Gerar Patch, Aplicar Patch, Rodar Testes, Permitir arquivo, Criar PR, Tema claro/escuro.
- Correções e robustez: validação de prompt no frontend, tratamento de 400/404, remoção de listeners duplicados e mensagens de erro mais claras.
- Backend: adicionado `chat_store.py` (persistência), novos endpoints e ajustes no `server.py` e `patch_store.py`.
- Tests: adicionados testes de integração para chat/patch e endpoint de PR (pytest).

Arquivos principais alterados/adicionados:
- agent/static/js/app.js
- agent/templates/index.html
- agent/static/css/style.css
- agent/chat_store.py
- agent/server.py
- agent/tests/test_chat_and_patch_ui.py
- agent/patch_store.py
- (diversos ajustes em arquivos existentes e testes)

Próximos passos sugeridos: parser de diff avançado (renames/binary), testes E2E com Playwright e aprimoramento do visual do diff.

Assinado: AGENTE-IA — data não informada\n  - `aa361fa148c4be3aa6758bc06538b27b8cc57038` — Initial commit — data não informada
\n## 5. William-kelvem94/AppFlowy-Will

- **Registros retornados:** 100
- **Amostra:**
  - `4af02cdc87468be10ab15dbb4afd27fbf53ce89b` — fix: add autofillHints support to AFTextField (#8594)

* chore: bump version to 0.11.4 and update changelog

* feat: add autofillHints support to AFTextField

* fix: remove autoFocus from font search input

* chore: fix code formatting — data não informada\n  - `bbe886fcdd5295ff49aaeec883181c67ca89ec29` — Update README.md (#8327) — data não informada\n  - `f0f10b05f4f2a22ed8632287e9e81d4eaf6fbbbd` — fix: prevent page flickering on rapid sidebar clicks (#8278)

* fix: prevent page flickering on rapid sidebar clicks

* refactor: improve deduplication to check both plugin and view IDs — data não informada\n  - `b5a1ccb4eedf27934a115f3d94cc7dd1ba0cdb9e` — Update Italian Translations (#8253)

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦 — data não informada\n  - `148f26892369a15f76603dbe292904592ff79acb` — chore: update translations with Fink 🐦 (#8320) — data não informada\n  - `1ed3d5439b47705ebef19c92a3259cec94c8eb63` — fix: enable password manager autofill for all password fields (#8295)

- Added autofillHints to password fields in sign-in, password setup, and password change screens
- Enables password managers (1Password, LastPass, Bitwarden, etc.) to detect and autofill password fields
- Minimal change: only added AutofillHints.password property to 8 password fields across 4 files — data não informada\n  - `2e00509ebb38304fd142e3db7a601b32a8a1fdd5` — fix: set autoFocus true for font dropdown search input (#8294) — data não informada\n  - `41ca1dd8eef815becc407058b883e9d0d667494d` — chore: bump version 0.9.9 (#8214) — data não informada\n  - `a447af334dca18cc5afeb0c48941a82f0e6dd776` — chore: update zh-TW translations (#8128)

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦

* chore: update translations with Fink 🐦 — data não informada\n  - `223126aff7500d79beca2d5dae4c40ee61ddbf66` — chore: update cs-CZ translations with Fink 🐦 (#8157) — data não informada\n  - `6654e0c6b3cbf172bd4c3316be36a2c3d9a3106e` — chore: update ar-SA translations with Fink 🐦 (#8167) — data não informada\n  - `1fbd37631a269177aff1a210451520e1cd0c3a66` — chore: update zh-CN translations (#8174)

Some Chinese translations have been revised to make them look more authentic. — data não informada\n  - `6b84c4b9701c9ca0b47123b6318a189ea8583318` — chore: upgrade AGP version to 8.1.0 (#8119)

* chore: upgrade AGP version to 8.1.0

* chore: update version info — data não informada\n  - `7599c1902d5574da3c15b5d787f0bc0b7803dd43` — fix: prevent location from being accessed continuously on Windows (#8110) — data não informada\n  - `7b1a15374910a4ea2fa44e8f07778ad902efdfdf` — chore: remove extra space in createdAt translation of zh-CN (#8094) — data não informada\n  - `d83faa46751236ae62719a889e2f41df8890bdf7` — fix: inlang not working for translators (#8073) — data não informada\n  - `460fd54182f54fb98b3505ccccebd9814e005f5e` — chore: adjust toast component (#8060)

* chore: adjust toast component

* test: fix tests — data não informada\n  - `d4f9c71ec233627a90bf8bb64e8ab89e9565a52f` — refactor: rename dialog (#8059)

* refactor: rename dialog

* test: fix test — data não informada\n  - `a480889c281f45d5f026f87278572bba8d68f109` — chore(mobile): add selected sources count indicator (#8056) — data não informada\n  - `8d5019471b388693170dcbf78e9f22e5d08461ee` — chore: add local ai learn more button (#8053) — data não informada
\n## 6. William-kelvem94/Atividade-01

- **Registros retornados:** 2
- **Amostra:**
  - `9981aae366803679e2488e07b7109d39405fbcf5` — Atualização dia 23-09 — data não informada\n  - `9f8de278cf1ef075de7b4d6b07eb3a429efe77d4` — Initial commit — data não informada
\n## 7. William-kelvem94/Atividade-03

- **Registros retornados:** 2
- **Amostra:**
  - `468d20ecc3c427cb4c6c1ebb04d92d382a0d7f7e` — 27/09/2021 — data não informada\n  - `5b5d0c6e313e621144408ae37ef117232d0f7d82` — Initial commit — data não informada
\n## 8. William-kelvem94/att_18_ago

- **Registros retornados:** 1
- **Amostra:**
  - `22befabfba253f598024b6002ab40de8cf11ac3a` — Add files via upload — data não informada
\n## 9. William-kelvem94/AULA_PROG_AVAN

- **Registros retornados:** 1
- **Amostra:**
  - `0a8a8c0a026363825711f9dfaa1abd5e23d18a33` — Initial commit — data não informada
\n## 10. William-kelvem94/Auto-boletos

- **Registros retornados:** 100
- **Amostra:**
  - `e3712011843c71faad2d125374bb4c8a1854b3e4` — fix: configurar @tailwindcss/postcss para compatibilidade com Tailwind CSS v4 — data não informada\n  - `29658b9bf4179581097ac9025fce1ce353d2da5c` — build: substituir npm ci por npm install no Dockerfile — data não informada\n  - `d018450ee1a95fe090960fd8ba0774f44836277d` — fix: Correcoes de imports, Dockerfile, configuracao do Flask e scripts de teste

- Corrigido build do frontend no Dockerfile com 'npm ci' para instalar devDependencies (Vite/Tailwind) e gerar assets.
- Otimizada a instalacao de dependencias do Chromium no Docker com 'playwright install --with-deps chromium'.
- Corrigidos imports obsoletos nos scripts de teste ('validate_system.py' e 'tests/test_setup.py') substituindo 'src.equatorial_automation' por 'src.services.equatorial_service'.
- Atualizadas as rotas de teste no 'test_setup.py' para a nova versao com prefixo '/api/v1/'.
- Consertada a assinatura do construtor de 'EquatorialAutomationFacade' no 'test_equatorial.py' e corrigido docstring invalido.
- Unificado o carregamento de configuracoes do Flask em 'src/app.py' utilizando 'Config' para manter a paridade com as variaveis de ambiente. — data não informada\n  - `cf8924857e3ce60787ad881c3a62fb399bdb6c59` — feat: adicionar suporte ao build do frontend no Dockerfile com Node.js — data não informada\n  - `ddb8c82695a62b019da4ce85a2352c3de5fe0f49` — feat: adicionar documentação de arquitetura e roadmap do projeto — data não informada\n  - `54985f958fe80c510ea1a84c6206f4863093ddf7` — fix: build React frontend no Docker para Render deploy completo (npm run build + copy to static) (BLACKBOXAI) — data não informada\n  - `994106309734aa7a0b3726882e8809f9988e0f0f` — fix(app.py): ajustar rota principal para SPA Routing — data não informada\n  - `61c35b10864e45d665fd222c9960176a5ddb3a14` — feat: interface MODERNA standalone Tailwind em src/static/index.html + SPA routing no app.py + render.yaml frontend (BLACKBOXAI) — data não informada\n  - `f38ad8c31033b92791dd1e68a0c09ab2a681af77` — Fix: resolve NameError timedelta + corrigir indentação app.py (BLACKBOXAI) — data não informada\n  - `7044d5a5bfd427edec7bfcf06a9473c8c6969a4a` — fix(TODO.md, app.py): corrigir erros e atualizar plano de ação — data não informada\n  - `653412dc7f835acb99d5718482047317a6d786c9` — fix(syntax): equatorial_service.py docstrings - Render gunicorn boot 100% — data não informada\n  - `000e78e750e218072ede12e397c4a9cb5c515203` — fix(models.py): SyntaxError docstrings - Render boot OK — data não informada\n  - `96839de7a54f987ff1ab81c72ceddea255b50b66` — \fix(deploy-final): prod requirements + headless opencv + gunicorn CMD Render 100% OK" — data não informada\n  - `9fe82f51cff36941f0cc8fe67e13c671c64b13ea` — fix(Render Docker): flask-limiter==3.5.1 compat — data não informada\n  - `f4a42f6518b89f6904eb989331e120f012eda9f1` — \fix(Render): requirements clean pytest-playwright=0.7.2 - Docker pip OK" — data não informada\n  - `914185534309ca80d61d9022769444f618d4a697` — fix(final): Render deps + indent + frontend SPA - 100% working — data não informada\n  - `9f9a18ff096f6141adc52036a6a44496a978a001` — fix(docker): pytest-playwright 0.7.2 compat Render Python — data não informada\n  - `f52ba2fb02816bbdf2c3c86c09d26bd2fff2b943` — fix(indent): corrigir indentation app.py IndentationError linha 39 — data não informada\n  - `09381d02a22f756a0089049007ab7c979d8fef18` — feat: JWT fullstack, frontend auth, retry deps - Render ready — data não informada\n  - `17cb861c11fc7e8a0e4fb6387363cd1a718a9031` — feat: implement EquatorialAutomation service with CAPTCHA handling and update project TODO list — data não informada
\n## 11. William-kelvem94/AUTOBOT

- **Registros retornados:** 3
- **Amostra:**
  - `92326da7240abeab3341c53ef557713aee8a76b1` — segurança: reescrever histórico removendo .env versionado — data não informada\n  - `8add515e461181da8a41309ec53979cc19af95e1` — RECOMEÇAR — data não informada\n  - `e78489f7c172e6e155d5c012ecf593d1b764c701` — first commit — data não informada
\n## 12. William-kelvem94/Automatizador

- **Registros retornados:** 4
- **Amostra:**
  - `ec0e1bf381b86fcd0f9206926729d8c367583f65` — feat: 🚀 Integração total do Motor de Automação e Monitoramento em Tempo Real v5.0. 🔄 Monitoramento Real: Dashboard agora reflete dados reais de sistema e execução. ⚙️ Configurações Centralizadas: Sincronização reativa entre abas de automação e settings. 🚀 Automação de Verdade: Integração do motor Selenium real para execução de login. 📟 Barra de Status Ativa: Sensores de CPU, Memória e Rede funcionando. 🛠️ Bugfixes: Remocão de métodos duplicados e correção de imports relativos. — data não informada\n  - `6d8957c6a47a8b6c83a214d2d59fc8e07ff0d4e1` — 🚀 refactor: Reestruturação completa da arquitetura v5.0 e Auto-Loader

✨ Melhorias Implementadas:
- 🏗️ Fragmentação do monólito UI: De modern_interface.py para um sistema modular em /ui/views e /ui/components.
- 🎨 Design System: Centralização da paleta de cores, tipografia e espaçamentos em /ui/styles.
- 🛡️ Qualidade de Código: Integração de Black, Isort, Flake8 e Pydantic para validação robusta de configurações.
- 🧪 Testes: Migração para Pytest com suite de testes unitários mockados.
- 🚀 Experiência do Usuário: Criação do run.py (Auto-Loader) para instalação automática de dependências e execução simplificada via executar.bat.
- 🔄 CI/CD: Configuração de GitHub Actions (Lint e Tests).

📝 README atualizado com as novas instruções de execução simplificada. — data não informada\n  - `cd82d31d44b200a87a53e015ffd5d79f9b5ea491` — 🚀 Atualização do Automatizador IA - Sistema Inteligente v5.0

📋 DESCRIÇÃO GERAL:
Versão aprimorada do sistema de automação de login, agora com inteligência artificial integrada e uma interface revolucionária.

🎯 NOVAS FUNCIONALIDADES IMPLEMENTADAS:
• Interface moderna com design system avançado e tema escuro
• Detecção automática de campos com aprendizado adaptativo
• Agendamento preditivo inteligente e notificações flutuantes
• Logs estruturados e coloridos para melhor visualização

📁 ESTRUTURA ATUALIZADA:
• Remoção de arquivos obsoletos e reorganização do .gitignore
• Atualização das dependências no requirements.txt
• Inclusão de novas configurações no arquivo config_exemplo.ini

🧪 TESTES E VALIDAÇÕES:
• Testes automatizados atualizados para refletir as novas funcionalidades
• Validação de integração com a nova arquitetura modular

⚙️ TECNOLOGIAS UTILIZADAS:
• Python 3.11+ e Selenium 4 para automação web
• Tkinter Modern para interface gráfica
• APScheduler para agendamento inteligente

📈 STATUS DO PROJETO:
✅ Sistema atualizado e funcional
✅ Interface gráfica revolucionária implementada
✅ Documentação técnica revisada e ampliada
✅ Pronto para uso em produção

🔄 PRÓXIMOS PASSOS PLANEJADOS:
• Suporte a CAPTCHA avançado
• Integração com APIs REST
• Implementação de IA generativa para automação autônoma

📅 DESENVOLVIDO EM: Outubro 2023
👨‍💻 AUTOR: William Pereira (William-kelvem94)
📄 VERSÃO: 5.0.0 - PRODUÇÃO — data não informada\n  - `e1b5fddd468a1bfa414c2d93b56d33c2cacfc524` — 🚀 Implementação inicial do Automatizador de Login - Sistema Inteligente v2.0

📋 DESCRIÇÃO GERAL:
Sistema profissional completo para automação inteligente de login em sites web, desenvolvido em Python com interface gráfica moderna e arquitetura robusta.

🎯 FUNCIONALIDADES IMPLEMENTADAS:

🔧 CORE DO SISTEMA:
• Motor de automação inteligente (login_automator.py) com validação avançada
• Interface gráfica profissional (gui_moderna.py) com design moderno
• Sistema de detecção inteligente de campos usando 5 estratégias diferentes
• Modo híbrido adaptativo com fallback inteligente
• Agendamento automático baseado em horário do sistema local

📁 ESTRUTURA ORGANIZADA:
• src/ - Código fonte principal com módulos bem estruturados
• config/ - Configurações estruturadas e dependências Python
• tests/ - Suite completa de testes automatizados (8 testes diferentes)
• docs/ - Documentação técnica completa e guias de usuário
• scripts/ - Scripts de instalação e execução automatizados

🧪 TESTES IMPLEMENTADOS:
• Teste completo do sistema moderno (teste_completo_moderno.py)
• Validação de importações e dependências
• Teste de funcionalidades core do automatizador
• Verificação da interface gráfica moderna
• Testes de configuração de arquivos
• Validação de funcionalidades de configuração
• Testes de dependências do sistema
• Verificação de constantes da interface

⚙️ TECNOLOGIAS UTILIZADAS:
• Python 3.11+ como linguagem principal
• Selenium WebDriver para automação web
• Tkinter para interface gráfica profissional
• APScheduler para agendamento automático
• ConfigParser para gerenciamento de configurações
• Logging estruturado com níveis e timestamps

🚀 CARACTERÍSTICAS TÉCNICAS:
• Fluxo de 8 fases estruturado para automação completa
• Detecção multi-estratégia de elementos HTML
• Validação avançada de páginas web
• Interface com 2 painéis (configuração e operações)
• Logs detalhados em tempo real
• Tratamento robusto de exceções
• Suporte a múltiplos layouts de formulários

📦 INSTALAÇÃO E EXECUÇÃO:
• Script executar.bat para inicialização automática
• Instalador automático de dependências
• Configuração profissional do navegador
• Validação completa do ambiente

🎨 INTERFACE PROFISSIONAL:
• Design moderno com paleta de cores consistente
• Header profissional com logo e títulos
• Painéis organizados (configuração e controle)
• Barra de status em tempo real
• Logs detalhados com scrollbar
• Controles intuitivos para todas as operações

📈 STATUS DO PROJETO:
✅ Sistema completamente funcional
✅ Interface gráfica moderna implementada
✅ Testes automatizados passando
✅ Documentação técnica completa
✅ Arquitetura profissional estabelecida
✅ Pronto para uso em produção

🔄 PRÓXIMOS PASSOS PLANEJADOS:
• Suporte a múltiplos navegadores
• Interface web responsiva
• API REST para integração
• Suporte avançado a CAPTCHA
• Dashboard de monitoramento em tempo real

📅 DESENVOLVIDO EM: Dezembro 2025
👨‍💻 AUTOR: William Pereira (William-kelvem94)
📄 VERSÃO: 2.0.0 - PRODUÇÃO — data não informada
\n## 13. William-kelvem94/BITRIX-DADOS

- **Registros retornados:** 3
- **Amostra:**
  - `2a6ab2711ad7f50da100290184369c22d34af611` — Sistema completo de extracao de dados Bitrix24 implementado

- Infraestrutura Node.js/TypeScript completa
- Cliente REST API com autenticacao Bitrix24
- Extracao de 2122 registros (CRM, usuarios, organizacao)
- Sistema de templates com 89 itens organizados
- Exportacao em 4 formatos (JSON, PDF, DOCX, TXT)
- Chat interativo e visualizadores avancados
- Documentacao completa e scripts automatizados
- Sistema 100% funcional e pronto para producao — data não informada\n  - `491fbe5a03f9d13192ff0dc963dada577f1c7fc1` — Remove all source files and configuration for the Bitrix24 Data Extractor project, including scripts, extractors, exporters, and documentation files. — data não informada\n  - `d34f62f7db39677a109520326ad5ca1a60cbdfd8` — first commit — data não informada
\n## 14. William-kelvem94/C.A.I.N.E

- **Registros retornados:** 6
- **Amostra:**
  - `2055ad5c4615c58703c437202f80ed176ec5ba29` — Correções aleatorias

Não lembro oq tem aí, só tem kkkkkkkk — data não informada\n  - `1b2125c62c7a89f2e043ad0282cfe768a7fb366f` — feat: initialize n8n-gemini-agent project with essential files and structure

- Add package.json for project dependencies and scripts
- Create render.yaml for deployment configuration
- Implement GeminiClient for API interaction
- Develop markdown-builder for Obsidian note creation
- Create obsidian-builder for file management in Obsidian
- Set up server.js with Express to handle API requests and integrate all components

Co-authored-by: Copilot <copilot@github.com> — data não informada\n  - `7273408d3b2ae9625c3f90b18e7362ffe67d856d` — Add multimodal model integration guidelines to README — data não informada\n  - `010a346ed4464d06746007b7bd071fe6135ab019` — Enhance hardware detection for model loading and training scripts — data não informada\n  - `1d0c8bcdc98907a33b8bd586f6a8dfd22e0c5f5c` — Add incremental training guidelines to README — data não informada\n  - `73fa9b20cd618cf86b9ed9f20f1302519792f8db` — first commit — data não informada
\n## 15. William-kelvem94/CLONNER

- **Registros retornados:** 54
- **Amostra:**
  - `d474fb622956a673693de447a4299ad579c8ab00` — Resolução de conflitos e integração das melhores funcionalidades das branches. Inclui melhorias na API, configuração e dependências. — data não informada\n  - `7a451c64d76539643b5c0c269c6e9c74dc199502` — Refactor Dockerfiles to install dependencies from requirements.txt and enhance logging in the file manager — data não informada\n  - `c4c11b70d35db4aafbbaad3e9906fc05a62d66da` — Initial project structure, docs, and CI setup

Add project documentation, configuration files for linting and testing (.flake8, .pylintrc, .coveragerc, mypy.ini, pytest.ini, pyproject.toml), pre-commit hooks, and GitHub Actions workflow for tests. Introduce Docker Compose for production, multi-stage Dockerfiles for all services, and initial source code layout including API, middleware, monitoring, cache, exceptions, and utility modules. Add comprehensive documentation and initial test suite (unit, integration, e2e). — data não informada\n  - `8cb9d29407eb8851a103a3cc4ab949f3345e507a` — Redesign UI with holographic glassmorphism styles

Revamps the application's visual style to a modern holographic glassmorphism theme. Updates include new gradients, glass backgrounds, animated borders, and enhanced component styling for cards, buttons, forms, tables, monitor/visualization, and layout. Improves responsiveness, accessibility, and visual feedback across the interface. — data não informada\n  - `c1fc906ecc6b4f53ced8058c154ee68006b847c6` — Ensure all projects are listed regardless of DB presence

Moved default value initialization and project appending outside the database existence check. This guarantees that all projects, even those without a database file, are included in the project list. — data não informada\n  - `72728a49448c5e8f63f25398f554c0d18e355b8f` — Improve cloning robustness and add data capture options

This update enhances the site cloning process with better error handling, progress reporting, and support for capturing additional data such as APIs, forms, and session data. The frontend now allows users to choose whether to include data capture, and the UI provides real-time progress and statistics updates using SSE with automatic fallback to polling. The backend and core logic have been refactored for more reliable status tracking, normalized URL handling, and improved database migrations. — data não informada\n  - `f8ac5749b2cc7fa6c38d1f43bc8a532ef439a6b2` — Refactor project structure and Docker support

Major reorganization: removed legacy documentation and scripts, added new Docker documentation and scripts, modularized source code into engines and feature folders, and updated Dockerfile and compose files for improved containerization. Updated .dockerignore and .gitignore for new structure. Added static assets and modernized the web interface. This commit prepares the project for streamlined Docker-based development and deployment. — data não informada\n  - `1949e0d1a17077bf98367d2f580a56f5f59f6f9e` — feat: Adiciona melhorias na interface e otimizações de desempenho

- Atualiza a interface principal para uma experiência mais fluida e responsiva.
- Implementa otimizações de desempenho, incluindo ajustes no carregamento de scripts e gerenciamento de cache.
- Melhora a documentação da interface para refletir as novas funcionalidades e alterações.
- Remove arquivos desnecessários e obsoletos, contribuindo para uma estrutura de projeto mais limpa e organizada. — data não informada\n  - `145136f030c990f82d57ba3018a306866b662f3e` — chore: Remove arquivos obsoletos e desnecessários do projeto

- Exclui arquivos de configuração e documentação desatualizados, incluindo .dockerignore, .gitignore, CHANGELOG.md, e outros arquivos de suporte.
- Limpa a estrutura do projeto, focando em uma versão mais enxuta e organizada.
- Melhora a manutenção do repositório ao eliminar arquivos que não são mais relevantes para o desenvolvimento atual. — data não informada\n  - `3ca6dd72ca7ac868b8023aaf237bace7844e9867` — feat: Atualiza a interface principal e adiciona rota para versão antiga

- Modifica a rota principal para renderizar a interface corrigida sem cache.
- Adiciona nova rota '/old' para acessar a versão antiga da interface, que apresenta problemas de cache.
- Atualiza a documentação da função index para refletir as mudanças na interface. — data não informada\n  - `71ff4bbeea240b4bd5fa3eb23c4b76cdf57fcf27` — feat: Adiciona nova rota para recarregar a página e atualiza configurações de cache

- Implementa a rota '/reload-now' para uma página de reload forçado.
- Atualiza a porta padrão de 5000 para 8080 no arquivo de configuração.
- Realiza ajustes no cache busting, incluindo um novo timestamp para os scripts JavaScript.
- Melhora os logs de inicialização na interface, adicionando informações detalhadas sobre o estado do aplicativo. — data não informada\n  - `6593ce9bf2542e78aa56f6fc6defe69cb1dd3de2` — feat: Implementa cache busting para scripts JavaScript

- Adiciona um timestamp único para forçar o reload de todos os scripts JavaScript.
- Atualiza as referências dos scripts para incluir o timestamp, garantindo que as versões mais recentes sejam carregadas.
- Melhora a gestão de cache na interface, evitando problemas de carregamento de scripts desatualizados. — data não informada\n  - `6aa82e2d754f873dbf85ad734ed40992c34daa68` — feat: Adiciona novas rotas e funcionalidades de limpeza de cache

- Implementa a rota '/test' para uma página de teste de JavaScript.
- Adiciona a rota '/clear-cache' para permitir a limpeza de cache via interface.
- Inclui um botão na interface para limpar o cache e recarregar a página.
- Atualiza o gerenciamento de temas para usar uma instância global do ThemeManager.
- Melhora a inicialização do aplicativo com tratamento de erros e logs informativos. — data não informada\n  - `7bdfbff359c838c6f235810eca5c5359ba6cbeb1` — feat: Adiciona estilos personalizados e melhorias responsivas

- Implementa um scrollbar customizado para melhor usabilidade.
- Ajusta espaçamentos e paddings em diversos componentes para uma aparência mais consistente.
- Melhora a responsividade da interface, especialmente em dispositivos móveis, com ajustes em grids e elementos de layout.
- Adiciona suporte para preferências de redução de animações.
- Atualiza a estrutura de classes CSS para uma melhor organização e legibilidade. — data não informada\n  - `f50dd3883c794e5de40bd8ce29169f21fba8a4fd` — Remove outdated documentation files: ARCHITECTURE_GUIDE.md, AVISOS_ACEITAVEIS.md, IMPLEMENTATION_SUMMARY.md, LINTER_FIXES_COMPLETE.md, and RESULTADO_FINAL.md. Update requirements.txt to include Flask-WTF and Flask-Limiter for enhanced security and form handling. Clean up run.py by removing unnecessary imports. — data não informada\n  - `3a6c035199d730cf91ef0d9365c70235125ccd5c` — feat: Adiciona suporte a encoding UTF-8 no Windows

- Implementa configuração para garantir que a saída do console utilize encoding UTF-8 em sistemas Windows.
- Melhora a compatibilidade do aplicativo com diferentes plataformas, especialmente para usuários do Windows. — data não informada\n  - `312f277cf100d131088a3be7692d62feecc97f99` — Atualiza a licença e remove arquivos obsoletos do projeto

- Atualizada a licença para refletir a mudança de autoria para a equipe CLONNER.
- Removidos arquivos antigos e desnecessários, incluindo mega_hybrid_api.py, mega_hybrid_cloner.py, PROJECT_STRUCTURE.md, e outros arquivos de backup.
- Estrutura do projeto agora mais limpa e organizada, focando na versão atualizada do MEGA HYBRID CLONER v2.0.

Status: Projeto otimizado e pronto para uso. — data não informada\n  - `13992ed9fc8d5f752bbb93db9dfd6675f71a6f5a` — Refatoracao completa: MEGA HYBRID CLONER v2.0

REESTRUTURACAO COMPLETA DO PROJETO

Arquivos Principais Criados:

- mega_hybrid_cloner.py (678 linhas): Motor completo de clonagem

- mega_hybrid_api.py (340 linhas): API Flask com endpoints REST

- templates/mega_hybrid_interface.html: Interface web moderna

- static/css/style.css: Estilos personalizados

Configuracao e Setup:

- requirements.txt: Dependencias atualizadas

- setup.bat: Instalador Windows

- setup.sh: Instalador Linux/macOS

- .gitignore: Configuracao completa

Documentacao Completa:

- README.md: Documentacao detalhada (400+ linhas)

- QUICK_START.md: Guia de inicio rapido

- PROJECT_STRUCTURE.md: Estrutura do projeto

- PROJETO_RECRIADO.md: Resumo da recriacao

- LICENSE: Licenca MIT

Funcionalidades Implementadas:

- Clonagem completa de sites web

- Sistema de login automatico

- Captura de screenshots

- Download de assets (CSS, JS, imagens)

- Monitoramento em tempo real

- Controles: pausar, retomar, cancelar

- Banco de dados SQLite

- Relatorios em JSON

- Interface web responsiva

- API RESTful completa

Limpeza:

- Codigo antigo movido para _BACKUP_ANTIGO/

- Removido arquivos duplicados

- Removido projetos de teste antigos

- Estrutura limpa e profissional

Versao: 2.0

Data: 26 de Outubro de 2025

Status: Projeto completamente funcional e pronto para uso

BREAKING CHANGES: Refatoracao completa do projeto — data não informada\n  - `f00212b97694ef4f20db9ff9eaf1c63df848bda3` — chore: Remove arquivo .gitkeep da pasta de projetos

- Deletado o arquivo .gitkeep que não contém mais conteúdo relevante, mantendo a estrutura do repositório limpa e organizada. — data não informada\n  - `d9d937f53a762691625c247c21509d8e04d5422c` — feat: Adiciona novas classes CSS e melhorias na estrutura da interface

- Introduzidas novas classes CSS para estilização, incluindo utilitários de layout e cores.
- Refatoradas seções do HTML para utilizar as novas classes, melhorando a legibilidade e a manutenção do código.
- Atualizadas as referências de estilo para garantir consistência visual na interface. — data não informada
\n## 16. William-kelvem94/CONVERSOR-DE-FORMATO-DE-ARQUIVO

- **Registros retornados:** 3
- **Amostra:**
  - `3a0c9222f5238382749c31165c029ecbf3c13e89` — feat: Implementacao completa do motor de conversao real e funcional

Novas Funcionalidades:
- Motor de conversao hibrido: WebCodecs API + FFmpeg.wasm (fallback)
- Suporte para 50+ formatos reais (video, audio, imagem, documento)
- Sistema de cancelamento de conversao com AbortController
- Estimativa e tempo restante de conversao baseado no tamanho do arquivo
- Indicador visual do motor de conversao em uso (WebCodecs/FFmpeg/Image/Document)

Novos Formatos Suportados:
- Video: FLV, WMV, 3GP, M2TS, TS, VOB, ASF, RM, RMVB
- Audio: M4A, WMA, OPUS, AMR, AIFF, AU, RA, AC3, DTS
- Imagem: HEIC, HEIF, AVIF, SVG, ICO, WebP animado, APNG
- Documento: RTF, ODT, EPUB, PPTX para PNG/JPEG

Melhorias Tecnicas:
- Conversao completa de documentos preservando formatacao
- Conversao PDF para DOCX, DOCX para PDF, PPTX para PDF, XLSX para CSV
- Sistema de fallback inteligente (WebCodecs -> FFmpeg -> Erro)
- FFmpeg.wasm carregado localmente (sem dependencia de CDN)
- Validacao robusta de arquivos com tratamento de erros
- Sistema de notificacoes Toast para feedback ao usuario
- Error Boundary para captura de erros JavaScript

Arquitetura:
- Refatoracao completa em componentes modulares
- Custom hooks: useFileConversion, useConversionSteps, useFileUpload
- Componentes de passo: UploadStep, FormatStep, ProcessingStep, CompletedStep
- Store Zustand para gerenciamento de estado global
- Factory pattern para selecao inteligente do motor de conversao

Melhorias de UI/UX:
- Design moderno com glassmorphism e animacoes fluidas
- Avisos para arquivos grandes (>500MB)
- Progresso detalhado com tempo estimado e restante
- Botao de cancelamento durante conversao
- Preview melhorado para todos os formatos
- Remocao de estatisticas enganosas

Docker:
- Dockerfile multi-stage otimizado
- docker-compose.yml para desenvolvimento e producao
- Configuracao para porta 1000

Bibliotecas Adicionadas:
- heic2any, pdfjs-dist, pptxgenjs, xlsx, html2pdf.js
- pizzip, docx-preview, jszip

Seguranca e Qualidade:
- Validacao de tipos TypeScript rigorosa
- Tratamento de erros abrangente
- Limpeza de recursos (URL.revokeObjectURL)
- Validacao de entrada em todas as funcoes criticas — data não informada\n  - `59d741622afaf937e03295b471e90661a4ac0f92` — Add Electron desktop support and advanced conversion features

Introduces Electron integration for desktop builds with native FFmpeg support, including main and preload scripts, and Nextron configuration. Adds advanced conversion logic, batch conversion, file validation, error handling, and new UI components for file preview, loading spinner, and quality settings. Updates the README with desktop instructions, expands supported formats, and enhances the upload and format selection flows to support batch mode, preview, and advanced settings. Updates dependencies and scripts to support Electron and FFmpeg, and improves state management and conversion progress handling. — data não informada\n  - `42c8245361ca56db4f42e944f504718c4d9a29e1` — first commit — data não informada
\n## 17. William-kelvem94/CORETEMP-SOUNDPAD

- **Registros retornados:** 10
- **Amostra:**
  - `5a882983c5eef9661faf1b88993bc054bd8105f0` — AtualizaÃ§Ã£o completa: adiciona sistema de configuraÃ§Ã£o e logging, refatora formulÃ¡rio principal e remove arquivos de projeto desnecessÃ¡rios — data não informada\n  - `c7dd520abbabefe453fc91bcbf6a9debeda6c72f` — ALPHA 2.0 — data não informada\n  - `47b219df0bd73145ceea976a1bf63d06b35cd499` — Considerar versão Alpha 1.0
Tudo funcionando, falta ajeitar pequenos detalhes na interface — data não informada\n  - `ca2437438b9f656c10204ff5660d7ae8d232b36a` — quase pronto 2 - mas não ta autoredimensionvavel — data não informada\n  - `67dbd5d0d61c256a997b65de71841b852a73aa3e` — quase finalizado interface e funcionalidade — data não informada\n  - `32b35fdef17b537b8e74af93ce708221be6704db` — Funcionando monitoramento, falta detalhes na interface — data não informada\n  - `a302224e21af1a95ec60a10d45211dd242fb769d` — Funcionando monitoramento, falta detalhes na interface — data não informada\n  - `f06482b7d9fa9ce88d70458dff71e0abce783992` — Tentativa de correção da interface — data não informada\n  - `d100ceb4782577fe6a65aacbb6ee9c70b734b78f` — Atualizações — data não informada\n  - `50b5f1246140a2e941611ac4b6d388847ac895fc` — Initial commit — data não informada
\n## 18. William-kelvem94/Criador_de_audios

- **Registros retornados:** 74
- **Amostra:**
  - `1789c02129c2c75f7a1e1807962467cd215e9b35` — [Infraestrutura e Correções Profundas PT-BR]

- Corrigido bug crítico de import (Boolean) no backend-service/models/database.py
- Ajustes em requirements.txt do backend-service: removido travamento em numpy/librosa/TTS, pip agora resolve automaticamente versões de compatibilidade para stack de áudio e IA
- Dockerfile backend-service alterado para garantir instalação correta de dependências
- docker-compose.yml, healthcheck, scripts e arquivos front-end/monitoramento ajustados
- Adicionados arquivos do monitoring-service e database.py ao versionamento
- Contextualização: stack migrada para ambiente completamente compatível Docker Compose com microserviços, build auditado e documentado, prioridade para boot local OK
- Arquivos do frontend e workflows .github reorganizados para maior manutenção futura

Esse commit marca uma virada estrutural: o backend-service finalmente compila e resolve suas dependências, pronto para testes e deploy.

TODO (após commit): finalizar build (pip), subir serviços, healthcheck detalhado e debug geral no backend+API+frontend.

Commit EXTREMAMENTE detalhado conforme solicitado, comentários e histórico todo em PT-BR, mantendo rastreabilidade completa da evolução do projeto.

# Conflicts:
#	services/backend-service/models/database.py — data não informada\n  - `1ee0c92aec51377e36615895cb45e428d2c6e8e2` — Add SQLAlchemy models for TTS backend

Introduce the database schema for the TTS backend service. Adds SQLAlchemy declarative models and enums to store audio synthesis history (AudioSynthesis), available voices (Voice), TTS models (TTSModel), voice cloning/training (VoiceClone), user preferences (UserSettings) and audit logs (AuditLog). Models include status enums, sensible defaults, timestamps, JSON fields for lists/metrics, and common synthesis/training fields to support result storage, model/voice management, cloning workflows and auditing. — data não informada\n  - `d302b813f8be06591040786cf4a21f2840adf370` — Merge pull request #1 from William-kelvem94/copilot/create-audio-generation-cloning-system

Implement complete TTS system with voice cloning, emotion presets, and dual-mode UI — data não informada\n  - `a2d01fa084b560e4d53807e1046dac4dce3b249c` — Fix CI workflow to match actual project structure (services/ instead of src/)

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `a566fed771255774bbb5d39154683fbaa168c7fd` — Fix missing utils.ts file and add database_service import to audio endpoint

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `38a94e19eaa08e4218730597c0d1138376f4f352` — Update README with complete feature descriptions and quick start guide

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `c99df50e2a3ec948145b3371d7c59af2c482f0cc` — Add comprehensive documentation: installation guide, user guide, and API documentation

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `f19297f1b38ab418e14554d1e241110b8a13d0b3` — Add complete frontend structure with React Router, Zustand, and UI components

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `306ecd918740528951974c89ed95a2c9d26505a7` — Add models directory with audio and voice schemas, update gitignore

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `dea1c5c035d1fdb04b607d14ddf61e63fc773b71` — Add backend models, services and API endpoints for voice cloning and audio effects

Co-authored-by: William-kelvem94 <90722323+William-kelvem94@users.noreply.github.com> — data não informada\n  - `75fcd70899743efd46a2abdc625914f7524136a3` — Initial plan — data não informada\n  - `97478809e3b279131d73933e1fa22cf60e0fa0a1` — feat: Otimizacao completa da infraestrutura Docker e servicos

🔧 Backend Service (Dockerfile):
- Refatoracao completa com multi-stage build (base, builder, production, development)
- Adicao de usuario nao-root para seguranca
- Otimizacao de camadas Docker com cache de dependencias
- Configuracoes especificas para producao e desenvolvimento
- Healthcheck aprimorado e exposicao correta da porta 8000
- Labels informativos e metadados do servico

🌐 Frontend Service (Dockerfile):
- Simplificacao da configuracao Nginx movendo para arquivo separado
- Remocao de configuracao inline do nginx.conf
- Otimizacao de permissoes e estrutura de arquivos
- Manutencao do healthcheck e exposicao da porta 80

⚙️ Configuracoes do Docker Compose:
- Ajuste no nome do container do frontend para 'criador-audios-frontend-final-fixed'
- Correcao na referencia de volumes compartilhados

🔀 Nginx Configuration:
- Simplificacao drastica do arquivo nginx.conf
- Remocao de configuracoes HTTP globais desnecessarias
- Foco nas configuracoes essenciais do servidor
- Ajuste do proxy para backend usando host.docker.internal
- Manutencao dos endpoints /api/ e /health

🛠️ Script de Inicializacao (quick-start.ps1):
- Correcao na logica do switch statement
- Padronizacao do tratamento de acoes de desenvolvimento
- Melhoria na estrutura condicional do script

📝 Outros ajustes:
- Atualizacao do arquivo de configuracao do cSpell
- Correcoes menores no API Gateway
- Ajustes na interface React do frontend
- Adicao de novos arquivos de configuracao nginx

Esta atualizacao traz melhorias significativas em:
- Seguranca (usuario nao-root, permissoes adequadas)
- Performance (multi-stage builds, cache otimizado)
- Manutenibilidade (codigo mais limpo e organizado)
- Escalabilidade (configuracoes separadas por ambiente) — data não informada\n  - `f6a99e2bc6dcb0a1694fc5739b344bad47ce4887` — 🔧 Atualizações no Docker e melhorias na estrutura do Frontend

- **Docker Compose**: Alterado o serviço `frontend-service` para construir a imagem a partir de um Dockerfile em vez de usar uma imagem pré-construída do Nginx, permitindo uma configuração mais flexível e personalizada.
- **Dockerfile do Frontend**: Implementada uma nova abordagem de multi-stage build, utilizando Node.js para construir a aplicação antes de servir os arquivos estáticos com Nginx, melhorando a eficiência do processo de build.
- **Frontend**: Atualizações no `index.html` para incluir um favicon e ajustes na estrutura do projeto, removendo código desnecessário e preparando a aplicação para uma melhor performance e manutenção.

Essas mudanças visam otimizar o processo de desenvolvimento e a entrega do frontend, alinhando-se com a nova arquitetura de microserviços. — data não informada\n  - `502409f686afe0d775f046e5005e659ae5bf67d1` — 🔧 Atualizações no Makefile e configuração do Nginx

- **Makefile**: Ajustados caminhos para os serviços frontend e backend, garantindo que os testes, formatação e linting sejam executados corretamente nos novos diretórios de microserviços.
- **Nginx**: Alterado o `server_name` para `localhost` e `api.localhost` para desenvolvimento, além de atualizar os certificados SSL para uso em ambiente de desenvolvimento.

Essas mudanças visam melhorar a estrutura de desenvolvimento e garantir que as configurações estejam alinhadas com a nova arquitetura de microserviços. — data não informada\n  - `8c4c23a974de84cb834688920200acdc399cdbdf` — 📋 ROADMAP DETALHADO v3.0 - Migração Completa para Microserviços Enterprise

🎯 MILESTONE ALCANÇADO: Arquitetura de Microserviços Enterprise Finalizada

🏗️ MIGRAÇÃO MONUMENTAL CONCLUÍDA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ ARQUITETURA TRANSFORMADA:
• DE: Monolito disfarçado com containers acoplados
• PARA: 6 Microserviços Independentes e Especializados

🌐 MICROSERVIÇOS IMPLEMENTADOS (100% FUNCIONAIS):

1️⃣ API GATEWAY SERVICE (porta 8000)
   • Roteamento inteligente entre serviços
   • Rate limiting avançado (100 req/min)
   • Autenticação JWT centralizada
   • Circuit breaker para resiliência
   • Load balancing automático
   • Health checks unificados

2️⃣ BACKEND SERVICE (via gateway)
   • Lógica de negócio core (FastAPI + SQLAlchemy)
   • Gerenciamento completo de projetos de áudio
   • Controle de usuários e permissões (RBAC)
   • Integração com TTS e File services
   • Cache inteligente com Redis
   • API versioning (v1/)

3️⃣ TTS SERVICE (via gateway)
   • Síntese de voz especializada (Coqui TTS + PyTorch)
   • Otimização automática GPU/CPU
   • Cache de modelos em memória
   • Streaming de áudio em tempo real
   • Compressão automática de arquivos

4️⃣ AUTH SERVICE (porta 8001 interna)
   • Autenticação independente e segura
   • JWT com refresh token rotation
   • Hash bcrypt para senhas
   • Controle de sessões Redis
   • Role-based access control

5️⃣ FILE SERVICE (porta 8002 interna)
   • Gerenciamento inteligente de arquivos
   • Upload até 50MB com validação
   • Streaming otimizado de downloads
   • Compressão automática
   • Preparado para CDN

6️⃣ FRONTEND SERVICE (porta 3000)
   • SPA moderna React + TypeScript + Vite
   • Interface responsiva com shadcn/ui
   • Player de áudio integrado
   • Upload drag-and-drop
   • Real-time feedback

🐳 INFRAESTRUTURA DOCKER COMPLETA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Imagens especializadas para cada microserviço
• Perfis Docker Compose otimizados (dev/prod/staging)
• Makefile unificado com 20+ comandos
• Deploy independente por serviço possível

📊 MONITORAMENTO ENTERPRISE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Prometheus + Grafana dashboards completos
• Métricas: latência (<10ms), throughput, erros
• Logging unificado e estruturado
• Health checks automáticos

🔒 SEGURANÇA MULTI-CAMADAS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Autenticação JWT em todos os serviços
• Rate limiting inteligente
• HTTPS obrigatório em produção
• Input validation rigorosa
• CORS configurado

🚀 PERFORMANCE CONQUISTADA:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• API Gateway: <10ms latência média
• TTS Service: <2s para síntese de 30s
• Throughput: 1000+ req/min
• Uptime: 99.9% com circuit breaker

🧪 QUALIDADE E TESTES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Cobertura ~70% com testes unitários/integração/e2e
• CI/CD completo com GitHub Actions
• Linting e formatação automática
• Type safety com TypeScript + mypy

📋 STATUS ATUAL DO PROJETO:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎉 CONQUISTADO (90% COMPLETO):
• Arquitetura de microserviços enterprise-grade
• Escalabilidade horizontal verdadeira
• Resiliência máxima com isolamento de falhas
• Performance excepcional
• Monitoramento e observabilidade completos

⏳ PENDÊNCIAS (PRÓXIMOS 2-3 DIAS):
• Testes de integração entre serviços (70% → 100%)
• Configuração produção final (80% → 100%)
• Documentação API completa (60% → 100%)

🚀 PRONTO PARA:
• Deploy em produção zero-downtime
• Escalabilidade para milhões de usuários
• Evolução contínua com novas funcionalidades
• Integração com Kubernetes e cloud providers

🏆 RESULTADO FINAL:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sistema de síntese de voz com arquitetura de microserviços
moderna, escalável e enterprise-grade, pronto para competir
com soluções comerciais de ponta!

📅 Data: 16 de dezembro de 2025
🏗️ Versão: v3.0 - Microserviços Enterprise — data não informada\n  - `1fc60bd6d643e35a9bb56035bdfc7e5138da68a4` — 🚀 [v3.0] Migração Completa para Arquitetura de Microserviços Enterprise

## 🎯 **GRANDE MIGRAÇÃO REALIZADA**
Transformação completa do monolito em **6 microserviços independentes e escaláveis**

### 📜 **ARQUITETURA IMPLEMENTADA**

#### 🏗️ **Microserviços Core (6 serviços)**
- **🌐 Frontend Service**: React 18 + TypeScript + Vite (porta 3000)
- **🔐 API Gateway**: FastAPI com rate limiting inteligente (porta 8000)
- **🛠️ Backend Service**: Lógica de negócio com SQLAlchemy
- **🤖 TTS Service**: Síntese especializada com Coqui TTS + PyTorch
- **🔑 Auth Service**: Autenticação independente com JWT + bcrypt
- **📁 File Service**: Gerenciamento de arquivos com streaming

#### 🐳 **Infraestrutura Docker Avançada**
- **Perfis especializados**: dev, prod, staging, monitoring, microservices
- **Orquestração otimizada**: 30+ comandos no Makefile
- **Imagens especializadas**: Dockerfile por serviço
- **Configuração adaptativa**: Detecção automática de GPU/CPU

#### 💾 **Banco de Dados & Cache**
- **PostgreSQL**: Dados relacionais otimizados
- **Redis Cluster**: Cache distribuído ultra-rápido
- **Monitoramento**: Prometheus + Grafana dashboards

#### 🔒 **Segurança Enterprise**
- **Autenticação multi-camadas**: JWT + bcrypt + refresh tokens
- **Rate limiting inteligente**: 100 req/min por IP
- **Circuit breaker**: Proteção automática contra falhas
- **HTTPS obrigatório**: Em produção

#### 📊 **Observabilidade Completa**
- **Métricas em tempo real**: Latência, taxa de erro, utilização
- **Dashboards Grafana**: Visão geral + performance por serviço
- **Logs unificados**: Estrutura de logging consistente
- **Health checks**: Monitoramento contínuo de saúde

### 🔄 **REFATORAÇÃO MASSIVA REALIZADA**

#### 📤 **ARQUIVOS REMOVIDOS (167 arquivos)**
- `app/` - Estrutura monolítica antiga
- `backend/` - Backend único removido
- `frontend/` - Frontend antigo removido
- `server.py` - Servidor único removido
- Dockerfiles antigos e configurações obsoletas
- Scripts de inicialização antigos

#### 📥 **NOVA ESTRUTURA CRIADA**
- `services/` - 6 microserviços independentes
- `docker/services/` - Dockerfiles especializados
- `config/` - Configurações por ambiente
- `docs/` - Documentação completa
- `scripts/tools/` - Ferramentas de automação

#### 🔧 **ARQUIVOS MODIFICADOS**
- `.env.example` - Variáveis para nova arquitetura
- `docker-compose.yml` - Orquestração completa
- `pyproject.toml` - Dependências atualizadas
- `Makefile` - 30+ comandos otimizados
- `tests/` - Testes atualizados para nova estrutura

### 🚀 **FUNCIONALIDADES IMPLEMENTADAS**

#### ⚡ **Performance Otimizada**
- **GPU Detection**: Configuração automática GPU/CPU
- **Cache inteligente**: Redis para modelos TTS
- **Load balancing**: API Gateway distribuindo carga
- **Circuit breaker**: Isolamento de falhas

#### 🔧 **Desenvolvimento Acelerado**
- **Hot-reload**: Desenvolvimento com recarga automática
- **Debugging**: Logs específicos por serviço
- **Testes paralelos**: Unitários + integração + e2e
- **CI/CD completo**: Build, test, deploy automático

#### 📦 **Deploy Estratégico**
- **Ambientes isolados**: dev/staging/prod independentes
- **Zero-downtime**: Deploy sem interrupção
- **Auto-scaling**: Escala automática por demanda
- **Backup automatizado**: Dados seguros

### 📈 **MÉTRICAS DE SUCESSO**

#### 🎯 **Performance Alcançada**
- **API Gateway**: <10ms latência média
- **TTS Service**: <2s síntese de 30s áudio
- **Escalabilidade**: Horizontal infinita
- **Resiliência**: Isolamento total de falhas

#### 📊 **Qualidade do Código**
- **Arquitetura**: Microserviços enterprise-grade
- **Testes**: Cobertura completa (unit + int + e2e)
- **Documentação**: README + arquitetura + APIs
- **CI/CD**: Pipeline completo automatizado

### 🎉 **RESULTADO FINAL**

**🏆 Sistema preparado para milhões de usuários com arquitetura enterprise!**

#### ✅ **Benefícios Conquistados**
- **Escalabilidade infinita** com Kubernetes pronto
- **Resiliência máxima** com isolamento de serviços
- **Performance otimizada** com GPU/CPU adaptativo
- **Manutenibilidade** com serviços independentes
- **Observabilidade completa** com métricas em tempo real

#### 🚀 **Próximos Passos Preparados**
- Kubernetes manifests prontos
- CDN integration preparada
- Multi-region deployment
- Machine Learning avançado
- Cloud providers (AWS/GCP/Azure)

### 🏷️ **TAGS E VERSÃO**
- **Versão**: 3.0.0
- **Arquitetura**: Microserviços Enterprise
- **Compatibilidade**: Python 3.10+, Docker 20+
- **Licença**: MIT

---

**💪 Migração histórica concluída com sucesso! Sistema agora enterprise-ready! 🚀** — data não informada\n  - `32a1255ec3b546678c4544b9867b172499f950d8` — Remover commit_msg.txt (arquivo temporário de mensagem de commit) — data não informada\n  - `e7ca757cd324a9b8b9a23eb57caed2de07d476f9` — ﻿Servir frontend estático e ajustar healthcheck/porta do Docker

Descrição:
- Monta os arquivos estáticos do frontend em / via app/main.py (StaticFiles -> frontend/dist), permitindo servir index.html e assets diretamente. Corrige 404s na UI.
- Substitui o healthcheck que dependia de curl por um healthcheck em Python em docker-compose.yml (evita falha quando curl não está presente na imagem).
- Mapeia a porta do host para 9000:8000 em docker-compose.yml para acesso consistente à aplicação em http://localhost:9000.

Testes realizados:
- Rebuild e restart do serviço app localmente; index.html retornou HTTP 200.

Observações:
- Se preferir porta diferente (ex.: 1000), alterar docker-compose.yml e reiniciar o serviço. — data não informada\n  - `6a5a28ea3bb6b04e1ba25f04a0811fac59ab9ce9` — Add Docker orchestration scripts and update configs

Introduces start-docker.bat and start-docker.sh scripts for easier Docker orchestration on Windows and Linux. Updates Dockerfile and docker-compose.yml to unify backend and frontend deployment, adds config.env.example for environment configuration, and enhances frontend Vite config for improved development and proxy support. — data não informada\n  - `038ff43dd5c9019e6514e53128dfb29e35467051` — Add legacy API routes and update paths

Introduces app/api/legacy.py with legacy-compatible endpoints for synthesis, voice cloning, voices, history, and advanced features to align with the current frontend. Updates settings.py to use PROJECT_ROOT for audio and voices directories. Registers the legacy router in main.py for root-level compatibility routes. — data não informada
\n## 19. William-kelvem94/crud_basico

- **Registros retornados:** 1
- **Amostra:**
  - `1557bc49371c34f1d0fa24e11b8d030a3dfbf5ce` — primeiro commit — data não informada
\n## 20. William-kelvem94/crud_basico-2.0

- **Registros retornados:** 1
- **Amostra:**
  - `1557bc49371c34f1d0fa24e11b8d030a3dfbf5ce` — primeiro commit — data não informada
\n## 21. William-kelvem94/CRUD_BASICO-3.0

- **Registros retornados:** 1
- **Amostra:**
  - `1557bc49371c34f1d0fa24e11b8d030a3dfbf5ce` — primeiro commit — data não informada
\n## 22. William-kelvem94/CRUD_BASICO4.0

- **Registros retornados:** 1
- **Amostra:**
  - `1557bc49371c34f1d0fa24e11b8d030a3dfbf5ce` — primeiro commit — data não informada
\n## 23. William-kelvem94/CRUD_VENDAS_WILL

- **Registros retornados:** 2
- **Amostra:**
  - `42815292b80db98f727bcf2b1e37e35b9d064128` — Add files via upload — data não informada\n  - `19a6bbbd8448c3b8443ac1f746b7cee7ffdd7265` — Initial commit — data não informada
\n## 24. William-kelvem94/DEEP-LEARNING

- **Registros retornados:** 12
- **Amostra:**
  - `de3cf52e7310f35fa5e43dbc9f109c4e5c831227` — feat: implement full-stack architecture with WebSocket chat interface, system monitoring, and configuration management — data não informada\n  - `944d439c6da0f9ba262c33c6ab9056562d45c46b` — feat: implement core agent architecture, websocket API, and frontend dashboard for JARVIS system — data não informada\n  - `62f4c4aa370fe39ddac7f85d2dcbc4b09926e339` — feat: implement REST API routes for chat, RAG, evolution, and system monitoring with initial frontend scaffolding. — data não informada\n  - `b01061e8009e7df50fa06d274a0de898c9d9a797` — feat: initialize SQLite database for Jarvis data storage — data não informada\n  - `603d0bfade8227d2fe625ea83b238c7ad34dfc0f` — feat: aprimorar validação e sanitização de dados no sistema de memória e agente — data não informada\n  - `b9a53a0b136e67d05b12b2c2118fe9bd5849732f` — feat: implement REST API routes and core agent/LLM logic for system management — data não informada\n  - `268420fbdc8ccb52d5175555285d6bf83e368353` — feat: implement core frontend UI, REST API routes, and LLM integration architecture — data não informada\n  - `846ffb776f7a6e74f8396e6d383ab468da48ae73` — feat: atualizar README.md com objetivos, métricas e instruções de instalação detalhadas — data não informada\n  - `57a0a09496b6a6055631a0a88e39589ae780985f` — feat: implement initial frontend UI with glassmorphism styling and backend API route structure — data não informada\n  - `d1db39c004dd2b224855e547d2d3164bea774461` — feat: implement local LLM brain, self-evolution engine, and configuration wizard for autonomous agent management — data não informada\n  - `101ae7956e55e49a069f133b17f23a304ecaa133` — chore: revisão e ajustes no projeto Jarvis - correção de inconsistências e sugestão de testes — data não informada\n  - `3575b77b7831ffd63cc344322f710c504a14a589` — first commit — data não informada
\n## 25. William-kelvem94/DEEPSEEK-JARVIS-LOCAL

- **Registros retornados:** 1
- **Amostra:**
  - `c72a33ae1b7b8cb307ae0b72443b588a02e0511b` — ✨ Inicializa repositório sem binários pesados — data não informada
\n## 26. William-kelvem94/DeepSeek-V3---C-PIA

- **Registros retornados:** 47
- **Amostra:**
  - `2f7b80eecebf3d1c84da5a0d465f6639ea175012` — Merge pull request #611 from Konano/chore-stale

chore: add stale issue management configuration — data não informada\n  - `76d8d39560032fc85c67950e29550868e128b6c5` — chore: add stale issue management configuration — data não informada\n  - `5ee97a83f0457d0d805b862aeb387358e1801e6d` — fix comment — data não informada\n  - `1d7d440461e9db6051174d2d1c54db3c41f89935` — Merge pull request #432 from luislh-dev/main

remove redundant asterisks in README — data não informada\n  - `09d108620abb9dd5392fc5f8d3c229f8498fcace` — Merge pull request #440 from spenserblack/main

Add syntax highlighting to requirements code block — data não informada\n  - `d0f8c4fca360922395e8508e3b84327c5c2b07bc` — Merge pull request #528 from WSL0809/main

Fix table bold formatting in TriviaQA EM comparison — data não informada\n  - `87a01053e4a1cadb483861bfeb146e334378e3e7` — Merge pull request #556 from XxAlonexX/main

Fix Linear Layer Bias Initialization — data não informada\n  - `a157077c611884f870f02307c746fa4a4b5a3e62` — Merge pull request #408 from fitzjalen/refactor

Clarify assertion errors — data não informada\n  - `c32c957fb092cbc1af629307cfe458d772496f89` — Merge pull request #364 from Dhie-boop/feature/table-of-content

Add table of contents to README for better navigation — data não informada\n  - `6a30b43249a5710a3adb18c11763222d3fca8756` — Fix Linear Layer Bias Initialization — data não informada\n  - `97b35f1fcadf435b41a835d5f4e86c8d9dc4497b` — docs: remove redundant asterisks in note — data não informada\n  - `d5c08b384b4d4096e494d61ba7d329f593116872` — Update README.md

fix(table): correct bold formatting for TriviaQA EM comparison

- Remove redundant bolding on LLaMA3.1 405B (82.7)
- Retain single bold style for DeepSeek-V3's highest score (82.9)
- Aligns with evaluation convention of highlighting only the best performance — data não informada\n  - `760d22821fa8d019cd63fb4a986dc4c48f4bee49` — Add syntax highlighting to requirements code block — data não informada\n  - `6784e1976df5e5ebdff031523384807b992992f4` — Fix TOC links to correctly link to headings in Markdown — data não informada\n  - `2756e130c2430eedc916ca331f5e360b519ed7ab` — clarify assertion error — data não informada\n  - `ddc501b80e812f05a4237514c592f286554f2a11` — Add table of contents to README — data não informada\n  - `b5d872ead062c94b852d75ce41ae0b10fcfa1c86` — Merge pull request #341 from enochkan/main

docs: Add system requirements for DeepSeek-Infer demo — data não informada\n  - `53d8dc9966be4fa2629f7191a782311eb6b7e50c` — docs: Update system requirements with GitHub Markdown callout — data não informada\n  - `722e6885ef02adcbbc4e5cb55ecc848087d60b77` — docs: Improve system requirements section formatting — data não informada\n  - `53b055bc1e6e9de307b7c72ff2afd0b6d18e865a` — docs: Add system requirements for DeepSeek-Infer demo — data não informada
\n## 27. William-kelvem94/demandas-organizadas

- **Registros retornados:** 76
- **Amostra:**
  - `a6a84c9d637225eeb217af5428d2d705cb6ecbdb` — docs: align repo map with renamed repositories — data não informada\n  - `7f45ff4ddcea698abb7f7e22d0d59a95523d09ac` — docs: reorganize repo as umbrella line — data não informada\n  - `7c80f779f7b8f8b89ce97bb0e30cda9d71ff7d6c` — Correções automáticas: permissões, OpenSSL, dependências atualizadas, comentários em português — data não informada\n  - `0c5295b30f7bd3a38b3bbdd7a7edffaae5bd36c9` — PROJETO VALIDADO: Correções finais - variáveis .env, loops resolvidos, lint corrigido, backend estável — data não informada\n  - `4078752eb001f3bf7e3fcc04ee18e590f8f62c61` — Correções: migrations, Jest ESModules, Babel, .env, await, lint e segurança. Detalhes: - Checagem de colunas nas migrations; - await correto; - preset Babel-Jest; - placeholders .env destacados; - imports/lint ajustados; - sintaxe corrigida. — data não informada\n  - `9a79260d67d4c6dd616627bfdb63d04e7710b021` —  REFATORAÇÃO COMPLETA - Sistema 100% corrigido e otimizado

 PRINCIPAIS MELHORIAS:
-  Backend index.js recriado do zero
-  Dependências atualizadas e vulnerabilidades corrigidas
-  Multer atualizado para v2.0.2 (seguro)
-  Middleware premium refatorado
-  Logger Winston otimizado
-  Configurações .env padronizadas
-  Package.json limpos e organizados
-  Frontend com React 18 e dependências atuais
-  README completo com instruções claras
-  Estrutura de arquivos organizada
-  Zero vulnerabilidades de segurança
-  Compatibilidade Node.js 18+

 CORREÇÕES TÉCNICAS:
- Arquivo index.js principal restaurado
- Rate limiting configurado
- Logs estruturados implementados
- CORS adequadamente configurado
- Headers de segurança aplicados
- Graceful shutdown implementado
- Socket.IO integrado
- Métricas de performance

 RESULTADO: Sistema totalmente funcional e pronto para produção! — data não informada\n  - `53105c0081de348666149b39d286de3f5a65d771` — Backup before complete refactor — data não informada\n  - `68878463f029b35ba5d990351aba0a2a9a9900c9` — feat: projeto completo com interface frontend e backend funcionando

- Interface completa no Docker (porta 3000)
- Backend API rodando (porta 4000)
- Banco PostgreSQL configurado (porta 5432)
- Redis para cache (porta 6379)
- Adminer para gerenciamento do banco (porta 8080)
- Projeto pronto para produção
- Arquivos duplicados removidos
- Estrutura limpa e organizada — data não informada\n  - `e726db28db5c1774b265d6bd1a0285db08610d85` — feat: atualizações completas do projeto para produção — data não informada\n  - `b2660515a8ee04ed6567017bd192db289d378c32` — Organização completa do projeto: estrutura profissional, documentação, scripts e configs otimizados — data não informada\n  - `b6d94b6c2ca5825145d34ecbcaaef304d91dd7e5` — Subindo todo o projeto para o GitHub: versão inicial completa, incluindo backend, frontend, integrações, scripts, documentação, configurações de docker e dependências. Estrutura organizada conforme demanda do sistema WEBFLASH. Data: 02/09/2025. — data não informada\n  - `a776b5f2fb53e5b6b9b4d02a5f617bd3cd560ee0` — feat(documentacao): adiciona dashboard interativo para análise de problemas do projeto — data não informada\n  - `b3cefeb07b81faea36b9823670149ee9f775c71a` — feat(seguranca): Reforça a segurança e corrige vulnerabilidades críticas

Esta atualização aborda várias vulnerabilidades de segurança críticas e melhora a robustez geral do projeto, seguindo a auditoria técnica.

Principais mudanças:

- **Segredos Removidos:** Credenciais e chaves de API foram removidas do controle de versão.
  - **AÇÃO NECESSÁRIA:** As chaves expostas foram revogadas e substituídas por variáveis de ambiente.
- **Gerenciamento de Dependências:** Dependências de desenvolvimento (jest,
odemon) foram movidas para devDependencies para otimizar o build de produção.
- **Segurança do Backend:**
  - Adicionado helmet para proteger contra vulnerabilidades web comuns através de headers HTTP.
  - Implementado express-rate-limit para mitigar ataques de força bruta.
- **Segurança de Contêiner:** O Dockerfile foi atualizado para usar um usuário não-root, aplicando o princípio do menor privilégio.
- **.gitignore Aprimorado:** Arquivos sensíveis e de ambiente agora são ignorados pelo Git.
- **Relatório de Auditoria:** Adicionado um dashboard (ANALISE_PROJETO.html) com o detalhamento dos problemas e soluções aplicadas. — data não informada\n  - `991673fbfe57fef115a8124bae9f819d933a9531` — feat: substitui npm install por npm ci no Dockerfile para garantir instalação consistente de dependências — data não informada\n  - `6ca90338085b56b1a63ab18c058febafc3ccd9fd` — feat: Reorganização completa do projeto e implementação de funcionalidades premium

Esta é uma refatoração abrangente do projeto para uma estrutura mais organizada e a integração de funcionalidades premium.

Principais alterações incluem:

1.  **Reorganização da Estrutura de Pastas:**
    *   Criação de diretórios dedicados para `config/`, `database/`, `docs/`, `scripts/` e `credentials/`.
    *   Movimentação de arquivos de configuração (`docker-compose.yml`, `.env.production`, `client_secret_*.json`) para `config/`.
    *   Movimentação do banco de dados (`demandas.db`) para `database/`.
    *   Consolidação de toda a documentação (`.md`, `.txt`, `Anotações`, `RELATORIOS`) para a pasta `docs/`.
    *   Movimentação de scripts de automação (`start-docker.bat`, `start-docker.sh`, `test-docker.js`, `validate-docker.js`) para `scripts/`.
    *   Organização de arquivos de credenciais para `credentials/`.

2.  **Implementação e Refatoração de Funcionalidades Premium:**
    *   Atualizações significativas no `backend/` para integrar funcionalidades premium, incluindo:
        *   Refatoração do `backend/database.js` para usar Knex e suportar PostgreSQL em produção.
        *   Ajustes no `backend/Dockerfile` e `backend/docker-entrypoint.sh` para otimização e compatibilidade com Docker.
        *   Melhorias nos controladores (`authController.js`, `controleQualidadeController.js`) e middlewares (`premiumMiddleware.js`).
        *   Atualizações nas migrações (`migrations/`).
        *   Ajustes nas rotas (`routes/index.js`) para incluir novas funcionalidades e autenticação OAuth.
    *   Atualizações no `frontend/src/` para suportar as novas funcionalidades e componentes (`App.jsx`, `AuthContext.jsx`, `ControleQualidade.jsx`, `CriacaoAcesso.jsx`, `SuporteTecnico.jsx`, `api.js`).

3.  **Atualização de Configurações e Caminhos:**
    *   Ajustes em `backend/.env` e `backend/config/passport.js` para refletir as novas configurações de ambiente e OAuth.
    *   Atualização de caminhos internos em vários arquivos para se adequarem à nova estrutura.

Esta commit consolida todas as alterações de organização e implementação de funcionalidades, preparando o projeto para um ambiente de produção mais robusto e escalável. — data não informada\n  - `8a1579951b09c0c809cf5d0449851bacfc0e63fd` — feat: adiciona Dockerfile de teste com script de entrada — data não informada\n  - `62920adec4564345ceed698844ea7839c4dd2185` — feat: adiciona suporte ao cliente PostgreSQL e melhorias no script de inicialização — data não informada\n  - `dfd17738f13c0a367dbefaff9da36de46e60dd98` —  DEPLOY COMPLETO: Sistema Premium com Docker Ready para Produção

 PRINCIPAIS MELHORIAS:

 DOCKERIZAÇÃO COMPLETA:
- Docker Compose multi-serviço (backend, frontend, PostgreSQL, Redis)
- Multi-stage builds otimizados para produção
- Health checks automáticos para todos os serviços
- Volumes persistentes para dados e logs
- Rede isolada entre containers

 ARQUIVOS DOCKER CRIADOS:
- docker-compose.yml: Orquestração completa dos serviços
- backend/Dockerfile: Build otimizado Node.js com Alpine
- frontend/Dockerfile: Build React + Nginx otimizado
- .dockerignore: Otimização de contexto de build
- docker-entrypoint.sh: Script de inicialização inteligente

 SCRIPTS DE AUTOMAÇÃO:
- start-docker.bat: Inicialização automática Windows
- start-docker.sh: Inicialização automática Linux/Mac
- validate-docker.js: Validação completa do sistema
- test-docker.js: Teste de conectividade dos serviços

 CONFIGURAÇÕES DE PRODUÇÃO:
- PostgreSQL 15 com SSL configurado
- Redis 7 para cache e sessões
- Nginx otimizado para servir React
- Variáveis de ambiente organizadas
- Backup e recovery configurados

 SEGURANÇA PREMIUM:
- Containers executam com usuários não-root
- Senhas configuráveis via environment
- Rede isolada entre serviços
- Headers de segurança configurados
- Rate limiting e validação rigorosa

 MONITORAMENTO AVANÇADO:
- Health checks com retry logic
- Logs centralizados e estruturados
- Métricas de performance em tempo real
- Alertas automáticos configurados
- Auditoria de segurança completa

 CONFIGURAÇÃO DE REDE:
- Frontend: http://localhost:3000
- Backend: http://localhost:39871
- Health check: /api/premium/health
- Proxy reverso configurado

 DOCUMENTAÇÃO COMPLETA:
- README.md: Guia completo atualizado
- DOCKER_README.md: Guia específico Docker
- Scripts de exemplo e troubleshooting
- Comandos úteis documentados

 PERFORMANCE OTIMIZADA:
- Build times reduzidos com cache
- Imagens Alpine para menor footprint
- Compressão gzip habilitada
- Cache estático configurado
- Connection pooling no PostgreSQL

 DEPLOY EM UM COMANDO:
npm start OU docker-compose up --build -d

 SISTEMA TESTADO E VALIDADO:
- Todos os serviços funcionando
- Health checks passando
- Conectividade verificada
- Performance otimizada
- Logs estruturados

 PRONTO PARA USO EM QUALQUER AMBIENTE! — data não informada\n  - `4f1c335170f539e0bcd7875a5ef0ef7f956c7313` — feat: adiciona comandos úteis para monitoramento, desenvolvimento, testes e debug — data não informada\n  - `46d9c2e4bccd42e07f1aa0a09bc4c6cd7c4e4e03` — feat: validação premium completa e processamento máximo garantido — data não informada
\n## 28. William-kelvem94/demandas-organizadas-v2-legacy

- **Registros retornados:** 60
- **Amostra:**
  - `d8f6455beed8caf5c6aee83c0c19e9579dcdc48f` — ci: dispatch scheduled copilot tests from main branch — data não informada\n  - `c363f0eae8ffbbd5bf2c7eef98037dbcab304e8d` — docs: add legacy status readme — data não informada\n  - `412179ba635658ee0d89dec8bcc8674f772cdbad` — Readiciona código e atualiza referências para William Kelvem Pereira — data não informada\n  - `b1c5cedf688f36df89ca101c3aa97ce337e6a2d4` — Atualiza autoria para William Kelvem Pereira e ajusta licença — data não informada\n  - `b110b1269f5fa29d88c6181a7800856c89f97284` — Limpeza massiva: remoção de arquivos e diretórios obsoletos/removidos — data não informada\n  - `6cbe4fc660916348bde67b918354ed3026a16c4d` — refactor: reorganizar SettingsPage com reducer e componentes — data não informada\n  - `ee94266c7873367712b2dc814ce781920897721c` — chore: salvar todas as alterações anteriores

Inclui:
- correção de endpoints no DashboardPage e ReportsPage
- importação de Loader2 nos componentes
- tratamento de erros e CORS em documentos
- novos testes para API de documentos
- ajustes visuais e lógicos em vários componentes

Estava restando muitos arquivos modificados; agora foi tudo commitado. — data não informada\n  - `d8f11c955c6bb9f9ca98388eb18a1a8dbea22ab1` — chore: remover DuckDNS e ngrok 🗑️

- comentários explicativos deixados como rascunho para possível reativação
- labels de Traefik apontando para domínio DuckDNS comentados
- serviço duckdns removido do compose
- bloco de resolver ACME em traefik.yml comentado
- variáveis de ambiente relacionadas ao DuckDNS/NGROK comentadas
- atualização do .env com explicações e tokens como referência

Este commit limpa a configuração externa; tudo permanece funcional
localmente e pode ser reativado com poucos ajustes. — data não informada\n  - `aa8a32b59d1b77e4ffdbba939e7cbcdfcb543aeb` — Merge branch 'main' of https://github.com/William-kelvem94/DEMANDAS_ORGANIZADAS_2.0 — data não informada\n  - `1e75c56e2f17d9eeac308cf20782af24622709ad` — feat: add TypeScript declaration for y-websocket module — data não informada\n  - `e1d500e0a08383f533935af771ba7caefc95cfa4` — 🔧 refactor: update hocuspocus service configuration and simplify frontend Dockerfile — data não informada\n  - `4884bd442400afc1d2dd4c6469a077a4f46f6b7a` — 🚀 feat: modernização completa do WillHub — stack 2026

✨ Novas Funcionalidades
- Adicionado Feature-Sliced Design no frontend (features/, shared/)
- Canvas colaborativo migrado para @xyflow/react 12 + HocusPocus
- Kanban reescrito com @dnd-kit (substitui react-beautiful-dnd)
- Dashboard com TanStack Query v5 e cards de KPI
- Relatórios com Recharts (gráficos de linha e barra) + exportar PDF
- SettingsPage com tema light/dark/system
- LoginPage e RegisterPage reescritos com Zod + React Hook Form
- Indicador de força de senha no cadastro
- QueryClientProvider centralizado em shared/lib/queryClient.ts

🔧 Melhorias de Infraestrutura
- docker-compose.yml: y-websocket substituído por HocusPocus (ueberdosis/hocuspocus)
- Criado pyproject.toml com uv, Ruff e pytest configurados
- .pre-commit-config.yaml com Ruff + ESLint + trailing-whitespace
- vite.config.ts: code splitting manual por chunk (react, xyflow, yjs, motion)
- .env.example atualizado com VITE_Y_WEBSOCKET_URL e senhas seguras

📦 Dependências Frontend Atualizadas
- @xyflow/react ^12.3.6 (era reactflow ^11)
- @hocuspocus/provider ^2.13.0 (era y-websocket)
- @dnd-kit/core, @dnd-kit/sortable, @dnd-kit/utilities
- @tanstack/react-query ^5.56.0 + devtools
- @tanstack/react-table ^8.20.0
- react-hook-form ^7.53.2 + @hookform/resolvers
- zod ^3.23.8
- recharts ^2.13.3
- zustand ^5.0.2
- vitest ^2.1.4 + @testing-library/react
- pnpm@9 como gerenciador de pacotes

🧪 Testes
- backend/tests/conftest.py: fixtures pytest com SQLite in-memory
- backend/tests/test_auth.py: registro, login, /users/me (5 casos)
- backend/tests/test_health.py: health check e OpenAPI
- frontend/vitest.config.ts: configuração de coverage com thresholds
- frontend/src/tests/setup.ts: setup @testing-library/jest-dom
- frontend/src/tests/LoginPage.test.tsx: 3 testes de componente

🤖 CI/CD
- .github/workflows/ci.yml: pipeline completo com
  - Backend: lint Ruff + pytest (com Postgres e Redis via services)
  - Frontend: ESLint + Vitest + type-check + build
  - Docker: build check dos dois Dockerfiles

🗂️ Stores & Lib Compartilhada
- src/store/useTenantStore.ts: NOVO — multi-tenant com zustand persist
- src/store/useAuthStore.ts: adicionado tenant_id ao tipo User
- src/store/useThemeStore.ts: suporte a tema 'system' (prefers-color-scheme)
- src/shared/lib/api.ts: axios melhorado com tipagem AxiosError
- src/shared/lib/yjs.ts: HocusPocus provider (substitui createYjsProvider)
- src/shared/lib/queryClient.ts: QueryClient com retry inteligente por HTTP status
- src/shared/lib/utils.ts: cn(), formatDate(), formatDateTime(), truncate()

📚 Documentação
- README.md reescrito: stack 2026, tabelas, 3 comandos para rodar
- CONTRIBUTING.md criado: guia completo de setup, testes, convenções, PRs
- PROJECT_STATUS.md atualizado: status real pós-modernização

BREAKING CHANGES:
- reactflow -> @xyflow/react (atualizar imports nos componentes legados)
- y-websocket -> @hocuspocus/provider (atualizar conexão Yjs)
- react-beautiful-dnd removido -> usar @dnd-kit — data não informada\n  - `55226cbcca195da6bb8907cb68cd8851b5106aac` — 🔒 Adicionado .gitignore básico (python, node, venv, etc) — data não informada\n  - `94006a90e04efe5701757f4125859baadff769d1` — 🧹 Removidos arquivos gerados e dependências rastreadas — data não informada\n  - `f3cfc63b4b0e8d96121decf78337b15dbe9152e7` — ✅ Atualizações amplas no backend e frontend 🚀 — data não informada\n  - `8dd913dd7c72799111edacfc68021d772ad63d67` — ✨ Commit completo e detalhado: ajustes gerais e melhorias — data não informada\n  - `37bb5a82db4cdb1f07ca4116dd2fd9b7fdeb3a25` — docker-compose: set web API_URL to api container — data não informada\n  - `0987677568e6e74670b846bc46b43813d908a883` — frontend: improve header styling, fix login errors, add proxy & router flags, correct DocsPage state — data não informada\n  - `cc9ce9d7af6f904da228fbbb5364c08fb190685f` — docker: optimize builds with cache mounts and .dockerignore; add admin env vars and display card — data não informada\n  - `6a234c48625b5fc239322f0720bb61d2ae0c7441` — 🎨 Atualiza branding para WillHub e corrige navegação do login — data não informada
\n## 29. William-kelvem94/demandas-organizadas-v3-experimental

- **Registros retornados:** 4
- **Amostra:**
  - `0411efbccda8dbe7f0fa536eca9d7bf28cc1429d` — chore: align package name with repository rename — data não informada\n  - `73d08ae49e7d931648ccf9bad8c095eb79f0760d` — docs: clarify repo role and legacy status — data não informada\n  - `4c67a61e83d78904e9004aea407798d27a185bb1` — feat: initialize FlowWorkspace AI Pro

Setup core project structure including React, Tailwind CSS, Vite configuration, and AI-powered task management state. — data não informada\n  - `8b533893227aa28ac99ee79590b06dcf6715e751` — Initial commit — data não informada
\n## 30. William-kelvem94/Dev.Finances

- **Registros retornados:** 1
- **Amostra:**
  - `52b6177165fae2e09d9ea722c82e4226a1dcfe84` — first commit — data não informada
\n## 31. William-kelvem94/DIA-DAS-MULHERES

- **Registros retornados:** 97
- **Amostra:**
  - `c18a0a80b3fe96e93136c42cc9929ff9573fdf36` — gera novo pacote offline com correções — data não informada\n  - `7b2701f0aed292dcb73868e923f0c3ab981de9ff` — corrige travamento do scroll causado pela timeline — data não informada\n  - `1850ad5d9faedc8de04dd0679d3dcc688213d316` — adiciona ferramenta para gerar pacote offline — data não informada\n  - `0214cf6afb4442064cd51ced2a41bb1f3e3f817f` — adiciona imagens webp otimizadas — data não informada\n  - `01d1fe14ac105076b3ce9011d8d9a96dfc11453b` — documenta build, imagens e toggle de partículas — data não informada\n  - `c80ef67877d5871a9185166d59003352488575b1` — remove app.js fonte não usado — data não informada\n  - `a93fd51d527f018987965d31f6b967cf0e166293` — evita fechamento da lightbox ao clicar em setas — data não informada\n  - `81d6e689c2cdca6dd7f4fb8e196f2f7efd9f3367` — oculta canvas durante scroll e reduz taxa de updates da barra — data não informada\n  - `1d14ca8015d1dd4d34dc86227aa47743221754af` — tornar listener de scroll passivo e cachear elementos — data não informada\n  - `a153954dee018b5cad49469b08570332c88c2c2c` — melhora lightbox: legenda visível, animação e corrige scroll/progress — data não informada\n  - `d906756e26b4758bd96e2a5bf19eb01a7a7b6e4b` — corrige persistência de legendas na galeria e limpa CSS — data não informada\n  - `394838523d2589ac76a3cdfed84f70d7bf43c7aa` — corrige legendas da galeria e lightbox + melhora desempenho de rolagem — data não informada\n  - `abd46a1eb1af065b2412155ed3830b14311413cb` — ✍️ Revisão ortográfica e de acentuação (PT-BR)

Correção textual completa em frases da página, mantendo o sentido original e o tom romântico.

Ajustes de acentos/cedilha em blocos de momentos, seção extra, galeria e carta; revisão das legendas curtas do mosaico. — data não informada\n  - `92da234e6349339db2436176f97ee95f658cc922` — 🚀 Força atualização real no GitHub Pages

Adiciona limpeza de Service Worker legado (/scripts/sw.js), registro robusto com update e bump de versão para evitar cache antigo persistente.

Atualiza versões para 20260308-9 e namespace de cache v10 para entrega imediata das melhorias. — data não informada\n  - `789208d6355f4254ac76bb1d8be4a032c7e6e521` — 🔄 Sincroniza ajustes finais de Service Worker

Inclui atualizações pendentes em sw.js e scripts/sw.js para manter comportamento de cache consistente entre as branches. — data não informada\n  - `84f415791b2135171aa8eedaed06f9f64496e09b` — 📝 Conteúdo novo adicionado sem remover o existente

✅ Mantido o conteúdo atual da página e adicionada seção complementar com frases extras da identidade do casal.

🎨 Mantida legenda elegante no mosaico com copy refinada e revisão de acentuação onde aplicável.

🧹 Arquivos formatados com Prettier e validados sem erros. — data não informada\n  - `06c50622692cdc8e325d071e612f67d579cd5924` — 🛠️ Correção completa de SW e áudio no navegador

✅ Service Worker: removido ponto frágil do cache.addAll, agora o preload é resiliente com Promise.allSettled e ignora falhas individuais sem quebrar instalação.

🔊 AudioContext: sons de reveal agora só iniciam após gesto real do usuário e com resume seguro, eliminando spam de bloqueio de autoplay no console.

🚀 Cache-busting atualizado para versão 20260308-7 e namespace de cache v8 para garantir entrega imediata das correções.

🧪 Validação local concluída: assets principais respondendo 200 na nova versão. — data não informada\n  - `dc2ec02ee379c2efa93765c31feb7750a29e72f4` — 🎯 Centralização corrigida + pente fino visual

✅ Corrigida a causa do desalinhamento no hero: reintroduzido bloco .hero-content e aplicado centralização estrutural com margin-inline auto nos elementos-chave.

📱 Melhoria de responsividade no topo com min-height em svh para manter composição centralizada em telas móveis com barra dinâmica.

🛡️ Cache-busting atualizado para v20260308-6 e nova versão do Service Worker, garantindo entrega imediata da correção sem versão antiga presa. — data não informada\n  - `80f366576aa8af6174dd999d792eae6f1e76d7bc` — 🎞️ Rodízio inteligente de fotos por contexto

🧠 Rodízio reformulado com pools temáticos por seção para manter coerência com cada texto dos momentos.

📸 Fotos novas distribuídas de forma balanceada entre os momentos, mantendo variedade sem perder narrativa.

🛡️ Cache atualizado novamente para garantir entrega imediata da nova lógica de rotação e fallback.

✅ Validação concluída: sem erros de arquivo e assets da versão 20260308-5 respondendo com 200 localmente. — data não informada\n  - `3806633ba7c257112f5c8ed6bcdfc055e580a373` — 🩹 Correção de imagens quebradas na galeria

✅ Fallback robusto no carregamento das fotos: WEBP -> JPEG codificado -> JPEG bruto, evitando blocos com alt 'Memória nossa' quebrado.

🧹 Tratamento de falha final no mosaico para remover itens inválidos em vez de exibir ícone quebrado.

🚀 Cache-busting reforçado com nova versão de assets e Service Worker para forçar atualização da lógica nova no cliente. — data não informada
\n## 32. William-kelvem94/Domni

- **Registros retornados:** 100
- **Amostra:**
  - `dbe6de9462dfce2f19f75df1819b77f455286af4` — fix(ui): compactar menu global de usuário e proteger viewports estreitas

- centraliza o contrato visual do menu de usuário para painel administrativo e Portal do Inquilino;
- limita largura e altura pelo espaço real da viewport, TopBar e navegação inferior;
- habilita scroll interno e overscroll contido quando a altura disponível é pequena;
- adiciona collision padding para impedir que o dropdown encoste nas bordas do PWA/mobile;
- reduz densidade vertical do perfil, itens, separadores e seção de aparência sem diminuir alvos de toque;
- coloca Aparência e seletor de tema na mesma linha para economizar altura;
- preserva perfil, configurações, atalhos, área do inquilino, segurança, logout e regras de autenticação existentes;
- aplica o mesmo contrato no Portal, evitando divergência visual entre contextos;
- adiciona E2E dedicado que abre o menu e valida viewport, BottomNav/Dock e scroll interno em toda a matriz responsiva;
- amplia a configuração Playwright para executar o contrato do menu junto da QA responsiva existente.

Correção aplicada diretamente na branch main, sem alterar regras de negócio, permissões, dados ou persistência. — data não informada\n  - `f105be0fb109aebe7afc0a3ee4d7c54ebc80e536` — Add TCC model and correction guide docs

Add two Word documents under docs/MUDANÇA DE SENTRY PRA GLITCHTIP: 'Modelo TCC - Monografia (1).docx' (TCC template) and 'O QUE CORRIGIR/Guia de Correcao TCC - Sentry para Glitchtip.docx' (correction guide for migrating references from Sentry to GlitchTip). These are documentation assets only; no code changes. — data não informada\n  - `a64a274e5a1a55db09770edcda634b028a086ccb` — fix(responsivo): consolidar modo tablet touch e densidade global

- cria um modo responsivo transversal para superfícies touch intermediárias entre 640px e 1280px, evitando que tablets em landscape sejam tratados automaticamente como notebooks apenas por cruzarem breakpoints lg/xl;
- preserva integralmente autenticação, RBAC, isolamento por tenant, rotas, APIs, persistência e regras de negócio, alterando somente composição visual e contratos de responsividade;
- mantém o BottomNav como navegação canônica em tablets touch mesmo acima de 1024px e oculta visualmente o Dock desktop nesse contexto, sem duplicar itens nem mudar a NAVIGATION_CONFIG;
- garante que o Cockpit de Gestão continue abrindo em tablets acima de lg e reserva corretamente o espaço inferior para a navegação de toque;
- troca a busca expandida da TopBar pela lupa compacta em tablets touch, mantendo a command palette desktop para ponteiro fino;
- torna grids globais de métricas, cards e conteúdo compacto sensíveis a capacidade de toque e orientação: duas colunas em tablet retrato e até três colunas em landscape, evitando fileiras excessivamente densas;
- recompõe os gráficos do Dashboard em tablet: gráfico principal em largura confortável e gráficos secundários em uma ou duas colunas conforme a orientação, eliminando a miniaturização observada em landscape;
- cria tratamento de viewport baixo para landscape, reduzindo apenas a geometria do chrome superior sem diminuir alvos de toque;
- amplia a matriz Playwright com 800x600, 1024x768 e 1280x800 como tablets touch reais, além dos cenários já existentes de mobile, tablet retrato, notebook, desktop e PWA;
- atualiza os testes de contrato para proteger o modo tablet touch, os marcadores semânticos da TopBar, os gráficos adaptativos e a matriz de QA multi-viewport.

Alteração aplicada diretamente na branch main como um único commit atômico, sem criação de branch auxiliar. — data não informada\n  - `7412672f464d216743f256adc7bd72abdca205e6` — test(calendario): proteger detalhe somente leitura antes de abrir registro — data não informada\n  - `c13b59a02b80b5173d8e4f3c05ac5524e1a50c11` — feat(calendario): abrir eventos em detalhe somente leitura antes da edição — data não informada\n  - `cb67c8efb47c070fa84540353236be5db072014f` — fix(calendario): corrigir tipagem dos indicadores e ação redundante da visão Dia — data não informada\n  - `f21cd98fd961b895f7e2bb68da465a19a1bd2e7b` — test(calendario): incluir agenda na matriz visual multi-viewport — data não informada\n  - `e990bf12e1db247eaf2adeee41386ece0907d17d` — test(calendario): proteger experiência diária, filtros e responsividade — data não informada\n  - `16d8b867114311fb81b0e95a229d26fe7270a285` — feat(calendario): transformar agenda operacional em experiência diária responsiva — data não informada\n  - `501070ca2445774def6b5a31a40df3eb5786fd87` — chore(responsivo): expor resultado do gate visual no commit

- publica status pending/success/failure da QA Visual Responsiva no SHA que disparou o workflow;
- mantém diagnósticos e bootstrap de baseline existentes;
- facilita validar a matriz autenticada sem depender de inspeção manual da aba Actions. — data não informada\n  - `d3a4491e744488dd09becc7dae42cd2b1ca0d80d` — chore(responsivo): evitar execução duplicada no bootstrap visual

- mantém a matriz completa no bootstrap de baseline, pois a própria geração já executa todas as asserções estruturais e autenticadas;
- executa o gate de comparação completo nas rodadas seguintes, reduzindo tempo sem reduzir cobertura. — data não informada\n  - `13b496371eaac58e972163df86efd295118be462` — chore(responsivo): oficializar comandos de QA visual e autenticada

- adiciona atalhos npm para auditoria estática, seed E2E, matriz Playwright, atualização controlada de baselines e runner completo;
- mantém os comandos existentes e não altera dependências nem runtime de produção. — data não informada\n  - `d125be5410793d3fd2d15367ee19e8c18cd523e9` — test(responsivo): fechar QA autenticada e regressão visual do Domni

- cria seed E2E isolado e bloqueado em produção com identidade única OWNER + inquilino vinculada a contrato ativo;
- valida o cenário dual-contexto sem reutilizar conta, senha ou banco de produção;
- torna a matriz Playwright autenticada obrigatória quando RESPONSIVE_REQUIRE_AUTH=true;
- amplia o gate de viewport para scroll horizontal global, conteúdo fora da tela e textos comprimidos;
- adiciona comparação visual por baseline em mobile 390, notebook 1366 e PWA 390, mantendo a auditoria estrutural em 320, 360, 390, 412, 768, 1366 e 1920;
- estabiliza screenshots com tema claro, reduced-motion, fontes carregadas e animações/transições neutralizadas;
- adiciona workflow dedicado por mudanças relevantes de UI/PWA/layout, com PostgreSQL efêmero e Chromium;
- permite atualização explícita dos baselines por workflow_dispatch e bootstrap inicial seguro;
- persiste somente screenshots de QA gerados no banco descartável, nunca dados reais;
- mantém diagnósticos Playwright como artefato apenas em falha e preserva integralmente regras de negócio e produção. — data não informada\n  - `8dbd3564602a695d72c4e9a701c6bd9375f63b1e` — feat(responsivo): consolidar hardening visual e matriz de QA multi-viewport

- cria contrato responsivo transversal com quebra segura de textos, limites de conteúdo, grids auto-fit e ações adaptativas para 320px até desktop amplo;
- reaproveita data-app-content no Portal autenticado e reforça contenção horizontal sem alterar autenticação, RBAC, APIs, schema ou persistência;
- padroniza métricas do Dashboard, Financeiro e Portal pela largura real disponível em vez de colunas fixas por viewport;
- evita compressão do cabeçalho de pagamentos abaixo de 380px e mantém vencimento, status e identificação legíveis;
- adapta ações dos cards de imóveis e inquilinos para uma coluna em 320px, duas a partir de 360px e três em cards realmente largos;
- melhora nomes, e-mails, documentos, endereços, valores e títulos longos com contrato explícito de quebra sem remover truncate onde ele é intencional;
- adiciona matriz Playwright dedicada para 320, 360, 390, 412, tablet, notebook, desktop e modo PWA standalone;
- cobre Dashboard, Imóveis, Inquilinos, Contratos, Financeiro, Relatórios, Configurações e Portal do Inquilino, além das superfícies públicas de autenticação;
- detecta scroll X global, conteúdo fora da viewport e textos comprimidos em colunas estreitas, anexando screenshots para inspeção;
- mantém credenciais E2E exclusivamente por variáveis de ambiente e pula superfícies autenticadas quando elas não são fornecidas, sem segredos hardcoded;
- cria scanner estático que bloqueia apenas padrões de alto risco nas telas críticas e registra padrões ambíguos como revisão para evitar correções mecânicas regressivas;
- adiciona runner único de QA responsiva que funciona localmente ou contra preview/produção sem depender de GitHub Actions recorrente;
- adiciona testes de contrato e documentação detalhada da auditoria, decisões preservadas e comandos de validação.

Implementação aplicada sobre o HEAD atual da branch main, preservando integralmente o commit simultâneo de overlays e busca global. — data não informada\n  - `36282d76e4ff0767a272de69299ccd6111addf91` — fix(ui): consolidar overlays responsivos e busca global

- corrige a busca global no PWA e no mobile com fullscreen real, sem herdar largura, centralização e limite de altura do modal desktop que geravam a superfície quadrada com margens;
- mantém a busca como command palette central e limitada em tablet/desktop, com uma única região rolável, safe areas, cabeçalho compacto e ações independentes para limpar e fechar;
- cria variantes canônicas e retrocompatíveis de Dialog (modal, large, sheet-mobile e fullscreen-mobile), mantendo modal como padrão para não alterar consumidores existentes;
- adiciona contrato transversal de overlays para limitar popovers, dropdowns, selects e alert dialogs ao viewport e às safe areas em navegador, PWA, landscape e tablets;
- remove o efeito colateral da regra global que transformava todo link textual em alvo de 44px e diferencia corretamente ponteiro fino de interfaces touch, preservando alvos mínimos de toque onde são necessários;
- substitui a transição global irrestrita por propriedades controladas, sem impedir componentes que já declaram animações próprias;
- preserva integralmente autenticação, rate limit e isolamento por tenant da busca global, sem alteração de schema, migrations, RBAC ou persistência;
- amplia candidatos da busca de forma limitada, adiciona ranqueamento por relevância e abre diretamente imóveis, inquilinos, contratos e manutenções quando existe rota canônica de detalhe;
- mantém pagamentos em /financeiro?search=... porque o módulo ainda não possui rota canônica /financeiro/[id], evitando inventar navegação inexistente;
- alinha a ordem do teclado à ordem visual agrupada dos resultados, impede índice negativo sem resultados e exibe estado de falha em vez de transformar erro em lista vazia silenciosa;
- adiciona testes de contrato para variantes responsivas, fullscreen PWA, safe areas, touch/mouse, redução de movimento, segurança da busca, ranking e existência das rotas de detalhe;
- documenta o novo padrão transversal para futuras telas e componentes.

Alteração aplicada diretamente na branch main como um único commit atômico, sem branch auxiliar. — data não informada\n  - `12dabec2382e543a1f900f27819c2432e599a50c` — fix(pwa): reforçar responsividade geral e corrigir overflow visual

- elimina o segundo padding horizontal do MainLayout e devolve largura útil às páginas protegidas em celulares e PWA;
- cria contrato transversal data-app-content para impedir filhos flex/grid de empurrarem a viewport em X;
- restringe scroll horizontal a componentes que o declaram explicitamente com data-app-scroll-x;
- reforça Card, CardHeader, CardContent e CardFooter com min-width 0 e max-width 100%;
- remove truncamento obrigatório dos títulos globais de Card, permitindo quebra natural quando o espaço é estreito;
- mantém as abas de Configurações como scroller local, com itens que não encolhem e snap de navegação;
- recompõe Saúde do sistema para empilhar status e ações em mobile sem esmagar texto;
- substitui grids rígidos do diagnóstico por auto-fit/minmax baseado na largura real disponível;
- permite até duas linhas em mensagens, status, métricas e registros antes de truncar conteúdo essencial;
- preserva comportamento compacto em tablet, notebook e desktop sem alterar APIs, permissões ou regras de negócio;
- amplia o contrato PWA de regressão e documenta a auditoria responsiva geral.

Alteração aplicada diretamente na branch main, sem branch auxiliar. — data não informada\n  - `acb14fadb6fd28c5d8dcfa2669e8452b815d67bd` — fix(portal): concluir compatibilidade segura da sessão residencial em produção

- mantém TENANT_JWT_SECRET dedicado como primeira opção quando válido, exclusivo e com entropia suficiente;
- preserva os fallbacks segregados de SOCKET_AUTH_SECRET, NEXTAUTH_SECRET e AUTH_SECRET para ambientes legados;
- adiciona SUPABASE_SERVICE_ROLE_KEY como última fonte server-only de alta entropia quando os segredos históricos de autenticação não atendem ao mínimo atual;
- aplica separação de domínio à fonte alternativa e nunca reutiliza literalmente a credencial do Supabase como chave JWT;
- mantém ausência total de segredo hardcoded e falha fechada se nenhuma fonte server-only segura estiver disponível;
- não altera User.role, senha, TenantContract nem sessões administrativas;
- reforça o teste de regressão e atualiza a documentação da autenticação do Portal.

Correção aplicada diretamente sobre a branch main após validação do health de produção. — data não informada\n  - `2b03c6acd28e6bb346faddf1a7a72142fa7d4809` — fix(portal): tolerar segredo residencial legado sem usar valor inseguro

- trata TENANT_JWT_SECRET presente porém incompatível como fonte inutilizável, em vez de derrubar imediatamente a autenticação do Portal;
- mantém o segredo dedicado como primeira opção quando ele possui entropia mínima e não reutiliza outros segredos de autenticação;
- quando o dedicado é legado, curto ou duplicado, deriva a chave residencial de SOCKET_AUTH_SECRET, NEXTAUTH_SECRET ou AUTH_SECRET com separação de domínio;
- nunca usa o segredo dedicado inválido e não introduz fallback hardcoded;
- mantém falha fechada quando nenhuma fonte alternativa segura está disponível;
- adiciona contrato de regressão específico para esse cenário de produção;
- atualiza a documentação da correção para refletir o comportamento validado no ambiente real.

Aplicado diretamente sobre a branch main, preservando as alterações concorrentes de UI já presentes no HEAD. — data não informada\n  - `66cba1c3a4392af5da77751f51956b8f7c3b1380` — fix(ui): tornar Cockpit móvel responsivo em qualquer viewport

- consolida um contrato responsivo único para o Cockpit de Gestão em navegador móvel, PWA, tablets e janelas intermediárias abaixo do Dock desktop;
- preserva integralmente as regras atuais de permissão e visibilidade de atalhos, inclusive o acesso completo de SUPERADMIN, sem alterar autenticação, autorização, rotas, APIs ou persistência;
- substitui visualmente a distribuição livre da grade por 4 colunas em telas estreitas, 5 colunas em celulares largos e 6 colunas em tablets e viewports intermediários, evitando rótulos quebrados e fileiras excessivamente espalhadas;
- adapta tablets e larguras entre 640px e 1023px para uma superfície flutuante limitada a 48rem, com margens reais, cantos completos, borda e contraste de card em vez de um sheet de ponta a ponta;
- cria tratamento específico para viewports largos e baixos, como 780x600 e 900x600, centralizando o Cockpit verticalmente, limitando a altura a min(90dvh, 34rem) e mantendo uma única área interna de rolagem;
- compacta seletor de espaço, ícones, gaps e rótulos apenas quando a altura disponível é curta, preservando alvos de toque e legibilidade;
- reforça a superfície no tema escuro para separar corretamente o Cockpit do backdrop e do conteúdo administrativo ao fundo;
- diferencia visualmente DevOps/Admin e Backup sem mexer no filtro de permissões, mantendo as ferramentas administrativas reconhecíveis quando existirem;
- mantém o comportamento original de celular em modo retrato e todas as safe areas do sistema;
- adiciona teste de contrato específico para proteger os breakpoints 4/5/6 colunas, o modo de baixa altura, a centralização do painel e a regra de SUPERADMIN;
- correção aplicada diretamente sobre a main como um único commit funcional, sem branch auxiliar e sem perda das alterações anteriores. — data não informada\n  - `179eca7d92e1e1fd88bfe44a866f8e6f3a0ace06` — fix(portal): recuperar autenticação no ambiente de produção

- mantém TENANT_JWT_SECRET como segredo dedicado e preferencial do Portal;
- amplia a compatibilidade controlada para derivar a chave residencial de SOCKET_AUTH_SECRET quando o segredo dedicado estiver ausente;
- preserva separação de domínio, sem reutilizar literalmente a chave de socket na assinatura JWT;
- rejeita TENANT_JWT_SECRET explicitamente configurado quando ele reutiliza qualquer segredo de autenticação conhecido;
- mantém o limite mínimo de entropia para qualquer segredo usado como fonte;
- atualiza a documentação de produção para refletir a estratégia de compatibilidade observada pelo health check.

Hotfix aplicado diretamente na branch main após validação do primeiro deploy. — data não informada
\n## 33. William-kelvem94/Empresa-de-Agentes

- **Registros retornados:** 5
- **Amostra:**
  - `da2cb34c067f778917375d6a6e7e03ab26fc8f13` — Add React Vite app scaffold, server and docs

Introduce a new React + TypeScript Vite application (shadcn + Tailwind) with UI components, configs (tsconfig, tailwind, vite, eslint, postcss), package.json and generated artifacts. Add a server folder (index.js, package.json), COPILOTX-WSL-SETUP.md documenting local CopilotX/WSL proxy setup, a zip export of the app, and update .gitignore to ignore server/node_modules. — data não informada\n  - `dace4e35daea0b46c1450b2242cd9df577c6b419` — Padronização e detalhamento: atualiza modelo de agentes, cria cultura, visão geral, e organiza README. Mais clareza, indicadores, interfaces, desafios, fluxos e onboarding! — data não informada\n  - `08340e3eae2e1fdf781093d988b6b8218a9bac26` — Adiciona .gitignore para ignorar o arquivo .env — data não informada\n  - `45570be2a1742979f5193e933096192c013c209b` — Add company docs, agent scripts & Discord

Add comprehensive company documentation and operational tooling: organizational docs (agentes/, fluxos/, estrutura.md, templates), operational guides for Discord and Pixel Agents, automation examples and checklists. Add Python agent implementations (operacional/scripts/*), Discord integration bots (discord_bot_empresa.py, bot_discord.py, discord_bot_teste.py, test_bot.py), utils_obsidian for pulling vault context, and pixel_agents_config.yaml mapping agents to their handler functions. Note: a .env with a hardcoded DISCORD_BOT_TOKEN was added — treat as sensitive, remove from repo and rotate the token; prefer environment variables for deployment. — data não informada\n  - `c7834d1a40614bc89474ebfcb1e184dc1b3f4b26` — Initial commit — data não informada
\n## 34. William-kelvem94/extra-o-de-ideias

- **Registros retornados:** 2
- **Amostra:**
  - `d06e777083893ced3d063fcf9cdbadaf49b49b25` — ✨ feat: Documentação completa e detalhada do Projeto Jarvis/Néctar

O repositório foi totalmente reestruturado e expandido com informações detalhadas:

📂 Organização de arquivos em estrutura modular na pasta \docs/\.
🧠 Especificação técnica do Motor de IA, Banco de Dados e Sincronização.
💻 Planos de engenharia para Desktop (Tauri/Rust) e Android (React Native).
📡 Detalhamento de integrações externas (WhatsApp, Alexa, Calendário).
📑 Criação do Índice Mestre para facilitar a navegação.
🧹 Limpeza da raiz do projeto para um ambiente profissional.

Este conjunto de documentos consolida a inteligência extraída do vídeo e do site oficial. — data não informada\n  - `6196cb1a5e6c35ee93fdadc0d1f71e58f765a69b` — Initial commit — data não informada
\n## 35. William-kelvem94/Extrator

- **Registros retornados:** 2
- **Amostra:**
  - `79e595a15705930ab852c2399a4b3b125740bf1c` — Atualiza projeto Extrator — data não informada\n  - `24623d6020e1bb608bb88cca687036b98476044d` — feat: add project documentation, extraction scripts, and set up mock server dependencies — data não informada
\n## 36. William-kelvem94/GAMMAAP

- **Registros retornados:** 3
- **Amostra:**
  - `4d76a2de5486919f54063b86f4ca78af7d5a9524` — fix: corrige loop infinito do container mongodb-backup

- Cria script de inicialização (init-backup.sh) para configurar cron corretamente
- Corrige expansão de variáveis de ambiente no docker-compose.yml
- Resolve erro 'bad minute' no crontab que causava reinicialização contínua
- Implementa validação e configuração adequada do agendamento de backups
- Adiciona criação do arquivo de log antes do tail para evitar erros
- Container agora roda estável aguardando horário agendado (padrão: 2h da manhã)

Mudanças técnicas:
- Novo arquivo: scripts/init-backup.sh
- Atualizado: docker-compose.yml (mongodb-backup service)
- Uso de script bash dedicado em vez de comando inline complexo
- Melhor tratamento de variáveis de ambiente no container — data não informada\n  - `b7ce183a1914108acfc40a8735e3e694b3518d92` — Refactor AI integration and enhance user authentication features

- Replaced OpenAI integration with Groq and Ollama for AI functionalities in the backend.
- Updated environment variables in docker-compose and README for new AI services.
- Added password recovery functionality using a security word in the authentication controller.
- Removed credits management from user model and related routes.
- Enhanced user registration to include a security word with validation.
- Updated frontend to support password recovery and improved user experience in registration. — data não informada\n  - `57eb2238f2c07b2b2c4a826be9a676f978bf7949` — first commit — data não informada
\n## 37. William-kelvem94/Gerenciador_Financeiro-4.0

- **Registros retornados:** 14
- **Amostra:**
  - `bc4cb2f8d7154fe4cfe5adc2cd2ed1e9a2a9d86e` — Create start-background.ps1 — data não informada\n  - `e43b71e34d83b34c273232901e982feb015d2d0a` — Add new feature to process user input

Implemented a function to handle and validate user input in the main application module. This improves input reliability and prepares the codebase for future enhancements. — data não informada\n  - `a2c387edd9a7b1e249e96179eb99f832e09d6242` — Create .env.firebase — data não informada\n  - `46dbd1741737ea125b74d5fe31787d1170272c18` — 90% FUNCIONAL, CONSIDERAR BETA 2

QUASE TUDO FUNCIONANDO — data não informada\n  - `338312119e2b14ec96f2a8f19d1507887a7ef6c1` — INTERFACE OK, Add new feature to user profile page

Implemented additional functionality on the user profile page, including support for editing user details and updating the profile picture. Refactored related components for better maintainability. — data não informada\n  - `cef1979674e35333d1c61c2ada0d005dc2d36569` — Atualizações — data não informada\n  - `6afeb1e92f1f245f69362d3e5ba6363ba0a00ccf` — Importação funcionando - parcialmente

o sistema ja está extraindo e importando dados bancarios do extrato do bradesco
aparecendo em transações com uma leve falha de identificação do banco
dashboard não funcionando — data não informada\n  - `81c9059c14a8787de0a9aec6dc433a172809f9b6` — Apenas backup

não tem nada funcionando — data não informada\n  - `d23fee9094961f9ad2c0d8bddc14bc550b8c430b` — Atualização do README.MD e algumas configs

Atualização do README.MD e algumas configs — data não informada\n  - `fea14ee004f5a900887c3f8393304fd5b531eb0f` — atualizações — data não informada\n  - `537475bcbc67f49129e75ae9adf221a5cf9bacbe` — Tela de transações implementada

conseguimos realizar registros manuais na tela de transações bem como visualizar o registro feito, interface basica funcionando, tela de transações funcionando e aparentemente registrando no banco de dados, seguindo agora para a dashboard — data não informada\n  - `af485204162bbc14338b04cf812ec9e8ad7e06b6` — Construção da tela de Transações

estou tentando recriar o backend que foi excluido por acidente por problemas de commit dentro do github desktop
e construindo a tela de Transações — data não informada\n  - `7273b272964afca7e031d4279ac38bc4c2986cb3` — Acesso básico funcional

Conseguimos andar pelas páginas ( funções ) do projeto
a interface está sem bugs, responsiva e simples porém aparentemente funcional para a navegação basica e geral do projeto — data não informada\n  - `f62f87931a2c91220bec6a59b8991840f618173d` — Initial commit — data não informada
\n## 38. William-kelvem94/Gerenciador_Financeiro-5.0

- **Registros retornados:** 100
- **Amostra:**
  - `ff710b51d5877516173d632507b5110d72944343` — refactor: enhance Dockerfiles for frontend and backend with improved build processes and security measures

This commit updates the Docker configurations for both the frontend and backend of the Will Finance application, transitioning to a more enterprise-ready setup. Key changes include:

- Refactored Dockerfile for the frontend to optimize build stages and improve caching.
- Enhanced backend Dockerfile with better dependency management and security practices, including the introduction of a custom entrypoint script.
- Added health checks and verification steps to ensure application stability.
- Removed obsolete migration files to streamline the database setup.

These updates aim to improve performance, security, and maintainability across the application. — data não informada\n  - `18ecd1659baab5391d30fbc5b6532b8530c0d553` — feat: upgrade to Will Finance 6.0 with enhanced Docker configurations and backend improvements

This commit introduces significant updates to the project, including the transition from version 5.0 to 6.0. Key changes include:

- Updated Docker Compose configuration for a production-ready setup, integrating PostgreSQL, Redis, and Nginx.
- Enhanced backend with improved user registration and login processes, including email validation and better error handling.
- Refactored frontend Dockerfile for optimized builds with React and Vite.
- Updated application constants to reflect the new version and name.
- Improved health checks and resource management in Docker configurations.

These changes aim to enhance performance, security, and maintainability across the application. — data não informada\n  - `438d769e09c2395fce38692d1cb9a95f3db961b2` — refactor: remove deprecated files and update project version to 6.0

This commit includes the deletion of obsolete Dockerfiles and the old docker-compose configuration, streamlining the project structure. Additionally, the project version has been updated from 5.0 to 6.0 in package.json, reflecting significant enhancements and refactoring efforts across the codebase. — data não informada\n  - `d0f3f70603a33e392b69e31936d1590a875027a8` — Fase 2: Refatoração dos hooks enterprise, início do sistema modular de middleware Zustand, correção de erros TypeScript e limpeza de arquivos conflitantes. Base para stores enterprise avançados. — data não informada\n  - `41d0593bae8ecbe236b22f18c50034d41d835602` — docs: Phase 1 completion documentation and Phase 2 roadmap — data não informada\n  - `4ffd2e2437f95eaf3539be2f54db822739ab1125` — feat: configure automated quality tools (Prettier + Husky + lint-staged) - Phase 1 complete — data não informada\n  - `ef0c67fb19e1830b392c9d3fe6964a9843a61a5a` — fix: ajustar permissões do script de deploy para 644 — data não informada\n  - `b427b3e1940707a43a2a0d24c615af4c52b3adc2` — Merge branch 'main' of https://github.com/William-kelvem94/Gerenciador_Financeiro-5.0 — data não informada\n  - `c7dafd59fba658e6a02a4a622a37acf8416b2501` — Commit completo: subida de todos arquivos do projeto, incluindo client, server, scripts, infra, documentação e configs. Estrutura enterprise, Docker, CI/CD, testes, DTOs, Prisma, configs, assets, e documentação técnica. Atualização geral do workspace. — data não informada\n  - `9de63b255bf43e862a1c8ab4c0e419e6a43c68cd` — feat: Atualização completa de dependências e configuração de deploy

Descrição:

Este commit abrange uma ampla gama de atualizações e melhorias no projeto, com foco na modernização das dependências, refatoração da configuração de contêineres e aprimoramento do ambiente de desenvolvimento e produção.

Principais Mudanças:

*   **Atualização de Dependências:**
    *   Atualizadas as dependências `npm` nos pacotes `client`, `server` e no `root` do projeto para as versões mais recentes, resolvendo vulnerabilidades e trazendo melhorias de performance.
    *   Removido `client/package-lock.json` para reconstrução a partir do `package.json` atualizado.

*   **Configuração de Docker:**
    *   Introduzidos novos arquivos `Dockerfile.prod` para `client` e `server`, otimizados para builds de produção.
    *   Adicionado `docker-compose.prod.yml` para orquestração do ambiente de produção.
    *   O `docker-compose.yml` foi atualizado, e o antigo salvo como `docker-compose.old.yml`.

*   **Testes:**
    *   Modificados vários arquivos de teste no `client` e adicionado o novo teste `simple-test.test.ts`.

*   **Documentação:**
    *   Atualizado o `README.md` e adicionado `docs/DEPLOY_MULTIPLATAFORMA.md`.

*   **Scripts de Deploy:**
    *   Adicionados novos scripts de deploy (`deploy-master.js`, `deploy.js`).

*   **Configuração de Ambiente e Infra:**
    *   Adicionados `.env.development` e `infra/nginx/nginx.simple.conf`. — data não informada\n  - `1e664d1ba7a4eede769422e05b07212c41e67463` — feat: Grande refatoração e Dockerização do projeto Will Finance 5.0

Esta atualização introduz uma reformulação significativa em todo o projeto, focando em escalabilidade, manutenibilidade e capacidades de implantação. As principais mudanças incluem a Dockerização completa, melhorias na gestão de estado do frontend, otimizações na arquitetura do backend e aprimoramentos na qualidade do código TypeScript. — data não informada\n  - `5d67249c8c76af27987f5888bc9964099f23575d` — feat: Implement comprehensive enterprise-grade refactoring and Dockerization

This commit introduces a major overhaul across the entire project, focusing on enhancing scalability, maintainability, and deployment capabilities.

Key changes include:

- **Full Dockerization & Deployment Pipeline:**
  - Added new `DOCKER.md` for detailed deployment instructions.
  - Introduced robust Docker Compose configurations (`docker-compose.yml`) and multi-stage Dockerfiles for both client and server.
  - Developed comprehensive deployment scripts (`.ps1`, `.sh`) for various environments, including health checks and graceful shutdowns.
  - Integrated Prometheus, Grafana, and Loki for advanced monitoring and logging.

- **Frontend State Management & Testing Overhaul:**
  - Migrated frontend state management to Zustand, introducing dedicated stores for authentication, transactions, and budgets (`authStore.ts`, `transactionStore.ts`, `budgetStore.ts`).
  - Implemented new React Contexts for family, settings, and theme management.
  - Significantly expanded and improved client-side testing infrastructure with new test utilities (`test-utils.tsx`, `setupTests.ts`) and dedicated tests for hooks and stores.
  - Updated UI components (`FinancialDashboard.tsx`, `FamilyUserSelector.tsx`, `FinancialReportGenerator.tsx`, `Table.tsx`) for better type safety, accessibility, and integration with new state management.

- **Backend Architecture & Database Optimization:**
  - Migrated database provider from SQLite to PostgreSQL in `prisma/schema.prisma`.
  - Implemented extensive database indexing across all models (`User`, `Account`, `Category`, `Transaction`, `Budget`, `Goal`, `Notification`, `AiInsight`) for significant performance improvements.
  - Refactored `PrismaService` to include enterprise-grade features like advanced logging, transactional operations, and robust health checks.
  - Introduced DTOs (`auth.dto.ts`) for improved data validation and type safety in API endpoints.
  - Enhanced `main.ts` for production-ready application bootstrapping, including advanced CORS, global validation pipes, and graceful shutdown hooks.
  - Removed legacy `server/src/utils/index.ts` and `server/test/app.controller.spec.ts` for a cleaner, more modular NestJS architecture.

- **TypeScript & Code Quality:**
  - Addressed and resolved all major TypeScript compilation errors by refining `tsconfig.json` and `tsconfig.build.json` for stricter type checking and optimized build processes.
  - Ensured consistent type usage across frontend and backend, particularly for transaction and budget types (e.g., `income` -> `INCOME`).
  - Added detailed documentation (`docs/BATCH_1_CONCLUSAO_STORES_TYPING.md`, `docs/BATCH_3_CONCLUIDO.md`, `docs/CORRECAO_TYPESCRIPT_COMPLETA.md`) outlining the scope and impact of these refactoring batches.

This release lays a solid foundation for future feature development, ensuring high performance, scalability, and maintainability across the entire Will Finance 5.0 application. — data não informada\n  - `d5b5c7e76086583036289ebed3fd7e12c2309316` — feat(core): Estruturação e padronização enterprise do projeto Will Finance 5.0

- Implementa arquitetura avançada para frontend (client/) e backend (server/), conforme especificação cyberpunk premium.
- Adiciona convenções de nomenclatura profissional para arquivos, funções, componentes, tipos, constantes, diretórios e variáveis CSS.
- Aplica template master para componentes React com validação Zod, React Query, Framer Motion, estados otimizados e tratamento de erros.
- Inclui tema cyberpunk premium com variáveis CSS neon, gradientes, animações, responsividade e acessibilidade.
- Refatora scripts do package.json para automação completa: dev, build, test, lint, db, docker, análise, deploy, monitoramento e segurança.
- Adiciona pipeline CI/CD avançado no GitHub Actions, cobrindo análise estática, testes unitários/integrados/E2E, build, docker, deploy, segurança e monitoramento.
- Estrutura Dockerfile e docker-compose para ambiente distribuído, seguro e escalável.
- Documenta guidelines de desenvolvimento, padrões de resposta API, tratamento de erros, validação rigorosa, segurança JWT/Firebase, testes enterprise e JSDoc.
- Garante cobertura mínima de 80% nos testes, performance frontend <2s FCP, backend <100ms (p95), e validação/sanitização de todas entradas.
- Atualiza README e documentação técnica para onboarding rápido e referência de arquitetura. — data não informada\n  - `673d1eb874d4f1fab1e11b0905365a9389d19881` — refactor: organização completa do projeto

- Estrutura reorganizada conforme padrão fullstack enterprise
- Arquivos movidos para pastas adequadas (components, hooks, pages, services, stores, types, utils, etc)
- Imports ajustados para refletir novos caminhos
- Removidos arquivos obsoletos e duplicados
- Documentação e scripts mantidos em diretórios próprios
- Recomenda-se rodar lint, typecheck e testes após a reorganização
- Push automático para a branch main — data não informada\n  - `a69b422c52e539e9cf0d629bcc76975c5c0dc204` — feat: commit detalhado

- Validação completa dos arquivos principais do backend e client
- Nenhum erro de lint, typecheck ou configuração encontrado
- Estrutura do projeto estável e pronta para novas funcionalidades
- Novos hooks adicionados: useAnimation, useMaster, useSettings, useSound, useTheme
- Novo componente de UI: cyberpunkProgressStyles
- Removidos arquivos obsoletos de configuração e rotas duplicadas
- Recomenda-se rodar os scripts de lint, typecheck e testes para garantir qualidade total
- Push automático para a branch main — data não informada\n  - `112069a9b3ae76e9f716f884f951b7ff99a804aa` — feat: commit detalhado

- Validação completa dos arquivos principais do backend e client
- Nenhum erro de lint, typecheck ou configuração encontrado
- Estrutura do projeto estável e pronta para novas funcionalidades
- Novos hooks adicionados: useAnimation, useMaster, useSettings, useSound, useTheme
- Novo componente de UI: cyberpunkProgressStyles
- Removidos arquivos obsoletos de configuração e rotas duplicadas
- Recomenda-se rodar os scripts de lint, typecheck e testes para garantir qualidade total
- Push automático para a branch main — data não informada\n  - `1d9806b31ccee52b876f9304fc776b3f1da58013` — feat: adicionar opções de compilação estritas e consistência de nomenclatura nos arquivos — data não informada\n  - `e27d7f4c655eb1d16ac31ec9a56c9d396c01e34f` — feat: commit completo - estrutura validada e sem erros críticos — data não informada\n  - `ddbb976875b05d05bf0876307bad9b50d4e82efe` — feat: Atualizar Dockerfile para otimização de segurança e desempenho, incluindo criação de usuário não-root e healthcheck — data não informada\n  - `b0d551441d2d8aa92f598897e4f52b3e8e30eb22` — feat: Atualização completa para Will Finance 6.0

- Remoção do README.md antigo e inclusão de nova documentação detalhada para versão 6.0
- Atualização da configuração do Nginx para refletir novos ports e arquitetura distribuída
- Exclusão do README.md obsoleto dos scripts
- Incremento da versão do pacote server para 6.0.0
- Refatoração de arquivos e estrutura para aderência ao novo padrão enterprise
- Melhoria da interface cyberpunk premium e integração avançada de IA
- Ajustes em dependências, configurações e scripts para compatibilidade total com a stack 6.0
- Limpeza de arquivos desnecessários e padronização de diretórios

Essa versão marca o início da arquitetura distribuída, segurança reforçada, experiência cyberpunk e recursos de IA preditiva. — data não informada
\n## 39. William-kelvem94/Gerenciador_Financeiro-6.0

- **Registros retornados:** 9
- **Amostra:**
  - `819b744946190f9d6367c48d58ab2ffb5f1d9aa6` — feat: Adicionar novas animações e classes de cores dinâmicas

- Adicionar classes CSS para animações com delays (animate-float-delay, animate-slide-up-delay, animate-bounce-delay, animate-slide-in-delay)
- Implementar classes para ícones de conta e legendas de gráfico com cores dinâmicas usando data attributes
- Atualizar tsconfig.json para forçar consistência na capitalização dos nomes de arquivos
- Modernizar componentes de página (CreateAccountModal, AccountsPage, LoginPage, RegisterPage, DashboardPage) para utilizar novas classes e animações — data não informada\n  - `106a3c66c5391d9e073c2c985ac5f8b55a3c479d` — fix: Corrigir todos os problemas de acessibilidade e lint

- Adicionar aria-label e title em todos os botÃµes sem texto (Dialog, Toast, Modal, CreateAccountModal)
- Adicionar htmlFor nos labels e id nos inputs (ReportsPage, SettingsPage)
- Melhorar acessibilidade dos checkboxes com labels clicÃ¡veis
- Corrigir todos os avisos axe/name-role-value
- Corrigir todos os avisos axe/forms (labels associados)
- Melhorar UX com labels clicÃ¡veis nos checkboxes

Todos os problemas crÃ­ticos de acessibilidade foram resolvidos.
Os avisos de estilos inline (no-inline-styles) sÃ£o aceitÃ¡veis pois sÃ£o usados para animationDelay dinÃ¢mico. — data não informada\n  - `4f868c8d3aa383f56635c71b422e8f77ad741bf7` — feat: Adicionar componentes UI avanÃ§ados e modernizar RegisterPage

- Criar componentes reutilizÃ¡veis: Skeleton, Dialog, Tooltip, Select, Toast
- Modernizar RegisterPage com layout 2 colunas e benefÃ­cios destacados
- Adicionar animaÃ§Ãµes e glassmorphism no registro
- Implementar skeleton loaders para estados de carregamento
- Criar sistema de toast notifications
- Header jÃ¡ estÃ¡ modernizado com gradientes — data não informada\n  - `89b76ec783da68fa6c4f674de521635cda8b5d0b` — feat: Modernizar UI completa com design system robusto

- Implementar sistema de cores CSS variables completo (light/dark)
- Criar componentes UI modernos baseados em shadcn/ui (Card, Button, Badge, Input, Label)
- Adicionar animaÃ§Ãµes sofisticadas (blob, gradient-slow, float, pulse-glow, shimmer, slide-up, etc.)
- Implementar glassmorphism e efeitos visuais avanÃ§ados
- Modernizar pÃ¡gina de Login com layout de 2 colunas e features destacadas
- Melhorar Dashboard com cards vibrantes, gradientes e animaÃ§Ãµes
- Adicionar suporte completo para dark mode em todos os componentes
- Implementar Material Design 3 inspired elevations e state layers
- Adicionar scrollbars customizadas e gradientes modernos
- Melhorar loading states com animaÃ§Ãµes elaboradas

Inspirado no melhor do design moderno de aplicaÃ§Ãµes enterprise. — data não informada\n  - `9f1192dac0b8b1fe501bd5abc56d51d50fadd380` — docs: Adicionar README Enterprise completo com documentacao robusta — data não informada\n  - `ff7512bcaa4fc5fd886053ec2e41123d28930a06` — ﻿feat: Migrar para arquitetura Enterprise com Docker e PostgreSQL

INFRAESTRUTURA DOCKER COMPLETA
- Docker Compose com servicos PostgreSQL, Redis, Backend e Frontend
- Multi-stage Dockerfiles otimizados para dev e producao
- Health checks em todos os servicos
- Volumes persistentes para dados
- Network isolada para comunicacao entre servicos
- Nginx reverse proxy para producao

MIGRACAO BANCO DE DADOS
- Migrado de SQLite para PostgreSQL 15
- Schema atualizado com tipos Decimal para valores monetarios
- Binary targets configurados para Docker (linux-musl)
- Suporte a escala horizontal e replicas
- Melhor performance e confiabilidade

SCRIPTS DE GERENCIAMENTO
- docker-start.ps1 (Windows PowerShell)
- docker-start.sh (Linux/Mac Bash)
- Menu interativo com opcoes:
  * Modo desenvolvimento (hot-reload)
  * Modo producao (otimizado)
  * Stop, rebuild, logs, cleanup

CONFIGURACAO
- Arquivo .env.example com todas as variaveis
- Suporte a variaveis de ambiente por servico
- Configuracao separada dev/prod
- Redis para cache e sessions
- CORS e seguranca configurados

SERVICOS DISPONIVEIS
- Frontend: http://localhost:5173
- Backend: http://localhost:4000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Nginx (prod): http://localhost

PROXIMOS PASSOS
- PWA com Service Worker
- Sistema de testes automatizados
- OAuth Google
- Documentacao Swagger/OpenAPI — data não informada\n  - `03a4585f5f471338cb2a1550efd7a2472f16c5ef` — ﻿feat: Implementar sistema completo de tema claro e escuro

FUNCIONALIDADES ADICIONADAS:
- Botao alternador de tema no Header (Sol/Lua)
- Persistencia da preferencia do usuario no localStorage
- Transicoes suaves entre temas (300ms)
- Suporte completo a dark mode em todos os componentes

COMPONENTES ATUALIZADOS:
- Header: Botao de tema com icones animados
- Sidebar: Cores e gradientes adaptados para dark mode
- MainLayout: Fundo e circulos decorativos no modo escuro
- Dashboard: Textos e cards responsivos ao tema
- Cards, inputs, labels e badges com variantes dark

IMPLEMENTACAO TECNICA:
- Store Zustand para gerenciamento do tema
- Tailwind dark mode com classe 'dark'
- Classes CSS dark:* em todos os componentes
- useEffect no App.tsx para inicializar tema
- Gradientes ajustados para melhor contraste

EXPERIENCIA DO USUARIO:
- Animacao de rotacao nos icones do botao
- Cores otimizadas para leitura em ambos os temas
- Glassmorphism mantido com opacidades ajustadas
- Bordas e sombras adaptadas para cada modo — data não informada\n  - `d8c82a25c6510b9022fa28cc87b2ef7d9822f4c4` — fix: Adicionar arquivo .env.example com configuraÃ§Ã£o da API

- Criado frontend/.env.example documentando VITE_API_URL
- URL configurada para http://localhost:4000/api
- Resolve problema de login e registro que nÃ£o funcionavam
- UsuÃ¡rios agora sabem qual configuraÃ§Ã£o usar no .env local — data não informada\n  - `c26dffd444052f530d984e2ab2e6ef4c28951b5a` — feat: Modernização completa da interface com efeitos visuais premium e migração para SQLite

🎨 Interface Modernizada:
• Tela de login com fundo animado e gradientes dinâmicos
• Círculos decorativos flutuantes com animações suaves
• Ícones decorativos flutuantes (TrendingUp, PieChart, BarChart3)
• Logo com efeito glassmorphism e brilho pulsante
• Cards com backdrop blur e sombras modernas

📊 Dashboard Premium:
• Header com gradientes coloridos em texto
• Cards KPI com gradientes, hover scale e animações escalonadas
• Barras de progresso coloridas
• Gráficos melhorados com gradientes e tooltips modernos
• Legendas interativas com efeitos de hover

🎯 Layout Principal:
• Fundo com gradiente suave e círculos decorativos
• Header com glassmorphism
• Seletor de empresa modernizado
• Notificações com animação pulsante
• Sidebar premium com navegação estilizada
• Logo com gradiente e efeitos de transformação

✨ Efeitos CSS Adicionados:
• Animações personalizadas: float, gradient-shift, pulse-glow, slide-in
• Classes utilitárias: hover-glow, animate-*
• Scrollbar customizada com gradiente
• Botões com transformações (scale, shadow)
• Glassmorphism em componentes

🗄️ Migração de Banco de Dados:
• Migrado de PostgreSQL para SQLite
• Schema adaptado para compatibilidade SQLite
• Enums convertidos para strings
• Json e arrays convertidos para strings
• Migrations executadas com sucesso
• Seed com dados de demonstração

🚀 Configuração do Projeto:
• Backend configurado na porta 4000
• Frontend configurado na porta 5173
• Ambiente de desenvolvimento pronto
• Banco de dados SQLite criado e populado
• Servidores rodando em background

📦 Tecnologias Visuais:
• Glassmorphism (backdrop-blur)
• Gradientes animados
• Transformações CSS
• Sombras dinâmicas
• Animações suaves
• Efeitos interativos de hover

🔧 Melhorias Técnicas:
• Prisma Client regenerado
• Dependências instaladas
• Configuração .env criada
• Linter errors corrigidos
• Acessibilidade melhorada

Credenciais Demo:
Email: admin@gerenciador.com
Senha: Admin@123456 — data não informada
\n## 40. William-kelvem94/Gerenciador_Financeiro-7.0

- **Registros retornados:** 100
- **Amostra:**
  - `9a7edad7202c2634e87c0fb08837c51ef5fa17db` — Rearma gate após consolidação do CSS canônico

- absorve a remoção de adaptive-overrides.css já concluída na main
- passa a auditar ausência do override legado e referências órfãs
- mantém alinhamento IA, Next 16, ESLint 9 e bundle
- preserva gates separados de Prisma, lint, TypeScript, Jest, Playwright e build
- mantém proteção contra main móvel durante a validação — data não informada\n  - `a749a993a53801a45a6901893f0cb60047d59757` — refactor(frontend): elimina overrides e unifica geometria global do Numni

- remove adaptive-overrides.css e absorve apenas compatibilidades ainda necessárias no Responsive System
- restringe adaptive-ui.css a capacidade do dispositivo, densidade adaptativa e semântica financeira
- deixa Liquid Glass como proprietário único da paleta base, gutters e tokens financeiros
- centraliza contenção de auth, gráficos, Recharts, tabelas, tabs, dialogs e touch largo no responsive-system.css
- remove neutralizações de wrappers max-width e padding sem consumidores reais
- remove o workflow antigo de manutenção única e preserva a retomada mais recente já presente na main
- remove metadado/constante Twitter legado sem inventar novo identificador público
- atualiza documentação e testes arquiteturais para impedir nova fragmentação da cascata
- preserva regras financeiras, autenticação, persistência e comportamento funcional — data não informada\n  - `739d393f6e05f38ec11839933075203650c11e4d` — Torna gate de manutenção resiliente à indentação

- substitui comparações literais do next.config por padrões estruturais
- mantém cancelamento da execução obsoleta pela mesma concurrency group
- preserva todos os gates de Prisma, lint, TypeScript, Jest, Playwright e build
- continua bloqueando publicação se a main avançar durante a validação — data não informada\n  - `22b2d8662622dc58c24fb73cc7991193c8fff61c` — Retoma manutenção validada sobre a main atual

- cancela a execução temporária obsoleta pela mesma chave de concorrência
- reaplica o lote sobre o estado atual da main sem criar branch auxiliar
- alinha IA, Next 16, ESLint 9 e análise de bundle
- regenera o lockfile pelo npm e audita dependências órfãs
- exige Prisma, lint, TypeScript, Jest, Playwright Chromium e build antes do commit final
- bloqueia o push se a main avançar novamente durante a validação — data não informada\n  - `68b477fa29b12d3aa60d048d6ac14d123445f763` — refactor(frontend): consolida base visual canônica do Numni

- remove o antigo useHeaderAdaptive e o helper de spacing do Header, já sem consumidores
- remove design-tokens legado e deixa LayoutContext restrito à busca global
- elimina utilitários responsive-* desconectados das PagePrimitives
- reduz responsive-spacing aos tokens ainda consumidos pelos controles canônicos
- remove OptimizedImage órfão e sua exportação pública
- limpa referências imobiliárias herdadas da documentação de componentes UI
- mantém Button, Card, Tabs e demais primitivas ativas sem alteração de regra de negócio
- reforça testes arquiteturais contra reintrodução dos sistemas responsivos antigos
- preserva compatibilidade da rota antiga de chat apontando para o assistente do Numni — data não informada\n  - `05728305a10b577da9589b69a3836c80c43d2af4` — Executa manutenção validada de IA e toolchain do Numni

- adiciona rotina temporária e autocontida para alinhar concorrência da IA e toolchain Next 16
- regenera package-lock pelo npm em vez de editar lockfile manualmente
- audita dependências órfãs, branding e CSS diretamente no checkout
- exige Prisma, lint, TypeScript, Jest, Playwright Chromium e build antes de publicar o lote
- gera evidência de validação e remove o próprio workflow após sucesso — data não informada\n  - `66cc3f410661dbd9fb1e417a453592ee604c2c10` — Corrige narrowing do payload na telemetria global

- garante payload validado antes de acessar timestamp e demais campos
- remove o erro de TypeScript apontado pela build da Vercel
- preserva integralmente os buckets globais, retenção, rate limit e sanitização introduzidos no lote anterior — data não informada\n  - `e49c948e5bc3542bb27378be6029d328e4dd73a0` — Torna telemetria do Dock global e compatível com serverless

- remove o buffer em memória que limitava a observação à instância atual da Vercel
- elimina o delegate Prisma dockTelemetryDailyAggregate inexistente e mascarado por any
- reutiliza SystemSetting como armazenamento agregado de baixo custo, sem Redis nem novo serviço
- agrupa eventos em buckets de 5 minutos com retenção de 48 horas e limpeza oportunística
- adiciona atualização otimista para reduzir perda de contagem em concorrência entre instâncias
- mantém apenas métricas operacionais agregadas, sem conteúdo financeiro ou identificadores pessoais
- limita e normaliza eventos, timestamps e tempo para ação antes da persistência
- atualiza o painel administrativo para refletir a janela global consolidada — data não informada\n  - `78dc343be3fe7c623089aa3013afb0d926b9ad44` — Fortalece fallback global e remove branding legado

- substitui Gerenciador Financeiro por Numni na última barreira de erro da aplicação
- remove linguagem imprecisa sobre monitoramento e mensagens antigas de matrix
- reduz dependências visuais e de navegação da tela fatal para aumentar a chance de recuperação quando a árvore raiz falhar
- usa viewport dinâmica 100dvh e controles nativos acessíveis
- mantém captura opcional no Sentry sem tornar observabilidade requisito para recuperação
- oculta stack em produção e preserva digest como código técnico seguro — data não informada\n  - `8fec743905bfa940bedfaadb1d23aa1eea83fa39` — Consolida cadastro no AuthShell e alinha progresso à política de senha

- migra o cadastro para o AuthShell canônico e remove viewport, divisão 42/58 e seletor de tema duplicados
- preserva formulário completo, honeypot, disponibilidade de e-mail, ViaCEP, municípios do IBGE e dados opcionais
- corrige o progresso que marcava senha de 8 caracteres como válida embora o schema exija 12
- mantém Zod, CPF, telefone, idade mínima, callback seguro e fluxo de verificação de e-mail
- melhora semântica do accordion de dados opcionais e tratamento tipado de erro
- não altera endpoint de cadastro, persistência nem regras financeiras — data não informada\n  - `9cd642795a93d1f5515c2c2b4054772c82b72dd6` — Consolida homepage pública com resolução de sessão no servidor

- extrai a interface visual animada para HomePageContent mantendo Framer Motion apenas onde há interação cliente
- remove useSession, useEffect, router e spinner de autenticação da homepage
- resolve a sessão no servidor antes da hidratação e redireciona usuários autenticados pelo callback seguro já existente
- preserva integralmente conteúdo, CTA, tema, layout responsivo e identidade visual pública
- troca min-h-screen por 100dvh para respeitar viewport dinâmica em PWA/mobile
- reduz JavaScript de controle de sessão na superfície pública sem alterar autenticação ou regras financeiras — data não informada\n  - `734aeeebd140da1bf96f567b0ce52f32e87db256` — Converte raiz de autenticação em redirecionamento server-side

- remove useSession, useEffect, spinner e JavaScript de uma rota que só decide destino
- resolve a sessão no servidor com a mesma configuração NextAuth do projeto
- redireciona autenticados para dashboard e demais acessos para login antes de renderizar HTML
- reduz hidratação e elimina flash visual sem alterar o destino ou a política de autenticação — data não informada\n  - `14ee1d76a96a04e90f5f4d457593b284fc86a0c7` — Migra redefinição de senha e corrige estado transitório do token

- move viewport, divisão desktop e seletor de tema para AuthShell
- adiciona estado explícito de resolução do token para não anunciar link inválido antes de ler query string ou fragmento
- mantém a remoção imediata do token da barra do navegador e limita entradas anormalmente longas
- preserva Zod, força da senha, endpoint de reset, expiração e encerramento de sessões do backend
- melhora aria-invalid, associa mensagens de campo e usa estados semânticos de erro
- mantém a identidade visual e a experiência de recuperação em duas colunas no desktop — data não informada\n  - `8245d33a79a34fe64b594cbce70ef409ae4c11fa` — Migra primeiro acesso e elimina renderização fora do estado autenticado

- move viewport e seletor de tema para AuthShell
- impede o formulário de senha definitiva de aparecer enquanto a sessão redireciona usuário não autenticado ou conta que já concluiu o primeiro acesso
- mantém política forte de senha, senha atual para credentials, endpoint mandatory-password e encerramento das sessões anteriores
- adiciona região live para erro/sucesso e melhora atributos aria dos controles
- converte espaçamentos locais em dimensões fluidas sem alterar as regras de segurança — data não informada\n  - `d2f5ba36be2d725a4d09818d1024cbc7235d1719` — Consolida verificação de e-mail e convite no fluxo público

- migra confirmação e reenvio de e-mail para AuthShell com estados acessíveis e viewport canônico
- corrige branding legado "Entrar no GF" para "Entrar no Numni"
- normaliza e valida o e-mail no cliente antes do reenvio sem alterar a resposta genérica anti-enumeração do backend
- limita tokens de verificação anormais antes da chamada pública e preserva cancelamento por AbortController
- transforma /auth/accept-invite em redirecionamento server-side, removendo JavaScript e tela intermediária desnecessários
- mantém endpoints, tokens, rate limits e regras de autenticação existentes — data não informada\n  - `4dabc3e324386c974a39a48f2b75eae406e911cd` — Migra login para o shell canônico de autenticação

- remove a segunda implementação local de viewport, divisão 58/42 e seletor de tema
- reutiliza AuthShell preservando integralmente sessão, callback seguro, lock-status e credenciais NextAuth
- mantém react-hook-form, Zod, mensagens específicas de acesso e limpeza de sessão inválida
- substitui paddings responsivos duplicados por dimensões fluidas centralizadas
- melhora o estado de erro com semântica destructive e mantém foco, labels, aria-invalid e região live
- conserva a identidade visual do login e o painel institucional desktop — data não informada\n  - `e702298f7ac546e9dc0db1ff11f7915d4d201696` — Cria shell canônico para autenticação e migra recuperação

- adiciona AuthShell para centralizar viewport, divisão desktop, safe areas e seletor de tema das rotas públicas
- migra Esqueci minha senha para a nova estrutura sem alterar endpoint, validação ou proteção contra enumeração
- migra a página de erro do NextAuth para o mesmo contrato responsivo
- melhora aria-invalid, estados de erro e ícones decorativos na recuperação
- substitui paddings rígidos por dimensões fluidas e mantém a experiência desktop de duas colunas
- prepara a fundação para migrar login, cadastro e demais fluxos de autenticação sem duplicar geometria — data não informada\n  - `8c6843a31bbdbeb6a410daa7d888d63f1df39fe3` — Reduz camada de overrides após migração das superfícies críticas

- reposiciona adaptive-overrides como compatibilidade temporária em vez de autoridade responsiva
- remove correção de viewport do Assistente IA, agora absorvida pela rota e pelo MainLayout
- remove overrides de alturas fixas de Recharts já substituídos por ChartFrame e adaptive-chart
- elimina media query residual que existia somente para essas alturas legadas
- mantém apenas compatibilidades ainda necessárias para wrappers antigos, tokens financeiros, tabs, auth e touch
- reduz CSS de exceção sem alterar regras de negócio ou identidade visual configurável — data não informada\n  - `15de31d09b7234bf524dcce42d722ab297c200e3` — Remove componentes legados e desconectados da IA

- elimina AIConversationSidebar, AIPersonalityControls e InsightPanel sem referências ativas
- remove VirtualizedMessageList e MessageFeedback, que formavam uma cadeia antiga também desconectada da superfície atual
- mantém AIChatAssistant e AIFloatingWidget como implementações realmente usadas
- reduz código morto e superfície de manutenção sem alterar APIs, histórico, anexos ou ações financeiras
- preserva integralmente as confirmações explícitas e proteções de operações financeiras — data não informada\n  - `4e6c435ec6e024174c7e527dae83835c4b744cc9` — Remove viewport rígido da superfície do assistente IA

- elimina calc(100dvh - chrome) duplicado e deixa a altura sob responsabilidade do MainLayout
- remove max-width e breakpoints locais da rota do assistente
- reutiliza app-fill-viewport e padding fluido baseado no container
- preserva seleção de conversa por query string e o componente AIChatAssistant sem tocar em ações financeiras ou confirmações — data não informada
\n## 41. William-kelvem94/Gestor_Aluguel

- **Registros retornados:** 51
- **Amostra:**
  - `4a8255147928a5a63a4fefd08ff0a4b8241f71de` — feat: implementar rotina automática de envio de e-mails para vencimento de aluguel e adicionar templates de e-mail — data não informada\n  - `fac6663dce5d465cf870fb6c4171c1c7a76a4596` — Refatoração e organização enterprise:

- Removidos arquivos e scripts legados, centralizando tudo em estrutura enterprise
- Backup completo da integração WhatsApp movido para improvements/whatsapp_backup (serviços, UI, scripts)
- Scripts de build, testes e instalador agora em scripts/ com documentação e automação profissional
- Novo tema moderno (dark) para UI, removendo temas antigos
- Refatoração dos serviços: src/services agora é pacote enterprise, com __init__.py e reexportação
- Atualização e validação dos testes de integração, unitários e cobertura
- Atualização dos assets e documentação
- Melhoria na estrutura de dados, validação e logging

Commit detalhado para rastreabilidade e auditoria. — data não informada\n  - `ce1d477a4e5225806b79b898734b6f19c743169c` — feat: configurar Alembic, adicionar testes de integração e scripts de setup + validação

- Atualiza lembic/env.py para proteger fileConfig e usar engine do projeto
- Ajusta lembic.ini para apontar para sqlite:///data/database.db
- Adiciona migration validation test 	ests/test_alembic.py (upgrade/downgrade)
- Adiciona testes de exportação Excel real 	ests/test_excel_export_real.py (cria dados quando necessário)
- Adiciona 	ests/test_installation.py para checar dependências via importlib
- Atualiza pyproject.toml com dependências detectadas (pandas, openpyxl, etc.)
- Adiciona alidate_complete_system.py para validação end-to-end do sistema
- Adiciona scripts de setup: setup_dev.py e setup_dev.sh

Notas:
- Execução automática de setup_dev.py falhou na etapa lembic upgrade head porque lembic não estava disponível no PATH do ambiente; ativar venv e instalar dependências antes de rodar o script.
- Testes de integração de Excel e migração passaram localmente durante a validação. — data não informada\n  - `d99d37cb5bee3c421a83c515833aa9edf858b017` — feat: adiciona testes de integração para validação de renda no TenantValidator — data não informada\n  - `233d93fabce7f222d80bcc68f6b6a4d7a8d42094` — feat: add income field to tenant model and update related services

- Added 'income' field to TenantData model.
- Updated TenantService to handle income during tenant creation and updates.
- Enhanced ReportService to evaluate tenant payment reliability based on income.
- Modified UI components to include income input in tenant dialogs and display in tenant views.
- Updated migration script to add 'income' column to tenants table.
- Created smoke report script to generate financial reports over the last 60 days. — data não informada\n  - `1eda97e4b373dfdd74f0e044f78a892e1d2a568f` — Ajusta pool do DB para SQLite (NullPool) e roda gerador: adiciona scripts de seed/geração e migração — data não informada\n  - `feee6721ca16264e59d22fd1dec19994aaf9a3a9` — Adiciona scripts de seed/geração de dataset e corrige modelo Payment para aceitar comprovantes (proof_content/proof_filename) — data não informada\n  - `0795ba3de0ff9d9d1eaae9287cfd65dd61542b5d` — Melhorias: relatórios e filtros de imóveis (PT-BR) — data não informada\n  - `30c39b51cb8d8c9f06d22010824014454000ad4c` — Melhora o tratamento de erros no main.py, garantindo que falhas no logger não quebrem a aplicação. Adiciona método para atualizar a lista de propriedades no PropertyTableModel e implementa filtros de status na PropertyView. Exibe mensagem ao usuário quando não há pagamentos no relatório. — data não informada\n  - `8243cea5485903d2d941ad31f74ec419210ed3b8` — Melhora a exibição de status no PropertyDialog, traduzindo opções para o usuário e garantindo a compatibilidade com o banco de dados. Filtra contratos ativos por padrão no RentalTableModel. — data não informada\n  - `a6ad828b2bd99f579cf66cba79cea38fda3de3ec` — Melhora a mensagem de erro de validação no PaymentService, incluindo o campo obrigatório na exceção levantada. — data não informada\n  - `a42f36ed6f2809a85f183d93ddc0d90a3989f8fa` — Melhora o registro de desempenho no PerformanceOptimizer, garantindo que falhas no monitor não quebrem a aplicação. Adiciona suporte para dicts leves no modelo de dados de aluguéis, otimizando a recuperação e exibição de informações no RentalTableModel e RentalView. — data não informada\n  - `d57702708c5133565e2dfebbf7e3dea0914a78e9` — Adiciona script run_app_debug.py para facilitar a execução e depuração da aplicação, garantindo que o diretório raiz esteja no sys.path. — data não informada\n  - `98c4b46c0464125c29eb3dc533581a0231719165` — Remove Qt logging handler antes do encerramento da aplicação para evitar acesso a objetos já destruídos. — data não informada\n  - `d5ab821d6880a8ef86add22a2e43835eb3219a7e` — Implementa carregamento sob demanda para a instância global do PerformanceOptimizer, evitando a criação no import. Atualiza chamadas para usar a função de acesso à instância. — data não informada\n  - `b54334bcbe7c2eac66a09845e4988c909e5eb666` — Refatora importações e otimiza o sistema de estabilidade, evitando side-effects durante o import. Adiciona função para calcular o ciclo de cobrança e ajusta o uso de campos de aluguel. Melhora a compatibilidade com QDate e implementa eager-loading para evitar DetachedInstanceError na visualização de aluguéis. — data não informada\n  - `317a47325d1c59936592d1393b01d87261a11c17` — Melhora o design dos cards no dashboard com responsividade e animações, além de ajustar a estilização de widgets e cabeçalhos nas visualizações de pagamento, propriedade e aluguel. — data não informada\n  - `8298218decf45f8c48840c928f58ecdb2be8459d` — Adiciona ícone do aplicativo nas janelas principais e diálogos — data não informada\n  - `a5470873f4cf99a7c75d531bf46c5f4ed6262068` — Adiciona ícones e atualiza títulos nas visualizações de pagamento, propriedade e aluguel — data não informada\n  - `79b90884bdd840bcda5b879f941aadeca7d42626` — Move design styles to QSS for centralized management in StatCard — data não informada
\n## 42. William-kelvem94/hermes-agent-pinokio

- **Registros retornados:** 2
- **Amostra:**
  - `875648a7fbf69a76185b866335329adb01894d24` — Expand Hermes notes: remote brain & local agent

Add detailed explanation of the Hermes agent architecture: the "Remote Brain, Local Hands" pattern, token-bridge/compression to minimize context sent to remote models, and how Hermes reads local files, sends summaries, applies remote model suggestions, writes files and runs tests. Describes sub-agent/task delegation to avoid hallucinations and gives next step: configure an OpenRouter or Google AI Studio API key in .env (mentions local repo path). — data não informada\n  - `8910aafc11c9b96bae4f0b8e8d91401695ddde82` — first commit — data não informada
\n## 43. William-kelvem94/hermes-agent-pinokio-wk

- **Registros retornados:** 0
- **Amostra:**
  - Nenhum registro retornado.
\n## 44. William-kelvem94/IA_LOCAL_S_ULTRA

- **Registros retornados:** 53
- **Amostra:**
  - `ec5e43a8bb4e2571c915fd09363a9b3bc7b758e4` — feat: Redesign completo da interface AMOLED HUD, correcoes no Android 14 e super-poderes nativos

- Redesign da interface adaptada para telas Dynamic AMOLED 2X (Galaxy S23/S24 Ultra).
- Componente visual animado ArcReactorView em Canvas nativo com resposta em tempo real.
- Suporte a WindowInsets / Edge-to-Edge para alinhamento com a barra de status e camera frontal.
- Icones vetoriais de alta resolucao para microfone e envio.
- Novos super-poderes e ferramentas de sistema: controle de midia, volume, timers, alarmes, clipboard, notificacoes e lanterna direta.
- Blindagem e correcoes de crashes para servicos em segundo plano no Android 14+.
- Resolucao para restricoes de acessibilidade da Samsung One UI e Assistente de Voz padrao. — data não informada\n  - `87b1bac10b021c294f7a540f927da77c7bd42cfa` — Bump Gradle wrapper to 8.13

Update the Gradle wrapper distribution URL from 8.10 to 8.13 so the project uses the newer Gradle release and its fixes and improvements. — data não informada\n  - `a67631cf67bde4cada5cf080fa46d577727eedd1` — Refatora distribuição do modelo e registry de ferramentas Android

Remove o download e empacotamento do Qwen3 GGUF durante o build Gradle, reduzindo drasticamente o peso e o custo do pipeline de compilação. Introduz ModelDownloader em runtime com armazenamento privado, retomada via HTTP Range, preservação de arquivo parcial, redirects limitados a HTTPS, controle de espaço livre, progresso por bytes/percentual e validação SHA-256 obrigatória antes de promover o modelo para uso pelo llama.cpp.

Integra o fluxo de download à MainActivity usando a LinearProgressIndicator existente, mantendo a barra ativa durante download e checksum e reutilizando uma cópia previamente validada nos boots seguintes. Atualiza ModelManager para o novo modelo em runtime e inclui migração segura de uma cópia local antiga.

Refatora AndroidToolRegistry para um sistema modular baseado na interface AndroidTool e AndroidToolDiscovery. Cada ferramenta passa a declarar nome, risco, catálogo e execução em uma classe própria, organizada por domínio. O registry mantém centralizadas confirmação, modo privado, tratamento de erro e auditoria, rejeita nomes duplicados e gera o catálogo do prompt diretamente das ferramentas descobertas, eliminando o grande bloco when e a duplicação entre despacho e documentação do agente.

Atualiza README, ARQUITETURA, MODELOS e ROADMAP para a versão 0.3.0, documenta as próximas fases de memória, controle térmico, RAG, Google APIs, visão, foreground service e criptografia, e ajusta o workflow Android para refletir que o APK não contém mais o GGUF nem baixa 2,5 GB durante o CI. — data não informada\n  - `a02832cae826f3c00d252920dd94ea99cc249baa` — Downgrade Gradle wrapper and foojay plugin

Revert Gradle toolchain versions for compatibility: update gradle/wrapper/gradle-wrapper.properties to use gradle-8.10-bin.zip (was 9.3.0) and lower org.gradle.toolchains.foojay-resolver-convention plugin from 0.9.0 to 0.8.0 in settings.gradle.kts. This aligns the build environment with the project's supported Gradle/toolchain versions. — data não informada\n  - `103f7b653d29192e22039cdbc00ea181d8f51729` — Bump Foojay toolchain resolver

Update the Gradle Foojay toolchain resolver convention plugin from 0.8.0 to 0.9.0 in the settings configuration. This keeps the project aligned with the newer resolver version for toolchain auto-detection. — data não informada\n  - `918f73cc3d3e751d651c4b12a5c0909766c42f96` — Add Gradle toolchain resolver plugin

Enable the Foojay Gradle toolchain resolver convention plugin in settings.gradle.kts so Gradle can automatically resolve and provision required JDK toolchains for the project. — data não informada\n  - `488175467ad6c013ed323f866298ff0514dc4edf` — Add Gradle wrapper scripts

Add the Gradle wrapper bootstrap files needed to run the project consistently across environments. This includes the Unix and Windows launcher scripts, the wrapper properties, and the wrapper JAR, locking the build to Gradle 9.3.0. — data não informada\n  - `0cfd794fb28da8b48066d9b20e003793ea55e3b0` — Enable parallel Gradle tooling

This change enables Gradle's parallel tooling sync for Gradle 9.4+ by setting org.gradle.tooling.parallel=true. This helps improve build performance in environments that benefit from parallel synchronization. — data não informada\n  - `cfb0ed226389cdac5fb8aecc10c6abcbb647d6a1` — tmp — data não informada\n  - `6ec2286dfbad397d76e3114f1d76f0d369ff8148` — tmp — data não informada\n  - `ab02d90a82aef2bddc1d73fffddedf398d87bbd7` — tmp — data não informada\n  - `57ffa7b9fe180da29b4c3793177561bc8f71d779` — tmp — data não informada\n  - `d2a2b0f301d190bf12c6703c19ab91959762bde1` — tmp — data não informada\n  - `372c392126386df7a8cca4eca0a51decee63dc63` — tmp — data não informada\n  - `2c1e633c2f2b76e627a773ee4903d1486c754a43` — tmp — data não informada\n  - `871ff76f9c5c9d4860b1f0416d3588b4fedf5f98` — tmp — data não informada\n  - `804315ee9253598095fc82dca722419cb8d367fe` — tmp — data não informada\n  - `8d67279f85f15fef31c6b5193973ef4c81febde7` — tmp — data não informada\n  - `fef82793b034f0052d0df34fe11b32e972f7235c` — tmp — data não informada\n  - `26db2731ab221ee865f87746e217b3f8723134f9` — tmp — data não informada
\n## 45. William-kelvem94/IA_MUSIC

- **Registros retornados:** 6
- **Amostra:**
  - `f09323fdbd72a8ee9eea246c9f2521d484144ea2` — Add filename sanitizer and diagnostic report

Introduces a sanitize_filename function in test_sanitize.py to clean and normalize filenames by removing special characters and accents. Also adds a diagnostic_report_20250719_084706.json file containing system and environment information. — data não informada\n  - `6ea549940da9ae9b0e4429080d3237e24c719dba` — Salvando alterações do Codespace — data não informada\n  - `366529bac4ae902e68ceb0ab4d04ea51df702015` —  Status final do projeto - Sistema 100% completo e superior à versão anterior — data não informada\n  - `b9ba31323870da0f9f457cad35a44738abe4f25d` —  Sistema completo de diagnóstico, configuração avançada e limpeza automática — data não informada\n  - `2738b803c7a0086e8670f2301140335d20419bae` —  Adicionando sistema completo de utilitários e ferramentas avançadas de download — data não informada\n  - `d9ab44422afd4c7d778066a7a15e631399f578c5` —  Initial commit - IA Musical Complete System

 Features:
- FastAPI server with modern web interface
- YouTube audio download and processing
- AI-powered style transfer (MusicGen + Demucs)
- 11 musical styles supported (Sertanejo, Funk, Rock, etc.)
- Optimized audio processing with memory management
- Complete project structure with auto-download models

 Ready for production deployment!
 Auto-install scripts included
 Working Demucs integration with Windows optimization — data não informada
\n## 46. William-kelvem94/IA-MIDIA

- **Registros retornados:** 1
- **Amostra:**
  - `a2c09e2936ea8a16126010c43c3ce229fa24c2a8` — Adiciona estrutura inicial do projeto IA-MIDIA — data não informada
\n## 47. William-kelvem94/IA-POTENTE

- **Registros retornados:** 5
- **Amostra:**
  - `d0f45fc331a45c061ba1a5036a3f3bbc6529f2ec` — security: update scikit-learn to 1.5.0 — data não informada\n  - `d0e189226df814e60efe21b93353e10194c37e2a` — security: disable vulnerable transformers dependency — data não informada\n  - `da7711c4c207ca021b10671203905a3be7bcb04c` — security: disable vulnerable transformers dependency — data não informada\n  - `760c9e1297c8ce0d93018b870ca6ee48587a5bc5` — Create README.md — data não informada\n  - `18afb1f6c47a8e4d082798b4401f5aba3ac7f4ee` — first commit — data não informada
\n## 48. William-kelvem94/IA.IDE

- **Registros retornados:** 2
- **Amostra:**
  - `4c985d3f8b42607a1648e1aedb63d7ba1e4e9385` — 🧹 Ignora blobs grandes no gitignore — data não informada\n  - `1da0d61191c1957e46779b1ca8bf8ba6cd82600f` — feat: Implementação completa de IA local com stack profissional

🚀 Adiciona solução completa de IA local estilo ChatGPT/DeepSeek com API própria

## 📦 Componentes Principais

### Infraestrutura Docker
- docker-compose.yml configurado para CPU e GPU
- Suporte automático a NVIDIA CUDA quando disponível
- Limites de memória configurados automaticamente
- Serviços: Ollama, Open WebUI, GPT4All API, GPT4Free

### Scripts PowerShell Automatizados
- INSTALAR.ps1 - Instalação completa em um comando
- scripts/setup-completo.ps1 - Setup automático completo
- scripts/configurar-automatico.ps1 - Configuração baseada em hardware
- scripts/detectar-memoria.ps1 - Detecção automática de memória e recomendações
- scripts/up.ps1 e scripts/down.ps1 - Gerenciamento da stack
- scripts/pull-models.ps1 - Download inteligente de modelos
- scripts/configurar-deepseek-v3.ps1 - Configuração DeepSeek-V3

### Sistema de Autenticação
- Autenticação via API Keys implementada
- Suporte a signup/login completo
- Scripts para criação de usuários admin
- Configuração de segurança habilitada por padrão

### Documentação Completa
- README.md - Documentação principal e guia de uso
- GUIA_RAPIDO_ORGANIZADO.md - Guia rápido simplificado
- DEEPSEEK_V3_GUIA.md - Guia completo DeepSeek-V3
- docs/INTEGRACAO.md - Integração com VS Code, Docker, n8n
- Múltiplos guias especializados (treinamento, modelos, validação)

### Modelos de IA Suportados
- Modelos gerais: qwen2.5 (32B, 14B, 7B), llama3.1 (8B)
- Modelos de programação: qwen2.5-coder (32B, 14B), starcoder2 (7B)
- Modelos de raciocínio: DeepSeek-V3, deepseek-r1 (14B, 7B)
- Modelos multimodais: llava (34B, 13B)
- Modelos especializados: deepseek-math, mistral

### Sistema de Fine-Tuning
- Estrutura completa para treinamento de modelos próprios
- Scripts automatizados para preparação de dados
- Suporte a ModelFile e Python fine-tuning
- Exemplos e templates de dados de treinamento

### Integrações
- API OpenAI-compatible em http://localhost:3000/api/v1
- Suporte a VS Code (Continue Extension)
- Integração com Docker containers
- Integração com n8n workflows
- Exemplos em Python, Node.js, curl

### Recursos Avançados
- Detecção automática de hardware (CPU/GPU)
- Otimização automática de memória
- Sistema de fila de requisições
- Scripts de validação e diagnóstico
- Suporte a múltiplos perfis (CPU/GPU)

## 🔧 Configurações

- env.example - Template completo de configuração
- Suporte a variáveis de ambiente para personalização
- Configuração de tunables do Ollama
- Gerenciamento de limites de memória

## 📁 Estrutura do Projeto

- 96 arquivos adicionados
- 9000+ linhas de código e documentação
- Scripts PowerShell para todas as operações
- Documentação em português brasileiro completa
- Exemplos e templates incluídos

## ✅ Funcionalidades Implementadas

- ✅ Instalação automática em um comando
- ✅ Detecção automática de hardware
- ✅ Configuração otimizada por hardware
- ✅ API com autenticação por chaves
- ✅ Interface web estilo ChatGPT
- ✅ Suporte CPU e GPU automático
- ✅ Sistema de fine-tuning completo
- ✅ Integração com ferramentas populares
- ✅ Documentação detalhada em PT-BR
- ✅ Scripts de validação e diagnóstico

## 🎯 Casos de Uso

- Desenvolvimento com assistência de IA no VS Code
- Automação de workflows com n8n
- Processamento em batch com Docker
- Assistente pessoal local e privado
- Análise de documentos e imagens
- Geração de código assistida

Este commit representa a versão completa e funcional do projeto IA Local,
com todos os componentes necessários para uma experiência profissional de IA
completamente local, gratuita e privada. — data não informada
\n## 49. William-kelvem94/JARVIS-2.0

- **Registros retornados:** 12
- **Amostra:**
  - `847c9b8394f5e603ed571b3831ef2c06551c3e50` — fix: preserve unrelated node-wav type version — data não informada\n  - `a2baf5f688d50a4a9b5710d5300202cb0f0a9778` — security: update ajv to 8.18.0 — data não informada\n  - `1da6c99065bc0a10b6dc12ef301ce50bf7a262f8` — security: update python-dotenv to 1.2.2 — data não informada\n  - `b32723115dd5e13e67acfa442438b94c7e1cbe9c` — security: update requests to 2.32.4 — data não informada\n  - `7c8c4b61a940e80dbdb269e75c299a8651e35e74` — docs: clarify transitive launch-editor remediation — data não informada\n  - `ea37fbba791afaea147c55a2308b37f266e03068` — security: preserve manifest and update vulnerable dependencies — data não informada\n  - `3a5cf22bcc8e46dffafcf53619cc764993bef0e1` — docs: record security remediation notes — data não informada\n  - `91160b7f3586a23c4b693cc0268d9e771443f8b1` — security: update vulnerable bridge dependencies — data não informada\n  - `80815cc8f9606f0f2f74e8fc6ac1259de44326e6` — security: update vulnerable Node dependencies — data não informada\n  - `ca031fb9e469e6d36d83457028cf79c8ca6f32b9` — security: disable vulnerable transformers dependency — data não informada\n  - `052bdf4a744da499940291253ea0edb648c03875` — atualização

projeto estava funcionando em ingles
porém foi tentado atualizar ele para pt br e até agora ainda não foi testado se funciona ou não — data não informada\n  - `36704060a43d10927e45c035348611f3b823d9f6` — Initial commit — data não informada
\n## 50. William-kelvem94/JOGO-SANDBOX

- **Registros retornados:** 3
- **Amostra:**
  - `ef2a47ce957824505465c6f63a04835bad1022fb` — fix: Corrigir erros de compilacao no Unity

- Corrigir GUID do script ElementParticle no prefab
- Adicionar propriedades padrao do ElementPainter na cena
- Configurar GravityController com propriedades corretas
- Corrigir import SceneManagement no GameManager
- Desabilitar scripts com dependencias problematicas (GameUIManager, DemoController, NatureSandboxEditor)

Resolve erros que impediam o modo Play no Unity — data não informada\n  - `16847382b07725b980a925da8e98079dbc036084` — Sure! Pl — data não informada\n  - `b56d431aa8345b5a2431b5b03801aaf6500c9ef6` — Initial commit — data não informada
\n## 51. William-kelvem94/LEITOR-TELA

- **Registros retornados:** 7
- **Amostra:**
  - `054e1035a6b021c53d7833b718e519be937c9b65` — Code style and cleanup across modules

Apply consistent formatting and minor cleanups across the project: standardize string quotes to double quotes, add trailing commas, and normalize logging handler definitions; reformat subprocess invocations and exception handling (use BaseException in some catch-alls); tidy whitespace and line breaks; reorganize and add imports in main.py; update __all__ in package init; and perform small API-consistent adjustments in multiple core modules. Changes touch launcher, launcher_clean, main.py, setup.py, various src/core modules and tests — purely stylistic and minor robustness improvements without functional changes. — data não informada\n  - `e2a8acc37250a191d006313d9680d1c21191a06a` — feat: Evolução do Leitor de Tela para Agente de IA 'Jarvis' completo

Principais implementações:
- Núcleo do Agente (ai_agent.py): Orquestrador com integração Gemini e Ollama (Llava).
- Camada de Ação (action_controller.py): Automação de mouse e teclado via PyAutoGUI.
- Sistema de Voz Jarvis (voice_controller.py): Vozes naturais via Edge-TTS/Google e STT offline via Vosk.
- Memória Neural (neural_memory.py): Banco de vetores ChromaDB para contexto semântico e lembranças do sistema.
- Auto-Treinamento (dataset_collector.py e fine_tune_preparator.py): Coleta de dados de uso para fine-tuning de modelos locais.
- Interface Inteligente (main_window.py): Aba de chat integrada com controles de voz.
- Dockerização: Adicionado Dockerfile e docker-compose.yml para execução em ambiente isolado e integrado com Ollama.
- Inicialização unificada no main.py. — data não informada\n  - `62384bdb9bad3b7de56b3296fbfa911bc1155667` — refactor: Melhorias na estrutura e desempenho do sistema

- Otimização do código para melhor desempenho e eficiência
- Atualização das dependências para versões mais recentes
- Refinamento da interface gráfica para maior usabilidade
- Ajustes na documentação para refletir as mudanças recentes
- Implementação de melhorias de segurança e estabilidade

Essas alterações visam aprimorar a experiência do usuário e garantir um funcionamento mais robusto do sistema. — data não informada\n  - `ce8eb6a3a6811bc94a8b98b34536200b1304c83d` — fix: Sistema funcionando completamente - corrigidos problemas crÃ­ticos

- Resolvido erro de importaÃ§Ã£o 'system_helper'
- Corrigido problema de encoding Unicode no Windows CMD
- Removidos emojis incompatÃ­veis com terminal Windows
- Simplificado requirements.txt removendo dependÃªncias opcionais
- Criado launcher limpo sem caracteres especiais
- Sistema agora inicia automaticamente e funciona perfeitamente

O sistema estÃ¡ 100% funcional:
âœ… Launcher inteligente detecta configuraÃ§Ã£o
âœ… Instala dependÃªncias automaticamente se necessÃ¡rio
âœ… Executa aplicaÃ§Ã£o completa sem erros
âœ… Interface grÃ¡fica carrega corretamente
âœ… Todos os mÃ³dulos essenciais funcionando

Para usar: apenas clique duplo em LeitorTela.bat — data não informada\n  - `f26ac5eb04d38b9bce82535ff6f454a700dcf967` — feat: Melhorar interaÃ§Ã£o e usabilidade do launcher

- Implementar modo automÃ¡tico inteligente no launcher
- Remover menu interativo confuso, adicionar modo direto
- Adicionar argumentos de linha de comando mais intuitivos
- Melhorar LeitorTela.bat com modos especÃ­ficos
- Atualizar documentaÃ§Ã£o com instruÃ§Ãµes mais claras
- Sistema agora detecta automaticamente o que precisa fazer
- Remover dependÃªncias desnecessÃ¡rias e simplificar estrutura

UsuÃ¡rio agora pode simplesmente clicar em LeitorTela.bat
e o sistema cuida de tudo automaticamente. — data não informada\n  - `5ec8a9d70f7d0fd33f5530acf1fdbb939c994f13` — feat: Sistema profissional finalizado - Leitor de Tela Inteligente

- ImplementaÃ§Ã£o completa do sistema de captura e anÃ¡lise de tela
- Arquitetura modular com core, gui, database e utils
- OCR hÃ­brido com Tesseract e EasyOCR
- AnÃ¡lise inteligente com spaCy e processamento de linguagem natural
- Interface grÃ¡fica moderna com CustomTkinter
- Sistema de banco de dados SQLAlchemy com persistÃªncia completa
- ExportaÃ§Ã£o mÃºltipla (JSON, CSV, Excel, PDF)
- Launcher profissional com diagnÃ³stico automÃ¡tico
- DocumentaÃ§Ã£o tÃ©cnica completa
- Testes automatizados com pytest
- Sistema de configuraÃ§Ã£o avanÃ§ado
- Logs estruturados e tratamento de erros robusto
- Suporte multiplataforma (Windows/Linux/macOS)

Sistema totalmente funcional para extraÃ§Ã£o inteligente de dados visuais. — data não informada\n  - `1912788cbc0bbe9352a64197f4027ce38565457d` — feat: Adicionar estrutura inicial do projeto e funcionalidades core do Leitor de Tela Inteligente

- Criado .gitignore para excluir arquivos e diretórios desnecessários
- Adicionados COMO_INICIAR.txt e INSTRUCOES_INICIO.txt com instruções para iniciar o projeto
- Implementados scripts INICIAR.py e instalar_rapido.py para instalação automática de dependências e inicialização da aplicação
- Desenvolvidos scripts install_and_run.bat e install_and_run.ps1 para usuários Windows e PowerShell, respectivamente
- Introduzido main.py como ponto de entrada da aplicação, junto com README.md abrangente e requirements.txt para dependências
- Estabelecida estrutura básica de diretórios com pastas src, tests e documentação
- Incluídos modelos iniciais de banco de dados e funcionalidades core para captura de tela, processamento OCR e análise de dados
- Configurado logging e gerenciamento de configurações para melhor monitoramento da aplicação e controle de configurações
- Adicionado pytest.ini para configuração de testes e casos de teste iniciais para configuração e funções auxiliares
- Criadas funcionalidades avançadas e diretrizes de contribuição na documentação

Este commit estabelece a base para o Leitor de Tela Inteligente, permitindo aos usuários capturar, processar e analisar dados de tela de forma eficaz. — data não informada
\n## 52. William-kelvem94/MEU_NECTAR_JARVIS

- **Registros retornados:** 7
- **Amostra:**
  - `37cea79b9ed580721c31f8d8590cdadc36727059` — feat: implementação completa de melhorias de performance, acessibilidade e robustez

✨ Funcionalidades Adicionadas:
- Índices de banco de dados para otimização de queries (userId, createdAt, status)
- Paginação em todas as listagens (tasks, habits, finances) com limite de 100 itens
- Exception filters customizados para tratamento de erros robusto
- Logging interceptor estruturado com sanitização de dados sensíveis
- System prompts melhorados com exemplos few-shot e instruções específicas
- Parsing mais robusto com múltiplas tentativas e correção automática de JSON
- Validação rigorosa de dados extraídos (tipos, ranges, datas, enums)
- Otimização de contexto IA (limite de 2000 tokens, compressão inteligente)
- Acessibilidade completa (ARIA labels, navegação por teclado, screen readers)
- React.memo em componentes pesados (MessageBubble, ChatCard)
- Otimização de queries React Query (staleTime, gcTime)
- Hook useDebounce para otimizar buscas
- Testes unitários com Jest e configuração de CI/CD
- Documentação JSDoc/TSDoc em serviços principais

🔧 Melhorias Técnicas:
- Performance de queries usando select para buscar apenas campos necessários
- Atualização de tarefas atrasadas em batch (mais eficiente)
- Tratamento de erros com mensagens sanitizadas para produção
- Contexto IA limitado a 2000 tokens com compressão inteligente
- Cache de queries React Query otimizado (2-5 minutos staleTime)
- Batch operations para atualização de tarefas atrasadas

🐛 Correções:
- Duplicação de scripts no package.json
- Queries N+1 através de índices e select otimizado

📁 Novos Módulos e Arquivos:
- backend/src/common/ (filters, interceptors)
- backend/src/auth/decorators/
- backend/src/banks/
- backend/src/credit-cards/
- backend/src/payment-methods/
- backend/src/files/
- backend/src/alexa/
- backend/src/whatsapp/
- frontend/src/lib/hooks/useDebounce.ts
- frontend/src/components/FileUpload.tsx
- .github/workflows/ (CI/CD)
- CHANGELOG.md
- MELHORIAS-IMPLEMENTADAS.md

📊 Impacto:
- Redução estimada de 30-50% no tempo de resposta de queries
- Redução de ~40% em re-renderizações desnecessárias no frontend
- 100% das exceções capturadas e logadas
- Taxa de sucesso de parsing aumentada significativamente
- Conformidade WCAG AA melhorada — data não informada\n  - `81488123f07c148ebb75426139cf0766d3e3543a` — Merge branch 'main' of https://github.com/William-kelvem94/MEU_NECTAR_JARVIS — data não informada\n  - `e602aa4dc1bc6ed261896781581056cf90c6ac8e` — Implement full feature set: notifications, export, templates, hardware detection, and streaming

Adds hardware auto-detection (CPU/GPU) and optimal model selection to the AI local service, with a new hardware_detector.py module. Implements real-time streaming responses via WebSocket, improved context management with recent message history, and context caching. Backend gains modules for notifications (WebSocket), export/import (JSON, CSV, Excel), search, and templates, with corresponding Prisma migrations and schema updates. Frontend receives new components (MarkdownRenderer, NotificationCenter, GlobalSearch, AdvancedFilters, GroupedList, VoiceInput, etc.), cyberpunk theming, and pages for export and templates. Docker setup, troubleshooting, and documentation are updated to reflect the complete, production-ready system. — data não informada\n  - `067ec50ea43c6da310a1f0d7f21c1bc18f31c4b6` — Melhoriass — data não informada\n  - `ae775cb77af40d4c5827700c1bd97a6faca79e68` — Implement full dashboard and advanced modules

Added complete dashboard pages and modules for brain dumps, diary, finances (with recurrences and installments), reminders, projects, habits, tasks, and briefing. Updated backend with new controllers, services, DTOs, and Prisma schema/migrations to support new features. Enhanced AI local service with Whisper-based audio transcription, improved health checks, and Dockerfile updates. Frontend now includes new dashboard sections, components, and dark mode support. Documentation and implementation status files were added for project tracking. — data não informada\n  - `940617ca90b3477f35b20d18bbf9fb54156d726f` — Update Dockerfiles and compose for improved dev workflow

Refactored Dockerfiles for ai-local, backend, and frontend to improve compatibility and development experience. Backend now installs OpenSSL for Prisma, uses 'npm install' instead of 'npm ci', and defaults to development mode. The compose file now uses 'prisma db push' for schema sync. Added missing 'next-env.d.ts' to frontend for Next.js TypeScript support. — data não informada\n  - `6dab0f3e5b62257dd4508ae4ce4c91829143e8fe` — Initial commit — data não informada
\n## 53. William-kelvem94/MONITORADOR-ANTIGRAVITY

- **Registros retornados:** 1
- **Amostra:**
  - `919d30260bde6cf983cc35f3385721f7592bc839` — Initial commit — data não informada
\n## 54. William-kelvem94/Movimentador_de_arquivo

- **Registros retornados:** 8
- **Amostra:**
  - `6852d591bf14bb50d6dee3b893f5cf8125e8fa6a` — feat: reorganizar motor e validar organizador

- separa o nucleo de organizacao em organization_core para concentrar regras, duplicados, journal e reversao
- reduz processador a uma fachada fina e mantém a interface usando a mesma base funcional
- adiciona regras com prioridade e destino sugerido, alem de suporte a estrategia de organizacao
- melhora o launcher do Windows para abrir com Python 3.11 instalado localmente
- inclui testes unitarios e de integracao em ambiente temporario com tempfile
- valida o fluxo com compilacao e smoke tests apos a refatoracao — data não informada\n  - `df4e9f670d75da820c7b69a929fe423f14f1d447` — feat: transformar organizador em app configuravel

- adiciona launcher Windows usando a .venv para abrir o projeto de forma limpa
- cria README com a proposta do produto e o fluxo de uso
- implementa regras inteligentes para WhatsApp, notas fiscais, trabalho e estudos
- adiciona painel editavel de regras com incluir, editar, remover e reordenar
- melhora a tela de duplicados com decisao manual e fluxo visual mais claro
- separa a aba de limpeza do fluxo principal de organizacao
- ajusta o ponto de entrada e o processamento para reduzir dependencia do terminal — data não informada\n  - `ba014329fa654f03dba8494b3d7a89f110683d6d` — melhorias 34x

Correção de erros e melhorias na interface do Organizador de Arquivos

- Corrigido erro de sintaxe no arquivo `interface.py`.
- Adicionada a classe `ProcessingThread` para gerenciar o processamento de arquivos em uma thread separada.
- Implementada a interface gráfica do usuário (GUI) usando PyQt5 na classe `MainWindow`.
- Adicionados métodos para configurar temas (claro e escuro) na interface.
- Melhorada a organização do código com métodos específicos para adicionar, remover e selecionar pastas.
- Implementado monitoramento do sistema (CPU, memória e disco) na interface.
- Adicionado tratamento de exceções para capturar e exibir erros durante o processamento.
- Atualizado o arquivo `requirements.txt` com as dependências necessárias (PyQt5 e psutil).
- Criado o script `iniciar_projeto.bat` para ativar o ambiente virtual e iniciar a aplicação.
- Melhorada a responsividade e a usabilidade da interface. — data não informada\n  - `f38f2ef18c69e31cbc4a3f2cf97abac8341c9dc5` — Melhorias

Refatoração e melhorias no projeto Organizador de Arquivos

- Adicionada a classe `ProcessingThread` para gerenciar o processamento de arquivos em uma thread separada.
- Implementada a interface gráfica do usuário (GUI) usando PyQt5 na classe `MainWindow`.
- Adicionados métodos para configurar temas (claro e escuro) na interface.
- Melhorada a organização do código com métodos específicos para adicionar, remover e selecionar pastas.
- Implementado monitoramento do sistema (CPU, memória e disco) na interface.
- Adicionado tratamento de exceções para capturar e exibir erros durante o processamento.
- Atualizado o arquivo `requirements.txt` com as dependências necessárias (PyQt5 e psutil).
- Criado o script `iniciar_projeto.bat` para ativar o ambiente virtual e iniciar a aplicação.
- Melhorada a responsividade e a usabilidade da interface. — data não informada\n  - `e5218925deb4e1e9f8e40defbe4b3aee9f9433a7` — Adiciona .gitignore — data não informada\n  - `86673184fcd5a14a65dfea6916568e45db8fba13` — Initial commit — data não informada\n  - `248459268ace442d4ca52ae4225e881aae91a479` — Initial commit — data não informada\n  - `4c56f790b9e4c5fcd58a9b0dce5531ddeae3987b` — Initial commit — data não informada
\n## 55. William-kelvem94/NEXUS-VENDAS

- **Registros retornados:** 11
- **Amostra:**
  - `e63485ad22f4f940538cfc0129abb6c1196702f0` — Refactor frontend structure and add profile update endpoints

Major frontend restructuring: removed legacy files, added new app directory with updated layout, pages, and components, and updated configuration files for Next.js 14. Added endpoints in backend auth module for updating user profile and password. Dockerfile updated for more robust Prisma generation and dependency handling. — data não informada\n  - `5fb42f3c26c06264d96f7d47e57a46eb70f70b66` — Improve auth forms validation and error handling UX

Adds client-side validation to login and register forms, improves error message display with icons and dismiss buttons, and ensures form fields are not cleared on error. Refactors API error handling for more robust and user-friendly messages. Updates dashboard user management to use the shared API utility and toast notifications for feedback. — data não informada\n  - `d070df0b7f8ffe39fe35ca9d4674e013288a80bd` — Refactor API usage and improve Dockerfile build steps

Refactored frontend authentication logic to use a centralized api function for login and registration, reducing code duplication and improving maintainability. Updated the api function to handle body serialization more robustly. Improved Dockerfile build steps to ensure correct bcrypt compilation and dependency installation order. — data não informada\n  - `1dbdfc881a44bd07ea9f30b01966893fe020483b` — Implement Nexus Vendas branding and dashboard improvements

Rebrand the application from 'Koop Vendas' to 'Nexus Vendas' across documentation, environment variables, and UI. Add Dockerfile, docker-compose, and PM2 ecosystem config for unified deployment. Refactor frontend dashboard and clients page with new components, improved UI/UX, client debt display, CSV export, pagination, and enhanced feedback. Update dependencies and add new utility hooks and components for notifications, validation, and sidebar navigation. — data não informada\n  - `999c247b43f736b15043ccb9e440b4ed718bba1e` — Add expenses module and restructure dashboard/auth routes

Introduces a new expenses module to the backend with controller, service, DTOs, and module registration. Updates backend modules to import PrismaModule where needed. Renames all references from 'koop-vendas' to 'nexus-vendas' across backend, frontend, Docker, and documentation. Refactors frontend routing to use (auth) and (dashboard) layouts, moving and updating pages accordingly. Adds new login and register pages with modern UI, updates logo and project branding, and improves .dockerignore files. Updates docker-compose and documentation for new naming and structure. — data não informada\n  - `8da6c772235b4cc5ab7d5e81506b1e0ee095a117` — feat: implement multi-tenancy and user role management

- Updated ProductsService to associate products with users.
- Modified ReportsController to change API endpoint path.
- Enhanced SalesController and SalesService to include user ID in sales operations.
- Added user authentication and authorization in the frontend with protected routes.
- Created login and registration pages with form validation.
- Implemented user management for secondary users by master users.
- Introduced badges for user status indication.
- Added API error handling and token management in the frontend.
- Created database migration for multi-tenancy with user roles and relationships. — data não informada\n  - `03108b14799d3120dfb6f1f06b3bb94634efdc72` — feat: implement multi-tenancy authentication with JWT and user management

- Added AuthModule with JWT and local strategies for user authentication.
- Created endpoints for user registration, login, and secondary user management.
- Implemented guards for protecting routes and ensuring user roles.
- Updated ReportsController to include user-specific data filtering.
- Enhanced Prisma schema to support multi-tenancy with user associations.
- Removed old migration files and created a new migration for the updated schema.
- Updated package.json with necessary dependencies for authentication.
- Implemented theme provider and toggle for UI theme management. — data não informada\n  - `51570566ae5ff94146485e2bddb2d911c6b979b3` — feat: restructure layout and enhance UI components

- Updated RootLayout to include a sidebar navigation with icons for better user experience.
- Enhanced HomePage with a welcoming message and improved card layout for product management.
- Implemented ProductsPage with CRUD functionality using React Query for data fetching and state management.
- Added new UI components: Button, Card, Dialog, Input, Label, Table, and utility functions for better styling and functionality.
- Introduced Tailwind CSS configuration for dark mode and custom theming.
- Created initial Prisma migration for database schema including Products, Clients, Sales, and related entities.
- Improved API error handling and response formatting. — data não informada\n  - `355b605ab66af74e54dd4559b01275489b09cf9d` — feat: initialize frontend with Next.js, Tailwind CSS, and TypeScript

- Add package.json with dependencies for Next.js, React, and Tailwind CSS
- Configure PostCSS with Tailwind CSS and Autoprefixer
- Create logo.svg for branding
- Implement Clients, Dashboard, Home, Products, Reports, and Sales pages with basic layout
- Add global styles using Tailwind CSS
- Set up API utility for fetching products
- Configure Tailwind CSS with content paths
- Set up TypeScript configuration for the project — data não informada\n  - `cca513fbcb43f3a94b3f9835f0754014de6e38a9` — Add initial NestJS backend with sales, products, and clients modules

Introduces a new backend project using NestJS, Prisma, and SQLite (dev) with modules for products, clients, sales, and reports. Includes Prisma schema for products, clients, sales, payments, and expenses, as well as CRUD endpoints for products and clients, sales creation with stock management and installments, and a basic reports summary endpoint. Adds environment example, project configuration, and updates the README with setup and API documentation. — data não informada\n  - `759a112ead23f06edb0c460d3319412e5ca1780c` — Initial commit — data não informada
\n## 56. William-kelvem94/openclaude-wk

- **Registros retornados:** 100
- **Amostra:**
  - `aac2d8cdc8368d404bb1fba56bf69a9da5279e19` — fix(openai-shim): guard tool-arg field lookup against prototype keys (#1880)

STRING_ARGUMENT_TOOL_FIELDS is a plain-object lookup table keyed by a
provider-supplied tool-call name. hasToolFieldMapping used `name in table` and
getPlainStringToolArgumentField used a bare `table[name]` lookup, both of which
resolve inherited Object.prototype members. A tool call whose function.name is
'constructor', 'toString', '__proto__', etc. therefore reported a field mapping
(the Object constructor function), which is truthy, so the `?? null` fallback
never fired and normalizeToolArguments wrapped a JSON-encoded string argument
into a garbage-keyed object ({ 'function Object() { [native code] }': value })
instead of passing it through. Gate both lookups on Object.hasOwn, matching the
codebase convention for provider-keyed maps.

Consumers: src/services/api/openaiShim.ts (normalizeToolArguments /
hasToolFieldMapping over decoded tool_calls[i].function.name). — data não informada\n  - `2f98208eafdc121f3d8308060016ee7363519ac7` — fix(command-semantics): treat linter exit 1 as violations, not an error (#1846)

* fix(command-semantics): treat linter exit 1 as violations, not an error

Linters and formatters use exit code 1 to mean "violations found", not a
crash. commandSemantics fell back to DEFAULT_SEMANTIC for ruff/eslint, so a
run that merely reported lint findings was flagged isError: true and the
model retried the same command up to 3 times before giving up (observed on
Windows with `uvx ruff check --fix`).

Add a LINT_SEMANTIC (exit 1 = violations found, 2+ = real error, mirroring
the existing grep/diff pattern) for ruff and eslint, in both the Bash and
PowerShell tables. Wrapper runners (uvx, npx) inherit the wrapped tool's
semantics only when it resolves to a recognized command — an unrecognized
wrapped tool still falls back to the default, so `uvx <arbitrary>` is not
blanket-treated as non-error.

Adds coverage for ruff/eslint exit codes and the uvx/npx unwrap (including
the unknown-wrapper fallback) in both Bash and PowerShell suites.

* fix(command-semantics): normalize path-prefixed and quoted Bash linters

extractBaseCommand returned the raw first token, so path-prefixed or quoted
invocations (./node_modules/.bin/eslint, "ruff", /usr/bin/uvx ruff, npx
./node_modules/.bin/eslint) fell through to default exit-code semantics and a
linter's exit 1 was mis-reported as an error. Normalize the base and wrapped
command names (strip surrounding quotes and any path prefix) like the
PowerShell implementation does, and match the wrapper by its normalized name.
Adds regression coverage for path-prefixed and quoted linter/wrapper commands.

* fix(command-semantics): normalize Windows .cmd/.bat/.ps1 shims on PowerShell path

extractBaseCommand only stripped .exe, so npm-installed tools and wrappers
invoked via their Windows .cmd shims (eslint.cmd, npx.cmd,
. — data não informada\n  - `5105dff5f4fe05d1fd177bc62c7712c9ff5374e0` — fix(config): recover from a healthy backup when the global config is corrupt (#1819)

* fix(config): recover from a healthy backup when the global config is corrupt

A present-but-corrupt ~/.openclaude.json took getConfig down the
ConfigParseError path, which reset to defaults (silently discarding the
user's settings) or re-threw, even though healthy timestamped backups exist
in ~/.claude/backups. getConfig only consulted a backup on ENOENT, and then
only to print a manual 'cp' hint. Now a corrupt parse first tries to recover
the most recent backup that still parses (merged over defaults) before doing
anything destructive, so a one-off bad write no longer wipes config or
crashes startup. Falls back to the existing defaults path when no backup is
usable. Adds direct unit tests for the recovery helper.

Closes #1807

* fix(config): iterate backups on recovery and skip rotating a corrupt file

Address review on #1819:

- recoverConfigFromBackup only tried the single newest backup, so a corrupt
  newest .backup left startup on the corrupted-config fallback even when an
  older healthy snapshot existed. Add listBackupsNewestFirst and iterate
  candidates newest-first, recovering from the first that parses. Added a
  newest-corrupt/older-healthy regression test.

- saveGlobalConfig copied the live file into the backup rotation before
  writing. After an in-memory recovery the on-disk file is still corrupt, so
  that copy poisoned the rotation with the same bad content. Only rotate the
  current file into backups when it parses.

* fix(config): never prune backups while the live config is corrupt

Address review: the MAX_BACKUPS cleanup ran unconditionally, so when the live
config is corrupt and only an older snapshot is healthy, startup's
runMigrations() -> saveGlobalConfig() could unlink that last usable backup
before the recovered config is durably written (#1807).

Extract the prune decision into a pure, exported selectBackupsToPrune() that
returns [] whenever the live config fails to parse, and gate the cleanup loop
on it. Hoist the parse check so both the backup-copy and the prune paths share
it.

Add production-path coverage: getConfig recovery via _getConfigForTesting
(corrupt live config -> healthy backup, and newest-corrupt -> older-healthy),
plus direct selectBackupsToPrune tests (corrupt -> prunes nothing; healthy ->
keeps newest maxBackups).

* fix(config): skip valid-but-non-object backups during recovery

recoverConfigFromBackup() returned the first backup that parsed, even
when the parsed value was not a config object. A newest backup holding
valid JSON like null, [], or a bare string spread into bare defaults or
index/char keys and stopped, discarding the older healthy snapshots the
#1807 recovery is meant to fall through to. Guard that parsedBackup is a
non-null, non-array object before returning; otherwise continue to the
next older backup.

Adds a regression test: a valid-but-unusable newest backup (null) is
skipped in favor of an older healthy one.

* fix(config): recover global config from legacy backups and self-heal corrupt startup

Two gaps in the #1807 recovery path surfaced in review:

- listBackupsNewestFirst filtered only on the active basename, so once the
  global config is .openclaude.json it never tried the pre-rename
  .claude.json.backup.* snapshots that #1807 reports as the only surviving
  clean source. Recover the global config from the legacy basename too, and
  order backups by their .backup.<ts> timestamp so current and legacy
  snapshots interleave by recency instead of grouping by filename.
- enableConfigs validated the global config with the throwing mode, so a
  corrupt config with no usable backup rethrew ConfigParseError through
  startup and locked users out on every launch. Drop the throwing mode so the
  corrupt-file/default fallback runs and startup self-heals.

Adds regression coverage: legacy-basename recovery plus a scoping guard, and
an enableConfigs no-crash test for the unrecoverable corrupt-config case.

* test(config): re-register real env module after startup validation test

The enableConfigs (#1807) regression test installs mock.module('./env.js', ...)
so getGlobalClaudeFile() points at the virtual config path. Bun's mock.module()
is process-global and is not undone by mock.restore(), so the teardown that only
reset the fs implementation left later same-process tests importing ./env.js on
the virtual path. Capture the real env module once in beforeAll and re-register
it in afterEach alongside the fs reset, matching the established restore pattern
in user.test.ts/effort.test.ts.

---------

Co-authored-by: Pablosinyores <nikhilbajaj0182@gmail.com> — data não informada\n  - `f7d472e826d28d798931f48d0cf09c23387bcc2f` — fix(provider): add Use Anthropic option to switch back from third-party profiles (#1429)

* fix(provider): add Use Anthropic option to switch back from third-party profiles

The /provider menu offered no way back to built-in Anthropic once any
third-party provider profile was active: getActiveProviderProfile falls
back to profiles[0] when activeProviderProfileId is unset, so clearing
the active id still re-selected a saved profile. Users had to hand-edit
~/.openclaude.json and restart.

Add an explicit ANTHROPIC_DEFAULT_PROFILE_ID sentinel that getActive-
ProviderProfile resolves to undefined (Anthropic) instead of profiles[0],
and a clearActiveProviderProfile() that records the sentinel, clears the
managed provider env in-session, and removes the startup profile mirror.
Surface it as a 'Use Anthropic (built-in)' choice in /provider, shown
whenever the current provider is not Anthropic. Saved profiles are kept
for re-selection; the switch takes effect without a restart.

Fixes #1426

* fix(provider): wire Use Anthropic into live ProviderManager and keep the sentinel

Addresses review feedback on #1429:

- The "Use Anthropic (built-in)" option now lives in the live ProviderManager
  "Set active provider" flow (the wizard path is test-only). It is offered only
  when a third-party profile or GitHub Models is currently active, and routes
  through clearActiveProviderProfile() + resets the session model to the
  built-in Anthropic default so the switch takes effect without a restart.

- Teach the add/update/delete fallbacks that ANTHROPIC_DEFAULT_PROFILE_ID is a
  valid active state. Previously, adding a profile with makeActive:false,
  updating any profile, or deleting an inactive profile while on built-in
  Anthropic would silently reactivate profiles[0], switching the user back to a
  third-party provider. The delete path also no longer resolves the sentinel to
  profiles[0] when re-applying env.

Added regression tests covering the add/update/delete sentinel-preservation
paths.

* fix(provider): clear startup provider overrides when switching back to Anthropic

The /provider Anthropic activation branch cleared the managed session env
and the startup profile file but left the startup provider override in user
settings intact, so a restart would replay the third-party provider. Clear it
the same way the saved-profile and GitHub paths do, surfacing any cleanup
failure as a warning. Also assert the managed provider env is removed in the
clearActiveProviderProfile session-env test.

* fix(provider): clear startup overrides from /provider Anthropic branch; honor makeActive:false for implicit-active profiles

Addresses two review findings on #1429:

- The /provider 'Use Anthropic (built-in)' branch only called
  clearActiveProviderProfile(), so settings-backed startup overrides
  (CLAUDE_CODE_USE_OPENAI / OPENAI_BASE_URL / API key) survived and
  re-selected the third-party provider on restart. It now also calls
  clearStartupProviderOverrides() and surfaces a cleanup warning in the
  onDone message instead of reporting unconditional success, mirroring the
  ProviderManager Anthropic branch.

- addProviderProfile(makeActive:false) still promoted the new profile when
  activeProviderProfileId was unset but saved profiles existed, because
  getActiveProviderProfile() implicitly resolves that state to the first
  profile while the old ternary treated !currentActive as 'no active'.
  Resolve the effective active state (sentinel, explicit id, or implicit
  first profile) before deciding, so makeActive:false never silently
  switches the active provider. Adds a regression test for the
  implicit-first-profile case (fails on the old ternary).

* fix(provider): honor stale active id and clear hydrated GitHub token on Anthropic switch

Addresses two findings on the switch-back-to-Anthropic path (#1426).

P2 — stale active profile id (providerProfiles.ts):
addProviderProfile's makeActive:false guard only preserved the
implicit-first-profile case when activeProviderProfileId was unset. If the
config carried an id for a deleted/missing profile, the guard treated it as "no
active" and promoted the newly added profile, ignoring makeActive:false — even
though getActiveProviderProfile() resolves a stale id to profiles[0]. Resolve an
effectiveActiveId the same way getActiveProviderProfile does (sentinel ->
built-in Anthropic, valid id -> that profile, stale/unset id with profiles ->
implicit first, none -> nothing active) and keep it when makeActive:false.
+regression test for the stale-id case (fails on the old guard).

P2 — hydrated GitHub token leak (ProviderManager.tsx):
Selecting "Use Anthropic (built-in)" while GitHub Models was active called only
clearActiveProviderProfile(), which clears managed flags but leaves a
GITHUB_TOKEN hydrated from secure storage (and its marker) in the session.
Mirror the GitHub delete path: new clearHydratedGithubModelsTokenFromEnv() drops
the hydrated token + marker while preserving a user-supplied token (one that
does not match the stored credential). +unit tests for match / user-supplied /
empty-storage / no-marker cases.

* fix(provider): keep switch-back reachable when a non-Anthropic provider is active

hasSelectableProviders gated the 'Set active provider' menu item, so when a
non-Anthropic provider (GitHub Models or a saved profile) was active but no
profile was saved and GitHub credentials were unavailable, the 'Use Anthropic
(built-in)' recovery option was unreachable. Add a scoped canSwitchActiveProvider
(true whenever GitHub is active or a profile is active) for the activate path
only; edit/delete still require an actual profile.

Add a ProviderManager UI test for the switch-back flow: select 'Use Anthropic
(built-in)' and assert the onDone state (provider name, model reset) and that no
managed CLAUDE_CODE_USE_* flags remain.

* fix(provider): drop dead wizard switch-back path, dedup switch guard

Address review on the legacy ProviderWizard 'anthropic' branch. ProviderWizard
is test-only (live /provider renders ProviderManager), so its switch-back option
duplicated the real path while diverging from it (no hydrated-GitHub-token
cleanup, no model reset) and went untested. Remove the wizard's 'Use Anthropic'
option, its handler branch, the now-unused ProviderChoice member, and the imports
only it used, leaving the single tested switch-back in ProviderManager.

Also reuse the component-scope canSwitchActiveProvider in renderMenu instead of
recomputing it, so the two sites cannot drift.

* test(provider): restore env + dispose mount in finally, assert token cleanup

Address review on the switch-back manager-UI test: snapshot and restore the
mutated process env and dispose the Ink mount in a finally block so a failed
wait or assertion cannot leak provider flags or a live mount into later tests,
and assert clearHydratedGithubModelsTokenFromEnv was called so dropping the
hydrated GitHub token cleanup cannot pass unnoticed.

* test(provider): assert switch-back forwards stored GitHub Models token

The switch-back test seeded no stored token (readGithubModelsToken
returned undefined) and only asserted clearHydratedGithubModelsTokenFromEnv
was called, so it would still pass if the branch stopped forwarding the
stored token into the helper. Seed a stored token and assert
toHaveBeenCalledWith(storedToken) so the regression covers the exact
GitHub Models switch-back path that preserves a user-supplied
GITHUB_TOKEN while clearing only the hydrated secure-storage token.

* fix(provider): keep built-in Anthropic active through the startup fallback

applyActiveProviderProfileFromConfig() returned without marking provider
env as handled for the Anthropic sentinel (getActiveProviderProfile resolves
it to undefined). On a cold start after clearActiveProviderProfile() deleted
the profile mirror, buildStartupEnvFromProfile() then treated the missing
file as a fresh install and synthesized the default Gitlawb OpenGateway env,
moving the user off built-in Anthropic. Clear managed provider env and set
the applied flag for the sentinel so the fresh-install fallback is suppressed;
an explicit startup provider selection still wins. Adds a cold-start
regression test.

* test(provider): assert startup-override cleanup and isolate cold-start env

Address review findings:
- ProviderManager switch-back test now anchors on the mocked
  clearStartupProviderOverrides symbol and asserts the Anthropic branch calls
  it, so the test fails if that call is dropped and a restart replays the
  third-party provider (proven fail-on-removal).
- Cold-start sentinel test snapshots and clears every CLAUDE_CODE_USE_* flag
  (OpenAI/GitHub/Gemini/Mistral/Bedrock/Vertex/Foundry) plus the base-url/model
  and applied markers, restoring them in finally, so an inherited provider flag
  can no longer route it down the explicit-selection path or leak into later
  tests.

* fix(provider): undo Copilot-key hydration on env cleanup

hydrateGithubModelsTokenFromSecureStorage() has two hydration modes: a
copilot_key blob populates GITHUB_COPILOT_KEY, while an OAuth blob
populates GITHUB_TOKEN. clearHydratedGithubModelsTokenFromEnv() only
cleared GITHUB_TOKEN, so undoing a copilot_key hydration removed the
ownership marker while leaving the hydrated Copilot key in the session.
Clear the GITHUB_COPILOT_KEY branch symmetrically (same stored-token
match guard that preserves a user-supplied value).

Adds helper coverage for both Copilot-key cases (matched key cleared;
user-supplied differing key preserved).

* fix(provider): revert hydrated Copilot key on GitHub provider delete

The GitHub Models delete path hand-rolled its own env cleanup that only
dropped GITHUB_TOKEN, so a hydrated copilot_key (stored in GITHUB_COPILOT_KEY
under the same marker) was left behind once the marker was removed. Delegate
to the shared clearHydratedGithubModelsTokenFromEnv helper so the delete flow
reverts both hydration modes consistently with the switch-back path, and add
a ProviderManager delete-flow regression test.

* test(provider): assert switch-back refreshes session AppState model

Capture AppState updates via onChangeAppState in the switch-back test and
assert the Use Anthropic (built-in) path sets mainLoopModel to the Anthropic
model from the result and clears mainLoopModelForSession to null. Without
this the test would still pass if the setAppState block regressed, leaving a
running session on the previous provider model. — data não informada\n  - `a46046ee90a4efe292d7c0b404c58382f7e43133` — fix(proxy): bypass subdomains for a bare NO_PROXY domain entry (#1848)

* fix(proxy): bypass subdomains for a bare NO_PROXY domain entry

shouldBypassProxy matched a bare NO_PROXY entry (`example.com`) against the
request host exactly, so a subdomain like `api.example.com` was routed THROUGH
the proxy. But this module also drives undici's EnvHttpProxyAgent via
getProxyAgent, and that path bypasses subdomains for a bare entry (matching the
curl/Go/deno NO_PROXY convention). The result was that the same
`NO_PROXY=example.com` produced different decisions for the same host depending
on transport: bypassed on the fetch/undici path, proxied on the axios/WebSocket
path.

Match a bare domain against the host and any subdomain, aligning both paths. A
lookalike such as `notexample.com` still does not match (the leading dot is
required), and an IP-address entry can never gain a spurious subdomain match.

* fix(proxy): align port-qualified and wildcard NO_PROXY entries with undici

Two more spots where shouldBypassProxy diverged from the undici
EnvHttpProxyAgent path this module also drives via getProxyAgent:

- Port-qualified entries compared the whole `host:port` string, so
  `NO_PROXY=example.com:8080` bypassed `example.com:8080` but proxied
  `api.example.com:8080`. Parse the port off first (mirroring undici's
  `/^(.+):(\d+)$/`), require it to match, then apply the same
  exact-or-subdomain host predicate.
- Leading-wildcard entries like `*.example.com` were treated as literal
  hostnames, so they never matched a subdomain. undici strips the leading
  `*.` (upstream proxy lists use `*.githubusercontent.com`); normalize it to
  the leading-dot suffix form before matching.

Extends the regression coverage with the `api.example.com:8080` and
`*.example.com` cases.

* test(proxy): document IP-literal NO_PROXY exact-match boundary

An all-numeric final label (e.g. 10.1.2.3.4) is not a valid WHATWG URL, so
such a host never reaches the bare-domain subdomain-suffix arm; add coverage
that the would-be dotted-IP subdomain of a bare IP entry does not bypass, plus
a bracketed IPv6 exact-match case. — data não informada\n  - `67bebbdaca9efc93f4fd5ecfe75dfda9b9a49bed` — fix(bg): match background-session command args on token boundaries (#1834)

* fix(bg): match background-session command args on token boundaries

commandLineContainsArgs matched each stored launch arg as a raw
substring, so a selector like "1642" was satisfied by an unrelated live
token "16420" in the same position. A reused PID whose command line
merely contained the stored digits could therefore keep a dead session
classified as running, and the kill path could target the wrong
process.

Match each stored arg against a whole whitespace-delimited token, in
order, instead of a substring. Add regression coverage through
isBackgroundSessionProcessAlive for the collision, the exact-token
match, the session-id match, and the dead-process case.

Refs #1770

* fix(bg): match the session id on token boundaries and span multi-word args

Address review on #1770:

- commandLineMatchesBackgroundSession matched session.sessionId with a raw
  includes(), so a short id like 'sess-1' matched an unrelated live command
  containing 'sess-100' and kept a reused-PID session classified as running.
  Route it through the same whole-token matcher.
- commandLineContainsArgs required each stored arg to equal a single token, so
  a prompt stored as one argv entry (e.g. 'refactor auth') never matched the
  words ps renders it as, breaking --from-pr/resume launches that rely on the
  stored command. Expand each arg into its own tokens and match the flattened
  sequence as an ordered subsequence.

Add regression tests: session-id substring collision stays dead, exact id
token is alive, and a multi-word prompt arg matches across command tokens
(all proven fail-on-old).

* fix(bg): require background-session args to match as a contiguous token run

The token-boundary matcher for background-session process identity treated
the stored argv tokens as an ordered subsequence of the live command line, so
unrelated tokens between matches were skipped. A reused PID whose command
interleaves the stored tokens (e.g. stored [node, openclaude, 1642] against
"node attacker openclaude extra 1642 --serve") was still classified alive,
keeping the wrong-process kill risk open for token-insertion collisions.

Match the flattened stored argv as one contiguous whole-token run instead.
Leading interpreter path and trailing flags still match; interspersed tokens
no longer do. Add a regression test asserting an interspersed-token command
line is rejected (fails on the prior subsequence matcher, passes now).

Refs #1770

* fix(bg): trim quotes so Windows quoted command lines match stored argv

Get-CimInstance CommandLine returns the raw, quoted Windows command line, so
a whitespace split fuses quotes onto the edge tokens ("C:\Program,
node.exe", "refactor, auth") while session.command stores those values
unquoted. The contiguous whole-token run therefore never matched, and a live
non-forked --from-pr resume (whose only identity path is the stored command)
was marked stale, letting kill <id> report success without signalling the
process. Trim a single surrounding quote from each token before comparing;
POSIX ps output is unquoted so this is a no-op there and preserves the #1770
token-boundary guard.

---------

Co-authored-by: 0xghost42 <nikhilbajajj01@gmail.com> — data não informada\n  - `a5b277971d078ffc62fea7fb1be6deba367bfe29` — feat(settings): add settings-based subscription override and agy terminal support (#1731)

* feat(settings): add settings-based subscription override and agy terminal support

* feat(provider): rebrand Gemini wizard setup steps to Google AI / Gemini

* fix(settings): restrict subscription override to trusted sources

Addresses jatmn's CodeRabbit review on #1731.

P1 — untrusted settings sources could spoof subscriber state:
  Reads subscriptionType only from policy/flag/user/local settings,
  excluding project and repository settings which can be checked into
  shared repos. Adds getTrustedSubscriptionType() helper used by both
  isClaudeAISubscriber() and getSubscriptionType().

P2 — subscriptionType: "free" did not short-circuit OAuth-detected
  subscriber state. With a valid Claude AI OAuth token and
  subscriptionType: "free" in settings, isClaudeAISubscriber() still
  returned true. Now "free" is authoritative and returns false.

P3 — test isolation: added afterEach(mock.restore()) to auth.test.ts
  so Bun's module mocks cannot leak into subsequent tests.

Also splits the antigravity askpass test into focused cases for
"agy" and "antigravity" substrings.

* fix(settings): restrict subscriptionType override to user settings and return false early for free

* fix(auth): clean up unused import and return type matching in tests

* fix(provider): align Gemini chooser copy with the wizard's actual auth methods

Addresses jatmn's review on #1731. The /provider chooser advertised "Google AI /
Gemini Subscription" and "Use your Google AI Premium plan, …", but the Gemini
setup wizard only offers three auth methods — API key, access token, and local
ADC — with no subscription/Premium sign-in flow. Drop the "Subscription" label
and "Google AI Premium plan" framing so the chooser matches the wizard (and the
"Google AI / Gemini" wording used elsewhere in the file). No OAuth/subscription
sign-in is planned: using Google AI/Gemini subscriptions via third-party tools
violates Google's Terms of Service.

* fix(pr1731): resolve review follow-ups

* fix(pr1731): close review follow-ups

* fix(pr1731): close antigravity and gemini follow-ups

---------

Co-authored-by: jatmn <the@jat.mn> — data não informada\n  - `aa936cda111d50985b797f1ec0475cc3c9e1820f` — Centralize credential redaction in src/utils/redaction.ts + channel gate tests (#1711)

* feat(utils): add centralized redaction utility

Single source of truth for stripping API keys, tokens, and other
secrets from strings and JSON. Provider env-var coverage is generated
from getKnownProviderSecretEnvKeys() so adding a new provider cannot
silently create an unredacted path.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* refactor(Feedback): import redactSensitiveInfo from utils

Remove the inline 40-line regex implementation in favor of the
centralized redaction utility, eliminating drift between Feedback
and the transcript share path.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* refactor(submitTranscriptShare): import redactSensitiveInfo from utils

Update import path to point at the centralized utility instead of the
Feedback component. Removes the implicit re-export contract that
required Feedback.tsx to keep redactSensitiveInfo exported.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* feat(log,debug): redact secrets in default error and debug output

Wire the centralized redaction utility into logError and logForDebugging
so secrets cannot leak into in-memory error logs or the debug file even
if a caller forgets to pass through redactSensitiveInfo.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* feat(api/logging): redact error message in logAPIError

Apply the centralized redaction utility to the error string passed to
logEvent so analytics events cannot capture unredacted credentials from
upstream API failures.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix: resolve merge conflict from upstream sync

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(channelNotification): allow null in getEffectiveChannelAllowlist signature

ChannelsNotice.tsx passes getSubscriptionType() which returns
SubscriptionType | null, but the signature only accepted string |
undefined. Widen to string | null so the call site typechecks.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* feat(redaction): exclude specific token fields from redaction process

* fix(redaction): lower AIza minimum length to {10,}

Real GCP/Gemini keys are 39 chars total (4 prefix + 35 suffix), but
the {35} suffix bound missed short tokens like 'AIzaSyDUMMY-secret-token'
(21 chars after AIza). Lower to {10,} to match the diagnostics module
and catch any AIza-shaped value. Same precision trade-off the
diagnostics redaction makes.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(redaction,log): address review feedback

- Drop quotes from ANTHROPIC/OPENAI key negative lookarounds so
  JSON-shaped values like "sk-ant-..." redact.
- Add private_key pattern to GENERIC_HEADER_FIELD_PATTERN and
  privatekey to SENSITIVE_FIELD_SUBSTRINGS.
- logError now builds a sanitized Error (redacted message + stack)
  before passing to the sink and queue, not just the in-memory log.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* refactor(redaction): consolidate into single module + add channel gate tests

Address the three P2 review findings on the central-redaction PR:

[1] Consolidate four redaction modules into src/utils/redaction.ts.
    Previously lived in:
      - src/utils/redaction.ts            (logs/bug reports/transcript shares)
      - src/utils/urlRedaction.ts         (URL display)
      - src/utils/statusRedaction.ts      (/status output)
      - src/utils/diagnostics/redaction.ts (doctor reports)
    The four surfaces share the same regex set / credential lists
    but had drifted into separate per-domain files. Merged into
    one module; deleted the three shim files. Updated six direct
    consumers (openaiShim.ts, ProviderManager.tsx, status.tsx,
    requestSizeBreakdown.ts, diagnostics/issueReport.ts,
    scripts/system-check.ts) and three test files to import from
    redaction.js.

[2] Add gateChannelServer() test coverage.
    src/services/mcp/channelNotification.test.ts: 13 cases for the
    six gate paths (capability, runtime, session, marketplace,
    plugin allowlist, server-entry dev) plus end-to-end register.
    Mocks channelAllowlist.js (GrowthBook-backed) so tests stay
    independent of feature-flag state.

[3] Apply jsonRedactor in transcript share.
    src/components/FeedbackSurvey/submitTranscriptShare.ts now does
    redactSensitiveInfo(jsonStringify(data, jsonRedactor)) — the
    key-aware redaction applies during serialization, and the text
    pass stays as defense in depth for free-form fields.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* test(channelNotification): cover findChannelEntry multi-candidate branch

Regression test for the disambiguation path in `findChannelEntry`
(channelNotification.ts:201-230): when two same-name plugin entries
exist in the allowed-channels list with different marketplaces,
`pluginSource` must select the matching entry before the marketplace
and allowlist gates evaluate.

Without this branch being exercised, the gate could lock onto
whichever entry sorts first and either skip the user's real
installation or wrongly authorize a typo-squatted one.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(redaction): align URL fallback regex + add path-prefix boundary check

Two related redaction correctness fixes:

[1] URL fallback regex covers the same parameter set as the primary
    path. The malformed-URL branch in `redactUrlForDisplay` previously
    had a hand-rolled alternation of credential parameter names that
    could drift behind `SENSITIVE_URL_QUERY_PARAM_TOKENS`. New
    `MALFORMED_URL_PARAM_PATTERN` derives from that same list, so
    the two paths can never diverge. Tests cover the full credential
    set (`api_key`, `access_token`, `refresh_token`, `signature`,
    `sig`, `secret`, `password`, `apikey`) plus a non-sensitive
    `model` that must survive.

[2] `redactPathForStatus` now requires a path-separator boundary
    after the home prefix. The previous `startsWith` check matched
    `/home/alice2/project` against `/home/alice` and emitted
    `~2/project`. The fix requires the character at
    `normalizedCandidate.length` to be `/` or `\` so `alice` no longer
    matches `alice2` or `alice.bak`. Test pins the false-positive
    paths and the true-positive (`/home/alice/project` → `~/project`).

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(channel,redaction): restore dev-channel warning + align URL fallback

Two related security fixes:

[1] Restore DevChannelsDialog when --dangerously-load-development-channels
    is passed and the channels feature is enabled. The previous logic
    skipped the dialog when OAuth was absent, which was safe only while
    gateChannelServer() blocked no-OAuth sessions. With the OAuth/org-
    policy gates removed in this PR, an API-key session could pass the
    flag, skip the warning, and still register the dev channel. The
    only remaining skip is the genuinely-disabled feature case
    (`!isChannelsEnabled()`), where the dialog is moot.

[2] Malformed-URL fallback now uses the same substring predicate as
    the primary `URL` parser path. The previous regex matched only
    exact parameter names (`api_key=`, `access_token=`, …), so
    `my_api_key=SECRET` and `x_access_token=TOKEN` slipped through
    unchanged even though `shouldRedactUrlQueryParam` flags them as
    sensitive. New `redactMalformedQuery` walks the query pairs and
    runs the predicate on each key. Three new tests cover prefixed
    keys, non-sensitive keys, and fragment preservation.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(redaction): widen key boundary class + tighten dev-channel comment

Two small follow-ups from the latest CodeRabbit review:

[1] Boundary class on key-prefix patterns widened from `[A-Za-z0-9]`
    to `[A-Za-z0-9_-]` so a raw key embedded in a JSON string value
    (`"sk-ant-..."`, `"AIza..."`, `"ghp_..."`, etc.) is still caught.
    Quotes act as delimiters, not blockers — the previous boundary
    class was correct for unquoted text but let quoted keys slip
    through.

[2] Tighten the dev-channel dialog comment in interactiveHelpers.tsx
    so future readers don't misread the security boundary. Skip
    condition is `isChannelsEnabled()` (the channels feature flag
    gate), not KAIROS / KAIROS_CHANNELS as the previous wording
    implied. Comment now matches the code.

Skipped with reason:
- getEffectiveChannelAllowlist divergence from gateChannelServer
  allowlist — by design; the effective-list override is a UI hint
  consumed only by ChannelsNotice for the org-override indicator.
  Trust boundary is enforced by gateChannelServer() reading the
  hardcoded ledger.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(redaction,channel): address P1/P2 review findings

P1 - malformed URL fallback secrets:
- Decode percent-encoded query param keys via decodeURIComponent() before
  applying shouldRedactUrlQueryParam (e.g. %74oken -> token)
- Stop userinfo regex at ? and # delimiters to avoid consuming query params
  when matching @ signs in email addresses or fragment delimiters

P2 - channel notice/gate allowlist sync:
- Remove org override path from getEffectiveChannelAllowlist() so
  ChannelsNotice startup guidance uses the same ledger source as
  gateChannelServer's runtime enforcement
- Simplify ChannelsNotice to drop unused sub/policy params and the
  source === 'org' conditional

* fix(channel): apply marketplace matching to permission relays, remove stale OAuth/org-policy blockers, add dev-channel dialog coverage

P1: Thread runtime pluginSource through filterPermissionRelayClients
so findChannelEntry disambiguates same-name plugin entries from
different marketplaces before sending permission request previews.

P2: Remove stale noAuth and policyBlocked branches from ChannelsNotice
that would render '--channels ignored' before reaching the listening
message, confusing non-OAuth users.

P2: Add test coverage that mocks isChannelsEnabled() both true and
false, verifies DevChannelsDialog appears with onAccept marking entries
dev:true in the enabled case, and verifies the disabled branch registers
entries directly without dialog.

* test(dev-channel): clarify count assertion comment + add afterEach with mock.restore()

* fix(channel): mirror marketplace gate in permission relay + restore mock

Two follow-ups from the latest review:

[1] Permission relay predicate no longer relies on findChannelEntry
    alone. After resolving the entry, the predicate now requires a
    runtime pluginSource whose marketplace matches the session
    entry's marketplace for plugin-kind entries — mirroring the
    gateChannelServer check at channelNotification.ts:303-312. A
    `plugin:slack@evilcorp` client whose session allows
    `plugin:slack@anthropic` is now rejected instead of piggy-backing
    on the approved entry to receive permission-request previews.
    Server-kind entries still match on bare name.

[2] bugfixes.test.ts now re-registers the real channelAllowlist
    module in afterEach via a cache-busted reference, so the
    neighbor channelNotification.test.ts continues to import
    getChannelAllowlist after this suite runs. mock.restore() does
    not clear module-level mock.module() overrides in bun (the
    registry is process-global). Pattern matches compact.test.ts:27-36.

Also expanded the dev-map count comment in bugfixes.test.ts to
document the security invariant (a dev entry must never be confused
with a production entry in the allowlist check) per CodeRabbit's
request.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* refactor(redaction): consolidate into single module + add channel gate tests

Address the three P2 review findings on the central-redaction PR:

[1] Consolidate four redaction modules into src/utils/redaction.ts.
    Previously lived in:
      - src/utils/redaction.ts            (logs/bug reports/transcript shares)
      - src/utils/urlRedaction.ts         (URL display)
      - src/utils/statusRedaction.ts      (/status output)
      - src/utils/diagnostics/redaction.ts (doctor reports)
    The four surfaces share the same regex set / credential lists
    but had drifted into separate per-domain files. Merged into
    one module; deleted the three shim files. Updated six direct
    consumers (openaiShim.ts, ProviderManager.tsx, status.tsx,
    requestSizeBreakdown.ts, diagnostics/issueReport.ts,
    scripts/system-check.ts) and three test files to import from
    redaction.js.

[2] Add gateChannelServer() test coverage.
    src/services/mcp/channelNotification.test.ts: 13 cases for the
    six gate paths (capability, runtime, session, marketplace,
    plugin allowlist, server-entry dev) plus end-to-end register.
    Mocks channelAllowlist.js (GrowthBook-backed) so tests stay
    independent of feature-flag state.

[3] Apply jsonRedactor in transcript share.
    src/components/FeedbackSurvey/submitTranscriptShare.ts now does
    redactSensitiveInfo(jsonStringify(data, jsonRedactor)) — the
    key-aware redaction applies during serialization, and the text
    pass stays as defense in depth for free-form fields.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix(test): align malformed URL fragment expectation with preservation behavior

* fix: address review findings P1 and P2

[P1] Enforce dev flag for server-kind entries in permission relay
predicate, matching gateChannelServer() behavior. Add coverage for
both dev and non-dev server relay paths.

[P2] Drop fragments in malformed URL fallback (redactMalformedQuery)
to match the valid-URL path, preventing credential leaks via
fragment-carried tokens. Update existing tests and add regression
for fragment-only malformed URLs.

* test(relay): add plugin-kind marketplace regression tests

* fix: address review findings P1 and P2

[P1] Add PEM private key redaction pattern to redactSensitiveInfo
so multi-line PEM values are fully consumed instead of leaking
after the first whitespace. Add [ to generic header pattern's
value exclusion set to prevent re-consuming [REDACTED] tokens.

[P2] Use truthy check (Boolean()) for claude/channel capability in
filterPermissionRelayClients to match gateChannelServer's behavior,
rejecting explicit false capabilities.

* fix(debug): redact before JSON-stringify multiline messages

Reorder logForDebugging so redactSensitiveInfo runs before jsonStringify,
ensuring PEM/private-key patterns match the raw (unescaped) message text
rather than the JSON-encoded form where colons and quotes are escaped.

* test(debug): add end-to-end regression for multiline PEM redaction in logForDebugging

Uses mock.module on process.js to capture stderr output and exercises the
full logForDebugging path with multiline PEM private_key input, verifying
the redact-before-JSON-stringify ordering produces redacted output.

* fix(test): preserve original process.env.DEBUG and process.argv in logForDebugging test hooks

* fix: address PR review findings P1-P3/P5-P7

- P1: clear isDebugMode/isDebugToStdErr memoize caches in test beforeEach
      + cache-busting query param for fresh debug.ts imports
- P2: restore mock.module afterAll instead of leaking mock
      + mutate err in-place in logError to preserve name/cause
- P3: post-processing regex absorbs trailing bracket content after [REDACTED]
- P5: (was P3) expand jsonRedactor EXCLUDED_KEYS for maxTokens etc.
- P7: capture HOME/USERPROFILE per-test instead of at module scope

* fix: address CodeRabbit review findings

- interactiveHelpers.tsx: update dev-channel comment — OAuth/org-policy
  gates removed from gateChannelServer(), org policy is not enforced
- channelNotification.test.ts: add afterAll mock.restore() to clean up
  process-global channelAllowlist.js mock
- channelNotification.ts: fix comments — isChannelsEnabled() still reads
  tengu_harbor, not always true
- log.ts: sanitize err.message and err.stack separately so message
  doesn't get replaced with full stack trace
- redaction.ts: add 'i' flag to redactHomePath regex for Windows
  case-insensitive path matching

* fix: address second review round

- interactiveHandler.ts: [P2] redact input_preview via redactSensitiveInfo
  before sending to channel servers
- log.ts: [P3] copy error via Object.assign(Object.create(err), err)
  before sanitizing instead of mutating in-place

* fix: address CodeRabbit second round

- channelPermissions.ts: redact before truncate in truncateForPreview
  so partial credentials don't leak at the 200-char boundary
- interactiveHandler.ts: remove outer redactSensitiveInfo — now
  handled inside truncateForPreview
- log.ts: derive errorInfo.error from already-sanitized sanitizedErr;
  fix Object.assign comment to accurately describe what is copies

* fix: improve permission relay client filtering and enhance redaction functions

* fix: address third review round (P1, P2, P3)

- P1: update test expectations for [REDACTED_*] output format
- P2: add total_tokens, prompt_tokens, completion_tokens to jsonRedactor EXCLUDED_KEYS
- P3: remove ) and } from GENERIC_HEADER_FIELD_PATTERN value capture to prevent content leak after embedded parens
- Fix buildKnownEnvVarPattern capture group to preserve env-var separator ([REDACTED])
- Add & to GENERIC_CREDENTIAL_ENV_PATTERN value exclusion to prevent URL query over-consumption

* fix: address latest reviewer P2/P3 findings (errorLogSink redaction, X_API_KEY/AUTHORIZATION patterns, regression tests)

* fix: address reviewer P1/P2 — bracketed values and multi-word header values

- P1: Remove  and  from value captures in X_API_KEY_PATTERN,
  AUTHORIZATION_PATTERN, GENERIC_HEADER_FIELD_PATTERN,
  GENERIC_CREDENTIAL_ENV_PATTERN so bracketed secrets like
  are fully redacted instead of passing through unchanged.

- P2: Widen header-style value captures to include spaces by removing
   from exclusions, using  as delimiter (stops at newlines
  and URL query separators). Fixes multi-word leaks:
  , ,
  , .

- GENERIC_CREDENTIAL_ENV_PATTERN: add  to negative lookbehind
   to prevent matching  inside
  when the latter is already redacted.

- GENERIC_HEADER_FIELD_PATTERN replacer: skip values starting with
   to preserve specific labels from earlier passes.

- Add 7 regression tests covering both finding categories.

* fix: address reviewer findings P1-P4

P1: Custom enumerable error properties now redacted in log.ts
  logError iterates all own enumerable properties on the original error
  and applies redactSensitiveInfo to string values and jsonRedactor to
  object values, preventing credential-bearing custom fields from leaking
  through the sanitized error. Regression tests added in log.test.ts.

P2: Soften single-source-of-truth claim; migrate easy call sites
  Header comment in redaction.ts updated to acknowledge that specialized
  scanners (secretScanner.ts, xaa.ts) are intentional exceptions.
  src/services/mcp/client.ts and src/services/mcp/auth.ts now use
  jsonRedactor for header redaction instead of ad-hoc key checks.

P3: Fix mock.restore cleanup in channelNotification.test.ts
  Cache-bust the real channelAllowlist module at describe-entry and
  re-register it in afterAll, following the pattern from bugfixes.test.ts.
  mock.restore alone does not clear mock.module overrides in Bun.

P4: Remove unused ChannelGateResult kinds
  Removed 'auth' and 'policy' from the skip kind union and removed
  corresponding dead branches in useManageMCPConnections.ts.

* fix: extract sanitizeError() to fix CI test fragility

The logError tests were failing in CI due to parallel test execution
racing on the module-level errorLogSink singleton. Extract the inline
sanitization logic into an exported sanitizeError() helper and test
that directly — it's pure, has no env-var or sink dependencies, and
doesn't interact with shared mutable state.

* fix: use Object.getPrototypeOf(err) instead of err as prototype in sanitizeError

Object.create(err) sets the original error instance as the prototype of the
sanitized copy, leaking non-enumerable own properties through the prototype
chain. Use Object.getPrototypeOf(err) instead so the prototype is the error
constructor's prototype (e.g. TypeError.prototype), preserving instanceof
checks without exposing the original error's non-enumerable fields.

Add a regression test verifying non-enumerable properties do not leak and
update the prototype-chain test to assert Object.getPrototypeOf result.

* fix: apply key-aware redaction and fail closed on non-serializable error props

- String properties: use jsonRedactor(key, value) instead of
  redactSensitiveInfo(value) so keys like apiKey with innocuous values
  (e.g. 'my-key') are still caught via SENSITIVE_FIELD_SUBSTRINGS.
- Object path: catch now replaces non-serializable/circular references
  with '[REDACTED]' instead of leaving the original object reference.
- Add 2 regression tests for key-aware redaction and fail-closed behavior.

* Update src/utils/log.ts

Co-authored-by: coderabbitai[bot] <136622811+coderabbitai[bot]@users.noreply.github.com>

* fix: redact bare auth header keys in JSON/header objects

- Add 'auth' to SENSITIVE_FIELD_SUBSTRINGS in src/utils/redaction.ts:109 to match URL/diagnostic redactors treatment of auth
- Add regression test for bare auth header keys in src/utils/diagnostics/redaction.test.ts:88

Co-authored-by: openhands <openhands@all-hands.dev>

* fix: narrow auth matching, redact nested transcript JSONL, fix channel skip message

* fix: address CodeRabbit nits — comment, hint, JSONL fallback redaction

* fix: key-aware malformed JSONL fallback and auth/x-auth in free-form text

* fix: strengthen redactJsonLines trailing rest redaction and auth test assertions

* fix: preserve non-JSON prefix in redactJsonLines fallback and redact it

* fix: tighten redactJsonLines prefix test to exact output assertion

* fix: redact MCP log sink payloads and errorStr before writing to disk

* fix: address P1 findings — URL #-in-password, ;-delimited query params, split channel trust-boundary

- Allow  in URL userinfo password on malformed-URL fallback path
  (new URL() fails when password contains fragment delimiter).
- Redact -delimited sensitive query params by splitting on both & and ;
  in redactMalformedQuery, plus redactSemicolonQueryParams post-processor
  for valid-URL output.
- Restore channelNotification.ts to upstream/main to fully split
  OAuth/org-policy trust-boundary changes from credential redaction PR.

* fix: update callers to match upstream/main function signatures

channelNotification.ts was restored to upstream/main to split
trust-boundary changes from the redaction PR. This commit updates
the three caller sites that previously passed extra arguments:

- ChannelsNotice.tsx: pass getSubscriptionType() + undefined to
  getEffectiveChannelAllowlist (needs 2 args upstream)
- interactiveHandler.ts, channelNotification.test.ts: drop 3rd
  pluginSource arg from findChannelEntry (takes 2 args upstream)

* fix: address reviewer findings — OAuth mock, notice states, marketplace disambiguation

P1: Mock getClaudeAIOAuthTokens and getSubscriptionType in channel
notification tests so they pass on CI where no real OAuth exists.

P2: Restore blocked-auth/org-policy notice states in ChannelsNotice.tsx
so the UI shows the correct blocker when gateChannelServer rejects
unauthenticated users or orgs without channelsEnabled.

P2: Add pluginSource disambiguation to findChannelEntry so same-name
plugin entries from different marketplaces are matched by runtime
source rather than first-match order. Add regression test with
non-matching marketplace first to cover the bug.

* fix: address reviewer findings — relay gate parity and allowlist regression test

- Replace filterPermissionRelayClients in interactiveHandler with inline
  gateChannelServer call so the relay predicate checks ALL gates including
  disabled-channel, auth, org policy, and approved-plugin allowlist, not
  just session entry + marketplace.
- Clean up unused imports (getAllowedChannels, parsePluginIdentifier,
  findChannelEntry, filterPermissionRelayClients).
- Add regression test: gateChannelServer rejects marketplace-matched
  plugin not on approved allowlist (full-gate path).

* fix: redact mixed semicolon secrets in valid-URL path and route OpenAI shim through centralized redactor

P1: Pre-redact semicolon-delimited sensitive query params from the raw
query string in redactUrlForDisplay BEFORE URLSearchParams encodes
; as %3B. Previously model=ok;token=SECRET leaked because
parsed.toString() reserialized to model=ok%3Btoken%3DSECRET, making
it invisible to the post-process pass.

P1: Route openaiShim's redactUrlForDiagnostics through the centralized
redactUrlForDisplay so the semicolon fix, malformed-URL fallback, and
all future redaction improvements apply to OpenAI-compatible
diagnostic logs too. Keep redactSecretValueForDisplay as an additional
safety net after the centralized pass.

Add 3 regression tests for mixed-separator queries.

* Update src/utils/redaction.ts

Co-authored-by: coderabbitai[bot] <136622811+coderabbitai[bot]@users.noreply.github.com>

* fix: add fragment-query credential regression test and correct dev-channel gate comments

P2: Add regression test for redactUrlForDisplay with query-like credential
in fragment (e.g. #debug?token=SECRET). Fix raw-query pre-processing to
only extract query before the first #, preventing fragment content from
being treated as query parameters.

P3: Update comments in interactiveHelpers.tsx to match the actual gate
order — OAuth and org-policy gates still exist in gateChannelServer()
after restoring to upstream/main; the --dangerously-load-development-
channels flag only bypasses the allowlist gate.

* fix: add port+fragment+@ fallback test and restructure dev-channels dialog tests

* fix: registerDevChannels seam, bare-host #-in-password heuristic, and coverage restructure

* fix: add OAuth and org-policy gate test coverage

- Refactor auth module mock to use mutable variables per test
- Auth gate test: empty OAuth tokens -> kind:auth
- Policy gate test: team subscription without channelsEnabled -> kind:policy

* fix: prefer exact server channel entries before plugin disambiguation

- Return exact server-kind candidate first when candidates include both server and plugin entries with same name
- Added regression test covering mixed server/plugin --channels entries to ensure exact server opt-in is not overridden by plugin candidate
- This prevents a plugin marketplace mismatch from incorrectly rejecting a server the user explicitly selected via server:plugin:slack

* fix: only trust exact [REDACTED] placeholder in generic header field pattern

- Changed GENERIC_HEADER_FIELD_PATTERN to only bypass exact '[REDACTED]' canonical placeholder
- Prevents non-canonical placeholders like '[REDACTED_API_KEY]' or '[REDACTED_actual_secret]' from leaking through
- Updated tests to expect canonical '[REDACTED]' output for generic pattern

* fix: handle bare hosts in malformed URL userinfo fallback

- Added regex to recognize bare hostnames (with optional port) in the fragment heuristic
- Added tests for //alice:sec#ret@host and //alice:sec#ret@host:443

* fix: add relay dispatch path test for non-allowlisted plugin

- Added test using full gateChannelServer predicate in filterPermissionRelayClients
- Mirrors the exact relay dispatch path used in interactiveHandler
- Ensures marketplace-matched plugin not on allowlist is excluded from permission preview

* fix: enhance URL redaction logic to handle valid hosts before fragment

* fix: refine URL redaction logic to ensure valid host checks before fragment

* fix: enhance redaction logic to handle embedded URLs in free-form text

* fix: update redaction logic to remove user info from OpenAI base URL in diagnostic report

* fix: ensure findChannelEntry returns undefined when no exact matches are found

* fix: improve URL redaction logic to remove user info and ensure proper formatting

* fix: enhance redactDiagnosticUrl to preserve query-param values and trailing slashes

* fix: refine redaction logic to preserve meaningful path segments and handle trailing slashes correctly

* fix: enhance redactDiagnosticUrl to preserve literal path segments and handle trailing slashes correctly

* fix: preserve semicolon-delimited query params during redaction

* fix: update redaction logic to support semicolon-delimited query parameters

* fix: enhance redactUrlForDisplay to handle bare hosts and improve fragment redaction

* fix: enhance redactUrlForDisplay to correctly handle username-only userinfo with fragments

* fix: address privacy findings — URL redaction in jsonRedactor, base URL redaction, diagnostic object collapsing, structural channel previews, pluginSource telemetry

* fix: preserve falsey env-presence values in diagnostic redaction

- false, "", and 0 under isEnvPresenceKey keys are now preserved as-is
  instead of misrepresented as "[set]"
- Added regression test for absent/falsey env-presence inputs

* fix: address CodeRabbit findings — sync describe, heartbeat emitter, responsesBody filtering, dev entry precedence

* chore: remove stray Windows path artifact

* fix: update redaction import path in taskReport module

* fix: address CodeRabbit P1-P3 findings and rebase regressions

- F1: rebase onto upstream/main, fix taskReport.ts import path
- F2: Ollama native chat code recovered via rebase (6 functions)
- F3: &-truncation in credential regexes fixed via post-processing pass
- F4: 'tokens' added to jsonRedactor EXCLUDED_KEYS
- F5: redactHomePath case-sensitivity aligned with redactPathForStatus
- F6: credential metadata object preserved in issue report (sensitive-key check
  moved inside type branches)
- F7: heartbeat tests updated for pre-drain write behavior
- F8: reportTask test expects [REDACTED] (matches centralized output)
- rm: stray C:\repo\ Windows path artifact

* fix: address reviewer findings — generic regex &-handling and diagnostic secret-key masking

- Remove & from excluded char classes in 4 generic patterns so they consume
  full secret values (URL-query &-splitting belongs in redactUrlForDisplay).
- Remove now-obsolete &-tail post-processor pass.
- Remove credential from DIAGNOSTIC_SECRET_KEY_PATTERN so issue report
  credential metadata objects are traversed, not collapsed.
- Restore broad isDiagnosticSecretKey check before type dispatch in
  redactDiagnosticObjectInternal so objects/arrays under secret-marked keys
  (auth, password, token, etc.) are masked.
- Update issue report test baseUrl expectation (no trailing &mode=test after
  generic redactor consumes past &).

* fix: address reviewer findings — URL delimiter safety, jsonRedactor #-drop, embedded URL query redaction

- Restore &#; delimiters in generic pattern value classes (F1) so safe
  query tails (&mode=test) survive. Re-add &-tail post-processor for
  non-URL abc&def case.
- Gate redactUrlForDisplay in jsonRedactor to https?:// strings only (F2)
  to prevent #-drop on ordinary text like 'fails after #setup'.
- Add URL query redaction step to redactSensitiveInfo (F3) that extracts
  https?:// URLs from free-form text and routes them through
  redactUrlForDisplay, catching signature/sig params that generic patterns
  miss. Skip already-redacted URLs to avoid double-redaction.

* fix: add Cookie/Set-Cookie semicolon-safe redaction pass, tighten &-tail regex

* fix: COOKIE_PATTERN consume comma-joined multi-cookie values

* fix: address P2 findings — URL redact skip, pre-drain write promise, permission truthy check

* fix: update log.test.ts expectation, add protocol-relative URL support

* fix: enhance redaction for provider env-vars in URLs, preserve safe query params

* fix: enhance redaction for uppercase provider keys and cookie query params

* fix: enhance redaction for bare Bearer and JWT tokens in sensitive info

* fix: update report task test expectations for new redaction format

* fix: limit token exemption to numeric values, protect semicolon cookie query tails

* test: add tests for truncateForPreview to ensure sensitive data redaction

---------

Co-authored-by: Gravirei <gravirei@users.noreply.github.com>
Co-authored-by: Claude Opus 4.6 <noreply@anthropic.com>
Co-authored-by: coderabbitai[bot] <136622811+coderabbitai[bot]@users.noreply.github.com>
Co-authored-by: openhands <openhands@all-hands.dev> — data não informada\n  - `c3db07f1f255ed42afe3fc6c74a338ff235f28fd` — feat(codex-oauth): manual callback URL paste for SSH / remote sessions (#1288) (#1414)

* feat(codex-oauth): manual callback paste for SSH / remote sessions

Codex OAuth required the browser to reach the openclaude host's
localhost:1455 callback. On SSH / containerized installs that callback
resolves to the user's workstation instead of the openclaude host, so
the redirect lands on a dead URL and the CLI hangs.

Add a manual-paste fallback (mirrors the xAI OAuth recovery path):
after authorizing in the browser, the user copies the full redirected
URL from the address bar and pastes it into the CLI. CodexOAuthService
validates the state parameter against the in-flight flow, races the
manual code against the loopback listener, and reuses the same
authorization-code → token exchange.

SSH_CONNECTION / SSH_CLIENT triggers a warning banner explaining why
the loopback redirect failed; non-SSH sessions get a dim hint covering
containerized / remote setups.

Closes #1288

* test(codex-oauth): type manual-paste fetch mock via asMockFetch

The raw `mock(...) as typeof fetch` cast no longer typechecks against the
base branch's stricter `fetch` type (now requires `preconnect`). Route the
manual-callback-paste test's mock through the shared `asMockFetch` helper,
matching the other fetch mocks in this file.

* fix(codex-oauth): mask the pasted manual callback URL input

The manual-recovery field echoed the redirected callback URL verbatim, which
carries the OAuth code and state query params — enough to complete the
in-flight exchange. Mask it with mask="*", matching the adjacent xAI
manual-code field, so it stays out of terminal scrollback, recordings, and
shared sessions.

* test(codex-oauth): bound state wait and cover hook manual-callback contract

- Bound the while (!capturedState) wait in the manual-callback test with a 5s
  deadline so a regression fails with a clear assertion instead of hanging the
  suite.
- Add a useCodexOAuthFlow test asserting the waiting status exposes
  submitManualCallback and delegates both success and failure results from the
  service back to the caller.

* test(codex-oauth): stabilize onAuthenticated in the manual-callback test

The new hook test passed a fresh inline `onAuthenticated: async () => {}` on
every render, so the hook effect re-ran each render, restarting the flow and
looping setStatus → render ("Maximum update depth exceeded" when run alongside
ProviderManager.test.tsx). Hoist the callback to a stable reference, matching
the other tests in the file.

* test(codex-oauth): cover the ProviderManager manual-callback UI

Add focused coverage for the waiting-state paste surface: the masked callback
input renders, a good callback delegates to status.submitManualCallback with no
inline error, the SSH banner appears when SSH_CONNECTION is set, and a rejected
callback surfaces the hook's inline error. — data não informada\n  - `5afd4f4d1061961bc667e7f4f0fabf76ca235e4d` — fix(tokens): include attachments in incremental cache key (#800)

Co-authored-by: jatmn <the@jat.mn> — data não informada\n  - `230888181a42c71fc452539cf8802189e28bb297` — fix(websearch): match allowed/blocked domains case-insensitively (#1872)

hostMatchesDomain compared the request host against the caller's
allowed_domains / blocked_domains entries with a raw ===/endsWith. The host is
always lowercased (WHATWG new URL().hostname via safeHostname), but the domain
entries come straight from tool input and are never normalized. A capitalized
entry therefore never matched:

- blocked_domains: ['Reddit.com'] silently failed to block reddit.com results.
- allowed_domains: ['GitHub.com'] dropped every legitimate github.com hit.

Hostnames are case-insensitive, so lowercase both operands before comparing.
Lookalike hosts (notexample.com) are still rejected. — data não informada\n  - `8d90849fe6567b82b8e0915b5f5b9c5de6e690b5` — fix(diff): don't overcount new-file additions by the trailing newline (#1873)

countLinesChanged's new-file branch counted added lines as
newFileContent.split(/\r? — data não informada\n  - `8599560b8265f793df2d06041993f25c21dbf190` — fix(websearch): add built-in provider request timeouts (#1874)

* Add timeouts for web search providers

* Fix WebSearch timeout body-stall test

* Address WebSearch timeout review feedback — data não informada\n  - `db01038d5ce397e1cd4228f55075ef7b21cc2553` — feat(model-picker): surface inactive provider profiles in /model (#1119 piece 2) (#1164)

* feat(model-picker): surface inactive provider profiles in /model

When a user configures multiple providerProfiles (Kimi + Z.AI + OpenRouter
+ SambaNova in the #1119 repro, but the pattern fits any multi-provider
setup), switching the main session between them currently requires
round-tripping through /provider — /model only shows the active
profile's models.

Make /model the single switcher:

- ModelOption gains an optional `switchToProfileId`. Existing options
  leave it unset and behave exactly as today.
- `getInactiveProviderProfileOptions` enumerates every configured
  profile that isn't the active one and emits a picker entry per model,
  labelled `<model> · <profile.name>` so the user can see the choice
  changes providers, not just models.
- Each option's `value` is encoded with `__switch_profile__:<id>:<model>`
  so the picker's plain-string `value` channel stays the source of truth
  and same-named models under different base URLs (`gpt-4o` on multiple
  OpenAI-compatible endpoints) stay disambiguated.
- /model's handleSelect detects the prefix, calls
  `setActiveProviderProfile` (same path /provider uses — applies env,
  persists active profile, refreshes startup file), then sets
  `mainLoopModel` to the bare model string.

Only surfaces inactive options when `CLAUDE_CODE_PROVIDER_PROFILE_ENV_APPLIED`
is set, so users who haven't opted into the multi-profile workflow at all
don't see the affordance.

Tests cover round-trip encoding (including OpenRouter-style colon-bearing
model strings), the active-filter, the multi-model explosion, and that
`getModelOptions()` 3P path includes the inactive options only when the
profile env is applied. Combined invocation with the rest of
`src/utils/model/` + `src/commands/model/` + `src/utils/providerProfiles.test.ts`
runs clean to guard against mock-leak (per the 2026-04-30 lesson —
spreads `import * as actual` for every `mock.module` factory).

Refs #1119

* fix(model-picker): run fast-mode cleanup on cross-profile switch

The new switch-profile branch returned before reaching the fast-mode
reconciliation, so a user with fastMode latched on Anthropic Opus could
switch to an OpenAI profile and silently keep fastMode on even though
the new model can't support it. Extract the cleanup into a pure helper
`reconcileFastModeForSwitch` and call it from both branches.

Refs #1119.

* fix(model-picker): decode cross-profile values before effort/display lookup

Inactive-profile entries encode the picker value as
`__switch_profile__:<profileId>:<model>`, but `resolveOptionModel`
forwarded the raw string straight to `parseUserSpecifiedModel`. For a
reasoning-capable cross-profile entry such as `gpt-5.4`,
`modelSupportsEffort()` then saw the prefixed string and reported
"Effort not supported", and `handleSelect` dropped the toggled effort
even when the underlying model accepts it.

Run `parseSwitchProfileValue` first; when it matches, hand the bare
target model to `parseUserSpecifiedModel` so effort capability,
default-effort lookup, and display-name resolution all key off the real
model id.

* fix(model-picker): include inactive profiles on local OpenAI-compatible scope

The inactive-profile compute lived after the
`getAdditionalModelOptionsCacheScope()?.startsWith('openai:')` early
return, so users with a local OpenAI-compatible profile active (Ollama,
lm-studio, any localhost endpoint) never saw the cross-profile switcher
in `/model`. They still had to round-trip through `/provider` to change
profile.

Hoist `profileEnvApplied`, the active-profile lookup, and
`getInactiveProviderProfileOptions(activeProfileId)` above the early
return, and append `inactiveProfileOptions` to the local-OpenAI branch
return value. Other branches (Claude.AI, MiMo, MiniMax, ant) were
already either irrelevant or have their own gating.

Test: new regression in modelOptions.crossProfile.test.ts pins
`getAdditionalModelOptionsCacheScope` to an `openai:` value and confirms
the inactive profile still surfaces with a parseable
`__switch_profile__` value.

* fix(model-picker): apply the allowlist to the decoded cross-profile model

filterModelOptionsByAllowlist evaluated cross-profile options by their encoded
__switch_profile__:<id>:<model> value, so an availableModels allowlist that
permits the bare target (e.g. glm-5.1) dropped every inactive-profile entry.
Check the allowlist against parseSwitchProfileValue(value)?.model ?? value, and
cover both the allowed and denied cases.

* fix(model-picker): only surface cross-profile switch options on the /model path

The inactive-profile entries come from the shared getModelOptions() list, but
only the /model command's onSelect decodes __switch_profile__ values and
activates the target profile. The prompt hotkey and Settings pickers wrote the
encoded value straight to mainLoopModel, sending an invalid model string.

Gate these options behind a new allowProfileSwitch prop that only the /model
command sets; inline pickers no longer surface an option they cannot honor.
Also apply the org allowlist to the decoded target model in the /model select
handler.

* test(model-picker): drop flaky cross-profile allowlist case

The decoded-allowlist assertion drove the org allowlist through the shared
session settings cache, which is racy across bun's single-process run and could
leak availableModels into sibling suites (the providerConfig cache-scope tests
went red in CI). The decode itself is a one-line guard already exercised by the
parseSwitchProfileValue round-trip coverage, so remove the unreliable case
rather than ship CI flake.

Also snapshot the real provider/auth modules before mocking so each harness
call rebuilds its mock from a clean base instead of a previous test's overrides
(bun live-repoints the imported namespace to the active mock).

* test(model-picker): stop cross-profile mocks leaking into provider suites

The cross-profile tests mock.module'd ../providerProfiles, ./providers,
../auth and ../../services/api/providerConfig per test. bun's mock.module is
process-wide and mock.restore() does not undo it, so these persisted into later
files — most damagingly the providerConfig mock, which replaced the module with
a single-function stub and stripped resolveProviderRequest /
getAdditionalModelOptionsCacheScope from providerConfig.local's suite (now
adjacent after the rebase onto #1706).

Install each mock once at module load, keep the full export surface, and gate
the overrides on module-level flags cleared in beforeEach/afterEach so the
persisted mocks are transparent passthroughs for every other suite. Same
pattern as the cross-spawn / install-surfaces leak fixes.

* fix(model): reconcile fast mode before activating the switched profile

In the cross-profile /model switch path, reconcileFastModeForSwitch ran after
setActiveProviderProfile. The reconciler gates on isFastModeEnabled(), which
reads the *active* provider — so once the target profile is activated it
reflects the new (fast-mode-less) provider and short-circuits to 'unchanged',
leaving fastMode latched on for a model that can't use it.

Compute the reconciliation before activating the profile, so it evaluates
against the source provider and correctly returns 'off' for an unsupported
target. Add a command-level regression test that drives handleSelect with a
__switch_profile__ value while setActiveProviderProfile flips the fast-mode
state, and asserts fastMode is set to false (it fails if the call order
regresses).

* fix(model): re-check fast mode after activating a switched profile

The pre-activation reconcile gates on the source provider, so its 'on' result
is stale when the target provider cannot run fast mode even though the target
model name passes the source-side support check (e.g. a third-party shim
exposing a claude-opus-* model). Re-evaluate isFastModeEnabled / supported /
available after setActiveProviderProfile and force fastMode off when it is no
longer genuinely supported. Add a command-level regression test for that path
and wrap the cross-profile test cleanup in try/finally so a failing assertion
still unmounts the Ink instance (jatmn review, #1119).

* test(model-picker): cover cross-profile allowlist with isolated settings

Re-add the regression dropped in 06a0c80: filterModelOptionsByAllowlist must
evaluate the allowlist against the decoded target model, not the encoded
__switch_profile__ wrapper. Uses this suite's per-test settings cache (reset in
afterEach) instead of the shared cache that made the earlier version flaky
(jatmn review, #1119).

* test(model-picker): make the cross-profile allowlist test leak-proof

The new allowlist test drove availableModels through setSessionSettingsCache,
but sibling suites (ModelPicker, ProviderManager, ...) mock.module both
settings.js (getSettings_DEPRECATED) and modelAllowlist.js (isModelAllowed)
process-wide, so in the full sequential run the leaked stubs defeated the cache
and the denied option was not filtered (smoke-and-tests red on the full suite,
green in isolation).

Drive the allowlist deterministically from this suite instead: install-once,
gated, passthrough mocks of getSettings_DEPRECATED (the filter gate) and
isModelAllowed (the per-option check), both keyed off a single
activeSettingsOverride and cleared in afterEach. Same gated-passthrough pattern
as the suite's existing providerConfig/providers/auth/profiles mocks and the
agent.test.ts allowlist approach.

* fix(model): keep cross-profile switch options out of the SDK models list

getModelOptions() now returns inactive-profile entries encoded as
__switch_profile__:<id>:<model>. print.ts mapped those straight into the
ModelInfo list returned to SDK/web callers, exposing UI-only values that
are not selectable model ids. Filter them with parseSwitchProfileValue
before building modelInfos. Add ModelPicker coverage for the
allowProfileSwitch filter (hidden inline, shown when allowed) and
document cross-profile /model switching in the provider-profile docs.

* test(model-picker): prove cross-profile switch options never reach SDK models

Extract selectSdkModelOptions as the single gate the SDK modelInfos
builder runs every getModelOptions() entry through, and cover it directly:
an encoded __switch_profile__:<id>:<model> option is dropped while real
model ids pass through. Fails if an inactive-profile affordance ever leaks
into the initialize.models response again (#1119).

* docs(model-picker): clarify the env gate for inactive-profile entries

The inactive-profile models only appear when the provider-profile env
workflow is active (CLAUDE_CODE_PROVIDER_PROFILE_ENV_APPLIED=1), not for
every multi-profile setup. Spell that out and restore the local-only
`--provider ollama` guidance that was folded into the paragraph.

* fix(model-picker): gate SDK option filter on switchToProfileId marker

selectSdkModelOptions filtered on the encoded __switch_profile__ value
prefix, which also reserved that prefix for every custom model id. A real
configured model whose id starts with __switch_profile__: would vanish
from the SDK models response and non-switching pickers. Key the gate on
the explicit switchToProfileId marker, which only synthesized switch
options carry, and add the collision regression.

Refs #1119

* fix(model-picker): reuse switch confirmation for cross-profile selections

The cross-profile branch built its own "Switched to" message and returned
before the regular path appended the selected effort and the
"Billed as extra usage" notice, hiding cost-impacting feedback when a
reasoning/extra-usage target was chosen through an inactive profile.
Append effort and the extra-usage check to the switch confirmation.

Refs #1119

* fix(model-picker): surface inactive profiles on the active Ollama path

The isOllamaProvider() early return ran before the inactive-profile
options were computed, so an active local Ollama profile saw only its own
models and lost the cross-profile switcher, forcing the /provider
round-trip this feature removes. Hoist the inactive-profile compute above
the Ollama branch and append it to the Ollama returns.

Refs #1119

* fix(model): surface inactive profiles on all provider branches; decode only real switch options

Two follow-ups to the #1119 unified /model switcher:

- inactiveProfileOptions was computed before the early-return branches but only
  appended on Ollama / local-scope / PAYG paths. The GitHub Copilot, NVIDIA NIM,
  MiniMax, Xiaomi MiMo, ant, and Claude-subscriber branches returned first, so a
  user with a saved profile active on any of those routes lost the cross-profile
  entries and had to round-trip through /provider. Append the (env-gated, so
  empty unless a profile is applied) inactive options on those branches too.

- filterModelOptionsByAllowlist decoded any value starting with
  `__switch_profile__:` via parseSwitchProfileValue, even a normal custom model
  id that merely shares that prefix, evaluating the allowlist against the wrong
  inner model. Gate the decode on the `switchToProfileId` marker (the type's
  documented contract) so non-switch ids are checked verbatim.

Extends the cross-profile harness with gated getAPIProvider / NVIDIA / subscriber
overrides and adds branch-append + verbatim-allowlist regressions (red-green).

* fix(model): key profile-switch handling on the marker across picker and command

The allowlist/SDK paths already used the switchToProfileId marker, but two
surfaces still keyed on the raw `__switch_profile__:` value prefix:

- ModelPicker's inline-picker filter hid any option whose value started with
  the prefix, so a real custom model id like `__switch_profile__:vendor:gpt-5.4`
  disappeared from prompt/settings pickers. It now filters on
  `switchToProfileId === undefined`.
- the /model command decoded parseSwitchProfileValue(model) for any prefixed
  string and tried to activate the encoded profile id, so selecting such a
  custom model activated a nonexistent profile instead of setting the literal
  model. It now only treats the value as a switch when the decoded profile id
  maps to a real configured provider profile — which every synthesized switch
  option does, and a prefix-colliding custom id does not.

Drops the now-unused SWITCH_PROFILE_VALUE_PREFIX import from ModelPicker. Adds a
picker regression (marked switch hidden, prefixed custom model stays visible) and
completes the cross-profile branch coverage (MiniMax, Xiaomi MiMo, ant) so every
branch that appends inactive-profile options is locked.

* test(model): register target profiles in cross-profile switch tests

The /model command now only treats a `__switch_profile__:` value as a switch
when its decoded profile id maps to a real configured provider profile. The
cross-profile switch tests set up setActiveProviderProfile but left the shared
getProviderProfiles mock empty, so the new guard classified their switch values
as literal models and the fast-mode / effort / extra-usage assertions no longer
ran. Register each test's target profile via getProviderProfiles so the switch
path executes as intended.

* fix(model): gate cross-profile switches on the selected option marker

Selecting a value that merely parses as `__switch_profile__:<profileId>:<model>`
activated the provider whenever <profileId> existed, so a literal custom model
id such as `__switch_profile__:profile_openai:gpt-5-mini` wrongly switched the
active provider instead of being applied verbatim.

Thread the picked option's `switchToProfileId` marker from ModelPicker.onSelect
(selectOptions already carries it) and only activate a profile when the marker
matches the decoded id. The effort/display resolver had the same gap — it
decoded every prefixed value; gate it on a genuine marker-backed switch option
too. Add a regression asserting a marker-less prefixed id is applied literally.

* test(model): cover Max/Team Premium and empty-catalog switch-append paths

The cross-profile branch-coverage suite exercised the populated-catalog returns
but not the Max/Team Premium subscriber early return nor the empty-catalog
fallbacks (NVIDIA/MiniMax/Xiaomi), which are the same paths that previously
dropped the inactive-profile switch options. Lock them so every changed return
that appends `...inactiveProfileOptions` is covered.

* fix(model): keep inactive-profile switch options in /model discovery overrides

The interactive /model command passes an optionsOverride into ModelPicker for
descriptor-backed and legacy OpenAI-compatible discovery contexts, built from
mergeActiveProfileModelOptions which only merges the ACTIVE profile's route
models. Because the picker renders optionsOverride ?? getModelOptions(), the
inactive-profile switch entries getModelOptions() appends never reached those
paths, so the unified switcher vanished for provider-profile routes
(OpenRouter/Kimi/MiniMax, refreshed local profiles). Re-append the same
inactive-profile switch options (allowlist-filtered on the decoded target) to
any override list before handing it to the picker.

* fix(model): base the switch marker on the presented option, treat ties as ambiguous

The picker derived switchToProfileId with selectOptions.find(value===...), and
the effort/display resolver decoded when any getModelOptions() entry with the
same value carried the marker. If a literal custom model id collided with an
encoded switch value, the literal could borrow a different same-value option's
marker and wrongly activate a provider. Add resolveSelectedSwitchProfileId,
which keys on the actual presented option and treats duplicate-value matches as
ambiguous (no switch), and route both the onSelect marker and the decode
decision through it. — data não informada\n  - `338f9ad85fc93dce6b0702ebf9147f3b49a21e34` — chore(main): release 0.23.0 (#1870)

Co-authored-by: github-actions[bot] <41898282+github-actions[bot]@users.noreply.github.com> — data não informada\n  - `b8c8b2417bb329d8757d38c236868f2a23f0f535` — fix(opencode-go): surface clear error on subscription quota exhaustion (#1749)

* fix(opencode-go): surface clear error on subscription quota exhaustion

The opencode.ai/zen/go gateway returns 429 with FreeUsageLimitError or
GoUsageLimitError in the body when a user's Go subscription quota runs
out. Previously these fell through to the generic "Request rejected
(429)" path, causing a mysterious stop with no actionable hint.

Detect the opencode-go-specific error markers, surface a clear message
with the upgrade URL (free tier) or reset duration + workspace + limit
name (paid tier), and skip retry — the quota is terminal until reset.

Mirrors the canonical implementation in anomalyco/opencode
packages/opencode/src/session/retry.ts.

* fix(api): abort retry and avoid thinking hang on quota/allotment exhaustion

* fix: implement request URL precedence and add test coverage

* fix(api): make 'x-opencode-request-url' header authoritative for OpenCode Go errors

* fix(api): preserve OpenCode Go quota message and reuse non-stream converter in JSON fallback

Addresses the two remaining P2 review items on #1749.

withRetry: the early isQuotaExhausted guard wrapped OpenCode Go
FreeUsageLimitError/GoUsageLimitError 429s in the generic "API quota
exhausted or not enabled" message, clobbering the actionable subscribe/
reset guidance. Skip the generic guard for OpenCode Go quota errors so they
fall through to the standard shouldRetry=false terminal path, which rethrows
the original APIError and lets getAssistantMessageFromError surface the
specific message. Consolidate detection in a shared isOpenCodeGoQuotaError
predicate (errors.ts) and drop the duplicated inline header check in
shouldRetry.

openaiShim: the application/json fallback in openaiStreamToAnthropic
hand-rolled a thin converter that dropped tool_calls, forwarded raw OpenAI
finish_reason values as Anthropic stop reasons, skipped array-content
normalization, bypassed <think> stripping, and lost raw text tool-call
recovery. Extract the established non-streaming conversion into a shared
convertNonStreamingResponseToAnthropicMessage and route the fallback through
it, re-emitting the result as stream events. _convertNonStreamingResponse
now delegates to the same function.

Adds regression coverage: a withRetry test proving the OpenCode Go message
survives the retry loop, and JSON-fallback tests for tool_calls, stop-reason
mapping, <think> stripping, array content, and raw text tool-call recovery.

* fix(api): terminate OpenCode Go quota in fast mode; treat empty tool_calls as absent

Addresses CodeRabbit's review on #1749.

- [Major] withRetry.ts: throw CannotRetryError for isOpenCodeGoQuotaError BEFORE
  the fast-mode 429 fallback. Previously the guard only *skipped* the generic
  quota throw, so an OpenCode Go 429 while fast mode was active hit the fast-mode
  retry/cooldown path instead of surfacing the quota message immediately.
  Wrapping the original APIError still preserves the OpenCode Go assistant
  message via getAssistantMessageFromError. Adds a fast-mode regression test
  (mutation-checked) and a forceFastMode option on the test helper.

- [Minor] openaiShim.ts: an empty tool_calls array is truthy, which skipped the
  raw "Tool calls requested" recovery in convertNonStreamingResponseToAnthropicMessage.
  Gate on a single hasStructuredToolCalls (length > 0) check across both the
  string- and array-content raw-recovery paths and the structured loop. Adds a
  JSON-fallback regression test for tool_calls: [] (mutation-checked).

- [Minor] openaiShim.test.ts: collectFallbackEvents now saves and restores
  globalThis.fetch in a finally block so the stub can't leak past the helper.

* test(openai-shim): cover empty tool_calls raw-recovery on array content too

Addresses CodeRabbit's follow-up on #1749: the empty-tool_calls regression only
exercised the string-content path, but the hasStructuredToolCalls fix also gates
the array-content branch. Add a companion JSON-fallback test with array-form
message.content and tool_calls: [] so the array branch can't regress silently.
Mutation-checked: reverting hasStructuredToolCalls to a truthiness check fails it.

* fix(api): preserve OpenCode Go quota errors

---------

Co-authored-by: jatmn <the@jat.mn> — data não informada\n  - `2edec9a1407b6afd1d12260fca20c59c771269f6` — fix(deps): ship a zero-warning, minimal install (#1784)

* fix(deps): ship a zero-warning, minimal install

The published package declared 62 runtime `dependencies`, but `dist/cli.mjs`
is a fully-bundled esbuild output that inlines almost all of them. End users
therefore installed ~476 transitive packages — including three subtrees the
bundle never needs at install time, each emitting an install warning:

  - node-domexception (deprecated) via google-auth-library
  - protobufjs (allow-scripts)     via @grpc/* (already bundled into dist)
  - sharp (allow-scripts)          native image module

The repo's `overrides`/`allowScripts` silence these locally, but those are
root-only npm settings and are ignored when the package is installed as a
dependency — so end users saw the warnings.

Core changes:
  - package.json: runtime dependencies trimmed 62 -> 3 (@orama/orama,
    @orama/plugin-data-persistence, @vscode/ripgrep). Bundled packages, plus
    the optional sharp/google-auth-library, move to devDependencies so they
    are built/tested but not shipped.
  - package.json: @anthropic-ai/sdk, @modelcontextprotocol/sdk, react and
    react-reconciler declared as OPTIONAL peerDependencies — externalized by
    the ./sdk bundle but bundled into the CLI. Optional peers keep the CLI
    install minimal and warning-free while still resolving for ./sdk consumers.
  - externals.ts: sharp, google-auth-library and @anthropic-ai/bedrock-sdk
    marked OPTIONAL_RUNTIME_EXTERNALS (loaded on demand, not shipped).
  - validate-externals.ts: runtime deps validate against externals; bundled
    deps validate against dependencies + devDependencies.
  - client.ts: load @anthropic-ai/bedrock-sdk via the runtime importer so
    esbuild no longer inlines it and hoists its static @aws-sdk import into
    the CLI bundle (that was a startup crash for default installs).

Optional-dependency UX (consistent, actionable errors):
  - New src/utils/optionalRuntimeModule.ts exports importRuntimeModule and
    importOptionalRuntimeModule. The optional variant translates a missing
    package (code === 'ERR_MODULE_NOT_FOUND', specifier present in message)
    into "<feature> requires "<pkg>" ... Run `npm i -g <pkg>`". Generic so
    typed call sites keep their module types.
  - Routed ALL optional-package load sites through it (previously only one
    did): google-auth-library (client.ts, auth.ts, geminiAuth.ts),
    @anthropic-ai/foundry-sdk + @azure/identity (client.ts), and the
    @aws-sdk/* Bedrock paths (model/bedrock.ts, tokenEstimation.ts, aws.ts).
  - imageProcessor.ts: sharp-missing error now says `npm i -g sharp`.
  - docs/advanced-setup.md: new "Optional provider packages" table and a
    Vertex note documenting the on-demand installs.
  - Unit test for the helper (friendly error, success path, specifier match,
    raw passthrough).
  - knip.json: ignore google-auth-library (now loaded via runtime string).

Verified on the current tree:
  - tsc, build/validate-externals, knip, and tests all pass.
  - npm pack + install --omit=dev adds 8 packages, zero deprecation/
    allow-scripts/funding warnings; --version/--help/mcp list run.
  - With packages absent, CLAUDE_CODE_USE_BEDROCK and CLAUDE_CODE_USE_VERTEX
    print the friendly `npm i -g <pkg>` error (verified end-to-end).
  - ./sdk imports once its optional peers are present (24 exports, no warns).
  - Bundled ajv + ajv-formats validate with no ajv installed; no unguarded
    native runtime requires (fsevents absent in chokidar 4; bun:sqlite Bun-only).

Trade-off: image reads, AWS Bedrock, Azure Foundry and GCP/Vertex now prompt
a one-time `npm i -g <pkg>` instead of being shipped to every user.

Co-Authored-By: OpenClaude <openclaude@gitlawb.com>

Review fixes (CodeRabbit + jatmn):
- validate-externals: the INTENTIONALLY_BUNDLED exemption is now scoped per
  bundle. The CLI exempts every bundled package; the SDK does NOT exempt
  packages declared as peerDependencies (keyed on package.json, an independent
  source of truth) so dropping react/@anthropic-ai/sdk from SDK_EXTERNALS now
  fails validation instead of silently passing. Added an explicit minimal-
  install contract check: bundled packages must be devDependencies-only — never
  in `dependencies`, and only the SDK-external subset may be optional peers.
  Validation logic extracted to scripts/externalsValidation.ts + tests.
- FileReadTool oversized-image fallback now loads via the shared
  getImageProcessor() (not a raw import('sharp')) and re-throws
  ImageProcessorUnavailableError, so a missing processor surfaces the
  `npm i -g sharp` install hint instead of returning an over-budget image.
- optionalRuntimeModule: match the missing specifier as a QUOTED token, not a
  raw substring, so a missing transitive package whose name contains the
  requested one (sharp vs sharp-libvips, @aws-sdk/client-bedrock vs
  @aws-sdk/client-bedrock-runtime) no longer triggers the wrong install hint.
  Predicate extracted to isMissingSpecifierError() with regression tests.
- docs/advanced-setup.md: the Vertex auth section now shows both documented
  paths (gcloud ADC and a GOOGLE_APPLICATION_CREDENTIALS service-account file).

Review fixes (round 2, CodeRabbit):
- validate-externals: assert the optional-peer install contract — every
  peerDependency must be { optional: true } in peerDependenciesMeta
  (validateOptionalPeers), so losing that flag fails the build instead of
  silently reintroducing install warnings.
- validate-externals: hard-check OPTIONAL_RUNTIME_EXTERNALS placement
  (validateOptionalRuntimeexternals). Anything esbuild can see statically must
  stay external in BOTH bundles (dropping sharp/google-auth-library now fails);
  the runtime-indirection-only subset (new RUNTIME_INDIRECTION_ONLY_EXTERNALS)
  must stay OUT of externals so esbuild never re-exposes their static imports.
- Deeper-dig fix: @anthropic-ai/foundry-sdk was misclassified as
  INTENTIONALLY_BUNDLED, but it is loaded only through the Function indirection
  (esbuild never sees it, so it was never actually bundled) — its sole presence
  in dist is the specifier string. Per the PR's own "Azure Foundry now prompts"
  trade-off it is on-demand, so it now lives in OPTIONAL_RUNTIME_EXTERNALS +
  RUNTIME_INDIRECTION_ONLY_EXTERNALS (mirroring bedrock-sdk). sandbox-runtime is
  genuinely statically imported, so it stays bundled.
- Provider-routing coverage (scripts/optionalRuntimeSpecifiers.test.ts): a
  static scan asserts every importOptionalRuntimeModule specifier is a declared
  OPTIONAL_RUNTIME_EXTERNAL and never also INTENTIONALLY_BUNDLED — the
  invariant that keeps a provider's optional package loadable on demand.
- All new validators extracted to scripts/externalsValidation.ts with tests.

Review fixes (round 3, CodeRabbit):
- client.ts: gate the Vertex google-auth-library import behind the non-skip
  branch. CLAUDE_CODE_SKIP_VERTEX_AUTH (proxy/test) uses a mock GoogleAuth and
  must not require the optional package; it was loaded unconditionally before.
- optionalRuntimeModule: drop the hard-coded `npm i -g`. The helper backs both
  the global CLI and project-local ./sdk consumers, so the hint is now
  context-neutral ("npm install <pkg>" / add -g for the global CLI).
- validate-externals: every SDK_ONLY_EXTERNALS entry must STAY a
  peerDependency (a dropped peer leaves runtimeDeps while the SDK still
  externalizes it); and OPTIONAL_RUNTIME_EXTERNALS must never be shipped (fail
  on overlap with dependencies/peerDependencies). Both with tests + live-verified.
- optionalRuntimeSpecifiers.test: pin the EXACT set of optionally-loaded
  specifiers instead of a >=5 count (a count passes even if a provider path
  regresses).
- attachments: extract tryReadEditedImageAttachment() — background watched-file
  image attachments DEGRADE to null on any failure (incl.
  ImageProcessorUnavailableError) so a missing optional package never aborts a
  turn, while the explicit FileReadTool path still surfaces the install hint.
  Deterministic regression test (bad path -> null).
- docs: Bedrock row notes profile-based auth also needs
  @aws-sdk/credential-providers; install-hint wording matches the new message.

Review fixes (round 4, CodeRabbit):
- attachments: stop sending the raw file path through the analytics
  bypass-cast (tengu_watched_file_compression_failed). Send only the safe
  file extension via getFileExtensionForAnalytics, matching the existing
  tengu_file_read_dedup pattern, so no usernames/project paths can leak.
- externals.ts: corrected the OPTIONAL_RUNTIME_EXTERNALS header comment,
  which still claimed all entries "remain in COMMON_EXTERNALS" — no longer
  true since the indirection-only subset (bedrock/foundry) must stay OUT of
  the externals lists.

(Other CodeRabbit comments on this push re-surface items already addressed in
prior commits: the peerDependenciesMeta-optional check (validateOptionalPeers),
the SDK-peers-present and optional-not-shipped validator rules, the
exact-specifier-set test, the attachments degrade contract + test, and the
context-neutral install hint are all present. The "assert every optional
external is a devDependency" suggestion is intentionally NOT applied: @aws-sdk/*
and @azure/identity are transitive devDeps via bedrock-sdk/foundry-sdk, so a
blanket assertion would be incorrect; source resolution is covered by the
build + tests that import these packages.)

Review fixes (round 5, CodeRabbit):
- attachments: stop leaking file paths via logError in the background-image
  degrade path. readImageWithTokenBudget can throw path-bearing messages
  (e.g. "Image file is empty: <path>") and logError persists message/stack, so
  log only the error TYPE name now. (Analytics payload was already sanitized.)
- attachments: tryReadEditedImageAttachment takes an injectable reader so the
  degrade contract is tested for the EXACT error types — ImageProcessorUnavailableError
  and a path-bearing read error both degrade to null (not just ENOENT) — plus a
  success case. No mocking.
- validate-externals: enforce the source-install half of the optional contract.
  Non-transitive OPTIONAL_RUNTIME_EXTERNALS must be devDependencies so `bun
  install` source builds resolve them. The new TRANSITIVE_OPTIONAL_EXTERNALS
  documents the exemption (@aws-sdk/* via @anthropic-ai/bedrock-sdk, @azure/identity
  via @anthropic-ai/foundry-sdk — provided transitively, not direct devDeps). A
  blanket "all optionals are devDeps" check would have wrongly failed on those.
  Tests + live-verified (dropping sharp from devDependencies now fails).

Review fixes (round 6, CodeRabbit + jatmn):
- optionalRuntimeSpecifiers.test: the call-site scan regex missed
  generic-annotated calls (importOptionalRuntimeModule<...>(...)) in
  model/bedrock.ts and tokenEstimation.ts, so the exact-set assertion was
  incomplete. Regex now allows an optional generic; EXPECTED_SPECIFIERS adds
  @aws-sdk/client-bedrock and @aws-sdk/client-bedrock-runtime (7 total).
- importOptionalRuntimeModule default generic is now <T = unknown> (was any),
  so destructured imports are no longer silently any. Every call site now
  supplies its module type — typeof import('<pkg>') where the package is
  type-resolvable (bedrock-sdk, foundry-sdk, @aws-sdk/credential-providers,
  google-auth-library), and a named minimal-shape alias for @azure/identity
  (not a direct devDep, so typeof import can't resolve it). This gives
  compile-time verification of each provider's module contract (export names,
  shapes) — the structural answer to the "cover the provider branches" ask.
- attachments: tryReadEditedImageAttachment takes injectable {read,log,track};
  a new test asserts the sanitized-telemetry contract directly — the logError
  payload is path-free and the analytics payload carries only `ext`, never the
  edited-image path.

* fix(deps): address optional runtime review findings

* test(deps): isolate optional runtime importer mocks

* fix(deps): clarify AWS optional auth labels

* fix(deps): close optional runtime review gaps

---------

Co-authored-by: jatmn <the@jat.mn> — data não informada\n  - `2a506f9f38609c65903a70e10429573aa893a917` — added tencent hy3 to opengateway available models (#1876) — data não informada\n  - `4be017bd4dca1fc757e1664292c12a7057e8b05b` — fix: resolve zai-compatible config for all GLM remote models (#1752)

* fix: resolve zai-compatible config for all GLM remote models

* fix: address PR reviews for GLM thinking continuation, custom aliases, Fireworks catalog entries, and reasoning effort preservation

* fix(integrations): gate GLM Z.AI shim to non-catalog routes

The name-based matcher applied the full Z.AI reasoning contract to any
model path containing `glm-<digit>`, overriding catalog-backed non-Z.AI
routes (NEAR AI `zai-org/GLM-5.1-FP8`, Fireworks `glm-5p2`). Now the GLM
branch fires only when there is no catalog entry; Z.AI-contract GLM
routes (opencode-go, atlas-cloud) declare the shim explicitly via
transportOverrides, and a shared ZAI_GLM_OPENAI_SHIM constant is the
single source of truth. Adds negative (NEAR AI) and positive
(opencode-go, atlas) regressions.

* test(integrations): cover the direct Z.AI vendor catalog route in the gating block

Addresses CodeRabbit's nitpick on #1752: the GLM catalog-aware gating describe
block had NEAR AI (negative), opencode-go, and atlas-cloud (positive) cases but
no direct `zai` vendor catalog positive. Add one asserting the full GLM contract
(routeId 'zai', preserveReasoningContent, thinkingRequestFormat 'zai-compatible',
requireReasoningContentOnAssistantMessages) alongside the override-based routes.

* fix(effort): extend supportsZaiReasoningEffort for provider-prefixed GLM-5.2 models

The previous implementation only matched bare 'glm-5.2' and 'zai-org/glm-5.2'. When accessed via an aggregator alias like 'openrouter/zhipu/glm-5.2', the model name doesn't start with 'glm-' or match the zai-org prefix, so supportsZaiReasoningEffort returned false and reasoning_effort was omitted from the request body. Add an endsWith('/glm-5.2') fallback to match any provider-scoped path ending in the base model name.

* fix(gateways): wire Z.AI GLM shim to atlas-cloud GLM entries and opengateway GLM 5.2

- Add enableToolStreaming to ZAI_GLM_OPENAI_SHIM shared constant
- Apply transportOverrides.openaiShim to all 7 atlas-cloud zai-org/glm-*
  entries so catalog-backed routes get the full Z.AI shim contract
- Layer Z.AI-specific overrides (thinkingRequestFormat,
  preserveReasoningContent, enableToolStreaming) on the opengateway-glm-5.2
  entry without conflicting with the gateway-level max_completion_tokens
  and removeBodyFields

Refs #1752

* refactor(gateways): derive opengateway GLM shim from shared ZAI_GLM_OPENAI_SHIM

* fix(gateways): align Atlas + OpenCode Zen GLM entries with Z.AI wire format

- Atlas Cloud GLM entries: wireFormat 'reasoning_effort' → 'zai_compatible'

- OpenCode Go catalogEntry: add reasoning + capabilities for zaiGlm models

- OpenCode Go model descriptors: add reasoning: true for GLM entries

* fix(integrations): rebase onto upstream/main, fix Atlas/OpenCode Zen GLM wiring per review

Rebased onto upstream/main (13cf30af) which brought in verified Moonshot/Kimi Code effort metadata.

Changes:

- atlas-cloud.ts: restored upstream moonshot/grok entries; kept GLM entries with wireFormat: 'zai_compatible' + ZAI_GLM_OPENAI_SHIM

- opencode.ts: added zaiGlm metadata + ZAI_GLM_OPENAI_SHIM for glm-5.1 and glm-5

- effort.codex.test.ts: updated expectations for glm-5.2 (zai_compatible), split GLM into separate verification loop

- runtimeMetadata.test.ts: merged upstream Moonshot/Kimi Code tests, updated Atlas Cloud maxOutputTokens

* fix(integrations): type opencode zen openaiShim and test zen GLM catalog-aware overrides

* fix(integrations): restrict Z.AI GLM effort levels and add Atlas GLM regression test — data não informada\n  - `885bd81045d4370fef028d129e0930159cbefcf8` — fix(hicap): add missing hicap-claude-opus-4.7 catalog entry (#1797)

* fix(hicap): add missing hicap-claude-opus-4.7 catalog entry

* test(integrations): cover hicap-claude-opus-4.7 runtime limits and catalog entry

* fix(hicap): add claude-opus-4-7 alias and update provider request test

* test(hicap): cover opus 4.7 catalog aliases — data não informada
\n## 57. William-kelvem94/Openclaw_Docker_Will

- **Registros retornados:** 13
- **Amostra:**
  - `adcbe7580c50346986fcbc703fe1db965aacbee9` — Add ripgrep 14.1.0 Debian package

Add ripgrep_14.1.0-1_amd64.deb as a new binary artifact. This introduces the Debian package for ripgrep v14.1.0 (amd64) to the repository for distribution/testing. — data não informada\n  - `e57a6192dbc8798a294c40e781d533c117cfb59a` — Add start_openclaw script; install zstd in WSL

Update setup_wsl.sh to install zstd alongside curl. Add scripts/start_openclaw.sh which stops any running OpenClaw gateway, writes a local ~/.openclaw/openclaw.json config (token: "admin123"), and launches the gateway bound to loopback on port 8000, printing the token and UI URL. — data não informada\n  - `9289c1e7142deb0d18c46d4bb2c317ef7bc26a66` — docs: adiciona guia em txt para setup local — data não informada\n  - `3f21a9dfaf713c47536177803604ece565b1ee2e` — docs: adiciona guia e script para setup local WSL+Ollama+OpenClaw — data não informada\n  - `dc71d94e0ae419e3a7f8de0afd29914344d40435` — fix: adiciona token auth para bind lan, todos erros de deploy corrigidos — data não informada\n  - `01607a30df129f951ab92f91b3fe00d2527c7208` — fix: bind invalido 0.0.0.0, troca para lan — data não informada\n  - `bf871620cca9d1fb5fc19d2f453e78b266a5b26f` — fix: atualiza Node.js para v22 via NodeSource (Ubuntu apt vinha com v12) — data não informada\n  - `55e6732fb9eed2fb7f0a1577a4c19c329de80d99` — fix: instala OpenClaw no build e inicia gateway com --allow-unconfigured (#6) — data não informada\n  - `743bcd2387071a872cc4f1a8d78fbfe9728e3e36` — infra: Ubuntu base, instalação manual OpenClaw, docs e scripts para cloud — data não informada\n  - `f1f3858c7eef72326a4f8ec05b1dacf3b8430a9f` — fix: openclaw docker deploy sem onboarding interativo (OPENCLAW_SKIP_ONBOARDING=1) — data não informada\n  - `ab5e9d386609ac9fa4d2391539e7c5cccfa7cc8a` — fix: corrige erro de configuração ausente do OpenClaw via gateway.mode=local — data não informada\n  - `9c18ea969e83f71327be9009e43e49e8e39f3479` — Configuração inicial: Docker, Render e segurança — data não informada\n  - `930054bc723e19f49686597ca0a77e7ee31297ba` — Initial commit — data não informada
\n## 58. William-kelvem94/Personal-Voice-Assistent

- **Registros retornados:** 2
- **Amostra:**
  - `b3757bba21ac03092b7aa3e44013585ef6dad035` — Code style and formatting cleanup

Apply consistent formatting and style fixes across pva.py, pvatrayicon.py, usr/local/sbin/ai.py, and usr/local/sbin/f5tts.py. Changes include: normalizing quotes to double quotes, reflowing and indenting long argument lists, tidying argparse definitions and prints, minor refactors of http_request and function signatures, small whitespace/PEP8 adjustments, and cleaner string concatenation for os.system calls. No intended behavioral changes — primarily readability and consistency improvements. — data não informada\n  - `012b8fa5c193f75643ba7e5feebe6b022bed4beb` — Initial commit — data não informada
\n## 59. William-kelvem94/pixel-agents

- **Registros retornados:** 100
- **Amostra:**
  - `a915301f09b0f84382363a1ae00ade772d6dbc56` — fix: subagent characters not despawning on completion (#231)

Sub-agent characters were created with transient hook tool IDs (hook-XXXX)
but all cleanup paths used JSONL tool IDs (toolu_XXXX), causing a key
mismatch that prevented character removal.

Three fixes:
- Skip agentToolStart from PreToolUse for Task/Agent tools so JSONL
  creates sub-agent characters with stable tool IDs
- Always send agentToolStart/Done for Task/Agent via JSONL even when
  hooks are active, ensuring consistent sub-agent lifecycle
- Add safety net agentToolsClear in markAgentWaiting when activeToolIds
  is empty (JSONL cleared them before Stop hook fired)
- SubagentStop now only matches parents with active sub-agent tracking

Co-authored-by: Pablo De Lucca <pablo@Pablos-Mac-mini.local>
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com> — data não informada\n  - `7e90d12b336f4381e6fcdb9bbc19469b5c0fcf91` — feat: hooks-first session management with dual-mode architecture (#214)

* feat: add SessionStart/SessionEnd hooks for /clear detection and session lifecycle

* feat: hooks-first session management with external detection, /clear, and full hook coverage

* docs: add dual-mode architecture documentation

* feat: expand PreToolUse/PostToolUse to handle tool visuals

* test: update and expand hookEventHandler tests for hooks-first implementation

* fix: /resume spawning new agent

* fix: relax session end grace time for /resume

* fix: normalize paths in hook projectDir comparison for Windows

* fix: Windows path casing in hook projectDir comparisons and session adoption

* feat: enable debug logging by default

* feat: provider-agnostic hooks with optional transcript_path

* feat: heuristic /resume detection for internal agents

* test: add provider-agnostic hook tests for optional transcript_path — data não informada\n  - `a679dd630bd4a8a960dea713fe485d053a380f54` — fix: add shared/ to lint, format, and lint-staged (#212)

* fix: add shared/ to lint, format, and lint-staged

* fix: remove unused exports and tag barrel-reexported symbols as @internal for knip — data não informada\n  - `8a19483ecf56e6b397e055e047006bb19a738da4` — chore(deps-dev): bump the minor-and-patch group across 1 directory with 3 updates (#209)

Bumps the minor-and-patch group with 3 updates in the /webview-ui directory: [@types/node](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/node), [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/tree/HEAD/packages/typescript-eslint) and [vite](https://github.com/vitejs/vite/tree/HEAD/packages/vite).


Updates `@types/node` from 25.5.0 to 25.5.2
- [Release notes](https://github.com/DefinitelyTyped/DefinitelyTyped/releases)
- [Commits](https://github.com/DefinitelyTyped/DefinitelyTyped/commits/HEAD/types/node)

Updates `typescript-eslint` from 8.57.1 to 8.58.0
- [Release notes](https://github.com/typescript-eslint/typescript-eslint/releases)
- [Changelog](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/typescript-eslint/CHANGELOG.md)
- [Commits](https://github.com/typescript-eslint/typescript-eslint/commits/v8.58.0/packages/typescript-eslint)

Updates `vite` from 8.0.2 to 8.0.3
- [Release notes](https://github.com/vitejs/vite/releases)
- [Changelog](https://github.com/vitejs/vite/blob/main/packages/vite/CHANGELOG.md)
- [Commits](https://github.com/vitejs/vite/commits/create-vite@8.0.3/packages/vite)

---
updated-dependencies:
- dependency-name: "@types/node"
  dependency-version: 25.5.2
  dependency-type: direct:development
  update-type: version-update:semver-patch
  dependency-group: minor-and-patch
- dependency-name: typescript-eslint
  dependency-version: 8.58.0
  dependency-type: direct:development
  update-type: version-update:semver-minor
  dependency-group: minor-and-patch
- dependency-name: vite
  dependency-version: 8.0.3
  dependency-type: direct:development
  update-type: version-update:semver-patch
  dependency-group: minor-and-patch
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> — data não informada\n  - `8ac3c3b0b235f78d868791fe3ad16db19dc804b7` — chore(deps-dev): bump the minor-and-patch group across 1 directory with 5 updates (#210)

Bumps the minor-and-patch group with 5 updates in the / directory:

| Package | From | To |
| --- | --- | --- |
| [@playwright/test](https://github.com/microsoft/playwright) | `1.58.2` | `1.59.1` |
| [@types/node](https://github.com/DefinitelyTyped/DefinitelyTyped/tree/HEAD/types/node) | `25.5.0` | `25.5.2` |
| [esbuild](https://github.com/evanw/esbuild) | `0.27.4` | `0.28.0` |
| [eslint](https://github.com/eslint/eslint) | `10.1.0` | `10.2.0` |
| [typescript-eslint](https://github.com/typescript-eslint/typescript-eslint/tree/HEAD/packages/typescript-eslint) | `8.57.1` | `8.58.0` |



Updates `@playwright/test` from 1.58.2 to 1.59.1
- [Release notes](https://github.com/microsoft/playwright/releases)
- [Commits](https://github.com/microsoft/playwright/compare/v1.58.2...v1.59.1)

Updates `@types/node` from 25.5.0 to 25.5.2
- [Release notes](https://github.com/DefinitelyTyped/DefinitelyTyped/releases)
- [Commits](https://github.com/DefinitelyTyped/DefinitelyTyped/commits/HEAD/types/node)

Updates `esbuild` from 0.27.4 to 0.28.0
- [Release notes](https://github.com/evanw/esbuild/releases)
- [Changelog](https://github.com/evanw/esbuild/blob/main/CHANGELOG.md)
- [Commits](https://github.com/evanw/esbuild/compare/v0.27.4...v0.28.0)

Updates `eslint` from 10.1.0 to 10.2.0
- [Release notes](https://github.com/eslint/eslint/releases)
- [Commits](https://github.com/eslint/eslint/compare/v10.1.0...v10.2.0)

Updates `typescript-eslint` from 8.57.1 to 8.58.0
- [Release notes](https://github.com/typescript-eslint/typescript-eslint/releases)
- [Changelog](https://github.com/typescript-eslint/typescript-eslint/blob/main/packages/typescript-eslint/CHANGELOG.md)
- [Commits](https://github.com/typescript-eslint/typescript-eslint/commits/v8.58.0/packages/typescript-eslint)

---
updated-dependencies:
- dependency-name: "@playwright/test"
  dependency-version: 1.59.1
  dependency-type: direct:development
  update-type: version-update:semver-minor
  dependency-group: minor-and-patch
- dependency-name: "@types/node"
  dependency-version: 25.5.2
  dependency-type: direct:development
  update-type: version-update:semver-patch
  dependency-group: minor-and-patch
- dependency-name: esbuild
  dependency-version: 0.28.0
  dependency-type: direct:development
  update-type: version-update:semver-minor
  dependency-group: minor-and-patch
- dependency-name: eslint
  dependency-version: 10.2.0
  dependency-type: direct:development
  update-type: version-update:semver-minor
  dependency-group: minor-and-patch
- dependency-name: typescript-eslint
  dependency-version: 8.58.0
  dependency-type: direct:development
  update-type: version-update:semver-minor
  dependency-group: minor-and-patch
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> — data não informada\n  - `221ad7a5ab7b7dfbdfb7071dfe849afb593fea46` — feat: claude code hooks for instant agent status detection (#187)

* feat: replace heuristic agent status detection with Claude Code Hooks

Use Claude Code's hook system (PermissionRequest, Stop, Notification) for
instant, accurate detection of permission prompts and turn completion,
replacing the 7s/5s heuristic timers.

- Add hookServer.ts: localhost HTTP server receives hook events via POST
- Add hookInstaller.ts: auto-installs hooks into ~/.claude/settings.json
  (user-level, zero repo clutter) and writes hook script to ~/.pixel-agents/hooks/
- Add hookEventHandler.ts: maps session_id → agentId, dispatches events
- Heuristic timers kept as fallback (suppressed when hooks are active)
- Multi-window support via PID-based port files
- Preemptive hookDelivered flag avoids first-turn race condition

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* feat: add permission sound notification

Descending A5 → E5 chime plays when an agent needs permission approval,
distinct from the ascending done sound.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* feat: replace hook infrastructure with server foundation

* fix: cleanup for server foundation (timing-safe auth, body guard, provider validation)

* fix: CLAUDE.md update

* test: add server foundation e2e tests

* fix: addressing some moderate and high vulnerability with npm audit and npm audit fix

* feat: audit checks are no longer advisory

* feat: knip for finding unused dependency

* chore: remove unused dependency

* chore: lint hardening, check-types fails in CI

removed check-types in pre-commit since it adds too much time when committing
it already fails in pipeline and blocks the merge

* chore: add gitleaks

* revert: error is visible in CI

precommit and prepush should block essential or run fast. Or they should autolint

* fix: webview audit

* fix: unreachable code

* fix: harden CI audits, tsconfig lint settings

* chore: add type-checking to pre-push hook

* fix: prevent /clear from adopting pre-existing shell terminals

* chore: unify lint/test scripts, add server to CI coverage, update docs

* fix: match hooks info modal styling

* chore: change ESLint rules from warn to error - will block committing

* chore: configure knip workspaces

---------

Co-authored-by: Pablo De Lucca <pablo@Pablos-Mac-mini.local>
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
Co-authored-by: Florin Timbuc <florin@sowild.design>
Co-authored-by: NNTin <nguyen.ngoctindaniel@gmail.com> — data não informada\n  - `1afbd538593fa6a20f3e4b0d388049a8efd8ce03` — feat: load custom characters from assets directory (#208)

Co-authored-by: Pablo De Lucca <pablo@Pablos-Mac-mini.local>
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com> — data não informada\n  - `dfb5b30f7699e2a7613952e5e4d4c8637cb07d23` — refactor: migrate webview-ui to Tailwind CSS v4 (#204)

* feat: migrate webview-ui from inline styles to Tailwind CSS v4

Replace all inline React styles with Tailwind utility classes across
the webview. Centralizes repeated patterns (panels, buttons, modals,
menus, tabs, checkboxes) as component classes in index.css using
@layer components, and defines the full pixel-art design token set
via @theme with 1px spacing base.

- Install tailwindcss + @tailwindcss/vite
- Add @tailwindcss/vite plugin to vite.config.ts
- Convert 10 component files from style={{}} to className
- Eliminate hover useState in several components (use hover: variants)
- Net reduction: ~500 lines removed

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* refactor: extract UI components, define text scale, clean up theme tokens

- Extract 5 reusable shadcn-style UI components (Button, Modal,
  Dropdown, MenuItem, Checkbox) into components/ui/
- Button supports variant (default/active/disabled/accent/ghost) and
  size (sm/md/lg/xl) props, replacing 12 CSS component classes
- Move color values from @theme to :root for VS Code intellisense
  color swatches, reference via @theme inline for utility generation
- Define pixel-art text size scale (text-xs through text-5xl, base=22px)
  and set as inherited default on body
- Strip redundant pixel- prefix from all color tokens
- Rename agent-* tokens to accent-*, set text color as body default
- Remove 12 CSS component classes from index.css, keeping only 4
  layout-specific ones (pixel-panel, pixel-color-panel, pixel-thumb-btn,
  pixel-carousel)

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* refactor: extract ColorPicker and ItemSelect components, simplify editor toolbar

- Extract ColorPicker component (HSBC sliders + optional colorize
  toggle), replacing 3 repeated slider groups (~90 lines) in
  EditorToolbar with one-liner usages
- Extract ItemSelect component (canvas thumbnail button with draw
  callback), replacing FloorPatternPreview, WallSetPreview, and
  inline furniture preview (~90 lines)
- Remove pixel-color-panel and pixel-thumb-btn CSS classes (styling
  now lives in components)
- Use Checkbox component for Debug View toggle in SettingsModal
- Update furniture manifests

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* refactor: standardize all buttons to Button component, centralize color tokens

- Convert all remaining raw <button> elements to <Button> component
  across AgentLabels, DebugView, SettingsModal, VersionIndicator,
  ZoomControls, ToolOverlay, and App
- Add icon size variant for square zoom buttons
- Unify all close/dismiss buttons to ghost variant with hover:text-danger
- Move all inline VS Code theme color references (vscode-charts-*,
  vscode-editor-background, etc.) to centralized :root tokens
  (status-permission, status-active, status-success, status-error)
- Remove redundant editor-bg, foreground, selection-bg, widget-border
  tokens in favor of existing bg, text, active-bg, border tokens
- Convert AgentLabels.tsx to Tailwind (was missed in initial migration)

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* refactor: replace hardcoded colors with tokens, rename FloorColor to ColorValue, skip permissions hover menu

- Replace text-[#999] with text-text-muted, rgba accent with bg-accent/accent-accent
- Create shared ui/types.ts with ColorValue, removing office/ dependency from UI
- Rename FloorColor → ColorValue across all files (21 files)
- Move tailwindcss and @tailwindcss/vite to devDependencies
- Fix inverted text scale: text-2xs (16px) < text-xs (18px) per convention
- Refactor agent button skip-permissions to hover menu, clean up removed CSS token refs

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* fix: standardize z-index layers across all UI components

Arrange z-order in ascending layers: agent labels (z-5), toolbars and
controls (z-10), version indicator popups (z-15), debug view (z-40),
modals (z-50+). Lift SettingsModal out of BottomToolbar's stacking
context into App.tsx. Extract EditActionBar and MigrationNotice into
own component files.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* fix: multi-root workspace folder picker and reorganize App.tsx overlays

Fix workspace folder picker for multi-root workspaces. Simplify hover
logic to prevent menu conflicts between bypass and folder menus. Also:
remove unused AgentLabels component, move inline pulse keyframes to
index.css as shared .pixel-pulse class, restructure App.tsx to group
debug/non-debug UI with ternary, and fix z-index layering.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

---------

Co-authored-by: Pablo De Lucca <pablo@Pablos-Mac-mini.local>
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com> — data não informada\n  - `d2cf76c5adea002710848165f0be26238653ab69` — fix: prevent duplicate restores, fix tool status reconnect, and improve agent tool detection (#197)

Co-authored-by: mitre88 <mitre88@users.noreply.github.com>
Co-authored-by: noam971 <noam971@users.noreply.github.com> — data não informada\n  - `f1c0e4aca982a1bedbb2e56ecfcc18ba9314108c` — chore(deps): bump actions/cache from 4 to 5 (#192)

Bumps [actions/cache](https://github.com/actions/cache) from 4 to 5.
- [Release notes](https://github.com/actions/cache/releases)
- [Changelog](https://github.com/actions/cache/blob/main/RELEASES.md)
- [Commits](https://github.com/actions/cache/compare/v4...v5)

---
updated-dependencies:
- dependency-name: actions/cache
  dependency-version: '5'
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> — data não informada\n  - `b3666d5227e51c59ad1c2f612f5ced64aae4bc62` — chore(deps): bump schneegans/dynamic-badges-action from 1.7.0 to 1.8.0 (#191)

Bumps [schneegans/dynamic-badges-action](https://github.com/schneegans/dynamic-badges-action) from 1.7.0 to 1.8.0.
- [Release notes](https://github.com/schneegans/dynamic-badges-action/releases)
- [Changelog](https://github.com/Schneegans/dynamic-badges-action/blob/master/changelog.md)
- [Commits](https://github.com/schneegans/dynamic-badges-action/compare/v1.7.0...v1.8.0)

---
updated-dependencies:
- dependency-name: schneegans/dynamic-badges-action
  dependency-version: 1.8.0
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> — data não informada\n  - `5c443ca8c7395671e9f935906002c8fc7ab1bf22` — ci: add GitHub Releases download count to badge stats (#190) — data não informada\n  - `0e61c4f060b007be253f0586f9577b955516c1d2` — feat: detect agents across all workspace folders in multi-root workspaces (#102)

* feat: support multi-root workspace agent scanning

In multi-root workspaces, Claude Code sessions started in different
workspace folders write their JSONL transcripts to different project
directories (e.g. `-home-user-projectA/` vs `-home-user-projectB/`).
Currently only the first workspace folder's project dir is scanned,
making agents in other folders invisible.

Changes:
- ensureProjectScan now tracks all registered project dirs in a
  module-level Set and scans all of them in the shared interval timer.
  Calling it multiple times with different dirs is safe — the seed
  logic always runs, but the timer is only started once.
- PixelAgentsViewProvider registers project dirs for all workspace
  folders (not just the first) when webviewReady fires.

This means in a multi-root workspace with folders [~/projectA, ~/projectB],
Claude agents started in either folder will be discovered and tracked.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* fix: add smart JSONL pre-registration and all-terminals scanning

Two fixes for multi-workspace scanning:

1. ensureProjectScan: Add smart pre-registration logic that skips
   files >3KB and modified within the last 10 minutes, so active
   JSONL files can still be picked up by terminal scanning.

2. scanForNewJsonlFiles: Iterate over all vscode.window.terminals
   instead of only vscode.window.activeTerminal, so agents in
   non-focused terminals are also discovered.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>

* feat: add global session scanning, multi-workspace support, and persist settings

---------

Co-authored-by: Shadow <cmdshadow@example.local>
Co-authored-by: Claude Opus 4.6 <noreply@anthropic.com>
Co-authored-by: Florin Timbuc <florin@sowild.design> — data não informada\n  - `51a08df2ee8d303d91581db498c0b00bf11156ae` — feat: add external session support and Agent tool recognition (#115)

* feat: add agent connection diagnostics, JSONL parser resilience, and path encoding fuzzy matching

* fix: simplify file watching to single poll, drop unreliable fs.watch/fs.watchFile

* feat: add external session support and Agent tool recognition

Detect and track Claude Code sessions running in the VS Code extension
panel (WebSocket transport, no terminal). These produce JSONL transcripts
like terminal sessions but have no associated Terminal object.

Changes:
- Make terminalRef optional, add isExternal flag to AgentState
- Add external session scanning (5s interval) and stale cleanup (5min timeout)
- Persist/restore external agents across reloads
- Guard terminal-specific code paths (focus, close, /clear reassignment)
- Recognize renamed 'Agent' tool alongside 'Task' for sub-agents

Known limitation: external sessions rely on JSONL file mtime for stale
detection (no close event available), so agents linger up to 5 minutes
after the extension panel session ends.

Supersedes #76 and #77.

* fix: improve external session lifecycle and /clear safety

---------

Co-authored-by: Florin Timbuc <florin@sowild.design> — data não informada\n  - `e22e1249b2b49c59e8eec113b70ecaa487c516a8` — feat: v1.2.0 release — changelog modal, version indicator, and release notes (#186)

Add in-app changelog modal with version indicator that highlights new updates.
Bump version to 1.2.0 and add comprehensive release notes covering external
asset packs, bypass permissions, improved seating, diagnostics, and more.

Co-authored-by: Pablo De Lucca <pablo@Pablos-Mac-mini.local>
Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com> — data não informada\n  - `b717efb1aa35689ee0f80bc37c96c2e56ea7ccb9` — feat: add agent connection diagnostics, JSONL parser resilience (#183)

* feat: add agent connection diagnostics, JSONL parser resilience, and path encoding fuzzy matching

* fix: simplify file watching to single poll, drop unreliable fs.watch/fs.watchFile

* docs: add rebase check to PR template

* docs: add Debug View guidance to bug report template

* fix: patch VS Code product.json to bypass Updating in progress in e2e tests — data não informada\n  - `28f7f0a9aa1982d51aa236fb6f1c59c24ec1f0f5` — fix: agents not appearing on Linux Mint (and likely macOS) when no folder is open (#70)

* fix: support Linux/macOS when no workspace folder is open

When VS Code is launched without a folder (e.g. bare `code` command,
common on Linux and macOS), `workspaceFolders` is empty and
`getProjectDirPath()` returned null. This caused `launchNewTerminal()`
to bail out early before sending `agentCreated` to the webview, so no
character ever appeared despite the terminal being created.

Fix: fall back to `os.homedir()` in both `getProjectDirPath` and the
`cwd` used for terminal creation. This matches the directory Claude Code
itself uses when started with no explicit working directory, ensuring the
extension correctly locates the JSONL transcript files.

Windows behavior is unchanged: workspaceFolders is always populated in
the common Windows workflow, so the fallback is never reached there.

Co-Authored-By: Logan <d4rkd0s@github.com>

* docs: update README for Linux/macOS platform support

- Add platform support note to Requirements section
- Replace "Windows-only testing" known limitation with a
  helpful tip for Linux/macOS users launching VS Code
  without a workspace folder open

Co-Authored-By: Logan <d4rkd0s@github.com>

* fix: remove dead code after getProjectDirPath home directory fallback

* ci: add type-check to pre-commit and full build to pre-push hooks

---------

Co-authored-by: Logan <d4rkd0s@github.com>
Co-authored-by: Florin Timbuc <florin@sowild.design> — data não informada\n  - `1689f7c008f7f5e99388519cc34d649623c134c0` — feat: improve seating, sub-agent spawning, and background agent support (#180)

* feat: prioritize PC-facing seats when spawning agents

Agents now prefer seats facing electronics (PCs, monitors) over other
seats like couches or benches. Selection is randomized within each tier:
PC seats first, then other seats, then random walkable tiles.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* fix: skip background tile rows when creating seats from chairs

Chairs with backgroundTiles (e.g. tall backrests) were producing seats
on their background rows, allowing agents to spawn on the backrest.
Also fixes back-facing chair z-sorting to use the bottom footprint row
so the chair back renders in front of the character even with bg tiles.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

* feat: improve sub-agent spawning and support background agents

Sub-agents now spawn on the closest walkable tile to their parent
(avoiding furniture and other characters) instead of claiming seats.
They also face the same direction as the parent agent.

Background agents (run_in_background: true) now stay alive until their
queue-operation completion record arrives, instead of being removed
immediately when the "Async agent launched" tool_result comes back.

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>

---------

Co-authored-by: Claude Opus 4.6 (1M context) <noreply@anthropic.com> — data não informada\n  - `19408ec9fede0b52e6cb16f750b03d45ee9a8077` — feat: playwright e2e tests for vscode extension (#161)

* feat: add Playwright e2e infrastructure for VS Code extension testing

Adds a complete end-to-end test setup using Playwright's Electron API to
validate the Pixel Agents extension inside a real VS Code instance.

- e2e/playwright.config.ts     — config with video, trace, 1-worker isolation
- e2e/global-setup.ts          — downloads VS Code via @vscode/test-electron
- e2e/helpers/launch.ts        — launches VS Code with isolated HOME + mock PATH
- e2e/helpers/webview.ts       — waits for the webview frame, clicks + Agent
- e2e/fixtures/mock-claude     — deterministic claude shim: creates JSONL file,
                                  logs invocation; no real Claude CLI required
- e2e/tests/agent-spawn.spec.ts — first spec: click + Agent → assert mock called,
                                  JSONL session file created, terminal tab visible
- e2e/tsconfig.json            — strict TypeScript config for test code

NPM scripts added: e2e (xvfb-run headless), e2e:headed, e2e:debug
CONTRIBUTING.md updated with running instructions, artifact paths, mock docs
test-results/ and playwright-report/ added to .gitignore

Test passes locally in 25 s; video recording confirmed at
test-results/e2e/videos/<test-name>/*.webm

Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>

* feat: revert this commit later, for now we will include video report in artifact

* test: enlarge panel for e2e webview

* feat: enable tests in pipeline

* feat: add debugging help for e2e test

* ci: install Playwright with deps and chromium

* revert: add debugging help for e2e test

This reverts commit 52096c0fe3d6e5aad2a4bc6c3c256b403985c587.

* fix: cross-platform e2e fixes for Playwright tests on macOS

* fix: Windows e2e support, add mock-claude.cmd

* feat: enable matrix CI run

* fix: resolve e2e failures across CI platforms

* fix: prevent Windows CI installs from failing

* fix: e2e:headed broke

* revert: fix: e2e:headed broke

This reverts commit bcffe69ba73061556d53802ac1f9f61fc0782717.

* chore: dropping support for headed

* docs: dropped support for headed

* fix: using cached vscode-test

* fix: wrong path for cache

* feat: restore and cache .vscode-test. First run will always say cache not found

* fix: poisoned cache, retrying with new

* feat: caching playwright as well

* fix: flaky test step in macos ci

* fix: e2e dynamic VS Code cache key, keychain cleanup

* fix: e2e avoid stale row selection

* fix: e2e macos display palette

* ci: skip PR title check for Dependabot, restrict badge updates to main repo

* ci: skip PR title check for Dependabot, restrict badge updates to main repo

---------

Co-authored-by: Claude Sonnet 4.6 <noreply@anthropic.com>
Co-authored-by: Florin Timbuc <florin@sowild.design> — data não informada\n  - `07898b71ddd8ab5846fb9ba0dc1a6098c09ca44a` — ci: skip PR title check for Dependabot, restrict badge updates to main repo (#181) — data não informada
\n## 60. William-kelvem94/postifolio-will

- **Registros retornados:** 2
- **Amostra:**
  - `549cfb151c8f415fafb93e165fd90edcb037a57a` — Create README.md — data não informada\n  - `4b74be1bd9b07deb399f039a50a963579fa4dffb` — Initial commit — data não informada
\n## 61. William-kelvem94/PROJECT_JARVIS_3.0

- **Registros retornados:** 13
- **Amostra:**
  - `9cda33a6b24e6a78c2cb5b570e6de3b75620932f` — Remove LocalJarvis and add new Jarvis 3.0 local AI setup

Deleted the entire LocalJarvis directory, including all source code, configuration, plugins, tests, and documentation. Added new documentation, configuration files, core modules, web assets, Docker setup, and scripts for a restructured Jarvis 3.0 local AI environment with support for multiple personalities, web and API interfaces, and improved modularity. — data não informada\n  - `e0b6cfe29a414e477f42144e7942a5f2f2e5cef9` — Versão Beta 2.0

interface ok
backend ok
falta treinar IA
organizar pequenos detalhes na interface
falta confirmar integração com alexa
configurar OCR ou qualquer configuração para a visão funcionar 100% — data não informada\n  - `f164333c86ca4a568cfba600f7de7713aa75a49c` — ATUALIZAÇÃO FUNCIONAL

INTERFACE OK
RESPOSTA DA IA NO OK
INICIANDO EM LOCALHOST:5000 OK — data não informada\n  - `af6aecaf862cb86d090a6793aadcd6faf80ba2e4` — ATUALIZAÇÃO FUNCIONAL

Tela inicial funcionando, interface montada em localhost:5000
projeto aparentemente inicial
falta corrigir a resposta da IA e organizar alguns pontos de estetica simples — data não informada\n  - `9e4c7ca5c91627103b8a40fc23723dedc2122f5c` — Atualização dnv

tentativa de melhorias na interface e etc — data não informada\n  - `eaed81aa02cee8f8e93b0ba37db01771f3ddf711` — Atualização de novo

tentativa de fazer rodar, melhorias nos serviços, melhorias no docker e interface — data não informada\n  - `72c9966de61fe738cbdefacc5e9487e7c388e9b0` — atualização

melhorias nos testes, no uso e desempenho do jarvis — data não informada\n  - `9587834ef2a78b915bbeead16afd8c885ff3dedc` — Mais atualização — data não informada\n  - `91451d531a26bd16fc6a394bbe663379897b697c` — atualização — data não informada\n  - `1dbcc0b137ac54662e71a46bf790da4aafd6b372` — Atualização — data não informada\n  - `f6dc859b559fdc4f5779b844e8fe3a51fe648eae` — Atualizações

Melhorias em docker-composer, dockerfile, requirements.txt — data não informada\n  - `7fe35aedab509b119ad40bc0e6022390a2684c58` — Atualização

Estou subindo esse projeto em um novo repositorio pois os repositorios antigos bugaram e eu não conseguia subir pro git — data não informada\n  - `0e7b7e1e910b680218f2b4802a1ad2b83bd665dc` — Initial commit — data não informada
\n## 62. William-kelvem94/PROJECT_JARVIS_5.0

- **Registros retornados:** 100
- **Amostra:**
  - `eb91b9f710072982298f75036cb1798067e8cf6f` — Add installation log (2026-08-09)

Add the JARVIS installer log produced on 2026-08-09. The file records hardware detection, Python/.venv validation, Ollama runtime and models installed (llama3.2:3b, qwen2.5vl:3b), autostart and native service setup, diagnostics (native service not-installed, low free RAM warning), and final installation success. Useful for reproducing or debugging the install process. — data não informada\n  - `1794c040a2093ff21447c1d3ca8d86dcd19eb061` — fix(book2): require validated install state before fast GUI launch — data não informada\n  - `7e5fc8ff642389b0870a2301c5dea9536603fb7c` — fix(book2): preserve self-healing installer launcher semantics — data não informada\n  - `4a334dc5ab9ee1aa99b4401d750e47165b8fae82` — fix(book2): make setup fallback batch-safe and preserve status — data não informada\n  - `6a77c9f6a4b1bf7741dd96fedbd256bf7c649969` — fix(book2): preserve launcher exit codes outside batch blocks — data não informada\n  - `774c59deec5041818b24f8d7968bd06f6ba63056` — fix(book2): make smart launcher fast and self-healing — data não informada\n  - `aec57c6c802a1bd92f449c05819a5526ea76c434` — fix(book2): harden runtime launcher and align profile environment — data não informada\n  - `3851e3b6a8af66329c4b58666f71ff2c7ee58349` — fix(book2): harden configuration launcher and preserve exit code — data não informada\n  - `2e9b51a7d109a1d6099b769c914b8fdb7e1b88ca` — fix(book2): make interface launcher use fast startup path — data não informada\n  - `b6863cfb87b88a00a365bf7b14facf902bc5fe10` — Add installer logs for 2026-08-09

Add two JARVIS installer logs to data/setup capturing installation runs on 2026-08-09. install-20260809-132746.log records a failed Operator browser step (Task was destroyed but it is pending), while install-20260809-133216.log records a successful installation (Playwright/Chromium, Ollama models, autostart and diagnostics). These logs provide troubleshooting context for the installer runs and environment detection. — data não informada\n  - `af89de0ee12c3de762e528a0304ff29976200c55` — fix(installer): resolve PowerShell ErrorActionPreference stderr error trap during Playwright chromium setup — data não informada\n  - `d3f3d865d2bc3a9767ed6050605854a97fbb5e70` — Refina interface futurista do JARVIS

Reproduz o painel visual de referência com núcleo oficial otimizado, composição responsiva, cards operacionais, composer amplo e navegação simplificada. Mantém Operator acessível por Presença, atualiza o build React e preserva todas as funções existentes. — data não informada\n  - `253ca338b8505088b6ccd46b2eb67a5e68211dc4` — Implementa plataforma Operator completa e controlada

Adiciona automação Windows por UI Automation, navegador autenticado com perfil persistente, memória cifrada entre dois PCs, atualização GitHub somente fast-forward, visão contínua opt-in, tarefas longas duráveis, serviço nativo não interativo, parada de emergência, aplicativos personalizados, interface Operator e instaladores inteligentes. Inclui segurança local, documentação, build React e 131 testes. — data não informada\n  - `16677621ea0bae0e8934592a0f4dd98b69ae74ed` — Corrige pipeline de voz e valida escuta ponta a ponta

Elimina a disputa de microfone entre bandeja e GUI, mantém um único ouvinte persistente, trata silêncio como condição normal, melhora wake word e texto falado, valida síntese Piper real e adiciona teste físico microfone → Whisper → TTS na interface e na CLI. Atualiza instalador, documentação, build React e cobertura automatizada. — data não informada\n  - `3316dc5eff7f915b0d1c1dd97da04525dc34afef` — Adiciona corpo digital controlado ao JARVIS

Implementa wake word persistente opt-in, catálogo seguro de aplicativos, câmera e tela sob confirmação, Microsoft UI Automation com verificação, novos controles na interface moderna, instalador atualizado, testes e documentação. — data não informada\n  - `e06d645465d04e3fc288a7402c597c4bb8077d36` — Add JARVIS installation log from 2026-08-07

Installation log documenting successful setup of JARVIS on book2-360 profile, including Python dependencies, Ollama server, hardware inventory, and operational diagnostics. — data não informada\n  - `79c27e2faaf11b15d56195c8e6ebcfe7a765858a` — Moderniza interface e recupera Ollama

Substitui a central Tkinter por uma experiência React/WebView2 moderna, conecta todos os painéis ao núcleo Python, adiciona recuperação e autoteste do Ollama, endurece o instalador nos dois PCs e cobre o fluxo com 101 testes. — data não informada\n  - `356d5852a91f230ead6c203225a3a660a523a7d3` — Adiciona instaladores inteligentes para os dois PCs

Cria inicializadores de clique único para Book2 360 e desktop, bootstrap seguro via WinGet, reparo idempotente, detecção automática de perfil, instalação de voz e Ollama, diagnóstico, logs, atalhos, visão opcional, testes e documentação. — data não informada\n  - `1395f901d46c17233c85887aa5126a819eb4f513` — Implementa consciência operacional persistente

Adiciona Event Store SQLite, presença segura no Windows, modelo do mundo, atenção proativa, memória versionada, planos verificados, pesquisa protegida, UI Automation somente leitura, bandeja, diagnósticos, testes e documentação. — data não informada\n  - `8ae14d1d8d10fbb3054fbfa61ab101d1753940cb` — Adiciona central pessoal com agenda, Gmail, notícias e digest

Integra GUI Tkinter, iCal, Gmail somente leitura, triagem local em lote, Google News, Open-Meteo, Morning Digest, comandos de voz, caches cifrados por DPAPI, testes e documentação. — data não informada
\n## 63. William-kelvem94/PROJECT-JARVIS

- **Registros retornados:** 4
- **Amostra:**
  - `d405cb45e1403b5421000ef4696b786d6ae373e4` — atualização

teste — data não informada\n  - `283fce07e98d89f52660ff111bbccfe9125a526b` — Resolvendo conflitos e unificando históricos — data não informada\n  - `57c3594debfc3facd2df2cfddf8ca0bf22ab4bd2` — Initial commit — data não informada\n  - `c6a349e48e1c56947d60370d116663c12201b9c9` — Commit inicial — data não informada
\n## 64. William-kelvem94/rentai-manager

- **Registros retornados:** 5
- **Amostra:**
  - `d11b6bddd10bdc52c1af296e5ec73086d46f6522` — Add mock auth and header+CRUD

Implement visual mock authentication, header with search/notifications, theme toggle, and property CRUD form with Zod validation. Integrates mock auth context, theme context, protected routes, header layout, and property management components ready for backend integration.

X-Lovable-Edit-ID: edt-5c5cc7ab-fa67-4267-a85f-538aef74f105 — data não informada\n  - `e22429757926ee9de3e86cc46f5a2a94233d72e0` — Changes — data não informada\n  - `a883b5536385c81fbdc6d84d27296295c17c4eee` — Add rental frontend scaffold

Implements a comprehensive rental management frontend scaffold including:
- Dashboard with metrics cards and charts
- Property, tenant, and payments data models and mock data
- UI components: Sidebar, MainLayout, Button, Badge, and various dashboard widgets
- Pages for Dashboard, Properties, Tenants, Payments, Chat AI, and Settings (partial)
- AI chat integration with simulated responses and quick-actions
- Type definitions and data mocks for rapid UI iteration

X-Lovable-Edit-ID: edt-391542d9-d985-46d7-930f-56b0db109df8 — data não informada\n  - `560b9ce02681125939021688d53a377c5245afc6` — Changes — data não informada\n  - `978b4595134c013e11c3a333d13b0639600b20ca` — Initial commit from template vite_react_shadcn_ts_20250728_minor — data não informada
\n## 65. William-kelvem94/ruflo

- **Registros retornados:** 100
- **Amostra:**
  - `4cbcfc2671ad3f13ac9a648c1604c09fdb934248` — chore(release): bump claude-flow / @claude-flow/cli / ruflo to 3.10.45

Patch release shipping a single fix landed since 3.10.44:

- #2301 (e7b9eea9f) — hive-mind --dangerously-skip-permissions: complete
  the kebab→camel parser-normalization fix by adding the yargs-style
  negation deny clause (autoPermissions === false). Without this, the
  prior commit's activation half worked but --no-auto-permissions could
  no longer block, leaving the spawn strictly more permissive than the
  pre-fix state. 9/9 regression tests pass — 3 new cases pin the parser
  negation contract. Co-authored with @JOhnsonKC201 (original PR) and
  @rvrheenen (issue reporter who supplied the original patch). Closes #2269.

Published to npm with latest + alpha + v3alpha tags for all three
packages. 9/9 dist-tag combinations verified at 3.10.45.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `50bc51643bb791bb24302ca0129be997b8378395` — fix(cli): #2269 honor --dangerously-skip-permissions in hive-mind spawn (#2301)

* fix(cli): #2269 honor --dangerously-skip-permissions in hive-mind spawn

The arg parser (parser.ts normalizeKey) converts kebab-case to camelCase
and stores ONLY the normalized key, so `flags['dangerously-skip-permissions']`
is always undefined and `=== true` always evaluates false. The flag was
silently dropped: headless `hive-mind spawn --claude --non-interactive
--dangerously-skip-permissions` ran in permissionMode "default", so every
Edit/Write was auto-denied (no TTY to approve) and the agent finished
having changed nothing.

Fix mirrors the dual-key fallback used a few lines above for
`isNonInteractive` (`flags['non-interactive'] || flags.nonInteractive`).
This also honors the documented `default: true` for the option declaration
(line 590), since the parser populates the camelCase key with the default.

Repro from the issue:
  npx @claude-flow/cli hive-mind spawn --claude --non-interactive \
    --dangerously-skip-permissions -o "edit any file in this repo"

Before: init event shows `"permissionMode":"default"`, Edit calls land
in permission_denials, files unchanged.
After:  `--dangerously-skip-permissions` is appended to claudeArgs,
spawned `claude` runs in `bypassPermissions`, edits succeed.

Fixes #2269

Co-Authored-By: RuFlo <ruv@ruv.net>

* test(cli): #2269 regression test for hive-mind --dangerously-skip-permissions

Pins down two invariants together:
1. The parser stores ONLY the camelCase form of --dangerously-skip-permissions
   (this is the parser behavior that caused the original drop).
2. The skipPermissions predicate from hive-mind.ts evaluates true when the
   parser-produced flags shape is passed through it.

Also exercises the --no-auto-permissions opt-out and the legacy
hand-constructed-flag-map paths, so a future refactor of either the
parser's normalizeKey or the hive-mind action can't silently regress
the flag-drop bug.

The predicate is kept inline rather than imported, because the hive-mind
spawn action does real side effects (childSpawn) at module load and isn't
trivially importable for a pure unit test. The predicate's source of
truth (hive-mind.ts) and the test mirror are both annotated with #2269.

Co-Authored-By: RuFlo <ruv@ruv.net>

* fix(hive-mind): handle yargs-style negation for --no-auto-permissions

The original PR (#2301) correctly diagnosed the kebab→camel parser
normalization that made the activation half of the
--dangerously-skip-permissions flag silently no-op. The deny half had
the same shape of bug but the patch only widened it to kebab|camel —
neither of which is what the parser actually produces for
--no-auto-permissions.

The parser stores yargs-style negation:

  --no-auto-permissions → { autoPermissions: false }

NOT { 'no-auto-permissions': true } or { noAutoPermissions: true }.

So after the original fix, --dangerously-skip-permissions
--no-auto-permissions would have skipped permissions anyway — strictly
more permissive than the pre-fix state, where activation never fired at
all. Caught by running hive-mind-skip-permissions.test.ts case "skip
permissions=false when --no-auto-permissions is also passed", which
went red.

This commit adds the third deny clause (`flags.autoPermissions === false`)
and pins the parser contract with three new tests:
- parser produces autoPermissions:false for --no-auto-permissions
- predicate denies when only the yargs-style negation key is set
- predicate ignores autoPermissions:true (not a deny signal)

Tests: 9/9 pass. Closes #2269.

Co-Authored-By: JOhnsonKC201 <johnsonkc201@users.noreply.github.com>
Co-Authored-By: rvrheenen <rvrheenen@users.noreply.github.com>
Co-Authored-By: RuFlo <ruv@ruv.net>

---------

Co-authored-by: RuFlo <ruv@ruv.net>
Co-authored-by: JOhnsonKC201 <johnsonkc201@users.noreply.github.com>
Co-authored-by: rvrheenen <rvrheenen@users.noreply.github.com> — data não informada\n  - `6ec7268f4506b2a23104651816099a7665fea193` — chore(release): bump claude-flow / @claude-flow/cli / ruflo to 3.10.44

Patch release bundling two fixes landed since 3.10.43:

- #2348 (7c6362633) — break embedder-rescue mutual recursion that OOM'd
  v3-ci.yml at the V8 heap limit. memory-bridge's rescueAgentdbEmbedder
  now delegates to generateLocalEmbedding (bridge-free leaf), not
  generateEmbedding (bridge-first). Closes #2312. CI gate re-enabled.
- #2366 (a21f6808f) — Windows plugin install/uninstall/upgrade. npm on
  Windows is a bash shim with no .exe (spawn ENOENT) and Node refuses
  to spawn .cmd directly post-CVE-2024-27980 (spawn EINVAL). Routes
  through cmd.exe /d /s /c npm <args> on Windows; POSIX unchanged.
  Validated via the existing validatePackageName regex gate and Node's
  array-form argument quoting. (community PR by @danielsOink.)

Held from this batch:
- #2301 (hive-mind --dangerously-skip-permissions) — passing 5/6 but the
  --no-auto-permissions deny case fails because the parser uses yargs-
  style negation (autoPermissions: false), which the predicate doesn't
  read. Comment posted with proposed fix.

Published to npm with latest + alpha + v3alpha tags for all three
packages. 9/9 dist-tag combinations verified at 3.10.44.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `a21f6808fb9bce2ffd56a859f281c23306d1eb85` — fix(plugins): make npm install/uninstall/upgrade work on Windows (#2366)

`PluginManager` spawned `npm` via `execFile` without a shell. On Windows
that hits two separate Node failure modes:

  1. `npm` is a bash shim (no `.exe`), so `spawn('npm', ...)` resolves to
     a file Node cannot launch and fails with `spawn npm ENOENT`.
  2. Falling back to `npm.cmd` runs into CVE-2024-27980 (Node
     18.20.2 / 20.12.2): the runtime refuses to spawn `.cmd`/`.bat`
     files directly and throws `spawn EINVAL`.

Route all three call sites (install / uninstall / upgrade) through a
single `runNpm` helper that invokes `cmd.exe /d /s /c npm <args>` on
Windows. `cmd.exe` is a real `.exe`, so neither failure mode applies,
and Node's safe array-form argument escaping is preserved.

Verified locally on Windows 11 / Node 20:
  ruflo plugins install -n @claude-flow/security
  -> Installed @claude-flow/security@3.0.0-alpha.10

Co-authored-by: RuFlo <ruv@ruv.net> — data não informada\n  - `7c6362633edbe1e68a84b9ff76418e6473fb0660` — fix(memory): #2312 — break embedder-rescue recursion that OOM'd CI at 4GB (#2348)

Root cause (found by container bisection, not the suspected SONA/EWC chain):
memory-bridge's rescueAgentdbEmbedder (#2256-followup) monkey-patches
agentdb.embedder.embed to delegate to memory-initializer's generateEmbedding.
But generateEmbedding is bridge-FIRST — it calls bridgeGenerateEmbedding,
which calls registry.getAgentDB().embedder.embed — the patched function:

  generateEmbedding → bridgeGenerateEmbedding → embedder.embed (patched)
    → generateEmbedding → … unbounded async cycle

Microtask-driven, so no stack overflow — just monotonic heap growth to the
V8 limit (4050MB on the CI runner, SIGABRT 134, ~35s). The cycle only arms
when @xenova/transformers fails to init (pipeline=null → rescue applies),
which is why Linux CI died while Windows/macOS dev boxes never reproduced.
TEST 1 passed because the cycle needs the bridge registry initialized first
(post-task's bridgeRecordFeedback does that), which is also why the earlier
CLAUDE_FLOW_SKIP_RUVLLM_TRAJECTORY bypass had no effect — the allocator was
never in the ruvllm/SONA/EWC chain at all (bisection shows them flat at
122MB).

Fix:
- memory-initializer: extract generateLocalEmbedding (transformers/ruvector/
  hash chain, never the bridge). generateEmbedding now delegates to it after
  the bridge attempt — behavior unchanged for normal callers.
- memory-bridge rescue: delegate to generateLocalEmbedding (bridge-free
  leaf). If the import doesn't expose it (stale pairing), decline the rescue
  — fail safe, never recurse.
- Probe hardening: the old probe accepted any non-zero vector, which the
  deterministic hash fallback also satisfies — so it "rescued" agentdb's
  mock with our own mock. Now requires backend === 'onnx'. When declining
  because the local chain is also degraded, tag embedder.backend='mock' so
  bridgeGenerateEmbedding's AUDIT-#3 check stops labeling mock vectors as
  onnx.
- v3-ci.yml: drop continue-on-error from the graph-trajectory smoke — it
  gates again. Verified in a node:22-bookworm container (CI-equivalent
  fresh install + build): 10/10 pass at DEFAULT heap and at 512MB, cold and
  warm model cache. Pre-fix repro in the same container OOM'd in ~36s.
- smoke script: use pathToFileURL for dist imports so it runs on Windows
  (ERR_UNSUPPORTED_ESM_URL_SCHEME) — needed for local debugging of this.

Fixes #2312 — data não informada\n  - `53cab89de8075183c5be4ce5f6f4052dac259093` — chore(release): bump claude-flow / @claude-flow/cli / ruflo to 3.10.43

Patch release bundling four bug fixes that landed on main since 3.10.42:

- #2358 (b12788777) — agent_execute now omits temperature/top_p/top_k for
  Fable 5 / Opus 4.8 / Opus 4.7, which 400 the request if sampling
  params are sent (#2357 Finding A, HIGH; invisible on Claude-Max,
  fatal on raw ANTHROPIC_API_KEY)
- #2365 (99bd9db59) — OpenRouter fallback model + haiku/sonnet/opus
  aliases refreshed from the Oct-2025 retired claude-3.5-* / claude-3-
  opus slugs to the current 4.x family (#2357 Finding C)
- #2361 (a553da343) — daemon self-terminating TTL + idle shutdown,
  global status --all, honest HNSW/init footguns (community PR by
  @shaal, addresses @pacphi's multi-day immortal-daemon token-leak
  investigation; #2360)
- #2364 (d687753cc) — federation plugin caps agentic-flow peer to
  <2.0.13, which dropped the ./transport/loader subpath upstream

Published to npm with latest + alpha + v3alpha tags for all three
packages. 9/9 dist-tag combinations verified at 3.10.43.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `99bd9db590793382d23a83ce3e70c8ebabcbc2ae` — fix(agent-execute): refresh retired OpenRouter Claude slugs (#2357 Finding C) (#2365)

The OpenAI-compat path (used for OPENROUTER_API_KEY callers) still
referenced the Oct-2025 retired model IDs:

- defaultModel: anthropic/claude-3.5-sonnet    → anthropic/claude-sonnet-4-6
- haiku alias:  anthropic/claude-3.5-haiku     → anthropic/claude-haiku-4-5
- sonnet alias: anthropic/claude-3.5-sonnet    → anthropic/claude-sonnet-4-6
- opus alias:   anthropic/claude-3-opus        → anthropic/claude-opus-4-8

Aligns with MODEL_MAP (the canonical Anthropic resolution table).
OPENROUTER_DEFAULT_MODEL still wins for callers who want to pin a
different slug.

Companion fix to PR #2358 (Finding A, merged in b12788777). Together
the two cover the entire current frontier family across both the
Anthropic native path and the OpenRouter vendored path.

Refs #2357. — data não informada\n  - `b12788777a64bbabeb0043b5c5e77917c661b1c6` — fix(agent-execute): omit removed sampling params for Fable 5 / Opus 4.8 / Opus 4.7 (#2357) (#2358)

callAnthropicMessages always sent temperature (default 0.7), but the
adaptive-thinking family (claude-fable-5, claude-opus-4-8,
claude-opus-4-7) removed temperature/top_p/top_k — the Anthropic API
returns 400 "Extra inputs are not permitted", so agent_execute /
workflow_run / the WASM-agent Anthropic path could not call any
current frontier model when an ANTHROPIC_API_KEY was set.

Gate the param on a new exported modelRejectsSamplingParams() predicate
(prefix-matched so dated snapshots are covered). Behavior for models
that still accept sampling params (sonnet / haiku / opus <= 4.6) is
unchanged, including the 0.7 default. The Ollama / OpenRouter
OpenAI-compat paths accept temperature and are untouched.

Vitest regression included (sampling-params-2357.test.ts), pinning
both the predicate and the request-body contract via a mocked fetch.

Part of #2357 (Finding A) — does not close the issue.

Co-authored-by: Mak Allen <mak@heroforge.ai>
Co-authored-by: ruflo <ruv@ruv.net> — data não informada\n  - `a553da34394371ddf4e895fee1c9262d86c71308` — fix(daemon): self-terminating TTL + idle shutdown, global status --all, honest HNSW/init footguns (#2361)

Carry-forward of the still-open, fixable-in-ruflo findings from
pacphi/ruflo-machine-ref (token-leak + honesty investigations). Most of
that kit's findings already landed upstream (#2219 SQLite, #2222 route
persistence, #2239 encoder collapse in 3.10.11); this addresses what
remained.

Daemon token-leak (root cause of multi-day background token burn):
- worker-daemon: self-terminating lifecycle. New ttlMs (default 24h) +
  idleShutdownMs (opt-in) config, sourced constructor > config.json
  (daemon.ttlSecs/idleSecs) > env (RUFLO_DAEMON_TTL_SECS/IDLE_SECS) >
  default. A monitor (unref'd, 60s) grace-shuts-down via stop()+exit(0),
  mirroring the signal path so the foreground ref'd keep-alive can't leave
  a zombie. An explicit 0 disables (preserves run-until-stopped).
- daemon command: --ttl flag (forwarded through the background fork) and
  TTL shown in the status/start boxes.
- daemon status --all: global view across every workspace via the same
  ps/tasklist scan used by kill-stale, reading each workspace's
  daemon-state.json for age + TTL and flagging daemons past their TTL/12h.
  Leaked daemons in other workspaces were previously invisible.

Honest status / init footguns:
- neural status: getHNSWStatus() now reports real capability
  (@ruvector/core resolvable) vs in-process load, ending the false
  "HNSW Not loaded" when the package is installed.
- init: keep auth-gated cloud MCP servers (ruv-swarm, flow-nexus) opt-in
  even under --full via a new --cloud-mcp flag (committed .mcp.json +
  per-session token cost).
- claudemd-generator: emit `ruflo@latest mcp start` (matches the actual
  generated .mcp.json) instead of legacy `@claude-flow/cli@latest`, and
  note the daemon's token cost + TTL.

Tests: TTL/idle precedence + 0-disable + monitor arming; the
extractWorkspaceFromDaemonLine helper behind --all; HNSW status contract
updated to assert initialized-vs-available separation.

Credit: investigation, reproductions, and statistical eval by
@pacphi (https://github.com/pacphi/ruflo-machine-ref). — data não informada\n  - `d687753cc2f10cc4c2ddd12e1804c07be7fda3ae` — fix(federation): cap agentic-flow peer to <2.0.13 (#2364)

agentic-flow@2.0.13 dropped the ./transport/loader subpath from its
exports map. The federation plugin imports
'agentic-flow/transport/loader' for loadQuicTransport, AgentMessage,
QuicTransportConfig, and WebSocketFallbackTransport. With 2.0.13
resolved, that subpath throws ERR_PACKAGE_PATH_NOT_EXPORTED.

Runtime impact is bounded — midstream-aware-loader.ts wraps the dynamic
import in try/catch and returns null on failure, so the plugin falls
back to the midstream-native path rather than crashing. But the peer
range previously said ">=2.0.12-fix.8" which silently accepted 2.0.13;
tighten to ">=2.0.12-fix.8 <2.0.13" so npm install warns about the
incompatibility instead of letting it surface as a runtime fallback.

Type imports continue to work because the devDependency is still pinned
to 2.0.12-fix.8 for typecheck.

This is the in-repo half of the fix. Upstream agentic-flow needs to
either restore ./transport/loader to its exports map (Option A in the
issue body) or publish migration notes for callers (Option B). The
peer cap will widen again once upstream resolves either way.

Closes #2364.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `d1e558b48e9187b0a65bacc6073cd4e009ce1d52` — docs(readme): propagate image removal to mirror READMEs

dfe1b9cf9 dropped the agentic-appliance and Summit hero images from the
root README but left the two mirror copies (npm wrapper + CLI package)
out of sync. Match them now.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `dfe1b9cf993c34571fa5f2d08f5772e0672c68ab` — docs(readme): remove agentic-appliance and Summit hero images

Drops two large hero images from the README header:
- RuFlo-agentic-appliance.png (cognitum.one/appliance)
- ruFlo-Summit.jpg (Budapest 2026 summit, #1967)

Badges and the main banner are retained.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `456b8e2a14ac06393ac4b91e151bfcf303424783` — revert: restore original README.md

Reverts the plain-language rewrite from 61b988e68 at the user's request.
Original README content restored from a88b9369b.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `61b988e68c2eb5e8b1b7941815dfbe6fa88dbee3` — docs(readme): rewrite root README in plain language

Replaces the 416-line marketing-heavy README with a 256-line plain-language
walkthrough aimed at a developer evaluating Ruflo for the first time:
- What it actually is (CLI + MCP server on top of Claude Code)
- What problem it solves (forgetting / single-threaded / one-model-fits-all)
- Three things you can use day-to-day
- Core concepts in one sentence each
- "When you should NOT use Ruflo" section
- File layout `init` writes, with reversal instructions
- FAQ on phone-home / data / uninstall

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `a88b9369bdec81278e68fde3c76271bb9814a99e` — chore(release): bump claude-flow / @claude-flow/cli / ruflo to 3.10.42

Patch release for #2346-style community bug batch (PR #2355).

- Fixes #2352 (Windows path validation + silent failure on hooks post-edit)
- Fixes #2351 (trajectory-end feedback never distilled into searchable pattern)
- Fixes #2350 (init hooks subcommand wrote no hooks block to settings.json)

Published to npm with latest + alpha + v3alpha tags for all three packages.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `0bb7c4e3d7f4eda29d58832322154f6348156c3a` — fix: community bug batch — Windows path validation (#2352), trajectory-end feedback (#2351), init hooks settings (#2350) (#2355)

Three reproducible bugs reported by @grym3s, batched in the style of #2346.

#2352 — hooks post-edit: Windows paths rejected, failure printed as [OK]
  - validatePath used the general SHELL_META set which includes `\`, so
    every absolute Windows path (E:\Repos\...) failed with "shell
    metacharacters". Claude Code hook events deliver absolute paths in
    tool_input.file_path, so all Windows users had silent learning loss.
    Path-specific PATH_SHELL_META drops `\` (still rejects ; & | ` $ etc.)
    and the sanitized output normalizes to forward slashes.
  - CLI post-edit action printed `Outcome recorded for ...` whenever the
    MCP call returned at all, ignoring `{success:false}`. Now checks
    result.success, surfaces the error, and exits non-zero.

#2351 — trajectory-end: step-less feedback never distilled
  - When `trajectory-end` is called with `feedback` but no recorded steps,
    the feedback was persisted with the trajectory but never embedded as a
    searchable pattern — patternsExtracted always reported 0 and
    pattern-search never surfaced it. Step-less trajectories are the
    common case for LLM agents. Now routes feedback through the same
    bridge.bridgeStorePattern / store-fallback path that pattern-store
    uses, with modest default confidence (0.6 success / 0.4 failure)
    since step-less feedback hasn't been validated by execution evidence.
    Best-effort: distillation failures do not fail the trajectory-end call.

#2350 — init hooks: subcommand writes no hooks block
  - settings-generator (#1744 fix) only emits the `hooks` block when
    `components.helpers` is true, because hooks point at the helper
    handler script. The `init hooks` subcommand was setting helpers:false,
    so the one subcommand whose purpose is "Initialize only hooks
    configuration" produced settings.json with no `hooks` key while
    reporting "N hooks enabled". Helpers must ship with hooks.

Tests
- v3/@claude-flow/cli/__tests__/validate-input-path-2352.test.ts (22 tests):
  pins Windows-path acceptance, POSIX-path acceptance, and rejection of
  shell metacharacters, traversal, empty/non-string/oversized input.
- All existing validate-input, init-wizard-bugs, hooks-intelligence, and
  hooks-post-task tests still pass. — data não informada\n  - `58716fd141b9c90b9b9a802bc089f2401da3d108` — chore: sync root package-lock.json to 3.10.41

The lockfile was stuck at "claude-flow@3.10.39" — older than the prior
v3.10.40 release. npm publish updated it during the v3.10.41 release.
Committing the synced version so future `npm ci` / `npm audit` calls
match the published package.json version.

No dependency changes — just the top-level `name`+`version` strings.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `6a2964ac94e10ca9916da030302686c725638adb` — chore(release): bump claude-flow / @claude-flow/cli / ruflo to 3.10.41

PATCH release covering three merged PRs since v3.10.40:

 - #2336 — feat(agents): ADR-147 nested subagent (depth=5) infra + P2 stage 1
 - #2340 — chore(security): Socket.dev alert baseline + remove broken pages.yml
 - #2346 — fix: community bug batch:
     • fix(session) atomic writes to current.json + self-heal (#2307, @BIWizzard)
     • fix(hive-mind) await spawned claude before returning (#2297, @clement-livdeo)
     • fix(statusline) resolve installed CLI bin + bump cache 10s→60s (#2337, @shaal)

No API breaks → PATCH per CLAUDE.md versioning policy.

Co-Authored-By: RuFlo <ruv@ruv.net> — data não informada\n  - `eaaf59d1bd938832478629a4bc038504fa621e21` — fix: community bug batch — session atomic writes (#2307), hive-mind await (#2297), statusline storm (#2337) (#2346)

* fix(session): atomic writes to current.json + corrupted-file self-heal (#2307)

Apply BIWizzard's diff from the issue verbatim. Same class as #1707 (metrics
partial-JSON corruption) and #1637 (daemon-state.json write-race) which were
both fixed elsewhere with atomic writes; session.js was missed in that sweep.

Changes:
  - Add atomicWrite(file, data) helper: writes to `${file}.tmp.${pid}` then
    rename()s into place. rename() is atomic on the same filesystem, so
    concurrent writers (session-restore, metric, daemon workers, teammates)
    can't interleave partial content.
  - Replace all 5 fs.writeFileSync calls on session files with atomicWrite.
  - In restore(): wrap JSON.parse in try/catch so existing corrupt session
    files self-heal — log the error and start a fresh session rather than
    throwing out of the hook.

Why this matters: per-fd offsets in writeFileSync mean writer B can overwrite
the first N bytes of writer A's payload but cannot shrink the file — A's tail
dangles past B's end, producing valid JSON + trailing garbage. session-restore
then throws on the bare JSON.parse.

Closes #2307.

Co-Authored-By: BIWizzard <noreply@github.com>
Co-Authored-By: RuFlo <ruv@ruv.net>

* fix(hive-mind): await spawned claude before returning (#2297)

Per clement-livdeo's root-cause: spawnClaudeCodeInstance() spawned the
`claude` child with stdio:'inherit', registered an exit handler for logging
only, then returned `{ success: true, promptFile }` immediately. The command
handler resolved, the CLI process finished, and the still-initializing
`claude` child lost its controlling terminal and was killed/orphaned.

The signature tell that confirms the diagnosis: a stray XTVERSION reply
("iTerm2 3.6.1064;1;2;4;6;17;18;21;22;52") leaked onto the next shell prompt
— the terminal queried for capabilities, but the child died before reading
the answer.

Also explains why the existing `claudeProcess.on('exit', ...)` log lines
("Claude Code completed successfully", "Claude Code exited with code N")
never printed — the parent was already gone.

Fix: await the child's exit (or error) before returning. The existing exit-
handler logging now works, and the non-interactive (-p / --non-interactive)
path completes only after Claude Code does.

Different cause from #1748 (which fixed an MCP-config issue where workers
exited because they lacked mcp__ruflo__* tools via --mcp-config).

Closes #2297.

Co-Authored-By: clement-livdeo <noreply@github.com>
Co-Authored-By: RuFlo <ruv@ruv.net>

* fix(statusline): resolve installed CLI bin + bump cache TTL 10s→60s (#2337)

Per shaal's report: the statusline helper ran
`npx --yes @claude-flow/cli@latest hooks statusline --json` on every
uncached render, cached only 10 s. Because of the `@latest` tag, npx
re-resolves the package from the registry and relaunches the entire
@claude-flow/cli on each call. Claude Code refreshes the statusline
several times a second while streaming, and with multiple concurrent
sessions this spawned a near-continuous storm of `npm exec` / node
processes:

  - load average 40-65 on a 12-core machine (~6 concurrent sessions)
  - each live `npm exec` process burned 55-90 % of a core
  - new PIDs every 1-2 s as the storm cycled

Raising the local cache TTL alone dropped the reporter's load from
~43 to ~2.3, confirming this delegation as the dominant source.

Fix (applied to BOTH the committed dogfood helper at
`.claude/helpers/statusline.cjs` AND the init generator template at
`v3/@claude-flow/cli/src/init/statusline-generator.ts` so existing
and future installs both benefit):

  1. New `resolveCliBin()` — mirrors getPkgVersion()'s install-location
     probing and returns the absolute path to a usable `bin/cli.js`
     (project / monorepo / plugin marketplace / global node_modules,
     incl. custom-prefix layouts like ~/.npm-global).

  2. `getStatuslineData()` now invokes the CLI directly via
     `process.execPath` + the resolved bin — no npx, no registry
     round-trip, no @latest re-resolve. Falls back to
     `npx --prefer-offline @claude-flow/cli` (no @latest) only when
     nothing is installed locally, so cold environments still work.

  3. `CACHE_TTL_MS` 10_000 → 60_000.

Closes #2337.

Co-Authored-By: shaal <noreply@github.com>
Co-Authored-By: RuFlo <ruv@ruv.net>

---------

Co-authored-by: BIWizzard <noreply@github.com> — data não informada\n  - `16a55f7a537c4a405e448e59859866eebbdd45a0` — chore(security): document Socket.dev alert baseline + remove broken pages.yml workflow (#2340)

Two coupled changes from triaging the Socket alerts on the published
claude-flow@3.10.40 (https://socket.dev/npm/package/claude-flow/alerts/3.10.40)
and the persistent Deploy Pages CI failure.

1) docs/security/socket-baseline.md — comprehensive triage:

   - What's protected today (root overrides for protobufjs/uuid/+25 others,
     supply-chain-audit CI job in v3-ci.yml line 629 already enforces
     npm audit + lockfile integrity + allowlist + typosquat + publisher
     trust).
   - What's NOT cleanly fixable: npm overrides only apply to the root of
     the dep tree. When claude-flow is a consumer's dep, our overrides are
     ignored, so a clean install of claude-flow@3.10.40 still pulls in the
     vulnerable protobufjs/uuid cascade through @xenova/transformers (no
     patched upstream version exists yet). Documented with the actual
     CVE chain and three concrete paths forward, all tracked in #2339.
   - Inherent flags: 13 alert categories (network/filesystem/env-var/shell
     access, install scripts, native code, etc.) that describe normal
     CLI/agent behaviour, not bugs. Documented one-by-one with the
     justification for each.
   - False positives: explicitly triages Socket's "did you mean z-schema?"
     suggestion against our zod dep (which is the 10M-weekly-download
     canonical schema library, not a typosquat), plus the AI-heuristic
     categories that are weak signals.
   - Operational policy: when to add overrides, when to update this doc,
     when to revisit.

2) Remove .github/workflows/pages.yml:

   - The workflow has FAILED on every single run since first appearing
     2026-05-30 (10+ consecutive failures, including the f5a180423 merge
     from earlier today).
   - Root cause: GitHub Pages is not enrolled on this repo
     (gh api repos/ruvnet/ruflo/pages returns HTTP 404). The workflow's
     actions/configure-pages@v4 step fails with "Get Pages site failed.
     Please verify that the repository has Pages enabled".
   - Nothing has ever been deployed from this workflow, so removing it
     loses no functionality. If Pages is wanted later, the proper sequence
     is: enable Pages in repo Settings → Security and analysis → Pages,
     then re-add a workflow with the right enablement/source config.
   - Without this removal, any push to main that touches docs/** (which
     this PR does) re-triggers the same failure, polluting CI status and
     specifically violating the "all build actions must pass" intent
     stated for this work.

Refs ruvnet/ruflo#2339 — data não informada
\n## 66. William-kelvem94/search_works

- **Registros retornados:** 6
- **Amostra:**
  - `a7aab58cdb44486373f38e4847b436ee7fa966c9` — organiza arquitetura e perfil local — data não informada\n  - `142457bd07fee197a3a5cd21c5e93c75b023361c` — fix: atualiza imagem do Playwright para v1.60.0 e remove .env do cache do Git

- Atualiza o Dockerfile para usar mcr.microsoft.com/playwright:v1.60.0-jammy corrigindo o erro de execucao dos navegadores.
- Remove .env do tracking do Git para seguranca de credenciais. — data não informada\n  - `4e019aa711302fd5b5831867d2742f768d90e5c2` — fix: rebaixa versao do pdf-parse para 1.1.1 para estabilidade no Node

- Corrige erro de execucao 'ReferenceError: DOMMatrix is not defined' causado pela versao 2.4.5 (que usa pdfjs-dist v5 com dependencias de browser/DOM). — data não informada\n  - `4bed9aa4954ff40547050ddd35c90ea40ee31413` — fix: remove o parametro response_format para provedores locais de IA

- Corrige erro HTTP 400 Bad Request ao chamar o LM Studio omitindo o response_format.
- Atualiza a URL padrao do local backend para host.docker.internal no .env para permitir conexao do container. — data não informada\n  - `e898e8dee8e1f010dd25de57c38e84dc6cf843fd` — refactor: implementa leitura dinamica de PDF de curriculo e adiciona ignore de arquivos locais

- Adicionado parser de PDF (pdf-parse) no src/aiClient.ts para extrair texto do curriculo configurado no .env em tempo de execucao.
- Criado arquivo .gitignore para evitar tracking de node_modules, dist, .env e .browser_session.
- Removidos arquivos compilados da pasta dist/ e lock files locais do tracking do Git.
- Atualizado o README.md com as novas instrucoes de configuracao e operacao do bot via Docker e Dashboard local. — data não informada\n  - `8185417737f2e00192996e905c14f8e1e4a0ae9e` — first commit — data não informada
\n## 67. William-kelvem94/slack-agent-template

- **Registros retornados:** 1
- **Amostra:**
  - `2fdc15357d47369453883f6f806567377f1d2c3e` — Initial commit

Created from https://vercel.com/new — data não informada
\n## 68. William-kelvem94/STUDY_LLMS

- **Registros retornados:** 19
- **Amostra:**
  - `7054774832841a4697a5865f81e68de4588de45f` — feat: add script to fix tokenizer and export model to GGUF format — data não informada\n  - `2b5ac826a85229e1581a4c9cc73ddca76973d4b0` — feat: add script to convert and quantize model to GGUF format using Unsloth — data não informada\n  - `eb83b928442d5273941d5afe89c13d2cb87d7192` — 🔥 Clean: Remoção definitiva de arquivos legados e pastas vazias (Estrutura WILL-JARVIS Consolidada) 🏗️ — data não informada\n  - `c67b2b928989d230eeb9abc76d6388ed183ec40c` — chore: Remoção de scripts e pastas isoladas da fase V1 para foco integral na documentação WILL-JARVIS — data não informada\n  - `313d14c9ef7ebf752dcba6c3cfe376f1fa8969d1` — docs: Cria base de conhecimento FAQ detalhando engenharia de VRAM, hacks e evolução de IAs — data não informada\n  - `9e7cc095bd3569f40dc55f375713564f25691528` — 📝 JARVIS: Atualização maciça do diário de bordo com as estratégias finais de VRAM e Sobrevivência 🛡 — data não informada\n  - `33a7e4e54476bf1215de9c0874abd7e06dca86cd` — ⚙️ JARVIS: Checkpoints ultra-seguros a cada 35 mins com lixeira automática (limite 3) — data não informada\n  - `cc6a50d14fe5bcd2f4f04d0927dbef4ca72b110e` — ⚙️ JARVIS: Adicionado sistema de Auto-Recuperação e Pontos de Salvamento constantes contra quedas de luz ⚡ — data não informada\n  - `b1ff848ded3b02f819bf3e4dfe7cf968caa401a4` — ⚙️ JARVIS: Downgrade estratégico de 3B para 1.5B para adequação física à VRAM da 1050 Ti — data não informada\n  - `24dea47e92856df8ed7a4958600ab79fe621951f` — feat: add fine-tuning script for Qwen2.5-Coder-3B using Unsloth and LoRA 4-bit optimization — data não informada\n  - `6fe8cf2ef890f650b824b59d87b78f44c984bc08` — ⚙️ JARVIS: Treinamento blindado para 4GB VRAM (512 seq, r=8) 💎 — data não informada\n  - `62aa0912a746e1b53e83ab4082b94edfc2a9f13c` — chore: ignore unsloth cache dir — data não informada\n  - `a26719619a70c323ef68d4eda0466c51437f459e` — ⚙️ JARVIS: VRAM memory ceiling fixed, Unsloth training explicitly operational 🚀🦾 — data não informada\n  - `4b332ef5638b3ccaffbfad319e441c9597916498` — 📝 Update log: Training officially running via Unsloth — data não informada\n  - `b2a4b1e815b91d34175fb3fabda55a12e819aa60` — 🏁 JARVIS: Nascimento iniciado! Motor CUDA a 100% no carregamento! 🚀🦾 — data não informada\n  - `2d9909810509a23f8857dd7c339ee5807af583fb` — feat: add distillation dataset for jarvis assistant training examples — data não informada\n  - `aa69c65140a4e390816c1998c21ef76d02b56ded` — feat: add distillation dataset for jarvis assistant training — data não informada\n  - `e455b68ad0891a8bad4453cc52e8b520100662f4` — 🧠 JARVIS: Cérebro carregado e repositório unificado com sucesso! 🚀🦾 — data não informada\n  - `bee7ebd754033a29e7bc280a6954492554d75a30` — JARVIS: Inicializacao limpa do repositorio sem arquivos gigantes — data não informada
\n## 69. William-kelvem94/SuperProjeto

- **Registros retornados:** 1
- **Amostra:**
  - `d6f2d9ceb7cb16a3334057e83132f7a5ed2e16e8` — Initial commit — data não informada
\n## 70. William-kelvem94/TCC_FINAL

- **Registros retornados:** 20
- **Amostra:**
  - `2569b5c1f51d95c412807533e51064124c590aea` — Update README.md — data não informada\n  - `8fde9072c2fcd077beec8402859c65cb187470b5` — Update README.md — data não informada\n  - `d6b593671d27a1c6219e591db4abab82249c02f0` — Décimo segundo commit — data não informada\n  - `e6a6c91a566832c86e193f02de82a6f4656a0ffe` — Décimo primeiro commit — data não informada\n  - `7fbf1b3b8c26e4f2ad9003b3ccec8900daa2db01` — Décimo commit — data não informada\n  - `d9c14a991bbaf1aeab08b794268845630f73c230` — Merge branch 'main' of github.com:William-kelvem94/TCC_FINAL — data não informada\n  - `9afca6b2ec222ddaeb035dde318d48fbcf4fff4a` — Décimo commit — data não informada\n  - `683103bb4240aade427ea8946365f09aa3f04328` — Update README.md — data não informada\n  - `5da5f3b051fe22485779c7ac4592708a43fa1279` — Nono commit — data não informada\n  - `0691c96c356fcccf9d7dd022f005337b4aef509a` — Oitavo commit — data não informada\n  - `e5d51c830d4aa6dae2655f7b2a72a6454eebc076` — Update README.md — data não informada\n  - `47e42b80d060842fb4ff63f84589a06bf4394311` — Sétimo commit — data não informada\n  - `9887db979bce77d0808d1c52383f061e55ac3cc9` — Sexto commit — data não informada\n  - `d1ef5e91534a2b5df1fba8e450e7cf4d9916c5dc` — Update README.md — data não informada\n  - `1bce2957afb048565d0100133b790ece1b13bf6d` — Update README.md — data não informada\n  - `108e9c6e16862b4bcf56b8389b4fbbf8c766e446` — Quinto commit - Funcional — data não informada\n  - `b7603edb0f607d68be0f06e0dfab2ff9b8ffc5bb` — Terceiro commit feito — data não informada\n  - `3dab0de1aa203dba31bc716c8376b8498b3ba51b` — Segundo commit feito — data não informada\n  - `afcfc5d40970829b2b9857fff32fd3899fece0d2` — adsa — data não informada\n  - `3433525ccda0b9f1f2389ca1075eb6e03895bd0c` — first commit — data não informada
\n## 71. William-kelvem94/TCC1---Modelo-Antigo

- **Registros retornados:** 1
- **Amostra:**
  - `32faecddd07378a747d5277a8c3bc0614fe3de03` — first commit — data não informada
\n## 72. William-kelvem94/TCC2_FINAL

- **Registros retornados:** 3
- **Amostra:**
  - `da46bf969eeccff1b01c508caa3892e8fd335957` — tentativa de rodar via docker

impossibilitado porque o docker não acessa camera e microfone — data não informada\n  - `5bf00d63df46d4c11f42a90b4a46d7e5d0cb1433` — Commit inicial do projeto TCC — data não informada\n  - `d94c27b5d440d30131620a864ed0f3b21c0eddca` — Initial commit — data não informada
\n## 73. William-kelvem94/teste

- **Registros retornados:** 0
- **Amostra:**
  - Nenhum registro retornado.
\n## 74. William-kelvem94/TESTER

- **Registros retornados:** 4
- **Amostra:**
  - `90a99fbb79963b2b8b2f1e8ffe3eeba61dbddc6f` — ci: use configured site for mobile test — data não informada\n  - `293aa51ee7d75071d07bdd3db4f0b8fa76fdcb0e` — ci: use configured site for scheduled browser tests — data não informada\n  - `e3d915e63748166cfbeeb0cc72f4bb77594ed722` — Enhance TestadorInterface with automation sequence features and UI improvements. Added a new tab for managing automation sequences, including recording, saving, and executing sequences. Updated the main window size and improved layout for better usability. Enhanced README to document new automation capabilities. — data não informada\n  - `9746fdb9dc376d406b2f06004629d4b919964856` — first commit — data não informada
\n## 75. William-kelvem94/Tradutor-2.0

- **Registros retornados:** 5
- **Amostra:**
  - `71e8ae47ef7403d8c27f364079a85c0de36d457e` — Ajustes no Requirements — data não informada\n  - `9e5b2014bd451d24430773593f864164304d4c37` — Criação do Requirements — data não informada\n  - `85c246dabb4e13a8fed20853d6645ced40f7a696` — Novas implementações — data não informada\n  - `8775fa1bed82971fdd15974f1d6ce2eaa8066f9e` — Novas Implementações — data não informada\n  - `3b772a27a2aca6b96f86d94295b4643325407a83` — Projeto inicial — data não informada
\n## 76. William-kelvem94/TRADUTOR-WKP

- **Registros retornados:** 6
- **Amostra:**
  - `4fea64af365cd6cfc23db20bc8c763a6d698792a` — Subindo projeto inicial ignorando venv — data não informada\n  - `71e8ae47ef7403d8c27f364079a85c0de36d457e` — Ajustes no Requirements — data não informada\n  - `9e5b2014bd451d24430773593f864164304d4c37` — Criação do Requirements — data não informada\n  - `85c246dabb4e13a8fed20853d6645ced40f7a696` — Novas implementações — data não informada\n  - `8775fa1bed82971fdd15974f1d6ce2eaa8066f9e` — Novas Implementações — data não informada\n  - `3b772a27a2aca6b96f86d94295b4643325407a83` — Projeto inicial — data não informada
\n## 77. William-kelvem94/TRANSCRITOR

- **Registros retornados:** 100
- **Amostra:**
  - `2a08311f075d337e37954733c37010f5e2b71205` — Corrige polling apos conclusao da transcricao — data não informada\n  - `15bb88a804a778ad0f0b80d4b9577613f8c0984f` — Evita corrida de inicializacao dos servicos — data não informada\n  - `ef069987ad64107a93167226da65e32201aef151` — Exibe transcrição ao vivo e integra resumo — data não informada\n  - `307a78682c9b33b492a4928133ab361f8c1a1817` — Moderniza telas React do TRANSCRITOR — data não informada\n  - `314e3b3f1ff04d1701430a2aec8b9095aa969b31` — Permite modelos incompatíveis com recomendação automática — data não informada\n  - `d8fe54e6d935156eda4e376fde55baf3f130a805` — Integra catalogo de modelos Whisper no frontend — data não informada\n  - `53554f0767496b2a6213ef82da484c67b1e2af14` — Aprimora selecao e validacao dos modelos Whisper — data não informada\n  - `91f6a7a222e5dc6385a435febcedb46d89f30e72` — Eleva qualidade padrão das transcrições — data não informada\n  - `78849453c516659cb14cc279ecf7efdb4b2c08d7` — Reformula frontend e persiste jobs assincronos — data não informada\n  - `bc4fc691cb8aa73a43fd7695cf34b30dc0af169b` — Corrige exibicao de resultado assincrono — data não informada\n  - `116624d031a25fe01f063be38722aaad24132fe4` — Mescla dashboards e refatoracao do frontend — data não informada\n  - `cd3c4b02fb026c95b9185cc04587683ba09498c7` — Refatora frontend e corrige worker de transcricao — data não informada\n  - `3590e72f3e9e6a5ecb4fe09007281d1e617021f8` — Adiciona dashboards completos do Grafana — data não informada\n  - `b07c4e1d4dd3a537883ce879c90d048ecf8eab92` — Corrigir encaminhamento e leitura da DLQ — data não informada\n  - `804038e302603b6e4d840586930b30710fb5fac4` — Corrigir fallback de consulta de jobs — data não informada\n  - `4101bfff90e3a9f212c1de6ce9e8f1169f50b7aa` — Corrigir health check do modo extractive — data não informada\n  - `181dd159261b68b63b8d6ea6884f667bd152b61c` — Corrigir endpoint de metricas do extrator — data não informada\n  - `314bb41f082f4499220b568c8d67e165bb39020a` — Corrigir encaminhamento da transcrição assíncrona — data não informada\n  - `ff4616289a0b3d7856d4f9ebec74a88219dd15c9` — Corrigir leitura de resultados na Web UI — data não informada\n  - `501f57420d84eecf2f5c47af302eaea037ba0112` — Configurar lint da Web UI — data não informada
\n## 78. William-kelvem94/vibe-coding-platform

- **Registros retornados:** 0
- **Amostra:**
  - Nenhum registro retornado.
\n## 79. William-kelvem94/webflash-intermediador-de-demandas

- **Registros retornados:** 29
- **Amostra:**
  - `fd5d8b290aabe1ebbdae7441f469ecd4da88575a` — docs: simplify repo positioning and legacy status — data não informada\n  - `84724aa73309a89083b831b3c38020ab6db7f085` — Remove arquivos gerados localmente e sincroniza o repositório — data não informada\n  - `21c1ad545e39e883ca892033234df9b27ad84010` — feat: Atualiza configuração do frontend para desenvolvimento sem Nginx

## 📋 Descrição
Modificações nos arquivos de configuração do Docker e do frontend para remover o uso do Nginx, ajustando as portas e comandos de execução.

## 🔧 Mudanças Técnicas
- Alteração do serviço `frontend` no `docker-compose.dev.yml` para expor a porta 3000 diretamente.
- Atualização do `Dockerfile.dev` para remover a instalação do Nginx e simplificar o health check.
- Modificação do `webpack.config.js` para ajustar o roteamento e permitir compressão, hot reloading e live reload.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Facilita o desenvolvimento local com um servidor mais simples.
- ⚡ **Manutenibilidade**: Estrutura de configuração mais clara e adaptada para um fluxo de trabalho de desenvolvimento ágil. — data não informada\n  - `b4f504d377a6a87fde573a320f1e70fb77eadc29` — feat: Atualiza configuração do frontend para uso do Nginx e melhorias na estrutura do projeto

## 📋 Descrição
Modificações nos arquivos de configuração do Docker e do frontend para implementar o Nginx como servidor, além de ajustes nas dependências e scripts.

## 🔧 Mudanças Técnicas
- Alteração do serviço `frontend` no `docker-compose.dev.yml` para usar Nginx e expor a porta 80.
- Atualização do `Dockerfile.dev` para incluir a instalação do Nginx e configuração.
- Modificação do `package.json` para adicionar novos scripts e dependências, como `clsx` e `tailwind-merge`.
- Ajustes no `webpack.config.js` para permitir acesso de hosts externos e melhorar a configuração do servidor de desenvolvimento.
- Alterações na estrutura de componentes e páginas para melhor organização e usabilidade.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Melhoria na performance e na experiência do usuário com o uso do Nginx.
- ⚡ **Manutenibilidade**: Estrutura de código mais organizada e adaptada para futuras expansões e melhorias. — data não informada\n  - `e969cdafe273e3f042c417c7d19c79a575cc1ad5` — feat: Atualiza configuração do Docker e implementa novas funcionalidades no backend

## 📋 Descrição
Modificações no arquivo `docker-compose.dev.yml` para incluir novos volumes e variáveis de ambiente, além de implementar health checks para os serviços. Atualizações no backend para suportar uploads de arquivos, autenticação com JWT, e novas rotas para gerenciamento de comentários e histórico.

## 🔧 Mudanças Técnicas
- Adição de volumes para logs e uploads no Docker.
- Inclusão de variáveis de ambiente para configuração do banco de dados e Redis.
- Implementação de health checks para os serviços de backend e frontend.
- Criação de novas rotas no backend para uploads, comentários e histórico de demandas.
- Atualização do README.md com novas funcionalidades e melhorias na documentação.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Melhoria na gestão de arquivos e feedback do usuário.
- ⚡ **Manutenibilidade**: Estrutura de código mais organizada e adaptada para futuras expansões. — data não informada\n  - `891c4f70390c2d4782c2e3ae35a42a4a2e846960` — feat: Adiciona dashboard executivo e funcionalidades de gerenciamento de demandas

## 📋 Descrição
Implementa um dashboard executivo com estatísticas em tempo real e um sistema de gerenciamento de demandas, incluindo CRUD completo e notificações.

## 🔧 Mudanças Técnicas
- Adição de novas seções no README.md para descrever funcionalidades e cenários de teste.
- Implementação da página de Dashboard com visualização de métricas do sistema e demandas.
- Integração de um sistema de notificações para feedback do usuário nas páginas de gerenciamento de demandas.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Melhoria na visualização de dados e interações do usuário.
- ⚡ **Manutenibilidade**: Estrutura de código mais organizada, facilitando futuras expansões e melhorias. — data não informada\n  - `743ec34c0d7c6ab90cb1fb90814c1acf8721ade1` — feat: Implementa navegação e gerenciamento de demandas no frontend

## 📋 Descrição
Adiciona a funcionalidade de navegação e gerenciamento de demandas na aplicação frontend, utilizando `react-router-dom` para rotas.

## 🔧 Mudanças Técnicas
- Implementação de rotas para as páginas de status e demandas.
- Criação de um serviço para gerenciar as operações de demandas, incluindo listagem, criação, atualização e exclusão.
- Estilização e estruturação do layout para uma melhor experiência do usuário.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Facilita a navegação entre diferentes seções da aplicação.
- ⚡ **Manutenibilidade**: Estrutura de código mais clara e organizada, permitindo futuras expansões e melhorias. — data não informada\n  - `d6038780d0b7004159310ddbfebee12ead7162d8` — refactor: Atualiza configurações do TypeScript para desativar verificações estritas

## 📋 Descrição
Modificação do arquivo `tsconfig.json` para desativar as opções de verificação estrita do TypeScript, facilitando o desenvolvimento.

## 🔧 Mudanças Técnicas
- Alteração das configurações de `strict`, `noImplicitAny`, `strictNullChecks`, e `exactOptionalPropertyTypes` para `false`.

## 🎯 Benefícios Alcançados
- ⚡ **Manutenibilidade**: Redução da rigidez nas verificações de tipo, permitindo um desenvolvimento mais ágil e flexível. — data não informada\n  - `059886140865556eb624d8045af676b0e03e5b25` — fix: Corrige importação de demandas no arquivo api.ts

## 📋 Descrição
Comentado temporariamente o import do `demandasRouter` no arquivo `api.ts` para evitar conflitos durante o desenvolvimento.

## 🔧 Mudanças Técnicas
- O import de `demandasRouter` foi comentado para facilitar a manutenção e evitar erros de execução.

## 🎯 Benefícios Alcançados
- ⚡ **Manutenibilidade**: Melhoria na clareza do código e prevenção de possíveis conflitos durante o desenvolvimento. — data não informada\n  - `0fab5ab0c705067a44bbd73c60b2ebbf6534f86d` — feat: Implementa novos endpoints para gerenciamento de demandas

## 📋 Descrição
Adição de endpoints para criação e consulta de demandas no backend, simplificando a estrutura de rotas.

## 🔧 Mudanças Técnicas
- Implementação do endpoint GET `/demandas` para retornar uma lista de demandas simuladas.
- Implementação do endpoint POST `/demandas` para criar uma nova demanda simulada.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Facilita a interação com o sistema de demandas.
- ⚡ **Manutenibilidade**: Estrutura de rotas mais clara e adaptada para futuras expansões. — data não informada\n  - `8fff1662a96a79790335d1e9285117d08af60ccc` — refactor: Atualiza comandos de execução e estrutura do banco de dados

## 📋 Descrição
Modificações nos arquivos de configuração do Docker e no esquema do banco de dados para otimizar o ambiente de desenvolvimento e a estrutura de dados.

## 🔧 Mudanças Técnicas
- Alteração do comando de execução no `docker-compose.dev.yml` para compilar e iniciar a aplicação em sequência.
- Adição de novas tabelas e índices no arquivo `init.sql` para o PostgreSQL, incluindo a tabela de `demandas` e `demanda_historico`.
- Implementação de um novo endpoint de teste no backend para verificar a conexão com o banco de dados.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Inicialização mais eficiente do ambiente de desenvolvimento e melhor estrutura de dados.
- ⚡ **Manutenibilidade**: Estrutura de banco de dados mais clara e adaptada para o fluxo de trabalho de desenvolvimento contínuo. — data não informada\n  - `fad397bb46bbd4eb0c57c7620618a23793f690a9` — chore: Atualiza dependências e configurações no package.json e package-lock.json

## 📋 Descrição
Modificações nos arquivos `package.json` e `package-lock.json` para incluir novas dependências e atualizar versões existentes.

## 🔧 Mudanças Técnicas
- Adição da dependência `ts-jest` e suas dependências relacionadas.
- Atualização das versões de `compression`, `express`, `express-rate-limit`, `zod`, e tipos associados.
- Inclusão de novos módulos no `package-lock.json`, como `bs-logger`, `handlebars`, `lodash.memoize`, `make-error`, `neo-async`, e `uglify-js`.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Melhoria na gestão de dependências e suporte a testes com TypeScript.
- ⚡ **Manutenibilidade**: Estrutura de dependências mais clara e atualizada, facilitando o desenvolvimento contínuo. — data não informada\n  - `ad8f9ce79ec34a19065ae0650c6c12dadc5e7b94` — refactor: Atualiza comando de instalação de dependências no Dockerfile.dev

## 📋 Descrição
Modificação no `Dockerfile.dev` para alterar o comando de instalação de dependências de `npm ci` para `npm install`, incluindo dependências de desenvolvimento.

## 🔧 Mudanças Técnicas
- Substituição do comando de instalação para permitir a inclusão de dependências de desenvolvimento durante a configuração do ambiente.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Melhoria na flexibilidade da instalação de pacotes durante o desenvolvimento.
- ⚡ **Manutenibilidade**: Estrutura de Docker mais adaptada para o fluxo de trabalho de desenvolvimento contínuo. — data não informada\n  - `934148d106b14c7cc101935543a6b3f742a9a10b` — refactor: Atualiza comandos de execução no Docker e package.json

## 📋 Descrição
Modificações nos arquivos de configuração do Docker e no package.json para otimizar o ambiente de desenvolvimento.

## 🔧 Mudanças Técnicas
- Alteração do comando de execução do serviço no `docker-compose.dev.yml` para `npm run dev`, simplificando o processo de inicialização.
- Atualização dos scripts no `package.json` para utilizar o caminho completo do `tsx`, garantindo a execução correta.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Inicialização mais rápida e eficiente do ambiente de desenvolvimento.
- ⚡ **Manutenibilidade**: Estrutura de comandos mais clara e consistente, facilitando o desenvolvimento contínuo. — data não informada\n  - `6c5e7c877f3c407f4e17e981b92d4e3b5047246b` — fix: Atualiza caminhos de arquivos TypeScript no tsbuildinfo

## 📋 Descrição
Modificação do arquivo `tsbuildinfo` para corrigir os caminhos dos arquivos TypeScript, refletindo a nova estrutura de diretórios.

## 🔧 Mudanças Técnicas
- Atualização dos caminhos para as definições de tipos do TypeScript, ajustando para a nova localização das bibliotecas.

## 🎯 Benefícios Alcançados
- ⚡ **Manutenibilidade**: Estrutura de arquivos mais clara e alinhada com a nova organização do projeto, facilitando o desenvolvimento contínuo. — data não informada\n  - `39a1e3510ab5fe836579a08c9193092e2412a4f6` — refactor: Atualiza comandos de execução e instalação de dependências no Docker

## 📋 Descrição
Modificações nos arquivos de configuração do Docker para otimizar a execução do ambiente de desenvolvimento.

## 🔧 Mudanças Técnicas
- Alteração do comando de execução do serviço no `docker-compose.dev.yml` para compilar e iniciar a aplicação em sequência.
- Atualização do `Dockerfile.dev` para instalar dependências de desenvolvimento e TypeScript globalmente, substituindo `npm ci` por `npm install`.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Inicialização mais eficiente do ambiente de desenvolvimento.
- ⚡ **Manutenibilidade**: Estrutura de Docker mais clara e adaptada para desenvolvimento contínuo. — data não informada\n  - `042a40cd10c8355142d29ba3cb5ba33bed840131` — chore: Atualiza dependências e remove configuração obsoleta do @ljharb/tsconfig

## 📋 Descrição
Atualização do arquivo `package-lock.json` para a versão 2.0.0, incluindo novas dependências e melhorias de segurança. Remoção de arquivos e configurações obsoletas do pacote `@ljharb/tsconfig`.

## 🔧 Mudanças Técnicas
- Atualização da versão do projeto para 2.0.0.
- Inclusão de novas dependências do Babel e ajustes nas versões do Node.
- Remoção de arquivos desnecessários do pacote `@ljharb/tsconfig`, incluindo `.eslintrc`, `CHANGELOG.md`, `LICENSE`, `package.json`, `README.md`, e `tsconfig.json`.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Melhoria na gestão de dependências e segurança do projeto.
- ⚡ **Manutenibilidade**: Estrutura de código mais limpa e organizada, facilitando futuras expansões. — data não informada\n  - `a919bbbf2604c5a7b84d66276789f6fb72ce80d0` — feat: Atualiza README e refatora o backend com melhorias de segurança e estrutura

## 📋 Descrição
Atualização do README para refletir a nova arquitetura e funcionalidades do WebFlash, além de refatorações no backend para melhorar a segurança e a estrutura do código.

## 🔧 Mudanças Técnicas
### README
- Adição de uma visão geral do projeto, características principais e tecnologias utilizadas.
- Inclusão de instruções detalhadas para instalação e configuração.

### Backend
- Implementação de middleware de segurança com Helmet, CORS e Rate Limiting.
- Refatoração do arquivo `app.js` para melhorar a estrutura e a legibilidade.
- Adição de um logger para monitoramento de requisições e erros.
- Melhoria no handler de erros para fornecer respostas mais informativas.

## 🎯 Benefícios Alcançados
- 🚀 **Usabilidade**: Documentação mais clara e abrangente para novos desenvolvedores.
- 🛡️ **Segurança**: Adoção de melhores práticas de segurança no backend.
- ⚡ **Manutenibilidade**: Código mais organizado e fácil de entender, facilitando futuras expansões. — data não informada\n  - `1644371c6ef1503a13a843e3fd3545c647173280` — refactor: Simplifica a estrutura do backend e atualiza a configuração do frontend

## 📋 Descrição
Refatoração significativa do backend e melhorias na configuração do frontend para otimizar a aplicação.

## 🔧 Mudanças Técnicas
### Backend
- Remoção de dependências não utilizadas e simplificação do código no arquivo `app.js`.
- Implementação de um novo endpoint de teste e um handler 404.
- Alteração na forma de iniciar o servidor, utilizando `app.listen` diretamente.

### Frontend
- Adição de novas dependências no `package.json` para suporte a Tailwind CSS e PostCSS.
- Atualização do `webpack.config.js` para integrar o `postcss-loader` e suporte a Tailwind.
- Modificação do arquivo `index.html` para refletir o novo título da aplicação e estrutura.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Inicialização mais rápida e estrutura de código mais limpa.
- ⚡ **Usabilidade**: Interface mais estilizada com suporte a novas funcionalidades de estilo.

## 🔍 Impacto
Essas alterações visam proporcionar uma base mais sólida e eficiente para o desenvolvimento contínuo do projeto, facilitando a integração e o deploy. — data não informada\n  - `8572dc70399c6a94730fb9ae16a7ed0eee70325f` — refactor: Simplifica Dockerfiles e remove arquivos de lock

## 📋 Descrição
Refatoração dos Dockerfiles do backend e frontend para simplificar a instalação de dependências e melhorar a estrutura de execução.

## 🔧 Mudanças Técnicas
- Alteração do comando de instalação de dependências no Dockerfile do backend de `npm ci` para `npm install`.
- Remoção do arquivo `package-lock.json` do backend e frontend para evitar conflitos de versão.
- Atualização do Dockerfile do frontend para corrigir a cópia dos arquivos de build.

## 🎯 Benefícios Alcançados
- 🚀 **Performance**: Inicialização mais rápida da aplicação.
- ⚡ **Manutenibilidade**: Estrutura de Docker mais clara e fácil de entender.

## 🔍 Impacto
Essas alterações visam proporcionar uma base mais sólida e eficiente para o desenvolvimento contínuo do projeto, facilitando a integração e o deploy. — data não informada
\n## 80. William-kelvem94/Will-obsidian

- **Registros retornados:** 100
- **Amostra:**
  - `bebdac31f7823e41bba5148cc3be314c611620ad` — docs(obsidian): registrar status de issues workflows releases e dependencias — data não informada\n  - `ba7afbfde4dbb419807e6975f2b1f89cb166be21` — data(obsidian): coletar manifestos e dependencias dos repositorios — data não informada\n  - `48b21cad3a116e033f279ade3991b1ced017aa98` — docs(obsidian): mapear semanticamente projetos estrategicos do GitHub — data não informada\n  - `654baea3d6276e3ba8cf30becdaf93930185b05f` — data(obsidian): registrar branches e estrutura raiz dos repositorios — data não informada\n  - `b4387e35753455acddd8ae04dedc8efcaa2d40d6` — data(obsidian): registrar telemetria de linguagens commits e arvores — data não informada\n  - `9c5b73f1dfce6892f7e02cd7c2b626e140306a05` — docs(obsidian): adicionar telemetria tecnica completa dos repositorios — data não informada\n  - `a24cdcd3a0b3a477e6e40f2130b7064c188de011` — data(obsidian): coletar READMEs dos repositorios GitHub — data não informada\n  - `bccd1c43a08ed827622f2f92bb8b50535476f28f` — docs(obsidian): adicionar fichas detalhadas dos 85 repositorios GitHub — data não informada\n  - `767b6c35670bb7b548831be0f8437ac7b2cdb2ef` — docs(obsidian): apontar master plan para inventario GitHub atualizado — data não informada\n  - `cc1ec99a188915aa92468892358409a2539c4afe` — docs(obsidian): atualizar inventario completo do GitHub em 2026-08-22 — data não informada\n  - `dcbbd91f4c5a777829dd46cd3f8aceea94bf029b` — Reconciliar manifesto do fechamento da manha — data não informada\n  - `8c207e07495cff2c29e5a415422ff121c9037279` — Registrar resultado Git do fechamento da manha — data não informada\n  - `df2d1163ceef644156dbaf0ec14e897a6cb66618` — Fechamento Codex da manha em 03/08/2026 — data não informada\n  - `99b6b3f9e50d0300cfe69defbb4675f397012edb` — Consolidar fechamento Codex de 31/07 a tarde — data não informada\n  - `9ec4ca8017a710b05fc8c2d85fb73d06afbc8cab` — Registrar confirmacao final do fechamento Codex 2026-07-31 — data não informada\n  - `049b0138cfed54caea50f1f27cf659d3f7af176e` — Registrar resultado Git do fechamento Codex 2026-07-31 — data não informada\n  - `7fc83c2d6e8bebe067595ce8101e4d81b7cecfe4` — Consolidar fechamento operacional do Codex de 2026-07-31 — data não informada\n  - `a5b45d4c3f28aa89223d47f4e48774c01c450d96` — Finalizar registro do fechamento Codex tarde — data não informada\n  - `bf2f7b34965487edc7e68022754faff18e0990db` — Registrar hash do fechamento Codex — data não informada\n  - `1fa8c5aebbbca6f8eef0fb3e05a93440c8d3ead2` — Fechamento Codex tarde: preservar fontes pendentes — data não informada
\n## 81. William-kelvem94/Will.Nexus

- **Registros retornados:** 100
- **Amostra:**
  - `3e895fc768f43affcac69ed612df442678b6cc15` — perf(supabase): remove índice duplicado da fila HITL — data não informada\n  - `8c00c8922359b17f71ded3010bb4bfd6d2b8381a` — feat(ui): adiciona cadeia causa efeito aos projetos — data não informada\n  - `145d692e17cf1f89eabf3f571252f96dceb0b6ff` — chore(supabase): versiona autenticação customizada das Edge Functions — data não informada\n  - `7b3bd91c1764d151704d2a3681abfcb1d34f6f1a` — chore(supabase): versiona gateway OIDC do Agent Core — data não informada\n  - `97308161a51c556fd82dc6f454187c58725a3c71` — feat(operations): mostra correlações causais no detalhe do projeto — data não informada\n  - `862a7663a8f380c5bc356f4afbcb09a1fcdbce22` — feat(operations): correlaciona commit deploy health e alertas — data não informada\n  - `8b384654220c4f717b3e7521f75be543cb4023d6` — chore(supabase): versiona auditoria do Agent Core e decisões HITL — data não informada\n  - `415213f7c99ad60e118b9a849327c7f8e747e001` — feat(agent): mostra freshness e HITL no Control Center — data não informada\n  - `7dd2305365132469da92f2186d4c788ef1d815b4` — feat(agent): mede freshness real dos adapters — data não informada\n  - `d01b7818ddc60fdfe8fa37883ab5d532f89cc3ba` — feat(agent): adiciona estado explícito de freshness aos adapters — data não informada\n  - `c2e4a6f3b2c4e1ad253c1560a5bd3c03463aaecf` — feat(agent): protege página de Ações com HITL autenticado — data não informada\n  - `5ee029d63642a4754f960044ee7ccdcddc972056` — feat(agent): adiciona painel HITL autenticado para aprovar e rejeitar propostas — data não informada\n  - `1b120f0ab41156671c6b65b77e76e523431eec2d` — feat(agent): conecta interface do Nexus AI ao Agent Chat com HITL — data não informada\n  - `5519c7a33548ac64528e9fe45965a24fbaafd759` — feat(agent): cria chat unificado com tool-calling e HITL persistente — data não informada\n  - `695b2ecfdb81961166377c3ee6f74c7a10bfdd5c` — test(agent): expõe self-test protegido do Agent Core — data não informada\n  - `95add64e3470429b85e6da591534e31d24a0c952` — test(agent): adiciona smoke test das skills disponíveis — data não informada\n  - `a1f2d41eb6f26ca95c193bb0428bb78c0e6bf16b` — feat(agent): protege fila de ações com sessão HITL do proprietário — data não informada\n  - `097283ae8313bf966d95757f575f7f597b3a5c77` — feat(operations): garante freshness do próprio WillNexus antes das leituras — data não informada\n  - `119950ccb921abf77201f4d867ab8bd2262970a1` — feat(operations): reconcilia deployment atual pelo runtime da Vercel — data não informada\n  - `38fe00e1e38d093cc13f03bf426194d751b4641a` — feat(agent): persiste auditoria verificável de cada tool run — data não informada
\n## 82. William-kelvem94/WilletHub

- **Registros retornados:** 1
- **Amostra:**
  - `d0554fc9758c0722e13f83a8494537637f6d1dfd` — chore: publicar WilletHub — data não informada
\n## 83. William-kelvem94/willethub-legacy

- **Registros retornados:** 5
- **Amostra:**
  - `f6ae0a1537121814351419c5ce928e8cb8c7f8da` — docs: clarify project role and separation — data não informada\n  - `5745b4e24402ee55055a296eac66a1edb992725a` — [BACKEND/INFRA] Atualizações e ajustes em backend, Docker e documentação

- Atualização do Dockerfile do backend para refletir novas dependências e práticas
- Atualização do package.json e package-lock.json do backend para dependências essenciais
- Ajustes em controllers, middlewares e rotas de autenticação
- Atualização do schema.prisma para refletir melhorias de modelo
- Ajustes no docker-compose.yml para melhor integração dos serviços
- Adição de arquivos de configuração e documentação (GUIA_DE_USO.md, prisma.config.ts)
- Adição de client.ts e configs do Prisma

#Backend #Docker #Prisma #Documentação — data não informada\n  - `444f26685ee4a8fd16184a47096fd95462944b8b` — [MELHORIA GERAL]  Refatoração e evolução massiva do projeto Notion Clone

- Instalação e configuração de todas as dependências essenciais para funcionalidades avançadas:
  - TipTap (editor rich text completo, extensões, blocos, slash commands)
  - DnD Kit (drag-and-drop para blocos, tabelas, board/kanban)
  - React Query (cache e sincronização de dados com backend)
  - React Big Calendar, date-fns (visualização de calendário)
  - React Hot Toast, CMDK, Zustand, Framer Motion, etc
- Atualização do package.json frontend e backend para suportar:
  - Blocos avançados, upload de arquivos, MinIO, permissões, sharing, search, etc
- Preparação para implementação de:
  - Editor TipTap funcional com toolbar, blocos, slash commands
  - Integração real frontend  backend (PageView, DatabaseView, TableView, BoardView)
  - Controllers completos no backend (Page, Block, Database, Permission, Sync, File Upload)
  - Sidebar hierárquico, múltiplos workspaces, sharing, comments, search global
- Estrutura pronta para colaboração em tempo real (Socket.io), upload de arquivos, e futuras features do Notion real

# Refatoração #Evolução #NotionClone #TipTap #DnDKit #ReactQuery #MinIO #SocketIO #MVP — data não informada\n  - `b31fbee2dae1f6313913d5bec82b2046acf2ab67` — Initial project structure and core feature scaffolding

Add backend and frontend directories with Docker, Prisma, and TypeScript setup. Implement initial authentication, page CRUD, and block system for a Notion-like collaborative platform. Include documentation, environment examples, and essential configuration files for rapid development and onboarding. — data não informada\n  - `64898f122d7ac261c6ce095ce7175747a8c074f8` — Initial commit — data não informada
\n## 84. William-kelvem94/WILLFINANCE-9.0

- **Registros retornados:** 2
- **Amostra:**
  - `5dc5260880cce599f59d30fcb9e429a7df4d068e` — feat: configuraÃ§Ã£o Docker completa e correÃ§Ãµes de autenticaÃ§Ã£o

- Adicionado Dockerfile multi-stage otimizado
- Configurado docker-compose.yml com PostgreSQL e aplicaÃ§Ã£o
- Implementada detecÃ§Ã£o automÃ¡tica de cliente DB (Neon vs PostgreSQL local)
- Adicionado suporte a pg (node-postgres) para Docker
- Corrigidos atributos autocomplete nos formulÃ¡rios de login/registro
- Desabilitado Vercel Analytics em desenvolvimento
- Adicionado endpoint de health check
- Criados scripts de inicializaÃ§Ã£o Docker
- DocumentaÃ§Ã£o Docker completa (DOCKER.md) — data não informada\n  - `fc609deb7a429433def616a453837a2617824b4f` — Initial commit — data não informada
\n## 85. William-kelvem94/William-kelvem94

- **Registros retornados:** 4
- **Amostra:**
  - `54792a2a913631c8cd64bb9f23a90555cdc5f5a7` — Adiciona arte ASCII discreta ao perfil público — data não informada\n  - `1252ddc9007795b708765a67f6ff120679e7a083` — Melhora apresentação visual do perfil sem expor informações sensíveis — data não informada\n  - `62bc2f85ad719950c238a6086d912e9946ee1f0b` — Atualiza portfolio com visual moderno e seguro — data não informada\n  - `feace1d23667279a20c4261f4cbc7009e77849f4` — Create README.md — data não informada


## Limitação

Para contagem total exata e histórico completo, é necessário acessar a API de commits com paginação por repositório ou clonar os repositórios.