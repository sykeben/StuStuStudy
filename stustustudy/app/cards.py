# Imports.
import random
import stustustudy.app.common as common
from ..menu import Menu, actions, MenuItem
from .cardFlash import cardFlashActivate

# Define linear static action.
def cardsLinearStaticAction(item:MenuItem):

    # Main loop.
    while (True):

        # Create starting point menu.
        startingPointMenu = Menu("[b][yellow]~[/yellow][/b] Linear", common.currentSetText())
        startingPointMenu.createItem("X", "[red]<[/red] Exit", "Exits this menu.")
        startingPointMenu.separate()
        startingPointMenu.items += [MenuItem(
            str(index+1),
            ("[yellow]*[/yellow]" if term.starred else "[white]»[/white]") + " " + term.term,
            term.definition
        ) for index, term in enumerate(common.currentSet.terms)]
        startingPointMenu.separate()
        startingPointMenu.createItem("B", "[yellow]{[/yellow] Beginning", "Start at the beginning of the term list.")
        startingPointMenu.createItem("E", "[yellow]}[/yellow] End", "Start at the end of the term list.")

        # Get starting point.
        startIndex = startingPointMenu.auto(False).upper()
        match startIndex:
            case "X":
                return # No starting point, exit requested.
            case "B":
                startIndex = 0
            case "E":
                startIndex = len(common.currentSet.terms) - 1
            case _:
                startIndex = int(startIndex) - 1

        # Main loop.
        currentIndex = startIndex
        lastSelection = None
        while (lastSelection != "X"):

            # Get term.
            currentTerm = common.currentSet.terms[currentIndex]

            # Activate card.
            lastSelection = cardFlashActivate("[yellow]~[/yellow] Linear", currentIndex, currentTerm)

            # Process result.
            match lastSelection:
                case "-1":
                    if (currentIndex > 0): currentIndex -= 1
                case "+1":
                    if (currentIndex < len(common.currentSet.terms)-1): currentIndex += 1

# Define random static action.
def cardsRandomStaticAction(item:MenuItem):

    # Shuffle cards.
    shuffledTerms = list(common.currentSet.terms)
    for i in range(random.randint(1, 3)):
        random.shuffle(shuffledTerms)

    # Main loop.
    currentIndex = 0
    lastSelection = None
    while (lastSelection != "X"):

        # Get term.
        currentTerm = shuffledTerms[currentIndex]

        # Activate card.
        lastSelection = cardFlashActivate("[yellow]¿[/yellow] Random", currentIndex, currentTerm)

        # Process result.
        match lastSelection:
            case "-1":
                if (currentIndex > 0): currentIndex -= 1
            case "+1":
                if (currentIndex < len(common.currentSet.terms)-1): currentIndex += 1


# Define populator for flashcards menu.
def cardsMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)

# Define flashcards menu.
cardsMenu = Menu("[b][green]¶[/green][/b] Flashcards", populator=cardsMenuPopulator)
cardsMenu.createItem("X", "[red]<[/red] Exit", "Exits this menu.", actions.exitAction())
cardsMenu.separate()
cardsMenu.createItem("L", "[yellow]~[/yellow] Linear", "Study flashcards in order.", actions.staticAction(cardsLinearStaticAction))
cardsMenu.createItem("R", "[yellow]¿[/yellow] Random", "Study flashcards after shuffling.", actions.staticAction(cardsRandomStaticAction))
