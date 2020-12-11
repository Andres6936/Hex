import sys
from PyQt5.QtWidgets import QApplication
from App.LoginWidget import LoginWidget
from App.RegisterWidget import RegisterWidget
from Controller.SignUpController import SignUpController

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    widget = SignUpController()
    sys.exit(app.exec_())