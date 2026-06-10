from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/ask")
def ask(data: Question):
    return {
        "answer": f"You asked: {data.question}"
    }