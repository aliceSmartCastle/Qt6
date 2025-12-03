import os.path
import sys

import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QApplication


class myIconGui(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        icon_path = os.path.join(os.path.dirname(__file__), "Icon", "bird-scepter.png")
        os.environ["QT_WM_CLASS"] = "IconSet"
        self.setWindowIcon(QIcon(icon_path))
        self.resize(1000, 800)
        self.show()

    @staticmethod
    def setting_tittle_name(qt_windos: PyQt6.QtWidgets.QWidget, names: str) -> None:
        qt_windos.setWindowTitle(names)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setDesktopFileName("IconSet")
    wins = myIconGui()
    wins.setting_tittle_name(qt_windos=wins, names="finally icon temp test")
    sys.exit(app.exec())
