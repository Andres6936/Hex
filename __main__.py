import sys
from PyQt5.QtWidgets import QApplication
from App.LoginWidget import LoginWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = LoginWidget()
    sys.exit(app.exec_())