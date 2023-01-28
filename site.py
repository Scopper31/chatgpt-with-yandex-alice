from flask import Flask, request
import logging
import json
import os
import os
import openai

key = "your chat gpt api key"
openai.api_key = key


def ans(s):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=s,
      temperature=0.5,
      max_tokens=1000,
      top_p=1.0,
      frequency_penalty=0.5,
      presence_penalty=0.0,
    )
    return response["choices"][0]["text"]


app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)


@app.route("/", methods=["POST"])
def main():
    logging.info(request.json)
    response = {
        "version": request.json["version"],
        "session": request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.json
    if req["session"]["new"]:
        response["response"]["text"] = "GO"
    else:
        response["response"]["text"] = ans(req["request"]["original_utterance"])

    return json.dumps(response)
