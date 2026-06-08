# Graph Legenda

#hub #graph

Este arquivo descreve as categorias do gráfico do Obsidian, as tags recomendadas e a organização que mantém o mapa visual limpo.

## Como funciona
- O gráfico usa `colorGroups` em `.obsidian/graph.json`.
- Cada grupo é ativado por tags.
- Use as tags listadas aqui em cada nota-chave e índice para manter a cor consistente.

## Tags e pastas principais
- **Hub & índices** — laranja `#f97316`
  - Aplicar em notas de entrada, MOCs e índices.
  - Pastas/arquivos: `Bem-vindo.md`, `Projetos.md`, `Projetos/README.md`, `Projetos/Privados/README.md`, `JARVIS/README.md`, `Will-Pessoal/README.md`, `Will-Pessoal/Perfil/README.md`, `Graph-Legenda.md`.
  - Tag principal: `#hub`
  - Observação: `Will-Pessoal/README.md` é o hub pessoal principal para perfil, vida, objetivos e conhecimento.

- **Projetos públicos** — verde `#22c55e`
  - Aplica a projetos no vault público e a notas de descrição de projeto.
  - Pastas: `Projetos/`, `Projetos/Python/`, `Projetos/PHP/`, `Projetos/Java/`, `Projetos/Outros/`.
  - Tag principal: `#projetos`

- **Projetos privados** — verde escuro `#15803d`
  - Aplica a clones locais e notas de análise de projetos que você mantém no vault.
  - Pasta: `Projetos/Privados/`.
  - Tag principal: `#privados`

- **Jarvis / IA** — azul `#2563eb`
  - Aplica a toda a estrutura do segundo cérebro e às notas de tomada de decisão ou conhecimento técnico do Jarvis.
  - Pasta: `JARVIS/`.
  - Tag principal: `#jarvis`

- **Estudos & pesquisa** — roxo `#c084fc`
  - Aplica a pesquisas técnicas, referências e estudos de caso.
  - Pastas: `Projetos/EstudosPesquisas/`, `Projetos/EstudosFocados/`, `JARVIS/Aprendizado/`.
  - Tags principais: `#estudos`, `#pesquisas`

- **Memórias & decisões** — vermelho `#dc2626`
  - Aplica a notas de memória, histórico e escolhas importantes.
  - Pastas: `JARVIS/Memorias/`, `JARVIS/Decisoes/`.
  - Tags principais: `#memoria`, `#decisao`

- **Perfil & pessoal** — ciano `#0ea5e9`
  - Aplica a notas de perfil, preferências pessoais e rotina.
  - Pastas/arquivos: `Will-Pessoal/Perfil/`, `Will-Pessoal/Perfil/William-kelvem94 Overview.md`, `Will-Pessoal/Perfil/Cerebro-Will.md`.
  - Tag principal: `#perfil`

- **Templates & configs** — turquesa `#14b8a6`
  - Aplica a templates e arquivos de estrutura.
  - Pasta: `JARVIS/Templates/`.
  - Tag principal: `#template`

- **Conhecimento-Geral** — âmbar `#f59e0b`
  - Aplica a toda a base de conhecimento multidisciplinar com 10 domínios.
  - Pasta: `Conhecimento-Geral/`.
  - Tag principal: `#conhecimento`

## Mapas de tags por pasta
- `Bem-vindo.md` → `#hub #projetos`
- `Projetos.md` → `#hub #projetos`
- `Projetos/README.md` → `#hub #projetos`
- `Projetos/Privados/README.md` → `#hub #privados`
- `Projetos/GitHub-Completo.md` → `#projetos #github`
- `Projetos/Plano-de-Acao.md` → `#projetos #prioridade`
- `Projetos/Organizacao-Completa.md` → `#projetos #organizacao`
- `JARVIS/README.md` → `#hub #jarvis`
- `JARVIS/Memorias/README.md` → `#jarvis #memoria`
- `JARVIS/Aprendizado/INDEX.md` → `#jarvis #aprendizado`
- `JARVIS/Decisoes/INDEX.md` → `#jarvis #decisao`
- `JARVIS/Templates/INDEX.md` → `#jarvis #template`
- `Will-Pessoal/Perfil/README.md` → `#perfil #will`
- `Will-Pessoal/README.md` → `#perfil #will`
- `Conhecimento-Geral/INDEX.md` → `#hub #conhecimento`

## Uso recomendado
1. Abra `Bem-vindo.md` para entrar no cofre.
2. Use `Projetos.md` como MOC de projetos públicos.
3. Use `Projetos/Privados/README.md` para acessar clones privados.
4. Use `JARVIS/README.md` como hub do segundo cérebro.
5. Use `JARVIS/Memorias/README.md` para buscar memórias e decisões.
6. Use `Conhecimento-Geral/INDEX.md` para navegar pelos 10 domínios de conhecimento.
7. Atualize os tags de cada nota nova no início do arquivo.

## Boas práticas de organização
- Mantenha cada projeto dentro da pasta certa: `Projetos/` ou `Projetos/Privados/`.
- Use uma nota de índice para cada subpasta importante.
- Não misture notas de `JARVIS/` com notas de `Projetos/` sem um link claro.
- Crie notas de status e diagnóstico em `Projetos/Plano-de-Acao.md` e `Projetos/Organizacao-Completa.md`.

## Observação
Se o gráfico não exibir cores na primeira vez, feche e reabra o vault ou a visualização do gráfico.

## Plugins recomendados
- Se o Obsidian nativo não aplicar cores de forma clara, o plugin `Juggl` costuma oferecer visualização de gráfico mais avançada e com suporte a nós coloridos.
- Outra opção é usar `Graph Analysis` / `Graph View` plugins adicionais que tenham suporte a grupos de cor e filtros por tag.
