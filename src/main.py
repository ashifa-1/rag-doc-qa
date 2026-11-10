import sys
from pathlib import Path
from src.loaders.pdf_loader import load_pdf_documents
from src.loaders.txt_loader import load_txt_documents
from src.chunking.text_chunker import chunk_text
from src.embeddings.embedder import TextEmbedder
from src.vector_store.store import VectorStore
from src.retrieval.retriever import Retriever
from src.prompts.rag_prompt import build_rag_prompt
from src.generation.answer_generator import AnswerGenerator


def is_cache_valid(cache_dir="data/cache", source_dirs=("data/raw/pdfs", "data/raw/txts")):
    cache_file = Path(cache_dir) / "index.faiss"
    meta_file = Path(cache_dir) / "metadata.pkl"
    if not cache_file.exists() or not meta_file.exists():
        return False
    cache_mtime = min(cache_file.stat().st_mtime, meta_file.stat().st_mtime)
    for d in source_dirs:
        folder = Path(d)
        if folder.exists():
            for f in folder.iterdir():
                if f.is_file() and f.stat().st_mtime > cache_mtime:
                    return False
    return True


def run_cli():
    force_rebuild = "--rebuild" in sys.argv
    cache_dir = "data/cache"

    embedder = TextEmbedder()

    if not force_rebuild and is_cache_valid(cache_dir):
        print(" Loading cached vector store from disk...")
        vector_store = VectorStore.load(cache_dir)
        print(f" Vector store loaded ({vector_store.index.ntotal} chunks) in instant mode.")
    else:
        print(" Loading documents...")
        pdf_docs = load_pdf_documents("data/raw/pdfs")
        txt_docs = load_txt_documents("data/raw/txts")
        all_docs = pdf_docs + txt_docs

        print(" Chunking documents...")
        chunks = chunk_text(all_docs)

        if not chunks:
            print(" No documents found to process.")
            print(" Please add .pdf files to data/raw/pdfs/ and/or .txt files to data/raw/txts/.")
            return

        print(f" Generating embeddings for {len(chunks)} chunks (cached for future runs)...")
        embeddings = embedder.embed_chunks(chunks)

        print(" Building vector store...")
        vector_store = VectorStore(embedding_dim=embeddings.shape[1])
        vector_store.add_embeddings(embeddings, chunks)
        vector_store.save(cache_dir)
        print(f" Vector store successfully cached to {cache_dir}/")

    retriever = Retriever(embedder, vector_store)
    generator = AnswerGenerator()

    print("\n System ready. Ask your questions!\n")

    while True:
        try:
            question = input(" Enter your question (or type 'exit'): ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n Goodbye!")
            break

        if not question:
            continue

        if question.lower() == "exit":
            print(" Goodbye!")
            break

        retrieved_chunks = retriever.retrieve(question, top_k=4)

        # 🔒 Relevance guard
        MAX_DISTANCE_THRESHOLD = 1.2  # safe for MiniLM

        if not retrieved_chunks or retrieved_chunks[0]["score"] > MAX_DISTANCE_THRESHOLD:
            print("\n ANSWER:\n")
            print("I don't know based on the provided documents.")
            print("\n SOURCES:\nNone\n")
            print("\n" + "=" * 80 + "\n")
            continue

        prompt = build_rag_prompt(retrieved_chunks, question)
        answer = generator.generate(prompt)

        print("\n ANSWER:\n")
        print(answer)

        print("\n SOURCES:\n")
        for i, chunk in enumerate(retrieved_chunks, 1):
            page_info = f" (page {chunk['page']})" if chunk.get("page") is not None else ""
            print(f"[{i}] {chunk['source']}{page_info}")

        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    run_cli()
