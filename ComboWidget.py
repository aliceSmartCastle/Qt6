import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QLabel, QComboBox, QApplication, QVBoxLayout, QCheckBox

from layout_methob import layout_modes


class comboDemo(QWidget):
    music_label: QLabel
    review_label: QLabel
    music_gener_list: list[str]
    music_combo: QComboBox
    music_layout: QVBoxLayout
    music_radio: QCheckBox

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.music_label = QLabel()
        self.review_label = QLabel()
        self.music_combo = QComboBox()
        self.music_layout = QVBoxLayout()
        self.music_radio = QCheckBox("sure your chosen ")

        self.setWindowTitle("Widget combo demo")
        self.resize(300, 200)

        self.music_label.setText("Please chose your like music genre :")

        self.music_gener_list = [' Pop & Mainstream', ' Hip-Hop & R&B', ' Electronic / EDM', ' Rock & Alternative',
                                 ' Trendy \\ Internet Vibes', 'Mood & Atmosphere', 'Other'
                                                                                   'Mood & Atmosphere', 'Other']
        for i in range(len(self.music_gener_list)):
            self.music_combo.addItem(self.music_gener_list[i])

        self.music_combo.activated.connect(self.music_list)
        self.music_radio.stateChanged.connect(self.music_list)

        layout_modes(widgets=(self.music_label, self.music_combo, self.music_radio, self.review_label),
                     layout=self.music_layout,
                     self=self, mode='vbox_center')

        self.show()

    def music_list(self, state):

        music_state = Qt.CheckState(state)
        if music_state == Qt.CheckState.Checked:
            self.review_label.setText(f"Your choice music genre is : {self.music_combo.currentText()}")
        elif music_state == Qt.CheckState.Unchecked:
            self.review_label.setText(f"you cancel choice music genre : {self.music_combo.currentText()}")


def main():
    app = QApplication(sys.argv)
    window = comboDemo()
    window.update()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
