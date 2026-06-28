class AppState:
    def __init__(self):
        self.input_file_path = None
        self.output_file_path = None
        self.users = []
        self.utm_params = {
            "base_url": "",
            "source": "",
            "utm_medium": "",
            "utm_campaign": "",
            "utm_content": "",
            "secret_key": ""
        }
        self.generated_hashes = []
        sel