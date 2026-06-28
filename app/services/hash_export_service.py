from pathlib import Path

from openpyxl import load_workbook

from app.state import AppState


class HashExportService:
    def __init__(self, app_state: AppState):
        self.app_state = app_state

    def export_hashes_to_file(self, output_file_path: str) -> str:
        input_file_path = self.app_state.input_file_path
        hashes = self.app_state.generated_hashes

        if not input_file_path:
            raise ValueError("Путь к входному файлу не указан")

        if not hashes:
            raise ValueError("Список хэшей пустой")

        if not output_file_path:
            raise ValueError("Путь к выходному файлу не указан")

        input_path = Path(input_file_path)
        output_path = Path(output_file_path)

        if not input_path.exists():
            raise FileNotFoundError(f"Входной файл не найден: {input_path}")

        if input_path.suffix.lower() != ".xlsx":
            raise ValueError("Пока поддерживается только формат .xlsx")

        if output_path.suffix.lower() != ".xlsx":
            output_path = output_path.with_suffix(".xlsx")

        workbook = load_workbook(input_path)
        sheet = workbook.active

        header_row = 1
        first_data_row = 2

        users_count = sheet.max_row - 1

        if len(hashes) != users_count:
            raise ValueError(
                f"Количество хэшей не соответствует количеству пользователей в файле. "
                f"Строк пользователей: {users_count}, хэшей: {len(hashes)}"
            )

        hash_column_index = sheet.max_column + 1

        sheet.cell(
            row=header_row,
            column=hash_column_index,
            value="user_hash"
        )

        for index, user_hash in enumerate(hashes):
            row_number = first_data_row + index

            sheet.cell(
                row=row_number,
                column=hash_column_index,
                value=user_hash
            )

        hash_column_letter = sheet.cell(
            row=header_row,
            column=hash_column_index
        ).column_letter

        sheet.column_dimensions[hash_column_letter].width = 80

        workbook.save(output_path)

        return str(output_path)