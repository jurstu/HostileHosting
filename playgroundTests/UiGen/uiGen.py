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
        dark = ui.dark_mode()
        dark.enable()

    def generateFpms(self, fpms):
        self.subpages = []
        for fpm in fpms:
            self.subpages.append(FilesPage(fpm))
            

if __name__ == "":
    from .uiGen import UiGen
    from nicegui import ui
    import time

    ug = UiGen()
    ui.run()
    while 1:
        time.sleep(1)