from PyQt5.QtCore import Qt, QRegExp
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtGui import QRegExpValidator


class IPEdit(QLineEdit):
    def __init__(self, father):
        super(IPEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[0-9]|[1-9][0-9]|[1][0-9][0-9]|[2][0-4][0-9]|[2][5][0-5]"))
        self.setValidator(validator)

class AddressEdit(QLineEdit):
    def __init__(self):
        super(AddressEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[1-9][0-9]|[1][0-9][0-9]|[2][0-3][0-9]|[2][4][0-7]"))
        self.setValidator(validator)

class TimeEdit(QLineEdit):
    def __init__(self):
        super(TimeEdit, self).__init__()
        self.setAlignment(Qt.AlignVCenter)
        validator = QRegExpValidator(QRegExp("[1-9][0-9]{4}"))
        self.setValidator(validator)