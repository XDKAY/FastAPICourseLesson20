import jwt
from datetime import datetime, timedelta, timezone
from application.app.core.config.settings import settings

__all__ = ("token_helper", )


class TokenHelper:
    def __init__(self, algorithm: str, secret: str, exp: int) -> None:
        self._algorithm = algorithm
        self._secret = secret
        self._exp = exp

    def generate(self, payload: dict) -> str:
        payload_copy = payload.copy()
        payload_copy["exp"] = datetime.now(timezone.utc) + timedelta(minutes=self._exp)

        return jwt.encode(
            payload_copy,
            self._secret,
            algorithm=self._algorithm,
        )

    def verify(self, token: str) -> dict:
        try:
            payload = jwt.decode(
                token,
                self._secret,
                algorithms=[self._algorithm],
            )
            return payload

        except jwt.exceptions.ExpiredSignatureError:
            raise

        except jwt.exceptions.InvalidTokenError:
            raise


token_helper = TokenHelper(
    algorithm=settings.jwt.algorithm,
    secret=settings.jwt.secret.get_secret_value(),
    exp=settings.jwt.exp,
)
