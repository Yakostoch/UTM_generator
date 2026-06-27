import hashlib
import hmac
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode


def add_user_hash_to_utm_link(email: str, utm_url: str, secret_key: str) -> str:
    """
    Принимает email пользователя, UTM-ссылку и секретный ключ.
    Возвращает ссылку с дополнительным параметром user_hash.

    SHA-256 не расшифровывается.
    Здесь используется HMAC-SHA256: хеш от email + секретного ключа.
    """

    if not email:
        raise ValueError("Email не должен быть пустым")

    if not utm_url:
        raise ValueError("UTM-ссылка не должна быть пустой")

    if not secret_key:
        raise ValueError("Секретный ключ не должен быть пустым")

    normalized_email = email.strip().lower()

    user_hash = hmac.new(
        secret_key.encode("utf-8"),
        normalized_email.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()

    url_parts = urlsplit(utm_url)

    query_params = dict(parse_qsl(url_parts.query))

    query_params["user_hash"] = user_hash

    new_query = urlencode(query_params)

    new_url = urlunsplit((
        url_parts.scheme,
        url_parts.netloc,
        url_parts.path,
        new_query,
        url_parts.fragment
    ))

    return new_url