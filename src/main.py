from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
books = {}

class Book(BaseModel):
    title: str
    author: str
    ISBN: str
    year: int

@app.post("/books/")
def create_book(book: Book):
    book_id = len(books) + 1
    books[book_id] = book.dict()
    return books[book_id]

@app.get("/books/{book_id}")
def read_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    books[book_id] = book.dict()
    return books[book_id]

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    if book_id not in books:
        raise HTTPException(status_code=404, detail="Book not found")
    del books[book_id]
    return {"message": "Book deleted successfully"}