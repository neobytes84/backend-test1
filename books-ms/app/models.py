from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    year = Column(Integer)
    language = Column(String)

    authors = relationship("BookAuthor", back_populates="book")


class BookAuthor(Base):
    __tablename__ = "book_author"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)

    book = relationship("Book", back_populates="authors")
