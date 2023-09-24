# Imports.
from rich.prompt import Prompt
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions

# Define populator for set properties menu.
def propertiesMenuPopulator(menu:Menu):
    common.currentSetPopulator(menu)
    menu.findItem("T").description = f"\"{common.currentSet.title}\""
    menu.findItem("D").description = f"\"{common.currentSet.description}\""

# Define set title static action.
def setTitleStaticAction(item:MenuItem):
    common.currentSet.title = Prompt.ask("Enter new set title (empty to cancel change)", default=common.currentSet.title, show_default=False)

# Define set description static action.
def setDescriptionStaticAction(item:MenuItem):
    common.currentSet.description = Prompt.ask("Enter new set description (empty to cancel change)", default=common.currentSet.description, show_default=False)

# Define set properties menu.
propertiesMenu = Menu("Set Properties", populator=propertiesMenuPopulator)
propertiesMenu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
propertiesMenu.separate()
propertiesMenu.createItem("T", "Set Title", "", actions.staticAction(setTitleStaticAction))
propertiesMenu.createItem("D", "Set Description", "", actions.staticAction(setDescriptionStaticAction))
