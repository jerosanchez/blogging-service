from test.posts.helpers.factories import build_post
from typing import Any
from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.posts.api.v1.posts import get_post_service, router
from app.posts.domain.post import Post

mock_service = MagicMock()

app = FastAPI()
app.include_router(router)
app.dependency_overrides[get_post_service] = lambda: mock_service

client = TestClient(app)


def assert_post_equal(response_post: dict[str, Any], domain_post: Post) -> None:
    assert response_post["id"] == str(domain_post.id)
    assert response_post["title"] == domain_post.title
    assert response_post["content"] == domain_post.content
    assert response_post["published"] == domain_post.published
    assert response_post["rating"] == domain_post.rating


def test_read_posts_returns_posts():
    # Arrange
    returned_posts = [build_post() for _ in range(3)]

    mock_service.get_all_posts.return_value = returned_posts

    # Act
    response = client.get("/posts")

    # Assert
    assert response.status_code == 200
    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert len(data) == len(returned_posts)

    for i, post in enumerate(returned_posts):
        assert_post_equal(data[i], post)


def test_read_posts_returns_empty_list():
    # Arrange
    returned_posts: list[Post] = []

    mock_service.get_all_posts.return_value = returned_posts

    # Act
    response = client.get("/posts")

    # Assert
    assert response.status_code == 200
    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert len(data) == len(returned_posts)
