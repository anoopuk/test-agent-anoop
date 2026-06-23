from fastapi import FastAPI
from pydantic import BaseModel

from agentrix_sdk import Agentrix, trace
# Initialize with PAT and agent context
agent = Agentrix(
    pat="rx_pat_502ed200-0223-4ced-9654-5c122e449066.zSsEPIh_m7seFcUFhtMOcrJ7dM6ucBFHq65h3vZMlSiQ1_Ivw4gGHqwNNQLJqWWW",
    project_id="prj-ff7218fe",
    agent_id="check-health")
agent.get_tracing_config()

@trace(name="process_query")
def handle_query(query: str) -> str:
    return f"You asked: {query}"

app = FastAPI()

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/ask")
def ask(data: Question):
    answer = handle_query(data.question)
    return {
        "answer": answer
    }