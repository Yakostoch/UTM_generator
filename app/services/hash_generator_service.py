import hmac
import hashlib
from app.state import AppState


class HashGeneratorService:
    def __init__(self, app_state: AppState):
        self.app_state = app_state

    def generate_hashes(self, users: list[dict], secret_key: str) -> list[str]:
        if not users:
            raise ValueError("Список пользователей пустой")
        if not secret_key:
            raise ValueError("Секретный ключ не может быть пустым")

        hashes = []

        for user in users:
            email = user.get("email")

            if not email:
                continue

            normalized_email = self._normalize_email(email)
            user_hash = self._generate_hmac_sha256(
                normalized_email,
                secret_key,
            )
            hashes.append(user_hash)

        self.app_state.generated_hashes = hashes
        
        return hashes

    def _normalize_email(self, email: str) -> str:
        return email.strip().lower()

    def _generate_hmac_sha256(self, value: str, secret_key: str) -> str:
        key_bytes = secret_key.encode("utf-8")
        value_bytes = value.encode("utf-8")
        return hmac.new(key_bytes, value_bytes, hashlib.sha256).hexdigest()
