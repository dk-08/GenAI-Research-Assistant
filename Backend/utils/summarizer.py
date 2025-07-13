from typing import List
import re

def split_into_sentences(text: str) -> List[str]:
    text = re.sub(r'\s+', ' ', text)  
    sentences = re.split(r'(?<=[.!?])\s', text)
    return sentences

def summarize_text(text: str, max_words: int = 150) -> str:
    sentences = split_into_sentences(text)

    summary = []
    word_count = 0

    for sentence in sentences:
        words = sentence.split()
        word_count += len(words)
        if word_count <= max_words:
            summary.append(sentence)
        else:
            break

    return " ".join(summary)
