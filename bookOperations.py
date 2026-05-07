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

def find_book(session: Session, id: int):
    try:
        libro = session.exec(select(BookId).where(BookId.id == id)).one()

    except:
        return {"Error":"Book not found"}

    return libro

def update_book(session: Session, uploadedBook: Book, id: int):
    book = find_book(session, id)
    if "Error" in book:
        return book

    book.name = uploadedBook.name
    book.language = uploadedBook.language
    book.autor = uploadedBook.autor
    book.available = uploadedBook.available
    book.pages = uploadedBook.pages

    session.add(book)
    session.commit()
    session.refresh(book)
    return book


