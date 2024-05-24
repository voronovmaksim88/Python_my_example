# Сначала необходимо установить DearPyGui, если она еще не установлена:
# pip install dearpygui

import dearpygui.dearpygui as dpg


def button_clicked():
    # Функция, которая выполняется при нажатии на кнопку
    print("Button clicked!")


# Инициализация DearPyGui
dpg.create_context()

# Создание первичного окна
with dpg.window(label="example"):
    # Добавление кнопки в окно
    # Первый аргумент - название, отображаемое на кнопке
    # Второй аргумент - функция, вызываемая при нажатии на кнопку
    dpg.add_button(label="Press me", callback=button_clicked)

# Создание визуального интерфейса в ранее созданном контексте
dpg.create_viewport(title='Example DearPyGui', width=600, height=200)
# Позиционирование окна по центру экрана
dpg.setup_dearpygui()
# Отображение окна
dpg.show_viewport()

# Запуск основного цикла обработки событий
dpg.start_dearpygui()

# Завершение работы с DearPyGui
dpg.destroy_context()
