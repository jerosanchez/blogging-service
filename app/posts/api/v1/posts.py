from fastapi import APIRouter, Depends

from app.core.db_engine import SessionLocal
from app.posts.api.v1.mappers.post import to_dto
from app.posts.api.v1.schemas.post import PostCreateRequest, PostReadResponse
from app.posts.repositories.db_post_repository import DBPostRepository
from app.posts.services.post_service import IPostRepository, PostService

router = APIRouter()


def get_post_repository() -> IPostRepository:
    return DBPostRepository(session=SessionLocal())


def get_post_service() -> PostService:
    return PostService(repository=get_post_repository())


@router.get("/posts", response_model=list[PostReadResponse])
async def read_posts(service: PostService = Depends(get_post_service)):
    return service.get_all_posts()


@router.post("/posts", response_model=PostReadResponse)
async def create_post(
    post_data: PostCreateRequest,
    service: PostService = Depends(get_post_service),
):
    return service.create_post(to_dto(post_data))
