from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QFontDialog


class CustomDialogWarning(QDialog):
    def __init__(self, params=None):
        super().__init__()

        font = QtGui.QFont()
        font.setPointSize(12)
        text = str(params)
        self.setWindowTitle("Warning!")

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)

        self.layout = QVBoxLayout()
        message = QLabel(text)
        message.setFont(font)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
