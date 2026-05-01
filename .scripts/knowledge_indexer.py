"""
Knowledge Indexer - Automatic Vault Embedding Generation
Monitors vault changes and updates embeddings automatically
"""

import os
import sys
import gzip
import json
from pathlib import Path
from datetime import datetime
import time
import argparse

# Add skills to path
VAULT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(VAULT_ROOT / "skills" / "04-knowledge-systems" / "rag-pipeline"))

try:
    from embeddings_generator import EmbeddingsGenerator
    from vector_store import VectorStore
except ImportError as e:
    print(f"❌ Error importing RAG pipeline: {e}")
    print("Make sure embeddings_generator.py and vector_store.py are in skills/04-knowledge-systems/rag-pipeline/")
    sys.exit(1)


class KnowledgeIndexer:
    """Automated knowledge base indexing"""
    
    def __init__(
        self,
        vault_path: Path,
        index_dir: Path = None,
        model_name: str = "all-MiniLM-L6-v2"
    ):
        """
        Initialize knowledge indexer
        
        Args:
            vault_path: Path to Obsidian vault
            index_dir: Directory for index files (default: vault/.knowledge_index)
            model_name: Embedding model
        """
        self.vault_path = Path(vault_path)
        self.model_name = model_name
        
        # Index directory
        if index_dir is None:
            self.index_dir = self.vault_path / ".knowledge_index"
        else:
            self.index_dir = Path(index_dir)
        
        self.index_dir.mkdir(exist_ok=True)
        
        # Paths
        self.embeddings_file = self.index_dir / "embeddings.json.gz"
        self.index_file = self.index_dir / "vault.index"
        self.log_file = self.index_dir / "indexer.log"
        
        # Initialize components
        self.generator = EmbeddingsGenerator(
            vault_path=str(self.vault_path),
            model_name=self.model_name,
            cache_dir=".knowledge_index"
        )
    
    def log(self, message: str):
        """Log message to file and console"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] {message}"
        
        print(log_line)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_line + '\n')
    
    def build_full_index(self, force: bool = False):
        """
        Build complete index from scratch
        
        Args:
            force: Force regenerate even if up to date
        """
        self.log("🚀 Starting full index build...")
        
        start_time = time.time()
        
        try:
            # 1. Generate embeddings
            self.log("📊 Generating embeddings...")
            embeddings_data = self.generator.generate_embeddings(force_regenerate=force)
            stats = embeddings_data["stats"]

            if stats["processed"] == 0:
                if self.embeddings_file.exists() and self._embeddings_file_has_chunks():
                    self.log("✅ No new files changed; using existing embeddings file")
                    self.log(f"   Embeddings target: {self.embeddings_file}")
                    self.log(f"   Exists: {self.embeddings_file.exists()}")
                else:
                    self.log("⚠️ No new files changed, but embeddings cache is empty or missing; regenerating all files")
                    embeddings_data = self.generator.generate_embeddings(force_regenerate=True)
                    stats = embeddings_data["stats"]
                    self.log("💾 Saving embeddings...")
                    output_filename = self.embeddings_file.name
                    if output_filename.endswith('.gz'):
                        output_filename = output_filename[:-3]
                    self.generator.save_embeddings(embeddings_data, output_file=output_filename)
                    self.log(f"   Embeddings target: {self.embeddings_file}")
                    self.log(f"   Exists: {self.embeddings_file.exists()}")
            else:
                self.log("💾 Saving embeddings...")
                output_filename = self.embeddings_file.name
                if output_filename.endswith('.gz'):
                    output_filename = output_filename[:-3]
                self.generator.save_embeddings(embeddings_data, output_file=output_filename)
                self.log(f"   Embeddings target: {self.embeddings_file}")
                self.log(f"   Exists: {self.embeddings_file.exists()}")

            # 3. Build FAISS index
            self.log("🔨 Building FAISS index...")
            store = VectorStore(dimension=384)  # all-MiniLM-L6-v2 dimension
            store.load_embeddings(self.embeddings_file)
            store.save_index(self.index_file)
            
            # 4. Stats
            elapsed = time.time() - start_time
            stats = embeddings_data["stats"]
            
            self.log(f"✅ Index build complete in {elapsed:.1f}s")
            self.log(f"   - Processed: {stats['processed']} files")
            self.log(f"   - Skipped: {stats['skipped']} files")
            self.log(f"   - Total chunks: {stats['total_chunks']}")
            
            return True
        
        except Exception as e:
            self.log(f"❌ Error building index: {e}")
            return False
    
    def update_index(self):
        """
        Incremental update - only regenerate changed files
        """
        self.log("🔄 Starting incremental update...")
        
        start_time = time.time()
        
        try:
            # Generate embeddings (will skip unchanged files)
            embeddings_data = self.generator.generate_embeddings(force_regenerate=False)
            
            stats = embeddings_data["stats"]
            
            if stats['processed'] == 0:
                if self.embeddings_file.exists() and self._embeddings_file_has_chunks():
                    self.log("✅ Index up to date, no changes detected")
                    return True
                self.log("⚠️ No changes detected, but embeddings cache is empty or missing; rebuilding from scratch")
                return self.build_full_index(force=True)
            
            # Rebuild index with new embeddings
            self.log(f"🔨 Rebuilding index ({stats['processed']} files changed)...")
            output_filename = self.embeddings_file.name
            if output_filename.endswith('.gz'):
                output_filename = output_filename[:-3]
            self.generator.save_embeddings(embeddings_data, output_file=output_filename)
            
            store = VectorStore(dimension=384)
            store.load_embeddings(self.embeddings_file)
            store.save_index(self.index_file)
            
            elapsed = time.time() - start_time
            self.log(f"✅ Update complete in {elapsed:.1f}s")
            self.log(f"   - Updated: {stats['processed']} files")
            self.log(f"   - Total chunks: {stats['total_chunks']}")
            
            return True
        
        except Exception as e:
            self.log(f"❌ Error updating index: {e}")
            return False
    
    def watch_mode(self, interval: int = 300):
        """
        Watch mode - periodically check for updates
        
        Args:
            interval: Check interval in seconds (default: 5 minutes)
        """
        self.log(f"👀 Starting watch mode (checking every {interval}s)")
        self.log("   Press Ctrl+C to stop")
        
        try:
            while True:
                self.update_index()
                time.sleep(interval)
        
        except KeyboardInterrupt:
            self.log("\n👋 Watch mode stopped")
    
    def _embeddings_file_has_chunks(self) -> bool:
        """Check whether the cached embeddings file contains any chunks"""
        if not self.embeddings_file.exists():
            return False
        try:
            with gzip.open(self.embeddings_file, 'rt', encoding='utf-8') as f:
                data = json.load(f)
            return len(data.get('chunks', [])) > 0
        except Exception:
            return False

    def stats(self):
        """Show index statistics"""
        if not self.index_file.exists():
            print("❌ Index not found. Run with --build first.")
            return
        
        try:
            store = VectorStore()
            store.load_index(self.index_file)
            
            stats = store.stats()
            
            print("\n📊 Knowledge Index Statistics")
            print("="*50)
            print(f"  Total chunks:    {stats['total_chunks']}")
            print(f"  Unique files:    {stats['unique_files']}")
            print(f"  Embedding dim:   {stats['dimension']}")
            print(f"  Model:           {stats['model']}")
            print(f"  Index file:      {self.index_file}")
            print(f"  Index size:      {self.index_file.stat().st_size / 1024 / 1024:.2f} MB")
            
            # Embeddings file
            if self.embeddings_file.exists():
                print(f"  Embeddings file: {self.embeddings_file}")
                print(f"  Embeddings size: {self.embeddings_file.stat().st_size / 1024 / 1024:.2f} MB")
            
            print("="*50)
        
        except Exception as e:
            print(f"❌ Error reading stats: {e}")
    
    def verify(self):
        """Verify index integrity"""
        self.log("🔍 Verifying index...")
        
        issues = []
        
        # Check files exist
        if not self.embeddings_file.exists():
            issues.append("❌ Embeddings file missing")
        
        if not self.index_file.exists():
            issues.append("❌ FAISS index file missing")
        
        # Try loading
        try:
            store = VectorStore()
            store.load_index(self.index_file)
            self.log(f"✅ Index loaded successfully ({store.stats()['total_chunks']} chunks)")
        except Exception as e:
            issues.append(f"❌ Cannot load index: {e}")
        
        if issues:
            self.log("\n⚠️ Issues found:")
            for issue in issues:
                self.log(f"  {issue}")
            return False
        else:
            self.log("✅ Index verification passed")
            return True


def main():
    """CLI for knowledge indexer"""
    parser = argparse.ArgumentParser(
        description="Knowledge Indexer - Automatic vault embedding generation",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Build index
  python knowledge_indexer.py --build
  
  # Update existing index
  python knowledge_indexer.py --update
  
  # Watch mode (auto-update every 5 min)
  python knowledge_indexer.py --watch
  
  # Show statistics
  python knowledge_indexer.py --stats
        """
    )
    
    parser.add_argument(
        "--vault",
        default=".",
        help="Path to Obsidian vault (default: current directory)"
    )
    
    parser.add_argument(
        "--model",
        default="all-MiniLM-L6-v2",
        help="Embedding model (default: all-MiniLM-L6-v2)"
    )
    
    # Actions
    action_group = parser.add_mutually_exclusive_group(required=True)
    action_group.add_argument("--build", action="store_true", help="Build full index")
    action_group.add_argument("--update", action="store_true", help="Incremental update")
    action_group.add_argument("--watch", action="store_true", help="Watch mode (auto-update)")
    action_group.add_argument("--stats", action="store_true", help="Show statistics")
    action_group.add_argument("--verify", action="store_true", help="Verify index integrity")
    
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force regenerate all embeddings (for --build)"
    )
    
    parser.add_argument(
        "--interval",
        type=int,
        default=300,
        help="Check interval in seconds for watch mode (default: 300)"
    )
    
    args = parser.parse_args()
    
    # Initialize indexer
    indexer = KnowledgeIndexer(
        vault_path=Path(args.vault),
        model_name=args.model
    )
    
    # Execute action
    if args.build:
        indexer.build_full_index(force=args.force)
    
    elif args.update:
        indexer.update_index()
    
    elif args.watch:
        indexer.watch_mode(interval=args.interval)
    
    elif args.stats:
        indexer.stats()
    
    elif args.verify:
        indexer.verify()


if __name__ == "__main__":
    main()
