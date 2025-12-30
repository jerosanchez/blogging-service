import uuid
from typing import Optional

from pydantic import BaseModel


class PostBase(BaseModel):
    id: uuid.UUID
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

    class ConfigDict:
        orm_mode = True


class PostRead(PostBase):
    pass
