from PyQt5.QtCore import QByteArray, QObject

class Chunk:
    def __init__(self):
        self.data = QByteArray()
        self.dataChanged = QByteArray()
        self.absPos : int = 0

class Chunks(QObject):
    def __init__(self):
        super().__init__()