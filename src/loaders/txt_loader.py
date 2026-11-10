from pathlib import Path

def load_txt_documents(folder_path: str):
    documents = []

    folder = Path(folder_path)
    if not folder.exists():
        return documents

    for file_path in folder.glob("*.txt"):
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()

            documents.append({
                "text": text,
                "source": file_path.name,
                "page": None
            })
        except Exception as e:
            print(f"Warning: Could not read {file_path.name}: {e}")

    return documents
