from database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String,Boolean,DateTime,ForeignKey
import uuid

    
class Books(Base):
    __tablename__ = 'books'

    book_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        index=True
    )

    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    is_borrowed = Column(Boolean, default=False)

    borrowed_date = Column(DateTime(timezone=True))

    borrowed_by = Column(
        UUID(as_uuid=True),
        ForeignKey("users.member_id")
    )