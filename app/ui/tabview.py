import customtkinter

from app.ui.upload_tab import UploadTab
from app.ui.utm_params_tab import UtmParamsTab


class MyTabView(customtkinter.CTkTabview):
    def __init__(self, master, app_state, **kwargs):
        super().__init__(master, **kwargs)

        self.app_state = app_state

        self.add("Загрузить файл")
        self.add("UTM-параметры")

        self.upload_file_tab = UploadTab(
            master=self.tab("Загрузить файл"), app_state=self.app_state
        )
        self.upload_file_tab.grid(row=0, column=0, sticky="nsew")

        self.utm_params_tab = UtmParamsTab(master=self.tab("UTM-параметры"))
        self.utm_params_tab.grid(row=0, column=0, sticky="nsew")
