import tkinter as tk
from tkinter import ttk
from datetime import datetime


class ClockApp:
    def __init__(self, tk_root):
        self.root = tk_root
        self.root.title("Текущее время")

        self.root.geometry("600x300")

        self.time_frame = ttk.Frame(self.root)
        self.time_frame.pack(expand=True, fill=tk.BOTH)  # Расширяем frame на весь root

        style = ttk.Style()
        style.configure("TLabel", background="black", foreground="green")
        style.configure("TFrame", background="black")

        # Словарь для преобразования месяцев
        self.months = {
            1: "January", 2: "February", 3: "March",
            4: "April", 5: "May", 6: "June",
            7: "July", 8: "August", 9: "September",
            10: "October", 11: "November", 12: "December"
        }

        # Словарь для преобразования дней недели на полные английские названия
        self.weekdays = {
            0: "Monday", 1: "Tuesday", 2: "Wednesday",
            3: "Thursday", 4: "Friday", 5: "Saturday", 6: "Sunday"
        }

        # Создаем label, используя place для точного позиционирования
        self.time_label = ttk.Label(self.time_frame, font=('Calibri bold', 80), style="TLabel")
        self.time_label.place(x=60, y=50)  # Пример позиционирования

        self.seconds_label = ttk.Label(self.time_frame, font=('Calibri', 40), style="TLabel")
        self.seconds_label.place(x=310, y=100)  # Пример позиционирования, рядом с time_label

        self.date_label = ttk.Label(self.root, font=('Calibri', 30), style="TLabel")
        self.date_label.place(x=50, y=180)  # Пример позиционирования в нижней части окна

        # Запуск функции обновления времени
        self.update_clock()

    def update_clock(self):
        now = datetime.now()

        time_str = now.strftime("%H:%M")
        seconds_str = now.strftime(":%S")

        # Получаем текстовое название месяца
        month_str = self.months[now.month]

        # Получаем сокращение дня недели
        weekday_str = self.weekdays[now.weekday()]

        # Формируем строку с датой, включающей текстовое название месяца
        date_str = f"{now.day} {month_str} {weekday_str}"

        self.time_label.config(text=time_str)
        self.seconds_label.config(text=seconds_str)
        self.date_label.config(text=date_str)

        # Планируем следующий вызов функции через 1000 миллисекунд (1 секунду)
        self.root.after(1000, self.update_clock)


if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()

if 1:
    a = 1
    print(a)
