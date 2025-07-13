import os
import fitz  
from typing import Literal

def load_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf(file_path: str) -> str:
    text = ""
    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def load_document(file_path: str) -> str:
    ext = os.path.splitext(file_path)[-1].lower()

    if ext == ".txt":
        return load_txt(file_path)
    elif ext == ".pdf":
        return load_pdf(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

