import faiss
import numpy as np
import pickle
from pathlib import Path

class VectorStore:
    def __init__(self, embedding_dim: int = 384):
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.metadata = []

    def add_embeddings(self, embeddings, chunks):
        embeddings = np.ascontiguousarray(embeddings, dtype=np.float32)
        self.index.add(embeddings)
        self.metadata.extend(chunks)

    def search(self, query_embedding, top_k=5):
        if self.index.ntotal == 0:
            return []

        k = min(top_k, self.index.ntotal)
        query_embedding = np.ascontiguousarray(query_embedding, dtype=np.float32)
        distances, indices = self.index.search(query_embedding, k)

        results = []
        for idx, dist in zip(indices[0], distances[0]):
            if idx == -1:
                continue
            chunk = self.metadata[idx]
            results.append({
                "text": chunk["chunk_text"],
                "source": chunk["source"],
                "page": chunk["page"],
                "score": float(dist)
            })

        return results

    def save(self, cache_dir: str = "data/cache"):
        dir_path = Path(cache_dir)
        dir_path.mkdir(parents=True, exist_ok=True)
        faiss.write_index(self.index, str(dir_path / "index.faiss"))
        with open(dir_path / "metadata.pkl", "wb") as f:
            pickle.dump(self.metadata, f)

    @classmethod
    def load(cls, cache_dir: str = "data/cache"):
        dir_path = Path(cache_dir)
        index_file = dir_path / "index.faiss"
        meta_file = dir_path / "metadata.pkl"
        if not index_file.exists() or not meta_file.exists():
            return None

        index = faiss.read_index(str(index_file))
        with open(meta_file, "rb") as f:
            metadata = pickle.load(f)

        store = cls(embedding_dim=index.d)
        store.index = index
        store.metadata = metadata
        return store


