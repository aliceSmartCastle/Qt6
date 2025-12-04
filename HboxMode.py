import sys

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLabel, QHBoxLayout

from layout_methob import layout_modes
from slots_and_signal import button_slot


class layoutMode(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Layout mode show")
        self.resize(400, 450)
        self.layout_method = 'hbox'

        self.yes_button = QPushButton("yes")
        self.no_button = QPushButton("No")
        self.cancel_button = QPushButton("Cancel")

        self.yes_button.setCheckable(True)
        self.no_button.setCheckable(True)
        self.cancel_button.setCheckable(True)

        if self.layout_method == 'vbox':
            button_slot(my_button=self.yes_button, signal=self.active_text)
            button_slot(my_button=self.no_button, signal=self.active_text)
            button_slot(my_button=self.cancel_button, signal=self.active_text)

        self.button_yes = QLabel()
        self.button_No = QLabel()
        self.button_cancel = QLabel()

        v_layouts = QVBoxLayout()
        H_layout = QHBoxLayout()
        if self.layout_method == 'vbox':
            layout_modes(layout=v_layouts, self=self,
                         widgets=(self.button_yes, self.yes_button, self.button_No, self.no_button,
                                  self.button_cancel,
                                  self.cancel_button))
        elif self.layout_method == 'hbox':
            layout_modes(layout=H_layout, self=self,
                         widgets=(self.button_yes, self.yes_button, self.button_No, self.no_button,
                                  self.button_cancel,
                                  self.cancel_button), mode='hbox', item_distance=[0, 2, 0, 2, 0, 1])

        self.show()

    def active_text(self):

        if self.yes_button.isChecked():
            self.button_yes.setText("Yes is active")
        else:
            self.button_yes.setText("Yes is not active")
        if self.no_button.isChecked():
            self.button_No.setText("No is active")
        else:
            self.button_No.setText("No is not active")
        if self.cancel_button.isChecked():
            self.button_cancel.setText("Cancel is active")
        else:
            self.button_cancel.setText("Cancel is not active")


def main():
    my_app = QApplication(sys.argv)
    windows = layoutMode()
    windows.update()
    sys.exit(my_app.exec())


if __name__ == '__main__':
    main()
