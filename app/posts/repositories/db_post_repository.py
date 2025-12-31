from sqlalchemy.orm import Session

from app.posts.domain.post import Post
from app.posts.repositories.mappers.post import to_domain
from app.posts.repositories.models.post import Post as DBPost
from app.posts.services.post_service import IPostRepository


class DBPostRepository(IPostRepository):
    def __init__(self, session: Session):
        self._db = session

    def get_all_posts(self) -> list[Post]:
        return list(map(to_domain, self._db.query(DBPost).all()))

    def add_post(self, post: Post) -> Post:
        return post
