# Imports.
from ..menu import Menu

# Define global initialization routine.
def initCommon():
    global currentSet, currentFile, lastSaved
    currentSet = None
    currentFile = None
    lastSaved = None

# Define current set populator.
def currentSetPopulator(menu:Menu, firstTime:bool):
    global currentSet, currentFile, lastSaved
    title = currentSet.title if currentSet else "No Set"
    file = (currentFile if currentFile else "Not Saved") if currentSet else "No File"
    saved = f"Saved at {lastSaved}" if lastSaved else None
    menu.subtitle = f"{title} ({file}{(', '+saved) if saved else ''})"
