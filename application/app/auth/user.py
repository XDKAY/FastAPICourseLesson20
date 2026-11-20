import secrets
import random
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from application.app.core.security.token import token_helper


__all__ = ("auth_user", "current_user", )

security = HTTPBearer()


def current_user(credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]) -> None:
    token_type = credentials.scheme

    if not secrets.compare_digest(token_type.lower().encode("utf-8"), "bearer".encode("utf-8")):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid token type"
        )

    token = credentials.credentials

    token_helper.verify(token)

    return


def auth_user(username: str, password: str) -> bool:
    return random.choice([True, False])
