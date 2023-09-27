# Imports.
import stustustudy.app.common as common
from ..utils.ui import ezTitle, ezPromptStr
from ..menu import Menu, MenuItem, actions

# Define populator for set properties menu.
def propertiesMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)
    menu.findItem("T").description = f"\"{common.currentSet.title}\""
    menu.findItem("D").description = f"\"{common.currentSet.description}\""

# Define set title static action.
def setTitleStaticAction(item:MenuItem):
    ezTitle("[b][white]¶[/white][/b] Changing Set Title")
    newTitle = ezPromptStr("new title", common.currentSet.title, defaultAsCurrent=True)
    if (newTitle != common.currentSet.title):
        common.currentSet.title = newTitle
        common.modified = True

# Define set description static action.
def setDescriptionStaticAction(item:MenuItem):
    ezTitle("[b][white]§[/white][/b] Changing Set Description")
    newDescription = ezPromptStr("new description", common.currentSet.description, defaultAsCurrent=True)
    if (newDescription != common.currentSet.description):
        common.currentSet.description = newDescription
        common.modified = True

# Define set properties menu.
propertiesMenu = Menu("[b][white]ƒ[/white][/b] Set Properties", populator=propertiesMenuPopulator)
propertiesMenu.createItem("X", "[red]<[/red] Exit", "Exits this menu.", actions.exitAction())
propertiesMenu.separate()
propertiesMenu.createItem("T", "[white]¶[/white] Set Title", "", actions.staticAction(setTitleStaticAction))
propertiesMenu.createItem("D", "[white]§[/white] Set Description", "", actions.staticAction(setDescriptionStaticAction))
