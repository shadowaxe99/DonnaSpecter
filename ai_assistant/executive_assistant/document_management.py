```python
import os
from PyPDF2 import PdfFileReader, PdfFileWriter

class DocumentManager:
    def __init__(self, user_profile, app_settings):
        self.user_profile = user_profile
        self.app_settings = app_settings

    def read_pdf(self, file_path):
        try:
            with open(file_path, "rb") as file:
                reader = PdfFileReader(file)
                content = reader.getPage(0).extractText()
                return content
        except FileNotFoundError:
            print(f"No file found at {file_path}")
            return None

    def write_pdf(self, file_path, content):
        writer = PdfFileWriter()
        page = writer.addPage()
        page.addText(content)
        with open(file_path, "wb") as file:
            writer.write(file)

    def list_documents(self, directory):
        try:
            files = os.listdir(directory)
            pdf_files = [file for file in files if file.endswith(".pdf")]
            return pdf_files
        except FileNotFoundError:
            print(f"No directory found at {directory}")
            return None

    def update_user_profile(self, new_data):
        self.user_profile.update(new_data)
        print("User profile updated successfully.")

    def update_app_settings(self, new_settings):
        self.app_settings.update(new_settings)
        print("App settings updated successfully.")
```