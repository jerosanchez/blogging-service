from app.posts.dtos import PostCreateDTO
from app.posts.mappers import to_domain
from app.posts.models import Post as DomainPost


def test_to_domain_returns_post_with_all_fields_when_all_fields_provided():
    # Arrange
    dto = PostCreateDTO(
        title="Test Title",
        content="Test Content",
        published=True,
        rating=10,
    )

    # Act
    result = to_domain(dto)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating == 10


def test_to_domain_returns_post_with_defaults_when_optional_fields_missing():
    # Arrange
    dto = PostCreateDTO(
        title="Default Title",
        content="Default Content",
    )

    # Act
    result = to_domain(dto)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.title == "Default Title"
    assert result.content == "Default Content"
    assert result.published is False
    assert result.rating is None
