import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.docs = []

    def add_documents(self, docs):
        """
        docs: list of {"page": int, "text": str}
        """
        texts = [d["text"] for d in docs]
        embeddings = self.model.encode(texts)
        embeddings = np.array(embeddings).astype("float32")

        if self.index is None:
            dim = embeddings.shape[1]
            self.index = faiss.IndexFlatL2(dim)
        
        self.index.add(embeddings)
        self.docs.extend(docs)

    def search(self, query, k=3):
        query_emb = self.model.encode([query]).astype("float32")
        D, I = self.index.search(query_emb, k)
        results = []
        for idx in I[0]:
            results.append(self.docs[idx])
        return results
