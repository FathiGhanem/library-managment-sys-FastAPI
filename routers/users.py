from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, Path, status
from database import SessionLocal
from services import users_service
from schemas.user_request import UserRequest


router = APIRouter(
    prefix="/members",
    tags=["members"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]




@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_new_user(db: db_dependency, user_request: UserRequest):
    return users_service.create_user(
        db,
        name=user_request.name,
        email=user_request.email
    )

@router.get("/")
async def get_all_users(db: db_dependency):
    return users_service.get_all_users(db)

@router.get("/{member_id}")
async def get_user_by_id(db: db_dependency, member_id=Path(min_length=1)):
    return users_service.get_user_by_id(db, member_id)

@router.delete("/{member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user_by_id(db: db_dependency, member_id=Path(min_length=1)):
    users_service.delete_user_by_id(db, member_id)
