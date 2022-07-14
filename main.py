from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from gui.main_window import MainWindow

import sys
import os


if __name__ == '__main__':

    app = QApplication(sys.argv)  # We define the application
    app.setStyle('Fusion')

    window = MainWindow()
    window.show()  # show the window

    # start loop
    sys.exit(app.exec())
