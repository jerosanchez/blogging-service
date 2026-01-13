import uuid

from app.posts.domain import Post as DomainPost
from app.posts.mappers import db_to_domain, domain_to_db
from app.posts.models import Post as DBPost


def test_to_db_returns_db_post_with_all_fields_when_all_fields_provided():
    # Arrange
    test_id = uuid.uuid4()
    domain_post = DomainPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=True,
        rating=5,
    )

    # Act
    result = domain_to_db(domain_post)

    # Assert
    assert isinstance(result, DBPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating == 5


def test_to_db_returns_db_post_with_defaults_when_optional_fields_missing():
    # Arrange
    test_id = uuid.uuid4()
    domain_post = DomainPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=False,
        rating=None,
    )

    # Act
    result = domain_to_db(domain_post)

    # Assert
    assert isinstance(result, DBPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is False
    assert result.rating is None


def test_to_domain_returns_domain_post_with_all_fields_when_all_fields_provided():
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
    result = db_to_domain(post)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is False
    assert result.rating == 7


def test_to_domain_returns_domain_post_with_defaults_when_optional_fields_missing():
    # Arrange
    test_id = uuid.uuid4()
    post = DBPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=True,
    )

    # Act
    result = db_to_domain(post)

    # Assert
    assert isinstance(result, DomainPost)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating is None
