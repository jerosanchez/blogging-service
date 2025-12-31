from fastapi import APIRouter, Depends

from app.core.db_engine import SessionLocal
from app.posts.api.v1.schemas import PostReadResponse
from app.posts.repositories.post_repository import DBPostRepository
from app.posts.services.post_service import PostRepositoryABC, PostService

router = APIRouter()


def get_post_repository() -> PostRepositoryABC:
    return DBPostRepository(session=SessionLocal())


def get_post_service() -> PostService:
    return PostService(repository=get_post_repository())


@router.get("/posts", response_model=list[PostReadResponse])
async def read_posts(service: PostService = Depends(get_post_service)):
    return service.get_all_posts()
