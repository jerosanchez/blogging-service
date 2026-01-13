from dataclasses import dataclass
from typing import Optional


@dataclass
class PostCreateDTO:
    title: str
    content: str
    published: bool = False
    rating: Optional[int] = None


@dataclass
class PostUpdateDTO:
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None
    rating: Optional[int] = None
