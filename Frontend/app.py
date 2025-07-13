import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="GenAI Research Assistant", layout="centered")

st.title("📄 GenAI Research Assistant")

# --- File Upload ---
st.header("1. Upload Document")
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])

if uploaded_file:
    st.success("File selected! Sending to backend...")

    files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
    response = requests.post(f"{API_URL}/upload", files=files)

    if response.status_code == 200:
        st.success(" File uploaded and processed successfully!")
    else:
        st.error(f" Error: {response.json().get('error')}")


# --- Summary ---
if st.button("🔍 Show Summary"):
    response = requests.get(f"{API_URL}/summary")

    if response.status_code == 200:
        st.subheader(" Auto-Summary (≤150 words)")
        st.write(response.json()["summary"])
    else:
        st.warning("No document uploaded yet. Please upload a file first.")


# --- Ask Anything ---
st.header("2. Ask Anything from the Document")
question = st.text_input(" Enter your question")

if st.button("Ask"):
    if question.strip() == "":
        st.warning("Please enter a question.")
    else:
        response = requests.post(f"{API_URL}/ask", data={"question": question})

        if response.status_code == 200:
            data = response.json()
            st.markdown(f"Answer:{data['answer']}")
            st.markdown(f"Justification: {data['justification']}")
        else:
            st.error(" Error: Make sure you've uploaded a file.")
# --- Challenge Me Section ---
st.header("3. Challenge Me!")

if st.button(" Generate Challenge"):
    challenge = requests.get(f"{API_URL}/challenge")

    if challenge.status_code == 200:
        challenge_data = challenge.json()
        st.session_state["challenge_question"] = challenge_data["question"]
        st.session_state["correct_answer"] = challenge_data["answer"]
    else:
        st.warning("Upload a document first!")

if "challenge_question" in st.session_state:
    st.markdown(f"**Fill in the blank:**\n\n{st.session_state['challenge_question']}")

    user_answer = st.text_input("Your answer:")

    if user_answer:
        correct = st.session_state["correct_answer"].lower().strip()
        if user_answer.lower().strip() == correct:
            st.success("Correct!")
        else:
            st.error(f"Incorrect. Try again!")
