from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from eliza import Eliza


class Item(BaseModel):
    text: str


app = FastAPI()
eliza = Eliza()
eliza.load('doctor.txt')


@app.get("/")
def read_root():
    eliza = Eliza()
    eliza.load('doctor.txt')
    # response = eliza.getInitial()
    response = eliza.runFromApi("I really need a friend")
    # initial = True
    return response


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.post("/eliza")
async def create_item(item: Item):
    return eliza.runFromApi(item.text)
