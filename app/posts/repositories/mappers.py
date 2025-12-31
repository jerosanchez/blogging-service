from app.posts.domain.post import Post
from app.posts.repositories.models import DBPost


def map_post(db_post: DBPost) -> Post:
    return Post(
        id=db_post.id,
        title=db_post.title,
        content=db_post.content,
        published=db_post.published,
        rating=db_post.rating,
    )
