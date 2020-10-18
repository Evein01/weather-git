from PyQt5 import uic, QtWidgets
from pyowm import OWM

Form, _ = uic.loadUiType("progw.ui")  # Загружаем окно с формой

# Обращаемся к окну
class Ui (QtWidgets.QDialog, Form):
    def __init__(self):
        super(Ui, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_weather_city)  # При нажатии на кнопку выполняется ф-ия

# Определяем ф-ию, которая выполняется при нажатии на кнопку
    def get_weather_city(self):
        owm = OWM('3a587a614352c7dc86422c337521fabe')  # Мой OWM API
        city = self.lineEdit.text()  # line Edit принимает название города/страны от пользователя

        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)  # Получаем погоду в заданном городе/стране
        w = observation.weather
        t = w.temperature('celsius')['temp']  # Получаем температуру

# Выводим в label сообщение с текущей температурой и советом
        if t > 20:
            self.label.setText(f'Температура: {t}\nКрутая погода, кайфуй!')
        elif t > 0:
            self.label.setText(f'Температура: {t}\nТам холодно, одевайся теплее ^_^')
        else:
            self.label.setText(f'Температура: {t}\nТы сумасшедший.\nОпомнись и останься дома!')

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)  # Генерируем и запускаем приложение
    w = Ui()
    w.show()
    sys.exit(app.exec_())