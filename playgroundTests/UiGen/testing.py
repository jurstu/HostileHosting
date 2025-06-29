from nicegui import ui
from urllib.parse import unquote

@ui.page('/browse/{full_path:path}')
def browse(full_path: str):
    path = unquote(full_path)  # in case there are URL-encoded characters
    ui.label(f'Browsing: {path}')
    # Dynamically generate the UI for this path

ui.run()