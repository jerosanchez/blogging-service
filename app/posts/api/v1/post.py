from fastapi import APIRouter, Depends

from app.core.db_engine import SessionLocal
from app.posts.models.dto import PostRead
from app.posts.repositories.db_post_repository import DBPostRepository
from app.posts.services.post_service import PostService

router = APIRouter()


def get_post_repository():
    return DBPostRepository(session=SessionLocal())


def get_post_service():
    return PostService(repository=get_post_repository())


@router.get("/posts", response_model=list[PostRead])
async def read_posts(service: PostService = Depends(get_post_service)):
    return service.get_all_posts()
