import math
import sys

import sympy
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSlider, QFormLayout, QWidget, QApplication, QLabel, QMessageBox
from qt_material import apply_stylesheet

from layout_methob import layout_modes


class numericalType:
    numerica_list: list[float]
    number_slider: QSlider
    number_layout: QFormLayout
    number_label: QLabel
    sprt_label: QLabel


class sprt_rule(QWidget, numericalType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("sprt widget")
        self.resize(400, 350)

        self.number_slider = QSlider(Qt.Orientation.Horizontal)
        self.number_slider.setRange(0, 100)

        self.numerica_list = [math.sqrt(i) for i in range(1, 101)]

        self.number_slider.setSingleStep(1)
        self.number_slider.setPageStep(1)
        self.number_slider.setValue(0)

        self.number_slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
        self.number_slider.valueChanged.connect(self.sprt_number)

        self.number_label = QLabel()
        self.sprt_label = QLabel()

        self.number_layout = QFormLayout()

        layout_modes(widgets=(self.number_label, self.number_slider, self.sprt_label), self=self,
                     layout=self.number_layout,
                     mode="form", element_name=('sprt_symbol : ', 'sprt_rule : ', 'sprt_value : '))
        self.show()

    def sprt_deque(self, deque_sprt, index: int) -> int | float:
        if index > len(deque_sprt) - 1:
            QMessageBox.warning(self, "error index", "index out of range")
            index = 0
            self.number_slider.setValue(index)
            return index
        else:
            return deque_sprt[index]

    def sprt_number(self, values):
        sprt_math = [sympy.nsimplify(math.sqrt(i)) for i in range(1, 101)]
        self.number_label.setText(str(self.sprt_deque(deque_sprt=sprt_math, index=values)))
        self.sprt_label.setText(str(self.sprt_deque(deque_sprt=self.numerica_list, index=values)))


def main():
    app = QApplication(sys.argv)
    sprt_window = sprt_rule()
    sprt_window.update()
    apply_stylesheet(app, theme="light_cyan.xml")
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
