from fastapi import FastAPI, UploadFile, Form
import shutil
import os

from ocr import extract_text_from_pdf
from embed_store import VectorStore
from rag_pipeline import generate_answer

app = FastAPI()
vector_store = VectorStore()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ocr_results = extract_text_from_pdf(file_path)
    docs = [{"page": page, "text": text} for page, text in ocr_results]
    vector_store.add_documents(docs)

    return {"message": f"Uploaded and indexed {file.filename}"}

@app.post("/ask/")
async def ask_question(query: str = Form(...)):
    results = vector_store.search(query, k=3)
    answer = generate_answer(query, results)
    return {"answer": answer, "sources": results}
