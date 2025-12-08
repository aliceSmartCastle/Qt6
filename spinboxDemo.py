from PyQt6.QtWidgets import QWidget, QSpinBox, QFormLayout, QApplication, QLabel
from qt_material import apply_stylesheet

from layout_methob import layout_modes


class PHwindow(QWidget):
    pH_table: QSpinBox
    ph_objet: QLabel
    ph_list: list[dict[str, int]]
    ph_layout: QFormLayout

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Ph check window ")
        self.resize(400, 380)

        self.pH_table = QSpinBox()
        self.ph_objet = QLabel('init ph object...')
        self.ph_layout = QFormLayout()
        self.ph_picture = QLabel()
        self.ph_list = [{"not object": -1, "battery Acid (Sulfuric Acid)": 0, " Stomach Acid (Gastric Acid)": 1
                            , "lemon juice": 2, "Orange juice": 3, "Tomato juice": 4,
                         "Acid rain": 5, 'Milk': 6, "Water": 7, "Sea water": 8, "Toothpaste": 9,
                         "Milk of Magnesia (Antacid)": 10, "Ammonia Solution (Cleaner)": 11,
                         "Bleach": 12, "Oven Cleaner": 13, "Liquid Drain Cleaner": 14
                         }]

        self.pH_table.setRange(-1, 14)
        self.pH_table.setSingleStep(1)
        self.pH_table.value = -1
        self.pH_table.setWrapping(True)

        self.pH_table.valueChanged.connect(self.ph_thing)

        layout_modes(layout=self.ph_layout, widgets=(self.pH_table, self.ph_objet), mode='form',
                     element_name=("pH value :", "pH object : "), self=self
                     )
        self.show()

    def ph_thing(self, ph_value):

        for i in self.ph_list:
            for j in i.items():
                if ph_value == j[1]:
                    self.ph_objet.setText(j[0])


def main():
    phApp = QApplication([])
    phWindow = PHwindow()
    phWindow.update()
    apply_stylesheet(phApp, theme='dark_teal.xml', invert_secondary=True)
    phApp.exec()


if __name__ == '__main__':
    main()
