# Импортирование необходимых модулей из библиотеки PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

count = 0


def on_clic_btn():
    print("hello")


def my_test_app():
    # Создание объекта QApplication
    app = QApplication(sys.argv)

    # Создание объекта QMainWindow
    window = QMainWindow()

    # Установка названия окна
    window.setWindowTitle('Test')

    # Установка начального положения и размеров окна.
    # Параметры - x позиция, y позиция, ширина, высота
    window.setGeometry(400, 400, 1000, 500)

    main_text = QtWidgets.QLabel(window)
    main_text.setText("Hello from PyQt5 ")
    main_text.move(100, 10)

    btn = QtWidgets.QPushButton(window)
    btn.setText('Button')

    btn.clicked.connect(on_clic_btn)
    btn.move(100, 50)

    # Отображение окна
    window.show()

    # Начало выполнения цикла обработки событий QApplication
    # sys.exit() гарантирует аккуратный выход из программы
    sys.exit(app.exec_())


# Если скрипт запущен напрямую (а не импортирован), запускаем функцию my_test_app()
if __name__ == '__main__':
    my_test_app()
