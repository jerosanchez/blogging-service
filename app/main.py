from fastapi import FastAPI

from app.core.config import config
from app.core.logging import setup_logging
from app.posts.api.v1.posts import router as posts_router

setup_logging()

app = FastAPI(title=config.app_name, debug=config.debug)


app.include_router(posts_router, prefix="/api/v1", tags=["posts"])
