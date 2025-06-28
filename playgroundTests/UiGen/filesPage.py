from nicegui import ui, app
import numpy as np
from fastapi import Response
import cv2
import time
from DataModels import FilesPageModel
from PathUtils import get_last_element


from LoggingSetup import getLogger
logger = getLogger(__name__)


class FilesPage:
    def __init__(self, fpm:FilesPageModel):
        self.fpm = fpm
        self.controls = {}

        
        ui.page(f'{self.fpm.webPath}')(self.spawnGui)
        logger.info(f"created {self.fpm.webPath} route")

    def spawnGui(self):
        with ui.row():
            self.controls["pathLabel"] = ui.label(text=get_last_element(self.fpm.localPath))
        
        


        