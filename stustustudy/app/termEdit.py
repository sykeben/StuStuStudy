# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..utils.ui import ezPromptStr

# Define globals.
termIndex = -1
termObject = None

# Define term edit static action.
def termTermStaticAction(item:MenuItem):
    global termObject
    termObject.term = ezPromptStr("new term", termObject.term)

# Define definition edit static action.
def termDefinitionStaticAction(item:MenuItem):
    global termObject
    termObject.definition = ezPromptStr("new definition", termObject.definition)

# Define populator for term edit menu.
def termEditMenuPopulator(menu:Menu, firstTime:bool):
    global termObject
    common.currentSetPopulator(menu, firstTime)
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
    termIndex = int(item.key) - 1
    termObject = common.currentSet.terms[termIndex]
    termEditMenu.auto()
