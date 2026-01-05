#!/bin/python3

import requests

# 1. GET all books
response = requests.get("http://127.0.0.1:8000/books")
print("All Books:", response.json())

# 2. POST a new book
new_book = {
    "id": 3,
    "title": "Brave New World",
    "author": "Aldous Huxley"
}
post_response = requests.post("http://127.0.0.1:8000/books", json=new_book)
print("Post Response:", post_response.status_code, post_response.json())

# 3. DELETE a book
delete_response = requests.delete("http://127.0.0.1:8000/books/1")
print("Delete Status:", delete_response.status_code)
