import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.document_loader import load_document
from utils.qa_engine import simple_answer_engine

file_path = r"C:\python\GenAI_Research_Assistant\Data\Uploaded_docs\sample.txt"


text = load_document(file_path)
question = "Who is Manolin?"

print(f"## Question: {question}\n")
answer, justification = simple_answer_engine(text, question)

print(f"## Answer: {answer}\n")
print(f"## Justification: {justification}")
