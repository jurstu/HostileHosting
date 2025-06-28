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
        
        self.subPages = {}

        if(self.isRoot):
            logger.info(f"created {self.fpm.getWebRoute()} route")
            ui.page(f'{self.fpm.getWebRoute()}')(self.spawnGui)()
        else:
            logger.info(f"CREATING SUBPAGE {self.fpm.webPath} route")
            ui.page(f'{self.fpm.webPath}')(self.spawnGui)()
        
        for s in self.stuffToInit:
            self.subPages[s.di] = FilesPage(s, False)

        #logger.info(f"{self.fpm.webPathHash} ")
        

    def spawnGui(self):
        ui.dark_mode().enable()
        #with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
        #    self.controls["pathLabel"] = ui.label(text=get_last_element(self.fpm.localPath))
        #    ui.label('HEADER')

        self.stuffToInit = []

        with ui.column():
            files = list_files_in_directory(self.fpm.localPath)
            dirs = list_directories_in_directory(self.fpm.localPath)
            
            for di in dirs:
                with ui.row():
                    localPath = os.path.join(self.fpm.localPath, di)
                    if(self.isRoot):
                        routePath = self.fpm.getWebRoute() + "/" + di
                    else:
                        routePath = f"{self.fpm.webPath}/{di}"


                    fpm = FilesPageModel(localPath, routePath)
                    fpm.di = di
                    self.stuffToInit.append(fpm)


                    em = get_emoji_for_file(di)
                    ui.label(f"{em} {di}")
                    ui.link(f"{em} {di}", routePath)
                    
            for fi in files:
                with ui.row():
                    em = get_emoji_for_file(fi.lower())
                    ui.label(f"{em} {fi}")
                


        


        