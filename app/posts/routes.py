from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

from app.core.db_engine import SessionLocal
from app.posts.exceptions import PostNotFoundException
from app.posts.mappers import create_request_to_dto, update_request_to_dto
from app.posts.repository import DBPostRepository
from app.posts.schemas import PostCreateRequest, PostReadResponse, PostUpdateRequest
from app.posts.service import IPostRepository, PostService

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
    return service.create_post(create_request_to_dto(post_data))


@router.get("/posts/{post_id}", response_model=PostReadResponse)
async def read_post(
    post_id: UUID,
    service: PostService = Depends(get_post_service),
):
    post = service.get_post_by_id(post_id)
    if post is None:
        _report_post_not_found()

    return post


@router.patch("/posts/{post_id}", response_model=PostReadResponse)
async def update_post(
    post_id: UUID,
    post_data: PostUpdateRequest,
    service: PostService = Depends(get_post_service),
):
    try:
        result = service.update_post(post_id, update_request_to_dto(post_data))
        if result is None:
            raise HTTPException(status_code=HTTP_204_NO_CONTENT)
        return result
    except PostNotFoundException:
        _report_post_not_found()


@router.delete("/posts/{post_id}", status_code=HTTP_204_NO_CONTENT)
async def delete_post(
    post_id: UUID,
    service: PostService = Depends(get_post_service),
):
    service.delete_post(post_id)


def _report_post_not_found():
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Post not found")
