import streamlit as st
from typing import List, Tuple
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain_core.messages import SystemMessage, HumanMessage
import time
import json
from datetime import datetime

# ---- CSS for Light Mode ----
LIGHT_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --bg-primary: #f8fafc;
    --bg-secondary: #ffffff;
    --bg-tertiary: #f1f5f9;
    --text-primary: #0f172a;
    --text-secondary: #475569;
    --text-muted: #64748b;
    --border-color: #e2e8f0;
    --accent-primary: #0ea5e9;
    --accent-secondary: #0284c7;
    --accent-light: #e0f2fe;
    --accent-lighter: #f0f9ff;
    --success-bg: #ecfdf5;
    --success-border: #a7f3d0;
    --success-text: #065f46;
    --danger-bg: #fef2f2;
    --danger-border: #fecaca;
    --danger-text: #991b1b;
    --warning-bg: #fffbeb;
    --warning-border: #fde68a;
    --warning-text: #92400e;
    --user-bubble: #f1f5f9;
    --user-border: #e2e8f0;
    --assistant-bubble: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
    --assistant-border: #bae6fd;
    --sidebar-bg: linear-gradient(180deg, #f8fafc 0%, #f1f5f9 100%);
    --header-bg: linear-gradient(135deg, #e0f2fe 0%, #f0f9ff 50%, #e0f2fe 100%);
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.05);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: var(--bg-primary);
}

.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 920px;
}

/* Header */
.app-header {
    background: var(--header-bg);
    padding: 1.8rem 2rem;
    border-radius: 1rem;
    border: 1px solid var(--border-color);
    margin-bottom: 1.25rem;
    box-shadow: var(--shadow-sm);
}
.app-badge {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent-secondary);
    background: var(--bg-secondary);
    border: 1px solid var(--accent-primary);
    border-radius: 999px;
    padding: 0.2rem 0.75rem;
    display: inline-block;
    margin-bottom: 0.5rem;
}
.app-title {
    font-size: 1.85rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    line-height: 1.25;
}
.app-subtitle {
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
    line-height: 1.5;
}

/* Crisis Banner */
.crisis-banner {
    background: var(--danger-bg);
    border: 1px solid var(--danger-border);
    border-left: 4px solid #ef4444;
    border-radius: 0.75rem;
    padding: 0.85rem 1.1rem;
    font-size: 0.88rem;
    color: var(--danger-text);
    margin-bottom: 1rem;
}

/* Info Card */
.info-card {
    background: var(--bg-secondary);
    border-radius: 0.85rem;
    padding: 1.1rem 1.3rem;
    border: 1px solid var(--border-color);
    font-size: 0.9rem;
    color: var(--text-secondary);
    box-shadow: var(--shadow-sm);
    margin-bottom: 1rem;
}
.info-card ul {
    margin: 0.4rem 0 0 0;
    padding-left: 1.2rem;
}
.info-card li {
    margin-bottom: 0.25rem;
}

/* Stats Card */
.stats-card {
    background: var(--success-bg);
    border-radius: 0.85rem;
    padding: 0.9rem 1.2rem;
    border: 1px solid var(--success-border);
    font-size: 0.88rem;
    color: var(--success-text);
    margin-bottom: 1rem;
}
.stats-sources {
    font-size: 0.78rem;
    opacity: 0.85;
    margin-top: 0.2rem;
}

/* Chat Bubbles */
.chat-user {
    background: var(--user-bubble);
    border-radius: 1rem 1rem 0.25rem 1rem;
    padding: 0.9rem 1.15rem;
    border: 1px solid var(--user-border);
    color: var(--text-primary);
    font-size: 0.92rem;
    line-height: 1.6;
}
.chat-assistant {
    background: var(--assistant-bubble);
    border-radius: 1rem 1rem 1rem 0.25rem;
    padding: 1rem 1.2rem;
    border: 1px solid var(--assistant-border);
    border-left: 3px solid var(--accent-primary);
    color: var(--text-primary);
    font-size: 0.92rem;
    line-height: 1.65;
    box-shadow: var(--shadow-sm);
}

/* Response Time */
.response-time {
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-top: 0.4rem;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--sidebar-bg);
}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: var(--text-secondary);
}

/* Sample Question Buttons */
.sample-q {
    background: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.82rem;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s ease;
    display: block;
    width: 100%;
    text-align: left;
    margin-bottom: 0.4rem;
}
.sample-q:hover {
    background: var(--accent-lighter);
    border-color: var(--accent-primary);
    color: var(--accent-secondary);
}

/* Input */
.stChatInput > div {
    border-radius: 0.85rem !important;
    border: 2px solid var(--border-color) !important;
    background: var(--bg-secondary) !important;
}
.stChatInput > div:focus-within {
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 3px rgba(14, 165, 233, 0.15) !important;
}
.stChatInput input, .stChatInput textarea {
    color: var(--text-primary) !important;
    caret-color: var(--text-primary) !important;
}
.stChatInput input::placeholder, .stChatInput textarea::placeholder {
    color: var(--text-muted) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    color: white;
    border: none;
    border-radius: 0.5rem;
    padding: 0.45rem 1rem;
    font-weight: 500;
    font-size: 0.85rem;
    transition: all 0.2s ease;
    box-shadow: 0 2px 6px rgba(14, 165, 233, 0.25);
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(14, 165, 233, 0.35);
}

/* Footer */
.footer-note {
    text-align: center;
    font-size: 0.78rem;
    color: var(--text-muted);
    padding: 0.8rem;
    background: var(--bg-tertiary);
    border-radius: 0.6rem;
}

/* Expander */
.streamlit-expanderHeader {
    font-size: 0.82rem;
    color: var(--text-secondary);
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}
.chat-user, .chat-assistant {
    animation: fadeIn 0.25s ease-out;
}

/* Mode Toggle */
.mode-toggle {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem;
    background: var(--bg-tertiary);
    border-radius: 0.5rem;
    margin-bottom: 1rem;
}
</style>
"""

# ---- CSS for Dark Mode ----
DARK_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

:root {
    --bg-primary: #0f172a;
    --bg-secondary: #1e293b;
    --bg-tertiary: #334155;
    --text-primary: #f1f5f9;
    --text-secondary: #cbd5e1;
    --text-muted: #94a3b8;
    --border-color: #334155;
    --accent-primary: #38bdf8;
    --accent-secondary: #0ea5e9;
    --accent-light: #0c4a6e;
    --accent-lighter: #082f49;
    --success-bg: #064e3b;
    --success-border: #065f46;
    --success-text: #6ee7b7;
    --danger-bg: #450a0a;
    --danger-border: #7f1d1d;
    --danger-text: #fca5a5;
    --warning-bg: #451a03;
    --warning-border: #78350f;
    --warning-text: #fcd34d;
    --user-bubble: #334155;
    --user-border: #475569;
    --assistant-bubble: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    --assistant-border: #0369a1;
    --sidebar-bg: linear-gradient(180deg, #1e293b 0%, #0f172a 100%);
    --header-bg: linear-gradient(135deg, #0c4a6e 0%, #1e293b 50%, #0c4a6e 100%);
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.4);
}

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: var(--bg-primary);
}

.main .block-container {
    padding-top: 1.5rem;
    padding-bottom: 3rem;
    max-width: 920px;
}

/* Header */
.app-header {
    background: var(--header-bg);
    padding: 1.8rem 2rem;
    border-radius: 1rem;
    border: 1px solid var(--border-color);
    margin-bottom: 1.25rem;
    box-shadow: var(--shadow-md);
}
.app-badge {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: var(--accent-primary);
    background: var(--bg-secondary);
    border: 1px solid var(--accent-primary);
    border-radius: 999px;
    padding: 0.2rem 0.75rem;
    display: inline-block;
    margin-bottom: 0.5rem;
}
.app-title {
    font-size: 1.85rem;
    font-weight: 700;
    color: var(--text-primary);
    margin: 0;
    line-height: 1.25;
}
.app-subtitle {
    font-size: 0.95rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
    line-height: 1.5;
}

/* Crisis Banner */
.crisis-banner {
    background: var(--danger-bg);
    border: 1px solid var(--danger-border);
    border-left: 4px solid #ef4444;
    border-radius: 0.75rem;
    padding: 0.85rem 1.1rem;
    font-size: 0.88rem;
    color: var(--danger-text);
    margin-bottom: 1rem;
}

/* Info Card */
.info-card {
    background: var(--bg-secondary);
    border-radius: 0.85rem;
    padding: 1.1rem 1.3rem;
    border: 1px solid var(--border-color);
    font-size: 0.9rem;
    color: var(--text-secondary);
    box-shadow: var(--shadow-sm);
    margin-bottom: 1rem;
}
.info-card ul {
    margin: 0.4rem 0 0 0;
    padding-left: 1.2rem;
}
.info-card li {
    margin-bottom: 0.25rem;
}

/* Stats Card */
.stats-card {
    background: var(--success-bg);
    border-radius: 0.85rem;
    padding: 0.9rem 1.2rem;
    border: 1px solid var(--success-border);
    font-size: 0.88rem;
    color: var(--success-text);
    margin-bottom: 1rem;
}
.stats-sources {
    font-size: 0.78rem;
    opacity: 0.85;
    margin-top: 0.2rem;
}

/* Chat Bubbles */
.chat-user {
    background: var(--user-bubble);
    border-radius: 1rem 1rem 0.25rem 1rem;
    padding: 0.9rem 1.15rem;
    border: 1px solid var(--user-border);
    color: var(--text-primary);
    font-size: 0.92rem;
    line-height: 1.6;
}
.chat-assistant {
    background: var(--assistant-bubble);
    border-radius: 1rem 1rem 1rem 0.25rem;
    padding: 1rem 1.2rem;
    border: 1px solid var(--assistant-border);
    border-left: 3px solid var(--accent-primary);
    color: var(--text-primary);
    font-size: 0.92rem;
    line-height: 1.65;
    box-shadow: var(--shadow-sm);
}

/* Response Time */
.response-time {
    font-size: 0.72rem;
    color: var(--text-muted);
    margin-top: 0.4rem;
    display: flex;
    align-items: center;
    gap: 0.3rem;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: var(--sidebar-bg);
}
section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    color: var(--text-secondary);
}
section[data-testid="stSidebar"] .stSlider label {
    color: var(--text-secondary) !important;
}

/* Sample Question Buttons */
.sample-q {
    background: var(--bg-tertiary);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    padding: 0.5rem 0.75rem;
    font-size: 0.82rem;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.15s ease;
    display: block;
    width: 100%;
    text-align: left;
    margin-bottom: 0.4rem;
}
.sample-q:hover {
    background: var(--accent-lighter);
    border-color: var(--accent-primary);
    color: var(--accent-primary);
}

/* Input */
.stChatInput > div {
    border-radius: 0.85rem !important;
    border: 2px solid var(--border-color) !important;
    background: var(--bg-secondary) !important;
}
.stChatInput > div:focus-within {
    border-color: var(--accent-primary) !important;
    box-shadow: 0 0 0 3px rgba(56, 189, 248, 0.2) !important;
}
.stChatInput input {
    color: var(--text-primary) !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
    color: var(--bg-primary);
    border: none;
    border-radius: 0.5rem;
    padding: 0.45rem 1rem;
    font-weight: 600;
    font-size: 0.85rem;
    transition: all 0.2s ease;
    box-shadow: 0 2px 8px rgba(56, 189, 248, 0.3);
}
.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 4px 14px rgba(56, 189, 248, 0.4);
}

/* Footer */
.footer-note {
    text-align: center;
    font-size: 0.78rem;
    color: var(--text-muted);
    padding: 0.8rem;
    background: var(--bg-secondary);
    border-radius: 0.6rem;
    border: 1px solid var(--border-color);
}

/* Expander */
.streamlit-expanderHeader {
    font-size: 0.82rem;
    color: var(--text-secondary);
    background: var(--bg-secondary);
}

/* Animation */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(8px); }
    to { opacity: 1; transform: translateY(0); }
}
.chat-user, .chat-assistant {
    animation: fadeIn 0.25s ease-out;
}

/* Text inputs in dark mode */
.stTextInput input {
    background: var(--bg-tertiary) !important;
    color: var(--text-primary) !important;
    border-color: var(--border-color) !important;
}

/* Slider */
.stSlider > div > div > div {
    background: var(--bg-tertiary) !important;
}
</style>
"""

CHROMA_PATH = "chroma"

SYSTEM_PROMPT = """You are a mental health assistant providing evidence-based information.

Rules:
1) Use ONLY the provided context to answer. Do not make up information.
2) If the answer is not in the context, say: "I don't have enough information to answer that question. Please consult a mental health professional."
3) Be warm, supportive, and empathetic in your tone.
4) Include inline citations like [1], [2] referring to the sources provided.
5) NEVER provide specific diagnoses or treatment plans.
6) Always encourage consulting licensed professionals for personal concerns.
7) If someone appears to be in crisis, remind them of crisis resources (988 Lifeline).

Format:
- Conversational, supportive tone
- Use bullet points for lists
- Keep responses focused and helpful
- Include source citations [#]
"""


def format_context(docs_with_scores: List[Tuple]):
    """Join top-k chunks and build source map"""
    context_parts = []
    sources = []
    for i, (doc, score) in enumerate(docs_with_scores, start=1):
        src = doc.metadata.get("source", f"doc_{i}")
        sources.append(src)
        context_parts.append(f"[{i}] {doc.page_content.strip()}")
    context_text = "\n\n---\n\n".join(context_parts)
    return context_text, sources


def query_rag(query_text: str, k: int = 4, min_relevance: float = 0.3, 
              embed_model: str = "nomic-embed-text", chat_model: str = "llama3.1:8b"):
    """Query the RAG system and return response with sources"""
    
    embeddings = OllamaEmbeddings(model=embed_model)
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    
    results = db.similarity_search_with_relevance_scores(query_text, k=k)
    if not results:
        return (
            "I couldn't find any relevant information in the knowledge base. "
            "Try rephrasing your question or asking about a specific mental health topic.",
            [], 0
        )
    
    results = [(d, s) for (d, s) in results if s >= min_relevance]
    if not results:
        return (
            "I couldn't find information relevant enough to answer that question confidently. "
            "Try asking about specific topics like depression, anxiety, PTSD, therapy types, or treatments.",
            [], 0
        )
    
    context_text, sources = format_context(results)
    
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=(
            f"Context:\n{context_text}\n\n"
            f"---\n\nQuestion: {query_text}\n\n"
            f"Sources (in order): {sources}"
        )),
    ]
    
    llm = ChatOllama(model=chat_model, temperature=0.0)
    
    start_time = time.time()
    response = llm.invoke(messages)
    elapsed = time.time() - start_time
    
    return response.content.strip(), sources, round(elapsed, 1)


def get_db_stats():
    """Get statistics about the ChromaDB"""
    try:
        import os
        import glob
        
        md_files = glob.glob(os.path.join("./papers_md", "*.md"))
        doc_count = len(md_files)
        
        embeddings = OllamaEmbeddings(model="nomic-embed-text")
        db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
        chunk_count = db._collection.count()
        
        return doc_count, chunk_count
    except:
        return None, None


def export_chat_history(messages):
    """Export chat history to JSON"""
    export_data = {
        "exported_at": datetime.now().isoformat(),
        "messages": messages
    }
    return json.dumps(export_data, indent=2)


def main():
    st.set_page_config(
        page_title="Mental Health Assistant",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session states
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False
    
    # Apply theme CSS
    if st.session_state.dark_mode:
        st.markdown(DARK_CSS, unsafe_allow_html=True)
    else:
        st.markdown(LIGHT_CSS, unsafe_allow_html=True)
    
    # ---- Sidebar ----
    with st.sidebar:
        st.markdown("### ⚙️ Settings")
        
        # Dark Mode Toggle
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("**Theme**")
        with col2:
            if st.button("🌙" if not st.session_state.dark_mode else "☀️", key="theme_toggle"):
                st.session_state.dark_mode = not st.session_state.dark_mode
                st.rerun()
        
        st.caption("Light Mode" if not st.session_state.dark_mode else "Dark Mode")
        
        st.divider()
        
        # Retrieval Settings
        st.markdown("**🔍 Retrieval**")
        k = st.slider(
            "Document snippets",
            min_value=1,
            max_value=15,
            value=5,
            help="Number of relevant passages to retrieve"
        )
        
        min_relevance = st.slider(
            "Relevance threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.25,
            step=0.05,
            help="Minimum similarity score (lower = more results)"
        )
        
        st.divider()
        
        # Model Settings
        st.markdown("**🤖 Models**")
        embed_model = st.text_input(
            "Embedding",
            value="nomic-embed-text",
        )
        chat_model = st.selectbox(
            "Chat Model",
            options=["llama3.1:8b", "gemma3:latest", "mistral:latest"],
            index=0
        )
        
        st.divider()
        
        # Sample Questions
        st.markdown("**💡 Quick Questions**")
        sample_questions = [
            "What is depression?",
            "How is anxiety treated?",
            "What are PTSD symptoms?",
            "How does CBT work?",
            "What is bipolar disorder?",
            "How can I manage stress?",
            "What is mindfulness?",
        ]
        
        for q in sample_questions:
            if st.button(f"→ {q}", key=f"sample_{q}", use_container_width=True):
                st.session_state.pending_question = q
                st.rerun()
        
        st.divider()
        
        # Actions
        st.markdown("**📋 Actions**")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Clear", use_container_width=True):
                st.session_state.messages = []
                st.rerun()
        with col2:
            if st.session_state.messages:
                export_data = export_chat_history(st.session_state.messages)
                st.download_button(
                    "📥 Export",
                    data=export_data,
                    file_name=f"chat_export_{datetime.now().strftime('%Y%m%d_%H%M')}.json",
                    mime="application/json",
                    use_container_width=True
                )
    
    # ---- Main Content ----
    
    # Header
    st.markdown(
        """
        <div class="app-header">
            <div class="app-badge">🧠 Evidence-Based Resource</div>
            <h1 class="app-title">Mental Health Assistant</h1>
            <p class="app-subtitle">
                Get information from peer-reviewed research and trusted clinical sources. 
                This is an educational tool—not a substitute for professional care.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Crisis Banner
    st.markdown(
        """
        <div class="crisis-banner">
            <strong>🆘 In Crisis?</strong> Call or text <strong>988</strong> (Suicide & Crisis Lifeline) 
            or go to your nearest emergency room immediately.
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    # Two columns for info and stats
    col1, col2 = st.columns([1.5, 1])
    
    with col1:
        st.markdown(
            """
            <div class="info-card">
                <strong>ℹ️ Important Notice</strong>
                <ul>
                    <li>This assistant is for <em>educational purposes only</em></li>
                    <li>Not for emergencies or crisis situations</li>
                    <li>Always consult a licensed mental health professional</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        doc_count, chunk_count = get_db_stats()
        if doc_count and chunk_count:
            st.markdown(
                f"""
                <div class="stats-card">
                    <strong>📚 Knowledge Base</strong><br>
                    {doc_count:,} articles · {chunk_count:,} passages
                    <div class="stats-sources">
                        PubMed · NIMH · Mayo Clinic · NAMI · CDC · WebMD · Healthline & more
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    
    st.markdown("")
    
    # Handle pending question from sidebar
    if "pending_question" in st.session_state:
        pending = st.session_state.pending_question
        del st.session_state.pending_question
        st.session_state.messages.append({"role": "user", "content": pending})
        
        # Generate response
        response, sources, elapsed = query_rag(
            pending, k=k, min_relevance=min_relevance,
            embed_model=embed_model, chat_model=chat_model
        )
        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "sources": sources,
            "time": elapsed
        })
        st.rerun()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            css_class = "chat-user" if message["role"] == "user" else "chat-assistant"
            st.markdown(
                f"<div class='{css_class}'>{message['content']}</div>",
                unsafe_allow_html=True,
            )
            
            if message["role"] == "assistant":
                # Show response time
                if "time" in message:
                    st.markdown(
                        f"<div class='response-time'>⏱️ {message['time']}s</div>",
                        unsafe_allow_html=True,
                    )
                
                # Show sources
                if "sources" in message and message["sources"]:
                    with st.expander("📖 View Sources"):
                        for i, source in enumerate(message["sources"], 1):
                            source_name = source.split("/")[-1] if "/" in source else source
                            st.caption(f"[{i}] {source_name}")
    
    # Chat input
    if prompt := st.chat_input("Ask about mental health topics..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(
                f"<div class='chat-user'>{prompt}</div>",
                unsafe_allow_html=True,
            )
        
        with st.chat_message("assistant"):
            with st.spinner("Searching knowledge base..."):
                try:
                    response, sources, elapsed = query_rag(
                        prompt, k=k, min_relevance=min_relevance,
                        embed_model=embed_model, chat_model=chat_model
                    )
                    
                    st.markdown(
                        f"<div class='chat-assistant'>{response}</div>",
                        unsafe_allow_html=True,
                    )
                    
                    st.markdown(
                        f"<div class='response-time'>⏱️ {elapsed}s</div>",
                        unsafe_allow_html=True,
                    )
                    
                    if sources:
                        with st.expander("📖 View Sources"):
                            for i, source in enumerate(sources, 1):
                                source_name = source.split("/")[-1] if "/" in source else source
                                st.caption(f"[{i}] {source_name}")
                    
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": response,
                        "sources": sources,
                        "time": elapsed
                    })
                    
                except Exception as e:
                    st.error(f"Error: {str(e)}")
                    st.info("Make sure Ollama is running: `ollama serve`")
    
    # Footer
    st.divider()
    st.markdown(
        """
        <div class="footer-note">
            <strong>CMPSC 441</strong> · Mental Health RAG Project · 
            Built with LangChain · ChromaDB · Ollama
        </div>
        """,
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
