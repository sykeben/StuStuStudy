# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..set import Set, SetTerm
from ..utils import ezTitle, ezPromptStr, ezConfirm
from .properties import propertiesMenu
from .terms import termsMenu

# Initialize globals.
common.initCommon()

# TODO - Remove this after done.
# Load testing set.
common.currentSet = Set("Testing Set", "A test set for development.", [
    SetTerm("Term 1", "This is term #1."),
    SetTerm("Term 2", "This is term #2."),
    SetTerm("Term 3", "This is term #3."),
    SetTerm("Term 4", "This is term #4."),
    SetTerm("Term 5", "This is term #5.")
])

# Define main menu populator.
def mainMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)
    menu.setDisableds(["FS", "FSA", "FC", "EP", "ET", "SF", "SL", "SQ"], not(bool(common.currentSet)))

# Define new set static action.
def newSetStaticAction(item:MenuItem):
    ezTitle("Creating a New Set")
    if ezConfirm("create a new set"):
        common.currentSet = Set(
            title = ezPromptStr("title", "Untitled Set", True),
            description = ezPromptStr("description", "No Description", True)
        )
        common.currentFile = None

# Define main menu.
mainMenu = Menu("Main Menu", populator=mainMenuPopulator)
mainMenu.createItem("AQ", "Quit", "Quits StuStuStudy (unsaved work may be lost).", actions.exitAction(confirm=True))
mainMenu.separate()
mainMenu.createItem("FN", "New", "Creates a new set file.", actions.staticAction(newSetStaticAction))
mainMenu.createItem("FO", "Open", "Opens an existing set file.", actions.placeholderAction())
mainMenu.createItem("FS", "Save", "Saves the currently open set file.", actions.placeholderAction())
mainMenu.createItem("FSA", "Save As", "Saves the currently open set file under another name.", actions.placeholderAction())
mainMenu.createItem("FC", "Close", "Closes the currently open set file.", actions.placeholderAction())
mainMenu.separate()
mainMenu.createItem("EP", "Properties", "Opens the set's properties for editing.", actions.submenuAction(propertiesMenu))
mainMenu.createItem("ET", "Terms", "Opens the set's term list for editing.", actions.submenuAction(termsMenu))
mainMenu.separate()
mainMenu.createItem("SF", "Flashcards", "Starts flashcard mode.", actions.placeholderAction())
mainMenu.createItem("SL", "Learn", "Starts learn mode.", actions.placeholderAction())
mainMenu.createItem("SQ", "Quiz", "Starts quiz mode.", actions.placeholderAction())

# Main method.
def main():

    # Start main menu.
    mainMenu.auto()
