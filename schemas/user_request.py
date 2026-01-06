from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    name: str = Field(min_length=3)
    email: str = Field(min_length=3)