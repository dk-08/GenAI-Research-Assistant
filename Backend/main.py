from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

from utils.document_loader import load_document
from utils.summarizer import summarize_text
from utils.qa_engine import simple_answer_engine
from utils.challenger import generate_challenge


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

document_text = ""

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    global document_text

    ext = os.path.splitext(file.filename)[-1].lower()
    temp_path = f"temp_upload{ext}"

    with open(temp_path, "wb") as f:
        f.write(await file.read())

    try:
        document_text = load_document(temp_path)
        os.remove(temp_path)
        return {"message": "File uploaded and processed successfully."}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)


@app.get("/summary")
def get_summary():
    if not document_text:
        return JSONResponse(content={"error": "No document uploaded yet."}, status_code=400)

    summary = summarize_text(document_text)
    return {"summary": summary}


@app.post("/ask")
def ask_question(question: str = Form(...)):
    if not document_text:
        return JSONResponse(content={"error": "No document uploaded yet."}, status_code=400)

    answer, justification = simple_answer_engine(document_text, question)

    return {
        "question": question,
        "answer": answer,
        "justification": justification
    }

@app.get("/challenge")
def get_challenge():
    if not document_text:
        return JSONResponse(content={"error": "No document uploaded yet."}, status_code=400)

    question, answer = generate_challenge(document_text)
    return {"question": question, "answer": answer}

