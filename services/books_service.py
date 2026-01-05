import datetime
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.books_model import Books
from services.users_service import get_user_by_id


def get_all_books(db: Session):
    return db.query(Books).all()


def get_book_by_id(db: Session, book_id):
    book = db.query(Books).filter(Books.book_id == book_id).first()

    if book is None:
        raise HTTPException(status_code=404, detail="book doesn’t exist")

    return book


def create_book(db: Session, title: str, author: str):
    book = Books(title=title, author=author)

    db.add(book)
    db.commit()

    return book


def update_book(db: Session, book_id, title: str, author: str):
    book = get_book_by_id(db, book_id)
    book.title = title
    book.author = author

    db.commit()


def delete_book(db: Session, book_id):
    book = get_book_by_id(db, book_id)

    db.delete(book)
    db.commit()


def borrow_book(db: Session, book_id, member_id):
    user = get_user_by_id(db,member_id)
    book = get_book_by_id(db, book_id)

    if book.is_borrowed:
        raise HTTPException(
            status_code=409,
            detail="Book is currently borrowed"
        )

    book.is_borrowed = True
    book.borrowed_by = user.member_id
    book.borrowed_date = datetime.datetime.now()

    db.commit()


def return_book(db: Session, book_id):
    book = get_book_by_id(db, book_id)

    if not book.is_borrowed:
        raise HTTPException(
            status_code=409,
            detail="The book is not borrowed"
        )

    book.is_borrowed = False
    book.borrowed_by = None
    book.borrowed_date = None

    db.commit()
