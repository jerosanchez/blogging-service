from app.posts.domain import Post as DomainPost
from app.posts.dtos import PostCreateDTO, PostUpdateDTO
from app.posts.models import Post as DBPost
from app.posts.schemas import PostCreateRequest, PostUpdateRequest

# ---------- API layer


def create_request_to_dto(post_data: PostCreateRequest) -> PostCreateDTO:
    return PostCreateDTO(
        title=post_data.title,
        content=post_data.content,
        published=post_data.published,
        rating=post_data.rating,
    )


def update_request_to_dto(post_data: PostUpdateRequest) -> PostUpdateDTO:
    return PostUpdateDTO(
        title=post_data.title,
        content=post_data.content,
        published=post_data.published,
        rating=post_data.rating,
    )


# ---------- Service/Domain layer


def dto_to_domain(post_create_dto: PostCreateDTO) -> DomainPost:
    return DomainPost(
        title=post_create_dto.title,
        content=post_create_dto.content,
        published=post_create_dto.published,
        rating=post_create_dto.rating,
    )


# ---------- DB layer


def domain_to_db(domain_post: DomainPost) -> DBPost:
    return DBPost(
        id=domain_post.id,
        title=domain_post.title,
        content=domain_post.content,
        published=domain_post.published,
        rating=domain_post.rating,
    )


def db_to_domain(db_post: DBPost) -> DomainPost:
    return DomainPost(
        id=db_post.id,
        title=db_post.title,
        content=db_post.content,
        published=db_post.published,
        rating=db_post.rating,
    )
