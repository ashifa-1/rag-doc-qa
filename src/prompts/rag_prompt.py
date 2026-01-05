def build_rag_prompt(context_chunks, question, max_chars=1500):
    context_text = ""
    total_chars = 0

    for i, chunk in enumerate(context_chunks, 1):
        block = (
            f"[{i}] Source: {chunk['source']}, Page: {chunk['page']}\n"
            f"{chunk['text']}\n\n"
        )

        if total_chars + len(block) > max_chars:
            break

        context_text += block
        total_chars += len(block)

    prompt = f"""
You are a question-answering assistant.

Use ONLY the context below to answer the question.
Write a clear and concise answer in your own words.
If the context describes a process, summarize it step by step.
If the answer is not present in the context, say:
"I don't know based on the provided documents."

Context:
{context_text}

Question:
{question}

Answer:
"""
    return prompt
