from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout


# noinspection PyUnresolvedReferences
class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.nameEntry = QLineEdit(self)
        self.passwordEntry = QLineEdit(self)
        self.buttonLogin = QPushButton(self)
        self.buttonLogin.setText('Login')
        self.buttonLogin.clicked.connect(self.verifyUserCheckTermsAndConditions)
        self.checkTerms = QCheckBox(self)
        self.checkTerms.setText('Terms and Conditions')
        self.initializeUI()

    def initializeUI(self):
        self.setBaseSize(400, 300)
        self.setWindowTitle('Login Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        mainLayout = QVBoxLayout(self)

        usernameLayout = QHBoxLayout(self)
        usernameLayout.addWidget(QLabel('Username: ', self))
        usernameLayout.addWidget(self.nameEntry)

        toolTipLayout = QVBoxLayout(self)
        toolTipLayout.addWidget(QLabel("Please, write your username", self))

        passwordLayout = QHBoxLayout(self)
        passwordLayout.addWidget(QLabel('Password: ', self))
        passwordLayout.addWidget(self.passwordEntry)

        checkTermsLayout = QHBoxLayout(self)
        checkTermsLayout.addWidget(self.checkTerms)

        buttonLayout = QHBoxLayout(self)
        buttonLayout.addWidget(self.buttonLogin)

        mainLayout.addLayout(usernameLayout)
        mainLayout.addLayout(toolTipLayout)
        mainLayout.addLayout(passwordLayout)
        mainLayout.addLayout(checkTermsLayout)
        mainLayout.addLayout(buttonLayout)

    def verifyUserCheckTermsAndConditions(self):
        if self.checkTerms.isChecked():
            print("Check")
        else:
            print("No Check")

