from PyQt5.QtWidgets import QStackedWidget
from App.LoginWidget import LoginWidget
from App.RegisterWidget import RegisterWidget

class SignUpController(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.addWidget(RegisterWidget())
        self.addWidget(LoginWidget())

        self.show()

    def showLoginForm(self):
        self.setCurrentIndex(1)