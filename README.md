#  Mental Health Chatbot

## fetch

```bash
python3 fetch.py --query "Paraventricular hypothalamic nucleus" --outdir ./pubmed_pdfs --top 30 --search-pool 40
```

## pdf2md
TODO: handle images and diagrams

```bash
python3 pdf2md.py ./pubmed_pdfs ./papers_md
```

## create_chromadb
TODO: Add pgvector support and benchmark

```bash
python3 create_chromadb.py
```

## rag_query
TODO: fix arguments (embeddings, etc.)
```bash
python3 rag_query.py "What are the functions of hypothalamic paraventricular nucleus in human body?"   --k 5  --embed_model nomic-embed-text   --chat_model gemma3:latest
```

## TODO

1. Change fetch.py to pull from sources like Mayo Clinic, WebMD, NIH or other relevant sites
2. Explore other embedding models, vector dbs and LLMs. (easy due to Ollama support)
3. Develop a web UI (Streamlit/Gradio/Flask/React?) 
4. Change system prompt and add guardrails.