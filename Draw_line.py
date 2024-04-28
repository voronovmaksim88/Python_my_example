import tkinter as tk


class SimplePaintApp:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, bg='white', width=800, height=600)
        self.canvas.pack()

        # Начальные и конечные координаты отрезка
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.canvas.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        if not self.start_x and not self.start_y:
            # Зафиксировать начало отрезка
            self.start_x = event.x
            self.start_y = event.y
        else:
            # Зафиксировать конец отрезка и нарисовать его
            self.end_x = event.x
            self.end_y = event.y
            self.canvas.create_line(self.start_x, self.start_y, self.end_x, self.end_y)
            # Сброс координат для следующего отрезка
            self.start_x = None
            self.start_y = None


if __name__ == "__main__":
    my_root = tk.Tk()
    app = SimplePaintApp(my_root)
    my_root.title("Простой графический редактор")
    my_root.mainloop()
