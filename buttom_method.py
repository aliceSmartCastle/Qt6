import os

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel

from layout_methob import layout_setting
from slots_and_signal import button_slot


def setting_button_icon(button: QPushButton, icon_path: str, button_size: tuple[int, int]) -> None:
    button.setIcon(QIcon(icon_path))
    button.setFixedSize(QSize(*button_size))


class yesodWindows(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("botton simple instruction")
        self.resize(300, 100)
        self.button_born = QPushButton("click me")
        self.button_label = QLabel("initial button")
        self.button_born.setCheckable(True)
        setting_button_icon(button=self.button_born, icon_path=os.path.join(os.getcwd(), 'svg', 'wsignel.svg'),
                            button_size=(250, 30))

        button_slot(self.button_born, signal=self.click_button)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout_setting(layout, self.button_label, self.button_born)

        self.show()

    def click_button(self) -> None:

        if self.button_born.isChecked():
            self.button_label.setText("hello")
        else:
            self.button_label.setText("bye")


def main() -> None:
    app = QApplication([])
    window = yesodWindows()
    window.update()
    app.exec()


if __name__ == "__main__":
    main()
