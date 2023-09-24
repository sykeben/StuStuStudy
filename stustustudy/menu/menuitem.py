# Imports.
from typing import Callable
from .menutransport import MenuTransport

# Menu item class.
class MenuItem:

    # Initializor.
    def __init__(
            self,
            key:str, name:str,
            description:str|None = None,
            action:Callable[[object, MenuTransport], MenuTransport]|None = None,
            disabled:bool = False
        ):

        # Set parameters.
        self.key = key
        self.name = name
        self.description = description
        self.action = action
        self.disabled = disabled

    # Activate method: Activates item action (if exists).
    def activate(self, transport:MenuTransport|None = None):

        # Configure transport.
        transport = transport if transport else MenuTransport()
        transport.chosenKey = self.key

        # Activate action.
        if self.action:
            transport = self.action(self, transport)

        # Return.
        return transport
