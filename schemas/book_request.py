from pydantic import BaseModel, Field


class BookRequest(BaseModel):
    title: str = Field(min_length=3)
    author: str = Field(min_length=3)