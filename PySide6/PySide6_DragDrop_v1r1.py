from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtCore import Qt

class Block(QLabel):
    last_square_number_AND = 0
    last_square_number_OR = 0
    last_square_number_IN = 0

    def __init__(self, *args, x=300, y=300, width=50, height=50, **kwargs):
        super().__init__(*args, **kwargs)

        # Передадим геометрию через аргументы метода super или последующий вызов setGeometry
        self.setGeometry(x, y, width, height)

        self.setStyleSheet("""
            background-color: black;
            color: white;
            font-size: 10px; 
            font-weight: bold; 
            qproperty-alignment: AlignCenter;
        """)

    def paintEvent(self, event):
        super().paintEvent(event)

        # Создаем объект QPainter для рисования
        painter = QPainter(self)
        # Устанавливаем кисть (цвет и стиль заливки)
        painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))

        # Вычисляем координаты для круга
        radius = 10  # Диаметр круга
        x = self.width() - radius // 2  # Сдвигаем круг на половину его радиуса влево, чтобы он был посередине края
        y = (self.height() // 2) - (radius // 2)  # Позиционируем по вертикали посредине виджета

        # Рисуем круг с заданными параметрами
        painter.drawEllipse(x, y, radius, radius)

        # Вычисляем координаты для круга
        radius = 10  # Диаметр круга
        x = 0-radius // 2  # Сдвигаем круг на половину его радиуса влево, чтобы он был посередине края
        y = (self.height() // 4) - (radius // 2)  # Позиционируем по вертикали посредине виджета

        # Рисуем круг с заданными параметрами
        painter.drawEllipse(x, y, radius, radius)

        # Вычисляем координаты для круга
        radius = 10  # Диаметр круга
        x = 0-radius // 2  # Сдвигаем круг на половину его радиуса влево, чтобы он был посередине края
        y = (self.height() // 4)*3 - (radius // 2)  # Позиционируем по вертикали посредине виджета

        # Рисуем круг с заданными параметрами
        painter.drawEllipse(x, y, radius, radius)

        painter.end()  # Завершаем рисование


    def mousePressEvent(self, event):
        self.__mousePressPos = event.globalPosition().toPoint()
        self.__mousePressWindowPos = self.pos()
        self.__mouseMovePos = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        currPos = self.mapToParent(event.position().toPoint())
        globalPos = event.globalPosition().toPoint()
        diff = globalPos - self.__mouseMovePos

        self.move(diff)
        self.__mouseMovePos = globalPos - self.pos()

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPosition().toPoint() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return


class BlockAND(Block):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("AND_" + str(BlockAND.last_square_number_AND))


class BlockOR(Block):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText("OR_" + str(BlockOR.last_square_number_OR))

class BlockIN(Block):
    def __init__(self, *args, x=300, y=300, width=50, height=25, **kwargs):
        super().__init__(*args, **kwargs)
        # Передадим геометрию через аргументы метода super или последующий вызов setGeometry
        self.setGeometry(x, y, width, height)

        self.setText("IN_" + str(BlockIN.last_square_number_IN))

        self.setStyleSheet("""
            background-color: green;
            color: white;
            font-size: 10px; 
            font-weight: bold; 
            qproperty-alignment: AlignCenter;
        """)




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)  # Используем QVBoxLayout

        self.button_AND = QPushButton("AND")
        self.layout.addWidget(self.button_AND)
        self.button_AND.clicked.connect(self.create_block_and)

        self.button_OR = QPushButton("OR")
        self.layout.addWidget(self.button_OR)
        self.button_OR.clicked.connect(self.create_block_or)

        self.button_IN = QPushButton("IN")
        self.layout.addWidget(self.button_IN)
        self.button_IN.clicked.connect(self.create_block_in)

        self.count_button = QPushButton("Показать количество")
        self.layout.addWidget(self.count_button)
        self.count_button.clicked.connect(self.show_counts)

        self.count_label_and = QLabel("AND: 0")
        self.layout.addWidget(self.count_label_and)

        self.count_label_or = QLabel("OR: 0")
        self.layout.addWidget(self.count_label_or)

        self.count_label_in = QLabel("IN: 0")
        self.layout.addWidget(self.count_label_in)

    def create_block_and(self):
        BlockAND.last_square_number_AND += 1
        BlockAND(self.central_widget).show()
        # Увеличиваем счётчик в соответствующем классе


    def create_block_or(self):
        BlockOR.last_square_number_OR += 1
        BlockOR(self.central_widget).show()
        # Увеличиваем счётчик в соответствующем классе

    def create_block_in(self):
        BlockIN.last_square_number_IN += 1
        BlockIN(self.central_widget).show()
        # Увеличиваем счётчик в соответствующем классе



    def show_counts(self):
        # Обновляем текст метки с использованием текущих значений
        self.count_label_and.setText(f"AND: {BlockAND.last_square_number_AND}")
        self.count_label_or.setText(f"OR: {BlockOR.last_square_number_OR}")
        self.count_label_in.setText(f"IN: {BlockIN.last_square_number_IN}")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 600, 600)
    window.show()
    sys.exit(app.exec())