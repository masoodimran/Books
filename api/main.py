from fastapi import FastAPI, HTTPException
from api.models import Book, BookCreate
from typing import List
from uuid import UUID

app = FastAPI()
books = []

@app.get("/books/{book_id}", response_model=Book)
async def read_book(book_id: UUID):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book, status_code=201)
async def create_book(book_data: BookCreate):
    book = Book.create(**book_data.model_dump())
    books.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
async def update_book(book_id: UUID, book_update: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = book_update
            return book_update
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", status_code=204)
async def delete_book(book_id: UUID):
    for index, book in enumerate(books):
        if book.id == book_id:
            del books[index]
            return
    raise HTTPException(status_code=404, detail="Book not found")