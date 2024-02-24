#!/usr/bin/python3
# -*- coding: utf-8 -*-
# https://pythonworld.ru/gui/pyqt5-firstprograms.html

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('SibPLC')
    w.show()

    sys.exit(app.exec_())
