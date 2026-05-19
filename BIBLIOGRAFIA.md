# Como Referenciar & Bibliografia no Will-obsidian

## Formatos possíveis
- Inline: `[Nome da fonte](https://link) DOI:10.x/abc.12.34`
- Padrão BibTeX: 
```bibtex
@article{autor2024,
  title={Título},
  author={Nome, A.},
  year={2024},
  journal={Revista X},
  doi={10.x/abc.12.34}
}
```
- Campo de frontmatter:
```yaml
referencias:
  - "[Nome da fonte](https://link) DOI:10.x/abc.12.34"
```
## Extração automática
Script `scripts/gen_bibliography.py` irá extrair DOIs, URLs e citações para compilar uma BIB completa do vault,
atualizando automaticamente este arquivo e as seções finais das notas principais.
