# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..utils.ui import ezTitle, ezPromptStr

# Define globals.
termIndex = -1
termObject = None

# Define term edit static action.
def termTermStaticAction(item:MenuItem):
    global termObject
    ezTitle("Changing Term")
    termObject.term = ezPromptStr("new term", termObject.term, defaultAsCurrent=True)

# Define definition edit static action.
def termDefinitionStaticAction(item:MenuItem):
    global termObject
    ezTitle("Changing Term's Definition")
    termObject.definition = ezPromptStr("new definition", termObject.definition, defaultAsCurrent=True)

# Define populator for term edit menu.
def termEditMenuPopulator(menu:Menu, firstTime:bool):
    global termIndex, termObject
    common.currentSetPopulator(menu, firstTime)
    menu.title = f"Editing Term {termIndex + 1}"
    menu.findItem("T").description = f"\"{termObject.term}\""
    menu.findItem("D").description = f"\"{termObject.definition}\""

# Define term edit menu.
termEditMenu = Menu("Edit Term", populator=termEditMenuPopulator)
termEditMenu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
termEditMenu.separate()
termEditMenu.createItem("T", "Term", "", actions.staticAction(termTermStaticAction))
termEditMenu.createItem("D", "Definition", "", actions.staticAction(termDefinitionStaticAction))
termEditMenu.separate()
termEditMenu.createItem("R", "Remove Term", "Removes this term from the set.", actions.placeholderAction())
termEditMenu.createItem("M", "Move Term", "Moves this term up/down.", actions.placeholderAction())
termEditMenu.createItem("I", "Insert Term", "Inserts a term after this term.", actions.placeholderAction())

# Define menu static action.
def termEditMenuStaticAction(item:MenuItem):
    global termIndex, termObject

    # Update globals.
    termIndex = int(item.key) - 1
    termObject = common.currentSet.terms[termIndex]

    # Start menu.
    termEditMenu.auto()

    # Clear globals.
    termIndex = -1
    termObject = None
