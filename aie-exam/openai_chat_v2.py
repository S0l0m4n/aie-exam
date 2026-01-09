#!/bin/python3
# Like the original script, but use the OpenAI library this time instead of
# Requests. Don't need to import the API key, this is done automatically by the
# library.

from openai import OpenAI
from openai.types.responses.response import Response

MODEL = "gpt-4o-mini"

body = {
        "model": "gpt-4o-mini",
        "temperature": 0.15,
        "max_output_tokens": 150,
}

client = OpenAI()

def get_output_text(response:Response) -> str:
    """
    Works the same as chat_parser() in the original script
    """
    answers = []
    for output in response.output:
        if output.type == "message" and output.role == "assistant":
            for content in output.content:
                if content.type== "output_text":
                    answers.append(content.text)
    return "".join(answers)
    # or you can simply return response.output_text

def post_messages(messages):
    response = client.responses.create(
            model=MODEL,
            input=messages,
    ) 
    #return get_output_text(response)
    return response.output_text

if __name__ == '__main__':
    messages = [
            {"role": "user", "content": "Hello, can you help me today?"},
            {"role": "user", "content": "What is the currency of Lebanon?"},
    ]
    answers = post_messages(messages)
    print(answers)
