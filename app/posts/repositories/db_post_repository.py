from typing import Any, Dict, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from app.posts.domain.post import Post
from app.posts.repositories.mappers.post import to_db, to_domain
from app.posts.repositories.models.post import Post as DBPost
from app.posts.services.post_service import IPostRepository


class DBPostRepository(IPostRepository):
    def __init__(self, session: Session):
        self._db = session

    def get_all_posts(self) -> list[Post]:
        return list(map(to_domain, self._db.query(DBPost).all()))

    def add_post(self, post: Post) -> Post:
        db_post = to_db(post)
        self._db.add(db_post)
        self._db.commit()
        self._db.refresh(db_post)
        return to_domain(db_post)

    def get_post_by_id(self, post_id: UUID) -> Optional[Post]:
        db_post = self._db.query(DBPost).filter(DBPost.id == post_id).first()
        if db_post:
            return to_domain(db_post)
        return None

    def update_post(self, post_id: UUID, post: Dict[str, Any]) -> Optional[Post]:
        db_post = self._db.query(DBPost).filter(DBPost.id == post_id).first()
        if not db_post:
            return None
        self._patch_db_post(db_post, post)
        self._db.commit()
        self._db.refresh(db_post)
        return to_domain(db_post)

    def _patch_db_post(self, db_post: DBPost, post: Dict[str, Any]):
        for key, value in post.items():
            if hasattr(db_post, key) and value is not None:
                setattr(db_post, key, value)
