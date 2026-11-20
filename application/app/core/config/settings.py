from typing import Annotated
from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, SecretStr, Field

__all__ = ("settings", )


class ApiSettings(BaseModel):
    prefix: str = "/api"
    version: str = "/v1"


class TokenSettings(BaseModel):
    secret: Annotated[SecretStr, Field(..., alias="SECRET")]
    algorithm: Annotated[str, Field(..., alias="ALGORITHM")]
    exp: Annotated[int, Field(..., alias="EXP")]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8",
        env_prefix="APP_",
        env_nested_delimiter="__",
        extra="ignore",
    )

    api: ApiSettings = ApiSettings()
    jwt: TokenSettings


settings = Settings()
