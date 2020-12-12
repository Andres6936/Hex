from PyQt5.QtCore import QByteArray, QObject, QIODevice, QBuffer

class Chunk:
    def __init__(self):
        self.data = QByteArray()
        self.dataChanged = QByteArray()
        self.absPos : int = 0

class Chunks(QObject):
    def __init__(self, parent : QObject = None, device : QIODevice = None):
        super().__init__(parent)
        self.device = QBuffer(self) if device is None else device
        self.chunks: [Chunk] = []
        self.position = 0
        self.size = 0

        self.setIODevice(self.device)

    def setIODevice(self, device: QIODevice) -> bool:
        self.device = device
        status = self.device.open(QIODevice.ReadOnly)
        if status:
            self.size = self.device.size()
            self.device.close()
        else:
            # Fallback is an empty buffer
            self.size = 0
            self.device = QBuffer(self)
        self.chunks.clear()
        self.position = 0
        return status

    def data(self, position : int, count : int = -1, highlighted : QByteArray = None) -> QByteArray:
        pass

    def write(self, device : QIODevice, position : int = 0, count : int = -1) -> bool:
        pass

    def setDataChanged(self, position : int, dataChanged : bool) -> None:
        pass

    def dataChanged(self, position: int) -> bool:
        pass

    def indexOf(self, array: QByteArray, _from: int) -> int:
        pass

    def lastIndexOf(self, array: QByteArray, _from: int) -> int:
        pass

    def insert(self, position: int, character: str) -> bool:
        pass

    def overwrite(self, position: int, character: str) -> bool:
        pass

    def removeAt(self, position: int) -> bool:
        pass

    def getPosition(self) -> int:
        pass

    def getSize(self) -> int:
        pass

    def __getitem__(self, item):
        pass
