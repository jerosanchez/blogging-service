from app.posts.dtos import PostCreateDTO, PostUpdateDTO
from app.posts.mappers import create_request_to_dto, update_request_to_dto
from app.posts.schemas import PostCreateRequest, PostUpdateRequest


def test_create_to_dto_returns_dto_with_all_fields_when_all_fields_provided():
    # Arrange
    request = PostCreateRequest(
        title="Test Title",
        content="Test Content",
        published=True,
        rating=8,
    )

    # Act
    result = create_request_to_dto(request)

    # Assert
    assert isinstance(result, PostCreateDTO)
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating == 8


def test_create_to_dto_returns_dto_with_defaults_when_optional_fields_missing():
    # Arrange
    request = PostCreateRequest(title="Default Title", content="Default Content")

    # Act
    result = create_request_to_dto(request)

    # Assert
    assert isinstance(result, PostCreateDTO)
    assert result.title == "Default Title"
    assert result.content == "Default Content"
    assert result.published is True  # Pydantic default
    assert result.rating is None


def test_update_to_dto_with_all_fields():
    request = PostUpdateRequest(
        title="Updated Title",
        content="Updated Content",
        published=False,
        rating=10,
    )
    result = update_request_to_dto(request)
    assert isinstance(result, PostUpdateDTO)
    assert result.title == "Updated Title"
    assert result.content == "Updated Content"
    assert result.published is False
    assert result.rating == 10


def test_update_to_dto_with_only_some_fields():
    request = PostUpdateRequest(title="Updated Title")
    result = update_request_to_dto(request)
    assert isinstance(result, PostUpdateDTO)
    assert result.title == "Updated Title"
    assert result.content is None
    assert result.published is None
    assert result.rating is None


def test_update_to_dto_with_no_fields():
    request = PostUpdateRequest()
    result = update_request_to_dto(request)
    assert isinstance(result, PostUpdateDTO)
    assert result.title is None
    assert result.content is None
    assert result.published is None
    assert result.rating is None
