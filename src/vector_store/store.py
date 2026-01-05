import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim: int):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def add_embeddings(self, embeddings, chunks):
        self.index.add(embeddings)
        self.metadata.extend(chunks)

    def search(self, query_embedding, top_k=5):
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            chunk = self.metadata[idx]
            results.append({
                "text": chunk["chunk_text"],
                "source": chunk["source"],
                "page": chunk["page"],
                "score": float(dist)
            })

        return results
