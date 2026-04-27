from pathlib import Path
import sys
vault = Path('.').resolve()
sys.path.insert(0, str(vault / '.scripts'))
from knowledge_indexer import KnowledgeIndexer
idx = KnowledgeIndexer(vault_path=vault)
print('embeddings_file=', idx.embeddings_file)
print('exists=', idx.embeddings_file.exists())
print('index_dir=', idx.index_dir)
print('cache_dir=', idx.generator.cache_dir)
print('cache_contents=', [p.name for p in idx.generator.cache_dir.iterdir()])
