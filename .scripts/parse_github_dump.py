#!/usr/bin/env python3
import os
import re
from pathlib import Path
from datetime import datetime

# Caminhos
SCRIPT_ROOT = Path(__file__).parent.resolve()
VAULT_ROOT = SCRIPT_ROOT.parent
DUMP_FILE = SCRIPT_ROOT / "github_dump.txt"

GITHUB_COMPLETO_1 = VAULT_ROOT / "Projetos" / "GitHub-Completo.md"
GITHUB_COMPLETO_2 = VAULT_ROOT / "Projetos" / "04-Master-Plan" / "GitHub-Completo.md"
OVERVIEW_MD = VAULT_ROOT / "Will-Pessoal" / "01-Identidade" / "Perfil" / "William-kelvem94 Overview.md"
PERFIL_MD = VAULT_ROOT / "Will-Pessoal" / "01-Identidade" / "Perfil" / "Perfil.md"

def parse_dump(dump_text):
    # 1. Substituir non-breaking space (xa0) por espaço normal
    text = dump_text.replace('\xa0', ' ')
    
    # 2. Impedir que "General Public License" crie um falso repositório chamado "General" de visibilidade "Public"
    text = text.replace("General Public License", "General_Public_License")
    text = text.replace("General Public", "General_Public")
    
    # 3. Remover lixos do cabeçalho web que colaram com o repositório IA-POTENTE
    text = re.sub(r'3\s+followers\s+·\s+3\s+following\s+Achievements\s*x2\s*x2\s*Organizations', ' ', text)
    text = re.sub(r'3\s+followers\s+3\s+followingAchievementsx2x2Organizations', ' ', text)
    text = text.replace('followingAchievementsx2x2Organizations', ' ')
    text = text.replace('Achievementsx2x2Organizations', ' ')
    
    # 4. Separar anos colados com nomes de repositórios (muito comum em colagens corridas)
    # Ex: 2021Atividade-03 -> 2021 Atividade-03
    text = re.sub(r'(\d{4})([a-zA-Z\-_])', r'\1 \2', text)
    
    # 5. Inserir quebras de linha cruciais antes de cada [Nome] [Private/Public]
    # Ex: ...Dec 14, 2024 Tradutor-2.0 Private... vira ...Dec 14, 2024\nTradutor-2.0 Private...
    text = re.sub(r'([\w\-\.]+)\s+(Private|Public)', r'\n\1 \2', text)
    
    # 6. Adicionar espaços ao redor de Private e Public para separar seções coladas
    text = re.sub(r'([a-zA-Z0-9\-_]+)(Private|Public)', r'\1 \2', text)
    text = re.sub(r'(Private|Public)([a-zA-Z0-9\-_]+)', r'\1 \2', text)
    
    # Normalizar múltiplos espaços para espaço simples por linha, sem apagar quebras
    lines = []
    for line in text.splitlines():
        line_clean = re.sub(r'\s+', ' ', line).strip()
        if line_clean:
            lines.append(line_clean)
            
    repos = {}
    i = 0
    total_lines = len(lines)
    
    # Linguagens ordenadas por tamanho/especificidade descrescente para evitar falsos positivos
    languages_check = ["TypeScript", "JavaScript", "PowerShell", "Python", "Shell", "HTML", "Dart", "Java", "C++", "PHP", "CSS", "C#"]
    
    while i < total_lines:
        line = lines[i]
        
        # Ignorar linhas de controle puras (apenas se forem correspondências completas e isoladas)
        if line in ["Skip to content", "User navigation", "Overview", "Repositories", "Projects", "Packages", "Stars", "Achievements", "Footer", "Terms", "Privacy", "Security", "Status", "Community", "Docs", "Contact", "Manage cookies", "Do not share my personal information", "Footer navigation", "© 2026 GitHub, Inc.", "© 2026 GitHub, Inc. Footer navigation", "© 2026 GitHub, Inc. Footer navigation Terms Privacy Security Status Community Docs Contact Manage cookies Do not share my personal information"]:
            i += 1
            continue
            
        # Padrão Corrido de Linha Única
        corrido_match = re.search(r"^([\w\-\.]+)\s+(Private|Public)\s+(.*?)\s*(Updated\s+on\s+.*|Updated\s+.*)?$", line)
        if corrido_match:
            name = corrido_match.group(1)
            visibility = corrido_match.group(2)
            meta = corrido_match.group(3).strip()
            updated = (corrido_match.group(4) or "").strip()
            
            # Limpa prefixos de ano residuais se o regex de separação deixou no nome sem querer
            if re.match(r'^\d{4}', name) and len(name) > 4:
                name = re.sub(r'^\d{4}', '', name)
                
            # Se updated ou se meta for substancial
            if updated or (meta and len(meta.split()) > 1 and not re.match(r'^(TypeScript|Python|PHP|JavaScript|HTML|CSS|Java|C#|C\+\+|Shell|PowerShell|Dart)$', meta)):
                # Extração de Forked
                forked_from = ""
                fork_match = re.search(r"Forked\s+from\s+([\w\-\./]+)", meta)
                if fork_match:
                    forked_from = fork_match.group(1)
                    meta = meta.replace(fork_match.group(0), "").strip()
                    
                # Extração de Linguagem respeitando prioridade
                lang = "N/A"
                for test_lang in languages_check:
                    if re.search(rf"\b{re.escape(test_lang)}\b", meta):
                        lang = test_lang
                        meta = re.sub(rf"\b{re.escape(test_lang)}\b", "", meta).strip()
                        break
                        
                # Licenças
                license = ""
                for lic in ["MIT License", "GNU Affero General Public License v3.0", "MIT", "Apache License 2.0", "GPL"]:
                    if lic in meta:
                        license = lic
                        meta = meta.replace(lic, "").strip()
                        break
                        
                desc = meta.split("Updated")[0].strip()
                desc = re.sub(r'\s{2,}', ' ', desc) # limpa múltiplos espaços
                if not desc or desc in ["Other", "config", "github-config", "1"]:
                    desc = "Sem descrição"
                    
                # Se o nome limpado for vazio ou curto demais após limpeza de ano, ignora
                if len(name) > 1:
                    repos[name] = {
                        "name": name,
                        "visibility": visibility,
                        "lang": lang,
                        "desc": desc,
                        "updated": updated or "N/A",
                        "forked_from": forked_from,
                        "license": license
                    }
                i += 1
                continue

        # Padrão Bloco Multilinhas (Seções 1 e 2)
        multiline_match = re.match(r"^([\w\-\.]+)\s+(Private|Public)$", line)
        if multiline_match:
            name = multiline_match.group(1)
            visibility = multiline_match.group(2)
            
            # Limpa prefixo de ano residual se houver
            if re.match(r'^\d{4}', name) and len(name) > 4:
                name = re.sub(r'^\d{4}', '', name)
                
            desc_lines = []
            lang = "N/A"
            updated = "N/A"
            forked_from = ""
            license = ""
            
            j = i + 1
            while j < total_lines:
                next_line = lines[j].strip()
                if not next_line:
                    j += 1
                    continue
                    
                # Condições de parada
                if re.match(r"^([\w\-\.]+)\s+(Private|Public)$", next_line):
                    break
                if re.search(r"^([\w\-\.]+)\s+(Private|Public)\s+(.*?)\s*(Updated\s+on\s+.*|Updated\s+.*)?$", next_line):
                    break
                if next_line in ["Footer", "Terms", "Privacy", "Security", "GitHub, Inc.", "Footer navigation", "© 2026 GitHub, Inc."]:
                    break
                    
                if next_line.startswith("Forked from"):
                    forked_from = next_line.replace("Forked from", "").strip()
                elif "Updated" in next_line:
                    updated = next_line.strip()
                    for test_lang in languages_check:
                        if test_lang in next_line:
                            lang = test_lang
                            updated = updated.replace(test_lang, "").strip()
                else:
                    matched_lang = False
                    for test_lang in languages_check:
                        if next_line == test_lang:
                            lang = test_lang
                            matched_lang = True
                            break
                    if not matched_lang:
                        if "License" in next_line or next_line in ["MIT", "GPL"]:
                            license = next_line
                        else:
                            if next_line != "1":
                                desc_lines.append(next_line)
                j += 1
                
            desc = " ".join(desc_lines).strip()
            if not desc or desc in ["Other", "config", "github-config"]:
                desc = "Sem descrição"
                
            if len(name) > 1:
                repos[name] = {
                    "name": name,
                    "visibility": visibility,
                    "lang": lang,
                    "desc": desc,
                    "updated": updated,
                    "forked_from": forked_from,
                    "license": license
                }
            i = j
            continue
            
        i += 1
        
    return repos

def format_repo_list(repos):
    sorted_repos = sorted(list(repos.values()), key=lambda x: (x['visibility'], x['name'].lower()))
    
    lines = []
    for r in sorted_repos:
        repo_link = f"https://github.com/William-kelvem94/{r['name']}"
        fork_info = f" (Fork de {r['forked_from']})" if r['forked_from'] else ""
        vis_emoji = "🔒" if r['visibility'] == "Private" else "🌐"
        
        vault_link = ""
        possible_note = VAULT_ROOT / "Projetos" / "01-Ativos" / "Privados" / f"{r['name']}.md"
        possible_note_alt = VAULT_ROOT / "Projetos" / "01-Ativos" / "Privados" / f"{r['name'].replace('_', '-')}.md"
        
        if possible_note.exists():
            vault_link = f" | [[Projetos/01-Ativos/Privados/{r['name']}|📄 Ver Nota]]"
        elif possible_note_alt.exists():
            vault_link = f" | [[Projetos/01-Ativos/Privados/{r['name'].replace('_', '-')}|📄 Ver Nota]]"
            
        lines.append(f"- {vis_emoji} **[{r['name']}]({repo_link})** ({r['lang']}){fork_info} - *{r['desc']}*{vault_link}\n  - *Atualização:* `{r['updated']}`  | Status: `{r['visibility']}`")
        
    return "\n".join(lines)

def run():
    print("📖 Carregando dump com limpador de lixos específicos...")
    if not DUMP_FILE.exists():
        print(f"❌ Arquivo {DUMP_FILE} não encontrado!")
        return
        
    dump_text = DUMP_FILE.read_text(encoding='utf-8')
    repos = parse_dump(dump_text)
    
    target_3 = ["IA-POTENTE", "DeepSeek-V3---C-PIA", "TRADUTOR-WKP", "Atividade-03", "Atividade-01"]
    print(f"\n🔍 TOTAL REPOSITÓRIOS ENCONTRADOS NO DUMP: {len(repos)} / 78")
    
    # Imprime lista rápida no painel para auditoria visual
    for idx, (name, details) in enumerate(sorted(repos.items()), 1):
        found_marker = "⭐" if name in target_3 else "  "
        print(f"[{idx:02d}]{found_marker} {name} ({details['visibility']}) - {details['lang']} - {details['desc'][:45]}...")
        
    # 1. Gerar Markdown de Lista
    repo_list_markdown = format_repo_list(repos)
    
    # 2. Atualizar Projetos/GitHub-Completo.md e Projetos/04-Master-Plan/GitHub-Completo.md
    for filepath in [GITHUB_COMPLETO_1, GITHUB_COMPLETO_2]:
        if filepath.exists():
            print(f"✏️ Atualizando {filepath.name}...")
            content = filepath.read_text(encoding='utf-8')
            
            # Atualiza cabeçalho (quantidade total e data)
            content = re.sub(r"GitHub Completo - William-kelvem94 \(\d+\s*Repos\)", f"GitHub Completo - William-kelvem94 ({len(repos)} Repos)", content)
            content = re.sub(r"Mapeamento de \d+ repositórios", f"Mapeamento de {len(repos)} repositórios", content)
            content = re.sub(r"Stats: \d+ repos", f"Stats: {len(repos)} repos", content)
            
            content = re.sub(r"\(\d+\s*repositórios\)", f"({len(repos)} repositórios)", content)
            content = re.sub(r"\(\d+\s*Repos\)", f"({len(repos)} Repos)", content)
            
            pattern = r"## Lista de Repositórios \(Automática\)[\s\S]*"
            new_section = f"## Lista de Repositórios (Automática)\n\n*Recuperado diretamente do perfil do GitHub em {datetime.now().strftime('%Y-%m-%d')}*\n\n{repo_list_markdown}"
            
            if re.search(pattern, content):
                new_content = re.sub(pattern, new_section, content)
            else:
                new_content = content.strip() + "\n\n" + new_section
                
            filepath.write_text(new_content, encoding='utf-8')
            print(f"   ✅ {filepath.name} atualizado.")
            
    # 3. Atualizar William-kelvem94 Overview.md
    if OVERVIEW_MD.exists():
        print("✏️ Atualizando William-kelvem94 Overview.md...")
        content = OVERVIEW_MD.read_text(encoding='utf-8')
        
        public_count = sum(1 for r in repos.values() if r['visibility'] == 'Public')
        private_count = sum(1 for r in repos.values() if r['visibility'] == 'Private')
        
        stat_table_pattern = r"\| Métrica \| Valor atual \| Meta \|[\s\S]*?(?=\n\n(?:###|##|---|\>)|$)"
        new_table = f"""| Métrica | Valor atual | Meta |
|---------|:-----------:|:----:|
| Repositórios públicos | {public_count} | 20+ |
| Repositórios privados | {private_count} | — |
| Repositórios totais | {len(repos)} | — |
| Seguidores | 3 followers | 10+ |
| Organizações | @ProjetoMeta | — |
| Conquistas | Pull Shark, Pair Extraordinaire, YOLO, Quickdraw | — |"""
        
        if re.search(stat_table_pattern, content):
            content = re.sub(stat_table_pattern, new_table, content)
            
        OVERVIEW_MD.write_text(content, encoding='utf-8')
        print("   ✅ William-kelvem94 Overview.md atualizado.")
        
    # 4. Atualizar Perfil.md
    if PERFIL_MD.exists():
        print("✏️ Atualizando Perfil.md...")
        content = PERFIL_MD.read_text(encoding='utf-8')
        content = re.sub(r"- \*\*GitHub:\*\* https://github.com/William-kelvem94 \(\d+\+?\s*repos\)", f"- **GitHub:** https://github.com/William-kelvem94 ({len(repos)} repos)", content)
        PERFIL_MD.write_text(content, encoding='utf-8')
        print("   ✅ Perfil.md atualizado.")

if __name__ == "__main__":
    run()
