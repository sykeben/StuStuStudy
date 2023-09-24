# Imports.
import stustustudy.app.common as common
from ..utils.ui import ezPromptStr
from ..menu import Menu, MenuItem, actions

# Define populator for set properties menu.
def propertiesMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)
    menu.findItem("T").description = f"\"{common.currentSet.title}\""
    menu.findItem("D").description = f"\"{common.currentSet.description}\""

# Define set title static action.
def setTitleStaticAction(item:MenuItem):
    common.currentSet.title = ezPromptStr("new title", common.currentSet.title)

# Define set description static action.
def setDescriptionStaticAction(item:MenuItem):
    common.currentSet.description = ezPromptStr("new description", common.currentSet.description)

# Define set properties menu.
propertiesMenu = Menu("Set Properties", populator=propertiesMenuPopulator)
propertiesMenu.createItem("X", "Exit", "Exits this menu.", actions.exitAction())
propertiesMenu.separate()
propertiesMenu.createItem("T", "Set Title", "", actions.staticAction(setTitleStaticAction))
propertiesMenu.createItem("D", "Set Description", "", actions.staticAction(setDescriptionStaticAction))
