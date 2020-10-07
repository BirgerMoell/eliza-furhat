const express = require('express')
const fetch = require('node-fetch')
const app = express()
const port = 3000

 

// anders tegnell bot

// läs film-manus

// prata på ett tema

// 


app.post('/', async (req, res) => {

  console.log("the request is", req)
  let joke = await getApi("https://official-joke-api.appspot.com/jokes/programming/random")
  console.log("the joke is", joke)
  let jokeResponse = joke[0].setup + " " + joke[0].punchline

  let responseJson =  {
    "fulfillmentText": jokeResponse,
    "fulfillmentMessages": [
        {
            "text": {
                "text": [
                  jokeResponse
                ]
            }
        }
    ],
    "source": ""
}

  res.send(responseJson)
})

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`)
})


const getApi = async (url) => {
  let response = await fetch(url)
  console.log("the response is", response)
  let responseJson = await response.json()
  return responseJson

}

async function getNews() {
  //let response = await fetch("http://newsapi.org/v2/everything?q=bitcoin&from=2020-09-07&sortBy=publishedAt&apiKey=92a8ad77f01d4898a17c89afa4c3ffc7")

  let response = await fetch("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=92a8ad77f01d4898a17c89afa4c3ffc7")

  console.log("the response is", response)
  let responseJson = await response.json()
  console.log("the response json is", responseJson)
  return responseJson
}


getNews()