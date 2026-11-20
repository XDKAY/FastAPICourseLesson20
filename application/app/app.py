from fastapi import FastAPI
from application.app.api import routers as api_routers

from application.app.handlers.exceptions import register_exceptions_handler

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_routers)

    register_exceptions_handler(app)

    return app
