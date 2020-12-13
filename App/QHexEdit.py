from PyQt5.QtWidgets import QAbstractScrollArea
from PyQt5.QtGui import QColor, QFont, QResizeEvent, QPaintEvent, QMouseEvent, QKeyEvent, QPainter, QPalette, QPen, \
    QBrush
from PyQt5.QtCore import QByteArray, QIODevice, QPoint, QRect, pyqtSignal, Qt, QTimer
from App.Chunks import Chunks
from App.UndoStack import UndoStack


class QHexEdit(QAbstractScrollArea):
    dataChanged = pyqtSignal()
    overwriteModeChanged = pyqtSignal(bool)

    # noinspection PyUnresolvedReferences
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

        self.chunks = Chunks(self)

        self.__font = QFont()
        self.data = QByteArray()
        self.cursorRect = QRect()
        self.penSelection = QPen()
        self.cursorTimer = QTimer()
        self.penHighlighted = QPen()
        self.undoStack = UndoStack()
        self.dataShown = QByteArray()
        self.brushSelection = QBrush()
        self.selectionColor = QColor()
        self.hexDataShow = QByteArray()
        self.markedShown = QByteArray()
        self.brushHighlighted = QBrush()
        self.addressAreaColor = QColor()
        self.highlightingColor = QColor()

        self.cursorTimer.timeout.connect(self.updateCursor)
        self.cursorTimer.setInterval(500)
        self.cursorTimer.start()

        self.verticalScrollBar().valueChanged.connect(self.adjust)
        self.horizontalScrollBar().valueChanged.connect(self.adjust)

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
        self.bytesPerLine = count
        self.hexCharInLine = count * 3 - 1
        self.adjust()
        self.setCursorPosition(self.cursorPosition)
        self.viewport().update()

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
        return self.chunks.data(position, count)

    def write(self, device: QIODevice, position: int, count: int) -> bool:
        return self.chunks.write(device, position, count)

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
        pxOffsetX = self.horizontalScrollBar().value()
        if event.rect() != self.cursorRect:
            pxPosStartY = self.pxCharHeight
            # Draw some patterns if needed
            painter.fillRect(event.rect(), self.viewport().palette().color(QPalette.Base))
            if self.addressArea:
                painter.fillRect(
                    QRect(-pxOffsetX, event.rect().top(), self.pxPosHexX - self.pxGapAdrHex // 2, self.height()),
                    self.addressAreaColor)

            if self.asciiArea:
                linePos = self.pxPosAsciiX - (self.pxGapHexAscii // 2)
                painter.setPen(Qt.gray)
                painter.drawLine(linePos - pxOffsetX, event.rect().top(), linePos - pxOffsetX, self.height())
            painter.setPen(self.viewport().palette().color(QPalette.WindowText))
            if self.addressArea:
                pxPosY = self.pxCharHeight
                for row in range(self.dataShown.size() // self.bytesPerLine):
                    address = "{0:0<16}".format(self.addressDigit)
                    painter.drawText(self.pxPosAdrX - pxOffsetX, pxPosY, address.upper() if self.hexCaps else address)
                    pxPosY += self.pxCharHeight
            colStandard = QPen(self.viewport().palette().color(QPalette.WindowText))
            painter.setBackgroundMode(Qt.TransparentMode)
            pxPosY = pxPosStartY
            for row in range(self.rowsShown):
                pxPosX = self.pxPosHexX - pxOffsetX
                pxPosAsciiX = self.pxPosAsciiX - pxOffsetX
                bPosLine = row * self.bytesPerLine
                pxPosY += self.pxCharHeight
                colIdx = 0
                while (bPosLine + colIdx) < self.dataShown.size() and colIdx < self.bytesPerLine:
                    c = self.viewport().palette().color(QPalette.Base)
                    painter.setPen(colStandard)
                    posBa = self.bPosFirst + bPosLine + colIdx
                    if self.getSelectionBegin() <= posBa < self.getSelectionEnd():
                        c = self.brushSelection.color()
                        painter.setPen(self.penSelection)
                    elif self.highlighting:
                        if self.markedShown.at(posBa - self.bPosFirst):
                            c = self.brushHighlighted.color()
                            painter.setPen(self.penHighlighted)
                    r = QRect()
                    if colIdx == 0:
                        r.setRect(pxPosX, pxPosY - self.pxCharHeight + self.pxSelectionSub, 2 * self.pxCharWidth,
                                  self.pxCharHeight)
                    else:
                        r.setRect(pxPosX - self.pxCharWidth, pxPosY - self.pxCharHeight + self.pxSelectionSub,
                                  3 * self.pxCharWidth, self.pxCharHeight)
                    painter.fillRect(r, c)
                    hex = self.hexDataShow.mid((bPosLine + colIdx) * 2, 2)
                    painter.drawText(pxPosX, pxPosY, hex.toUpper() if self.hexCaps else hex)
                    pxPosX += 3 * self.pxCharWidth
                    colIdx += 1

        # _cursorPosition counts in 2, _bPosFirst counts in 1
        hexPositionInShowData = self.cursorPosition - 2 * self.bPosFirst

        if 0 <= hexPositionInShowData < self.hexDataShow.size():
            if self.readOnly:
                color = self.viewport().palette().dark().color()
                painter.fillRect(
                    QRect(self.pxCursorX - pxOffsetX, self.pxCursorY - self.pxCharHeight + self.pxSelectionSub,
                          self.pxCharWidth, self.pxCharHeight), color)
            elif self.blink and self.hasFocus():
                painter.fillRect(self.cursorRect, self.palette().color(QPalette.WindowText))

            if self.editAreaIsAscii:
                asciiPositionInShowData = hexPositionInShowData // 2
                ch = self.dataShown.at(asciiPositionInShowData)
                if ch < ' ' or ch > '~':
                    ch = '.'
                painter.drawText(self.pxCursorX - pxOffsetX, self.pxCursorY, ch)
            else:
                painter.drawText(self.pxCursorX - pxOffsetX, self.pxCursorY,
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
            # to prevent division by zero use the min value 1
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
        return self.bSelectionBegin

    def getSelectionEnd(self) -> int:
        return self.bSelectionEnd

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
        self.bPosFirst = value * self.bytesPerLine
        self.bPosLast = self.bPosFirst + (self.rowsShown * self.bytesPerLine) - 1
        if self.bPosLast >= self.chunks.size:
            self.bPosLast = self.chunks.size - 1
        self.readBuffers()
        self.setCursorPosition(self.cursorPosition)

    # noinspection PyUnresolvedReferences
    def dataChangedPrivate(self) -> None:
        self.modified = self.undoStack.index() != 0
        self.adjust()
        self.dataChanged.emit()

    def refresh(self) -> None:
        self.ensureVisible()
        self.readBuffers()

    def readBuffers(self) -> None:
        self.dataShown = self.chunks.data(self.bPosFirst, self.bPosLast - self.bPosFirst + self.bytesPerLine + 1,
                                          self.markedShown)
        self.hexDataShow = QByteArray(self.dataShown.toHex())

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

    def updateCursor(self):
        if self.blink:
            self.blink = False
        else:
            self.blink = True
        self.viewport().update(self.cursorRect)
