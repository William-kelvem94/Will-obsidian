#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import hashlib
import re
import argparse

# Mapeamentos divididos por lotes
BATCHES = {
    1: {
        "04-Conhecimentos/01-IA-e-Agentes/Automacao": "04-Conhecimentos/01-IA-e-Agentes",
        "04-Conhecimentos/01-IA-e-Agentes/Futurologia": "04-Conhecimentos/01-IA-e-Agentes",
        "04-Conhecimentos/04-Seguranca-e-Redes/LGPD-Privacidade": "04-Conhecimentos/04-Seguranca-e-Redes",
        "04-Conhecimentos/04-Seguranca-e-Redes/Redes": "04-Conhecimentos/04-Seguranca-e-Redes",
        "04-Conhecimentos/04-Seguranca-e-Redes/Seguranca": "04-Conhecimentos/04-Seguranca-e-Redes"
    },
    2: {
        "04-Conhecimentos/05-Produto-UX-e-Carreira/Carreira": "04-Conhecimentos/05-Produto-UX-e-Carreira",
        "04-Conhecimentos/05-Produto-UX-e-Carreira/Produto-UX": "04-Conhecimentos/05-Produto-UX-e-Carreira",
        "04-Conhecimentos/06-Estudos-e-Aprendizagem/Habilidades": "04-Conhecimentos/06-Estudos-e-Aprendizagem",
        "04-Conhecimentos/06-Estudos-e-Aprendizagem/Matematica": "04-Conhecimentos/06-Estudos-e-Aprendizagem",
        "04-Conhecimentos/06-Estudos-e-Aprendizagem/Experimentacao": "04-Conhecimentos/06-Estudos-e-Aprendizagem"
    },
    3: {
        "04-Conhecimentos/08-Vida-Pratica/Produtividade": "04-Conhecimentos/08-Vida-Pratica",
        "04-Conhecimentos/08-Vida-Pratica/Saude-Rotina": "04-Conhecimentos/08-Vida-Pratica",
        "04-Conhecimentos/08-Vida-Pratica/Financas": "04-Conhecimentos/08-Vida-Pratica",
        "04-Conhecimentos/08-Vida-Pratica/Comunicacao": "04-Conhecimentos/08-Vida-Pratica",
        "04-Conhecimentos/08-Vida-Pratica/Saude-Mental": "04-Conhecimentos/08-Vida-Pratica"
    }
}

WIKILINK_RE = re.compile(r'(\[\[)([^\]|#\n]+)(#[^\]|\n]+)?(\|[^\]\n]+)?(\]\])')
MARKDOWN_LINK_RE = re.compile(r'(\[)([^\]\n]*)(\]\()([^)\n]+)(\))')

def get_file_hash(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        buf = f.read(65536)
        while len(buf) > 0:
            hasher.update(buf)
            buf = f.read(65536)
    return hasher.hexdigest()

def build_mappings(root_dir, mapping):
    old_to_new = {}
    
    # Mapear arquivos contidos nas pastas de origem
    for src_folder, dst_folder in mapping.items():
        src_path = os.path.join(root_dir, src_folder.replace('/', os.sep))
        if os.path.exists(src_path) and os.path.isdir(src_path):
            for dirpath, _, filenames in os.walk(src_path):
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    rel_path = os.path.relpath(filepath, root_dir).replace('\\', '/')
                    
                    src_folder_slash = src_folder.replace('\\', '/')
                    dst_folder_slash = dst_folder.replace('\\', '/')
                    
                    if rel_path.startswith(src_folder_slash):
                        new_rel_path = dst_folder_slash + rel_path[len(src_folder_slash):]
                        old_to_new[rel_path] = new_rel_path
                        
    return old_to_new

def resolve_and_update_link(target, source_new_rel, old_to_new, new_to_old, mapping):
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
            for src_folder, dst_folder in mapping.items():
                src_folder_slash = src_folder.replace('\\', '/')
                dst_folder_slash = dst_folder.replace('\\', '/')
                
                if path_part_norm == src_folder_slash:
                    matched_new = dst_folder_slash
                    break
                elif path_part_norm.startswith(src_folder_slash + '/'):
                    matched_new = dst_folder_slash + path_part_norm[len(src_folder_slash):]
                    break
            
            if not matched_new and not path_part_norm.lower().endswith('.md'):
                with_ext = path_part_norm + '.md'
                if with_ext in old_to_new:
                    matched_new = old_to_new[with_ext][:-3]
                else:
                    for src_folder, dst_folder in mapping.items():
                        src_folder_slash = src_folder.replace('\\', '/')
                        dst_folder_slash = dst_folder.replace('\\', '/')
                        if with_ext.startswith(src_folder_slash + '/'):
                            matched_new = (dst_folder_slash + with_ext[len(src_folder_slash):])[:-3]
                            break
                            
        if matched_new:
            new_path_part = matched_new
            
    if new_path_part is not None:
        return new_path_part + anchor_part
    return None

def update_links_in_file(filepath, root_dir, old_to_new, new_to_old, mapping, dry_run=True):
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
        new_target = resolve_and_update_link(full_target, source_new_rel, old_to_new, new_to_old, mapping)
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
        new_target = resolve_and_update_link(target, source_new_rel, old_to_new, new_to_old, mapping)
        if new_target:
            modified = True
            return f"{g1}{g2}{g3}{new_target}{g5}"
        return match.group(0)
        
    new_content = MARKDOWN_LINK_RE.sub(markdown_link_replacer, new_content)
    
    # 3. Textual References
    for src_folder, dst_folder in mapping.items():
        src_folder_slash = src_folder.replace('\\', '/')
        dst_folder_slash = dst_folder.replace('\\', '/')
        if src_folder_slash in new_content:
            new_content = new_content.replace(src_folder_slash, dst_folder_slash)
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
    parser = argparse.ArgumentParser(description="Consolida subpastas de conhecimento em lotes.")
    parser.add_argument("--lote", type=int, choices=[1, 2, 3], required=True, help="Número do lote a executar (1, 2 ou 3).")
    parser.add_argument("--apply", action="store_true", help="Aplica as mudanças físicas e atualiza links.")
    args = parser.parse_args()
    
    dry_run = not args.apply
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    mapping = BATCHES[args.lote]
    
    print(f"=== Reorganização de Subpastas - Lote {args.lote} ===")
    print(f"Diretório raiz: {root_dir}")
    print(f"Modo: {'APLICAR' if args.apply else 'SIMULAÇÃO (dry-run)'}")
    
    # 1. Build mappings
    old_to_new = build_mappings(root_dir, mapping)
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
            
    # 3. Physical moves
    print(f"\n--- Movimentação Física Planejada ---")
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
            
    # 4. Link updates
    md_files = find_all_markdown_files(root_dir)
    print(f"\n--- Atualização de Links ({len(md_files)} arquivos analisados) ---")
    
    updated_files_count = 0
    for md_file in md_files:
        rel_path = os.path.relpath(md_file, root_dir).replace('\\', '/')
        is_updated = update_links_in_file(md_file, root_dir, old_to_new, new_to_old, mapping, dry_run)
        if is_updated:
            print(f"[LINK ATUALIZADO] {rel_path}")
            updated_files_count += 1
            
    print(f"\nTotal de arquivos com links atualizados: {updated_files_count}")
    
    # 5. Empty Folders Cleanup
    print(f"\n--- Limpeza de Pastas Vazias ---")
    for folder in sorted(mapping.keys(), key=len, reverse=True):
        path = os.path.join(root_dir, folder.replace('/', os.sep))
        if os.path.exists(path) and os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(path, topdown=False):
                valid_files = [f for f in filenames if f not in ('.DS_Store', 'desktop.ini', '.gitkeep')]
                if not dirnames and not valid_files:
                    dir_rel = os.path.relpath(dirpath, root_dir).replace('\\', '/')
                    print(f"[REMOVER PASTA VAZIA] {dir_rel}")
                    if not dry_run:
                        try:
                            for f in filenames:
                                os.remove(os.path.join(dirpath, f))
                            os.rmdir(dirpath)
                        except Exception as e:
                            print(f"Erro ao remover {dir_rel}: {e}")

if __name__ == "__main__":
    main()
