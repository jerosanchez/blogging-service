from test.posts.helpers.factories import build_post
from unittest.mock import MagicMock
from uuid import UUID

import pytest

from app.posts.dtos import PostCreateDTO, PostUpdateDTO
from app.posts.exceptions import PostNotFoundException
from app.posts.service import IPostRepository, PostService


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


def test_get_post_by_id_returns_post_when_found(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("e2f1c3b4-5d6e-7a8b-9c0d-1e2f3a4b5c6d")
    expected_post = build_post(id=post_id)
    mock_repository.get_post_by_id.return_value = expected_post

    # Act
    result = post_service.get_post_by_id(post_id)

    # Assert
    assert result == expected_post


def test_get_post_by_id_returns_none_when_not_found(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("00000000-0000-0000-0000-000000000000")
    mock_repository.get_post_by_id.return_value = None

    # Act
    result = post_service.get_post_by_id(post_id)

    # Assert
    assert result is None


def test_update_post_returns_updated_post_when_valid_data(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("12345678-1234-5678-1234-567812345678")
    update_data = PostUpdateDTO(title="Updated Title", content="Updated Content")
    expected_post = build_post(
        id=post_id, title="Updated Title", content="Updated Content"
    )
    mock_repository.update_post.return_value = expected_post

    # Act
    result = post_service.update_post(post_id, update_data)

    # Assert
    assert result == expected_post


def test_update_post_returns_none_when_all_fields_none(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("87654321-4321-8765-4321-876543218765")
    update_data = PostUpdateDTO()  # All fields None

    # Act
    result = post_service.update_post(post_id, update_data)

    # Assert
    mock_repository.update_post.assert_not_called()
    assert result is None


def test_update_post_raises_exception_when_repository_returns_none(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("99999999-9999-9999-9999-999999999999")
    update_data = PostUpdateDTO(title="Doesn't matter")
    mock_repository.update_post.return_value = None  # Simulate not found

    # Act & Assert
    with pytest.raises(PostNotFoundException) as exc_info:
        post_service.update_post(post_id, update_data)
    assert str(post_id) in str(exc_info.value)


def test_delete_post_returns_none_when_not_found_or_already_deleted(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("99999999-9999-9999-9999-999999999999")
    mock_repository.delete_post.return_value = (
        False  # Simulate not found or already deleted
    )

    # Act
    result = post_service.delete_post(post_id)

    # Assert
    assert result is None


def test_delete_post_returns_none_when_deletion_is_successful(
    post_service: PostService, mock_repository: MagicMock
):
    # Arrange
    post_id = UUID("99999999-9999-9999-9999-999999999999")
    mock_repository.delete_post.return_value = True  # Simulate successful deletion

    # Act
    result = post_service.delete_post(post_id)

    # Assert
    assert result is None
