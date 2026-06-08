"""
Query Engine for RAG (Retrieval Augmented Generation)
Combines semantic search with LLM generation
"""

import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    print("⚠️ sentence-transformers required")

from vector_store import VectorStore


class QueryEngine:
    """RAG query engine combining retrieval + generation"""
    
    def __init__(
        self,
        index_path: Path,
        model_name: str = "all-MiniLM-L6-v2",
        llm_endpoint: Optional[str] = "http://localhost:11434"
    ):
        """
        Initialize query engine
        
        Args:
            index_path: Path to FAISS index
            model_name: Embedding model name
            llm_endpoint: Ollama endpoint for generation
        """
        self.index_path = Path(index_path)
        self.model_name = model_name
        self.llm_endpoint = llm_endpoint
        
        # Load vector store
        print("🔄 Loading vector store...")
        self.vector_store = VectorStore()
        self.vector_store.load_index(self.index_path)
        
        # Load embedding model
        print(f"🔄 Loading embedding model: {model_name}")
        self.embedding_model = SentenceTransformer(model_name)
        
        print("✅ Query engine ready!")
    
    def retrieve(self, query: str, top_k: int = 5, min_score: float = 0.3) -> List[Dict]:
        """
        Retrieve relevant chunks for query
        
        Args:
            query: User question
            top_k: Number of chunks to retrieve
            min_score: Minimum relevance score
            
        Returns:
            List of relevant chunks with metadata
        """
        results = self.vector_store.search(
            query=query,
            model=self.embedding_model,
            top_k=top_k,
            min_score=min_score
        )
        
        return results
    
    def format_context(self, chunks: List[Dict], max_tokens: int = 2000) -> str:
        """
        Format retrieved chunks into context for LLM
        
        Args:
            chunks: Retrieved chunks
            max_tokens: Max context length (approx chars/4)
            
        Returns:
            Formatted context string
        """
        context_parts = []
        total_chars = 0
        max_chars = max_tokens * 4  # Rough token estimate
        
        for chunk in chunks:
            # Format: [file.md > Heading] content
            header = f"[{chunk['file']}"
            if chunk.get('heading'):
                header += f" > {chunk['heading']}"
            header += "]"
            
            chunk_text = f"{header}\n{chunk['text']}\n"
            chunk_chars = len(chunk_text)
            
            if total_chars + chunk_chars > max_chars:
                break
            
            context_parts.append(chunk_text)
            total_chars += chunk_chars
        
        return "\n---\n".join(context_parts)
    
    def generate_with_ollama(
        self, 
        query: str, 
        context: str,
        model: str = "llama3.1:8b",
        stream: bool = False
    ) -> str:
        """
        Generate answer using Ollama
        
        Args:
            query: User question
            context: Retrieved context
            model: Ollama model name
            stream: Stream response
            
        Returns:
            Generated answer
        """
        import requests
        
        prompt = f"""You are a helpful assistant with access to a knowledge base.
Use the following context to answer the question. If the context doesn't contain the answer, say so.

Context:
{context}

Question: {query}

Answer:"""
        
        payload = {
            "model": model,
            "prompt": prompt,
            "stream": stream
        }
        
        try:
            response = requests.post(
                f"{self.llm_endpoint}/api/generate",
                json=payload,
                stream=stream
            )
            
            if stream:
                # Stream tokens
                answer = ""
                for line in response.iter_lines():
                    if line:
                        data = json.loads(line)
                        token = data.get("response", "")
                        answer += token
                        print(token, end="", flush=True)
                print()  # Newline after stream
                return answer
            else:
                # Get full response
                result = response.json()
                return result.get("response", "")
        
        except Exception as e:
            return f"❌ Error generating response: {e}"
    
    def query(
        self,
        question: str,
        top_k: int = 5,
        use_llm: bool = True,
        llm_model: str = "llama3.1:8b",
        stream: bool = False,
        return_sources: bool = True
    ) -> Dict:
        """
        Full RAG query: retrieve + generate
        
        Args:
            question: User question
            top_k: Number of chunks to retrieve
            use_llm: Generate answer with LLM
            llm_model: Ollama model
            stream: Stream LLM response
            return_sources: Include source chunks in response
            
        Returns:
            Dict with answer and sources
        """
        # 1. Retrieve relevant chunks
        print(f"🔍 Retrieving context for: '{question}'")
        chunks = self.retrieve(question, top_k=top_k)
        
        if not chunks:
            return {
                "answer": "No relevant information found in the knowledge base.",
                "sources": [],
                "query": question
            }
        
        # 2. Format context
        context = self.format_context(chunks)
        
        # 3. Generate answer (if LLM enabled)
        answer = None
        if use_llm:
            print(f"🤖 Generating answer with {llm_model}...")
            answer = self.generate_with_ollama(
                query=question,
                context=context,
                model=llm_model,
                stream=stream
            )
        
        # 4. Format response
        response = {
            "answer": answer,
            "query": question,
            "timestamp": datetime.now().isoformat()
        }
        
        if return_sources:
            response["sources"] = [
                {
                    "file": chunk["file"],
                    "heading": chunk.get("heading", ""),
                    "score": chunk["score"],
                    "preview": chunk["text"][:200] + "..."
                }
                for chunk in chunks
            ]
        
        return response
    
    def batch_query(self, questions: List[str], **kwargs) -> List[Dict]:
        """
        Process multiple queries
        
        Args:
            questions: List of questions
            **kwargs: Passed to query()
            
        Returns:
            List of response dicts
        """
        results = []
        
        for i, question in enumerate(questions, 1):
            print(f"\n{'='*60}")
            print(f"Query {i}/{len(questions)}: {question}")
            print('='*60)
            
            result = self.query(question, **kwargs)
            results.append(result)
        
        return results
    
    def interactive_mode(self, llm_model: str = "llama3.1:8b"):
        """Interactive query loop"""
        print("\n" + "="*60)
        print("🤖 RAG Query Engine - Interactive Mode")
        print("="*60)
        print("Type your questions. Commands:")
        print("  /sources - Toggle showing sources")
        print("  /stats   - Show vector store stats")
        print("  /quit    - Exit")
        print("="*60 + "\n")
        
        show_sources = True
        
        while True:
            try:
                question = input("\n❓ Question: ").strip()
                
                if not question:
                    continue
                
                if question == "/quit":
                    print("👋 Goodbye!")
                    break
                
                if question == "/sources":
                    show_sources = not show_sources
                    print(f"✅ Sources: {'ON' if show_sources else 'OFF'}")
                    continue
                
                if question == "/stats":
                    stats = self.vector_store.stats()
                    print("\n📊 Vector Store Stats:")
                    for key, value in stats.items():
                        print(f"  {key}: {value}")
                    continue
                
                # Process query
                result = self.query(
                    question,
                    use_llm=True,
                    llm_model=llm_model,
                    stream=True,
                    return_sources=show_sources
                )
                
                # Show sources
                if show_sources and result.get("sources"):
                    print("\n📚 Sources:")
                    for i, source in enumerate(result["sources"], 1):
                        print(f"\n  {i}. {source['file']} (score: {source['score']:.3f})")
                        if source['heading']:
                            print(f"     Section: {source['heading']}")
            
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")


def main():
    """CLI for query engine"""
    import argparse
    
    parser = argparse.ArgumentParser(description="RAG Query Engine")
    parser.add_argument("--index", required=True, help="Path to FAISS index")
    parser.add_argument("--model", default="all-MiniLM-L6-v2", help="Embedding model")
    parser.add_argument("--llm", default="llama3.1:8b", help="Ollama model for generation")
    parser.add_argument("--query", help="Single query to execute")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    parser.add_argument("--no-llm", action="store_true", help="Retrieval only (no generation)")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results")
    
    args = parser.parse_args()
    
    # Initialize engine
    engine = QueryEngine(
        index_path=Path(args.index),
        model_name=args.model
    )
    
    if args.interactive:
        engine.interactive_mode(llm_model=args.llm)
    
    elif args.query:
        result = engine.query(
            question=args.query,
            top_k=args.top_k,
            use_llm=not args.no_llm,
            llm_model=args.llm,
            stream=True
        )
        
        if result.get("sources"):
            print("\n\n📚 Sources:")
            for i, source in enumerate(result["sources"], 1):
                print(f"\n{i}. {source['file']} (score: {source['score']:.3f})")
    
    else:
        print("❌ Use --query or --interactive")


if __name__ == "__main__":
    main()
