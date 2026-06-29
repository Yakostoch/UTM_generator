from urllib.parse import urlencode

from app.state import AppState


class LinkGeneratorService:
    def __init__(self, app_state: AppState):
        self.app_state = app_state

    def generate_link(self, utm_params: dict | None = None) -> str:
        # CHANGED: accepts params from the UI while preserving AppState as the source of truth.
        if utm_params is not None:
            self.app_state.utm_params.update(utm_params)

        params = self.app_state.utm_params
        base_url = params["base_url"]
        query_params = {
            "utm_source": params["source"],
            "utm_medium": params["utm_medium"],
            "utm_campaign": params["utm_campaign"],
        }

        if params.get("utm_content"):
            query_params["utm_content"] = params["utm_content"]

        if params.get("utm_term"):
            query_params["utm_term"] = params["utm_term"]

        separator = "&" if "?" in base_url else "?"
        return f"{base_url}{separator}{urlencode(query_params)}"
