# Imports.
from pathlib import Path
from ..menu import Menu

# Define global initialization routine.
def initCommon():
    global currentSet, currentFile, modified
    currentSet = None
    currentFile = None
    modified = False

# Define current set populator.
def currentSetPopulator(menu:Menu, firstTime:bool):
    global currentSet, currentFile, modified
    title = currentSet.title if currentSet else "No Set"
    file = (currentFile.name if currentFile else "Unsaved") if currentSet else "No File"
    menu.subtitle = f"{title} ({file}{'*' if modified else ''})"
