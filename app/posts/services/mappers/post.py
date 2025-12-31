from app.posts.domain.post import Post
from app.posts.services.dtos.post import PostCreateDTO


def to_domain(post_create_dto: PostCreateDTO) -> Post:
    return Post(
        title=post_create_dto.title,
        content=post_create_dto.content,
        published=post_create_dto.published,
        rating=post_create_dto.rating,
    )
