from pathlib import Path
from pypdf import PdfReader

def load_pdf_documents(folder_path: str):
    documents = []

    folder = Path(folder_path)
    if not folder.exists():
        return documents

    for file_path in folder.glob("*.pdf"):
        try:
            reader = PdfReader(file_path)

            for page_num, page in enumerate(reader.pages):
                text = page.extract_text()
                if text:
                    documents.append({
                        "text": text,
                        "source": file_path.name,
                        "page": page_num + 1
                    })
        except Exception as e:
            print(f"Warning: Could not read {file_path.name}: {e}")

    return documents
