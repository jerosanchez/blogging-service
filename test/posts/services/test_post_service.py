from test.posts.helpers.factories import build_post
from unittest.mock import MagicMock

import pytest

from app.posts.services.dtos.post import PostCreateDTO
from app.posts.services.post_service import IPostRepository, PostService


@pytest.fixture
def mock_repository() -> MagicMock:
    return MagicMock(spec=IPostRepository)


@pytest.fixture
def post_service(mock_repository: MagicMock) -> PostService:
    return PostService(repository=mock_repository)


def test_get_all_posts_returns_all_posts_when_data_exists(
    post_service: PostService,
    mock_repository: MagicMock,
):
    # Arrange
    posts = [build_post() for _ in range(3)]
    mock_repository.get_all_posts.return_value = posts

    # Act
    result = post_service.get_all_posts()

    # Assert
    assert result == posts


def test_get_all_posts_returns_empty_list_when_no_posts(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    mock_repository.get_all_posts.return_value = []

    # Act
    result = post_service.get_all_posts()

    # Assert
    assert result == []


def test_create_post_returns_created_post_with_given_data(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_data = PostCreateDTO(
        title="New Post", content="New Content", published=True, rating=5
    )
    expected_post = build_post(
        title="New Post", content="New Content", published=True, rating=5
    )
    mock_repository.add_post.return_value = expected_post

    # Act
    result = post_service.create_post(post_data)

    # Assert
    assert result == expected_post


def test_create_post_returns_created_post_with_defaults(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_data = PostCreateDTO(title="Default Post", content="Default Content")
    expected_post = build_post(
        title="Default Post", content="Default Content", published=False, rating=None
    )
    mock_repository.add_post.return_value = expected_post

    # Act
    result = post_service.create_post(post_data)

    # Assert
    assert result == expected_post
