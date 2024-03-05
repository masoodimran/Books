from pydantic import BaseModel
from uuid import UUID, uuid4

class Book(BaseModel):
    id: UUID
    title: str
    author: str
    publication_year: int

    @classmethod
    def create(cls, **kwargs):
        kwargs['id'] = uuid4()
        return cls(**kwargs)

class BookCreate(BaseModel):
    title: str
    author: str
    publication_year: int