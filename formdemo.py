import os.path

from FuncTip import spiteLine
from PyQt6.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt6.QtWidgets import QWidget, QPushButton, QFormLayout, QApplication, QLabel, QLineEdit, QMessageBox, QTableView, \
    QHeaderView, QVBoxLayout

from layout_methob import layout_modes
from slots_and_signal import button_slot


class read_food_information(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("food information")
        self.resize(400, 300)
        data_path = os.path.join(os.getcwd(), 'sqlLib')
        this_db = QSqlDatabase.addDatabase('QSQLITE')
        this_db.setDatabaseName(os.path.join(data_path, 'food_information.db'))
        this_db.open()

        self.model_view = QSqlTableModel()
        self.model_view.setTable('food_information')
        self.model_view.select()

        view_food = QTableView()
        view_food.setModel(self.model_view)

        view_food.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        view_food.setAlternatingRowColors(True)
        view_food.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        view_food.setEditTriggers(QTableView.EditTrigger.EditKeyPressed)
        view_food.setSortingEnabled(True)

        layout = QVBoxLayout()

        layout.addWidget(view_food)
        self.setLayout(layout)


def load_food():
    app = QApplication([])
    windows = read_food_information()
    windows.show()
    app.exec()


class FormDemos(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("food information")
        self.resize(400, 300)

        self.layout_way = False

        layout = QFormLayout()

        foodName = QLabel("Food Name:")
        self.food_name_edit = QLineEdit()

        food_fromCountry = QLabel("origin :")
        self.food_fromCountry_edit = QLineEdit()

        food_package = QLabel("Packed in :")
        self.food_package_edit = QLineEdit()

        food_color = QLabel("Color :")
        self.food_color_edit = QLineEdit()

        food_price = QLabel("Price :")
        self.food_price_edit = QLineEdit()

        self.add_sql = QPushButton("Add to Sql")
        self.add_sql.setCheckable(True)
        button_slot(my_button=self.add_sql, signal=self.add_to_sql)

        if self.layout_way:

            layout_modes(widgets=(foodName, self.food_name_edit, food_fromCountry, self.food_fromCountry_edit
                                      , food_package, self.food_package_edit, food_price, self.food_price_edit,
                                  food_color,
                                  self.food_color_edit, self.add_sql),
                         self=self,
                         layout=layout, mode='form')
        else:
            layout_modes(
                widgets=(self.food_name_edit, self.food_fromCountry_edit, self.food_package_edit, self.food_price_edit,
                         self.food_color_edit,
                         self.add_sql),
                self=self, layout=layout, element_name=('Name :', 'origin :', 'packed in :',
                                                        'price :', 'color :',
                                                        ''), mode='form')

            self.show()

    def save_to_sql(self):
        data_path = os.path.join(os.getcwd(), 'sqlLib')
        this_db = QSqlDatabase.addDatabase('QSQLITE')
        this_db.setDatabaseName(os.path.join(data_path, 'food_information.db'))
        this_db.open()
        food_name = self.food_name_edit.text()
        food_origin = self.food_fromCountry_edit.text()
        food_packed = self.food_package_edit.text()
        food_price = self.food_price_edit.text()
        food_color = self.food_color_edit.text()

        query = QSqlQuery()
        query.exec(
            """CREATE TABLE IF NOT EXISTS food_information (id INTEGER PRIMARY KEY AUTOINCREMENT ,foodName TEXT, origin  TEXT,package_in TEXT, price REAL,
            color TEXT)""")

        model_food = QSqlTableModel()
        model_food.setTable('food_information')
        model_food.select()

        record_food = model_food.record()
        record_food.setValue('foodName', food_name)
        record_food.setValue('origin', food_origin)
        record_food.setValue('package_in', food_packed)
        record_food.setValue('price', food_price)
        record_food.setValue('color', food_color)
        model_food.insertRecord(-1, record_food)
        model_food.submitAll()

        if not query.exec():
            QMessageBox.critical(self, 'error', f'{query.lastError().text()}')
        else:
            QMessageBox.information(self, 'info', 'data saved successfully')
            this_db.close()

    def add_to_sql(self):
        if self.add_sql.isChecked():
            question = QMessageBox.question(self, 'spl', 'are you sure add date to sql',
                                            buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            if question == QMessageBox.StandardButton.Yes:
                self.save_to_sql()
                self.add_sql.setChecked(False)
            else:
                self.add_sql.setChecked(False)


def main():
    food_exe = QApplication([])
    food_window = FormDemos()
    food_window.update()
    food_exe.exec()


def control_food():
    chonse = input(spiteLine(
        context=f'which way do you control food {'*' * 37}\n{'*' * 12}enter 1 to save the food information to sql') +
                   spiteLine(context=f'\n{'*' * 12}enter 2 to read the food information from sql{'*' * 10}') + '\n')
    if chonse == '1':
        main()
    elif chonse == '2':
        load_food()
    else:
        print('please enter 1 or 2')


if __name__ == "__main__":
    control_food()
