from dataclasses import dataclass
from typing import Optional


@dataclass
class PostCreateDTO:
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None
