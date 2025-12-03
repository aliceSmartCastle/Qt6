import os.path
import sys

from PyQt6.QtGui import QPixmap, QMovie
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QApplication

from slots_and_signal import layout_setting, button_slot


def setting_svg(label: QLabel, svg_path: str) -> None:
    """set svg image to label"""
    pixmap = QPixmap(svg_path)
    label.setPixmap(pixmap)


def setting_gif(label: QLabel, gif_path: str) -> None:
    """set gif image to label"""
    set_gif = QMovie(gif_path)
    label.setMovie(set_gif)
    set_gif.start()


class kaliWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Label method")
        clear_botton = QPushButton("clear text")
        this_label = QLabel()
        pix_label = QLabel()
        gif_label = QLabel()
        this_label.setText("label is created")
        self.resize(1920, 1080)
        button_slot(my_button=clear_botton, signal=this_label.clear)
        setting_svg(label=pix_label, svg_path=os.path.join(os.getcwd(), "svg", 'onime.jpg'))
        setting_gif(label=gif_label, gif_path=os.path.join(os.getcwd(), "gif", 'chiikawa.gif'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout_setting(layout, clear_botton, this_label, pix_label, gif_label)


def main_label():
    app = QApplication(sys.argv)
    window = kaliWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main_label()
