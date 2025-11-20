from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

    books = relationship("AuthorBook", back_populates="author")


class AuthorBook(Base):
    __tablename__ = "author_book"

    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"), nullable=False)
    book_id = Column(Integer, nullable=False)

    author = relationship("Author", back_populates="books")
