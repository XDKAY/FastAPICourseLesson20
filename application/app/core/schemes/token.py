from pydantic import BaseModel


class TokenResponseScheme(BaseModel):
    access_token: str
    type: str = "Bearer"
