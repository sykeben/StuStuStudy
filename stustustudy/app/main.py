# Imports.
import stustustudy.app.common as common
from pathlib import Path
from ..console import console
from ..menu import Menu, MenuItem, actions
from ..set import Set
from ..utils import ezTitle, ezPromptStr, ezConfirm, ezUpdate, ezFinish
from .properties import propertiesMenu
from .terms import termsMenu
from .cards import cardsMenu

# Initialize globals.
common.initCommon()

# TODO: Remove this after done testing.
from ..set import SetTerm
common.currentSet = Set("Demo Set", "This is a demo set for testing. If this is loaded by default, something went wrong.", [
    SetTerm("Term #1", "This is term 1.", False),
    SetTerm("Term #2", "This is term 2.", False),
    SetTerm("Term #3", "This is term 3.", False),
    SetTerm("Term #4", "This is term 4.", False),
    SetTerm("Term #5", "This is term 5.", False),
    SetTerm("Term #6", "This is term 6.", False),
    SetTerm("Term #7", "This is term 7.", False),
    SetTerm("Term #8", "This is term 8.", False),
    SetTerm("Term #9", "This is term 9.", False)
])
common.currentFile = Path("D:/bsyke/Documents/GitHub/StuStuStudy/demo.study")
common.modified = False

# Define quit static action.
def quitExitingStaticAction(item:MenuItem):
    ezTitle("[b][red]<[/red][/b] Quitting StuStuStudy")
    if ezConfirm("quit"):
        if not(common.modified) or ezConfirm("discard your unsaved work"):
            return True
    return False

# Define new set static action.
def newSetStaticAction(item:MenuItem):
    ezTitle("[b][yellow]•[/yellow][/b] Creating a New Set")
    if ezConfirm("create a new set"):
        if not(common.modified) or ezConfirm("discard your unsaved work"):
            common.currentSet = Set(
                title = ezPromptStr("title", "Untitled Set", True),
                description = ezPromptStr("description", "No Description", True)
            )
            common.currentFile = None
            common.modified = True

# Define file error handler.
def handleFileError(action:str, reason:str, isReading:bool = True, isSavingAs:bool = False, fallbackFile:Path|None = None):
    if isReading:
        common.currentSet = None
        common.currentFile = fallbackFile
        common.modified = False
    if not(isReading) and isSavingAs:
        common.currentFile = fallbackFile
    ezFinish(False, f"Could not {action}, {reason}")

# Define open set static action.
def openSetStaticAction(item:MenuItem):

    # Initialize and confirm action.
    ezTitle("[b][yellow]~[/yellow][/b] Opening Set")
    if ezConfirm("open a different set"):
        if not(common.modified) or ezConfirm("discard your unsaved work"):

            # Attempt to get file path.
            filePath = Path(ezPromptStr("full file path (*.study)", blankAllowed=False))
            if (filePath.is_file()):
                if (filePath.suffix == ".study"):

                    # Attempt to open file.
                    ezUpdate("Opening file for reading...")
                    try:
                        filePointer = filePath.open("r")
                    except OSError:
                        handleFileError("open file", "system refused")
                        return
                    except:
                        handleFileError("open file", "unknown error")
                        return
                    common.currentFile = filePath
                    
                    # Attempt to load set.
                    ezUpdate("Reading set from file...")
                    try:
                        common.currentSet = Set.fromJSON(filePointer)
                    except:
                        handleFileError("read set", "JSON error")
                        filePointer.close()
                        return
                    
                    # Finish up.
                    ezUpdate("Finishing up...")
                    filePointer.close()
                    common.modified = False

                    # Display completion.
                    ezFinish(True)
                    
                else: handleFileError("open file", "wrong type")
            else: handleFileError("find file", "does not exist or is invalid")

# Define set writer.
def writeSet(isSavingAs:bool = False, fallbackFile:Path|None = None):

    # Attempt to open file.
    filePath = common.currentFile
    ezUpdate("Opening file for writing...")
    try:
        filePointer = filePath.open("w")
    except OSError:
        handleFileError("open file", "system refused", isReading=False, isSavingAs=isSavingAs, fallbackFile=fallbackFile)
        return
    except:
        handleFileError("open file", "unknown error", isReading=False, isSavingAs=isSavingAs, fallbackFile=fallbackFile)
        return
    
    # Attempt to write set.
    ezUpdate("Writing set to file...")
    try:
        common.currentSet.toJSON(filePointer)
    except:
        handleFileError("write set", "JSON error", isReading=False, isSavingAs=isSavingAs, fallbackFile=fallbackFile)
        filePointer.close()
        return
    
    # Finish up.
    ezUpdate("Finishing up...")
    filePointer.close()
    common.modified = False

    # Display completion.
    ezFinish(True)

# Define save set static action.
def saveSetStaticAction(item:MenuItem):
    ezTitle("[b][yellow]†[/yellow][/b] Saving Set")
    writeSet()

# Define save set as static action.
def saveSetAsStaticAction(item:MenuItem):

    # Initialize and confirm action.
    ezTitle("[b][yellow]‡[/yellow][/b] Saving Set As")
    if ezConfirm("save this set as a new file"):

        # Attempt to get file path.
        filePath = Path(ezPromptStr("full file path (*.study)", blankAllowed=False))
        if not(filePath.is_file()):
            if (filePath.suffix == ".study"):

                # Write.
                fallbackPath = Path(common.currentFile) if common.currentFile else None
                common.currentFile = filePath
                writeSet(isSavingAs=True, fallbackFile=fallbackPath)

            else: handleFileError("save file", "wrong type")
        else: handleFileError("overwrite file", "already exists or is invalid")

# Define close set static action.
def closeSetStaticAction(item:MenuItem):
    ezTitle("[b][yellow]<[/yellow][/b] Closing this Set")
    if ezConfirm("close this set"):
        if not(common.modified) or ezConfirm("discard your unsaved work"):
            common.currentSet = None
            common.currentFile = None
            common.modified = False

# Define main menu populator.
def mainMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)
    menu.setDisableds(["FSA", "FC", "EP", "ET", "SF", "SL", "SQ"], not(common.currentSet))
    menu.setDisabled("FS", not(common.currentSet) or not(common.currentFile))

# Define main menu.
mainMenu = Menu("[b][green]>[/green][/b] Main Menu", populator=mainMenuPopulator)
mainMenu.createItem("AQ", "[red]<[/red] Quit", "Quits StuStuStudy (unsaved work may be lost).", actions.exitingStaticAction(quitExitingStaticAction))
mainMenu.separate()
mainMenu.createItem("FN", "[yellow]•[/yellow] New", "Creates a new set file.", actions.staticAction(newSetStaticAction))
mainMenu.createItem("FO", "[yellow]~[/yellow] Open", "Opens an existing set file.", actions.staticAction(openSetStaticAction))
mainMenu.createItem("FS", "[yellow]†[/yellow] Save", "Saves the currently open set file.", actions.staticAction(saveSetStaticAction))
mainMenu.createItem("FSA", "[yellow]‡[/yellow] Save As", "Saves the currently open set file under another name.", actions.staticAction(saveSetAsStaticAction))
mainMenu.createItem("FC", "[yellow]<[/yellow] Close", "Closes the currently open set file.", actions.staticAction(closeSetStaticAction))
mainMenu.separate()
mainMenu.createItem("EP", "[white]ƒ[/white] Properties", "Opens the set's properties for editing.", actions.submenuAction(propertiesMenu))
mainMenu.createItem("ET", "[white]§[/white] Terms", "Opens the set's term list for editing.", actions.submenuAction(termsMenu))
mainMenu.separate()
mainMenu.createItem("SF", "[green]¶[/green] Flashcards", "Starts flashcard mode.", actions.submenuAction(cardsMenu))
mainMenu.createItem("SL", "[green]>[/green] Learn", "Starts learn mode.", actions.placeholderAction())
mainMenu.createItem("SQ", "[green]Ø[/green] Quiz", "Starts quiz mode.", actions.placeholderAction())

# Main method.
def main():

    # Start main menu.
    mainMenu.auto()
