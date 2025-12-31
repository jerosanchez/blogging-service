from app.posts.api.v1.schemas.post import PostCreateRequest
from app.posts.services.dtos.post import PostCreateDTO


def to_dto(post_data: PostCreateRequest) -> PostCreateDTO:
    return PostCreateDTO(
        title=post_data.title,
        content=post_data.content,
        published=post_data.published,
        rating=post_data.rating,
    )
