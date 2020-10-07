from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from eliza import Eliza


class DialogRequest(BaseModel):
    responseId: str
    queryResult: dict
    originalDetectIntentRequest: dict
    session: str

class DialogResponse(BaseModel):
    fulfillmentText: str
    fulfillmentMessages: list
    source: str



#   let responseJson =  {
#     "fulfillmentText": jokeResponse,
#     "fulfillmentMessages": [
#         {
#             "text": {
#                 "text": [
#                   jokeResponse
#                 ]
#             }
#         }
#     ],
#     "source": ""
# }

#     {
#   "responseId": "f487a623-3564-4850-9626-3f135cc1974b-fddac391",
#   "queryResult": {
#     "queryText": "I would like have all the codes",
#     "action": "input.unknown",
#     "parameters": {},
#     "allRequiredParamsPresent": true,
#     "outputContexts": [
#       {
#         "name": "projects/furhatoracle-ehcs/agent/sessions/4b925e3d-8b66-580b-9819-02b22db6a016/contexts/__system_counters__",
#         "lifespanCount": 1,
#         "parameters": {
#           "no-input": 0,
#           "no-match": 1
#         }
#       }
#     ],
#     "intent": {
#       "name": "projects/furhatoracle-ehcs/agent/intents/3acec099-cbda-4cf8-bf8e-d5e43323e449",
#       "displayName": "Default Fallback Intent",
#       "isFallback": true
#     },
#     "intentDetectionConfidence": 1,
#     "languageCode": "en"
#   },
#   "originalDetectIntentRequest": {
#     "source": "DIALOGFLOW_CONSOLE",
#     "payload": {}
#   },
#   "session": "projects/furhatoracle-ehcs/agent/sessions/4b925e3d-8b66-580b-9819-02b22db6a016"
# }


class Item(BaseModel):
    text: str

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


