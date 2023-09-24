# Imports.
from __future__ import annotations
from rich.table import Table
from rich.prompt import Prompt
from rich import box
from typing import Callable
from ..console import console
from .menuitem import MenuItem
from .menuseparator import MenuSeparator
from .menutransport import MenuTransport

# Menu class.
class Menu:

    # Initializor.
    def __init__(
            self,
            title:str|None = None,
            subtitle:str|None = None,
            promptText:str = "Choose",
            items:list[MenuItem|MenuSeparator]|None = None,
            caseSensitive:bool = False,
            populator:Callable[[Menu],None]|None = None
        ):

        # Set parameters.
        self.title = title
        self.subtitle = subtitle
        self.promptText = promptText
        self.items = items if items else list()
        self.caseSensitive = caseSensitive
        self.populator = populator

    # (Internal) Filter Items Only: Filters out any non-MenuItem items.
    def __filteredItemsOnly(self):
        return [item for item in self.items if isinstance(item, MenuItem)]

    # Find Item: Checks if an item with a specific key exists and returns it.
    def findItem(self, key:str):

        # Account for case-sensitivity.
        fixedTargetKey = key if self.caseSensitive else key.upper()
        fixedItemKey = (lambda key : key) if self.caseSensitive else (lambda key : key.upper())
        
        # Find item.
        items = self.__filteredItemsOnly()
        for item in items:
            if fixedItemKey(item.key) == fixedTargetKey:
                return item
                
        # Fallback.
        return None
    
    # (Internal) Add To List: Adds an item to the list at the end or at an index.
    def __addToList(self, newItem:MenuItem|MenuSeparator, index:int|None = None):

        # Ensure item doesn't already exist.
        if (newItem is MenuItem) and (self.findItem(newItem.key)):
            raise ValueError(f"Cannot add item with key \"{newItem.key}\" to menu: Item with such key already exists.")

        # Add/insert item.
        if index:
            self.items.insert(index, newItem)
        else:
            self.items.append(newItem)

    # Create Item (new): Adds a new menu item to the list.
    def createItem(
            self,
            key:str, name:str,
            description:str|None = None,
            action:Callable[[object, MenuTransport], MenuTransport]|None = None,
            index:int|None = None
        ):
        self.__addToList(MenuItem(key, name, description, action), index)
        
    # Add Item (existing): Adds an existing menu item to the list.
    def addItem(self, item:MenuItem, index:int|None = None):
        self.__addToList(item, index)

    # Separate: Adds a seprator to the list.
    def separate(self, index:int|None = None):
        self.__addToList(MenuSeparator(), index)

    # Print method: Displays menu.
    def print(self):

        # Create table.
        table = Table(title=self.title, caption=self.subtitle, box=box.ROUNDED)
        table.add_column("Key", justify="right", style="cyan", no_wrap=True)
        table.add_column("Item", justify="left", style="magenta")
        table.add_column("Description", justify="left", style="cyan")

        # Populate.
        for item in self.items:
            match item:
                case MenuItem():
                    table.add_row(item.key, f"[b]{item.name}[/b]", f"[i]{item.description}[/i]" if item.description else "")
                case MenuSeparator():
                    table.add_section()
        
        # Print.
        console.print(table)

    # Prompt method: Prompts user to select menu item.
    def prompt(self):

        # Get input.
        items = self.__filteredItemsOnly()
        if (self.caseSensitive):
            choices = [item.key for item in items]
        else:
            choices = [item.key.lower() for item in items] + [item.key.upper() for item in items]
        result = Prompt.ask(self.promptText, choices=choices, show_choices=False)

        # Return selected option.
        return result
    
    # Activate method: Activates an item.
    def activate(self, key:str, transport:MenuTransport|None = None):

        # Find item and make sure it exists.
        item = self.findItem(key)
        if not(item):
            raise IndexError(f"Cannot find item with key \"{key}\" in menu: No such item exists.")
        else:
            return item.activate(transport if transport else MenuTransport())
        
    # Populate method: Populates the menu using an external method.
    def populate(self):
        if (self.populator):
            self.populator(self)
        
    # Auto method: Automatically handles menu.
    def auto(self, forever:bool = True):

        # Main loop.
        lastTransport = MenuTransport()
        while forever and not(lastTransport.exitFlag):

            # Populate menu.
            self.populate()

            # Display menu.
            console.clear()
            self.print()

            # Get choice.
            console.print()
            choice = self.prompt()

            # Activate action.
            console.clear()
            lastTransport = self.activate(choice, lastTransport)

        # Return last choice.
        return lastTransport.chosenKey
