import tkinter as tk


class SimpleVectorPaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack()

        self.start_x = None
        self.start_y = None

        # Список объектов линий, представленных их координатами
        self.lines = []

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if not self.start_x and not self.start_y:
            # Зафиксировать начало отрезка
            self.start_x = event.x
            self.start_y = event.y
        else:
            # Создать вектор отрезка
            end_x = event.x
            end_y = event.y
            line = self.canvas.create_line(self.start_x, self.start_y, end_x, end_y)

            # Сохранить отрезок в списке линий
            self.lines.append((self.start_x, self.start_y, end_x, end_y, line))

            # Сброс координат для следующего отрезка
            self.start_x = None
            self.start_y = None

    # Функция сохранения векторного изображения (просто пример, не реализовано)
    def save_vector_image(self, filename):
        with open(filename, "w") as file:
            for line in self.lines:
                file.write(f"{line[0]},{line[1]},{line[2]},{line[3]}n")

    # Место для дополнительных функций, таких как загрузка, редактирование и удаление линий


if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleVectorPaintApp(root)
    root.title("Простой векторный графический редактор")
    root.mainloop()