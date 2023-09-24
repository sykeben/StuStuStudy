# Imports.
from rich.prompt import Prompt
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions

# Define add term action.
def addTermStaticAction(item:MenuItem):
    common.currentSet.createTerm(Prompt.ask("Term"), Prompt.ask("Definition"))

# Define term edit action.
def editTermStaticAction(item:MenuItem):

    # Get term.
    index = int(item.key) - 1
    term = common.currentSet.terms[index]

    # Define term edit static action.
    def termTermStaticAction(item:MenuItem):
        term.term = Prompt.ask("Enter new term (empty to cancel change)", default=term.term, show_default=False)

    # Define definition edit static action.
    def termDefinitionStaticAction(item:MenuItem):
        term.definition = Prompt.ask("Enter new definition (empty to cancel change)", default=term.definition, show_default=False)

    # Define populator for menu.
    def editingMenuPopulator(menu:Menu):
        common.currentSetPopulator(menu)
        menu.findItem("T").description = f"\"{term.term}\""
        menu.findItem("D").description = f"\"{term.definition}\""

    # Define editing menu.
    editingMenu = Menu("Edit Term", populator=editingMenuPopulator)
    editingMenu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
    editingMenu.separate()
    editingMenu.createItem("T", "Term", "", actions.staticAction(termTermStaticAction))
    editingMenu.createItem("D", "Definition", "", actions.staticAction(termDefinitionStaticAction))
    editingMenu.separate()
    editingMenu.createItem("R", "Remove Term", "Removes this term from the set.", actions.placeholderAction())
    editingMenu.createItem("M", "Move Term", "Moves this term up/down.", actions.placeholderAction())
    editingMenu.createItem("I", "Insert Term", "Inserts a term after this term.", actions.placeholderAction())

    # Activate editing menu.
    editingMenu.auto()

# Define populator for set terms menu.
def termsMenuPopulator(menu:Menu):
    common.currentSetPopulator(menu)
    menu.items.clear()
    menu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
    menu.separate()
    menu.items += [MenuItem(str(index+1), term.term, term.definition, actions.staticAction(editTermStaticAction)) for index, term in enumerate(common.currentSet.terms)]
    menu.separate()
    menu.createItem("A", "Add Term", "Adds a new term.", actions.staticAction(addTermStaticAction))
    menu.title = f"{len(common.currentSet.terms)} Terms"

# Define set terms menu.
termsMenu = Menu("Terms", populator=termsMenuPopulator)
