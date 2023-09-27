# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..utils.ui import ezTitle, ezPromptStr, ezConfirm
from .termMove import termMoveMenuActivate

# Define globals.
termIndex = -1
termObject = None

# Define term edit static action.
def termTermStaticAction(item:MenuItem):
    global termObject
    ezTitle("[b][white]¶[/white][/b] Changing a Term")
    newTerm = ezPromptStr("new term", termObject.term, defaultAsCurrent=True)
    if (newTerm != termObject.term):
        termObject.term = newTerm
        common.modified = True

# Define definition edit static action.
def termDefinitionStaticAction(item:MenuItem):
    global termObject
    ezTitle("[b][white]§[/white][/b] Changing a Term's Definition")
    newDefinition = ezPromptStr("new definition", termObject.definition, defaultAsCurrent=True)
    if (newDefinition != termObject.term):
        termObject.definition = newDefinition
        common.modified = True

# Define term star unstar static action.
def termStarUnstarStaticAction(item:MenuItem):
    global termObject
    termObject.starred = not(termObject.starred)
    common.modified = True

# Define term remove exiting static action.
def termRemoveExitingStaticAction(item:MenuItem):
    global termIndex
    ezTitle("[b][yellow]×[/yellow][/b] Removing a Term")
    if (ezConfirm("remove this term")):
        common.currentSet.removeTerm(termIndex)
        common.modified = True
        return True
    else:
        return False

# Define term move menu exiting static action.
def termMoveMenuExitingStaticAction(item:MenuItem):
    return termMoveMenuActivate(termIndex, termObject)

# Define add term action.
def insertTermStaticAction(item:MenuItem):
    global termIndex
    ezTitle("[b][yellow]•[/yellow][/b] Inserting a New Term")
    common.currentSet.createTerm(
        ezPromptStr("term", ""),
        ezPromptStr("definition", ""),
        termIndex
    )
    common.modified = True

# Define populator for term edit menu.
def termEditMenuPopulator(menu:Menu, firstTime:bool):
    global termIndex, termObject
    common.currentSetPopulator(menu, firstTime)
    menu.findItem("T").description = f"\"{termObject.term}\""
    menu.findItem("D").description = f"\"{termObject.definition}\""
    menu.findItem("S").description = f"Term is currently {'[b][u][yellow]STARRED[/yellow][/u][/b]' if termObject.starred else 'unstarred'}."

# Define term edit menu.
termEditMenu = Menu("[b][white]»[/white][/b] Editing a Term", populator=termEditMenuPopulator)
termEditMenu.createItem("X", "[red]<[/red] Exit", "Exits this menu.", actions.exitAction())
termEditMenu.separate()
termEditMenu.createItem("T", "[white]¶[/white] Term", "", actions.staticAction(termTermStaticAction))
termEditMenu.createItem("D", "[white]§[/white] Definition", "", actions.staticAction(termDefinitionStaticAction))
termEditMenu.createItem("S", "[white]@[/white] Star/Unstar", "", actions.staticAction(termStarUnstarStaticAction))
termEditMenu.separate()
termEditMenu.createItem("R", "[yellow]×[/yellow] Remove Term", "Removes this term from the set.", actions.exitingStaticAction(termRemoveExitingStaticAction))
termEditMenu.createItem("M", "[yellow]![/yellow] Move Term", "Moves this term up/down.", actions.exitingStaticAction(termMoveMenuExitingStaticAction))
termEditMenu.createItem("I", "[yellow]•[/yellow] Insert Term", "Inserts a new term before this term.", actions.staticAction(insertTermStaticAction, exitAfter=True))

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
