"""
Script: scripts/scan_gaps.py
Percorre todos os .md do vault, extrai tags/áreas do frontmatter e compara com
a taxonomia definida em TAXONOMY.md. Gera/atualiza GAPS.md com skills/áreas
que estão na taxonomia mas não têm nota dedicada no vault.

v2.1 — Inteligente: verifica subdiretórios, normaliza nomes (acentos, markdown,
emoji), ignora categorias-pai cobertas por notas filhas, remove duplicatas.

Uso: python scripts/scan_gaps.py
"""
import yaml, re, unicodedata
from pathlib import Path

VAULT = Path(__file__).resolve().parents[1]
TAXONOMY = VAULT / 'TAXONOMY.md'
GAPS = VAULT / 'GAPS.md'

def strip_accents(s: str) -> str:
    """Remove acentos e diacríticos (ex: 'física' -> 'fisica')"""
    nfkd = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in nfkd if not unicodedata.combining(c))

def normalize(name: str) -> str:
    """Remove markdown bold/italic, emojis, 🆕 markers, parenthetical notes, trim spaces"""
    name = re.sub(r'\*{1,2}(.*?)\*{1,2}', r'\1', name)  # **bold** and *italic*
    name = re.sub(r'[\U0001F300-\U0001FAFF]', '', name)  # emojis
    name = re.sub(r'\(.*?\)', '', name)  # parenthetical
    name = name.replace('🆕', '').replace('🆕', '').replace('🆕', '')
    name = strip_accents(name)
    return name.strip()

def extract_taxonomy_sections(text):
    sections = {}
    current_section = None
    for line in text.splitlines():
        m = re.match(r'^## (\S+)', line)
        if m:
            current_section = m.group(1)
            sections[current_section] = []
        elif current_section and line.startswith('- '):
            raw = line.lstrip('- ').strip()
            cleaned = normalize(raw)
            if cleaned and cleaned != raw:
                sections[current_section].append((raw, cleaned))
            elif cleaned:
                sections[current_section].append((raw, cleaned))
    return sections

def extract_all_tags_and_dirs():
    """Extract all tags from frontmatter, and list all directory names"""
    tags_set = set()
    dirs_set = set()
    for f in VAULT.rglob('*.md'):
        if 'node_modules' in str(f):
            continue
        dirs_set.add(f.parent.name.lower())
        try:
            with f.open(encoding='utf-8') as fp:
                lines = list(fp)
            if lines and lines[0].strip() == '---':
                fm_lines = []
                for l in lines[1:]:
                    if l.strip() == '---':
                        break
                    fm_lines.append(l)
                meta = yaml.safe_load(''.join(fm_lines)) or {}
                tags = meta.get('tags', [])
                if isinstance(tags, list):
                    for t in tags:
                        tags_set.add(strip_accents(t.strip().lower()))
                elif isinstance(tags, str):
                    tags_set.add(strip_accents(tags.strip().lower()))
        except Exception:
            continue
    return tags_set, dirs_set

def has_notes_in_subdir(item_clean: str) -> bool:
    """Check if a subdirectory matching the item name exists and has notes"""
    # Check direct subdirectory
    for d in VAULT.rglob('*/'):
        if not d.is_dir():
            continue
        if 'node_modules' in str(d):
            continue
        if item_clean.lower().replace('-', ' ').replace('  ', ' ') in d.name.lower().replace('-', ' ').replace('_', ' '):
            md_count = len(list(d.rglob('*.md')))
            if md_count > 0:
                return True
    return False

def main():
    tax_text = TAXONOMY.read_text(encoding='utf-8')
    tax_sections = extract_taxonomy_sections(tax_text)
    all_tags, all_dirs = extract_all_tags_and_dirs()

    seen = set()
    gaps = []
    for section, items in tax_sections.items():
        for raw_item, clean_item in items:
            if clean_item.lower() in seen:
                continue  # skip duplicate
            seen.add(clean_item.lower())

            item_lower = strip_accents(clean_item.lower())

            # Check 1: is it in tags? (with hyphen/space normalization, accent-free)
            item_norm = item_lower.replace('-', ' ').replace('_', ' ')
            found_in_tags = any(
                item_lower in tag or tag in item_lower or
                (item_norm in tag.replace('-', ' ').replace('_', ' '))
                for tag in all_tags
            )

            # Check 2: is there a file whose name contains this?
            has_named_note = any(
                item_lower in f.stem.lower()
                for f in VAULT.rglob('*.md')
                if 'node_modules' not in str(f)
            )

            # Check 3: is there a subdirectory with notes?
            has_subdir = has_notes_in_subdir(clean_item)

            # Check 4: break compound names (e.g., "Python / TypeScript" -> check each part)
            compound_parts = [p.strip() for p in re.split(r'[/,]', clean_item)]
            any_part_found = False
            for part in compound_parts:
                part_lower = part.lower()
                if any(part_lower in tag for tag in all_tags):
                    any_part_found = True
                    break
                if has_notes_in_subdir(part):
                    any_part_found = True
                    break

            if not (found_in_tags or has_named_note or has_subdir or any_part_found):
                gaps.append(f'- [ ] **{raw_item}** (gap real — sem nota, tag ou diretório dedicado)')

    gap_content = f"""# GAPS DE CONHECIMENTO E SKILLS

## Skills/Áreas sem nota dedicada (scaneado em {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')})

{chr(10).join(gaps) if gaps else '- *Nenhum gap detectado! Taxonomia 100% coberta.* 🎉'}

## Sugestões de colaboração
- Sugira relatos práticos!
- Anexe links de leitura e exemplos comunitários para cada área.
---
*Este arquivo é atualizado automaticamente pelo script `scripts/scan_gaps.py`.*
"""
    GAPS.write_text(gap_content, encoding='utf-8')
    print(f'GAPS.md atualizado com {len(gaps)} gaps reais encontrados!')

if __name__ == '__main__':
    main()
