from PyQt5.QtWidgets import QStackedWidget
from App.LoginWidget import LoginWidget
from App.RegisterWidget import RegisterWidget
from Controller.IController import IController, overrides

class SignUpController(QStackedWidget, IController):
    def __init__(self):
        super().__init__()

        self.addWidget(RegisterWidget())
        self.addWidget(LoginWidget())

        self.show()

    def showLoginForm(self):
        self.setCurrentIndex(1)

    @overrides(IController)
    def nextScene(self):
        pass