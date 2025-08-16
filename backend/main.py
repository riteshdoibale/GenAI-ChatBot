
from fastapi import FastAPI
import ollama
from pydantic import BaseModel
import openai

app = FastAPI()


class ChatRequest(BaseModel):
    message: str
    history: list[str] = []

@app.post("/chat/ollama")
async def chat(req: ChatRequest):
    messages = []
    for i, msg in enumerate(req.history):
        role = "user" if i % 2 == 0 else "assistant"
        messages.append({"role": role, "content": msg})
    messages.append({"role": "user", "content": req.message})
    # external call to ollama open source model
    response = ollama.chat(model="llama2", messages=messages)
    print("response",response)
    reply = response['message']['content']
    return {"reply": reply}


openai.api_key = ""

class ChatRequest(BaseModel):
    message: str
    history: list[str] = []

@app.post("/chat")
async def chat(req: ChatRequest):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            *[{"role": "user", "content": m} for m in req.history],
            {"role": "user", "content": req.message}
        ]
    )
    answer = response["choices"][0]["message"]["content"]
    return {"reply": answer}