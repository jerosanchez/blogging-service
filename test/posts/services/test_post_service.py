from test.posts.helpers.factories import build_post
from unittest.mock import MagicMock

import pytest

from app.posts.services.post_service import IPostRepository, PostService


@pytest.fixture
def mock_repository() -> MagicMock:
    return MagicMock(spec=IPostRepository)


@pytest.fixture
def post_service(mock_repository: MagicMock) -> PostService:
    return PostService(repository=mock_repository)


def test_get_all_posts_with_data(
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


def test_get_all_posts_empty(post_service: PostService, mock_repository: MagicMock):
    # Arrange
    mock_repository.get_all_posts.return_value = []

    # Act
    result = post_service.get_all_posts()

    # Assert
    assert result == []
