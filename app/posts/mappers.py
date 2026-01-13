from app.posts.dtos import PostCreateDTO, PostUpdateDTO
from app.posts.models import Post
from app.posts.schemas import PostCreateRequest, PostUpdateRequest

# ---------- API layer


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


# ---------- Service layer


def to_domain(post_create_dto: PostCreateDTO) -> Post:
    return Post(
        title=post_create_dto.title,
        content=post_create_dto.content,
        published=post_create_dto.published,
        rating=post_create_dto.rating,
    )
