from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from src.api.v1.routes import routes
from src.core.config import get_settings
from src.core.database import Database

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting up database mongodb")
    await Database.get_connection()
    await routes(app)

    yield

    logger.info("Shutting down...")
    await Database.close_connection()


def create_app() -> FastAPI:
    """This function is to initialize the application and all configurations."""
    application = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description=settings.APP_DESCRIPTION,
        root_path=settings.ROOT_PATH,
        lifespan=lifespan,
    )

    return application


app = create_app()
