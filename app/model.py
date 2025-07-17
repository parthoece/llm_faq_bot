import json

with open("app/qa_pairs.json") as f:
    QA_PAIRS = json.load(f)

def get_answer(prompt: str) -> str:
    return QA_PAIRS.get(prompt.lower(), "I don't know the answer.")
