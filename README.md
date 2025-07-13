# 🤖 GenAI Research Assistant

The **GenAI Research Assistant** is an intelligent, document-aware application that allows users to:

- 📤 Upload `.pdf` or `.txt` files
- 🧠 Automatically generate concise summaries
- ❓ Ask questions about the uploaded content
- 🧩 Take challenge-style quizzes based on the document

Built using **FastAPI** (backend) and **Streamlit** (frontend), the app enables interactive exploration and self-evaluation of textual content — all offline.

---

## 🚀 Features

- **Document Upload** — Supports `.txt` and `.pdf` files
- **Summarization** — Auto-generates summaries using simple heuristics
- **Question Answering** — Keyword-based Q&A with paragraph justification
- **Challenge Me Mode** — Generates fill-in-the-blank questions from document content
- **Clean UI** — Built with Streamlit, styled with a dark theme
- **Offline-First** — No external APIs needed (OpenAI optional upgrade)

---

## 🛠️ Tech Stack

| Layer       | Technology |
|-------------|------------|
| Frontend    | Streamlit  |
| Backend     | FastAPI    |
| Language    | Python 3.10+ |
| Parser      | PyMuPDF (`fitz`) |
| Styling     | Custom HTML/CSS injected into Streamlit |
| Git Hosting | GitHub     |

---

Here’s a clean and professional **“GenAI Support (Optional)”** section you can copy into your `README.md` 👇

---

### 🧠 GenAI Support (Optional Upgrade)

> This project supports optional integration with **OpenAI's GPT-3.5/4 API** to enable Generative AI–powered responses.

When enabled, the assistant can:

* Generate more **context-aware, human-like answers**
* Produce higher-quality **summaries and justifications**
* Be upgraded for use in advanced NLP use cases

#### 🔧 How to Enable GPT Support:

1. Get your OpenAI API key from [https://platform.openai.com](https://platform.openai.com)

2. In the backend terminal, set your key before running the server:

   ```bash
   $env:OPENAI_API_KEY="sk-..."
   ```

3. GPT logic is already implemented inside:

   * `utils/qa_engine.py`
   * (Optional) `utils/summarizer.py`

4. Run the backend:

   ```bash
   uvicorn main:app --reload
   ```

> ✅ GPT is not required — the app also works fully offline with rule-based logic.

---

## 📁 Project Structure

```

GenAI\_Research\_Assistant/
├── backend/
│   ├── main.py                # FastAPI server
│   ├── requirements.txt       # Backend dependencies
│   └── utils/
│       ├── document\_loader.py # Load txt/pdf
│       ├── summarizer.py      # Summarization logic
│       ├── qa\_engine.py       # Keyword-based Q\&A
│       ├── challenger.py      # Challenge Me logic
├── frontend/
│   ├── app.py                 # Streamlit UI
│   └── requirements.txt       # Frontend dependencies
├── Data/
│   └── Uploaded\_docs/         # Where uploaded docs are saved
├── screenshot.png             # UI Screenshot (add yours here)
└── README.md                  # This file

````

---

## 💻 How to Run the App

### 🔧 Backend (FastAPI)

```bash
cd backend
python -m venv venv
venv\Scripts\activate            # for Windows
pip install -r requirements.txt
uvicorn main:app --reload
````

🔗 Visit: `http://127.0.0.1:8000/docs` to access the FastAPI Swagger UI.

---

### 🖥️ Frontend (Streamlit)

In another terminal:

```bash
cd frontend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

🔗 Visit: `http://localhost:8501` to use the assistant.

---

## 📸 Sample UI
<img width="469" height="729" alt="Screenshot 2025-07-13 171606" src="https://github.com/user-attachments/assets/74bb45da-fd74-4cb6-b454-302ebaadebf7" />   <img width="477" height="722" alt="Screenshot 2025-07-13 171623" src="https://github.com/user-attachments/assets/8967930a-6355-4e05-a9bd-aa538b863865" />

---

## 🧠 Example Use Cases

* Reading summaries of research papers
* Asking questions from academic content
* Practicing document-based comprehension questions
* Self-testing using Challenge Me mode

---

## 📄 License

This project is for educational and research purposes only.

---

## 🙌 Author

**Disha Kaushik**
[GitHub](https://github.com/dk-08)
