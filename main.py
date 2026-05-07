from typing import List

from fastapi import FastAPI
from db import SessionDep, create_all_tables
from model import Book, BookId
from sqlmodel import select
from bookOperations import create_book, show_all_books

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
def book(book: Book, session: SessionDep):
    return create_book(session, book)