from nicegui import ui, app
import os
import tkinter as tk
from tkinter import filedialog
import threading

shared_folders = {}

def add_shared_folder(name: str, folder_path: str):
    route = f'/{name.strip("/")}'
    absolute_path = os.path.abspath(os.path.expanduser(folder_path))

    if not os.path.isdir(absolute_path):
        ui.notify(f"Folder doesn't exist: {absolute_path}", type='negative')
        return

    if route in shared_folders:
        ui.notify('This route already exists!', type='warning')
        return

    shared_folders[route] = absolute_path
    app.add_static_files(route, absolute_path)
    ui.notify(f"Shared {absolute_path} at {route}", type='positive')
    update_shared_table()

def update_shared_table():
    shared_table.clear()
    for route, path in shared_folders.items():
        with shared_table:
            with ui.row().classes('items-center gap-4'):
                ui.label(route).classes('text-blue-700 font-medium')
                ui.label(path).classes('text-gray-600')
                ui.link('Open', target=route).props('underline').classes('text-green-600')

def open_folder_picker():
    # Run tkinter folder dialog in a separate thread
    def choose_folder():
        root = tk.Tk()
        root.withdraw()
        folder_path = filedialog.askdirectory()
        root.destroy()
        if folder_path:
            path_input.value = folder_path
    threading.Thread(target=choose_folder).start()

### === UI Layout ===

ui.label('📁 Folder Sharing Panel').classes('text-2xl mt-4 mb-4')

with ui.row().classes('mb-4'):
    name_input = ui.input(label='Route Name (e.g., videos)')
    path_input = ui.input(label='Folder Path')
    ui.button('Select Folder...', on_click=open_folder_picker)

ui.button('Add Folder', on_click=lambda: add_shared_folder(name_input.value, path_input.value)).classes('mt-2')

ui.label('🔗 Shared Routes').classes('text-lg mt-2 mb-2')
shared_table = ui.column()

ui.run(port=8080)
