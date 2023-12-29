from pydantic import BaseModel


class Song(BaseModel):
    id: int
    name: str
    author: str
    description: str | None = None
    genre: str