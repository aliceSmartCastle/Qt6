import sys
from typing import Any

from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QApplication, QLabel, QLineEdit

from layout_methob import layout_setting


def button_slot(my_button: QPushButton, signal: Any | None = None) -> None:
    """
    add button signal  	call
    """
    if signal is not None:
        my_button.clicked.connect(signal)


class nyaWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("My Qt Application")
        my_button = QPushButton("please chick me nya~~")
        button_slot(my_button=my_button, signal=self.button_clicked)
        self.resize(100, 100)
        nya_label = QLabel()
        nya_edit = QLineEdit()
        self.label_edit(label=nya_label, edit=nya_edit)
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout_setting(layout, my_button, nya_label, nya_edit)
        self.show()

    @staticmethod
    def button_clicked() -> None:
        print("button has clicked")

    @staticmethod  # 使用静态方法装饰器，表明这是一个静态方法
    def label_edit(label: QLabel, edit: QLineEdit) -> None:  # 定义一个静态方法，接收一个QLabel和一个QLineEdit参数，无返回值
        edit.textChanged.connect(label.setText)  # 将QLineEdit的textChanged信号连接到QLabel的setText槽，当编辑框内容改变时更新标签文本


if __name__ == "__main__":
    app = QApplication(sys.argv)
    nya_app = nyaWindow()
    sys.exit(app.exec())
