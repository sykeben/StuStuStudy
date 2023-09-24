# Imports.
from rich.prompt import Prompt
import stustustudy.app.common as common
from ..menu import Menu, MenuItem, actions

# Define populator for set properties menu.
def propertiesMenuPopulator(menu:Menu):
    common.currentSetPopulator(menu)
    menu.findItem("ST").description = f"\"{common.currentSet.title}\""
    menu.findItem("SD").description = f"\"{common.currentSet.description}\""

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
propertiesMenu.createItem("ST", "Set Title", "", actions.staticAction(setTitleStaticAction))
propertiesMenu.createItem("SD", "Set Description", "", actions.staticAction(setDescriptionStaticAction))
