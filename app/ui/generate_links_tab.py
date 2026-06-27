import customtkinter

class GenerateLinksTab(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.label = customtkinter.CTkLabel(
            self,
            text="Секретный ключ:"
        )
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.secret_key = customtkinter.CTkEntry(
            self,
            width=350,
            placeholder_text="Введите секретный ключ"
        )
        self.secret_key.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="w")

        self.generate_button = customtkinter.CTkButton(
            self,
            text="Сгенерировать ссылки",
            command=self.generate_links
        )
        self.generate_button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    def generate_links(self):
        print("Генерация ссылок")