# Menu transport class.
class MenuTransport:

    # Initializor.
    def __init__(self, chosenKey:str|None = None, exitFlag:bool = False):

        # Set parameters.
        self.chosenKey = chosenKey
        self.exitFlag = exitFlag

    # Exit flag set/unset.
    def setExit(self):
        self.exitFlag = True
    def unsetExit(self):
        self.exitFlag = False
