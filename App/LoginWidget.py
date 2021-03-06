from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout


# noinspection PyUnresolvedReferences
class LoginWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.nameEntry = QLineEdit(self)
        self.nameEntry.setPlaceholderText('Username')
        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setPlaceholderText('Password')
        self.passwordEntry.setEchoMode(QLineEdit.Password)
        self.buttonLogin = QPushButton(self)
        self.buttonLogin.setText('Login')
        self.buttonLogin.setStyleSheet('background-color: #389FD6; border: 2px solid #3592C4; '
                                       'color: #FFFFFF; padding: 1px 0; margin: 3px 0; border-radius: 3px;'
                                       'font: bold;')
        self.buttonLogin.clicked.connect(self.verifyUserCheckTermsAndConditions)
        self.checkTerms = QCheckBox(self)
        self.checkTerms.setText('Terms and Conditions')
        self.checkTerms.setStyleSheet('margin-bottom: 10px;')
        self.initializeUI()

    def initializeUI(self):
        self.setBaseSize(400, 300)
        self.setWindowTitle('Login Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        mainLayout = QVBoxLayout(self)

        usernameLayout = QHBoxLayout()
        usernameLayout.addWidget(self.nameEntry)

        toolTipLayout = QVBoxLayout()
        toolTipLayout.addWidget(QLabel("Please, write your username", self))

        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(self.passwordEntry)

        checkTermsLayout = QHBoxLayout()
        checkTermsLayout.addWidget(self.checkTerms)

        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.buttonLogin)

        mainLayout.addLayout(usernameLayout)
        mainLayout.addLayout(toolTipLayout)
        mainLayout.addLayout(passwordLayout)
        mainLayout.addLayout(checkTermsLayout)
        mainLayout.addStretch()
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)

    def verifyUserCheckTermsAndConditions(self):
        if self.checkTerms.isChecked():
            print("Check")
        else:
            print("No Check")

