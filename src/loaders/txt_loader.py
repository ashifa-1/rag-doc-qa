from pathlib import Path

def load_txt_documents(folder_path: str):
    documents = []

    folder = Path(folder_path)
    for file_path in folder.glob("*.txt"):
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        documents.append({
            "text": text,
            "source": file_path.name
        })

    return documents
