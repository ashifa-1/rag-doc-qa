from sentence_transformers import SentenceTransformer

class TextEmbedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        try:
            self.model = SentenceTransformer(model_name, local_files_only=True)
        except Exception:
            self.model = SentenceTransformer(model_name)

    def embed_chunks(self, chunks, batch_size=64):
        texts = [chunk["chunk_text"] for chunk in chunks]
        embeddings = self.model.encode(
            texts,
            batch_size=batch_size,
            show_progress_bar=True,
            convert_to_numpy=True
        )
        return embeddings

