from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout

class RegisterWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.passwordConfirmEntry = QLineEdit(self)
        self.passwordConfirmEntry.setPlaceholderText('Confirm Password')
        self.buttonSignUp = QPushButton(self)
        self.buttonSignUp.setText('Sign Up')
        self.buttonSignUp.setStyleSheet('background-color: #389FD6; border: 2px solid #3592C4; '
                                        'color: #FFFFFF; padding: 1px 0; margin: 3px 0; border-radius: 3px;'
                                        'margin-top: 10px;')
        self.usernameEntry = QLineEdit(self)
        self.usernameEntry.setPlaceholderText('Enter Username')
        self.passwordEntry = QLineEdit(self)
        self.passwordEntry.setPlaceholderText('Enter Password')
        self.nameEntry = QLineEdit(self)
        self.nameEntry.setPlaceholderText('Enter Name')

        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Register Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        mainLayout =  QVBoxLayout(self)
        mainLayout.addWidget(self.nameEntry)
        mainLayout.addWidget(self.usernameEntry)
        mainLayout.addWidget(self.passwordEntry)
        mainLayout.addWidget(self.passwordConfirmEntry)
        mainLayout.addWidget(self.buttonSignUp)

        self.setLayout(mainLayout)