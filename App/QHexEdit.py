from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtGui import QColor, QFont, QResizeEvent, QPaintEvent, QMouseEvent, QKeyEvent
from PyQt5.QtCore import QByteArray, QIODevice
from App.Chunks import Chunks
from App.UndoStack import UndoStack

class QHexEdit(QAbstractScrollArea):
    def __init__(self):
        super().__init__()

        self.addressArea = True
        self.addressWidth = 4
        self.addressOffset = 0
        self.asciiArea = True
        self.overwriteMode = True
        self.highlighting = True
        self.readOnly = False
        self.cursorPosition = 0
        self.lastEventSize = 0
        self.hexCharInLine = 47
        self.bytesPerLine = 16
        self.editAreaIsAscii = False
        self.hexCaps = False
        self.dynamicBytesPerLine = False

        self.__font = QFont()
        self.chunks = Chunks()
        self.data = QByteArray()
        self.undoStack = UndoStack()
        self.selectionColor = QColor()
        self.addressAreaColor = QColor()
        self.highlightingColor = QColor()

    def setData(self, device : QIODevice) -> bool:
        pass

    def dataAt(self, position : int, count : int) -> QByteArray:
        pass

    def write(self, device : QIODevice, position : int, count : int) -> bool:
        pass

    def insertChar(self, index : int, character : str) -> None:
        pass

    def removeChar(self, index : int, length : int) -> None:
        pass

    def replaceChar(self, index : int, char : str) -> None:
        pass

    def insertAtArray(self, position : int, array : QByteArray) -> None:
        pass

    def replaceAtArray(self, position : int, length : int, array : QByteArray) -> None:
        pass

    def ensureVisible(self) -> None:
        pass

    def indexOf(self, array : QByteArray, _from : int) -> int:
        pass

    def isModified(self) -> bool:
        pass

    def lastIndexOf(self, array : QByteArray, _from : int) -> int:
        pass

    def redo(self) -> None:
        pass

    def selectionToReadableString(self) -> str:
        pass

    def selectedData(self) -> str:
        pass

    def setFont(self, font: QFont) -> None:
        pass

    def toReadableString(self) -> str:
        pass

    def undo(self) -> None:
        pass

    def keyPressEvent(self, event: QKeyEvent) -> None:
        pass

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        pass

    def mousePressEvent(self, event: QMouseEvent) -> None:
        pass

    def paintEvent(self, event: QPaintEvent) -> None:
        pass

    def resizeEvent(self, event: QResizeEvent) -> None:
        pass

    def focusNextPrevChild(self, nextChild: bool) -> bool:
        pass

    def resetSelection(self):
        pass

    def resetSelectionAtPosition(self, position : int) -> None:
        pass

    def setSelection(self, position : int) -> None:
        pass

    def getSelectionBegin(self) -> int:
        pass

    def getSelectionEnd(self) -> int:
        pass

    def adjust(self) -> None:
        pass

    def dataChangedPrivate(self) -> None:
        pass

    def refresh(self) -> None:
        pass

    def readBuffers(self) -> None:
        pass

    def toReadable(self, array : QByteArray) -> str:
        result = str()
        for i in range(array.size(), 16):
            addString = str(self.addressOffset + i)
            hexString = str()
            ascString = str()
            for j in range(16):
                if i + j < array.size():
                    hexString += " " + array.mid(i + j, 1).toHex()
                    character = int(array[i + j])
                    if character < 0x20 or character > 0x7E:
                        character = '.'
                    ascString += str(character)
            result += addString + ' ' + hexString + ' ' + ascString + '\n'
        return result
