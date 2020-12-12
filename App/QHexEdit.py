from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtGui import QColor, QFont, QResizeEvent, QPaintEvent, QMouseEvent, QKeyEvent, QPainter, QPalette
from PyQt5.QtCore import QByteArray, QIODevice, QPoint, QRect
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
        self.blink = True

        # Name Convention: pixel position start with px
        self.pxCharWidth = 0
        self.pxCharHeight = 0
        self.pxPosHexX = 0
        self.pxPosAdrX = 0
        self.pxPosAsciiX = 0
        self.pxGapAdr = 0
        self.pxGapAdrHex = 0
        self.pxGapHexAscii = 0
        self.pxCursorWidth = 0
        self.pxSelectionSub = 0
        self.pxCursorX = 0
        self.pxCursorY = 0

        # Name Convention: absolute byte position in chunks start with b
        self.bSelectionBegin = 0
        self.bSelectionEnd = 0
        self.bSelectionInit = 0
        self.bPosFirst = 0
        self.bPosLast = 0
        self.bPosCurrent = 0

        self.__font = QFont()
        self.chunks = Chunks()
        self.data = QByteArray()
        self.cursorRect = QRect()
        self.undoStack = UndoStack()
        self.selectionColor = QColor()
        self.hexDataShow = QByteArray()
        self.addressAreaColor = QColor()
        self.highlightingColor = QColor()

    def setAddressArea(self, addressArea: bool) -> None:
        pass

    def setAddressAreaColor(self, color: QColor) -> None:
        pass

    def setAddressOffset(self, addressOffset: int) -> None:
        pass

    def setAddressWidth(self, width: int) -> None:
        pass

    def setAsciiArea(self, asciiArea: bool) -> None:
        pass

    def setBytesPerLine(self, count: int) -> None:
        pass

    def setCursorPosition(self, position: int) -> None:
        pass

    def getCursorPositionAt(self, position: QPoint) -> int:
        # Calc cursor position depending on a graphical position
        posX = position.x() + self.horizontalScrollBar().value()
        posY = position.y() - 3
        if self.pxPosHexX <= posX < (self.pxPosHexX + (1 + self.hexCharInLine) * self.pxCharWidth):
            self.editAreaIsAscii = False
            x = (posX - self.pxPosHexX) / self.pxCharWidth
            x = (x / 3) * 2 + x % 3
            y = (posY / self.pxCharHeight) * 2 * self.bytesPerLine
            return self.bPosFirst * 2 + x + y
        elif self.asciiArea and self.pxPosAsciiX <= posX < (
                self.pxPosAsciiX + (1 + self.bytesPerLine) * self.pxCharWidth):
            self.editAreaIsAscii = True
            x = 2 * (posX - self.pxPosAsciiX) / self.pxCharWidth
            y = (posY / self.pxCharHeight) * 2 * self.bytesPerLine
            return self.bPosFirst * 2 + x + y
        else:
            return -1

    def setDataArray(self, array: QByteArray) -> None:
        pass

    def setDataDevice(self, device: QIODevice) -> bool:
        pass

    def dataAt(self, position: int, count: int) -> QByteArray:
        pass

    def write(self, device: QIODevice, position: int, count: int) -> bool:
        pass

    def insertChar(self, index: int, character: str) -> None:
        pass

    def removeChar(self, index: int, length: int) -> None:
        pass

    def replaceChar(self, index: int, char: str) -> None:
        pass

    def insertAtArray(self, position: int, array: QByteArray) -> None:
        pass

    def replaceAtArray(self, position: int, length: int, array: QByteArray) -> None:
        pass

    def ensureVisible(self) -> None:
        pass

    def indexOf(self, array: QByteArray, _from: int) -> int:
        pass

    def isModified(self) -> bool:
        pass

    def lastIndexOf(self, array: QByteArray, _from: int) -> int:
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
        painter = QPainter(self.viewport())
        pxOfsx = self.horizontalScrollBar().value()
        if event.rect() != self.cursorRect:
            pass

        # _cursorPosition counts in 2, _bPosFirst counts in 1
        hexPositionInShowData = self.cursorPosition - 2 * self.bPosFirst

        if 0 <= hexPositionInShowData < self.hexDataShow.size():
            if self.readOnly:
                color = self.viewport().palette().dark().color()
                painter.fillRect(
                    QRect(self.pxCursorX - pxOfsx, self.pxCursorY - self.pxCharHeight + self.pxSelectionSub,
                          self.pxCharWidth, self.pxCharHeight), color)
            elif self.blink and self.hasFocus():
                painter.fillRect(self.cursorRect, self.palette().color(QPalette.WindowText))

            if self.editAreaIsAscii:
                pass

    def resizeEvent(self, event: QResizeEvent) -> None:
        pass

    def focusNextPrevChild(self, nextChild: bool) -> bool:
        pass

    def resetSelection(self):
        pass

    def resetSelectionAtPosition(self, position: int) -> None:
        pass

    def setSelection(self, position: int) -> None:
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

    def toReadable(self, array: QByteArray) -> str:
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
