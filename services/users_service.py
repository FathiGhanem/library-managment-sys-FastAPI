from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.users_model import Users


def create_user(db: Session, name: str, email: str):
    user = Users(name=name, email=email)
    existing = db.query(Users).filter(Users.email == email).first()
    if existing:
        raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Email already registered"
    )
    db.add(user)
    db.commit()
    


def get_all_users(db: Session):
    return db.query(Users).all()


def get_user_by_id(db: Session, member_id):
    user = db.query(Users).filter(Users.member_id == member_id).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User Not Found."
        )

    return user


def delete_user_by_id(db: Session, member_id):
    user = get_user_by_id(db, member_id)

    db.delete(user)
    db.commit()
