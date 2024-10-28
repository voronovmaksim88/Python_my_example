class Buffer:
    def __init__(self):  # конструктор без аргументов
        self.ost = []

    def add(self, *a):  # добавить следующую часть последовательности
        for i in a:
            self.ost.append(i)
        while len(self.ost) >= 5:
            summa = 0
            for _ in range(5):
                summa += self.ost.pop(0)
            print(summa)

    def get_current_part(self):
        # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были
        # добавлены
        print(self.ost)


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part()
buf.add(4, 5, 6)
buf.get_current_part()
buf.add(7, 8, 9, 10)
buf.get_current_part()
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
buf.get_current_part() # вернуть [1]
