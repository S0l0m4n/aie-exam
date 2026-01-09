#!/bin/python3
# Send a couple of messages to the OpenAI API and parse the response.
# Set the model, temperature and token length accordingly.
# Use the Requests library to make the requests.

import os
import pdb
import requests

OPENAI_URL = "https://api.openai.com/v1/responses"
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
}

body = {
        "model": "gpt-4o-mini",
        "temperature": 0.15,
        "max_output_tokens": 150,
}

def chat_parser(response:dict) -> str:
    answers = []
    for item in response.get("output", []):
        if item.get("type") == "message" and item.get("role") == "assistant":
            for message in item.get("content", []):
                if message.get("type") == "output_text":
                    text = message.get("text", "")
                    answers.append(text)
    return "".join(answers)

def post_messages(messages):
    req_body = body.copy()
    req_body['input'] = messages
    response = requests.post(OPENAI_URL, headers=headers, json=req_body)
    response.raise_for_status()
    return chat_parser(response.json())

if __name__ == '__main__':
    messages = [
            {"role": "user", "content": "Hello, can you help me today?"},
            {"role": "user", "content": "What is the currency of Lebanon?"},
    ]
    answers = post_messages(messages)
    print(answers)
