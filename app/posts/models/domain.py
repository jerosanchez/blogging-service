from dataclasses import dataclass
from typing import Optional
from uuid import UUID


@dataclass
class Post:
    id: UUID
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None
