import sys

from PyQt5.QtCore import QByteArray, QObject, QIODevice, QBuffer

NORMAL = 1
CHUNK_SIZE = 100


class Chunk:
    def __init__(self):
        self.data = QByteArray()
        self.dataChanged = QByteArray()
        self.absPos: int = 0


class Chunks(QObject):
    def __init__(self, parent: QObject = None, device: QIODevice = None):
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

    def data(self, position: int, maxSize: int = -1, highlighted: QByteArray = None) -> QByteArray:
        delta = 0
        chunkIdx = 0
        chunk = Chunk()
        buffer = QByteArray()
        if highlighted:
            highlighted.clear()
        if position >= self.size:
            return buffer
        if maxSize < 0:
            maxSize = self.size
        elif (position + maxSize) > self.size:
            maxSize = self.size - position

        self.device.open(QIODevice.ReadOnly)
        while maxSize > 0:
            chunk.absPos = sys.maxsize
            chunksLoopOngoing = True
            while chunkIdx < len(self.chunks) and chunksLoopOngoing:
                # In this section, we track changes before our required data and
                # we take the editdet data, if availible. ioDelta is a difference
                # counter to justify the read pointer to the original data, if
                # data in between was deleted or inserted.
                chunk = self.chunks[chunkIdx]
                if chunk.absPos > position:
                    chunksLoopOngoing = False
                else:
                    count = 0
                    chunkIdx += 1
                    chunkOfs = position - chunk.absPos
                    if maxSize > chunk.data.size() - chunkOfs:
                        count = chunk.data.size() - chunkOfs
                        delta += CHUNK_SIZE - chunk.data.size()
                    else:
                        count = maxSize

                    if count > 0:
                        buffer += chunk.data.mid(chunkOfs, count)
                        maxSize -= count
                        position += count
                        if highlighted:
                            highlighted += chunk.dataChanged.mid(chunkOfs, count)
            if maxSize > 0 and position < chunk.absPos:
                byteCount = 0
                if (chunk.absPos - position) > maxSize:
                    byteCount = maxSize
                else:
                    byteCount = chunk.absPos - position
                maxSize -= byteCount
                self.device.seek(position + delta)
                readBuffer: QByteArray = self.device.read(byteCount)
                buffer += readBuffer
                if highlighted:
                    highlighted += QByteArray(readBuffer.size(), NORMAL)
                position += readBuffer.size()
        self.device.close()

    def write(self, device: QIODevice, position: int = 0, count: int = -1) -> bool:
        pass

    def setDataChanged(self, position: int, dataChanged: bool) -> None:
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
