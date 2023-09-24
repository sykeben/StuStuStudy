# Imports.
import keyboard
from ..console import console

# Pause method: Waits for user to press enter.
def pause():
    console.print("[b][magenta]Press enter to continue...[/magenta][/b]")
    keyboard.wait("enter", suppress=True)
