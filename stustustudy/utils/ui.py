# Imports.
from typing import List
from rich.prompt import Prompt, Confirm
from ..console import console

# Easy pause method: Waits for user to press enter.
def ezPause(actionText:str = "continue"):
    console.print(f"[b][cyan]Press enter to {actionText}...[/cyan][/b]")
    input()

# Easy prompt method (string): Prompts the user for string input.
def ezPromptStr(
        fieldText:str = "value",
        defaultValue:str = None,
        showDefault:bool = False,
        choiceValues:List[str]|None = None,
        showChoices:bool = False
    ):
    return Prompt.ask(f"[b][cyan]Enter {fieldText}[/cyan][/b]", default=defaultValue, show_default=showDefault, choices=choiceValues, show_choices=showChoices)

# Easy confirm method: Prompts the user to confirm an action.
def ezConfirm(actionText:str = "continue"):
    return Confirm.ask(f"[b][cyan]Are you sure you want to {actionText}?[/cyan][/b]")
