import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import random

class CircleDrawer(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.button = self.findChild(QPushButton, 'pushButton')
        self.button.clicked.connect(self.draw_circle)
        self.show()

    def draw_circle(self):
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setBrush(QColor(255, 255, 0))  # Yellow color
        diameter = random.randint(10, 100)
        painter.drawEllipse(random.randint(0, self.width() - diameter),
                            random.randint(0, self.height() - diameter),
                            diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    sys.exit(app.exec_())
