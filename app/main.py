from fastapi import FastAPI

from app.core.config import config
from app.core.logging import setup_logging
from app.posts.api.v1 import post

setup_logging()

app = FastAPI(title=config.app_name, debug=config.debug)


app.include_router(post.router, prefix="/api/v1", tags=["posts"])
