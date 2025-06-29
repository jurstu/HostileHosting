from nicegui import ui
import os
from pathlib import Path

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@ui.page("/")
def upload_page():
    ui.label("📁 Upload Your Files").classes("text-2xl font-bold mb-4")

    # Output area for upload info
    status = ui.label()

    def handle_upload(file):
        save_path = UPLOAD_DIR / file.name
        with open(save_path, "wb") as f:
            f.write(file.content.read())
        status.set_text(f"✅ Uploaded: {file.name}")

    ui.upload(
        label="Choose file(s)",
        multiple=True,
        on_upload=handle_upload,
    ).classes("mb-4")

    ui.button("Go to uploads folder", on_click=lambda: ui.open("file://" + str(UPLOAD_DIR.resolve())))

ui.run()
