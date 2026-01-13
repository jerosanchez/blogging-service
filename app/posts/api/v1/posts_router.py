from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app.core.db_engine import SessionLocal
from app.posts.api.v1.mappers.post import to_dto
from app.posts.api.v1.schemas.post import PostCreateRequest, PostReadResponse
from app.posts.repositories.db_post_repository import DBPostRepository
from app.posts.services.exceptions.post import PostNotFoundException
from app.posts.services.post_service import IPostRepository, PostService

router = APIRouter()


def get_post_repository() -> IPostRepository:
    return DBPostRepository(session=SessionLocal())


def get_post_service() -> PostService:
    return PostService(repository=get_post_repository())


@router.get("/posts", response_model=list[PostReadResponse])
async def read_posts(service: PostService = Depends(get_post_service)):
    return service.get_all_posts()


@router.post("/posts", response_model=PostReadResponse, status_code=HTTP_201_CREATED)
async def create_post(
    post_data: PostCreateRequest,
    service: PostService = Depends(get_post_service),
):
    return service.create_post(to_dto(post_data))


@router.get("/posts/{post_id}", response_model=PostReadResponse)
async def read_post(
    post_id: UUID,
    service: PostService = Depends(get_post_service),
):
    post = service.get_post_by_id(post_id)
    if post is None:
        _report_post_not_found()

    return post


@router.put("/posts/{post_id}", response_model=PostReadResponse)
async def update_post(
    post_id: UUID,
    post_data: PostCreateRequest,
    service: PostService = Depends(get_post_service),
):
    try:
        updated_post = service.update_post(post_id, to_dto(post_data))
        return updated_post

    except PostNotFoundException:
        _report_post_not_found()


def _report_post_not_found():
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
