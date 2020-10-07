from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from eliza import Eliza

class DialogRequest(BaseModel):
    responseId: str
    queryResult: dict
    originalDetectIntentRequest: dict
    session: str


app = FastAPI()
eliza = Eliza()
eliza.load('doctor.txt')

@app.post("/")
async def create_item(dialogRequest: DialogRequest):
    print("inside with item", dialogRequest)
    response = eliza.runFromApi(dialogRequest.queryResult['queryText'])
    print("the response is", response)

    return {
        "fulfillmentText": response,
        "fulfillmentMessages": [
            {"text": {"text": [response]}}
        ],
        "source": ""
        }    


