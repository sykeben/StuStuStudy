# Imports.
import stustustudy.app.common as common
from ..menu import Menu, actions

# Define populator for flashcards menu.
def cardsMenuPopulator(menu:Menu, firstTime:bool):
    common.currentSetPopulator(menu, firstTime)

# Define flashcards menu.
cardsMenu = Menu("[b][green]¶[/green][/b] Flashcards", populator=cardsMenuPopulator)
cardsMenu.createItem("X", "[red]<[/red] Exit", "Exits this menu.", actions.exitAction())
cardsMenu.separate()
cardsMenu.createItem("L", "[yellow]~[/yellow] Linear", "Study flashcards in order.", actions.placeholderAction())
cardsMenu.createItem("R", "[yellow]¿[/yellow] Random", "Study flashcards after shuffling.", actions.placeholderAction())
