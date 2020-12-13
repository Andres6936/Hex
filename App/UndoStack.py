from PyQt5.QtWidgets import QUndoStack


class UndoStack(QUndoStack):
    def __init__(self):
        super().__init__()

    def removeAt(self):
        pass

    def insertChar(self):
        pass

    def insertArray(self):
        pass

    def overwriteChar(self):
        pass

    def overwriteArray(self):
        pass
