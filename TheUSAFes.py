from typing import Any

import holidays
from PyQt6.QtWidgets import QFormLayout, QWidget, QLabel, QApplication, QDateEdit, QSpinBox, QLineEdit
from dateutil import parser

from layout_methob import layout_modes


class NeedType:
    date_layout: QFormLayout
    notice_message: QLabel
    notice_text: QLineEdit
    america_data: QDateEdit
    year_spin: QSpinBox


def America_holidays(years=2020) -> dict[Any, Any]:
    holidays_dict = {}
    holidays_day = []
    holidays_name = []

    for va in holidays.US(years=years).items():
        holidays_day.append(str(va[0].year) + "-" + str(va[0].month) + "-" + str(va[0].day))
        holidays_name.append(va[1])
        holidays_dict = dict(zip(holidays_day, holidays_name))

    return holidays_dict


class festival_America(QWidget, NeedType):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("holidays check")
        self.resize(400, 380)
        self.setMinimumWidth(240)

        self.year_spin = QSpinBox()
        self.year_spin.setRange(1000, 10000)
        self.year_spin.setSingleStep(1)
        self.year_spin.setWrapping(True)

        self.notice_message = QLabel()

        self.america_data = QDateEdit()

        self.notice_text = QLineEdit()
        self.notice_text.setReadOnly(True)

        self.america_data.editingFinished.connect(self.date_up)
        self.year_spin.valueChanged.connect(self.date_up)

        self.date_layout = QFormLayout()

        layout_modes(widgets=(self.america_data, self.notice_text, self.year_spin, self.notice_message,), self=self,
                     layout=self.date_layout, mode="form",
                     element_name=("Year-and-Date : ", "the USA holidays : ", "sure year : ",
                                   ""))

        self.show()

    def date_up(self):

        dates = self.america_data.date()
        pydate = dates.toPyDate()
        self.year_spin.setValue(pydate.year)

        sure_year = America_holidays(years=pydate.year)

        compare_date = tuple(sure_year.keys())

        ToDate = [parser.parse(i).date() for i in compare_date]
        holiday_name = tuple(sure_year.values())
        new_holiday_dict = dict(zip(ToDate, holiday_name))

        if pydate in ToDate:
            self.notice_text.setText(new_holiday_dict[pydate])

            self.notice_message.clear()
        else:

            self.notice_text.clear()

            self.notice_message.setText("No festivals on this day")


def main():
    app = QApplication([])
    fes = festival_America()
    fes.update()
    app.exec()


if __name__ == '__main__':
    main()
