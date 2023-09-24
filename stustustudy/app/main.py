# Imports.
from ..menu import Menu, actions
from ..set import Set

# Initialize globals.
currentSet:Set = None
currentFile:str = None

# Main method.
def main():

    # Define current set populator.
    def populateCurrentSet(menu:Menu):
        title = currentSet.title if currentSet else "No Set"
        file = currentFile if currentFile else "No File"
        menu.subtitle = f"{title} ({file})"

    # Define main menu.
    mainMenu = Menu("Main Menu", populator=populateCurrentSet)
    mainMenu.createItem("AQ", "Quit", "Quits StuStuStudy (unsaved work may be lost).", actions.exitAction(confirm=True))
    mainMenu.separate()
    mainMenu.createItem("FN", "New", "Creates a new set file.", actions.placeholderAction())
    mainMenu.createItem("FO", "Open", "Opens an existing set file.", actions.placeholderAction())
    mainMenu.createItem("FS", "Save", "Saves the currently open set file.", actions.placeholderAction())
    mainMenu.createItem("FSA", "Save As", "Saves the currently open set file under another name.", actions.placeholderAction())
    mainMenu.createItem("FC", "Close", "Closes the currently open set file.", actions.placeholderAction())
    mainMenu.separate()
    mainMenu.createItem("EP", "Properties", "Opens the set's properties for editing.", actions.placeholderAction())
    mainMenu.createItem("ET", "Terms", "Opens the set's term list for editing.", actions.placeholderAction())
    mainMenu.separate()
    mainMenu.createItem("SF", "Flashcards", "Starts flashcard mode.", actions.placeholderAction())
    mainMenu.createItem("SL", "Learn", "Starts learn mode.", actions.placeholderAction())
    mainMenu.createItem("SQ", "Quiz", "Starts quiz mode.", actions.placeholderAction())

    # Start.
    mainMenu.auto()
