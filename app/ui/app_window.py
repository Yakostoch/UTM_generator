import customtkinter
from app.ui.tabview import MyTabView
import app

class AppWindow(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("UTM Generator")
        self.geometry("900x600")

        self.tabview = MyTabView(self)
        self.tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")