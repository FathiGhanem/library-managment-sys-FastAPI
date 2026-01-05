from database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String
import uuid


class Users(Base):
    __tablename__ = 'users'

    member_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    name = Column(String,  nullable=False)
    email = Column(String, unique=True, nullable=False)
