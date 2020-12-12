import sys
from PyQt5.QtWidgets import QApplication
from Window.QHexWindow import QHexWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = QHexWindow()
    sys.exit(app.exec_())