from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QPushButton, QVBoxLayout
from PySide6.QtGui import QPainter, QBrush
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMenu
from PySide6.QtCore import Signal


class Block(QLabel):
    delete_requested = Signal(object)  # Сигнал, который будет вызван при удалении блока

    def __init__(self, *args, x=300, y=300, width=50, height=50, name=None, **kwargs):
        super().__init__(*args, **kwargs)

        # Передадим геометрию через аргументы метода super или последующий вызов setGeometry
        self.setGeometry(x, y, width, height)
        self.name = name  # Добавляем атрибут name

        self.setStyleSheet("""
            background-color: black;
            color: white;
            font-size: 10px; 
            font-weight: bold; 
            qproperty-alignment: AlignCenter;
        """)

        # Инициализация атрибутов, связанных с перемещением
        self.__mousePressPos = None
        self.__mousePressWindowPos = None
        self.__mouseMovePos = None

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
        x = 0 - radius // 2  # Сдвигаем круг на половину его радиуса влево, чтобы он был посередине края
        y = (self.height() // 4) - (radius // 2)  # Позиционируем по вертикали посредине виджета

        # Рисуем круг с заданными параметрами
        painter.drawEllipse(x, y, radius, radius)

        # Вычисляем координаты для круга
        radius = 10  # Диаметр круга
        x = 0 - radius // 2  # Сдвигаем круг на половину его радиуса влево, чтобы он был посередине края
        y = (self.height() // 4) * 3 - (radius // 2)  # Позиционируем по вертикали посредине виджета

        # Рисуем круг с заданными параметрами
        painter.drawEllipse(x, y, radius, radius)

        painter.end()  # Завершаем рисование

    def mousePressEvent(self, event):
        self.__mousePressPos = event.globalPosition().toPoint()
        self.__mousePressWindowPos = self.pos()
        self.__mouseMovePos = event.globalPosition().toPoint() - self.pos()

    def mouseMoveEvent(self, event):
        global_pos = event.globalPosition().toPoint()
        diff = global_pos - self.__mouseMovePos

        self.move(diff)
        self.__mouseMovePos = global_pos - self.pos()

    def mouseReleaseEvent(self, event):
        if self.__mousePressPos is not None:
            moved = event.globalPosition().toPoint() - self.__mousePressPos
            if moved.manhattanLength() > 3:
                event.ignore()
                return

    def contextMenuEvent(self, event):
        context_menu = QMenu(self)
        delete_action = context_menu.addAction(f"Удалить {self.name}")
        action = context_menu.exec(self.mapToGlobal(event.pos()))
        if action == delete_action:
            self.delete_requested.emit(self)
            self.deleteLater()


class BlockAND(Block):
    last_square_number_AND = 0

    def __init__(self, *args, **kwargs):
        BlockAND.last_square_number_AND += 1
        name = f"AND_{BlockAND.last_square_number_AND}"
        super().__init__(*args, name=name, **kwargs)
        self.setText(name)


class BlockOR(Block):
    last_square_number_OR = 0

    def __init__(self, *args, **kwargs):
        BlockOR.last_square_number_OR += 1
        name = f"OR_{BlockOR.last_square_number_OR}"
        super().__init__(*args, name=name, **kwargs)
        self.setText(name)


class BlockIN(Block):
    last_square_number_IN = 0

    def __init__(self, *args, x=300, y=300, width=50, height=25, **kwargs):
        BlockIN.last_square_number_IN += 1
        name = f"IN_{BlockIN.last_square_number_IN}"
        super().__init__(*args, x=x, y=y, width=width, height=height, name=name, **kwargs)
        self.setText(name)
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
        self.blocks = []

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
        self.count_button.clicked.connect(self.update_counts)

        self.count_label_and = QLabel("AND: 0")
        self.layout.addWidget(self.count_label_and)

        self.count_label_or = QLabel("OR: 0")
        self.layout.addWidget(self.count_label_or)

        self.count_label_in = QLabel("IN: 0")
        self.layout.addWidget(self.count_label_in)

    def create_block_and(self):
        block = BlockAND(self.central_widget)
        block.show()
        self.blocks.append(block)
        block.delete_requested.connect(self.remove_block)  # Создаем слот, который будет вызываться при удалении блока

    def create_block_or(self):
        block = BlockOR(self.central_widget)
        block.show()
        self.blocks.append(block)
        block.delete_requested.connect(self.remove_block)  # Создаем слот, который будет вызываться при удалении блока

    def create_block_in(self):
        block = BlockIN(self.central_widget)
        block.show()
        self.blocks.append(block)
        block.delete_requested.connect(self.remove_block)  # Создаем слот, который будет вызываться при удалении блока

    def remove_block(self, block):
        if block in self.blocks:
            self.blocks.remove(block)
        self.update_counts()

    def update_counts(self):
        and_count = sum(1 for block in self.blocks if isinstance(block, BlockAND))
        or_count = sum(1 for block in self.blocks if isinstance(block, BlockOR))
        in_count = sum(1 for block in self.blocks if isinstance(block, BlockIN))

        self.count_label_and.setText(f"AND: {and_count}")
        self.count_label_or.setText(f"OR: {or_count}")
        self.count_label_in.setText(f"IN: {in_count}")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = MainWindow()
    window.setGeometry(100, 100, 600, 600)
    window.show()
    sys.exit(app.exec())
