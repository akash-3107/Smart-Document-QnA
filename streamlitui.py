import streamlit as st

from ocr import extract_text_from_pdf
from embed_store import VectorStore
from rag_pipeline import generate_answer

# Initialize vector store once
if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()
    st.session_state.docs_loaded = False

st.set_page_config(page_title="Smart Document Q&A", layout="wide")
st.title("Smart Document Q&A System")

# --- Upload PDF ---
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_file is not None and not st.session_state.docs_loaded:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Extracting text with OCR..."):
        ocr_results = extract_text_from_pdf("temp.pdf")
        docs = [{"page": page, "text": text} for page, text in ocr_results]
        st.session_state.vector_store.add_documents(docs)
        st.session_state.docs_loaded = True
    st.success("Document processed and indexed!")

# --- Chat Interface ---
if st.session_state.docs_loaded:
    query = st.text_input("Ask a question about your document:")

    if query:
        with st.spinner("Thinking..."):
            results = st.session_state.vector_store.search(query, k=3)
            answer = generate_answer(query, results)

        st.markdown("###Answer:")
        st.write(answer)

        with st.expander("Sources"):
            for r in results:
                st.markdown(f"**Page {r['page']}**: {r['text'][:300]}...")

