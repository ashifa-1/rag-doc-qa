from src.loaders.pdf_loader import load_pdf_documents
from src.loaders.txt_loader import load_txt_documents
from src.chunking.text_chunker import chunk_text
from src.embeddings.embedder import TextEmbedder
from src.vector_store.store import VectorStore
from src.retrieval.retriever import Retriever
from src.prompts.rag_prompt import build_rag_prompt
from src.generation.answer_generator import AnswerGenerator


def run_cli():
    print(" Loading documents...")
    pdf_docs = load_pdf_documents("data/raw/pdfs")
    txt_docs = load_txt_documents("data/raw/txts")
    all_docs = pdf_docs + txt_docs

    print(" Chunking documents...")
    chunks = chunk_text(all_docs)

    print(" Generating embeddings...")
    embedder = TextEmbedder()
    embeddings = embedder.embed_chunks(chunks)

    print(" Building vector store...")
    vector_store = VectorStore(embedding_dim=embeddings.shape[1])
    vector_store.add_embeddings(embeddings, chunks)

    retriever = Retriever(embedder, vector_store)
    generator = AnswerGenerator()

    print("\n System ready. Ask your questions!\n")

    while True:
        question = input(" Enter your question (or type 'exit'): ").strip()
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


        # ✅ FIX: build_rag_prompt returns ONLY prompt
        prompt = build_rag_prompt(retrieved_chunks, question)
        answer = generator.generate(prompt)

        print("\n ANSWER:\n")
        print(answer)

        print("\n SOURCES:\n")
        for i, chunk in enumerate(retrieved_chunks, 1):
            print(f"[{i}] {chunk['source']} (page {chunk['page']})")

        print("\n" + "=" * 80 + "\n")


if __name__ == "__main__":
    run_cli()
