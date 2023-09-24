# Imports.
from typing import List
from rich.prompt import Prompt, Confirm
from ..console import console

# Easy pause method: Waits for user to press enter.
def ezPause(actionText:str = "continue"):
    console.print(f"[b][cyan]Press enter to {actionText}...[/cyan][/b]")
    input()

# Easy title: Prints a title.
def ezTitle(title:str):
    console.print(f"[u][i]{title}[/i][/u]")
    console.print("")

# Easy current method (any): Prints the current value of a variable.
def ezCurrentAny(value:str, fieldText:str|None = None):
    console.print(f"[cyan]Current {fieldText if fieldText else 'value'}[/cyan]: {value}")

# Easy current method (string): Prints the current value of a variable.
def ezCurrentStr(value:str, fieldText:str|None = None):
    ezCurrentAny(f"\"{value}\"", fieldText)

# Easy prompt method (string): Prompts the user for string input.
def ezPromptStr(
        fieldText:str = "value",
        defaultValue:str = None,
        showDefault:bool = False,
        choiceValues:List[str]|None = None,
        showChoices:bool = False,
        defaultAsCurrent:bool = False,
        currentFieldText:str = "value"
    ):
    if (defaultValue and not(showDefault) and defaultAsCurrent): ezCurrentStr(defaultValue, currentFieldText)
    return Prompt.ask(f"[b][cyan]Enter {fieldText}[/cyan][/b]", default=defaultValue, show_default=showDefault, choices=choiceValues, show_choices=showChoices)

# Easy confirm method: Prompts the user to confirm an action.
def ezConfirm(actionText:str = "continue"):
    return Confirm.ask(f"[b][cyan]Are you sure you want to {actionText}?[/cyan][/b]")
