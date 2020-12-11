import sys
from PyQt5.QtWidgets import QApplication
from App.LoginWidget import LoginWidget
from App.RegisterWidget import RegisterWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = RegisterWidget()
    sys.exit(app.exec_())