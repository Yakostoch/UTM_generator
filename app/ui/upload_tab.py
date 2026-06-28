import customtkinter
from tkinter import filedialog

from app.services.fileloader_service import FileLoaderService


class UploadTab(customtkinter.CTkFrame):
    def __init__(self, master, app_state):
        super().__init__(master)

        self.app_state = app_state
        self.file_loader_service = FileLoaderService()

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
            filetypes=[
                ("Excel files", "*.xlsx"),
                ("CSV files", "*.csv"),
            ],
        )
        if not file_path:
            return

        try:
            users = self.file_loader_service.load_users(file_path)

            self.app_state.selected_file_path = file_path
            self.app_state.users = users

            success_message = (
                f"Файл успешно загружен: {file_path}. "
                f"Количество пользователей: {len(users)}"
            )
            self.status_label.configure(text=success_message)

        except Exception as error:
            error_message = f"Ошибка при загрузке файла: {error}"
            self.status_label.configure(text=error_message)
