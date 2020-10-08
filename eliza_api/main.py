from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from eliza import Eliza
from generate import gpt2generator

class DialogRequest(BaseModel):
    responseId: str
    queryResult: dict
    originalDetectIntentRequest: dict
    session: str


app = FastAPI()
eliza = Eliza()
eliza.load('doctor.txt')

# Make screening test for ADHD

# 1. How often do you have trouble wrapping up the final details of a project,
# once the challenging parts have been done?
# 2. How often do you have difficulty getting things in order when you have to do
# a task that requires organization?
# 3. How often do you have problems remembering appointments or obligations?
# 4. When you have a task that requires a lot of thought, how often do you avoid or delay getting started?
# 5. How often do you fidget or squirm with your hands or feet when you have
# to sit down for a long time?
# 6. How often do you feel overly active and compelled to do things, like you
# were driven by a motor?
# 7. How often do you make careless mistakes when you have to work on a boring or
# difficult project?
# 8. How often do you have difficulty keeping your attention when you are doing boring
# or repetitive work?
# 9. How often do you have difficulty concentrating on what people say to you,
# even when they are speaking to you directly?
# 10. How often do you misplace or have difficulty finding things at home or at work?
# 11. How often are you distracted by activity or noise around you?
# 12. How often do you leave your seat in meetings or other situations in which
# you are expected to remain seated?
# 13. How often do you feel restless or fidgety?
# 14. How often do you have difficulty unwinding and relaxing when you have time
# to yourself?
# 15. How often do you find yourself talking too much when you are in social situations?
# 16. When you’re in a conversation, how often do you find yourself finishing
# the sentences of the people you are talking to, before they can finish
# them themselves?
# 17. How often do you have difficulty waiting your turn in situations when
# turn taking is required?
# 18. How often do you interrupt others when they are busy?

@app.post("/")
async def create_item(dialogRequest: DialogRequest):
    print("inside with item", dialogRequest)

    # Call another api
    # Do something fun
    # Compare results
    # Return best result
    # Backup is eliza

    #response = eliza.runFromApi(dialogRequest.queryResult['queryText'])
    response = gpt2generator(dialogRequest.queryResult['queryText'])
    print("the response is", response)

    return {
        "fulfillmentText": response,
        "fulfillmentMessages": [
            {"text": {"text": [response]}}
        ],
        "source": ""
        }    


