from app.posts.models.db_schema import Post as DBPost
from app.posts.models.domain import Post


def map_db_post(db_post: DBPost) -> Post:
    return Post(
        id=db_post.id,
        title=db_post.title,
        content=db_post.content,
        published=db_post.published,
        rating=db_post.rating,
    )
