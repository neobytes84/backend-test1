from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from ..events.producer import producer
import logging

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/authors", tags=["authors"])


@router.post("/", response_model=schemas.Author, status_code=201)
async def create_author(author_in: schemas.AuthorCreate, db: Session = Depends(get_db)):
    author = models.Author(name=author_in.name)
    db.add(author)
    db.commit()
    db.refresh(author)
    
    logger.info("Author created", extra={"author_id":author.id, "name": author.name})
    
    # Emitimos evento
    await producer.send_author_created(author.id, author.name)
    
    return author

@router.get("/", response_model=list[schemas.Author])
def list_authors(db: Session = Depends(get_db)):
    authors = db.query(models.Author).all()
    return authors

@router.get("/{author_id}", response_model=schemas.Author)
def get_author(author_id: int, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/{author_id}/assign-book", status_code=204)
async def assign_book_to_author(author_id: int, body: schemas.AuthorBook, db: Session = Depends(get_db)):
    author = db.query(models.Author).filter(models.Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    assoc = models.AuthorBookAssociation(author_id=author_id, book_id=body.book_id)
    db.add(assoc)
    db.commit()
    
    logger.info("Book assigned to author", 
                extra={"author_id":author.id, "book_id": body.book_id},
                )
    
    # Emitimos evento
    await producer.send_author_book_assigned(author.id, body.book_id)   
    return