from nicegui import ui, app
import os
from DataModels import FilesPageModel
from PathUtils import get_last_element,  list_directories_in_directory, list_files_in_directory, get_emoji_for_file


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

    def spawnGui(self, full_path):
        ui.dark_mode().enable()
        with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
            self.controls["pathLabel"] = ui.label(text=get_last_element(self.fpm.localPath))
            ui.label('Hostile Hosting')


        filesPath = os.path.join(self.fpm.localPath, full_path) # f"{self.fpm.localPath}/{full_path}"
        webPath = f"{self.fpm.getWebRoute()}/{full_path}"

        with ui.column():
            files = list_files_in_directory(filesPath)
            dirs = list_directories_in_directory(filesPath)
            
            for di in dirs:
                with ui.row():
                    routePath = webPath + di + "/"
                    


                    em = get_emoji_for_file(di, dir=True)
                    ui.label(f"{em} {di}")
                    ui.link(f"{em} {di}", routePath)
                    
            with ui.column():
                for fi in files:
                    with ui.row():
                        
                        em = get_emoji_for_file(fi.lower())
                        
                        ui.label(f"{em} {fi}")

                        fullPath = os.path.join(filesPath, fi)
                        logger.info(fullPath)
                        button = ui.button('download file', on_click=lambda e: self.downloadFile(e.sender))
                        button.path = fullPath
                        




        


        