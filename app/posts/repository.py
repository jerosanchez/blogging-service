from typing import Any, Dict, Optional
from uuid import UUID

from sqlalchemy.orm import Session

from app.posts.domain import Post as DomainPost
from app.posts.mappers import db_to_domain, domain_to_db
from app.posts.models import Post as DBPost
from app.posts.service import IPostRepository


class DBPostRepository(IPostRepository):
    def __init__(self, session: Session):
        self._db = session

    def get_all_posts(self) -> list[DomainPost]:
        return list(map(db_to_domain, self._db.query(DBPost).all()))

    def add_post(self, post: DomainPost) -> DomainPost:
        db_post = domain_to_db(post)
        self._db.add(db_post)
        self._db.commit()
        self._db.refresh(db_post)
        return db_to_domain(db_post)

    def get_post_by_id(self, post_id: UUID) -> Optional[DomainPost]:
        db_post = self._db.query(DBPost).filter(DBPost.id == post_id).first()
        if db_post:
            return db_to_domain(db_post)
        return None

    def update_post(self, post_id: UUID, post: Dict[str, Any]) -> Optional[DomainPost]:
        db_post = self._db.query(DBPost).filter(DBPost.id == post_id).first()
        if not db_post:
            return None
        self._patch_db_post(db_post, post)
        self._db.commit()
        self._db.refresh(db_post)
        return db_to_domain(db_post)

    def _patch_db_post(self, db_post: DBPost, post: Dict[str, Any]):
        for key, value in post.items():
            if hasattr(db_post, key) and value is not None:
                setattr(db_post, key, value)
