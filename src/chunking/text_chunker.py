def chunk_text(
    documents,
    chunk_size=500,
    overlap=100
):
    chunks = []

    for doc in documents:
        text = doc["text"]
        source = doc.get("source")
        page = doc.get("page", None)

        start = 0
        chunk_id = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "chunk_text": chunk_text,
                "source": source,
                "page": page,
                "chunk_id": f"{source}_{page}_{chunk_id}"
            })

            chunk_id += 1
            start += chunk_size - overlap

    return chunks
