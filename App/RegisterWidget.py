from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, QVBoxLayout, QHBoxLayout

class RegisterWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Register Widget')
        self.displayWidgets()
        self.show()

    def displayWidgets(self):
        pass