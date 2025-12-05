from PyQt6.QtWidgets import QWidget, QLabel, QRadioButton, QApplication, QVBoxLayout, QMessageBox

from layout_methob import layout_modes


class LoveMovie(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("movie lover choice")
        self.resize(300, 250)
        self.setMinimumWidth(300)

        movie_label = QLabel("Please choice one your favorite movie ")
        self.movie_message = QMessageBox()
        self.movie_message.setWindowTitle("movie lover")

        Avatar: QRadioButton = QRadioButton(" Avatar", self)
        Titanic: QRadioButton = QRadioButton(" Titanic", self)
        StarWars: QRadioButton = QRadioButton(" Star Wars", self)
        NO_Movie_like: QRadioButton = QRadioButton(" NO Movie like", self)
        self.choice_result = QLabel()

        Avatar.toggled.connect(self.update_effect)

        StarWars.toggled.connect(self.update_effect)
        Titanic.toggled.connect(self.update_effect)
        NO_Movie_like.toggled.connect(self.update_effect)

        layout = QVBoxLayout()
        layout_modes(widgets=(movie_label, Avatar, Titanic, StarWars, NO_Movie_like, self.choice_result),
                     layout=layout, self=self,
                     mode='vbox_center')
        self.show()

    def update_effect(self):
        try:

            Get_movie = self.sender()
            assert (isinstance(Get_movie, QRadioButton)), "is same type"
            if Get_movie.isChecked():
                self.choice_result.setText(f"You choice movie is :{Get_movie.text()}")
                self.movie_message.setText(f"You choice movie is : {Get_movie.text()}")
                self.movie_message.exec()
        except AttributeError:
            ...


def main():
    app = QApplication([])
    window = LoveMovie()
    window.update()
    app.exec()


if __name__ == "__main__":
    main()
