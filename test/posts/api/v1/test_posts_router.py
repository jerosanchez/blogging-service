from test.posts.helpers.factories import build_post
from typing import Any
from unittest.mock import MagicMock

from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.status import HTTP_200_OK, HTTP_201_CREATED

from app.posts.api.v1.posts_router import get_post_service, router
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


def test_get_posts_returns_200_and_list_of_posts():
    # Arrange
    returned_posts = [build_post() for _ in range(3)]

    mock_service.get_all_posts.return_value = returned_posts

    # Act
    response = client.get("/posts")

    # Assert
    assert response.status_code == HTTP_200_OK
    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert len(data) == len(returned_posts)

    for i, post in enumerate(returned_posts):
        assert_post_equal(data[i], post)


def test_get_posts_returns_200_and_empty_list_when_no_posts_exist():
    # Arrange
    returned_posts: list[Post] = []

    mock_service.get_all_posts.return_value = returned_posts

    # Act
    response = client.get("/posts")

    # Assert
    assert response.status_code == HTTP_200_OK
    data: list[dict[str, Any]] = response.json()
    assert isinstance(data, list)
    assert len(data) == len(returned_posts)


def test_create_post_returns_201_and_post_when_all_fields_provided():
    # Arrange
    post_data: dict[str, Any] = {
        "title": "New Post",
        "content": "New Content",
        "published": True,
        "rating": 5,
    }
    created_post = build_post(**post_data)
    mock_service.create_post.return_value = created_post

    # Act
    response = client.post("/posts", json=post_data)

    # Assert
    assert response.status_code == HTTP_201_CREATED
    data = response.json()
    assert_post_equal(data, created_post)
