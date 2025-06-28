from nicegui import ui
from hashlib import sha256

def getHash(text:str):
    return sha256(text.encode('utf-8')).hexdigest()

def updateUrl():
    global index
    index += 1
    ss = getHash(f"{index}")
    ui.navigate.history.replace(f"/{ss}")

index = 0
ui.timer(0.03, updateUrl)
ui.run()