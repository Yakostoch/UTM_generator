import customtkinter
from tkinter import filedialog

class UploadTab(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.label = customtkinter.CTkLabel(
            master=self,
            text="Загрузите файл Excel (.xlsx) или CSV (.csv):"
        )
        self.label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")

        self.button = customtkinter.CTkButton(
            master=self,
            text="Загрузить файл",
            command=self.upload_file
        )
        self.button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
        )
        if file_path:
            print(f"Файл загружен: {file_path}")