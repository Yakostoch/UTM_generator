from app.state import AppState


class LinkGeneratorService:
    def __init__(self, app_state: AppState):
        self.app_state = app_state

    def generate_link(self):
        base_url = self.app_state.utm_params["base_url"]
        utm_source = self.app_state.utm_params["source"]
        utm_medium = self.app_state.utm_params["utm_medium"]
        utm_campaign = self.app_state.utm_params["utm_campaign"]
        utm_content = self.app_state.utm_params["utm_content"]

        # Construct the base UTM link
        utm_link = f"{base_url}?utm_source={utm_source}&utm_medium={utm_medium}&utm_campaign={utm_campaign}&utm_content={utm_content}&'user_hash'"
        
        return utm_link