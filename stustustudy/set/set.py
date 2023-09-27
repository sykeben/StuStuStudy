# Imports.
from io import TextIOWrapper
import json
from .setterm import SetTerm

# Set class.
class Set:

    # Initializor.
    def __init__(
            self,
            title:str = "Untitled Set",
            description:str = "",
            terms:list[SetTerm]|None = None
        ):

        # Set parameters.
        self.title = title
        self.description = description
        self.terms = terms if terms else list()

    # (Internal) Add to Terms: Adds a term to the set at the end or at an index.
    def __addToTerms(self, newTerm:SetTerm, index:int|None = None):
        if index:
            self.terms.insert(index, newTerm)
        else:
            self.terms.append(newTerm)

    # Create Term (new): Adds a new term to the set.
    def createTerm(self, term:str = "", definition:str = "", starred:bool = False, index:int|None = None):
        self.__addToTerms(SetTerm(term, definition, starred), index)

    # Add Term (existing): Adds an existing term to the set.
    def addTerm(self, term:SetTerm, index:int|None = None):
        self.__addToTerms(term, index)

    # Remove Term: Removes a term from the set & returns it.
    def removeTerm(self, index:int):
        return self.terms.pop(index)
    
    # Move Term: Moves a term from index #x to #y.
    def moveTerm(self, nX:int, nY:int):
        self.addTerm(self.removeTerm(nX), nY)

    # (Static) From JSON: Creates a set from a JSON file.
    @staticmethod
    def fromJSON(filePointer:TextIOWrapper):
        
        # Load data.
        data = json.load(filePointer)
        properties = data["properties"]
        terms = data["terms"]

        # Create set from data.
        newSet = Set(properties["title"], properties["description"])
        for term in terms:
            newSet.createTerm(term["term"], term["definition"], (term["starred"] == "True"))

        # Return.
        return newSet
    
    # To JSON: Creates/overwrites the set to a JSON file.
    def toJSON(self, filePointer:TextIOWrapper):

        # Initialize data.
        data = {

            # Set properties.
            "properties": {
                "title": self.title,
                "description": self.description
            },

            # Terms list.
            "terms": [
                {
                    "term": term.term,
                    "definition": term.definition,
                    "starred": ("True" if term.starred else "False")
                } for term in self.terms
            ]

        }

        # Save data.
        json.dump(data, filePointer)
