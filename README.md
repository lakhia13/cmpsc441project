# Mental Health RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot for mental health information, built with LangChain, ChromaDB, and Ollama.

## Features

- **3,400+ articles** from trusted sources (PubMed, NIMH, Mayo Clinic, NAMI, CDC, WebMD, etc.)
- **Local LLM** via Ollama (llama3.1, gemma3, mistral)
- **Vector search** with ChromaDB + nomic-embed-text
- **Streamlit UI** with dark/light mode, chat export, and source citations
- **Safety guardrails** for crisis situations

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama (in separate terminal)
ollama serve
ollama pull llama3.1:8b
ollama pull nomic-embed-text

# Run the chatbot
streamlit run streamlit_chatbot.py
```

## Project Structure

| File | Description |
|------|-------------|
| `streamlit_chatbot.py` | Web UI for the chatbot |
| `create_chromadb.py` | Build/manage the vector database |
| `fetch_all_sources.py` | Fetch articles from web sources |
| `fetch.py` | Fetch PDFs from PubMed |
| `pdf2md.py` | Convert PDFs to markdown |
| `rag_query.py` | Command-line RAG query tool |

## Data Sources

- **PubMed** - Peer-reviewed scientific papers
- **NIMH** - National Institute of Mental Health
- **Mayo Clinic** - Clinical condition guides
- **NAMI** - National Alliance on Mental Illness
- **CDC** - Centers for Disease Control
- **WebMD, Healthline, Verywell Mind** - Consumer health content
- **Mind UK, Mental Health Foundation** - UK resources
- **APA** - American Psychiatric Association

## Usage

### Build ChromaDB

```bash
# Full build (all documents)
python create_chromadb.py --mode full

# Quick demo (200 documents)
python create_chromadb.py --mode fast --limit 200

# Check status
python create_chromadb.py --mode status
```

### Fetch Content

```bash
# Fetch from all web sources
python fetch_all_sources.py --source all

# Fetch from specific sources
python fetch_all_sources.py --source nimh --source mayo
```

### Command-line Query

```bash
python rag_query.py "What is depression?" --k 5 --chat_model llama3.1:8b
```

## Requirements

- Python 3.8+
- Ollama with `llama3.1:8b` and `nomic-embed-text` models
- ~3GB disk space for ChromaDB

## Team

CMPSC 441 - Fall 2025
