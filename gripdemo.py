import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QApplication, QMessageBox
from ReHelper import validUserName

from layout_methob import layout_modes
from slots_and_signal import button_slot


class gridWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("log in form")
        self.resize(400, 300)

        userNameLabel = QLabel("User name:")
        self.userLineEdit = QLineEdit()
        self.userLineEdit.setClearButtonEnabled(True)

        passwordLabel = QLabel("Password:")
        self.passwordLineEdit = QLineEdit()
        self.passwordLineEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordLineEdit.setClearButtonEnabled(True)

        self.login_button = QPushButton("Login")
        self.cancel_button = QPushButton("Cancel")
        self.login_button.setCheckable(True)
        self.cancel_button.setCheckable(True)

        button_slot(self.login_button, self.valid_login)
        button_slot(self.cancel_button, self.valid_login)

        layout = QGridLayout()
        layout_modes(
            widgets=(userNameLabel, self.userLineEdit, passwordLabel, self.passwordLineEdit, self.login_button,
                     self.cancel_button),
            self=self,
            layout=layout, mode='grid',
            alignment=(Qt.AlignmentFlag.AlignAbsolute, Qt.AlignmentFlag(0), Qt.AlignmentFlag(0), Qt.AlignmentFlag(0),
                       Qt.AlignmentFlag.AlignRight, Qt.AlignmentFlag.AlignRight),
            widget_position=((0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)))
        self.show()

    def valid_login(self):
        if self.login_button.isChecked():
            QMessageBox.information(self, 'log-in',
                                    validUserName(name=self.userLineEdit.text()))

        elif self.cancel_button.isChecked():
            cancel_window = QMessageBox.question(self, 'cancel', 'do you want to close the log window?',
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if cancel_window == QMessageBox.StandardButton.Yes:
                self.close()
            else:
                pass


def main():
    app = QApplication(sys.argv)
    window = gridWindow()
    window.update()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
