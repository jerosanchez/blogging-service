from sqlalchemy.orm import Session

from app.posts.models.db_schema import Post as DBPost
from app.posts.models.domain import Post
from app.posts.services.post_service import PostRepositoryABC


def map_to_domain(db_post: DBPost) -> Post:
    return Post(
        id=db_post.id,
        title=db_post.title,
        content=db_post.content,
        published=db_post.published,
        rating=db_post.rating,
    )


class DBPostRepository(PostRepositoryABC):
    def __init__(self, session: Session):
        self._db = session

    def get_all_posts(self) -> list[Post]:
        return list(map(map_to_domain, self._db.query(DBPost).all()))
