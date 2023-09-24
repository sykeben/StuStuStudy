# Imports.
from rich.prompt import Confirm, Prompt
import stustustudy.app.common as common
from .properties import propertiesMenu
from ..menu import Menu, MenuItem, actions
from ..set import Set

# Initialize globals.
common.initCommon()

# Define new set static action.
def newSetStaticAction(item:MenuItem):
    if Confirm.ask("Are you sure you want to create a new set?"):
        common.currentSet = Set(
            title=Prompt.ask("Give this set a title", default="Untitled Set"),
            description=Prompt.ask("Give this set a description", default="")
        )
        common.currentFile = None

# Define main menu.
mainMenu = Menu("Main Menu", populator=common.currentSetPopulator)
mainMenu.createItem("AQ", "Quit", "Quits StuStuStudy (unsaved work may be lost).", actions.exitAction(confirm=True))
mainMenu.separate()
mainMenu.createItem("FN", "New", "Creates a new set file.", actions.staticAction(newSetStaticAction))
mainMenu.createItem("FO", "Open", "Opens an existing set file.", actions.placeholderAction())
mainMenu.createItem("FS", "Save", "Saves the currently open set file.", actions.placeholderAction())
mainMenu.createItem("FSA", "Save As", "Saves the currently open set file under another name.", actions.placeholderAction())
mainMenu.createItem("FC", "Close", "Closes the currently open set file.", actions.placeholderAction())
mainMenu.separate()
mainMenu.createItem("EP", "Properties", "Opens the set's properties for editing.", actions.submenuAction(propertiesMenu))
mainMenu.createItem("ET", "Terms", "Opens the set's term list for editing.", actions.placeholderAction())
mainMenu.separate()
mainMenu.createItem("SF", "Flashcards", "Starts flashcard mode.", actions.placeholderAction())
mainMenu.createItem("SL", "Learn", "Starts learn mode.", actions.placeholderAction())
mainMenu.createItem("SQ", "Quiz", "Starts quiz mode.", actions.placeholderAction())

# Main method.
def main():

    # Start main menu.
    mainMenu.auto()
