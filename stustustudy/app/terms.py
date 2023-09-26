# Imports.
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions
from ..utils.ui import ezTitle, ezPromptStr
from .termEdit import termEditMenuStaticAction

# Define add term action.
def addTermStaticAction(item:MenuItem):
    ezTitle("Creating a New Term")
    common.currentSet.createTerm(
        ezPromptStr("term"),
        ezPromptStr("definition")
    )

# Define populator for set terms menu.
def termsMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)

    # Clear items.
    menu.items.clear()

    # Add header.
    menu.title = f"{len(common.currentSet.terms)} Terms"
    menu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
    menu.separate()

    # Generate items.
    menu.items += [MenuItem(
        str(index+1),
        term.term,
        term.definition,
        actions.staticAction(termEditMenuStaticAction)
    ) for index, term in enumerate(common.currentSet.terms)]
    menu.separate()

    # Add footer.
    menu.createItem("A", "Add Term", "Adds a new term.", actions.staticAction(addTermStaticAction))

# Define set terms menu.
termsMenu = Menu("Terms", populator=termsMenuPopulator)
