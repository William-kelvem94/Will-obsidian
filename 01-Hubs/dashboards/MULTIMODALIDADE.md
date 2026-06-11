# Padrão de Multimodalidade Will-obsidian

Todo arquivo .md pode referenciar assets no frontmatter:

```yaml
assets:
  - type: pdf
    file: arquivos/algum_doc.pdf
    description: Relatório de Pesquisa
  - type: image
    file: img/fluxograma.png
    description: "Fluxograma de dados"
  - type: audio
    file: audio/entrevista1.ogg
    description: "Coletânea de entrevistas"
```

Scripts automatizados (`scripts/preprocess_multimodal.py`) capturam todos os assets referenciados, constroem índice e,
se desejado, processam PDFs/textos/imagem em lote (PDF→texto, imagem→caption, audio→transcript).

## Como usar
- Sempre referencie assets reais existentes.
- Atualize o campo `assets` sempre que adicionar/remover arquivos correlatos.
- Evite anexar arquivos não processáveis.
