# Imports.
from rich.prompt import Confirm
from typing import Callable
from .menu import Menu
from .menuitem import MenuItem
from .menutransport import MenuTransport
from ..console import console
from ..utils.ui import pause

# Submenu action: Activates auto on a submenu.
def submenuAction(submenu:Menu):
    def action(item:MenuItem, transport:MenuTransport) -> MenuTransport:
        submenu.auto()
        return transport
    return action

# Exit action: Exits the current menu.
def exitAction(confirm:bool = False):
    if (confirm):
        def action(item:MenuItem, transport:MenuTransport) -> MenuTransport:
            if (Confirm.ask("Are you sure you want to exit?")):
                transport.setExit()
            return transport
    else:
        def action(item:MenuItem, transport:MenuTransport) -> MenuTransport:
            transport.setExit()
            return transport
    return action

# Text action: Displays a page of text.
def textAction(title:str|None = None, subtitle:str|None = None, text:str|None = None):
    def action(item:MenuItem, transport:MenuTransport) -> MenuTransport:
        if (title):
            console.print(f"[b]{title}[/b]")
        if (subtitle):
            console.print(f"[b][i][dim]{subtitle}[/dim][/i][/b]")
        if (text):
            if (title or subtitle):
                console.print()
            console.print(text)
        if (title or subtitle or text):
            console.print()
        pause()
        return transport
    return action

# Placehoder action: Displays error.
def placeholderAction():
    return textAction(title="[red]Error[/red]", subtitle="[red]Not Implemented[/red]", text="This function has not been implemented yet.")

# Static action: Executes a static-like method that doesn't modify the transport.
def staticAction(method:Callable[[MenuItem], None]):
    def action(item:MenuItem, transport:MenuTransport) -> MenuTransport:
        method(item)
        return transport
    return action
