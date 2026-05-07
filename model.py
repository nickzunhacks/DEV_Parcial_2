from sqlmodel import Field, SQLModel

from datetime import datetime


class Dog(SQLModel):
    __tablename__ = "Dogs"

    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )

class Sticker(SQLModel):
    __tablename__ = "Stickers"

    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )


class Book(SQLModel):
    __tablename__ = "Books"

    created: datetime = Field(
        default_factory=datetime.utcnow(),
        sa_column_kwargs={"server_default": "NOW()"}
    )

    name: str = Field(min_length=2)
    autor: str = Field(min_length=2)
    pages: int = Field(gt=10)
    available: bool = Field(...)
    language: str = Field(min_length=2)

class BookId(Book, table = True):
    id: int | None = Field(default=None, primary_key=True)