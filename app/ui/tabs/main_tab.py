import customtkinter


class MainTab(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=16)

        self.grid_columnconfigure(0, weight=1)

        self.title = customtkinter.CTkLabel(
            self,
            text="UTM Generator",
            font=customtkinter.CTkFont(size=30, weight="bold")
        )
        self.title.grid(row=0, column=0, padx=30, pady=(30, 10), sticky="w")

        self.subtitle = customtkinter.CTkLabel(
            self,
            text="Сгенерировать ссылки с UTM-метками и создать user-hash для рассылки",
            text_color="gray",
            font=customtkinter.CTkFont(size=15)
        )
        self.subtitle.grid(row=1, column=0, padx=30, pady=(0, 30), sticky="w")

#первая карточка
        self.info_card = customtkinter.CTkFrame(self, corner_radius=14)
        self.info_card.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.info_card.grid_columnconfigure(0, weight=1)

        self.info_title = customtkinter.CTkLabel(
            self.info_card,
            text="Как работать с пользователями(условное название)",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.info_title.grid(row=0, column=0, padx=24, pady=(24, 10), sticky="w")

        self.info_text = customtkinter.CTkLabel( #TO DO сделать памятку под функционал
            self.info_card,
            text=(
                "1. Загрузить файл с пользователями, которые участвуют в рассылке.\n"
                "2. Указать по какому параметру генерировть уникальный хеш.\n"
                "3. Сгенерировать хеш.\n"
                "4. Скачать готовый файл с уникальными хешами."
            ),
            justify="left",
            text_color="gray"
        )
        self.info_text.grid(row=1, column=0, padx=24, pady=(0, 24), sticky="w")

# вторая карточка
        self.second_info_card = customtkinter.CTkFrame(self, corner_radius=14)
        self.second_info_card.grid(row=3, column=0, padx=30, pady=10, sticky="ew")
        self.second_info_card.grid_columnconfigure(0, weight=1)

        self.second_info_title = customtkinter.CTkLabel( # TO DO сделать памятку под функционал
            self.second_info_card,
            text="Как создать UTM-ссылку",
            font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.second_info_title.grid(row=0, column=0, padx=24, pady=(24, 10), sticky="w")

        self.second_info_text = customtkinter.CTkLabel(
            self.second_info_card,
            text=(
                "1. Открыть вкладку с UTM-параметрами.\n"
                "2. Ввести основную ссылку на сайт.\n"
                "3. Заполнить utm_source, utm_medium и utm_campaign.\n"
                "4. Сгенерировать готовую ссылку для рассылки."
            ),
            justify="left",
            text_color="gray"
        )
        self.second_info_text.grid(row=1, column=0, padx=24, pady=(0, 24), sticky="w")
