#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import re

# Arquivos legados para mover para 08-Arquivo
LEGACY_FILES_MAPPING = {
    "04-Conhecimentos/INDEX-LEGACY.md": "08-Arquivo/INDEX-LEGACY.md",
    "04-Conhecimentos/README-LEGACY-Conhecimentos-Gerais.md": "08-Arquivo/README-LEGACY-Conhecimentos-Gerais.md",
    "04-Conhecimentos/README-LEGACY-Knowledge-Base.md": "08-Arquivo/README-LEGACY-Knowledge-Base.md",
    "05-Skills/README-LEGACY.md": "08-Arquivo/README-LEGACY-Skills.md"
}

# Pastas vazias para remover
EMPTY_FOLDERS = [
    "04-Conhecimentos/Knowledge-Base",
    "04-Conhecimentos/wiki"
]

WIKILINK_RE = re.compile(r'(\[\[)([^\]|#\n]+)(#[^\]|\n]+)?(\|[^\]\n]+)?(\]\])')
MARKDOWN_LINK_RE = re.compile(r'(\[)([^\]\n]*)(\]\()([^)\n]+)(\))')

def resolve_and_update_link(target, source_new_rel, old_to_new, new_to_old):
    if '#' in target:
        path_part, anchor_part = target.split('#', 1)
        anchor_part = '#' + anchor_part
    else:
        path_part = target
        anchor_part = ''
        
    path_part_norm = path_part.replace('\\', '/')
    
    if path_part_norm.startswith(('http://', 'https://', 'mailto:', 'file:')):
        return None
        
    source_old_rel = new_to_old.get(source_new_rel, source_new_rel)
    source_old_dir = os.path.dirname(source_old_rel)
    source_new_dir = os.path.dirname(source_new_rel)
    
    is_relative = path_part_norm.startswith('.')
    new_path_part = None
    
    if is_relative:
        resolved_old_target = os.path.normpath(os.path.join(source_old_dir, path_part_norm)).replace('\\', '/')
        matched_old = None
        matched_new = None
        
        if resolved_old_target in old_to_new:
            matched_old = resolved_old_target
            matched_new = old_to_new[resolved_old_target]
        else:
            if not resolved_old_target.lower().endswith('.md'):
                resolved_with_ext = resolved_old_target + '.md'
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
            for src_file, dst_file in LEGACY_FILES_MAPPING.items():
                src_slash = src_file.replace('\\', '/')
                dst_slash = dst_file.replace('\\', '/')
                
                # Suporte a correspondência sem extensão
                src_no_ext = src_slash[:-3] if src_slash.endswith('.md') else src_slash
                dst_no_ext = dst_slash[:-3] if dst_slash.endswith('.md') else dst_slash
                
                if path_part_norm == src_slash:
                    matched_new = dst_slash
                    break
                elif path_part_norm == src_no_ext:
                    matched_new = dst_no_ext
                    break
                    
        if matched_new:
            new_path_part = matched_new
            
    if new_path_part is not None:
        return new_path_part + anchor_part
    return None

def update_links_in_file(filepath, root_dir, old_to_new, new_to_old, dry_run=True):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        return False
        
    rel_path_file = os.path.relpath(filepath, root_dir).replace('\\', '/')
    if dry_run:
        source_old_rel = rel_path_file
        source_new_rel = old_to_new.get(source_old_rel, source_old_rel)
    else:
        source_new_rel = rel_path_file
        source_old_rel = new_to_old.get(source_new_rel, source_new_rel)
        
    modified = False
    
    # 1. Wikilinks
    def wikilink_replacer(match):
        nonlocal modified
        g1, g2, g3, g4, g5 = match.groups()
        target = g2
        anchor = g3 if g3 else ''
        display = g4 if g4 else ''
        
        full_target = target + anchor
        new_target = resolve_and_update_link(full_target, source_new_rel, old_to_new, new_to_old)
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
    
    # 2. Markdown Links
    def markdown_link_replacer(match):
        nonlocal modified
        g1, g2, g3, g4, g5 = match.groups()
        target = g4
        new_target = resolve_and_update_link(target, source_new_rel, old_to_new, new_to_old)
        if new_target:
            modified = True
            return f"{g1}{g2}{g3}{new_target}{g5}"
        return match.group(0)
        
    new_content = MARKDOWN_LINK_RE.sub(markdown_link_replacer, new_content)
    
    # 3. Textual References
    for src_file, dst_file in LEGACY_FILES_MAPPING.items():
        src_slash = src_file.replace('\\', '/')
        dst_slash = dst_file.replace('\\', '/')
        src_no_ext = src_slash[:-3] if src_slash.endswith('.md') else src_slash
        dst_no_ext = dst_slash[:-3] if dst_slash.endswith('.md') else dst_slash
        
        if src_slash in new_content:
            new_content = new_content.replace(src_slash, dst_slash)
            modified = True
        if src_no_ext in new_content:
            new_content = new_content.replace(src_no_ext, dst_no_ext)
            modified = True
            
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
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    print(f"=== Pente Fino no Vault ===")
    print(f"Diretório raiz: {root_dir}")
    
    old_to_new = {k.replace('\\', '/'): v.replace('\\', '/') for k, v in LEGACY_FILES_MAPPING.items()}
    new_to_old = {v: k for k, v in old_to_new.items()}
    
    # Mover arquivos fisicamente
    for src, dst in LEGACY_FILES_MAPPING.items():
        src_abs = os.path.join(root_dir, src.replace('/', os.sep))
        dst_abs = os.path.join(root_dir, dst.replace('/', os.sep))
        
        if os.path.exists(src_abs):
            print(f"[ARQUIVAR] {src} -> {dst}")
            os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
            shutil.move(src_abs, dst_abs)
        else:
            print(f"[INFO] Arquivo não encontrado (já movido?): {src}")
            
    # Atualizar links em todos os markdown files
    md_files = find_all_markdown_files(root_dir)
    print(f"\n--- Atualização de Links ({len(md_files)} arquivos analisados) ---")
    
    updated_files_count = 0
    for md_file in md_files:
        rel_path = os.path.relpath(md_file, root_dir).replace('\\', '/')
        is_updated = update_links_in_file(md_file, root_dir, old_to_new, new_to_old, dry_run=False)
        if is_updated:
            print(f"[LINK ATUALIZADO] {rel_path}")
            updated_files_count += 1
            
    print(f"\nTotal de arquivos com links atualizados: {updated_files_count}")
    
    # Remover pastas vazias
    print(f"\n--- Limpeza de Pastas Vazias ---")
    for folder in EMPTY_FOLDERS:
        path = os.path.join(root_dir, folder.replace('/', os.sep))
        if os.path.exists(path) and os.path.isdir(path):
            print(f"[REMOVER PASTA] {folder}")
            try:
                shutil.rmtree(path)
            except Exception as e:
                print(f"Erro ao remover {folder}: {e}")

if __name__ == "__main__":
    main()
