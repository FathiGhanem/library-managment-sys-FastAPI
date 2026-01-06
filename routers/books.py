from fastapi import APIRouter, Depends, Path, status
from sqlalchemy.orm import Session
from typing import Annotated
from database import SessionLocal
from services import books_service
from schemas.book_request import BookRequest


router = APIRouter(prefix="/books", tags=["books"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]





@router.get("/")
async def get_all_books(db: db_dependency):
    return books_service.get_all_books(db)


@router.get("/{book_id}")
async def get_book_by_id(db: db_dependency, book_id):
    return books_service.get_book_by_id(db, book_id)

@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_book(db: db_dependency, book_request: BookRequest):
    return books_service.create_book(
        db,
        title=book_request.title,
        author=book_request.author
    )

@router.put("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(db: db_dependency, book_request: BookRequest, book_id):
    books_service.update_book(
        db,
        book_id,
        title=book_request.title,
        author=book_request.author
    )

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(db: db_dependency, book_id):
    books_service.delete_book(db, book_id)


@router.post("/borrow/{book_id}/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def borrow_book(db: db_dependency, book_id, member_id):
    books_service.borrow_book(db, book_id, member_id)


@router.post("/return/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def return_book(db: db_dependency, book_id=Path(min_length=1)):
    books_service.return_book(db, book_id)
