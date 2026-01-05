#!/bin/python3
# A simple example demonstrating the use of FastAPI to create a server that
# provides APIs for maintaining a book database

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# This is our "data" (in a real app, it would be a database)
books = [
        {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
        {"id": 2, "title": "1984", "author": "George Orwell"},
]

# This defines what a "book" looks like (the schema)
class Book(BaseModel):
    id: int
    title: str
    author: str

# GET: Retrieve all books
@app.get("/books")
def get_books():
    return books

# POST: Create a new book
@app.post("/books")
def add_book(book: Book):
    books.append(book.dict())
    return {"message": "Book added successfully", "book": book}

# DELETE: Remove a book by ID
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book["id"] == book_id:
            books.pop(index)
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")

@app.get("/")
def home():
    return {"message": "Welcome to my book API! Go to /docs for the interactive UI."}
