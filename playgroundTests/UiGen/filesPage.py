from nicegui import ui, app
import os
from DataModels import FilesPageModel
from PathUtils import get_last_element,  list_directories_in_directory, list_files_in_directory, get_emoji_for_file, get_weight_in_human_readable

from LoggingSetup import getLogger
logger = getLogger(__name__)

class FilesPage:
    def __init__(self, fpm:FilesPageModel, isRoot:bool=True):
        self.fpm = fpm
        self.isRoot = isRoot
        self.controls = {}

        route = f'{self.fpm.getWebRoute()}/'
        ui.page(route + '{full_path:path}')(self.spawnGui)
        

    def downloadFile(self, sender):
        ui.download.file(sender.path)



    def handleUpload(self, file):
        pass

    def spawnGui(self, full_path):
        ui.dark_mode().enable()
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            self.controls["pathLabel"] = ui.label(text=get_last_element(self.fpm.localPath))
            ui.label('Hostile Hosting')


        filesPath = os.path.join(self.fpm.localPath, full_path) # f"{self.fpm.localPath}/{full_path}"
        webPath = f"{self.fpm.getWebRoute()}/{full_path}"
        with ui.row().classes('w-full'):
            with ui.column():
                with ui.grid(columns=3):
                    files = list_files_in_directory(filesPath)
                    dirs = list_directories_in_directory(filesPath)
                    
                    for i, (obj) in enumerate([*dirs, *files]):
                            if(i < len(dirs)):
                                em = get_emoji_for_file(obj, dir=True)
                                ui.label(f"{em} {obj}")
                                routePath = webPath + obj + "/"
                                ui.label("")
                                ui.link(f"{em} {obj}", routePath)
                            else:
                                em = get_emoji_for_file(obj.lower())
                                ui.label(f"{em} {obj}")
                                fullPath = os.path.join(filesPath, obj)
                                ui.label(f"{get_weight_in_human_readable(fullPath)}")
                                button = ui.button('download file', on_click=lambda e: self.downloadFile(e.sender))
                                button.path = fullPath
            ui.space()
            with ui.column():

                def handle_upload(file):
                    save_path = os.path.join(filesPath, file.name)
                    with open(save_path, "wb") as f:
                        f.write(file.content.read())

                ui.upload(
                    label="Choose file(s)",
                    multiple=True,
                    on_upload=handle_upload,
                    auto_upload=True
                ).classes("")