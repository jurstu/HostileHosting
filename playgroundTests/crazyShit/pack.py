from nicegui import native, ui

ui.label('Hello from PyInstaller')

ui.run(reload=False, port=native.find_open_port())
