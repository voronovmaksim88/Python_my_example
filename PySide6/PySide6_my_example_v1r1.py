from PySide6 import QtWidgets, QtCore

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.counter = 0

        self.label = QtWidgets.QLabel(str(self.counter))
        self.button_inc = QtWidgets.QPushButton('Increase')
        self.button_dec = QtWidgets.QPushButton('Decrease')

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button_inc)
        self.layout.addWidget(self.button_dec)

        self.button_inc.clicked.connect(self.increase)
        self.button_dec.clicked.connect(self.decrease)

    @QtCore.Slot()
    def increase(self):
        self.counter += 1
        self.label.setText(str(self.counter))

    @QtCore.Slot()
    def decrease(self):
        self.counter -= 1
        self.label.setText(str(self.counter))

app = QtWidgets.QApplication([])
win = MyWindow()
win.show()
app.exec_()