import customtkinter

from app.ui.tabs.main_tab import MainTab
from app.ui.tabs.upload_tab import UploadTab
from app.ui.tabs.generate_links_tab import GenerateLinksTab


class AppWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTM Generator")
        self.geometry("1000x650")
        self.minsize(900, 600)

        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = customtkinter.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsw")
        self.sidebar.grid_rowconfigure(5, weight=1)

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar,
            text="UTM Generator",
            font=customtkinter.CTkFont(size=22, weight="bold")
        )
        self.logo_label.grid(row=0, column=0, padx=24, pady=(30, 20), sticky="w")

        self.main_button = customtkinter.CTkButton(
            self.sidebar,
            text="Главная",
            height=42,
            command=self.show_main_tab
        )
        self.main_button.grid(row=1, column=0, padx=20, pady=8, sticky="ew")

        self.upload_button = customtkinter.CTkButton(
            self.sidebar,
            text="Загрузить пользователей",
            height=42,
            command=self.show_upload_tab
        )
        self.upload_button.grid(row=2, column=0, padx=20, pady=8, sticky="ew")

        self.generate_button = customtkinter.CTkButton(
            self.sidebar,
            text="Сгенерировать ссылку",
            height=42,
            command=self.show_generate_tab
        )
        self.generate_button.grid(row=3, column=0, padx=20, pady=8, sticky="ew")

        self.version_label = customtkinter.CTkLabel(
            self.sidebar,
            text="v0.1.0",
            text_color="gray"
        )
        self.version_label.grid(row=6, column=0, padx=20, pady=20, sticky="sw")

        self.content_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.content_frame.grid(row=0, column=1, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.current_tab = None
        self.show_main_tab()

    def clear_content(self):
        if self.current_tab is not None:
            self.current_tab.destroy()

    def show_main_tab(self):
        self.clear_content()
        self.current_tab = MainTab(self.content_frame)
        self.current_tab.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

    def show_upload_tab(self):
        self.clear_content()
        self.current_tab = UploadTab(self.content_frame)
        self.current_tab.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

    def show_generate_tab(self):
        self.clear_content()
        self.current_tab = GenerateLinksTab(self.content_frame)
        self.current_tab.grid(row=0, column=0, sticky="nsew", padx=30, pady=30)