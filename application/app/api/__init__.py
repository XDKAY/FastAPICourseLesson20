from fastapi import APIRouter
from .v1 import routers_version
from application.app.core.config.settings import settings

routers = APIRouter(prefix=settings.api.prefix)
routers.include_router(routers_version)
