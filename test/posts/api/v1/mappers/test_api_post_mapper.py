from app.posts.api.v1.mappers.post import post_create_request_to_dto
from app.posts.api.v1.schemas.post import PostCreateRequest
from app.posts.services.dtos.post import PostCreateDTO


def test_to_dto_returns_dto_with_all_fields_when_all_fields_provided():
    # Arrange
    request = PostCreateRequest(
        title="Test Title",
        content="Test Content",
        published=True,
        rating=8,
    )

    # Act
    result = post_create_request_to_dto(request)

    # Assert
    assert isinstance(result, PostCreateDTO)
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating == 8


def test_to_dto_returns_dto_with_defaults_when_optional_fields_missing():
    # Arrange
    request = PostCreateRequest(title="Default Title", content="Default Content")

    # Act
    result = post_create_request_to_dto(request)

    # Assert
    assert isinstance(result, PostCreateDTO)
    assert result.title == "Default Title"
    assert result.content == "Default Content"
    assert result.published is True  # Pydantic default
    assert result.rating is None
