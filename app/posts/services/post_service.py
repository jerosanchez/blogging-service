from abc import ABC, abstractmethod
from dataclasses import asdict
from typing import Any, Dict, Optional
from uuid import UUID

from app.posts.domain.post import Post
from app.posts.services.dtos.post import PostCreateDTO, PostUpdateDTO
from app.posts.services.exceptions.post import PostNotFoundException
from app.posts.services.mappers.post import to_domain


class IPostRepository(ABC):
    @abstractmethod
    def get_all_posts(self) -> list[Post]:
        pass

    @abstractmethod
    def add_post(self, post: Post) -> Post:
        pass

    @abstractmethod
    def get_post_by_id(self, post_id: UUID) -> Optional[Post]:
        pass

    @abstractmethod
    def update_post(self, post_id: UUID, post: Dict[str, Any]) -> Optional[Post]:
        pass


class PostService:
    def __init__(self, repository: IPostRepository):
        self._repository = repository

    def get_all_posts(self) -> list[Post]:
        return self._repository.get_all_posts()

    def create_post(self, post_data: PostCreateDTO) -> Post:
        return self._repository.add_post(to_domain(post_data))

    def get_post_by_id(self, post_id: UUID) -> Optional[Post]:
        return self._repository.get_post_by_id(post_id)

    def update_post(self, post_id: UUID, post_data: PostUpdateDTO) -> Optional[Post]:
        post_dict = asdict(post_data)

        if all(value is None for value in post_dict.values()):
            return None

        updated_post = self._repository.update_post(post_id, post_dict)
        if updated_post is None:
            raise PostNotFoundException(f"Post with id {post_id} not found")

        return updated_post
