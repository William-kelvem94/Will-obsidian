#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import hashlib
import re
import argparse

# Mapeamento de pastas para consolidação de segundo nível
FOLDER_MAPPING = {
    # Eliminar aninhamentos duplos
    "02-JARVIS/JARVIS": "02-JARVIS",
    "03-Projetos/Projetos": "03-Projetos",
    "05-Skills/skills": "05-Skills",
    "06-Will-Pessoal/Will-Pessoal": "06-Will-Pessoal",
    
    # Fundir Interfaces e Hubs
    "10-Interfaces/dashboards": "01-Hubs/dashboards",
    "10-Interfaces/Canvases": "01-Hubs/Canvases",
    "10-Interfaces/web-ui": "01-Hubs/web-ui",
    
    # Limpar a pasta raw
    "11-Dados-Brutos/raw/Clippings": "11-Dados-Brutos/Clippings",
    "11-Dados-Brutos/raw/Bases": "11-Dados-Brutos/Bases",
    
    # Categorizar Conhecimentos-Gerais
    "04-Conhecimentos/Conhecimentos-Gerais/01-IA": "04-Conhecimentos/01-IA-e-Agentes",
    "04-Conhecimentos/Conhecimentos-Gerais/02-Engenharia-Software": "04-Conhecimentos/02-Engenharia-de-Software",
    "04-Conhecimentos/Conhecimentos-Gerais/03-Estudos": "04-Conhecimentos/06-Estudos-e-Aprendizagem",
    "04-Conhecimentos/Conhecimentos-Gerais/04-Produtividade": "04-Conhecimentos/08-Vida-Pratica/Produtividade",
    "04-Conhecimentos/Conhecimentos-Gerais/05-Dados": "04-Conhecimentos/03-Dados-e-Analytics",
    "04-Conhecimentos/Conhecimentos-Gerais/06-Habilidades": "04-Conhecimentos/06-Estudos-e-Aprendizagem/Habilidades",
    "04-Conhecimentos/Conhecimentos-Gerais/07-Seguranca": "04-Conhecimentos/04-Seguranca-e-Redes/Seguranca",
    "04-Conhecimentos/Conhecimentos-Gerais/08-Redes": "04-Conhecimentos/04-Seguranca-e-Redes/Redes",
    "04-Conhecimentos/Conhecimentos-Gerais/09-Produto-UX": "04-Conhecimentos/05-Produto-UX-e-Carreira/Produto-UX",
    "04-Conhecimentos/Conhecimentos-Gerais/10-Matematica": "04-Conhecimentos/06-Estudos-e-Aprendizagem/Matematica",
    "04-Conhecimentos/Conhecimentos-Gerais/11-Carreira": "04-Conhecimentos/05-Produto-UX-e-Carreira/Carreira",
    "04-Conhecimentos/Conhecimentos-Gerais/12-Saude-Rotina": "04-Conhecimentos/08-Vida-Pratica/Saude-Rotina",
    "04-Conhecimentos/Conhecimentos-Gerais/13-Financas": "04-Conhecimentos/08-Vida-Pratica/Financas",
    "04-Conhecimentos/Conhecimentos-Gerais/14-Comunicacao": "04-Conhecimentos/08-Vida-Pratica/Comunicacao",
    "04-Conhecimentos/Conhecimentos-Gerais/15-Documentacao": "04-Conhecimentos/00-Mapas-e-Ontologia/Documentacao",
    "04-Conhecimentos/Conhecimentos-Gerais/16-Humanidades": "04-Conhecimentos/07-Humanidades",
    "04-Conhecimentos/Conhecimentos-Gerais/99-Templates": "04-Conhecimentos/99-Templates",
    
    # Categorizar Knowledge-Base
    "04-Conhecimentos/Knowledge-Base/IA-Aplicada": "04-Conhecimentos/01-IA-e-Agentes",
    "04-Conhecimentos/Knowledge-Base/BI-Analytics": "04-Conhecimentos/03-Dados-e-Analytics",
    "04-Conhecimentos/Knowledge-Base/Saude-Mental": "04-Conhecimentos/08-Vida-Pratica/Saude-Mental",
    "04-Conhecimentos/Knowledge-Base/Automacao": "04-Conhecimentos/01-IA-e-Agentes/Automacao",
    "04-Conhecimentos/Knowledge-Base/Experimentacao": "04-Conhecimentos/06-Estudos-e-Aprendizagem/Experimentacao",
    "04-Conhecimentos/Knowledge-Base/Futurologia": "04-Conhecimentos/01-IA-e-Agentes/Futurologia",
    "04-Conhecimentos/Knowledge-Base/LGPD-Privacidade": "04-Conhecimentos/04-Seguranca-e-Redes/LGPD-Privacidade"
}

FILE_MAPPING = {
    # Interfaces
    "10-Interfaces/Painel-Cockpit.md": "01-Hubs/Painel-Cockpit.md",
    "10-Interfaces/README.md": "01-Hubs/README-LEGACY-Interfaces.md",
    
    # Knowledge-Base
    "04-Conhecimentos/Knowledge-Base/IA-APLICADA.md": "04-Conhecimentos/01-IA-e-Agentes/IA-Aplicada.md",
    "04-Conhecimentos/Knowledge-Base/BI-ANALYTICS.md": "04-Conhecimentos/03-Dados-e-Analytics/BI-Analytics.md",
    "04-Conhecimentos/Knowledge-Base/SAUDE-MENTAL.md": "04-Conhecimentos/08-Vida-Pratica/Saude-Mental.md",
    "04-Conhecimentos/Knowledge-Base/AUTOMACAO.md": "04-Conhecimentos/01-IA-e-Agentes/Automacao.md",
    "04-Conhecimentos/Knowledge-Base/EXPERIMENTACAO.md": "04-Conhecimentos/06-Estudos-e-Aprendizagem/Experimentacao.md",
    "04-Conhecimentos/Knowledge-Base/FUTUROLOGIA.md": "04-Conhecimentos/01-IA-e-Agentes/Futurologia.md",
    "04-Conhecimentos/Knowledge-Base/LGPD-PRIVACIDADE.md": "04-Conhecimentos/04-Seguranca-e-Redes/LGPD-Privacidade.md",
    "04-Conhecimentos/Knowledge-Base/DATA-TOKEN-GOVERNANCE.md": "04-Conhecimentos/03-Dados-e-Analytics/DATA-TOKEN-GOVERNANCE.md",
    "04-Conhecimentos/Knowledge-Base/TOKEN-ECONOMY.md": "04-Conhecimentos/03-Dados-e-Analytics/TOKEN-ECONOMY.md",
    "04-Conhecimentos/Knowledge-Base/TOKEN-SHORTHAND.md": "04-Conhecimentos/03-Dados-e-Analytics/TOKEN-SHORTHAND.md",
    "04-Conhecimentos/Knowledge-Base/README.md": "04-Conhecimentos/README-LEGACY-Knowledge-Base.md",
    
    # Conhecimentos-Gerais root files
    "04-Conhecimentos/Conhecimentos-Gerais/00-Como-usar-este-vault-com-IA.md": "04-Conhecimentos/00-Mapas-e-Ontologia/00-Como-usar-este-vault-com-IA.md",
    "04-Conhecimentos/Conhecimentos-Gerais/00-Mapa-de-Lacunas-e-Roadmap.md": "04-Conhecimentos/00-Mapas-e-Ontologia/00-Mapa-de-Lacunas-e-Roadmap.md",
    "04-Conhecimentos/Conhecimentos-Gerais/00-Ontologia-de-Conhecimento-para-IA.md": "04-Conhecimentos/00-Mapas-e-Ontologia/00-Ontologia-de-Conhecimento-para-IA.md",
    "04-Conhecimentos/Conhecimentos-Gerais/INDEX.md": "04-Conhecimentos/INDEX-LEGACY.md",
    "04-Conhecimentos/Conhecimentos-Gerais/README.md": "04-Conhecimentos/README-LEGACY-Conhecimentos-Gerais.md"
}

WIKILINK_RE = re.compile(r'(\[\[)([^\]|#\n]+)(#[^\]|\n]+)?(\|[^\]\n]+)?(\]\])')
MARKDOWN_LINK_RE = re.compile(r'(\[)([^\]\n]*)(\]\()([^)\n]+)(\))')

# Lista de pastas e padrões de substituição em aspas para Dataview
QUOTED_PATTERNS = [
    "02-JARVIS/JARVIS", "03-Projetos/Projetos", "05-Skills/skills", "06-Will-Pessoal/Will-Pessoal",
    "10-Interfaces/dashboards", "10-Interfaces/Canvases", "10-Interfaces/web-ui", "11-Dados-Brutos/raw",
    "04-Conhecimentos/Conhecimentos-Gerais", "04-Conhecimentos/Knowledge-Base", "10-Interfaces"
]
QUOTED_PATH_RE = re.compile(r'(["\'])(' + '|'.join(re.escape(p) for p in QUOTED_PATTERNS) + r')(/)?')

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def get_new_path(rel_path):
    rel_path = rel_path.replace('\\', '/')
    
    # 1. Check exact file mapping
    if rel_path in FILE_MAPPING:
        return FILE_MAPPING[rel_path]
        
    # 2. Check folder mappings
    for src_folder, dst_folder in sorted(FOLDER_MAPPING.items(), key=lambda x: len(x[0]), reverse=True):
        if rel_path.startswith(src_folder + '/'):
            return dst_folder + rel_path[len(src_folder):]
            
    # 3. Dynamic Prefix stripping
    prefixes_to_strip = {
        "02-JARVIS/JARVIS/": "02-JARVIS/",
        "03-Projetos/Projetos/": "03-Projetos/",
        "05-Skills/skills/": "05-Skills/",
        "06-Will-Pessoal/Will-Pessoal/": "06-Will-Pessoal/",
        "11-Dados-Brutos/raw/": "11-Dados-Brutos/",
        "10-Interfaces/dashboards/": "01-Hubs/dashboards/",
        "10-Interfaces/Canvases/": "01-Hubs/Canvases/",
        "10-Interfaces/web-ui/": "01-Hubs/web-ui/"
    }
    for prefix, target in prefixes_to_strip.items():
        if rel_path.startswith(prefix):
            return target + rel_path[len(prefix):]
            
    return None

def get_legacy_aliases(rel_path):
    aliases = []
    
    replacements = [
        ("04-Conhecimentos/Conhecimentos-Gerais/", "Conhecimentos-Gerais/"),
        ("04-Conhecimentos/07-Humanidades/", "Conhecimento-Geral/"),
        ("04-Conhecimentos/Knowledge-Base/", "Knowledge-Base/"),
        ("04-Conhecimentos/wiki/", "wiki/"),
        ("02-JARVIS/JARVIS/", "JARVIS/"),
        ("03-Projetos/Projetos/", "Projetos/"),
        ("05-Skills/skills/", "skills/"),
        ("06-Will-Pessoal/Will-Pessoal/", "Will-Pessoal/"),
        ("01-Hubs/dashboards/", "dashboards/"),
        ("01-Hubs/Canvases/", "Canvases/"),
        ("01-Hubs/web-ui/", "web-ui/"),
        ("11-Dados-Brutos/raw/", "raw/"),
        ("11-Dados-Brutos/Bases/", "Bases/"),
        ("11-Dados-Brutos/Clippings/", "Clippings/")
    ]
    
    for current_prefix, legacy_prefix in replacements:
        if rel_path.startswith(current_prefix):
            aliases.append(legacy_prefix + rel_path[len(current_prefix):])
            
    return aliases

def build_mappings(root_dir):
    old_to_new = {}
    
    for dirpath, _, filenames in os.walk(root_dir):
        skip_dirs = {'.git', '.github', '.obsidian', '.cursor', '.continue', '.openclaude', '.agents'}
        if any(part in skip_dirs for part in os.path.split(dirpath)):
            continue
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')
            
            new_path = get_new_path(rel_path)
            if new_path:
                old_to_new[rel_path] = new_path
                aliases = get_legacy_aliases(rel_path)
                for alias in aliases:
                    old_to_new[alias] = new_path
            else:
                aliases = get_legacy_aliases(rel_path)
                for alias in aliases:
                    old_to_new[alias] = rel_path
                    
    return old_to_new

def resolve_and_update_link(target, source_new_rel, old_to_new, new_to_current):
    if '#' in target:
        path_part, anchor_part = target.split('#', 1)
        anchor_part = '#' + anchor_part
    else:
        path_part = target
        anchor_part = ''
        
    path_part_norm = path_part.replace('\\', '/')
    
    if path_part_norm.startswith(('http://', 'https://', 'mailto:', 'file:')):
        return None
        
    source_current_rel = new_to_current.get(source_new_rel, source_new_rel)
    source_current_dir = os.path.dirname(source_current_rel)
    source_new_dir = os.path.dirname(source_new_rel)
    
    is_relative = path_part_norm.startswith('.')
    
    new_path_part = None
    
    if is_relative:
        resolved_current_target = os.path.normpath(os.path.join(source_current_dir, path_part_norm)).replace('\\', '/')
        matched_old = None
        matched_new = None
        
        if resolved_current_target in old_to_new:
            matched_old = resolved_current_target
            matched_new = old_to_new[resolved_current_target]
        else:
            if not resolved_current_target.lower().endswith('.md'):
                resolved_with_ext = resolved_current_target + '.md'
                if resolved_with_ext in old_to_new:
                    matched_old = resolved_with_ext
                    matched_new = old_to_new[resolved_with_ext][:-3]
                    
        if matched_new:
            new_target_file = matched_new
            if matched_old.endswith('.md') and not new_target_file.endswith('.md'):
                new_target_file += '.md'
            rel_path = os.path.relpath(new_target_file, source_new_dir).replace('\\', '/')
            if not path_part_norm.lower().endswith('.md') and rel_path.endswith('.md'):
                rel_path = rel_path[:-3]
            new_path_part = rel_path
    else:
        matched_new = None
        if path_part_norm in old_to_new:
            matched_new = old_to_new[path_part_norm]
        else:
            # Check prefix matching on FOLDER_MAPPING and dynamic prefixes
            for src_folder, dst_folder in FOLDER_MAPPING.items():
                if path_part_norm == src_folder:
                    matched_new = dst_folder
                    break
                elif path_part_norm.startswith(src_folder + '/'):
                    matched_new = dst_folder + path_part_norm[len(src_folder):]
                    break
                    
            if not matched_new:
                # Check file extension fallback
                if not path_part_norm.lower().endswith('.md'):
                    with_ext = path_part_norm + '.md'
                    if with_ext in old_to_new:
                        matched_new = old_to_new[with_ext][:-3]
                    else:
                        for src_folder, dst_folder in FOLDER_MAPPING.items():
                            if with_ext.startswith(src_folder + '/'):
                                matched_new = (dst_folder + with_ext[len(src_folder):])[:-3]
                                break
                                
        if matched_new:
            new_path_part = matched_new
            
    if new_path_part is not None:
        return new_path_part + anchor_part
    return None

def update_links_in_file(filepath, root_dir, old_to_new, new_to_current, dry_run=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False
        
    rel_path_file = os.path.relpath(filepath, root_dir).replace('\\', '/')
    if dry_run:
        source_current_rel = rel_path_file
        source_new_rel = old_to_new.get(source_current_rel, source_current_rel)
    else:
        source_new_rel = rel_path_file
        source_current_rel = new_to_current.get(source_new_rel, source_new_rel)
        
    modified = False
    
    # 1. Update Wikilinks
    def wikilink_replacer(match):
        nonlocal modified
        g1, g2, g3, g4, g5 = match.groups()
        target = g2
        anchor = g3 if g3 else ''
        display = g4 if g4 else ''
        
        full_target = target + anchor
        new_target = resolve_and_update_link(full_target, source_new_rel, old_to_new, new_to_current)
        if new_target:
            modified = True
            if '#' in new_target:
                p, a = new_target.split('#', 1)
                a = '#' + a
            else:
                p, a = new_target, ''
            return f"{g1}{p}{a}{display}{g5}"
        return match.group(0)
        
    new_content = WIKILINK_RE.sub(wikilink_replacer, content)
    
    # 2. Update Markdown Links
    def markdown_link_replacer(match):
        nonlocal modified
        g1, g2, g3, g4, g5 = match.groups()
        target = g4
        new_target = resolve_and_update_link(target, source_new_rel, old_to_new, new_to_current)
        if new_target:
            modified = True
            return f"{g1}{g2}{g3}{new_target}{g5}"
        return match.group(0)
        
    new_content = MARKDOWN_LINK_RE.sub(markdown_link_replacer, new_content)
    
    # 3. Update Quoted Paths (for Dataview etc.)
    # Ex: "10-Interfaces/dashboards/" -> "01-Hubs/dashboards/"
    # Ex: "02-JARVIS/JARVIS/" -> "02-JARVIS/"
    def quoted_replacer(match):
        nonlocal modified
        quote = match.group(1)
        path = match.group(2)
        slash = match.group(3) if match.group(3) else ''
        
        # Determine the new path
        new_p = get_new_path(path)
        if not new_p:
            # Fallback for prefixes to strip
            prefixes_to_strip = {
                "02-JARVIS/JARVIS": "02-JARVIS",
                "03-Projetos/Projetos": "03-Projetos",
                "05-Skills/skills": "05-Skills",
                "06-Will-Pessoal/Will-Pessoal": "06-Will-Pessoal",
                "11-Dados-Brutos/raw": "11-Dados-Brutos",
                "10-Interfaces/dashboards": "01-Hubs/dashboards",
                "10-Interfaces/Canvases": "01-Hubs/Canvases",
                "10-Interfaces/web-ui": "01-Hubs/web-ui",
                "10-Interfaces": "01-Hubs"
            }
            new_p = prefixes_to_strip.get(path)
            
        if new_p:
            modified = True
            return f"{quote}{new_p}{slash}"
        return match.group(0)
        
    new_content = QUOTED_PATH_RE.sub(quoted_replacer, new_content)
    
    if modified:
        if not dry_run:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
        return True
    return False

def find_all_markdown_files(root_dir):
    md_files = []
    for dirpath, _, filenames in os.walk(root_dir):
        skip_dirs = {'.git', '.github', '.obsidian', '.cursor', '.continue', '.openclaude', '.agents'}
        if any(part in skip_dirs for part in os.path.split(dirpath)):
            continue
        for filename in filenames:
            if filename.endswith('.md'):
                md_files.append(os.path.join(dirpath, filename))
    return md_files

def main():
    parser = argparse.ArgumentParser(description="Consolida o vault Obsidian do Will.")
    parser.add_argument("--apply", action="store_true", help="Aplica as mudanças físicas e atualizações de links.")
    args = parser.parse_args()
    
    dry_run = not args.apply
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    print(f"=== Consolidação Profunda do Vault ===")
    print(f"Diretório raiz: {root_dir}")
    print(f"Modo: {'APLICAR' if args.apply else 'SIMULAÇÃO (dry-run)'}")
    
    # 1. Build mappings
    old_to_new = build_mappings(root_dir)
    
    # Build current_to_new map for files that actually exist right now
    current_to_new = {}
    for old_rel, new_rel in old_to_new.items():
        old_abs = os.path.join(root_dir, old_rel.replace('/', os.sep))
        if os.path.exists(old_abs) and os.path.isfile(old_abs):
            current_to_new[old_rel] = new_rel
            
    new_to_current = {v: k for k, v in current_to_new.items()}
    
    # 2. Plan physical moves
    moves_planned = []
    remove_duplicates = []
    
    for current_rel, new_rel in sorted(current_to_new.items()):
        old_abs = os.path.join(root_dir, current_rel.replace('/', os.sep))
        new_abs = os.path.join(root_dir, new_rel.replace('/', os.sep))
        
        if old_abs == new_abs:
            continue
            
        if os.path.exists(new_abs):
            old_hash = get_file_hash(old_abs)
            new_hash = get_file_hash(new_abs)
            if old_hash == new_hash:
                remove_duplicates.append(old_abs)
            else:
                new_dir = os.path.dirname(new_abs)
                base, ext = os.path.splitext(os.path.basename(new_abs))
                new_legacy_name = f"{base}-LEGACY{ext}"
                new_legacy_abs = os.path.join(new_dir, new_legacy_name)
                moves_planned.append((old_abs, new_legacy_abs, True))
        else:
            moves_planned.append((old_abs, new_abs, False))
            
    # 3. Execute / Simulate physical moves
    print(f"\n--- Movimentação Física (Fase 2) ---")
    for src, dst, is_conflict in moves_planned:
        src_rel = os.path.relpath(src, root_dir).replace('\\', '/')
        dst_rel = os.path.relpath(dst, root_dir).replace('\\', '/')
        print(f"{'[CONFLITO -> RENOMEADO] ' if is_conflict else '[MOVER] '}{src_rel} -> {dst_rel}")
        if not dry_run:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.move(src, dst)
            
    for src in remove_duplicates:
        src_rel = os.path.relpath(src, root_dir).replace('\\', '/')
        print(f"[REMOVER DUPLICADO IDÊNTICO] {src_rel}")
        if not dry_run:
            os.remove(src)
            
    # 4. Scan and update links in all markdown files
    md_files = find_all_markdown_files(root_dir)
    print(f"\n--- Atualização de Links (Consolidação) ({len(md_files)} arquivos analisados) ---")
    
    updated_files_count = 0
    for md_file in md_files:
        rel_path = os.path.relpath(md_file, root_dir).replace('\\', '/')
        is_updated = update_links_in_file(md_file, root_dir, old_to_new, new_to_current, dry_run)
        if is_updated:
            print(f"[LINK CONSOLIDADO] {rel_path}")
            updated_files_count += 1
            
    print(f"\nTotal de arquivos com links atualizados: {updated_files_count}")
    
    # 5. Cleanup empty legacy directories
    # Include all source folders to clean up
    folders_to_cleanup = [
        "02-JARVIS/JARVIS",
        "03-Projetos/Projetos",
        "05-Skills/skills",
        "06-Will-Pessoal/Will-Pessoal",
        "10-Interfaces/dashboards",
        "10-Interfaces/Canvases",
        "10-Interfaces/web-ui",
        "10-Interfaces",
        "11-Dados-Brutos/raw/Clippings",
        "11-Dados-Brutos/raw/Bases",
        "11-Dados-Brutos/raw",
        "04-Conhecimentos/Conhecimentos-Gerais",
        "04-Conhecimentos/Knowledge-Base"
    ]
    print(f"\n--- Limpeza de Pastas Vazias (Fase 2) ---")
    for folder in sorted(folders_to_cleanup, key=len, reverse=True):
        path = os.path.join(root_dir, folder)
        if os.path.exists(path) and os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path, topdown=False):
                valid_files = [f for f in filenames if f not in ('.DS_Store', 'desktop.ini')]
                if not dirnames and not valid_files:
                    dir_rel = os.path.relpath(dirpath, root_dir).replace('\\', '/')
                    print(f"[REMOVER PASTA VAZIA] {dir_rel}")
                    if not dry_run:
                        try:
                            os.rmdir(dirpath)
                        except Exception as e:
                            print(f"Erro ao remover {dir_rel}: {e}")

if __name__ == "__main__":
    main()
