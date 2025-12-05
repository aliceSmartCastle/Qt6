import sys
from typing import Any

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGridLayout, QCheckBox, QApplication, QMessageBox

from layout_methob import layout_modes


def checkbox_slot(box: QCheckBox, func: Any) -> None:
    box.stateChanged.connect(func)


class cheerup(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('cheerup for you like')
        self.resize(200, 210)

        self.today_pysco = QCheckBox("you feel happy today")
        self.today_pysco.setTristate(True)

        layout = QGridLayout()
        layout_modes(widgets=(self.today_pysco,), layout=layout, self=self, widget_position=(0, 0),
                     alignment=(Qt.AlignmentFlag.AlignCenter,), mode='grid')
        checkbox_slot(box=self.today_pysco, func=self.feel_today)
        self.show()

    @staticmethod
    def feel_today(state: Qt.CheckState) -> None:
        message = QMessageBox()
        message.setWindowTitle('cheerup your life')
        state_cond = Qt.CheckState(state)
        if state_cond == Qt.CheckState.Checked:
            message.setText('well done')
            message.exec()

        elif state_cond == Qt.CheckState.Unchecked:
            message.setText('you can do it')
            message.exec()
        elif state_cond == Qt.CheckState.PartiallyChecked:
            message.setText("today you are really best")
            message.exec()


if __name__ == '__main__':
    feel = QApplication(sys.argv)
    normal = cheerup()
    normal.update()
    sys.exit(feel.exec())
