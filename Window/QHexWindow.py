from PyQt5.QtWidgets import QMainWindow, QMenu, QToolBar, QAction
from PyQt5.QtGui import QCloseEvent, QDragEnterEvent, QDropEvent
from PyQt5.QtCore import QFile
from App.QHexEdit import QHexEdit


class QHexWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.currentFile = str()
        self.isUntitled = False

        self.hexEdit = QHexEdit()

        self.file = QFile()
        self.fileMenu = QMenu()
        self.editMenu = QMenu()
        self.helpMenu = QMenu()
        self.fileToolBar = QToolBar()
        self.editToolBar = QToolBar()
        self.undoAction = QAction()
        self.redoAction = QAction()
        self.openAction = QAction()
        self.saveAction = QAction()
        self.exitAction = QAction()
        self.findAction = QAction()
        self.aboutAction = QAction()
        self.closeAction = QAction()
        self.saveAsAction = QAction()
        self.saveReadable = QAction()
        self.aboutQtAction = QAction()
        self.optionsAction = QAction()
        self.findNextAction = QAction()
        self.saveReadableSelection = QAction()

        self.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        pass

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        pass

    def dropEvent(self, event: QDropEvent) -> None:
        pass

    def about(self):
        pass

    def dataChanged(self):
        pass

    def open(self):
        pass

    def optionsAccepted(self):
        pass

    def findNext(self):
        pass

    def save(self):
        pass

    def saveAs(self):
        pass

    def saveSelectionToReadableFile(self):
        pass

    def saveToReadableFile(self):
        pass

    def setAddress(self):
        pass

    def setOverwriteMode(self):
        pass

    def setSize(self):
        pass

    def showOptionsDialog(self):
        pass

    def showSearchDialog(self):
        pass

    def init(self):
        pass

    def createACtions(self):
        pass

    def createMenus(self):
        pass

    def createStatusBar(self):
        pass

    def createToolBars(self):
        pass

    def loadFile(self):
        pass

    def readSettings(self):
        pass

    def saveFile(self):
        pass

    def setCurrentFile(self):
        pass

    def strippedName(self):
        pass

    def writeSettings(self):
        pass
