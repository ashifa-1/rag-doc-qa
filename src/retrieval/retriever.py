import numpy as np
class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k=5):
        query_embedding = self.embedder.model.encode(
            [query],
            convert_to_numpy=True
        )
        return self.vector_store.search(query_embedding, top_k)
