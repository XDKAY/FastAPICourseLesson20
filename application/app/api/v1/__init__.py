from fastapi import APIRouter
from .routers import routers
from application.app.core.config.settings import settings

routers_version = APIRouter(prefix=settings.api.version)
routers_version.include_router(routers)
