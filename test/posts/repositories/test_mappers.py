import uuid

from app.posts.models.db_schema import Post as DBPost
from app.posts.models.domain import Post
from app.posts.repositories.mappers import map_db_post


def test_map_db_post_maps_all_fields():
    test_id = uuid.uuid4()
    db_post = DBPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=False,
        rating=7,
    )
    result = map_db_post(db_post)
    assert isinstance(result, Post)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is False
    assert result.rating == 7


def test_map_db_post_maps_missing_rating():
    test_id = uuid.uuid4()
    db_post = DBPost(
        id=test_id,
        title="Test Title",
        content="Test Content",
        published=True,
    )
    result = map_db_post(db_post)
    assert result.id == test_id
    assert result.title == "Test Title"
    assert result.content == "Test Content"
    assert result.published is True
    assert result.rating is None
