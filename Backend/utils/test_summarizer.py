import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.document_loader import load_document
from utils.summarizer import summarize_text

file_path = r"C:\python\GenAI_Research_Assistant\Data\Uploaded_docs\sample.txt"

print("Loading document from:", file_path)
try:
    text = load_document(file_path)
    print("Document loaded.")
except Exception as e:
    print("Error loading document:", e)
    text = ""

if text:
    print("\n Generating summary...\n")
    summary = summarize_text(text)

    print("📄 Summary:\n")
    print(summary)
    print(f"\n Word count: {len(summary.split())}")
else:
    print("No text to summarize.")
