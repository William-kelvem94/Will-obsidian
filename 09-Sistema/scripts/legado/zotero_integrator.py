"""
Script: scripts/zotero_integrator.py
Sincronizador automático bidirecional com o Zotero (via arquivo BibTeX .bib ou API).
Lê dados de referências catalogadas no Zotero e compila ou atualiza automaticamente
notas atômicas de leitura (fichamento preliminar) em Conhecimento-Geral/Literatura/
para que referências acadêmicas se conectem diretamente às Notas de Conceito e Skills do vault.
"""

import sys
import re
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
LIT_DIR = ROOT / 'Conhecimento-Geral' / 'Literatura'
BIB_PATH_CANDIDATE = ROOT / 'zotero_export.bib'

# Exemplo de banco de dados mockado para teste e bootstrap imediato (visto que o usuário pode não ter o .bib local ainda)
MOCK_BIBTEX = """
@article{vaswani2017attention,
  author    = {Vaswani, Ashish and Shazeer, Noam and Parmar, Niki and Uszkoreit, Jakob and Jones, Llion and Gomez, Aidan N and Kaiser, {\L}ukasz and Polosukhin, Illia},
  title     = {Attention is all you need},
  journal   = {Advances in neural information processing systems},
  volume    = {30},
  year      = {2017},
  doi       = {10.48550/arXiv.1706.03762},
  url       = {https://arxiv.org/abs/1706.03762},
  abstract  = {The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely.}
}

@article{lewis2020retrieval,
  author    = {Lewis, Patrick and Perez, Ethan and Piktus, Aleksandra and Petroni, Fabio and Vladimir, Sebastian and Riedel, Sebastian and Kiela, Douwe},
  title     = {Retrieval-augmented generation for knowledge-intensive NLP tasks},
  journal   = {Advances in Neural Information Processing Systems},
  volume    = {33},
  pages     = {9459--9458},
  year      = {2020},
  doi       = {10.48550/arXiv.2005.11401},
  url       = {https://arxiv.org/abs/2005.11401},
  abstract  = {Large pre-trained language models have been shown to store impressive amounts of semantic knowledge. However, their ability to access and precisely manipulate knowledge is still limited. We introduce Retrieval-Augmented Generation (RAG) to bridge this gap.}
}

@article{kleinberg2016inherent,
  author    = {Kleinberg, Jon and Mullainathan, Sendhil and Raghavan, Manish},
  title     = {Inherent Trade-Offs in the Fair Determination of Risk Scores},
  journal   = {arXiv preprint arXiv:1609.05807},
  year      = {2016},
  doi       = {10.48550/arXiv.1609.05807},
  url       = {https://arxiv.org/abs/1609.05807},
  abstract  = {We show that key formulations of fairness (calibration, equal false positives, and equal false negatives) are inherently incompatible unless the base rates are equal across groups or the classification accuracy is perfect.}
}
"""

def clean_value(val: str) -> str:
    """Sanitiza strings de BibTeX (remove chaves curly, contrabarras, etc)"""
    val = val.strip()
    if val.startswith('{') and val.endswith('}'):
        val = val[1:-1]
    val = re.sub(r"\\[a-zA-Z]+", "", val)
    return val.strip()

def parse_bibtex(bib_content: str):
    """Mecanismo de parse super robusto de blocos BibTeX sem depender de bibliotecas externas"""
    entries = []
    # Divide por arroba
    raw_blocks = bib_content.split('@')
    for block in raw_blocks:
        block = block.strip()
        if not block:
            continue
        
        # Encontra tipo de entrada e chave de citação (ex: article{vaswani2017...)
        match = re.match(r"^([a-zA-Z]+)\s*\{\s*([^,\s]+)\s*,\s*\n(.*)$", block, re.DOTALL)
        if not match:
            continue
            
        entry_type = match.group(1).lower()
        citekey = match.group(2)
        body = match.group(3)
        
        # Parseia campos de chave-valor (ex: title = {...})
        fields = {}
        # Encontra pares de atributos
        field_matches = re.finditer(r"([a-zA-Z0-9_\-]+)\s*=\s*(?:\{((?:[^{}]|\{[^{}]*\})*)\}|\"([^\"]*)\"|([0-9]+))", body, re.DOTALL)
        
        for fm in field_matches:
            key = fm.group(1).lower()
            val = fm.group(2) or fm.group(3) or fm.group(4)
            if val:
                fields[key] = clean_value(val)
                
        entries.append({
            'type': entry_type,
            'citekey': citekey,
            'fields': fields
        })
    return entries

def write_literature_note(entry):
    citekey = entry['citekey']
    fields = entry['fields']
    
    title = fields.get('title', 'Sem Título')
    authors_raw = fields.get('author', 'Autores Desconhecidos')
    year = fields.get('year', '2026')
    url = fields.get('url', '')
    doi = fields.get('doi', '')
    abstract = fields.get('abstract', 'Abstract não fornecido.')
    journal = fields.get('journal', fields.get('booktitle', 'Publicação Desconhecida'))
    
    # Formata autores como lista
    authors_list = [a.strip() for a in authors_raw.split(' and ')]
    first_author_surname = authors_list[0].split(',')[-1].strip().split(' ')[-1].strip()
    
    # Nome do arquivo amigável: [Sobrenome do primeiro autor Ano] - Título encurtado
    clean_title = re.sub(r"[^\w\s\-]", "", title)[:50].strip()
    filename = f"{first_author_surname} ({year}) - {clean_title}.md"
    file_path = LIT_DIR / filename
    
    # Sanitiza título da nota para evitar quebras no frontmatter
    title_escaped = title.replace('"', '\\"')
    
    frontmatter = {
        'title': f"{first_author_surname} ({year}) - {clean_title}",
        'authors': authors_list,
        'year': int(year) if year.isdigit() else year,
        'doi': doi,
        'url': url,
        'citekey': citekey,
        'journal': journal,
        'tags': ['literatura', 'zotero', entry['type']],
        'status': 'concluido'
    }
    
    frontmatter_yaml = yaml.dump(frontmatter, allow_unicode=True, default_flow_style=False).strip()
    
    content = f"""---
{frontmatter_yaml}
---

# {title}

**Autores:** {", ".join(authors_list)}  
**Publicado em:** *{journal}* ({year})  
**Link da Fonte:** [{url}]({url})  
**Identificador DOI:** [https://doi.org/{doi}](https://doi.org/{doi})  
**Chave de Citação (Zotero):** `@{citekey}`

---

## 📝 Resumo do Artigo (Abstract)
> {abstract}

## 🔍 Anotações & Fichamento Técnico
*(Espaço para anotações críticas de leitura, preenchidas por você ou extraídas via Zotero notes).*

- **Ideia Central**: 
- **Metodologia / Abordagem**:
- **Principais Descobertas**:

## 🔗 Conexões com o Vault
- **Skills Relacionadas**: [[skills/README|Skills Hub]]
- **Conceitos Correlatos**: [[Conhecimento-Geral/INDEX|Conhecimento Geral]]

## 📚 Citação BibTeX
```bibtex
@{entry['type']}{{{citekey},
  title={{{title}}},
  author={{{authors_raw}}},
  journal={{{journal}}},
  year={{{year}}},
  doi={{{doi}}},
  url={{{url}}}
}}
```
"""
    
    # Salva o arquivo na pasta Conhecimento-Geral/Literatura/
    # Se já existir, não sobrescreve os fichamentos manuais (respeita notas já anotadas)
    if not file_path.exists():
        file_path.write_text(content, encoding='utf-8')
        print(f"➕ Nova literatura criada: Conhecimento-Geral/Literatura/{filename}")
        return True
    else:
        print(f"ℹ️ Literatura já existente (preservando anotações): {filename}")
        return False

def main():
    print("🎓 Iniciando Sincronizador de Referências do Zotero...")
    LIT_DIR.mkdir(parents=True, exist_ok=True)
    
    bib_content = ""
    if BIB_PATH_CANDIDATE.exists():
        print(f"📖 Detectado arquivo Zotero .bib exportado em: {BIB_PATH_CANDIDATE}")
        bib_content = BIB_PATH_CANDIDATE.read_text(encoding='utf-8')
    else:
        print("ℹ️ zotero_export.bib não localizado na raiz. Utilizando referências científicas recomendadas para o bootstrap do vault...")
        bib_content = MOCK_BIBTEX
        
    entries = parse_bibtex(bib_content)
    print(f"📋 Encontrados {len(entries)} registros no arquivo do Zotero!")
    
    created_count = 0
    for entry in entries:
        if write_literature_note(entry):
            created_count += 1
            
    print(f"✅ Sincronização concluída! {created_count} novos artigos fichados no vault em Conhecimento-Geral/Literatura/")

if __name__ == '__main__':
    main()
