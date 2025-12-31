from abc import ABC, abstractmethod

from app.posts.domain.post import Post
from app.posts.services.dtos.post import PostCreateDTO
from app.posts.services.mappers.post import to_domain


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
        return self._repository.add_post(to_domain(post_data))
