from dataclasses import dataclass, field
from typing import Optional
from uuid import UUID, uuid4

# ---------- Domain models


@dataclass
class Post:
    title: str
    content: str
    id: UUID = field(default_factory=uuid4)
    published: bool = True
    rating: Optional[int] = None
