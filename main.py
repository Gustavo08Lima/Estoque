from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/")
def root():
    return {"api deu certo!"}

@app.get("/itens/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "busca": q}