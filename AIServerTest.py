# uvicorn AIServerTest:app --host 0.0.0.0 --port 8000

from fastapi import FastAPI
from pydantic import BaseModel
from ollama import Client

app = FastAPI()
client = Client(host='http://localhost:11434')  # Connects to localhost:11434

class QueryRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(request: QueryRequest):
    try:
        response = client.chat(model='ilsp/meltemi-instruct:latest', messages=[
            {"role": "user", "content": request.question}
        ])
        return {"response": response["message"]["content"]}
    except Exception as e:
        print(e)
        return {"error": str(e)}
