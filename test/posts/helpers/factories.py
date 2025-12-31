from typing import Any
from uuid import uuid4

from app.posts.domain.post import Post


def build_post(**kwargs: Any) -> Post:
    defaults: dict[str, Any] = {
        "id": uuid4(),
        "title": "Test Post",
        "content": "Content",
        "published": True,
        "rating": None,
    }
    defaults.update(kwargs)

    # Ensure correct types for Post fields
    if not isinstance(defaults["id"], uuid4().__class__):
        raise TypeError("id must be a UUID")

    return Post(
        id=defaults["id"],
        title=str(defaults["title"]),
        content=str(defaults["content"]),
        published=bool(defaults["published"]),
        rating=(
            defaults["rating"]
            if defaults["rating"] is None
            else int(defaults["rating"])
        ),
    )
