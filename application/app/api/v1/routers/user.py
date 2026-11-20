from fastapi import APIRouter, Depends, HTTPException, status
from application.app.core.schemes.user import UserRequestScheme
from application.app.core.schemes.token import TokenResponseScheme
from application.app.auth.user import auth_user, current_user
from application.app.core.security.token import token_helper


router = APIRouter(tags=["User"])


@router.post("/login", response_model=TokenResponseScheme)
def login_endpoint(user: UserRequestScheme):

    if not auth_user(user.username, user.password.get_secret_value()):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentails",
        )

    payload = {
        "sub": user.username
    }

    token = token_helper.generate(payload)

    return TokenResponseScheme(
        access_token=token
    )


@router.get("/protected_resource", dependencies=[Depends(current_user)])
def protected_resource_endpoint() -> dict:
    return {"status": "ok"}
