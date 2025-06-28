




from hashlib import sha256

def getHash(text:str):
    return sha256(text.encode('utf-8')).hexdigest()

class FilesPageModel:
    def __init__(self, localPath:str, webPath:str):
        self.localPath = localPath
        self.webPath = webPath
        self.webPathHash = getHash(webPath)

    def getWebRoute(self):
        return f"/{self.webPathHash}"




