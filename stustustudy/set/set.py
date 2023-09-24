# Imports.
from .setterm import SetTerm

# Set class.
class Set:

    # Initializor.
    def __init__(
            self,
            title:str = "Untitled Set",
            terms:list[SetTerm]|None = None
        ):

        # Set parameters.
        self.title = title
        self.terms = terms if terms else list()

    # (Internal) Add to Terms: Adds a term to the set at the end or at an index.
    def __addToTerms(self, newTerm:SetTerm, index:int|None = None):
        if index:
            self.terms.insert(index, newTerm)
        else:
            self.terms.append(newTerm)

    # Create Term (new): Adds a new term to the set.
    def createTerm(self, term:str = "", definition:str = "", index:int|None = None):
        self.__addToTerms(SetTerm(term, definition), index)

    # Add Term (existing): Adds an existing term to the set.
    def addTerm(self, term:SetTerm, index:int|None = None):
        self.__addToTerms(term, index)

    # Remove Term: Removes a term from the set & returns it.
    def removeTerm(self, index:int):
        return self.terms.pop(index)
    
    # Move Term: Moves a term from index #x to #y.
    def moveTerm(self, nX:int, nY:int):
        self.addTerm(self.removeTerm(nX), nY)
