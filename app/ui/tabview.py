import customtkinter
from app.ui.upload_tab import UploadTab
from app.ui.utm_params_tab import UtmParamsTab
from app.ui.generate_links_tab import GenerateLinksTab

class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Загрузить файл")
        self.add("UTM-параметры")
        self.add("Сгенерировать ссылки")

        self.upload_file_tab = UploadTab(
            master=self.tab("Загрузить файл")
        )
        self.upload_file_tab.grid(row=0, column=0, sticky="nsew")

        self.utm_params_tab = UtmParamsTab(
            master=self.tab("UTM-параметры")
        )
        self.utm_params_tab.grid(row=0, column=0, sticky="nsew")

        self.generate_links_tab = GenerateLinksTab(
            master=self.tab("Сгенерировать ссылки")
        )
        self.generate_links_tab.grid(row=0, column=0, sticky="nsew")
