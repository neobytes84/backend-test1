from pydantic import BaseModel
from typing import Optional, List

class BookBase(BaseModel):
    title: str
    year: Optional[int] = None
    language: Optional[str] = None
    
class BookCreate(BookBase):
    pass

class BookAuthor(BaseModel):
    author_id: int
    
class Book(BookBase):
    id: int
    authors: List[BookAuthor] = []
    
    class Config:
        orm_mode = True