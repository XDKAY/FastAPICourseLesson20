import jwt
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

__all__ = ("register_exceptions_handler", )


def register_exceptions_handler(app: FastAPI) -> None:
    @app.exception_handler(jwt.exceptions.ExpiredSignatureError)
    def expired_signature_error_hanlder(request: Request, exp: jwt.exceptions.ExpiredSignatureError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Not authenticated"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    @app.exception_handler(jwt.exceptions.InvalidTokenError)
    def invalid_token_error_hanlder(request: Request, exp: jwt.exceptions.InvalidTokenError):
        return JSONResponse(
            status_code=status.HTTP_401_UNAUTHORIZED,
            content={"detail": "Not authenticated"},
            headers={"WWW-Authenticate": "Bearer"},
        )
