#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import hashlib
import re
import argparse

# Configurações do script
FOLDER_MAPPING = {
    "Bases": "11-Dados-Brutos/Bases",
    "benchmarks": "09-Sistema/benchmarks",
    "Canvases": "10-Interfaces/Canvases",
    "Clippings": "11-Dados-Brutos/Clippings",
    "Conhecimento-Geral": "04-Conhecimentos/07-Humanidades",
    "Conhecimentos-Gerais": "04-Conhecimentos/Conhecimentos-Gerais",
    "dashboards": "10-Interfaces/dashboards",
    "flashcards": "04-Conhecimentos/06-Estudos-e-Aprendizagem/flashcards",
    "Ideias": "00-Inbox/Ideias",
    "JARVIS": "02-JARVIS/JARVIS",
    "Knowledge-Base": "04-Conhecimentos/Knowledge-Base",
    "Projetos": "03-Projetos/Projetos",
    "raw": "11-Dados-Brutos/raw",
    "schema": "09-Sistema/schema",
    "scripts": "09-Sistema/scripts/legado",
    "simuladores": "09-Sistema/simuladores",
    "skills": "05-Skills/skills",
    "Templates": "99-Templates/Legado",
    "tests": "09-Sistema/tests",
    "web-ui": "10-Interfaces/web-ui",
    "wiki": "04-Conhecimentos/wiki",
    "Will-Pessoal": "06-Will-Pessoal/Will-Pessoal"
}

FILE_MAPPING = {
    "Painel-Cockpit.md": "10-Interfaces/Painel-Cockpit.md",
    "Projetos.md": "03-Projetos/Projetos.md",
    "AGENTS.md": "09-Sistema/agents/AGENTS.md",
    "CLAUDE.md": "09-Sistema/agents/CLAUDE.md",
    "GEMINI.md": "09-Sistema/agents/GEMINI.md",
    "CLI-BOOTSTRAP.md": "09-Sistema/CLI-BOOTSTRAP.md",
    "claude_desktop_config.json": "09-Sistema/config/claude_desktop_config.json",
    "indexer_config.json": "09-Sistema/config/indexer_config.json"
}

WIKILINK_RE = re.compile(r'(\[\[)([^\]|#\n]+)(#[^\]|\n]+)?(\|[^\]\n]+)?(\]\])')
MARKDOWN_LINK_RE = re.compile(r'(\[)([^\]\n]*)(\]\()([^)\n]+)(\))')
QUOTED_PATH_RE = re.compile(r'(["\'])(Bases|benchmarks|Canvases|Clippings|Conhecimento-Geral|Conhecimentos-Gerais|dashboards|flashcards|Ideias|JARVIS|Knowledge-Base|Projetos|raw|schema|scripts|simuladores|skills|Templates|tests|web-ui|wiki|Will-Pessoal)/')

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def build_mappings(root_dir):
    old_to_new = {}
    
    # 1. Scan legacy folders (source)
    for src_folder, dst_folder in FOLDER_MAPPING.items():
        src_path = os.path.join(root_dir, src_folder)
        if os.path.exists(src_path) and os.path.isdir(src_path):
            for dirpath, _, filenames in os.walk(src_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')
                    
                    parts = rel_path.split('/')
                    if parts[0] in FOLDER_MAPPING:
                        parts[0] = FOLDER_MAPPING[parts[0]]
                        new_rel_path = '/'.join(parts)
                        old_to_new[rel_path] = new_rel_path

    # 2. Scan destination folders (already moved)
    for src_folder, dst_folder in FOLDER_MAPPING.items():
        dst_path = os.path.join(root_dir, dst_folder)
        if os.path.exists(dst_path) and os.path.isdir(dst_path):
            for dirpath, _, filenames in os.walk(dst_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')
                    
                    dst_folder_slash = dst_folder.replace('\\', '/')
                    if rel_path.startswith(dst_folder_slash + '/'):
                        old_rel_path = src_folder + rel_path[len(dst_folder_slash):]
                        if old_rel_path not in old_to_new:
                            old_to_new[old_rel_path] = rel_path

    # 3. File mapping
    for src_file, dst_file in FILE_MAPPING.items():
        src_path = os.path.join(root_dir, src_file)
        dst_path = os.path.join(root_dir, dst_file)
        if os.path.exists(src_path):
            old_to_new[src_file] = dst_file
        elif os.path.exists(dst_path):
            old_to_new[src_file] = dst_file

    return old_to_new

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
            for src_folder, dst_folder in FOLDER_MAPPING.items():
                if path_part_norm == src_folder:
                    matched_new = dst_folder
                    break
                elif path_part_norm.startswith(src_folder + '/'):
                    matched_new = dst_folder + path_part_norm[len(src_folder):]
                    break
            
            if not matched_new and not path_part_norm.lower().endswith('.md'):
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
    
    # 1. Update Wikilinks
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
    
    # 2. Update Markdown Links
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
    
    # 3. Update Quoted Paths
    def quoted_replacer(match):
        nonlocal modified
        quote = match.group(1)
        folder = match.group(2)
        if folder in FOLDER_MAPPING:
            modified = True
            return f"{quote}{FOLDER_MAPPING[folder]}/"
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
    parser = argparse.ArgumentParser(description="Reorganiza o vault Will-obsidian e atualiza links.")
    parser.add_argument("--apply", action="store_true", help="Aplica as mudanças físicas e atualizações de links.")
    args = parser.parse_args()
    
    dry_run = not args.apply
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    print(f"=== Reorganização do Vault ===")
    print(f"Diretório raiz: {root_dir}")
    print(f"Modo: {'APLICAR' if args.apply else 'SIMULAÇÃO (dry-run)'}")
    
    # 1. Build mappings
    old_to_new = build_mappings(root_dir)
    new_to_old = {v: k for k, v in old_to_new.items()}
    
    # 2. Plan physical moves
    moves_planned = []
    remove_duplicates = []
    
    for old_rel, new_rel in sorted(old_to_new.items()):
        old_abs = os.path.join(root_dir, old_rel.replace('/', os.sep))
        new_abs = os.path.join(root_dir, new_rel.replace('/', os.sep))
        
        if not os.path.exists(old_abs):
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
    print(f"\n--- Movimentação Física ---")
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
    print(f"\n--- Atualização de Links ({len(md_files)} arquivos analisados) ---")
    
    updated_files_count = 0
    for md_file in md_files:
        rel_path = os.path.relpath(md_file, root_dir).replace('\\', '/')
        is_updated = update_links_in_file(md_file, root_dir, old_to_new, new_to_old, dry_run)
        if is_updated:
            print(f"[LINK ATUALIZADO] {rel_path}")
            updated_files_count += 1
            
    print(f"\nTotal de arquivos com links atualizados: {updated_files_count}")
    
    # 5. Cleanup empty legacy directories
    print(f"\n--- Limpeza de Pastas Vazias ---")
    for folder in sorted(FOLDER_MAPPING.keys(), key=len, reverse=True):
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
