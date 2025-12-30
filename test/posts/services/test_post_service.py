from typing import Callable
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from app.posts.models.domain import Post
from app.posts.services.post_service import PostRepositoryABC, PostService


@pytest.fixture
def mock_repository() -> MagicMock:
    return MagicMock(spec=PostRepositoryABC)


@pytest.fixture
def post_service(mock_repository: MagicMock) -> PostService:
    return PostService(repository=mock_repository)


@pytest.fixture
def mock_post() -> Callable[..., Post]:
    from typing import Any

    def _factory(**kwargs: Any) -> Post:
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

    return _factory


def test_get_all_posts_with_data(
    post_service: PostService,
    mock_repository: MagicMock,
    mock_post: Callable[..., Post],
):
    # Arrange
    posts = [mock_post() for _ in range(3)]
    mock_repository.get_all_posts.return_value = posts

    # Act
    result = post_service.get_all_posts()

    # Assert
    assert result == posts


def test_get_all_posts_empty(post_service: PostService, mock_repository: MagicMock):
    # Arrange
    mock_repository.get_all_posts.return_value = []

    # Act
    result = post_service.get_all_posts()

    # Assert
    assert result == []
