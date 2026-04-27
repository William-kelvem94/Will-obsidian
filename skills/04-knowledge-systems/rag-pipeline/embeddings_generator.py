"""
Embeddings Generator for Obsidian Vault
Generates vector embeddings from markdown files for semantic search
"""

import os
import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import hashlib

try:
    from sentence_transformers import SentenceTransformer
    SENTENCE_TRANSFORMERS_AVAILABLE = True
except ImportError:
    SENTENCE_TRANSFORMERS_AVAILABLE = False
    print("⚠️ sentence-transformers not installed. Run: pip install sentence-transformers")


class EmbeddingsGenerator:
    """Generate and manage embeddings for markdown files"""
    
    def __init__(
        self, 
        vault_path: str,
        model_name: str = "all-MiniLM-L6-v2",
        cache_dir: str = ".embeddings_cache"
    ):
        """
        Initialize embeddings generator
        
        Args:
            vault_path: Path to Obsidian vault root
            model_name: HuggingFace model for embeddings (384-dim default)
            cache_dir: Directory to cache embeddings
        """
        self.vault_path = Path(vault_path)
        self.model_name = model_name
        self.cache_dir = self.vault_path / cache_dir
        self.cache_dir.mkdir(exist_ok=True)
        
        # Initialize model (lazy loading)
        self._model = None
        
        # Metadata file
        self.metadata_file = self.cache_dir / "embeddings_metadata.json"
        self.metadata = self._load_metadata()
    
    @property
    def model(self):
        """Lazy load the embedding model"""
        if self._model is None:
            if not SENTENCE_TRANSFORMERS_AVAILABLE:
                raise ImportError("sentence-transformers required. Install: pip install sentence-transformers")
            
            print(f"🔄 Loading embedding model: {self.model_name}")
            self._model = SentenceTransformer(self.model_name)
            print(f"✅ Model loaded ({self.model.get_sentence_embedding_dimension()} dimensions)")
        
        return self._model
    
    def _load_metadata(self) -> Dict:
        """Load embeddings metadata from cache"""
        if self.metadata_file.exists():
            with open(self.metadata_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "model": self.model_name,
            "created": datetime.now().isoformat(),
            "files": {}
        }
    
    def _save_metadata(self):
        """Save embeddings metadata"""
        self.metadata["updated"] = datetime.now().isoformat()
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2)
    
    def _file_hash(self, file_path: Path) -> str:
        """Calculate MD5 hash of file content"""
        with open(file_path, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    
    def _needs_update(self, file_path: Path) -> bool:
        """Check if file needs embedding regeneration"""
        rel_path = str(file_path.relative_to(self.vault_path))
        
        # Not in cache = needs generation
        if rel_path not in self.metadata["files"]:
            return True
        
        # File hash changed = needs update
        current_hash = self._file_hash(file_path)
        cached_hash = self.metadata["files"][rel_path].get("hash")
        
        return current_hash != cached_hash
    
    def extract_chunks(self, file_path: Path, chunk_size: int = 500) -> List[Dict]:
        """
        Extract meaningful chunks from markdown file
        
        Args:
            file_path: Path to markdown file
            chunk_size: Max characters per chunk
            
        Returns:
            List of chunk dicts with text and metadata
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(file_path, 'r', encoding='latin-1') as f:
                content = f.read()
        
        chunks = []
        current_chunk = []
        current_size = 0
        current_heading = ""
        
        lines = content.split('\n')
        
        for line in lines:
            # Track headings for context
            if line.startswith('#'):
                current_heading = line.lstrip('#').strip()
            
            line_size = len(line)
            
            # Chunk by size, but try to break at paragraphs
            if current_size + line_size > chunk_size and current_chunk:
                chunk_text = '\n'.join(current_chunk).strip()
                if chunk_text:
                    chunks.append({
                        "text": chunk_text,
                        "heading": current_heading,
                        "file": str(file_path.relative_to(self.vault_path))
                    })
                current_chunk = []
                current_size = 0
            
            current_chunk.append(line)
            current_size += line_size
        
        # Add final chunk
        if current_chunk:
            chunk_text = '\n'.join(current_chunk).strip()
            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "heading": current_heading,
                    "file": str(file_path.relative_to(self.vault_path))
                })
        
        return chunks
    
    def generate_embeddings(
        self, 
        file_paths: Optional[List[Path]] = None,
        force_regenerate: bool = False
    ) -> Dict:
        """
        Generate embeddings for files
        
        Args:
            file_paths: Specific files to process (None = all markdown files)
            force_regenerate: Regenerate even if cached
            
        Returns:
            Dict with embeddings and metadata
        """
        if file_paths is None:
            # Find all markdown files
            file_paths = list(self.vault_path.rglob("*.md"))
            # Exclude hidden directories and cache
            file_paths = [
                f for f in file_paths 
                if not any(part.startswith('.') for part in f.parts)
            ]
        
        print(f"📊 Processing {len(file_paths)} files...")
        
        all_embeddings = []
        all_chunks = []
        processed_files = 0
        skipped_files = 0
        
        for file_path in file_paths:
            # Skip if not changed (unless forced)
            if not force_regenerate and not self._needs_update(file_path):
                skipped_files += 1
                continue
            
            try:
                # Extract chunks
                chunks = self.extract_chunks(file_path)
                
                if not chunks:
                    continue
                
                # Generate embeddings for chunks
                texts = [chunk["text"] for chunk in chunks]
                embeddings = self.model.encode(texts, show_progress_bar=False)
                
                # Store
                for chunk, embedding in zip(chunks, embeddings):
                    chunk["embedding"] = embedding.tolist()
                    all_chunks.append(chunk)
                
                # Update metadata
                rel_path = str(file_path.relative_to(self.vault_path))
                self.metadata["files"][rel_path] = {
                    "hash": self._file_hash(file_path),
                    "chunks": len(chunks),
                    "updated": datetime.now().isoformat()
                }
                
                processed_files += 1
                
                if processed_files % 10 == 0:
                    print(f"  ✅ Processed {processed_files} files...")
            
            except Exception as e:
                print(f"  ⚠️ Error processing {file_path.name}: {e}")
        
        # Save metadata
        self._save_metadata()
        
        print(f"\n✅ Complete!")
        print(f"  - Processed: {processed_files} files")
        print(f"  - Skipped (unchanged): {skipped_files} files")
        print(f"  - Total chunks: {len(all_chunks)}")
        
        return {
            "chunks": all_chunks,
            "metadata": self.metadata,
            "stats": {
                "processed": processed_files,
                "skipped": skipped_files,
                "total_chunks": len(all_chunks)
            }
        }
    
    def save_embeddings(self, embeddings_data: Dict, output_file: str = "embeddings.json"):
        """Save embeddings to file"""
        # Normalize output filename to avoid double .gz
        if output_file.endswith('.gz'):
            output_file = output_file[:-3]

        output_path = self.cache_dir / output_file
        
        # Embeddings are large, save compressed
        import gzip
        
        gz_path = output_path.with_suffix(output_path.suffix + ".gz")
        with gzip.open(str(gz_path), 'wt', encoding='utf-8') as f:
            json.dump(embeddings_data, f)
        
        print(f"💾 Embeddings saved to: {gz_path}")
        print(f"   Size: {(gz_path.stat().st_size / 1024 / 1024):.2f} MB (compressed)")


def main():
    """CLI for generating embeddings"""
    import argparse
    
    parser = argparse.ArgumentParser(description="Generate embeddings for Obsidian vault")
    parser.add_argument("vault_path", help="Path to Obsidian vault")
    parser.add_argument("--model", default="all-MiniLM-L6-v2", help="Embedding model")
    parser.add_argument("--force", action="store_true", help="Force regenerate all")
    parser.add_argument("--chunk-size", type=int, default=500, help="Chunk size in characters")
    
    args = parser.parse_args()
    
    generator = EmbeddingsGenerator(
        vault_path=args.vault_path,
        model_name=args.model
    )
    
    embeddings_data = generator.generate_embeddings(force_regenerate=args.force)
    generator.save_embeddings(embeddings_data)


if __name__ == "__main__":
    main()
