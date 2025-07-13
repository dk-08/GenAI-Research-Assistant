import re
from typing import Tuple

def simple_answer_engine(document_text: str, user_question: str) -> Tuple[str, str]:
    paragraphs = [p.strip() for p in document_text.split("\n") if p.strip()]
    
    question_keywords = set(re.findall(r'\w+', user_question.lower()))
    
    best_match = ""
    best_score = 0
    best_para_index = -1

    for i, para in enumerate(paragraphs):
        words = re.findall(r'\w+', para.lower())
        match_score = len(set(words) & question_keywords)

        if match_score > best_score:
            best_score = match_score
            best_match = para
            best_para_index = i + 1  

    if best_score == 0:
        return ("Sorry, I couldn't find an answer in the document.", "")
    else:
        justification = f"This is supported by paragraph {best_para_index}."
        return (best_match, justification)
