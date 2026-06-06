"""
Script: scripts/gen_bibliography.py
Extrai automaticamente DOIs, URLs, referências de frontmatter e blocos BibTeX
de todas as notas do vault para gerar uma bibliografia compilada e estruturada.
Este script atualiza automaticamente o arquivo dashboards/BIBLIOGRAFIA.md.
"""

from pathlib import Path
import re
import yaml

ROOT = Path(__file__).resolve().parents[1]
BIB_FILE = ROOT / 'dashboards' / 'BIBLIOGRAFIA.md'

# Expressões regulares para captura
BIBTEX_RE = re.compile(r"```bibtex\s*\n(.*?)\n```", re.DOTALL | re.IGNORECASE)
DOI_RE = re.compile(r"(?:doi:|(?:https?://)?(?:dx\.)?doi\.org/)(10\.\d{4,9}/[-._;()/:A-Z0-9]+)", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^\s)\]]+", re.IGNORECASE)

def extract_from_file(p: Path):
    content = p.read_text(encoding='utf-8')
    refs = []
    
    # 1. Parse Frontmatter
    lines = content.splitlines()
    frontmatter = {}
    if lines and lines[0].strip() == '---':
        fm_lines = []
        for l in lines[1:]:
            if l.strip() == '---':
                break
            fm_lines.append(l)
        try:
            frontmatter = yaml.safe_load('\n'.join(fm_lines)) or {}
        except Exception:
            pass
            
    referencias_fm = frontmatter.get('referencias', [])
    if isinstance(referencias_fm, list):
        for r in referencias_fm:
            refs.append({
                'source': p,
                'type': 'Frontmatter',
                'detail': r.strip()
            })
    elif isinstance(referencias_fm, str):
        refs.append({
            'source': p,
            'type': 'Frontmatter',
            'detail': referencias_fm.strip()
        })

    # 2. Parse BibTeX blocks
    for match in BIBTEX_RE.finditer(content):
        bib_block = match.group(1).strip()
        # Parse minimal info from BibTeX
        title_match = re.search(r"title\s*=\s*[{'\"](.*?)['\"}]", bib_block, re.IGNORECASE)
        author_match = re.search(r"author\s*=\s*[{'\"](.*?)['\"}]", bib_block, re.IGNORECASE)
        year_match = re.search(r"year\s*=\s*[{'\"]?(\d{4})['\"]?", bib_block, re.IGNORECASE)
        
        detail = []
        if author_match:
            detail.append(author_match.group(1))
        if year_match:
            detail.append(f"({year_match.group(1)})")
        if title_match:
            detail.append(f"*{title_match.group(1)}*")
            
        ref_text = ", ".join(detail) if detail else "BibTeX Entry"
        # Add the raw bibtex blocks as extra detail or tooltip if needed, just show summarized
        refs.append({
            'source': p,
            'type': 'BibTeX',
            'detail': ref_text
        })

    # 3. Parse DOIs directly in text blocks (if not captured in frontmatter)
    # Search for DOI patterns line by line
    for line in lines:
        # Check if line contains a DOI that's not already in parsed elements
        doi_matches = DOI_RE.findall(line)
        for d in doi_matches:
            # check the markdown link context
            label_match = re.search(r"\[(.*?)\]\((.*?)\)", line)
            url_context = label_match.group(1) if label_match else f"DOI: {d}"
            
            # Avoid duplicate citations from same line
            if not any(d in r['detail'] for r in refs):
                refs.append({
                    'source': p,
                    'type': 'DOI',
                    'detail': f"[{url_context}](https://doi.org/{d}) (DOI: {d})"
                })
                
        # 4. Extract standard web URLs tagged under reference lines
        if "referencia" in line.lower() or "fonte" in line.lower() or "source" in line.lower():
            urls = URL_RE.findall(line)
            for u in urls:
                # avoid duplication
                if not any(u in r['detail'] for r in refs):
                    label_match = re.search(r"\[(.*?)\]\((.*?)\)", line)
                    disp = label_match.group(1) if label_match else "Link de Referência"
                    refs.append({
                        'source': p,
                        'type': 'URL',
                        'detail': f"[{disp}]({u})"
                    })
                    
    return refs

def main():
    print("🔍 Escaneando o vault em busca de referências bibliográficas...")
    all_refs = []
    
    # Exclude system and hidden dirs
    ignore_dirs = {'.logs', '.obsidian', 'node_modules', '.github', '.agents', '.continue'}
    
    for path in ROOT.rglob('*.md'):
        if any(part in ignore_dirs or part.startswith('.') for part in path.parts):
            continue
        # Avoid scanning dashboards/BIBLIOGRAFIA.md itself
        if path.resolve() == BIB_FILE.resolve():
            continue
            
        try:
            file_refs = extract_from_file(path)
            if file_refs:
                all_refs.extend(file_refs)
        except Exception as e:
            print(f"⚠️ Erro ao processar bibliografia de {path.name}: {e}")
            
    print(f"📚 Encontradas {len(all_refs)} referências bibliográficas!")
    
    # Organiza e atualiza o arquivo dashboards/BIBLIOGRAFIA.md
    if not BIB_FILE.exists():
        print("⚠️ dashboards/BIBLIOGRAFIA.md não encontrado. Criando um novo.")
        
    base_text = """# Como Referenciar & Bibliografia no Will-obsidian

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

---

## 📚 Bibliografia Compilada do Vault
*(Gerado automaticamente pelo script de manutenção)*

| Nota de Origem | Canal / Tipo | Referência Bibliográfica / Link |
| :--- | :--- | :--- |
"""
    
    for r in all_refs:
        rel_path = r['source'].relative_to(ROOT).as_posix()
        file_link = f"[[{rel_path}\\|{r['source'].stem}]]"
        ref_type = r['type']
        detail = r['detail'].replace("|", "\\|") # sanitize table separator
        
        base_text += f"| {file_link} | `{ref_type}` | {detail} |\n"
        
    BIB_FILE.write_text(base_text, encoding='utf-8')
    print(f"✅ Arquivo de Bibliografia dashboards/BIBLIOGRAFIA.md atualizado com sucesso!")

if __name__ == '__main__':
    main()
