# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..set import SetTerm
from ..utils.ui import ezTitle, ezPromptStr

# Define globals.
termIndex = -1
termObject = None

# Define move action.
def termMoveStaticAction(item:MenuItem):
    global termIndex

    # Move accordingly.
    if item.key != "E":
        common.currentSet.moveTerm(termIndex, int(item.key) - 1)
    else:
        common.currentSet.moveTerm(termIndex, None)

# Define populator for set terms menu.
def termMoveMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)

    # Clear items.
    menu.items.clear()

    # Add header.
    menu.title = f"Select Term to Move Before"
    menu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
    menu.separate()

    # Generate items.
    menu.items += [MenuItem(
        str(index+1),
        term.term,
        term.definition,
        actions.staticAction(termMoveStaticAction, exitAfter=True)
    ) for index, term in enumerate(common.currentSet.terms)]
    menu.separate()

    # Add end item.
    menu.createItem("E", "End", "Move to end of list.", actions.staticAction(termMoveStaticAction, exitAfter=True))

# Define term move menu.
termMoveMenu = Menu("Terms", populator=termMoveMenuPopulator)

# Define menu static action.
def termMoveMenuActivate(newIndex:int, newObject:SetTerm):
    global termIndex, termObject

    # Copy values.
    termIndex = newIndex
    termObject = newObject

    # Start menu.
    termMoveMenu.auto()

    # Clear globals.
    termIndex = -1
    termObject = None
