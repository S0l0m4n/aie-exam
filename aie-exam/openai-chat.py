#!/bin/python3
# Send a couple of messages to the OpenAI API and parse the response.
# Set the model, temperature and token length accordingly.
# Use the Requests library to make the requests.

import os
import requests

OPENAI_URL = "https://api.openai.com/v1/responses"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
}

body = {
        "model": "gpt-4o-mini",
        "temperature": 0.15,
        "input": "Test",
}

response = requests.post(OPENAI_URL, headers=headers, json=body)

print(response, response.text)
