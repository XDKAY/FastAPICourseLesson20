from typing import Annotated
from pydantic import BaseModel, Field, SecretStr


class UserRequestScheme(BaseModel):
    username: Annotated[str, Field(examples=["John"], min_length=3, max_length=20)]
    password: Annotated[SecretStr, Field(examples=["qwerty123"], min_length=8, max_length=20)]
