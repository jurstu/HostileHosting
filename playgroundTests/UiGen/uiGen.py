from nicegui import ui, events, app
from fastapi import Response
import time
import threading
from UiGen.filesPage import FilesPage

from LoggingSetup import getLogger
logger = getLogger(__name__)


class UiGen:
    def __init__(self):
        self.spawnGui()




    def run(self):
        logger.info("setting up nicegui server")
        self.t = threading.Thread(target=self.host, daemon=True)
        self.t.start()

    def host(self):
        ui.run(reload=False, show=False)

    def spawnGui(self):
        self.controls = {}
        ui.dark_mode().enable()
        
        self.controls["linkList"] = ui.column()
        

    def updateLinkList(self):
        self.controls["linkList"].clear()
        for page in self.subpages:
            with self.controls["linkList"]:
                with ui.row().classes('items-center gap-4'):
                    ui.label(page.fpm.webPath).classes('text-blue-700 font-medium')
                    ui.label(page.fpm.localPath).classes('text-gray-600')
                    ui.link('Open', target=page.fpm.getWebRoute()).props('underline').classes('text-green-600')



    def generateFpms(self, fpms):
        self.subpages = []
        for fpm in fpms:
            self.subpages.append(FilesPage(fpm))
        self.updateLinkList()
            

if __name__ == "":
    from .uiGen import UiGen
    from nicegui import ui
    import time

    ug = UiGen()
    ui.run()
    while 1:
        time.sleep(1)