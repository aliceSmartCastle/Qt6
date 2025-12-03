from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel

from HboxMode import layout_modes
from slots_and_signal import button_slot


class VboxWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Vbox method show")
        layout = QVBoxLayout()
        title_list = ["on power", 'off power', 'default']
        self.title_button = [QPushButton(i) for i in title_list]

        self.on_label = QLabel()
        self.off_label = QLabel()
        self.default_label = QLabel()

        for i in self.title_button:
            i.setCheckable(True)
            button_slot(i, self.text_tiger)  # alone_index = (total_index - i)
        layout_modes(
            widgets=(self.title_button[0], self.on_label, self.title_button[1], self.off_label, self.title_button[2],
                     self.default_label), mode="vbox_margins", self=self, layout=layout, margins=(20, 20, 20, 20)
        )
        self.show()

    def text_tiger(self):
        on, off, default = self.title_button[0], self.title_button[1], self.title_button[2]
        if on.isChecked():
            self.on_label.setText("on button is apply")
            self.on_label.setStyleSheet('QLabel{background-color:gray}')
        else:
            self.on_label.setStyleSheet('')
            self.on_label.clear()
        if off.isChecked():
            self.off_label.setText("off button is apply")
            self.off_label.setStyleSheet('QLabel{background-color:red}')
        else:
            self.off_label.setStyleSheet('')
            self.off_label.clear()
        if default.isChecked():
            self.default_label.setText("default button is apply")
            self.default_label.setStyleSheet('QLabel{background-color:green}')
        else:
            self.default_label.setStyleSheet('')
            self.default_label.clear()


def main():
    app = QApplication([])
    window = VboxWindow()
    window.update()
    app.exec()


if __name__ == "__main__":
    main()
