import random
import re
from typing import Tuple

def generate_challenge(document_text: str) -> Tuple[str, str]:

    sentences = re.split(r'(?<=[.!?])\s', document_text)
    sentences = [s.strip() for s in sentences if len(s.split()) >= 6]

    if not sentences:
        return ("Not enough content to generate a challenge.", "")

    sentence = random.choice(sentences)

    words = sentence.split()
    candidates = [w for w in words if w.isalpha() and len(w) > 3]

    if not candidates:
        return ("Couldn't find a good word to blank.", "")

    word_to_blank = random.choice(candidates)
    blanked_sentence = sentence.replace(word_to_blank, "_____")

    return (blanked_sentence, word_to_blank)
