from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Create FastAPI app instance
app = FastAPI(title="API Basics Demo")

# -------------------------
# DATA MODEL
# -------------------------
class Book(BaseModel):
    id: int
    title: str
    author: str


# In-memory list (temporary database)
books: List[Book] = []

# -------------------------
# BASIC ROUTES
# -------------------------

@app.get("/")
def home():
    return {"message": "Welcome to API Basics"}

# GET: Fetch all books
@app.get("/books")
def get_books():
    return books

# GET: Fetch a single book by ID
@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

# POST: Add a new book
@app.post("/books")
def add_book(book: Book):
    books.append(book)
    return book

# PUT: Update an existing book
@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: Book):
    for index, book in enumerate(books):
        if book.id == book_id:
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

# DELETE: Remove a book
@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return {"message": "Book deleted successfully"}
    raise HTTPException(status_code=404, detail="Book not found")

# -------------------------
# PATH & QUERY PARAM EXAMPLES
# -------------------------

@app.get("/hello/{name}")
def greet_user(name: str):
    return {"message": f"Hello {name}"}

# Example: /teas?name=GreenTea
@app.get("/teas")
def get_teas(name: str):
    return {"tea_name": name}
