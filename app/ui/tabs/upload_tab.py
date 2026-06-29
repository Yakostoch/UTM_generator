from pathlib import Path
from tkinter import filedialog, messagebox

import customtkinter

from app.services.fileloader_service import FileLoaderService
from app.services.hash_export_service import HashExportService
from app.services.hash_generator_service import HashGeneratorService
from app.state import AppState


class UploadTab(customtkinter.CTkFrame):
    def __init__(self, master, app_state: AppState | None = None, **kwargs):
        super().__init__(master, **kwargs)

        self.app_state = app_state or AppState()
        self.fileloader_service = FileLoaderService()
        self.hash_generator_service = HashGeneratorService(self.app_state)
        self.hash_export_service = HashExportService(self.app_state)

        self.loaded_users = []
        self.processed_hashes = []
        self.export_path = None

        self.grid_columnconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(
            master=self,
            text="Загрузите файл Excel (.xlsx) или CSV (.csv):"
        )
        self.label.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="w")

        self.button = customtkinter.CTkButton(
            master=self,
            text="Загрузить файл",
            command=self.upload_file
        )
        self.button.grid(row=1, column=0, padx=20, pady=10, sticky="w")

        self.selected_file_label = customtkinter.CTkLabel(
            master=self,
            text="Файл не выбран",
            text_color="gray"
        )
        self.selected_file_label.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.secret_key_label = customtkinter.CTkLabel(
            master=self,
            text="Секретный ключ:"
        )
        self.secret_key_label.grid(row=2, column=0, padx=20, pady=(20, 10), sticky="w")

        self.secret_key_entry = customtkinter.CTkEntry(
            master=self,
            width=350,
            placeholder_text="Введите секретный ключ"
        )
        self.secret_key_entry.grid(row=2, column=1, padx=20, pady=(20, 10), sticky="w")

        self.generate_hashes_button = customtkinter.CTkButton(
            master=self,
            text="Сгенерировать хэши",
            command=self.generate_hashes
        )
        self.generate_hashes_button.grid(row=3, column=0, padx=20, pady=10, sticky="w")

        self.download_button = customtkinter.CTkButton(
            master=self,
            text="Скачать готовый файл",
            command=self.download_file,
            state="disabled"
        )
        self.download_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
        )
        if not file_path:
            return

        try:
            self.loaded_users = self.fileloader_service.load_users(file_path)
            self.processed_hashes = []
            self.export_path = None
            self.app_state.input_file_path = file_path
            self.app_state.users = self.loaded_users
            self.app_state.generated_hashes = []
            self.selected_file_label.configure(text=file_path)
            self.download_button.configure(state="disabled")
            messagebox.showinfo("UTM Generator", "Файл успешно загружен")
        except Exception as error:
            self.loaded_users = []
            self.selected_file_label.configure(text="Файл не выбран")
            self.download_button.configure(state="disabled")
            messagebox.showerror("UTM Generator", f"Ошибка загрузки файла:\n{error}")

    def generate_hashes(self):
        if not self.loaded_users:
            messagebox.showwarning("UTM Generator", "Сначала загрузите файл с пользователями")
            return

        secret_key = self.secret_key_entry.get().strip()
        if not secret_key:
            messagebox.showwarning("UTM Generator", "Введите секретный ключ")
            return

        try:
            self.app_state.utm_params["secret_key"] = secret_key
            self.processed_hashes = self.hash_generator_service.generate_hashes(
                self.loaded_users,
                secret_key
            )
            self.download_button.configure(state="normal")
            messagebox.showinfo("UTM Generator", "Хэши успешно сгенерированы")
        except Exception as error:
            self.download_button.configure(state="disabled")
            messagebox.showerror("UTM Generator", f"Ошибка генерации хэшей:\n{error}")

    def download_file(self):
        if not self.processed_hashes:
            messagebox.showwarning("UTM Generator", "Сначала сгенерируйте хэши")
            return

        input_path = Path(self.app_state.input_file_path)
        output_file_path = filedialog.asksaveasfilename(
            title="Сохранить готовый файл",
            defaultextension=input_path.suffix,
            initialfile=f"{input_path.stem}_with_hashes{input_path.suffix}",
            filetypes=[("Excel files", "*.xlsx"), ("CSV files", "*.csv")]
        )
        if not output_file_path:
            return

        try:
            self.export_path = self.hash_export_service.export_hashes_to_file(output_file_path)
            self.app_state.output_file_path = self.export_path
            messagebox.showinfo("UTM Generator", f"Файл сохранен:\n{self.export_path}")
        except Exception as error:
            messagebox.showerror("UTM Generator", f"Ошибка экспорта файла:\n{error}")
