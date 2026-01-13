from app.posts.schemas import PostCreateRequest, PostUpdateRequest
from app.posts.services.dtos.post import PostCreateDTO, PostUpdateDTO


def post_create_request_to_dto(post_data: PostCreateRequest) -> PostCreateDTO:
    return PostCreateDTO(
        title=post_data.title,
        content=post_data.content,
        published=post_data.published,
        rating=post_data.rating,
    )


def post_update_request_to_dto(post_data: PostUpdateRequest) -> PostUpdateDTO:
    return PostUpdateDTO(
        title=post_data.title,
        content=post_data.content,
        published=post_data.published,
        rating=post_data.rating,
    )
