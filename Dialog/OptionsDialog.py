from PyQt5.QtWidgets import QDialog, QWidget


class OptionsDialog(QDialog):
    def __init__(self, parent: QWidget = None):
        super().__init__(parent)

    def show(self):
        super().show()
