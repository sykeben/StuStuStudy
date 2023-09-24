# Imports.
from rich.prompt import Prompt
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions

# Define populator for set terms menu.
def termsMenuPopulator(menu:Menu):
    common.currentSetPopulator(menu)
    menu.title = f"{len(common.currentSet.terms)} Terms"

# Define set terms menu.
termsMenu = Menu("Terms", populator=termsMenuPopulator)
termsMenu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
termsMenu.separate()
# Terms would go here (each term would have editor: term, description, action:delete, action:move, etc...)
termsMenu.separate()
termsMenu.createItem("A", "Add Term", "Adds a new term.", actions.placeholderAction())
