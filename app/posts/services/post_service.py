from abc import ABC, abstractmethod

from app.posts.models.domain import Post


class PostRepositoryABC(ABC):
    @abstractmethod
    def get_all_posts(self) -> list[Post]:
        pass


class PostService:
    def __init__(self, repository: PostRepositoryABC):
        self._repository = repository

    def get_all_posts(self) -> list[Post]:
        return self._repository.get_all_posts()
