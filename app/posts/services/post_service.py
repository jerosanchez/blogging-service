from abc import ABC, abstractmethod

from app.posts.domain.post import Post
from app.posts.services.dtos.post import PostCreateDTO


class IPostRepository(ABC):
    @abstractmethod
    def get_all_posts(self) -> list[Post]:
        pass

    @abstractmethod
    def add_post(self, post: Post) -> Post:
        pass


class PostService:
    def __init__(self, repository: IPostRepository):
        self._repository = repository

    def get_all_posts(self) -> list[Post]:
        return self._repository.get_all_posts()

    def create_post(self, post_data: PostCreateDTO) -> Post:
        new_post = Post(
            title=post_data.title,
            content=post_data.content,
            published=post_data.published,
            rating=post_data.rating,
        )
        return self._repository.add_post(new_post)
