from typing import Any

import holidays
from PyQt6.QtWidgets import QFormLayout, QDateTimeEdit, QWidget, QApplication, QLineEdit, QCompleter,QLabel

from qt_material import apply_stylesheet
from layout_methob import layout_modes


class DateTimeType:
    dataTimeLayout: QFormLayout
    dataTimeEdit: QDateTimeEdit
    countryLabel: QLineEdit
    holiLabel = QLineEdit
    timeNotice:QLineEdit


def holding_country(country_edit: QLineEdit) -> None:
    all_holiday = QCompleter(holidays.list_supported_countries())
    country_edit.setCompleter(all_holiday)
    country_edit.setClearButtonEnabled(True)


def worldwide_holidays(country_name, year: int) -> dict[Any, Any]:
    worldwide_holidays_dict = {}
    worldwide_holidays_name = []
    worldwide_holidays_day = []

   

    for vacation in holidays.country_holidays(country=country_name, years=year).items():
        worldwide_holidays_day.append(vacation[0])
        
        worldwide_holidays_name.append(vacation[1])
    worldwide_holidays_dict = dict(zip(worldwide_holidays_day, worldwide_holidays_name))
   
        

    return worldwide_holidays_dict


class DateTimeCustomer(DateTimeType, QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("Calender and Time")
        self.resize(400, 350)

        self.dataTimeEdit = QDateTimeEdit()
        self.dataTimeEdit.setCalendarPopup(True)
        self.dataTimeEdit.dateTimeChanged.connect(self.Calender_up)
        self.dataTimeEdit.editingFinished.connect(self.Calender_up)
        self.dataTimeEdit.setDisplayFormat('yyyy-MM-dd | hh:mm')

        self.countryLabel = QLineEdit()
        self.countryLabel.setPlaceholderText("Please enter the country code :")

        holding_country(country_edit=self.countryLabel)

        self.holiLabel = QLineEdit()
        self.holiLabel.setReadOnly(True)

        self.timeNotice = QLineEdit()
        #self.timeNotice.setReadOnly(True)
        self.timeNotice.setClearButtonEnabled(True)

        self.dataTimeLayout = QFormLayout()


        layout_modes(widgets=(self.dataTimeEdit, self.countryLabel, self.holiLabel,self.timeNotice), layout=self.dataTimeLayout,
                     self=self,
                     mode='form', element_name=('DateTime :', 'Country :', " Holidays :","TimeStatus : "))
        self.show()
    @staticmethod
    def parse_times(summer_solstice:dict,winter_solstice:dict,month_value:int,time_value:int,outLable:QLineEdit):
           
        

           if 6<month_value<11:
            
             for event,time_splite in  summer_solstice.items():
                  if time_value in time_splite:
    
                        if time_value in time_splite:
                         outLable.setText(event)
           
           if month_value<5 or month_value>11:
                for event,winter_time in winter_solstice.items():
            
                 if time_value in winter_time:
                      outLable.setText(event)
                
           
     
                  
    

    def Calender_up(self):
        Date_Value = self.dataTimeEdit.date().toPyDate()
        time_hour = self.dataTimeEdit.time().toPyTime().hour
        month_value = self.dataTimeEdit.date().toPyDate().month


        ## normal summer solstice  month is '6',and winnter solstice is '11'

        
        summer_solstice = {"Now is Dawn": (4,5),
                          "Now is Morning": (6, 7,8,9,10,11),
                          "Now is Noon": (12,),
                          "Now is Afternoon": (13,14, 15,16,17),
                          "Now is Dusk": (18,19),
                          "Now is Evening": (20,21, 22),
                          "Now is Night": (0, 1, 2, 3, 23)}
        winnter_solstice = {"Now is Dawn": (6,7),
                          "Now is Morning": (8,9,10,11),
                          "Now is Noon": (12,),
                          "Now is Afternoon": (13, 14, 15),
                          "Now is Dusk": (16,17),
                          "Now is Evening": (18,19,20,21,22),
                          "Now is Night": (0, 1, 2, 3, 4,5, 23)}
    
   
       
      
        if self.countryLabel.text() in holidays.list_supported_countries():
            holidays_world = worldwide_holidays(country_name=self.countryLabel.text(), year=Date_Value.year)
            if Date_Value in holidays_world.keys():
              
              self.holiLabel.setText(holidays_world[Date_Value])
            else:
                self.holiLabel.clear()
        self.parse_times(summer_solstice,winnter_solstice,month_value,
                         time_hour,self.timeNotice
                         )

           


def main():
    app = QApplication([])
    windowDate = DateTimeCustomer()
    apply_stylesheet(app,theme='dark_teal.xml', invert_secondary=True)
    app.exec()


if __name__ == '__main__':

  main()
