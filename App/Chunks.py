from PyQt5.QtCore import QByteArray, QObject, QIODevice

class Chunk:
    def __init__(self):
        self.data = QByteArray()
        self.dataChanged = QByteArray()
        self.absPos : int = 0

class Chunks(QObject):
    def __init__(self, parent : QObject = None, device : QIODevice = None):
        super().__init__(parent)
        self.device = QIODevice() if device is None else device
        self.chunks : [Chunk] = []
        self.position = 0
        self.size = 0

    def setIODevice(self, device : QIODevice) -> bool:
        pass

    def data(self, position : int, count : int = -1, highlighted : QByteArray = None) -> QByteArray:
        pass

    def write(self, device : QIODevice, position : int = 0, count : int = -1) -> bool:
        pass

    def setDataChanged(self, position : int, dataChanged : bool) -> None:
        pass

    def dataChanged(self, position : int) -> bool:
        pass

    def indexOf(self, array : QByteArray, _from : int) -> int:
        pass

    def lastIndexOf(self, array : QByteArray, _from : int) -> int:
        pass