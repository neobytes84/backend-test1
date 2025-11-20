from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas
from app.events.producer import producer

router = APIRouter(prefix="/books", tags=["books"])

@router.post("/", response_model=schemas.Book, status_code=201)
async def create_book(book_in: schemas.BookCreate, db: Session = Depends(get_db)):
    book = models.Book(
        title=book_in.title,
        year=book_in.year,
        language=book_in.language,
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    
    await producer.send_book_created(book.id, book.title)
    return book

@router.get("/", response_model=list[schemas.Book])
def list_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()

@router.get("/{book_id}", response_model=schemas.Book)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/{book_id}/assign-author", status_code=204)
async def assign_author(book_id: int, body: schemas.BookAuthor, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    assoc = models.BookAuthorAssociation(
        book_id=book_id,
        author_id=body.author_id,
    )
    db.add(assoc)
    db.commit()
    
    await producer.send_book_author_assigned(book_id, body.author_id)