# Imports.
from rich.panel import Panel
from rich import box
import stustustudy.app.common as common
from ..console import console
from ..menu import Menu
from ..set import SetTerm

# Define menu populator.
def cardFlashMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)

# Define menu.
cardFlashMenu = Menu(populator=cardFlashMenuPopulator)
cardFlashMenu.createItem("X", "[red]<[/red] Exit", "Return to flashcards menu.")
cardFlashMenu.separate()
cardFlashMenu.createItem("S", "[white]@[/white] Star/Unstar", "Toggle star on this term.")
cardFlashMenu.separate()
cardFlashMenu.createItem(",", "[green]{[/green] Previous", "Move one card back.")
cardFlashMenu.createItem("F", "[green]![/green] Flip", "Flip the flashcard.")
cardFlashMenu.createItem(".", "[green]}[/green] Next", "Move one card forward.")

# Define activation.
def cardFlashActivate(mode:str, termIndex:int, termObject:SetTerm):
    
    # Copy values.
    term = termObject.term
    definition = termObject.definition
    starred = termObject.starred

    # Main loop.
    flipped = False
    exitFlag = False
    while not(exitFlag):

        # Clear.
        console.clear()

        # Display flashcard.
        panel = Panel(
            f"{'[b][yellow]*[/yellow][/b]' if starred else ' '}[i][dim]{'Definition' if flipped else 'Term'}:[/dim][/i] {definition if flipped else term}",
            title = f"[b]{mode}: Card {termIndex+1}/{len(common.currentSet.terms)}[/b]",
            box = box.ROUNDED,
            padding = (2, 3)
        )
        console.print(panel)

        # Display menu.
        cardFlashMenu.populate(True)
        cardFlashMenu.print()
        selection = cardFlashMenu.prompt().upper()

        # Update accordingly.
        match selection:
            case "X":
                exitFlag = True
            case "S":
                termObject.starred = not(termObject.starred)
                starred = termObject.starred
            case ",":
                exitFlag = True
                return "-1"
            case "F":
                flipped = not(flipped)
            case ".":
                exitFlag = True
                return "+1"
            
    # Return.
    return "X"

