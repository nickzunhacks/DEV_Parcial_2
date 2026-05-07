from fastapi import FastAPI, HTTPException
from db import SessionDep, create_all_tables
from model import Book, BookId
from bookOperations import (create_book,
                            show_all_books,
                            find_book,
                            update_book
                            )

app = FastAPI(lifespan=create_all_tables)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/books")
def books_get_all(session: SessionDep):
    return show_all_books(session)

@app.post("/book")
def book_post(book: Book, session: SessionDep):
    return create_book(session, book)

@app.get("/book")
def book_get_one(session: SessionDep, id: int):
    book = find_book(session, id)

    if "Error" in book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book

@app.patch("/book")
def upload_book(session: SessionDep, book: Book, id: int):
    uploaded_book = update_book(session, book, id)

    if "Error" in uploaded_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return uploaded_book