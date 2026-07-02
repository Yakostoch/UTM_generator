from tkinter import messagebox

import customtkinter

from app.services.link_generator_service import LinkGeneratorService
from app.state import AppState


class UtmParamsTab(customtkinter.CTkFrame):
    def __init__(self, master, app_state: AppState | None = None):
        super().__init__(master)

        self.app_state = app_state or AppState()
        self.link_generator_service = LinkGeneratorService(self.app_state)
        self.generated_link = ""

        self.grid_columnconfigure(1, weight=1)

        # Базовая ссылка текст
        self.base_url_label = customtkinter.CTkLabel(self, text="Базовая ссылка:")
        self.base_url_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        # Базовая ссылка текстовое поле
        self.base_url_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="https://site.ru/offer"
        )
        self.base_url_entry.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        # UTM source текст
        self.utm_source_label = customtkinter.CTkLabel(self, text="utm_source:")
        self.utm_source_label.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        # UTM source текстовое поле
        self.utm_source_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="yandex_rassylki"
        )
        self.utm_source_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        # UTM medium текст
        self.utm_medium_label = customtkinter.CTkLabel(self, text="utm_medium:")
        self.utm_medium_label.grid(row=2, column=0, padx=20, pady=10, sticky="w")

        # UTM medium текстовое поле
        self.utm_medium_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="email"
        )
        self.utm_medium_entry.grid(row=2, column=1, padx=20, pady=10, sticky="w")

        # UTM campaign текст
        self.utm_campaign_label = customtkinter.CTkLabel(self, text="utm_campaign:")
        self.utm_campaign_label.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        # UTM campaign текстовое поле
        self.utm_campaign_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="detmir_june_2026"
        )
        self.utm_campaign_entry.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        # UTM content текст
        self.utm_content_label = customtkinter.CTkLabel(self, text="utm_content:")
        self.utm_content_label.grid(row=4, column=0, padx=20, pady=10, sticky="w")

        # UTM content текстовое поле
        self.utm_content_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="main_button"
        )
        self.utm_content_entry.grid(row=4, column=1, padx=20, pady=10, sticky="w")

        # UTM term текст
        self.utm_term_label = customtkinter.CTkLabel(self, text="utm_term:")
        self.utm_term_label.grid(row=5, column=0, padx=20, pady=10, sticky="w")

        # UTM term текстовое поле
        self.utm_term_entry = customtkinter.CTkEntry(
            self, width=350, placeholder_text="keyword"
        )
        self.utm_term_entry.grid(row=5, column=1, padx=20, pady=10, sticky="w")

        # Кнопка генерации
        self.generate_button = customtkinter.CTkButton(
            self, text="Сгенерировать UTM-ссылку", command=self.generate_link
        )
        self.generate_button.grid(row=6, column=0, padx=20, pady=10, sticky="w")

        # Поле для отображения сгенерированной ссылки
        self.generated_link_box = customtkinter.CTkTextbox(self, height=80, width=650)

        self.generated_link_box.grid(
            row=7, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew"
        )
        self.generated_link_box.configure(state="disabled")
        self.generated_link_box.grid_remove()

        # Кнопка копирования ссылки
        self.copy_button = customtkinter.CTkButton(
            self, text="Скопировать", command=self.copy_link, state="disabled"
        )

        self.copy_button.grid(row=8, column=0, padx=20, pady=10, sticky="w")
        self.copy_button.grid_remove()

    # функция для получения UTM-параметров из полей ввода
    def get_utm_params(self):
        return {
            "base_url": self.base_url_entry.get().strip(),
            "source": self.utm_source_entry.get().strip(),
            "utm_medium": self.utm_medium_entry.get().strip(),
            "utm_campaign": self.utm_campaign_entry.get().strip(),
            "utm_content": self.utm_content_entry.get().strip(),
            "utm_term": self.utm_term_entry.get().strip(),
        }

    # функция для генерации ссылки с UTM-параметрами
    def generate_link(self):
        utm_params = self.get_utm_params()
        required_fields = {
            "base_url": "Базовая ссылка",
            "source": "utm_source",
            "utm_medium": "utm_medium",
            "utm_campaign": "utm_campaign",
        }

        missing_fields = [
            label for key, label in required_fields.items() if not utm_params[key]
        ]

        if missing_fields:
            messagebox.showwarning(
                "UTM Generator",
                f"Заполните обязательные поля: {', '.join(missing_fields)}",
            )
            return

        try:
            self.generated_link = self.link_generator_service.generate_link(utm_params)
            # отображение сгенерированной ссылки и кнопки копирования
            self.generated_link_box.grid()
            self.copy_button.grid()

            self.generated_link_box.configure(state="normal")
            self.generated_link_box.delete("1.0", "end")
            self.generated_link_box.insert("1.0", self.generated_link)
            self.generated_link_box.configure(state="disabled")
            self.copy_button.configure(state="normal")
        except Exception as error:
            messagebox.showerror("UTM Generator", f"Ошибка генерации ссылки:\n{error}")

    def copy_link(self):
        if not self.generated_link:
            messagebox.showwarning("UTM Generator", "Сначала сгенерируйте ссылку")
            return

        self.clipboard_clear()
        self.clipboard_append(self.generated_link)
        messagebox.showinfo("UTM Generator", "Ссылка скопирована")
