import uuid

from app.posts.domain.post import Post as DomainPost
from app.posts.repositories.mappers.post import to_domain
from app.posts.repositories.models.post import Post as DBPost


def test_to_domain_maps_all_fields():
    # Arrange
    test_id = uuid.uuid4()
    post = DBPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=False,
        rating=7,
    )

    # Act
    result = to_domain(post)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is False
    assert result.rating == 7


def test_to_domain_maps_missing_rating():
    # Arrange
    test_id = uuid.uuid4()
    post = DBPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=True,
    )

    # Act
    result = to_domain(post)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating is None
