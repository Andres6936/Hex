from PyQt5.QtWidgets import QMainWindow, QMenu, QToolBar, QAction, QLabel, QFrame
from PyQt5.QtGui import QCloseEvent, QDragEnterEvent, QDropEvent, QIcon
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

        self.setAcceptDrops(True)
        self.init()
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
        self.setUnifiedTitleAndToolBarOnMac(True)
        self.setCentralWidget(self.hexEdit)
        self.createStatusBar()
        self.createToolBars()
        self.createActions()
        self.readSettings()
        self.createMenus()

    def createActions(self):
        self.openAction = QAction(QIcon('Icons/MenuOpen.svg'), '&Open', self)
        self.saveAction = QAction(QIcon('Icons/MenuSaveAll'), '&Save', self)
        self.saveAsAction = QAction('Save &As...', self)
        self.saveReadable = QAction('Save &Readable', self)
        self.exitAction = QAction('E&xit', self)
        self.undoAction = QAction(QIcon('Icons/Undo.svg'), '&Undo', self)
        self.redoAction = QAction(QIcon('Icons/Redo.svg'), '&Redo', self)
        self.saveReadableSelection = QAction('Save Selection Readable', self)
        self.aboutAction = QAction('&About', self)
        self.aboutQtAction = QAction('About &Qt', self)
        self.findAction = QAction(QIcon('Icons/Find.svg'), '&Find/Replace', self)
        self.findNextAction = QAction('Find &Next', self)
        self.optionsAction = QAction('&Options', self)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu('&File')
        self.fileMenu.addAction(self.openAction)
        self.fileMenu.addAction(self.saveAction)
        self.fileMenu.addAction(self.saveAsAction)
        self.fileMenu.addAction(self.saveReadable)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.editMenu = self.menuBar().addMenu('&Edit')
        self.editMenu.addAction(self.undoAction)
        self.editMenu.addAction(self.redoAction)
        self.editMenu.addAction(self.saveReadableSelection)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.findAction)
        self.editMenu.addAction(self.findNextAction)
        self.editMenu.addSeparator()
        self.editMenu.addAction(self.optionsAction)

        self.helpMenu = self.menuBar().addMenu('&Help')
        self.helpMenu.addAction(self.aboutAction)
        self.helpMenu.addAction(self.aboutQtAction)

    def createStatusBar(self):
        self.statusBar().addPermanentWidget(QLabel('Address:'))
        labelAddress = QLabel()
        labelAddress.setMinimumWidth(70)
        self.statusBar().addPermanentWidget(labelAddress)

        self.statusBar().addPermanentWidget(QLabel('Size:'))
        labelSize = QLabel()
        labelSize.setMinimumWidth(70)
        self.statusBar().addPermanentWidget(labelSize)

        self.statusBar().addPermanentWidget(QLabel('Mode:'))
        labelOverwriteMode = QLabel()
        labelOverwriteMode.setMinimumWidth(70)
        self.statusBar().addPermanentWidget(labelOverwriteMode)

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
