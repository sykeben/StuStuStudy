# Imports.
from typing import Callable
from .menu import Menu
from .menuitem import MenuItem
from .menutransport import MenuTransport
from ..console import console
from ..utils.ui import ezPause, ezConfirm

# Submenu action: Activates auto on a submenu.
def submenuAction(submenu:Menu):
    def action(item:MenuItem, transport:MenuTransport):
        submenu.auto()
        return transport
    return action

# Exit action: Exits the current menu.
def exitAction(confirm:bool = False):
    if (confirm):
        def action(item:MenuItem, transport:MenuTransport):
            if (ezConfirm("exit")):
                transport.setExit()
            return transport
    else:
        def action(item:MenuItem, transport:MenuTransport):
            transport.setExit()
            return transport
    return action

# Text action: Displays a page of text.
def textAction(title:str|None = None, subtitle:str|None = None, text:str|None = None):
    def action(item:MenuItem, transport:MenuTransport):
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
        ezPause()
        return transport
    return action

# Error action: Display an error.
def errorAction(errorName:str, errorNotes:str):
    return textAction(title="[red]Error[/red]", subtitle=f"[red]{errorName}[/red]", text=errorNotes)

# Placehoder action: Displays a non-implemented error.
def placeholderAction():
    return errorAction(errorName="Not Implimented", errorNotes="This function has not been implemented yet.")

# Static action: Executes a static-like method that doesn't modify the transport.
def staticAction(method:Callable[[MenuItem], None]):
    def action(item:MenuItem, transport:MenuTransport):
        method(item)
        return transport
    return action

# Locked action: Executes an action if and only if a method returns True.
def lockedAction(errorMessage:str, checkMethod:Callable[[MenuItem], bool], subAction:Callable[[object, MenuTransport], MenuTransport]):
    def action(item:MenuItem, transport:MenuTransport):
        if (checkMethod()):
            return subAction(item, transport)
        else:
            return errorAction(errorName="Invalid Action", errorNotes=errorMessage)
    return action
