from fastapi import FastAPI
from database import engine, Base

from models.users_model import Users
from models.books_model import Books

from routers import books, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(books.router)
app.include_router(users.router)
