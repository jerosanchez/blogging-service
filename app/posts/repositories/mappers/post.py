from posts.models import Post

from app.posts.repositories.models.post import Post as DBPost


def to_db(domain_post: Post) -> DBPost:
    return DBPost(
        id=domain_post.id,
        title=domain_post.title,
        content=domain_post.content,
        published=domain_post.published,
        rating=domain_post.rating,
    )


# DB layer -> Domain layer
def to_domain(db_post: DBPost) -> Post:
    return Post(
        id=db_post.id,
        title=db_post.title,
        content=db_post.content,
        published=db_post.published,
        rating=db_post.rating,
    )
