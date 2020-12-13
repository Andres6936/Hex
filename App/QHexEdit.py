from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtGui import QColor, QFont, QResizeEvent, QPaintEvent, QMouseEvent, QKeyEvent, QPainter, QPalette, \
    QFontMetrics
from PyQt5.QtCore import QByteArray, QIODevice, QPoint, QRect, pyqtSignal, Qt
from App.Chunks import Chunks
from App.UndoStack import UndoStack


class QHexEdit(QAbstractScrollArea):
    dataChanged = pyqtSignal()
    overwriteModeChanged = pyqtSignal(bool)

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
        self.modified = True
        self.addressDigit = 0
        self.rowsShown = 0

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
        self.dataShown = QByteArray()
        self.selectionColor = QColor()
        self.hexDataShow = QByteArray()
        self.addressAreaColor = QColor()
        self.highlightingColor = QColor()

        self.setFont(QFont("Monospace", 12))

    def setAddressArea(self, addressArea: bool) -> None:
        self.addressArea = addressArea
        self.adjust()
        self.setCursorPosition(self.cursorPosition)
        self.viewport().update()

    def setAddressAreaColor(self, color: QColor) -> None:
        self.addressAreaColor = color
        self.viewport().update()

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
        status = self.chunks.setIODevice(device)
        self.dataChangedPrivate()
        return status

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
        return self.modified

    def lastIndexOf(self, array: QByteArray, _from: int) -> int:
        pass

    def redo(self) -> None:
        pass

    def selectionToReadableString(self) -> str:
        pass

    def selectedData(self) -> str:
        pass

    def setFont(self, font: QFont) -> None:
        newFont = QFont(font)
        newFont.setStyleHint(QFont.Monospace)
        super(QHexEdit, self).setFont(newFont)
        metrics = self.fontMetrics()
        self.pxCharWidth = metrics.horizontalAdvance('2')
        self.pxCharHeight = metrics.height()
        self.pxGapAdr = self.pxCharWidth // 2
        self.pxGapAdrHex = self.pxCharWidth
        self.pxGapHexAscii = 2 * self.pxCharWidth
        self.pxCursorWidth = self.pxCharHeight // 7
        self.pxSelectionSub = self.pxCharHeight // 5
        self.viewport().update()

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
            pxPosStartY = self.pxCharHeight
            # Draw some patterns if needed
            painter.fillRect(event.rect(), self.viewport().palette().color(QPalette.Base))
            if self.addressArea:
                painter.fillRect(
                    QRect(-pxOfsx, event.rect().top(), self.pxPosHexX - self.pxGapAdrHex // 2, self.height()),
                    self.addressAreaColor)

            if self.asciiArea:
                linePos = self.pxPosAsciiX - (self.pxGapHexAscii // 2)
                painter.setPen(Qt.gray)
                painter.drawLine(linePos - pxOfsx, event.rect().top(), linePos - pxOfsx, self.height())
            painter.setPen(self.viewport().palette().color(QPalette.WindowText))
            if self.addressArea:
                pxPosY = self.pxCharHeight
                for row in range(self.dataShown.size() // self.bytesPerLine):
                    address = "{0:0<16}".format(self.addressDigit)
                    painter.drawText(self.pxPosAdrX - pxOfsx, pxPosY, address.upper() if self.hexCaps else address)
                    pxPosY += self.pxCharHeight

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
                asciiPositionInShowData = hexPositionInShowData // 2
                ch = self.dataShown.at(asciiPositionInShowData)
                if ch < ' ' or ch > '~':
                    ch = '.'
                painter.drawText(self.pxCursorX - pxOfsx, self.pxCursorY, ch)
            else:
                painter.drawText(self.pxCursorX - pxOfsx, self.pxCursorY,
                                 self.hexDataShow.mid(hexPositionInShowData,
                                                      1).toUpper() if self.hexCaps else self.hexDataShow.mid(
                                     hexPositionInShowData, 1))
        # emit event, if size has changed
        if self.lastEventSize != self.chunks.size:
            self.lastEventSize = self.chunks.size
            # self.currentSizeChanged(self.lastEventSize)

    def resizeEvent(self, event: QResizeEvent) -> None:
        if self.dynamicBytesPerLine:
            pxFixGaps = 0
            if self.addressArea:
                pxFixGaps = self.addressWidth * self.pxCharWidth + self.pxGapAdr
            pxFixGaps += self.pxGapAdrHex
            if self.asciiArea:
                pxFixGaps += self.pxGapHexAscii
            # +1 because the last hex value do not have space. so it is effective one char more
            charWidth = (self.viewport().width() - pxFixGaps) // self.pxCharWidth + 1
            # 2 hex alfa-digits 1 space 1 ascii per byte = 4; if ascii is disabled then 3
            # to prevent devision by zero use the min value 1
            self.setBytesPerLine(max(charWidth // (4 if self.asciiArea else 3), 1))
        self.adjust()

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
        if self.addressArea:
            self.addressDigit = self.addressWidth
            self.pxPosHexX = self.pxGapAdr + self.addressDigit * self.pxCharWidth * self.pxGapAdrHex
        else:
            self.pxPosHexX = self.pxGapAdrHex
        self.pxPosAdrX = self.pxGapAdr
        self.pxPosAsciiX = self.pxPosHexX + self.hexCharInLine * self.pxCharWidth + self.pxGapHexAscii

        # Set horizontalScrollBar()
        pxWidth = self.pxPosAsciiX
        if self.asciiArea:
            pxWidth += self.bytesPerLine * self.pxCharWidth
        self.horizontalScrollBar().setRange(0, pxWidth - self.viewport().width())
        self.horizontalScrollBar().setPageStep(self.viewport().width())

        # Set verticalScrollbar()
        self.rowsShown = (self.viewport().height() - 4) // self.pxCharHeight
        lineCount = (self.chunks.size // self.bytesPerLine) + 1
        self.verticalScrollBar().setRange(0, lineCount - self.rowsShown)
        self.verticalScrollBar().setPageStep(self.rowsShown)

        value = self.verticalScrollBar().value()

    # noinspection PyUnresolvedReferences
    def dataChangedPrivate(self) -> None:
        self.modified = self.undoStack.index() != 0
        self.adjust()
        self.dataChanged.emit()

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
