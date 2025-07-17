from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from .model import get_answer

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask(data: Question):
    answer = get_answer(data.question)
    return {"answer": answer}

@app.get("/", response_class=HTMLResponse)
def read_root():
    with open("app/static/index.html") as f:
        return f.read()
