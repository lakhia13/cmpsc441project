#!/usr/bin/env python3
"""
create_chromadb.py - UNIFIED ChromaDB Builder

Build modes:
    --mode full     : Build from all documents (default)
    --mode fast     : Build from first N documents (quick demo)
    --mode parts    : Build incrementally in parts
    --mode add      : Add new documents to existing DB

Usage:
    python create_chromadb.py                           # Full build
    python create_chromadb.py --mode fast --limit 200   # Quick demo with 200 docs
    python create_chromadb.py --mode parts --start 0 --count 100 --reset  # Part 1
    python create_chromadb.py --mode parts --start 100 --count 100        # Part 2
    python create_chromadb.py --mode add                # Add any new documents
"""

import argparse
import glob
import os
import shutil
from typing import List

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document

# ============================================================
# Configuration
# ============================================================

CHROMA_PATH = "chroma"
DATA_PATH = "./papers_md"
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
BATCH_SIZE = 50
EMBEDDING_MODEL = "nomic-embed-text"

# ============================================================
# Helper Functions
# ============================================================

def load_documents(file_paths: List[str]) -> List[Document]:
    """Load documents from file paths."""
    documents = []
    for i, file_path in enumerate(file_paths):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            doc = Document(page_content=content, metadata={"source": file_path})
            documents.append(doc)
            if (i + 1) % 500 == 0:
                print(f"  Loaded {i + 1}/{len(file_paths)} files...")
        except Exception as e:
            print(f"  Skipping {file_path}: {e}")
    return documents


def split_documents(documents: List[Document]) -> List[Document]:
    """Split documents into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True
    )
    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks")
    return chunks


def create_embeddings():
    """Create embedding function."""
    return OllamaEmbeddings(model=EMBEDDING_MODEL)


def save_chunks_to_chroma(chunks: List[Document], embeddings, reset: bool = False):
    """Save chunks to ChromaDB with batch processing."""
    if reset and os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
        print("Cleared existing database")
    
    db = None
    total_batches = (len(chunks) - 1) // BATCH_SIZE + 1
    
    for i in range(0, len(chunks), BATCH_SIZE):
        batch = chunks[i:i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        print(f"  Batch {batch_num}/{total_batches}...", end=" ", flush=True)
        
        try:
            if db is None and not os.path.exists(CHROMA_PATH):
                db = Chroma.from_documents(
                    documents=batch,
                    embedding=embeddings,
                    persist_directory=CHROMA_PATH,
                )
            else:
                if db is None:
                    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
                db.add_documents(batch)
            print("✓")
        except Exception as e:
            print(f"Error: {e}")
    
    return db


# ============================================================
# Build Modes
# ============================================================

def build_full(reset: bool = True):
    """Build ChromaDB from all documents."""
    print("=" * 60)
    print("🔨 FULL BUILD - All Documents")
    print("=" * 60)
    
    # Get all files
    md_files = sorted(glob.glob(os.path.join(DATA_PATH, "*.md")))
    print(f"Found {len(md_files)} markdown files")
    
    if not md_files:
        print("No files found!")
        return
    
    # Load and process
    print("\nLoading documents...")
    documents = load_documents(md_files)
    
    print("\nSplitting into chunks...")
    chunks = split_documents(documents)
    
    print("\nCreating embeddings and saving to ChromaDB...")
    embeddings = create_embeddings()
    save_chunks_to_chroma(chunks, embeddings, reset=reset)
    
    print(f"\n✅ Complete! Saved {len(chunks)} chunks from {len(documents)} documents")


def build_fast(limit: int = 200):
    """Build ChromaDB from first N documents (quick demo)."""
    print("=" * 60)
    print(f"⚡ FAST BUILD - First {limit} Documents")
    print("=" * 60)
    
    # Get limited files
    md_files = sorted(glob.glob(os.path.join(DATA_PATH, "*.md")))[:limit]
    print(f"Processing {len(md_files)} files")
    
    if not md_files:
        print("No files found!")
        return
    
    # Load and process
    print("\nLoading documents...")
    documents = load_documents(md_files)
    
    print("\nSplitting into chunks...")
    chunks = split_documents(documents)
    
    print("\nCreating embeddings and saving to ChromaDB...")
    embeddings = create_embeddings()
    save_chunks_to_chroma(chunks, embeddings, reset=True)
    
    print(f"\n✅ Complete! Saved {len(chunks)} chunks from {len(documents)} documents")


def build_parts(start: int, count: int, reset: bool = False):
    """Build ChromaDB incrementally in parts."""
    print("=" * 60)
    print(f"📦 PARTS BUILD - Documents {start} to {start + count}")
    print("=" * 60)
    
    # Get all files
    all_files = sorted(glob.glob(os.path.join(DATA_PATH, "*.md")))
    total_files = len(all_files)
    print(f"Total documents available: {total_files}")
    
    # Select files for this batch
    files_to_process = all_files[start:start + count]
    
    if not files_to_process:
        print("No files to process in this range!")
        return
    
    print(f"Processing: {start} to {min(start + count, total_files)}")
    
    # Load and process
    print("\nLoading documents...")
    documents = load_documents(files_to_process)
    
    print("\nSplitting into chunks...")
    chunks = split_documents(documents)
    
    print("\nCreating embeddings and saving to ChromaDB...")
    embeddings = create_embeddings()
    save_chunks_to_chroma(chunks, embeddings, reset=reset)
    
    print(f"\n✅ Done! Processed documents {start} to {start + len(documents)}")
    
    next_start = start + count
    if next_start < total_files:
        print(f"   Next: python create_chromadb.py --mode parts --start {next_start} --count {count}")
    else:
        print("   All documents processed!")


def build_add():
    """Add new documents to existing ChromaDB."""
    print("=" * 60)
    print("➕ ADD MODE - Add New Documents")
    print("=" * 60)
    
    if not os.path.exists(CHROMA_PATH):
        print("No existing database found. Run full build first.")
        return
    
    # Load existing DB to check what's already there
    embeddings = create_embeddings()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    
    # Get existing sources
    existing_sources = set()
    try:
        results = db.get()
        for meta in results.get('metadatas', []):
            if meta and 'source' in meta:
                existing_sources.add(meta['source'])
    except:
        pass
    
    print(f"Existing documents in DB: {len(existing_sources)}")
    
    # Get all files
    all_files = set(glob.glob(os.path.join(DATA_PATH, "*.md")))
    new_files = [f for f in all_files if f not in existing_sources]
    
    print(f"New documents to add: {len(new_files)}")
    
    if not new_files:
        print("No new documents to add!")
        return
    
    # Load and process new files
    print("\nLoading new documents...")
    documents = load_documents(sorted(new_files))
    
    print("\nSplitting into chunks...")
    chunks = split_documents(documents)
    
    print("\nAdding to ChromaDB...")
    save_chunks_to_chroma(chunks, embeddings, reset=False)
    
    print(f"\n✅ Added {len(chunks)} chunks from {len(documents)} new documents")


def show_status():
    """Show current ChromaDB status."""
    print("=" * 60)
    print("📊 ChromaDB Status")
    print("=" * 60)
    
    # Count source files
    md_files = glob.glob(os.path.join(DATA_PATH, "*.md"))
    print(f"Source documents: {len(md_files)}")
    
    # Check ChromaDB
    if os.path.exists(CHROMA_PATH):
        try:
            embeddings = create_embeddings()
            db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
            count = db._collection.count()
            print(f"ChromaDB chunks: {count}")
            
            # Get size
            size = sum(
                os.path.getsize(os.path.join(dirpath, filename))
                for dirpath, dirnames, filenames in os.walk(CHROMA_PATH)
                for filename in filenames
            )
            print(f"Database size: {size / 1024 / 1024:.1f} MB")
        except Exception as e:
            print(f"Error reading DB: {e}")
    else:
        print("ChromaDB: Not created yet")


# ============================================================
# Main
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description="Unified ChromaDB Builder",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python create_chromadb.py                                    # Full build
    python create_chromadb.py --mode fast --limit 200            # Quick demo
    python create_chromadb.py --mode parts --start 0 --count 100 --reset  # Start parts
    python create_chromadb.py --mode parts --start 100 --count 100        # Continue
    python create_chromadb.py --mode add                         # Add new docs
    python create_chromadb.py --mode status                      # Check status
        """
    )
    parser.add_argument("--mode", choices=["full", "fast", "parts", "add", "status"],
                       default="full", help="Build mode")
    parser.add_argument("--limit", type=int, default=200,
                       help="Document limit for fast mode")
    parser.add_argument("--start", type=int, default=0,
                       help="Start index for parts mode")
    parser.add_argument("--count", type=int, default=100,
                       help="Document count for parts mode")
    parser.add_argument("--reset", action="store_true",
                       help="Clear existing database first")
    
    args = parser.parse_args()
    
    if args.mode == "full":
        build_full(reset=args.reset if args.reset else True)
    elif args.mode == "fast":
        build_fast(limit=args.limit)
    elif args.mode == "parts":
        build_parts(start=args.start, count=args.count, reset=args.reset)
    elif args.mode == "add":
        build_add()
    elif args.mode == "status":
        show_status()


if __name__ == "__main__":
    main()
