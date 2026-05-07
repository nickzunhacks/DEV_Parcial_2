from sqlmodel import select, Session
from model import Book, BookId

def create_book(session: Session, book: Book):
    new_book = BookId.model_validate(book)
    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book

def show_all_books(session: Session):
    return session.exec(select(BookId)).all()

