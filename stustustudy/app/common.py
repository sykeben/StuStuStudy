# Imports.
from ..menu import Menu

# Define global initialization routine.
def initCommon():

    # Initialize global variables.
    global currentSet, currentFile
    currentSet = None
    currentFile = None

# Define current set populator.
def currentSetPopulator(menu:Menu):
    global currentSet, currentFile
    title = currentSet.title if currentSet else "No Set"
    file = (currentFile if currentFile else "Not Saved") if currentSet else "No File"
    menu.subtitle = f"{title} ({file})"
