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

# Easy update: Prints a status update.
def ezUpdate(message:str):
    console.print(f"[i][dim]{message}[/dim][/i]")

# Easy finish: Prints a final result and pauses.
def ezFinish(successful:bool, failReason:str = None):
    if successful:
        console.print("[b][green]Done.[/green][/b]")
    else:
        console.print(f"[b][red]Failed{'. Reason: '+failReason if failReason else ''}.[/red][/b]")
    console.print("")
    ezPause()

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
        currentFieldText:str = "value",
        blankAllowed:bool = True
    ):

    # Display current value.
    if (defaultValue and not(showDefault) and defaultAsCurrent):
        ezCurrentStr(defaultValue, currentFieldText)

    # Main loop.
    lastValue = None
    while not(lastValue):

        # Get value.
        lastValue = Prompt.ask(f"[b][cyan]Enter {fieldText}[/cyan][/b]", default=defaultValue, show_default=showDefault, choices=choiceValues, show_choices=showChoices)

        # Assert blank.
        if blankAllowed and not(lastValue):
            lastValue = ""

    # Return.
    return lastValue

# Easy confirm method: Prompts the user to confirm an action.
def ezConfirm(actionText:str = "continue"):
    return Confirm.ask(f"[b][cyan]Are you sure you want to {actionText}?[/cyan][/b]")
