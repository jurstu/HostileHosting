import json
from LoggingSetup import getLogger
from DataModels import FilesPageModel
from UiGen import UiGen

from LoggingSetup import getLogger
logger = getLogger(__name__)



class HostileHosting:
    def __init__(self, configPath="config.json"):
        self.configPath = configPath
        self.loadConfig()
        self.generateFpms()
        self.ug = UiGen()
        self.ug.generateFpms(self.pages)
        self.ug.run()

    def loadConfig(self):
        try:
            with open(self.configPath, "r") as f:
                self.config = json.load(f)
        except Exception as e:
            logger.error(f"couldn't load the config: {e}")


    def generateFpms(self):
        pages = self.config["fpms"]
        self.pages = []
        for i, page in enumerate(pages):
            try:
                self.pages.append(
                    FilesPageModel(page["localPath"], page["webPath"])
                )
            except Exception as e:
                logger.error(f"Couldn't load page from config at index {i}: {e}")
                



