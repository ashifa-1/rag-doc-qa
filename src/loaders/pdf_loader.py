from pathlib import Path
from pypdf import PdfReader

def load_pdf_documents(folder_path: str):
    documents = []

    folder = Path(folder_path)
    for file_path in folder.glob("*.pdf"):
        reader = PdfReader(file_path)

        for page_num, page in enumerate(reader.pages):
            text = page.extract_text()
            if text:
                documents.append({
                    "text": text,
                    "source": file_path.name,
                    "page": page_num + 1
                })

    return documents
