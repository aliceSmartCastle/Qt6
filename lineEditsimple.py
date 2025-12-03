from PyQt6.QtWidgets import QWidget, QLineEdit, QVBoxLayout, QApplication, QLabel, QPushButton, QCompleter

from layout_methob import layout_setting
from slots_and_signal import button_slot


def auto_complete_country(line_edit: QLineEdit, line_label: QLabel, setText: str = None) -> None:
    country_list = ["China", "Japan", "Korea", "Canada", "Australia", "India",
                    "Russia", "France", "Germany",
                    "Italy", "Spain", "Brazil", "Mexico", "Argentina", "Chile", "Peru", "Colombia",
                    "Venezuela", "Haiti", "Iceland", "Norway", "Oman", "Poland", "Qatar", "Romania",
                    "Ukraine", "Denmark", "South Africa", "Egypt", "Morocco", "Algeria", "Wales", "Turkey",
                    "Zambia", "Luxembourg", "Yemen",
                    "Nigeria", "Kenya",
                    "Tanzania", "The United States of America"]
    sort_country = sorted(country_list)
    country_name = QCompleter(sort_country)
    line_edit.setCompleter(country_name)
    line_edit.setClearButtonEnabled(True)
    if setText is None:
        line_label.setText("please enter the country name")
    else:
        line_label.setText(setText)


def password_window(password_box: QLineEdit, password_label: QLabel) -> None:
    password_label.setText("please enter the password")
    password_box.setEchoMode(QLineEdit.EchoMode.Password)


def search_widget(search_box: QLineEdit, search_label: QLabel, setSearchText: str = None,
                  default_Text: str = None) -> None:
    if setSearchText is None:
        search_label.setText("country information")
    else:
        search_label.setText(setSearchText)
    if default_Text is None:
        search_box.setPlaceholderText("please enter of country name to search...")
    else:
        search_box.setPlaceholderText(default_Text)
    search_box.setClearButtonEnabled(True)


class rolandWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("QlineEdit,welcome to my world")
        self.resize(300, 280)
        # search
        search_box = QLineEdit()
        search_label = QLabel()
        search_widget(search_box, search_label=search_label)

        # country
        complete_edit = QLineEdit()
        country_label = QLabel()
        auto_complete_country(complete_edit, country_label)

        # password
        self.password_box = QLineEdit()
        self.password_label = QLabel()
        password_window(self.password_box, self.password_label)
        password_valid = QPushButton("log in")
        button_slot(password_valid, signal=self.valid_password)

        # layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        layout_setting(layout, search_label, search_box, country_label, complete_edit, self.password_label,
                       self.password_box,
                       password_valid)
        self.show()

    def valid_password(self):
        if self.password_box.text() == "123456":
            self.password_label.setText("password is valid")
        else:
            self.password_label.setText("password is invalid")


def main():
    app = QApplication([])
    roland = rolandWindow()
    roland.update()
    app.exec()


if __name__ == '__main__':
    main()
