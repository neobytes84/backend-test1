from pydantic import BaseModel
from typing import List, Optional

class AuthorBase(BaseModel):
    name: str

class AuthorCreate(AuthorBase):
    pass

class AuthorBook(BaseModel):
    book_id: int

class Author(AuthorBase):
    id: int
    books: List[AuthorBook] = []
    
    class Config:
        orm_mode = True