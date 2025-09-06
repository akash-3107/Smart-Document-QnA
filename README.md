# Smart-Document-QnA

Smart Document Q&A System

An end-to-end system that allows users to upload scanned PDFs or images and ask natural language questions.
The system uses OCR + Vector Databases + RAG + Prompt Engineering to extract, index, and retrieve answers with citations.


================================================================================



Features

1. OCR: Extracts text from scanned PDFs/images using Tesseract.

2. Vector Search: Stores document chunks in Faiss for semantic retrieval.

3. RAG Pipeline: Retrieval-Augmented Generation for grounded answers.

4. Prompt Engineering: Ensures concise, citation-backed responses.

5. Streamlit UI: Upload documents and chat in an interactive interface.

================================================================================


Architecture

PDF/Image → OCR → Text Chunks → Embeddings → Vector DB (Faiss)
                 ↓
           RAG Pipeline → Prompt Engine → LLM Response

================================================================================


Tech Stack

OCR: Tesseract OCR

Embeddings: SentenceTransformers / OpenAI

Vector Database: Faiss

LLM: OpenAI GPT (configurable)

Backend/UI: Streamlit / FastAPI

================================================================================


Usage

Upload a PDF or scanned image.

Ask a natural language question in the chat box.

Get an answer with citations.

