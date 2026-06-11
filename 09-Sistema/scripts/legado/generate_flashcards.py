"""
Script: scripts/generate_flashcards.py
Varre as notas da pasta Conhecimento-Geral, extrai de forma inteligente conceitos,
termos em negrito e definições para gerar automaticamente flashcards compatíveis
com Anki (padrão CSV delimitado por ponto e vírgula).
Gera ou atualiza flashcards/Generated-Deck.csv.
"""

from pathlib import Path
import re
import csv

ROOT = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = ROOT / 'Conhecimento-Geral'
DECK_FILE = ROOT / 'flashcards' / 'Generated-Deck.csv'

# Padrões regulares para identificação de termos e conceitos
DEF_RE_LIST = [
    # Ex: - **Epistemologia**: Estudo do conhecimento...
    re.compile(r"^\s*[-*]\s+\*\*(.*?)\*\*:\s+(.*)$", re.IGNORECASE),
    # Ex: - **Ontologia** — Parte da metafísica...
    re.compile(r"^\s*[-*]\s+\*\*(.*?)\*\*\s+—\s+(.*)$", re.IGNORECASE),
    # Ex: **Empirismo** é a corrente... ou O Empirismo é um método...
    re.compile(r"\*\*(.*?)\*\*\s+(?:é\s+definid[oa]\s+como|é\s+um[aa]?|consiste\s+em)\s+(.*?)(?:\.|$)", re.IGNORECASE)
]

def clean_text(text: str) -> str:
    """Limpa marcações markdown indesejadas e caracteres problemáticos para o CSV"""
    text = re.sub(r"\[\[(.*?)\]\]", r"\1", text) # Remove links obsidian [[A|B]] ou [[A]]
    text = text.replace('"', '""') # Escapa aspas para conformidade com RFC 4180
    return text.strip()

def scan_for_flashcards():
    cards = []
    
    if not KNOWLEDGE_DIR.exists():
        print(f"⚠️ Diretório de Conhecimento Geral {KNOWLEDGE_DIR} não encontrado!")
        return cards
        
    for p in KNOWLEDGE_DIR.rglob('*.md'):
        if p.name.lower() == 'index.md' or p.name.lower() == 'como-contribuir.md':
            continue
            
        tags = ['conhecimento-geral', p.parent.name.lower()]
        
        try:
            content = p.read_text(encoding='utf-8')
            for line in content.splitlines():
                line_stripped = line.strip()
                if not line_stripped:
                    continue
                    
                for rx in DEF_RE_LIST:
                    match = rx.search(line_stripped)
                    if match:
                        term = clean_text(match.group(1))
                        definition = clean_text(match.group(2))
                        
                        # Ignorar termos muito curtos (ruído) ou definições incompletas
                        if len(term) < 3 or len(definition) < 10 or len(term) > 60:
                            continue
                            
                        front = f"O que é **{term}**?"
                        back = definition
                        
                        # Evitar repetições de perguntas no mesmo baralho
                        if not any(c['Front'] == front for c in cards):
                            cards.append({
                                'Front': front,
                                'Back': back,
                                'Tags': ",".join(tags)
                            })
                        break # Encontrou um padrão, pula para a próxima linha
        except Exception as e:
            print(f"⚠️ Erro ao varrer {p.name}: {e}")
            
    return cards

def main():
    print("🧠 Escaneando o conhecimento acadêmico para compilar flashcards...")
    cards = scan_for_flashcards()
    print(f"🎴 Extraídos {len(cards)} flashcards conceituais!")
    
    if not cards:
        print("ℹ️ Nenhuma nova definição padrão encontrada em Conhecimento-Geral.")
        return
        
    # Salva ou mescla no arquivo Generated-Deck.csv
    DECK_FILE.parent.mkdir(exist_ok=True)
    
    with open(DECK_FILE, 'w', newline='', encoding='utf-8') as f:
        # Força o uso de ponto e vírgula delimitador tal como no XAI-Fairness-Deck.csv
        writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Front', 'Back', 'Tags'])
        
        for c in cards:
            writer.writerow([c['Front'], c['Back'], c['Tags']])
            
    print(f"✅ Baralho de flashcards salvo em {DECK_FILE} com sucesso!")

if __name__ == '__main__':
    main()
