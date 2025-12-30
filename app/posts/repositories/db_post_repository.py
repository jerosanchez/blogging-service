from sqlalchemy.orm import Session

from app.posts.models.db_schema import Post as DBPost
from app.posts.models.domain import Post
from app.posts.repositories.mappers import map_db_post as map_to_domain
from app.posts.services.post_service import PostRepositoryABC


class DBPostRepository(PostRepositoryABC):
    def __init__(self, session: Session):
        self._db = session

    def get_all_posts(self) -> list[Post]:
        return list(map(map_to_domain, self._db.query(DBPost).all()))
