import customtkinter
from app.state import AppState
class UtmParamsTab(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.app_state = AppState()
        self.base_url_label = customtkinter.CTkLabel(
            self,
            text="Базовая ссылка:"
        )
        self.base_url_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.base_url_entry = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="https://site.ru/offer"
        )
        self.base_url_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        self.utm_source_label = customtkinter.CTkLabel(
            self,
            text="utm_source:"
        )
        self.utm_source_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.utm_source_entry = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="yandex_rassylki"
        )
        self.utm_source_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.utm_medium_label = customtkinter.CTkLabel(
            self,
            text="utm_medium:"
        )
        self.utm_medium_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        self.utm_medium_entry = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="email"
        )
        self.utm_medium_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        self.utm_campaign_label = customtkinter.CTkLabel(
            self,
            text="utm_campaign:"
        )
        self.utm_campaign_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.utm_campaign_entry = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="detmir_june_2026"
        )
        self.utm_campaign_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        self.utm_content_label = customtkinter.CTkLabel(
            self,
            text="utm_content:"
        )
        self.utm_content_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        self.utm_content_entry = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="main_button"
        )
        self.utm_content_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        self.label = customtkinter.CTkLabel(
            self,
            text="Секретный ключ:"
        )
        self.label.grid(row=5, column=0, padx=20, pady=(20, 10), sticky="w")

        self.secret_key = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="Введите секретный ключ"
        )
        self.secret_key.grid(row=5, column=1, padx=20, pady=(20, 10), sticky="w")

        self.generate_button = customtkinter.CTkButton(
            self,
            text="Сгенерировать хэши и общую utm ссылку"
        )
        self.generate_button.grid(row=6, column=0, padx=20, pady=10, sticky="w")

    def get_utm_params(self):
        return {
            "base_url": self.base_url_entry.get(),
            "utm_source": self.utm_source_entry.get(),
            "utm_medium": self.utm_medium_entry.get(),
            "utm_campaign": self.utm_campaign_entry.get(),
            "utm_content": self.utm_content_entry.get()
        }
