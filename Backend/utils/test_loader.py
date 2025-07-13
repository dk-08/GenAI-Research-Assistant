import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.document_loader import load_document

file_path = r"C:\\python\\GenAI_Research_Assistant\\Data\\Uploaded_docs\\sample.txt"

print("Looking for file at:", os.path.abspath(file_path))
print("Trying to load document...")

try:
    content = load_document(file_path)
    print("Document loaded successfully!\n")
    print(content[:1000])  
except Exception as e:
    print("Error loading document:", e)
